"""
PFAGD Renderer Module
Cross-platform rendering abstraction layer
"""

import os
from typing import Optional, Tuple
from abc import ABC, abstractmethod

try:
    import kivy
    from kivy.graphics import *
    from kivy.graphics.instructions import *
    KIVY_AVAILABLE = True
except ImportError:
    KIVY_AVAILABLE = False


class Renderer(ABC):
    """Abstract base class for renderers"""
    
    @abstractmethod
    def clear(self, color: Tuple[float, float, float, float] = (0, 0, 0, 1)):
        """Clear the screen with given color"""
        pass
    
    @abstractmethod
    def draw_sprite(self, image_path: str, pos: Tuple[int, int], size: Tuple[int, int]):
        """Draw a sprite at given position and size"""
        pass
    
    @abstractmethod
    def draw_text(self, text: str, pos: Tuple[int, int], color: Tuple[float, float, float, float] = (1, 1, 1, 1)):
        """Draw text at given position"""
        pass
    
    @abstractmethod
    def present(self):
        """Present the rendered frame"""
        pass


class KivyRenderer(Renderer):
    """Kivy-based renderer for cross-platform rendering"""
    
    def __init__(self, canvas=None):
        self.canvas = canvas
        self.loaded_textures = {}
    
    def clear(self, color: Tuple[float, float, float, float] = (0, 0, 0, 1)):
        """Clear the screen with given color"""
        if self.canvas:
            self.canvas.clear()
            with self.canvas:
                Color(*color)
                Rectangle(size=(9999, 9999))  # Cover entire screen
    
    def draw_sprite(self, image_path: str, pos: Tuple[int, int], size: Tuple[int, int]):
        """Draw a sprite at given position and size"""
        if not self.canvas or not os.path.exists(image_path):
            return
        
        with self.canvas:
            Color(1, 1, 1, 1)  # White tint
            Rectangle(source=image_path, pos=pos, size=size)
    
    def draw_text(self, text: str, pos: Tuple[int, int], color: Tuple[float, float, float, float] = (1, 1, 1, 1)):
        """Draw text at given position"""
        if not self.canvas:
            return
        
        # Note: Kivy text rendering requires Label widget
        # This is a simplified implementation
        pass
    
    def present(self):
        """Present the rendered frame"""
        # Kivy handles presentation automatically
        pass


class ConsoleRenderer(Renderer):
    """Console-based renderer for debugging/headless mode"""
    
    def __init__(self):
        self.frame_count = 0
    
    def clear(self, color: Tuple[float, float, float, float] = (0, 0, 0, 1)):
        """Clear the screen (console output)"""
        if self.frame_count % 60 == 0:  # Print once per second at 60 FPS
            print(f"[Frame {self.frame_count}] Screen cleared with color {color}")
    
    def draw_sprite(self, image_path: str, pos: Tuple[int, int], size: Tuple[int, int]):
        """Draw a sprite (console output)"""
        if self.frame_count % 60 == 0:
            print(f"[Frame {self.frame_count}] Sprite: {image_path} at {pos}, size {size}")
    
    def draw_text(self, text: str, pos: Tuple[int, int], color: Tuple[float, float, float, float] = (1, 1, 1, 1)):
        """Draw text (console output)"""
        if self.frame_count % 60 == 0:
            print(f"[Frame {self.frame_count}] Text: '{text}' at {pos}")
    
    def present(self):
        """Present the rendered frame"""
        self.frame_count += 1


def create_renderer(backend: str = "auto", **kwargs) -> Renderer:
    """Factory function to create appropriate renderer"""
    
    if backend == "auto":
        if KIVY_AVAILABLE:
            backend = "kivy"
        else:
            backend = "console"
    
    if backend == "kivy" and KIVY_AVAILABLE:
        return KivyRenderer(**kwargs)
    elif backend == "console":
        return ConsoleRenderer()
    else:
        raise ValueError(f"Renderer backend '{backend}' not available or supported")