"""
DUET inputs module
"""

from __future__ import annotations

# Core Imports
from pathlib import Path
from random import randint


class InputFile:
    """
    Class representing a DUET input file.

    Attributes
    ----------
    nx: int
        Number of cells in the x-direction.
    ny: int
        Number of cells in the y-direction.
    nz: int
        Number of cells in the z-direction.
    dx: float
        Cell size in the x-direction (m)
    dy: float
        Cell size in the y-direction (m)
    dz: float
        Cell size in the z-direction (m)
    random_seed: int
        Random number seed.
    wind_direction: float
        Wind direction (degrees).
    wind_variability: float
        Wind direction variability (degrees).
    duration:
        Duration of simulation (years).
    """

    def __init__(
        self,
        nx: int,
        ny: int,
        nz: int,
        dx: float,
        dy: float,
        dz: float,
        random_seed: int,
        wind_direction: float,
        wind_variability: float,
        duration: int,
    ):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.random_seed = random_seed
        self.wind_direction = wind_direction
        self.wind_variability = wind_variability
        self.duration = duration

    @classmethod
    def create(
        cls,
        nx: int,
        ny: int,
        nz: int,
        duration: int,
        wind_direction: float,
        dx: float = 2.0,
        dy: float = 2.0,
        dz: float = 1.0,
        random_seed: int = None,
        wind_variability: float = 359.0,
    ):
        if random_seed is None:
            random_seed = randint(1, 50000)
        return cls(
            nx,
            ny,
            nz,
            dx,
            dy,
            dz,
            random_seed,
            wind_direction,
            wind_variability,
            duration,
        )

    def to_file(self, directory: Path | str):
        """
        Writes a DUET input file to the specified path

        Parameters
        ----------
        directory: Path | str
            Directory for writing DUET input file

        Returns
        -------
        None:
            Writes duet.in to directory
        """
        if isinstance(directory, str):
            directory = Path(directory)
        self._validate()

        out_path = directory / "duet.in"
        with open(out_path, "w") as f:
            f.write(f"{self.nx}  ! number of cells in x direction\n")
            f.write(f"{self.ny}  ! number of cells in y direction\n")
            f.write(f"{self.nz}  ! number of cells in z direction\n")
            f.write(f"{self.dx}  ! cell size in x direction (in meters)\n")
            f.write(f"{self.dy}  ! cell size in y direction (in meters)\n")
            f.write(f"{self.dz}  ! cell size in z direction (in meters)\n")
            f.write(f"{self.random_seed}  ! random number seed\n")
            f.write(f"{self.wind_direction}  ! wind direction (in degrees)\n")
            f.write(
                f"{self.wind_variability}  ! wind direction variability (in degrees)\n"
            )
            f.write(f"{self.duration}  ! duration of simulation (in years)\n")

    @classmethod
    def from_directory(cls, dir: Path | str):
        """
        Creates an instance of class InputFile from a directory with a DUET input deck

        Parameters
        ----------

        dir: Path | str
            Path to the directory containing the DUET input deck.

        Returns
        -------
        InputFile
        """
        if isinstance(dir, str):
            dir = Path(dir)

        with open(dir / "duet.in") as f:
            lines = f.readlines()

        return cls(
            nx=int(lines[0].strip().split("!")[0]),
            ny=int(lines[1].strip().split("!")[0]),
            nz=int(lines[2].strip().split("!")[0]),
            dx=float(lines[3].strip().split("!")[0]),
            dy=float(lines[4].strip().split("!")[0]),
            dz=float(lines[5].strip().split("!")[0]),
            random_seed=int(lines[6].strip().split("!")[0]),
            wind_direction=float(lines[7].strip().split("!")[0]),
            wind_variability=float(lines[8].strip().split("!")[0]),
            duration=int(lines[9].strip().split("!")[0]),
        )

    def _validate(self):
        int_list = [self.nx, self.ny, self.nz, self.random_seed, self.duration]
        float_list = [
            self.dx,
            self.dy,
            self.dz,
            self.wind_direction,
            self.wind_variability,
        ]
        deg_list = [self.wind_direction, self.wind_variability]
        for attr in int_list:
            if not isinstance(attr, int):
                raise ValueError(f"{attr} must be of type int")
        for attr in float_list:
            if not isinstance(attr, float):
                if not isinstance(attr, int):
                    raise ValueError(f"{attr} must be of type float or int")
        for attr in deg_list:
            if not 0 <= self.wind_direction < 360:
                raise ValueError(f"{attr} must be in range [0,360)")
        for attr in self.__dict__.values():
            if attr < 0:
                raise ValueError(f"{attr} must be positive")
