"""
Strala Core Infrastructure Package

A shared Python package containing common utilities, schemas, and services
used across Strala's claims platform applications.
"""

__version__ = "0.1.0"
__author__ = "Strala"
__email__ = "dev@strala.com"

# Import main modules for easy access
from . import schemas
from . import utils
from . import services

__all__ = [
    "schemas",
    "utils", 
    "services",
    "__version__",
]
