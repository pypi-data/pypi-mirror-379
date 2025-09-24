"""
travelpy: Python wrapper for TRAVEL particle tracking simulations

A modern Python interface to the TRAVEL particle tracking code.
"""

__version__ = "0.1.0"

# Public API imports
from travelpy.beam.beam import Beam
from travelpy.beam.conversion import dat2dst, dat2txt, dst2dat, dst2txt, txt2dat
from travelpy.beamline import Beamline
from travelpy.config.paths import get_travel_directory, set_travel_directory
from travelpy.results.parsers import AvgOut, Deadray, RmsOut
from travelpy.simulation.runner import run_travel

__all__ = [
    "run_travel",
    "set_travel_directory",
    "get_travel_directory",
    "Beam",
    "Beamline",
    "AvgOut",
    "RmsOut",
    "Deadray",
    "dat2txt",
    "dat2dst",
    "dst2dat",
    "dst2txt",
    "txt2dat",
]
