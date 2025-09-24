"""
FSSG - FACET Static Site Generator

A production-grade static site generator built on deterministic principles.
Uses FACET v1.1 as the source format and generates optimized HTML.
"""

__version__ = "1.1.0"
__author__ = "Emil Rokossovskiy"
__email__ = "ecsiar@gmail.com"

from .core import FSSSGCore
from .config import FSSSGConfig
from .renderer import HTMLRenderer

__all__ = ["FSSSGCore", "FSSSGConfig", "HTMLRenderer"]
