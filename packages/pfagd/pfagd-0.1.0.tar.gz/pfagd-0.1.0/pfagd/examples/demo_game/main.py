"""
PFAGD Demo Game
A comprehensive example showcasing PFAGD features
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from pfagd.engine import Game, Scene
from pfagd.ui import Button, Label, Menu
from pfagd.assets import AssetManager


class MainMenu(Scene):
    """Main menu scene with navigation options"""
    
    def __init__(self):
        super().__init__("MainMenu")
        self.title_label = None
        self.menu = None
    
    def on_enter(self):
        print("Entering Main Menu")
        
        # Create title
        self.title_label = Label(
            "PFAGD Demo Game", 
            pos=(250, 450),
            size=(300, 50)
        )
        self.add_widget(self.title_label)
        
        # Create menu with buttons
        menu_buttons = [
            Button("Start Game", on_press=self.start_game),
            Button("Settings", on_press=self.open_settings), 
            Button("About", on_press=self.show_about),
            Button("Quit", on_press=self.quit_game)
        ]
        
        self.menu = Menu(menu_buttons, pos=(300, 250), spacing=15)
        self.add_widget(self.menu)
    
    def start_game(self):
        print("Starting game...")
        self.manager.switch_to("GameScene")
    
    def open_settings(self):
        print("Opening settings...")
        self.manager.switch_to("SettingsScene")
    
    def show_about(self):
        print("Showing about...")
        self.manager.switch_to("AboutScene")
    
    def quit_game(self):
        print("Quitting game...")
        sys.exit(0)


class GameScene(Scene):
    """Main gameplay scene"""
    
    def __init__(self):
        super().__init__("GameScene")
        self.player = None
        self.score = 0
        self.score_label = None
        self.game_time = 0
        self.enemies = []
    
    def on_enter(self):
        print("Starting gameplay...")
        
        # Create player (placeholder sprite)
        self.player = self.add_sprite("player.png", pos=(100, 300))
        print(f"Player created at {self.player.pos}")
        
        # Create UI elements
        self.score_label = Label(f"Score: {self.score}", pos=(10, 550))
        self.add_widget(self.score_label)
        
        # Control buttons
        back_button = Button("Back to Menu", on_press=self.back_to_menu, pos=(10, 10))
        self.add_widget(back_button)
        
        jump_button = Button("Jump", on_press=self.player_jump, pos=(650, 10))
        self.add_widget(jump_button)
        
        move_left_button = Button("Left", on_press=self.move_left, pos=(500, 10))
        self.add_widget(move_left_button)
        
        move_right_button = Button("Right", on_press=self.move_right, pos=(575, 10))
        self.add_widget(move_right_button)
    
    def update(self, dt):
        """Update game logic"""
        self.game_time += dt
        
        # Update player
        if self.player:
            self.player.update(dt)
            
            # Simple gravity simulation
            self.player.velocity[1] += 800 * dt  # Gravity
            
            # Ground collision
            ground_level = 300
            if self.player.pos[1] > ground_level:
                self.player.pos[1] = ground_level
                self.player.velocity[1] = 0
            
            # Screen boundaries
            if self.player.pos[0] < 0:
                self.player.pos[0] = 0
            elif self.player.pos[0] > 750:  # Assuming 800px screen width
                self.player.pos[0] = 750
        
        # Spawn enemies periodically (simple demo)
        if int(self.game_time) % 5 == 0 and int(self.game_time) > 0:
            if len(self.enemies) < 3:  # Max 3 enemies
                enemy = self.add_sprite("enemy.png", pos=(700, 300))
                enemy.velocity = [-100, 0]  # Move left
                self.enemies.append(enemy)
                print(f"Enemy spawned at {enemy.pos}")
        
        # Update enemies
        for enemy in self.enemies[:]:  # Copy list to avoid modification during iteration
            enemy.update(dt)
            
            # Remove enemies that went off screen
            if enemy.pos[0] < -50:
                self.enemies.remove(enemy)
                self.sprites.remove(enemy)
                self.score += 10
                self.score_label.set_text(f"Score: {self.score}")
                print(f"Enemy removed, score: {self.score}")
            
            # Simple collision detection
            if (abs(self.player.pos[0] - enemy.pos[0]) < 30 and 
                abs(self.player.pos[1] - enemy.pos[1]) < 30):
                print("Player hit by enemy! Game over!")
                self.manager.switch_to("GameOverScene")
                return
    
    def player_jump(self):
        """Make player jump"""
        if self.player and self.player.pos[1] >= 300:  # On ground
            self.player.jump()
            print("Player jumped!")
    
    def move_left(self):
        """Move player left"""
        if self.player:
            self.player.pos[0] = max(0, self.player.pos[0] - 50)
            print(f"Player moved left to {self.player.pos}")
    
    def move_right(self):
        """Move player right"""
        if self.player:
            self.player.pos[0] = min(750, self.player.pos[0] + 50)
            print(f"Player moved right to {self.player.pos}")
    
    def back_to_menu(self):
        """Return to main menu"""
        print("Returning to menu...")
        self.manager.switch_to("MainMenu")


class SettingsScene(Scene):
    """Settings scene for game configuration"""
    
    def __init__(self):
        super().__init__("SettingsScene")
    
    def on_enter(self):
        print("Entering settings...")
        
        title = Label("Settings", pos=(350, 450))
        self.add_widget(title)
        
        # Placeholder settings
        sound_label = Label("Sound: ON", pos=(300, 350))
        self.add_widget(sound_label)
        
        music_label = Label("Music: ON", pos=(300, 300))
        self.add_widget(music_label)
        
        difficulty_label = Label("Difficulty: Normal", pos=(300, 250))
        self.add_widget(difficulty_label)
        
        # Back button
        back_button = Button("Back", on_press=self.back_to_menu, pos=(350, 150))
        self.add_widget(back_button)
    
    def back_to_menu(self):
        self.manager.switch_to("MainMenu")


class AboutScene(Scene):
    """About scene with game information"""
    
    def __init__(self):
        super().__init__("AboutScene")
    
    def on_enter(self):
        print("Showing about information...")
        
        title = Label("About PFAGD Demo", pos=(300, 450))
        self.add_widget(title)
        
        info_lines = [
            "PFAGD Demo Game v1.0",
            "Built with PFAGD Framework",
            "Python for Android Game Development",
            "",
            "Features demonstrated:",
            "- Scene management",
            "- Sprite rendering", 
            "- UI widgets",
            "- Basic physics",
            "- Asset management"
        ]
        
        y_pos = 380
        for line in info_lines:
            if line:  # Skip empty lines
                label = Label(line, pos=(250, y_pos))
                self.add_widget(label)
            y_pos -= 25
        
        back_button = Button("Back", on_press=self.back_to_menu, pos=(350, 100))
        self.add_widget(back_button)
    
    def back_to_menu(self):
        self.manager.switch_to("MainMenu")


class GameOverScene(Scene):
    """Game over scene"""
    
    def __init__(self):
        super().__init__("GameOverScene")
    
    def on_enter(self):
        print("Game Over!")
        
        title = Label("GAME OVER", pos=(320, 400))
        self.add_widget(title)
        
        info = Label("You were caught by an enemy!", pos=(270, 350))
        self.add_widget(info)
        
        # Get final score from GameScene
        game_scene = self.manager.scenes.get("GameScene")
        final_score = game_scene.score if game_scene else 0
        
        score_label = Label(f"Final Score: {final_score}", pos=(300, 300))
        self.add_widget(score_label)
        
        # Buttons
        play_again_button = Button("Play Again", on_press=self.play_again, pos=(250, 200))
        self.add_widget(play_again_button)
        
        menu_button = Button("Main Menu", on_press=self.back_to_menu, pos=(400, 200))
        self.add_widget(menu_button)
    
    def play_again(self):
        """Restart the game"""
        print("Restarting game...")
        # Reset game scene
        self.manager.scenes["GameScene"] = GameScene()
        self.manager.switch_to("GameScene")
    
    def back_to_menu(self):
        """Return to main menu"""
        self.manager.switch_to("MainMenu")


def main():
    """Main function to run the demo game"""
    print("Starting PFAGD Demo Game...")
    
    # Create asset manager
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    assets = AssetManager(assets_dir)
    
    # Create game with main menu scene
    game = Game(
        title="PFAGD Demo Game",
        start_scene=MainMenu(),
        assets=assets,
        resolution=(800, 600)
    )
    
    # Add all scenes
    game.add_scene(GameScene())
    game.add_scene(SettingsScene())
    game.add_scene(AboutScene())
    game.add_scene(GameOverScene())
    
    print("Game initialized. Starting game loop...")
    
    # Run the game
    try:
        game.run()
    except KeyboardInterrupt:
        print("\nGame interrupted by user")
    except Exception as e:
        print(f"Game error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()