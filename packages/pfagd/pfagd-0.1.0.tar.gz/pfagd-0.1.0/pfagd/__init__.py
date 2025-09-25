"""
PFAGD - Python for Android Game Development
A comprehensive cross-platform game development framework for Python

Author: PFAGD Team
Version: 0.1.0
License: MIT
"""

from .engine.core import Game, Scene
from .engine.renderer import Renderer
from .assets.manager import AssetManager
from .ui.widgets import Button, Label

__version__ = "0.1.0"
__author__ = "PFAGD Team"
__license__ = "MIT"

# Main API exports
__all__ = [
    "Game",
    "Scene", 
    "Renderer",
    "AssetManager",
    "Button",
    "Label"
]