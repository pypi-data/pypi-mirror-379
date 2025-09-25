"""
Utility functions for DUET tools modules
"""

from __future__ import annotations

import geojson
import numpy as np
from pathlib import Path
from scipy.io import FortranFile
import shapefile  # pyshp
import io
import zipfile


def read_dat_to_array(
    directory: str | Path,
    filename: str,
    nx: int,
    ny: int,
    nz: int = None,
    nsp: int = None,
    order: str = "F",
    dtype: type = np.float32,
) -> np.ndarray:
    """
    Reads a fortran binary file (.dat) to a numpy array

    Parameters
    ----------
    directory: Path | str
        Path to directory of the .dat file.
    filename: str
        Name of the .dat file
    nx : int
        Number of cells in the x-direction
    ny : int
        Number of cells in the y-direction
    nz : int
        Number of cells in the z-direction
    nsp: int
        Number of species
    order : str
        Order of the .dat file. Must be one of "C" or "F". Defaults to "F".
    dtype : type
        Data type of the array. Defaults to np.float32

    Returns
    -------
        A numpy array with shape (nz, ny, nx).
    """
    if order not in ["C", "F"]:
        raise ValueError('Order must be either "C" or "F".')
    if isinstance(directory, str):
        directory = Path(directory)

    if (nz is None) and (nsp is None):
        shape = (nx, ny)
    elif nz is None:
        shape = (nsp, nx, ny)
    elif nsp is None:
        shape = (nx, ny, nz)
    else:
        shape = (nsp, nx, ny, nz)

    with open(Path(directory, filename), "rb") as fin:
        array = FortranFile(fin).read_reals(dtype=dtype).reshape(shape, order=order)

    if (nz is None) and (nsp is None):
        return np.moveaxis(array, 1, 0)
    elif nz is None:
        return np.moveaxis(array, 2, 1)
    elif nsp is None:
        return np.transpose(array)
    else:
        return np.moveaxis(np.moveaxis(array, 3, 1), 3, 1)


def write_array_to_dat(
    array: np.ndarray,
    dat_name: str,
    output_dir: Path | str,
    dtype: type = np.float32,
    reshape: bool = False,
) -> None:
    """
    Write a numpy array to a fortran binary file (.dat).

    Parameters
    ----------
    array : np.ndarray
        numpy array to be written to a file
    dat_name : str
        Filename ending with .dat
    output_dir : Path | str
        Directory where file will be written
    dtype : type
        Data type of the array. Defaults to np.float32
    reshape: bool
        Whether to reshape the array. Array dimensions in duet-tools are either (nz,ny,nx)
        or (nsp,ny,nx) and will be written in row-major order, meaning that with column-major
        order (default for fortran), they will be (nx, ny, nz). Reshaping (nsp, ny, nx) arrays
        to (ny, nx, nsp) will result in the column-major order of (nsp, nx, ny), which is
        expected by DUET and LANL Trees. If True, reshaping will only be applied to 3D arrays.
        Defaults to False.
    """
    if isinstance(output_dir, str):
        output_dir = Path(output_dir)
    # Reshape array from (nsp, ny, nx) to (ny, nx, nsp)
    if reshape:
        if len(array.shape) == 3:
            array = np.moveaxis(array, 0, 2).astype(dtype)
        else:
            array = array.astype(dtype)
    else:
        array = array.astype(dtype)

    # Written in row-major order
    with FortranFile(Path(output_dir, dat_name), "w") as f:
        f.write_record(array)


def read_shapefile_to_geojson(path: Path) -> geojson.Polygon:
    """
    Read a shapefile and convert to a geojson polygon. May be used to
    query LANDFIRE data. Assumes the shapefile has Polygon geometry.
    Only the first feature is converted to a geojson.

    Parameters
    ----------
    path : str
        Path to shapefile. File may be compressed (.zip), or uncompressed (.shp)
        with constituent files in the same directory.

    Returns
    -------
    A geojson Polygon object.
    """
    if path.suffix == ".zip":
        with zipfile.ZipFile(path, "r") as zip_ref:
            # Extract shapefile components to memory
            shp_name = next(
                (name for name in zip_ref.namelist() if name.endswith(".shp")), None
            )
            shx_name = next(
                (name for name in zip_ref.namelist() if name.endswith(".shx")), None
            )
            dbf_name = next(
                (name for name in zip_ref.namelist() if name.endswith(".dbf")), None
            )

            if not (shp_name and shx_name and dbf_name):
                raise FileNotFoundError("Zip must contain .shp, .shx, and .dbf files.")

            # Read each file into BytesIO
            shp_io = io.BytesIO(zip_ref.read(shp_name))
            shx_io = io.BytesIO(zip_ref.read(shx_name))
            dbf_io = io.BytesIO(zip_ref.read(dbf_name))

            reader = shapefile.Reader(shp=shp_io, shx=shx_io, dbf=dbf_io)
    else:
        if not path.exists():
            raise FileNotFoundError(f"Shapefile not found: {path}")
        reader = shapefile.Reader(str(path))

    shape = reader.shape(0)
    if shape.shapeType != shapefile.POLYGON:
        raise ValueError("Shapefile does not contain a polygon.")

    coords = shape.points
    parts = list(shape.parts) + [len(coords)]
    rings = [coords[parts[i] : parts[i + 1]] for i in range(len(parts) - 1)]
    polygon = geojson.Polygon([ring for ring in rings])

    reader.close()
    return polygon
