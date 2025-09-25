"""
Test module for the landfire module of the duet_tools package.
"""

from __future__ import annotations

import pytest
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import geojson
from unittest.mock import patch
from shutil import copyfile
import landfire

from duet_tools.calibration import Targets
from duet_tools.landfire import LandfireQuery, query_landfire, assign_targets_from_sb40

TEST_DIR = Path(__file__).parent
TMP_DIR = TEST_DIR / "tmp"
TMP_DIR.mkdir(exist_ok=True)
DATA_DIR = TEST_DIR / "test-data"


class TestLandfireTargets:
    """
    NOTICE:
    As of 9/19/25, requesting data through the landfire-python package no longer works.
    Until the landfire-python package updates its request_data function to accommodate changes
    in the LANDFIRE API, that function has been mocked out of all tests. Users should not expect
    query_landfire to work normally until this is resolved.
    """

    @classmethod
    def get_geojson(self):
        with open(DATA_DIR / "anderson_butte.geojson") as fid:
            sample_geojson = geojson.load(fid)
        return geojson.Polygon(sample_geojson["features"][0]["geometry"]["coordinates"])

    @staticmethod
    def fake_request_data(self, *args, **kwargs):
        """Fake method to replace Landfire.request_data."""
        test_zip = DATA_DIR / "landfire_test_data.zip"
        target_zip = TMP_DIR / "landfire_sb40.zip"
        copyfile(test_zip, target_zip)
        return target_zip

    def test_query_landfire(self):
        sample_aoi = self.get_geojson()
        with patch.object(
            landfire.Landfire, "request_data", new=self.fake_request_data
        ):
            query = query_landfire(
                area_of_interest=sample_aoi,
                year=2019,
                directory=TMP_DIR,
                input_epsg=4326,
            )
        assert isinstance(query, LandfireQuery)
        assert isinstance(query.fuel_types, np.ndarray)
        assert isinstance(query.loading, np.ndarray)
        assert isinstance(query.moisture, np.ndarray)
        assert isinstance(query.depth, np.ndarray)

    def test_query_landfire_years(self):
        sample_aoi = self.get_geojson()
        # Query for 2019 is above. Test 2020...
        with patch.object(
            landfire.Landfire, "request_data", new=self.fake_request_data
        ):
            query = query_landfire(
                area_of_interest=sample_aoi,
                year=2020,
                directory=TMP_DIR,
                input_epsg=4326,
            )
        # ...and 2022
        with patch.object(
            landfire.Landfire, "request_data", new=self.fake_request_data
        ):
            query = query_landfire(
                area_of_interest=sample_aoi,
                year=2022,
                directory=TMP_DIR,
                input_epsg=4326,
            )
        # make sure no other years work
        with pytest.raises(ValueError):
            with patch.object(
                landfire.Landfire, "request_data", new=self.fake_request_data
            ):
                query_landfire(
                    area_of_interest=sample_aoi,
                    year=2025,
                    directory=TMP_DIR,
                    input_epsg=4326,
                )

    def test_assign_targets_from_sb40(self):
        sample_aoi = self.get_geojson()
        with patch.object(
            landfire.Landfire, "request_data", new=self.fake_request_data
        ):
            query = query_landfire(
                area_of_interest=sample_aoi,
                year=2019,
                directory=TMP_DIR,
                input_epsg=4326,
            )
        # test just grass loading
        grass_loading = assign_targets_from_sb40(query, "grass", "loading")
        assert isinstance(grass_loading, Targets)
        assert grass_loading.method == "maxmin"
        assert grass_loading.args == ["max", "min"]
        assert len(grass_loading.targets) == 2
        # test fuel and parameter with only one value
        with pytest.warns(UserWarning):
            grass_moisture = assign_targets_from_sb40(query, "grass", "moisture")
        grass_moisture = assign_targets_from_sb40(
            query, "grass", "moisture", method="constant"
        )
        # get the rest of the fuels and params with maxmin
        grass_depth = assign_targets_from_sb40(query, "grass", "depth")
        litter_loading = assign_targets_from_sb40(query, "litter", "loading")
        litter_moisture = assign_targets_from_sb40(query, "litter", "loading")
        litter_depth = assign_targets_from_sb40(query, "litter", "loading")
        all_loading = assign_targets_from_sb40(query, "all", "loading")
        all_moisture = assign_targets_from_sb40(query, "all", "moisture")
        all_depth = assign_targets_from_sb40(query, "all", "depth")
        # test a couple with meansd
        grass_loading_meansd = assign_targets_from_sb40(
            query, "grass", "loading", method="meansd"
        )
        all_depth = assign_targets_from_sb40(query, "all", "depth", "meansd")
        # test wrong inputs
        with pytest.raises(ValueError):
            grass_depth = assign_targets_from_sb40(query, "both", "depth")
        with pytest.raises(ValueError):
            grass_depth = assign_targets_from_sb40(query, "all", "moist")
        with pytest.raises(ValueError):
            grass_depth = assign_targets_from_sb40(
                query, "all", "depth", method="minmax"
            )


def plot_array(x, title):
    plt.figure(2)
    plt.set_cmap("viridis")
    plt.imshow(x, origin="lower")
    plt.colorbar()
    plt.title(title, fontsize=18)
    plt.show()
