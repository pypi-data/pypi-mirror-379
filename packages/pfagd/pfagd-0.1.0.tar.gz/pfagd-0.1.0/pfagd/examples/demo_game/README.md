# PFAGD Demo Game

A comprehensive example showcasing PFAGD (Python for Android Game Development) framework features.

## What this demo shows:

- **Scene Management**: Multiple scenes (MainMenu, GameScene, SettingsScene, AboutScene, GameOverScene)
- **UI Widgets**: Buttons, labels, and menus  
- **Sprite System**: Player and enemy sprites with basic physics
- **Game Logic**: Simple platformer mechanics with collision detection
- **Asset Management**: Organized asset loading and management

## Running the Demo

### Desktop
```bash
python main.py
```

### With PFAGD CLI (if installed)
```bash
pfagd run main.py
```

## Game Controls

- **Jump**: Click the "Jump" button or implement keyboard controls
- **Move**: Use "Left" and "Right" buttons
- **Navigation**: Use menu buttons to navigate between scenes

## Game Mechanics

- Player can jump and move left/right
- Enemies spawn periodically from the right side
- Avoid enemies to keep playing
- Score increases when enemies go off-screen
- Game ends when player collides with an enemy

## Code Structure

```
demo_game/
├── main.py           # Main game file with all scenes
├── assets/           # Game assets directory  
│   ├── README.md     # Asset information
│   └── ...           # Placeholder asset files
└── README.md         # This file
```

## Extending the Demo

This demo serves as a template for creating your own PFAGD games. You can:

1. **Add new scenes** by creating new Scene classes
2. **Add more sprites** with different behaviors
3. **Implement sound effects** using the audio system
4. **Add animations** using the animation framework
5. **Include monetization** with ads or in-app purchases

## Building for Android

To build this demo as an Android APK:

1. Ensure you have a `buildozer.spec` file (create one with `pfagd scaffold`)
2. Run: `pfagd build-android main.py`

## Next Steps

- Study the code to understand PFAGD patterns
- Modify scenes and add your own game logic
- Replace placeholder assets with real graphics
- Add sound effects and music
- Test on both desktop and Android

Happy game development with PFAGD! 🎮