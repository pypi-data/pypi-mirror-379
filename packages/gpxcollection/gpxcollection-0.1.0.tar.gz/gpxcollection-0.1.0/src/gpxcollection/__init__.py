"""
GPX Collection Viewer
Generates static HTML pages with Leaflet maps for GPX file collections.
"""

from .main import GPXParser, GPXCollectionGenerator, main

__version__ = "0.1.0"
__all__ = ["GPXParser", "GPXCollectionGenerator", "main"]