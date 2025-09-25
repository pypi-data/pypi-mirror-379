from __future__ import annotations

from pathlib import Path
from duet_tools import (
    InputFile,
    import_duet,
    assign_targets,
    set_fuel_parameter,
    calibrate,
)

duet_path = Path(__file__).parent.parent / "tests" / "tmp"

# Create DUET input file
input_file = InputFile.create(nx=100, ny=100, nz=30, duration=5, wind_direction=270)
input_file.to_file(duet_path)

## DUET IS RUN LOCALLY

# Import DUET outputs
duet_run = import_duet(directory=duet_path)

# Assign targets for each fuel type and fuel parameter
## method options: "maxmin", "meansd", "constant"
grass_loading = assign_targets(method="maxmin", max=1.0, min=0.1)
litter_loading = assign_targets(method="meansd", mean=0.6, sd=0.05)
grass_depth = assign_targets(method="constant", value=1.0)
coniferous_depth = assign_targets(method="constant", value=0.03)
deciduous_depth = assign_targets(method="constant", value=0.1)

# Bring together fuel types for each parameter
loading_targets = set_fuel_parameter(
    parameter="loading", grass=grass_loading, litter=litter_loading
)
depth_targets = set_fuel_parameter(
    parameter="depth",
    grass=grass_depth,
    coniferous=coniferous_depth,
    deciduous=deciduous_depth,
)

# Calibrate the DUET run
calibrated_duet = calibrate(
    duet_run=duet_run, fuel_parameter_targets=[loading_targets, depth_targets]
)

# Look at individual numpy arrays
calibrated_litter_loading = calibrated_duet.to_numpy(
    fuel_type="litter", fuel_parameter="loading"
)  # 2D array
calibrated_depth = calibrated_duet.to_numpy(
    fuel_type="separated", fuel_parameter="depth"
)  # 3D array, three layers
calibrated_loading = calibrated_duet.to_numpy(
    fuel_type="integrated", fuel_parameter="loading"
)  # 2D array

# Export to QUIC-Fire .dat files
qf_path = Path(__file__).parent.parent / "tests" / "tmp"
calibrated_duet.to_quicfire(directory=qf_path)
