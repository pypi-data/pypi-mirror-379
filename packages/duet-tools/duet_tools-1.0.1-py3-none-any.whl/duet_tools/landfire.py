"""
Functions for interfacing with the LandFire API and processing the outputs
"""

# Core imports
from pathlib import Path
import importlib.resources
import re
import warnings
import zipfile

# External imports
import numpy as np
import pandas as pd
import geojson
import shapely
from pyproj import Transformer
import landfire
from landfire.geospatial import get_bbox_from_polygon
import rasterio as rio

# Internal imports
from duet_tools.calibration import Targets

try:  # Python 3.9+
    DATA_PATH = importlib.resources.files("duet_tools").joinpath("data")
except AttributeError:  # Python 3.6-3.8
    from pkg_resources import resource_filename

    DATA_PATH = resource_filename("duet_tools", "data")


class LandfireQuery:
    """
    Class containing the information from a LandFire query, to be passed to assign_targets()
    """

    def __init__(
        self,
        fuel_types: np.ndarray,
        loading: np.ndarray,
        moisture: np.ndarray,
        depth: np.ndarray,
    ):
        self.fuel_types = fuel_types
        self.loading = loading
        self.moisture = moisture
        self.depth = depth
        self._validate_arrays_shape()

    def _get_fueltype_indices(self, arr: np.ndarray, ft: int):
        ft_dict = {1: "grass", -1: "litter"}
        if ft not in arr.flatten():
            raise ValueError(f"Landfire query does not contain any {ft_dict[ft]} fuel.")
        return np.where(arr == ft)

    def _validate_arrays_shape(self):
        attributes = [
            getattr(self, attr)
            for attr in dir(self)
            if not callable(getattr(self, attr)) and not attr.startswith("__")
        ]
        first_shape = None
        for arr in attributes:
            if isinstance(arr, np.ndarray):
                if first_shape is None:
                    first_shape = arr.shape
                elif arr.shape != first_shape:
                    raise ValueError(
                        "All arrays in LandfireQuery must have the same shape."
                    )

    def _validate_get_targets(self, fuel_type, parameter, method):
        fueltypes_allowed = ["grass", "litter", "all"]
        parameters_alowed = ["loading", "moisture", "depth"]
        methods_allowed = ["maxmin", "meansd", "constant"]

        if fuel_type not in fueltypes_allowed:
            raise ValueError(
                f"Fuel type {fuel_type} not supported. Must be one of {fueltypes_allowed}."
            )
        if parameter not in parameters_alowed:
            raise ValueError(
                f"Parameter {parameter} not supported. Must be one of {parameters_alowed}."
            )
        if method not in methods_allowed:
            raise ValueError(
                f"Method {method} not supported. Must be one of {methods_allowed}."
            )


def query_landfire(
    area_of_interest: geojson.Polygon | shapely.Polygon,
    year: str,
    directory: str | Path,
    input_epsg: int,
    delete_files: bool = True,
) -> LandfireQuery:
    """
    Creates and submits a LANDFIRE query for a specified area of interest.

    Parameters
    ----------
    area_of_interest : geojson.Polygon | shapely.Polygon
        Area in which to query LANDFIRE data. For best results, dimensions in meters should
        match (nx*dx, ny*dy) of DUET domain.
    year : int
        Year of LANDFIRE data to query. Must be one of [2019, 2020, 2022].
    directory : Path | str
        Directory where files associated with the LANDFIRE query will be saved.
    input_epsg : int
        EPSG number for CRS of area_of_interest polygon
    delete_files : bool = True
        Whether to delete intermediate files created in the process of querying LANDFIRE data. Defaults to True

    Returns
    -------
    LandfireQuery
    """
    if isinstance(directory, str):
        directory = Path(directory)

    if isinstance(area_of_interest, geojson.Polygon):
        area_of_interest = shapely.Polygon(area_of_interest["coordinates"][0])

    valid_years = [2019, 2020, 2022]
    if year not in valid_years:
        raise ValueError(
            f"SB40 data for year {year} not available. Must be one of {valid_years}"
        )

    if input_epsg != 4236:
        area_of_interest = _reproject_polygon(
            area_of_interest, input_epsg, target_epsg=4326
        )

    _query_landfire(poly=area_of_interest, year=year, directory=directory)
    landfire_arr = _landfire_to_array(directory)

    # Import SB40 FBFM parameters table
    sb40_params_path = DATA_PATH / "sb40_parameters.csv"
    sb40_params = pd.read_csv(sb40_params_path)

    # Generate dict of fastfuels bulk density values and apply to Landfire query
    sb40_dict = _get_sb40_fuel_params(sb40_params)
    sb40_arr = _get_sb40_arrays(landfire_arr, sb40_dict)

    if delete_files:
        _delete_intermediate_files(directory)

    return LandfireQuery(
        fuel_types=sb40_arr[0, :, :],
        loading=sb40_arr[1, :, :],
        moisture=sb40_arr[2, :, :],
        depth=sb40_arr[3, :, :],
    )


def assign_targets_from_sb40(
    query: LandfireQuery, fuel_type: str, parameter: str, method: str = "maxmin"
) -> Targets:
    """
    Assign a calibration target and method for a given fuel type and parameter.

    Parameters
    ----------
    query : LandfireQuery
        An object of class LandfireQuery created with query_landfire. Calibration targets
        will be calculated from these values.
    fuel_type : str
        The fuel type to obtain target values for. Must be one of "grass", "litter", or "all".
    parameter : str
        The fuel parameter to obtain target values for. Must be one of "loading", "moisture", or "depth".
    method : str
        The desired calibration method for the sb40-derived targets. Must be one of "maxmin", "meandsd",
        or "constant". Default is "maxmin". "constant" is only recommended if only one parameter value
        is present for the given fuel type. "meansd" is not recommended since values often do not follow a
        normal distribution.

    Returns
    -------
    Targets :
        A Targets object with values derived from Landfire and SB40 fuel models
    """
    query._validate_get_targets(fuel_type, parameter, method)
    # select fuel parameter
    if parameter == "loading":
        param_arr = query.loading
    elif parameter == "moisture":
        param_arr = query.moisture
    else:
        param_arr = query.depth
    # select fuel type
    if fuel_type == "grass":
        fuel_arr = param_arr[query._get_fueltype_indices(query.fuel_types, 1)]
    elif fuel_type == "litter":
        fuel_arr = param_arr[query._get_fueltype_indices(query.fuel_types, -1)]
    else:
        fuel_arr = param_arr
    # get targets based on method
    fuel_arr = fuel_arr[np.where(fuel_arr > 0)]
    if method == "maxmin":
        if np.max(fuel_arr) == np.min(fuel_arr):
            warnings.warn(
                f"There is only one value for {fuel_type} {parameter}. "
                "Setting calibration method to 'constant'",
                UserWarning,
            )
            method = "constant"
            args = ["value"]
            targets = [np.mean(fuel_arr)]
        else:
            method = "maxmin"
            args = ["max", "min"]
            targets = [np.max(fuel_arr), np.min(fuel_arr)]
        return Targets(
            method=method,
            args=args,
            targets=targets,
        )
    if method == "meansd":
        if np.max(fuel_arr) == np.min(fuel_arr):
            warnings.warn(
                f"There is only one value for {fuel_type} {parameter}. "
                "Setting calibration method to 'constant'",
                UserWarning,
            )
            method = "constant"
            args = ["value"]
            targets = [np.mean(fuel_arr)]
        else:
            method = "meansd"
            args = ["mean", "sd"]
            targets = [np.mean(fuel_arr), np.std(fuel_arr)]
        return Targets(
            method=method,
            args=args,
            targets=targets,
        )
    if method == "constant":
        if np.max(fuel_arr) != np.min(fuel_arr):
            raise ValueError(
                "Multiple values present in Landfire query. Please use either maxmin "
                "or meansd calibration method."
            )
        return Targets(method="constant", args=["value"], targets=[np.mean(fuel_arr)])


def _query_landfire(
    poly: shapely.Polygon,
    year: int,
    directory: Path,
) -> None:
    """
    Download a grid of SB40 fuel models from Landfire for the unit and convert to a numpy array
    """

    if year == 2019:
        layer = ["200F40_19"]
    if year == 2020:
        layer = ["200F40_20"]
    if year == 2022:
        layer = ["220F40_22"]

    bbox = get_bbox_from_polygon(aoi_polygon=poly, crs=4326)

    # Download Landfire data to output directory
    lf = landfire.Landfire(bbox, output_crs="5070")
    lf.request_data(layers=layer, output_path=Path(directory, "landfire_sb40.zip"))

    # Exctract tif from compressed download folder and rename
    with zipfile.ZipFile(Path(directory, "landfire_sb40.zip")) as zf:
        extension = ".tif"
        rename = "landfire_sb40.tif"
        info = zf.infolist()
        for file in info:
            if file.filename.endswith(extension):
                file.filename = rename
                zf.extract(file, directory)


def _landfire_to_array(
    directory: Path,
) -> np.ndarray:
    # Upsample landfire raster to the quicfire resolution
    with rio.open(Path(directory, "landfire_sb40.tif")) as sb:
        arr = sb.read(1)

    return arr


def _get_sb40_fuel_params(params: pd.DataFrame) -> dict:
    """
    Builds a dictionary of SB40 fuel parameter values and converts them to
    the official FastFuels units

    Returns:
        dict: SB40 parameters for each fuel model
    """

    # Convert tons/ac-ft to kg/m^3
    params["1_hr_kg_per_m3"] = params["1_hr_t_per_ac"] * 0.22417
    params["10_hr_kg_per_m3"] = params["10_hr_t_per_ac"] * 0.22417
    params["100_hr_kg_per_m3"] = params["100_hr_t_per_ac"] * 0.22417
    params["live_herb_kg_per_m3"] = params["live_herb_t_per_ac"] * 0.22417
    params["live_woody_kg_per_m3"] = params["live_woody_t_per_ac"] * 0.22417

    # Convert inverse feet to meters
    params["dead_1_hr_sav_ratio_1_per_m"] = (
        params["dead_1_hr_sav_ratio_1_per_ft"] * 3.2808
    )
    params["live_herb_sav_ratio_1_per_m"] = (
        params["live_herb_sav_ratio_1_per_ft"] * 3.2808
    )
    params["live_wood_sav_ratio_1_per_m"] = (
        params["live_wood_sav_ratio_1_per_ft"] * 3.2808
    )

    # Convert percent to ratio
    params["dead_fuel_extinction_moisture"] /= 100

    # Convert feet to meters
    params["fuel_bed_depth_m"] = params["fuel_bed_depth_ft"] * 0.3048

    # Compute wet loading
    params["wet_load"] = params["1_hr_kg_per_m3"] + params["live_herb_kg_per_m3"]

    # Compute a live herb curing factor alpha as a function of wet loading.
    # This is kind of a B.S. approach raised by Rod on a phone call with
    # Anthony on 02/28/2023. I don't like this at all, but it is a temporary
    # Fix for the BP3D team to run some simulations.
    # low_load_fuel_models = [
    params["alpha"] = [0.5 if rho > 1 else 1.0 for rho in params["wet_load"]]

    # Compute dry loading
    params["dry_herb_load"] = params["live_herb_kg_per_m3"] * params["alpha"]
    params["dry_load"] = params["1_hr_kg_per_m3"] + params["dry_herb_load"]

    # Compute SAV
    params["sav_1hr_ratio"] = params["1_hr_kg_per_m3"] / params["dry_load"]
    params["sav_1hr"] = params["sav_1hr_ratio"] * params["dead_1_hr_sav_ratio_1_per_m"]
    params["sav_herb_ratio"] = params["dry_herb_load"] / params["dry_load"]
    params["sav_herb"] = (
        params["sav_herb_ratio"] * params["live_herb_sav_ratio_1_per_m"]
    )
    params["sav"] = params["sav_1hr"] + params["sav_herb"]

    # Convert nan to 0
    params.fillna(0, inplace=True)

    # Create dictionary for assigning fuel types for DUET calibration
    duet_dict = {
        "NB": 0,  # 0 = NEUTRAL, i.e. not predominantly grass or litter
        "GR": 1,  # 1 = GRASS predominantly
        "GS": 1,
        "SH": 1,  # I am considering shrubs as grass
        "TU": 0,
        "TL": -1,  # -1 = LITTER predominantly
        "SB": 0,
    }

    # Add column to df with DUET designations
    pattern = r"[0-9]"  # take out numbers from fbfm_type strings
    params["fbfm_cat"] = params["fbfm_code"].apply(lambda x: re.sub(pattern, "", x))
    params["duet_fuel_type"] = params["fbfm_cat"].apply(lambda x: duet_dict.get(x))

    # Build the dictionary with fuel parameters for the Scott and Burgan 40
    # fire behavior fuel models. Dict format: key ->
    # [name, loading (tons/ac), SAV (1/ft), ext. MC (percent), bed depth (ft)]
    # Note: Eventually we want to get rid of this and just use the dataframe.
    # This is legacy from the old parameter table json.
    sb40_dict = {}
    for key in params["key"]:
        row = params[params["key"] == key]
        sb40_dict[key] = [
            row["fbfm_code"].values[0],
            row["dry_load"].values[0],
            row["sav"].values[0],
            row["dead_fuel_extinction_moisture"].values[0],
            row["fuel_bed_depth_m"].values[0],
            row["duet_fuel_type"].values[0],
        ]
    sb40_dict[-9999] = ["NA", 0.0, 0.0, 0.0, 0.0, 0]

    return sb40_dict


def _get_sb40_arrays(sb40_keys: np.ndarray, sb40_dict: dict) -> np.ndarray:
    """
    Use a dictionary of fuel loading and fuel types that correspond to SB40
    fuel models to assign those values across the study area.

    Fuel types are as follows:
    - 1: Predominantly grass. All cells with a GR, GS, or SH designation from SB40.
    - -1: Predominantly tree litter. All cells with a TL designation from SB40.
    - 0: Neither predominantly grass or tree litter. All other SB40 designations.

    Returns:
    3D np.ndarray:
    4 layers:
        1. fuel types
        2. fuel loading (bulk density) values as calculated by fastfuels
        3. fuel moisture content values as calculated by fastfuels
        4. fuelbed depth values as caluclated by fastfuels
    """
    val_idx = [5, 1, 3, 4]
    fuel_arr = np.zeros((4, sb40_keys.shape[0], sb40_keys.shape[1]))
    for i in range(len(val_idx)):
        layer_dict = {key: val[val_idx[i]] for key, val in sb40_dict.items()}
        layer = np.vectorize(layer_dict.get)(sb40_keys)
        fuel_arr[i, :, :] = layer

    return fuel_arr


def _reproject_polygon(poly: shapely.Polygon, input_epsg: int, target_epsg: int):
    coords = list(poly.exterior.coords)
    transformer = Transformer.from_crs(input_epsg, target_epsg, always_xy=True)
    transformed_coords = transformer.transform(*zip(*coords))
    transformed_poly = shapely.Polygon(list(zip(*transformed_coords)))

    return transformed_poly


def _delete_intermediate_files(directory: Path):
    # Name intermediate files
    temp = [
        "landfire_sb40.zip",
        "landfire_sb40.tif",
        "sb40_upsampled.tif",
        "sb40_cropped.tif",
    ]
    [Path(directory, file).unlink() for file in temp if Path(directory, file).exists()]
