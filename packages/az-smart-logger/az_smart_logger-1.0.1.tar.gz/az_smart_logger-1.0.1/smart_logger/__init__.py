"""
Smart Logger Library
Python >=3.8
"""

__version__ = "0.1.0"

# Global dict to track active admin clients
# smart_logger/__init__.py

from .core.logger import SmartLogger
from .cli.commands import main as cli_main


__all__ = ["SmartLogger", "cli_main", "__version__"]
