"""
PFAGD Build System
Build PFAGD games for Android and Desktop platforms
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional


def build_android(game_file: str, output_dir: str = "dist", release: bool = False) -> int:
    """Build Android APK using Buildozer"""
    
    if not os.path.exists(game_file):
        print(f"Error: Game file '{game_file}' not found")
        return 1
    
    # Check if buildozer.spec exists
    buildozer_spec = Path("buildozer.spec")
    if not buildozer_spec.exists():
        print("Error: buildozer.spec not found")
        print("Run 'pfagd scaffold <project_name>' to create a new project with build configuration")
        return 1
    
    print(f"Building Android APK from {game_file}...")
    print(f"Output directory: {output_dir}")
    print(f"Release mode: {release}")
    
    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    try:
        # Check if buildozer is installed
        subprocess.run(["buildozer", "version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Buildozer not found. Installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "buildozer"], check=True)
        except subprocess.CalledProcessError:
            print("Error: Failed to install Buildozer")
            return 1
    
    # Build command
    build_cmd = ["buildozer"]
    
    if release:
        build_cmd.append("android")
        build_cmd.append("release")
    else:
        build_cmd.append("android")
        build_cmd.append("debug")
    
    # Add verbose output
    build_cmd.append("-v")
    
    print(f"Running: {' '.join(build_cmd)}")
    
    try:
        # Run buildozer
        result = subprocess.run(build_cmd, cwd=os.getcwd())
        
        if result.returncode == 0:
            # Move APK to output directory
            bin_dir = Path("bin")
            if bin_dir.exists():
                apk_files = list(bin_dir.glob("*.apk"))
                if apk_files:
                    for apk_file in apk_files:
                        dest = Path(output_dir) / apk_file.name
                        apk_file.rename(dest)
                        print(f"✓ APK built successfully: {dest}")
                else:
                    print("Warning: No APK files found in bin/ directory")
            
            print("✓ Android build completed successfully!")
            return 0
        else:
            print("✗ Android build failed")
            return result.returncode
    
    except KeyboardInterrupt:
        print("\nBuild cancelled by user")
        return 1
    except Exception as e:
        print(f"Error during build: {e}")
        return 1


def build_desktop(game_file: str, output_dir: str = "dist", platform: str = "auto") -> int:
    """Build desktop executable using PyInstaller"""
    
    if not os.path.exists(game_file):
        print(f"Error: Game file '{game_file}' not found")
        return 1
    
    print(f"Building desktop executable from {game_file}...")
    print(f"Output directory: {output_dir}")
    print(f"Target platform: {platform}")
    
    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    try:
        # Check if PyInstaller is installed
        subprocess.run([sys.executable, "-m", "PyInstaller", "--version"], 
                      check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: PyInstaller not found. Installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "PyInstaller"], check=True)
        except subprocess.CalledProcessError:
            print("Error: Failed to install PyInstaller")
            return 1
    
    # Build command
    build_cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # Single executable
        "--windowed",  # No console window (GUI app)
        "--distpath", output_dir,
        "--workpath", os.path.join(output_dir, "build"),
        "--specpath", os.path.join(output_dir, "spec"),
        game_file
    ]
    
    # Add hidden imports for common PFAGD dependencies
    hidden_imports = [
        "kivy.app",
        "kivy.uix.widget",
        "kivy.uix.button", 
        "kivy.uix.label",
        "PIL.Image",
        "pfagd.engine.core",
        "pfagd.ui.widgets",
        "pfagd.assets.manager"
    ]
    
    for import_name in hidden_imports:
        build_cmd.extend(["--hidden-import", import_name])
    
    # Add assets directory if it exists
    if os.path.exists("assets"):
        build_cmd.extend(["--add-data", f"assets{os.pathsep}assets"])
    
    print(f"Running: {' '.join(build_cmd[:5])} ... (full command truncated)")
    
    try:
        # Run PyInstaller
        result = subprocess.run(build_cmd)
        
        if result.returncode == 0:
            print("✓ Desktop build completed successfully!")
            
            # List output files
            output_path = Path(output_dir)
            exe_files = list(output_path.glob("*.exe")) + list(output_path.glob("*")) 
            exe_files = [f for f in exe_files if f.is_file() and not f.suffix in ['.spec']]
            
            for exe_file in exe_files:
                print(f"  📦 {exe_file}")
            
            return 0
        else:
            print("✗ Desktop build failed")
            return result.returncode
    
    except KeyboardInterrupt:
        print("\nBuild cancelled by user")
        return 1
    except Exception as e:
        print(f"Error during build: {e}")
        return 1


def clean_build_artifacts():
    """Clean build artifacts and temporary files"""
    
    artifacts = [
        "build",
        "dist", 
        "__pycache__",
        "*.spec",
        ".buildozer",
        "bin",
    ]
    
    print("Cleaning build artifacts...")
    
    for pattern in artifacts:
        if "*" in pattern:
            # Glob pattern
            from glob import glob
            for path in glob(pattern):
                _remove_path(Path(path))
        else:
            _remove_path(Path(pattern))
    
    print("✓ Build artifacts cleaned")


def _remove_path(path: Path):
    """Remove a file or directory"""
    try:
        if path.exists():
            if path.is_dir():
                import shutil
                shutil.rmtree(path)
                print(f"  Removed directory: {path}")
            else:
                path.unlink()
                print(f"  Removed file: {path}")
    except Exception as e:
        print(f"  Warning: Could not remove {path}: {e}")


if __name__ == '__main__':
    # Test build functions
    import sys
    
    if len(sys.argv) > 2:
        if sys.argv[1] == "android":
            build_android(sys.argv[2])
        elif sys.argv[1] == "desktop":
            build_desktop(sys.argv[2])
        elif sys.argv[1] == "clean":
            clean_build_artifacts()
    else:
        print("Usage: python build.py [android|desktop|clean] <game_file>")