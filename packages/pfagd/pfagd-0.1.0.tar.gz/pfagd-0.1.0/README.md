# PFAGD - Python for Android Game Development

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/pfagd/pfagd)
[![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)

**PFAGD** is a powerful, all-in-one Python framework for developing 2D and 3D games that run seamlessly on both desktop (Windows/Linux/Mac) and Android devices. Focus on your game logic and design while PFAGD handles cross-platform deployment, monetization, and optimization.

## 🎮 Features

### Core Game Engine
- **Cross-platform compatibility** - Write once, run on desktop and Android
- **Scene management** - Easy scene transitions and state management
- **2D/3D rendering** - Built on Kivy for smooth graphics
- **Physics engine** - Built-in 2D physics simulation
- **Animation framework** - Smooth sprite animations and transitions
- **Audio engine** - Sound effects and music playback

### UI Framework
- **Rich UI widgets** - Buttons, labels, sliders, menus
- **Flexible layouts** - Responsive UI that adapts to screen sizes
- **Custom themes** - Beautiful, customizable UI themes

### Asset Management
- **Smart asset loading** - Automatic optimization for mobile
- **Image processing** - Built-in image compression and format conversion
- **Audio optimization** - Efficient audio format handling
- **Caching system** - Fast asset loading with intelligent caching

### Monetization Ready
- **Ad network support** - AdMob integration with easy setup
- **In-app purchases** - Complete IAP system for Android
- **Analytics tracking** - Built-in game analytics and user tracking
- **A/B testing** - Easy implementation of feature testing

### Build System
- **One-command builds** - `pfagd build-android main.py`
- **Automatic packaging** - Handles manifest, permissions, icons
- **Hot reload** - Live code updates during development
- **Multi-platform** - Build for Android, Windows, Mac, Linux

## 🚀 Quick Start

### Installation

```bash
pip install pfagd
```

### Create a New Game

```bash
# Create a new project
pfagd scaffold mygame

# Navigate to project
cd mygame

# Run on desktop
pfagd run main.py

# Build for Android
pfagd build-android main.py
```

### Simple Game Example

```python
from pfagd.engine import Game, Scene
from pfagd.ui import Button, Label
from pfagd.assets import AssetManager

class MainMenu(Scene):
    def on_enter(self):
        title = Label("My Game", pos=(300, 400))
        self.add_widget(title)
        
        start_btn = Button("Start", on_press=self.start_game)
        self.add_widget(start_btn)
    
    def start_game(self):
        self.manager.switch_to("GameScene")

class GameScene(Scene):
    def on_enter(self):
        self.player = self.add_sprite("player.png", pos=(100, 100))
        
    def update(self, dt):
        # Game logic here
        pass

# Create and run game
game = Game(
    title="My Game",
    start_scene=MainMenu(),
    assets=AssetManager("assets/")
)
game.add_scene(GameScene())
game.run()
```

## 📱 Cross-Platform Development

PFAGD makes cross-platform development effortless:

### Desktop Development
- Instant testing with `pfagd run main.py`
- Hot reload for rapid iteration
- Full Python debugging support

### Android Development
- One-command APK builds
- Automatic permission handling
- Native Android API access through Python

### Code Sharing
- **100% code reuse** between platforms
- Platform-specific optimizations handled automatically
- Unified input handling (touch, mouse, keyboard)

## 🛠 CLI Commands

```bash
# Project Management
pfagd scaffold <name>              # Create new project
pfagd run <file> [--debug]         # Run game on desktop
pfagd run <file> --hot-reload      # Run with hot reload

# Building
pfagd build-android <file>         # Build Android APK
pfagd build-desktop <file>         # Build desktop executable

# Assets
pfagd import-assets <dir>          # Import and optimize assets

# Monetization
pfagd add-monetization admob       # Add AdMob ads
pfagd add-monetization iap         # Add in-app purchases
pfagd add-monetization analytics   # Add analytics tracking
```

## 📚 Examples

### Basic Platformer
```python
class Player(Scene):
    def on_enter(self):
        self.player = self.add_sprite("player.png")
        
    def update(self, dt):
        # Gravity
        self.player.velocity[1] += 500 * dt
        
        # Ground collision
        if self.player.pos[1] > 400:
            self.player.pos[1] = 400
            self.player.velocity[1] = 0
```

### Adding Monetization
```python
# Add AdMob ads
from monetization.ads import AdMobManager

ads = AdMobManager("your-app-id", "banner-id", "interstitial-id")
ads.show_banner("bottom")

# Track analytics
from monetization.analytics import AnalyticsManager

analytics = AnalyticsManager("your-api-key")
analytics.track_level_start("level_1")
```

## 🎯 Target Use Cases

PFAGD is perfect for:

- **Indie game developers** wanting to reach both desktop and mobile
- **Prototype development** with rapid iteration
- **Educational games** that need cross-platform deployment
- **Casual mobile games** with monetization requirements
- **Game jams** where speed of development is crucial

## 📦 Architecture

```
pfagd/
├── engine/          # Core game engine
│   ├── core.py      # Game loop, scenes
│   ├── renderer.py  # Cross-platform rendering
│   ├── physics.py   # Physics simulation
│   └── animation.py # Animation system
├── ui/              # UI framework
│   ├── widgets.py   # Buttons, labels, etc.
│   └── layout.py    # Layout management
├── assets/          # Asset management
│   └── manager.py   # Loading, optimization
├── monetization/    # Revenue features
│   ├── ads.py       # Ad networks
│   ├── iap.py       # In-app purchases
│   └── analytics.py # User tracking
└── cli/             # Command-line tools
    ├── scaffold.py  # Project creation
    └── build.py     # Build system
```

## 🔧 Requirements

- **Python 3.8+**
- **Kivy** (automatically installed)
- **Buildozer** (for Android builds)
- **PIL/Pillow** (for image processing)

Optional:
- **Android SDK** (for Android development)
- **PyInstaller** (for desktop builds)

## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/pfagd/pfagd.git
cd pfagd
pip install -e .
pip install -e .[dev]  # Install development dependencies
```

## 📄 License

PFAGD is released under the MIT License. See [LICENSE](LICENSE) for details.

## 🆘 Support

- **Documentation**: [pfagd.readthedocs.io](https://pfagd.readthedocs.io)
- **Issues**: [GitHub Issues](https://github.com/pfagd/pfagd/issues)
- **Discord**: [Join our Discord](https://discord.gg/pfagd)
- **Email**: support@pfagd.org

## 🎖 Acknowledgments

PFAGD is built on top of excellent open-source projects:
- [Kivy](https://kivy.org) - Cross-platform Python framework
- [Buildozer](https://github.com/kivy/buildozer) - Android packaging
- [PyInstaller](https://pyinstaller.org) - Desktop packaging
- [Pillow](https://pillow.readthedocs.io) - Image processing

---

**Start building your cross-platform game today with PFAGD!** 🚀🎮