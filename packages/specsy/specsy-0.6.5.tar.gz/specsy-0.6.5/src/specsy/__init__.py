"""
Specsy - A python package for the analysis of astronomical spectra
"""

import logging
import tomllib

from pathlib import Path

# Creating the lime logger
_logger = logging.getLogger("SpecSy")
_logger.setLevel(logging.INFO)

# Outputting format
consoleHandle = logging.StreamHandler()
consoleHandle.setFormatter(logging.Formatter('%(name)s %(levelname)s: %(message)s'))
_logger.addHandler(consoleHandle)

# Read lime configuration .toml
_inst_dir = Path(__file__).parent
_conf_path = _inst_dir/'config.toml'
with open(_conf_path, mode="rb") as fp:
    _setup_cfg = tomllib.load(fp)

__version__ = _setup_cfg['metadata']['version']

from .tools import flux_distribution
from .innate import Innate, load_inference_data, save_inference_data
from .treatement import SpectraSynthesizer, ChemicalModel
from .models import *
from .plotting.plots import plot_traces, plot_flux_grid, plot_corner_matrix, theme
from .io import load_cfg, load_frame