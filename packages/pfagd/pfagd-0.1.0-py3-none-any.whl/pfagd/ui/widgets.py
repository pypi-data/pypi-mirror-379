"""
PFAGD UI Widgets
Basic UI components for games
"""

from typing import Callable, Optional, Tuple
from abc import ABC, abstractmethod

try:
    from kivy.uix.button import Button as KivyButton
    from kivy.uix.label import Label as KivyLabel
    KIVY_AVAILABLE = True
except ImportError:
    KIVY_AVAILABLE = False


class Widget(ABC):
    """Base widget class"""
    
    def __init__(self, pos: Tuple[int, int] = (0, 0), size: Tuple[int, int] = (100, 50)):
        self.pos = pos
        self.size = size
        self.visible = True
        self.enabled = True
    
    @abstractmethod
    def render(self, renderer):
        """Render the widget"""
        pass
    
    def handle_event(self, event):
        """Handle input events"""
        pass


class Button(Widget):
    """Button widget for user interaction"""
    
    def __init__(self, text: str = "Button", on_press: Optional[Callable] = None,
                 pos: Tuple[int, int] = (0, 0), size: Tuple[int, int] = (100, 50)):
        super().__init__(pos, size)
        self.text = text
        self.on_press = on_press
        self.pressed = False
        
        # Create Kivy button if available
        if KIVY_AVAILABLE:
            self.kivy_button = KivyButton(
                text=text,
                pos=pos,
                size=size
            )
            if on_press:
                self.kivy_button.bind(on_press=lambda x: on_press())
    
    def render(self, renderer):
        """Render the button"""
        if not self.visible:
            return
        
        # Simple button rendering
        # In a real implementation, this would draw button graphics
        renderer.draw_text(self.text, self.pos)
    
    def handle_event(self, event):
        """Handle button click events"""
        if not self.enabled or not self.visible:
            return
        
        # Simple click detection (needs proper event system)
        if hasattr(event, 'pos'):
            x, y = event.pos
            if (self.pos[0] <= x <= self.pos[0] + self.size[0] and
                self.pos[1] <= y <= self.pos[1] + self.size[1]):
                if self.on_press:
                    self.on_press()


class Label(Widget):
    """Text label widget"""
    
    def __init__(self, text: str = "Label", pos: Tuple[int, int] = (0, 0),
                 size: Tuple[int, int] = (100, 30), color: Tuple[float, float, float, float] = (1, 1, 1, 1)):
        super().__init__(pos, size)
        self.text = text
        self.color = color
        
        # Create Kivy label if available
        if KIVY_AVAILABLE:
            self.kivy_label = KivyLabel(
                text=text,
                pos=pos,
                size=size
            )
    
    def render(self, renderer):
        """Render the label"""
        if not self.visible:
            return
        
        renderer.draw_text(self.text, self.pos, self.color)
    
    def set_text(self, text: str):
        """Update label text"""
        self.text = text
        if KIVY_AVAILABLE and hasattr(self, 'kivy_label'):
            self.kivy_label.text = text


class Menu(Widget):
    """Menu container for organizing buttons"""
    
    def __init__(self, buttons: list = None, pos: Tuple[int, int] = (0, 0),
                 spacing: int = 10):
        super().__init__(pos, (200, 300))  # Default menu size
        self.buttons = buttons or []
        self.spacing = spacing
        self._layout_buttons()
    
    def _layout_buttons(self):
        """Arrange buttons vertically"""
        current_y = self.pos[1]
        for button in self.buttons:
            button.pos = (self.pos[0], current_y)
            current_y += button.size[1] + self.spacing
    
    def render(self, renderer):
        """Render all buttons in the menu"""
        if not self.visible:
            return
        
        for button in self.buttons:
            button.render(renderer)
    
    def handle_event(self, event):
        """Pass events to buttons"""
        for button in self.buttons:
            button.handle_event(event)
    
    def add_button(self, button: Button):
        """Add a button to the menu"""
        self.buttons.append(button)
        self._layout_buttons()


class Slider(Widget):
    """Slider widget for value selection"""
    
    def __init__(self, min_val: float = 0, max_val: float = 100, value: float = 50,
                 pos: Tuple[int, int] = (0, 0), size: Tuple[int, int] = (200, 20)):
        super().__init__(pos, size)
        self.min_val = min_val
        self.max_val = max_val
        self.value = value
        self.dragging = False
        self.on_value_change = None
    
    def render(self, renderer):
        """Render the slider"""
        if not self.visible:
            return
        
        # Draw slider track
        # Draw slider handle
        # This is a simplified implementation
        progress = (self.value - self.min_val) / (self.max_val - self.min_val)
        handle_pos = (
            self.pos[0] + int(progress * self.size[0]),
            self.pos[1]
        )
        
        renderer.draw_text(f"Slider: {self.value:.1f}", self.pos)
    
    def set_value(self, value: float):
        """Set slider value"""
        self.value = max(self.min_val, min(self.max_val, value))
        if self.on_value_change:
            self.on_value_change(self.value)