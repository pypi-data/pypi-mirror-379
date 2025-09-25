"""
PFAGD Core Engine
Main game loop, scene management, and core functionality
"""

import time
import os
import threading
from typing import Dict, Optional, Any, List
from abc import ABC, abstractmethod

try:
    import kivy
    from kivy.app import App
    from kivy.clock import Clock
    from kivy.uix.widget import Widget
    KIVY_AVAILABLE = True
except ImportError:
    KIVY_AVAILABLE = False
    print("Warning: Kivy not available. Some features may be limited.")


class Scene(ABC):
    """Base class for game scenes"""
    
    def __init__(self, name: str = ""):
        self.name = name or self.__class__.__name__
        self.manager = None
        self.widgets = []
        self.sprites = []
        self.active = False
    
    def on_enter(self):
        """Called when scene becomes active"""
        self.active = True
    
    def on_exit(self):
        """Called when scene becomes inactive"""
        self.active = False
    
    def update(self, dt: float):
        """Update scene logic - called every frame"""
        pass
    
    def render(self, renderer):
        """Render scene - called every frame"""
        pass
    
    def add_widget(self, widget):
        """Add UI widget to scene"""
        self.widgets.append(widget)
        return widget
    
    def add_sprite(self, image_path: str, pos: tuple = (0, 0)):
        """Add sprite to scene"""
        sprite = Sprite(image_path, pos)
        self.sprites.append(sprite)
        return sprite
    
    def handle_event(self, event):
        """Handle input events"""
        pass


class SceneManager:
    """Manages multiple game scenes"""
    
    def __init__(self):
        self.scenes: Dict[str, Scene] = {}
        self.current_scene: Optional[Scene] = None
        self.transition_queue = []
    
    def add_scene(self, scene: Scene):
        """Add a scene to the manager"""
        scene.manager = self
        self.scenes[scene.name] = scene
    
    def switch_to(self, scene_name: str):
        """Switch to a different scene"""
        if scene_name not in self.scenes:
            raise ValueError(f"Scene '{scene_name}' not found")
        
        if self.current_scene:
            self.current_scene.on_exit()
        
        self.current_scene = self.scenes[scene_name]
        self.current_scene.on_enter()
    
    def update(self, dt: float):
        """Update current scene"""
        if self.current_scene:
            self.current_scene.update(dt)
    
    def render(self, renderer):
        """Render current scene"""
        if self.current_scene:
            self.current_scene.render(renderer)


class Sprite:
    """Basic sprite class for game objects"""
    
    def __init__(self, image_path: str, pos: tuple = (0, 0)):
        self.image_path = image_path
        self.pos = list(pos)
        self.size = (32, 32)  # Default size
        self.visible = True
        self.velocity = [0, 0]
    
    def update(self, dt: float):
        """Update sprite position and animation"""
        self.pos[0] += self.velocity[0] * dt
        self.pos[1] += self.velocity[1] * dt
    
    def jump(self):
        """Make sprite jump (simple example)"""
        self.velocity[1] = -200  # Upward velocity
    
    def collides_with(self, point: tuple) -> bool:
        """Check collision with a point"""
        x, y = point
        return (self.pos[0] <= x <= self.pos[0] + self.size[0] and
                self.pos[1] <= y <= self.pos[1] + self.size[1])


class Game:
    """Main PFAGD Game class"""
    
    def __init__(self, title: str = "PFAGD Game", start_scene: Scene = None, 
                 assets=None, resolution: tuple = (800, 600)):
        self.title = title
        self.resolution = resolution
        self.scene_manager = SceneManager()
        self.assets = assets
        self.running = False
        self.fps = 60
        
        # Add initial scene if provided
        if start_scene:
            self.scene_manager.add_scene(start_scene)
            self.scene_manager.switch_to(start_scene.name)
    
    def add_scene(self, scene: Scene):
        """Add scene to the game"""
        self.scene_manager.add_scene(scene)
    
    def run(self):
        """Start the game loop"""
        self.running = True
        
        if KIVY_AVAILABLE:
            self._run_kivy()
        else:
            self._run_basic()
    
    def _run_kivy(self):
        """Run game using Kivy (cross-platform)"""
        
        class PFAGDApp(App):
            def __init__(self, game_instance, **kwargs):
                super().__init__(**kwargs)
                self.game = game_instance
            
            def build(self):
                self.title = self.game.title
                root = Widget()
                Clock.schedule_interval(self.update, 1.0/self.game.fps)
                return root
            
            def update(self, dt):
                self.game.scene_manager.update(dt)
        
        app = PFAGDApp(self)
        app.run()
    
    def _run_basic(self):
        """Basic game loop without Kivy"""
        print(f"Starting {self.title} - Basic Mode")
        print("Kivy not available - running in console mode")
        
        dt = 1.0 / self.fps
        last_time = time.time()
        
        try:
            while self.running:
                current_time = time.time()
                actual_dt = current_time - last_time
                last_time = current_time
                
                # Update game
                self.scene_manager.update(actual_dt)
                
                # Simple frame rate limiting
                time.sleep(max(0, dt - actual_dt))
        
        except KeyboardInterrupt:
            print("Game stopped by user")
        
        self.stop()
    
    def stop(self):
        """Stop the game"""
        self.running = False
        print("Game stopped")


# Hot reload functionality
class HotReloader:
    """Enables hot-reloading of game code during development"""
    
    def __init__(self, watch_dirs: List[str]):
        self.watch_dirs = watch_dirs
        self.last_modified = {}
        self.enabled = False
    
    def enable(self):
        """Enable hot reloading"""
        self.enabled = True
        self._scan_files()
    
    def disable(self):
        """Disable hot reloading"""
        self.enabled = False
    
    def check_for_changes(self):
        """Check if any watched files have changed"""
        if not self.enabled:
            return False
        
        for watch_dir in self.watch_dirs:
            if os.path.exists(watch_dir):
                for root, dirs, files in os.walk(watch_dir):
                    for file in files:
                        if file.endswith('.py'):
                            filepath = os.path.join(root, file)
                            mtime = os.path.getmtime(filepath)
                            
                            if filepath in self.last_modified:
                                if mtime > self.last_modified[filepath]:
                                    print(f"Hot reload: {filepath} changed")
                                    self.last_modified[filepath] = mtime
                                    return True
                            else:
                                self.last_modified[filepath] = mtime
        
        return False
    
    def _scan_files(self):
        """Initial scan of all files"""
        for watch_dir in self.watch_dirs:
            if os.path.exists(watch_dir):
                for root, dirs, files in os.walk(watch_dir):
                    for file in files:
                        if file.endswith('.py'):
                            filepath = os.path.join(root, file)
                            self.last_modified[filepath] = os.path.getmtime(filepath)