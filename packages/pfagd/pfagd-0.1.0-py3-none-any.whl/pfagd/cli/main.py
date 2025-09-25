"""
PFAGD CLI Main Entry Point
Command-line interface for PFAGD game development toolkit
"""

# Disable Kivy argument parsing to prevent CLI conflicts
import os
os.environ['KIVY_NO_ARGS'] = '1'

import argparse
import sys
from pathlib import Path

from ..version import __version__
from .scaffold import create_project
from .build import build_android, build_desktop


def run_game(game_file: str, debug: bool = False, hot_reload: bool = False):
    """Run a PFAGD game"""
    if not os.path.exists(game_file):
        print(f"Error: Game file '{game_file}' not found")
        return 1
    
    try:
        # Add current directory to Python path
        current_dir = os.path.dirname(os.path.abspath(game_file))
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        # Enable debug mode if requested
        if debug:
            os.environ['PFAGD_DEBUG'] = '1'
        
        # Enable hot reload if requested
        if hot_reload:
            print("Hot reload enabled - press Ctrl+R to reload")
            os.environ['PFAGD_HOT_RELOAD'] = '1'
        
        # Import and run the game
        import runpy
        runpy.run_path(game_file, run_name='__main__')
        return 0
        
    except Exception as e:
        print(f"Error running game: {e}")
        if debug:
            import traceback
            traceback.print_exc()
        return 1


def import_assets(assets_dir: str, optimize: bool = True):
    """Import and process assets"""
    from ..assets.manager import AssetManager
    
    if not os.path.exists(assets_dir):
        print(f"Error: Assets directory '{assets_dir}' not found")
        return 1
    
    print(f"Importing assets from {assets_dir}...")
    
    # Initialize asset manager
    asset_manager = AssetManager(assets_dir)
    
    # Find all assets
    asset_files = []
    for ext in ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif', '*.wav', '*.mp3', '*.ogg', '*.json', '*.txt']:
        asset_files.extend(Path(assets_dir).rglob(ext))
    
    # Process assets
    relative_paths = [str(f.relative_to(assets_dir)) for f in asset_files]
    if optimize:
        print("Optimizing assets for mobile deployment...")
        asset_manager.preload_assets(relative_paths)
    
    print(f"Processed {len(relative_paths)} assets")
    info = asset_manager.get_asset_info()
    print(f"Cache directory: {info['cache_dir']}")
    return 0


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        prog='pfagd',
        description='PFAGD - Python for Android Game Development',
        epilog='For more help on a command, use: pfagd <command> --help'
    )
    
    parser.add_argument('--version', action='version', version=f'PFAGD {__version__}')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Scaffold command
    scaffold_parser = subparsers.add_parser(
        'scaffold',
        help='Create a new PFAGD project'
    )
    scaffold_parser.add_argument(
        'project_name',
        help='Name of the project to create'
    )
    scaffold_parser.add_argument(
        '--template',
        default='basic',
        choices=['basic', 'platformer', '2d-shooter', '3d-demo'],
        help='Project template to use'
    )
    
    # Run command
    run_parser = subparsers.add_parser(
        'run',
        help='Run a PFAGD game'
    )
    run_parser.add_argument(
        'game_file',
        help='Python file containing the game'
    )
    run_parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode'
    )
    run_parser.add_argument(
        '--hot-reload',
        action='store_true',
        help='Enable hot reload for development'
    )
    
    # Build Android command
    build_android_parser = subparsers.add_parser(
        'build-android',
        help='Build Android APK'
    )
    build_android_parser.add_argument(
        'game_file',
        help='Python file containing the game'
    )
    build_android_parser.add_argument(
        '--output',
        '-o',
        default='dist',
        help='Output directory for APK'
    )
    build_android_parser.add_argument(
        '--release',
        action='store_true',
        help='Build release APK (requires signing)'
    )
    
    # Build desktop command
    build_desktop_parser = subparsers.add_parser(
        'build-desktop',
        help='Build desktop executable'
    )
    build_desktop_parser.add_argument(
        'game_file',
        help='Python file containing the game'
    )
    build_desktop_parser.add_argument(
        '--output',
        '-o',
        default='dist',
        help='Output directory for executable'
    )
    build_desktop_parser.add_argument(
        '--platform',
        choices=['windows', 'linux', 'macos', 'all'],
        default='auto',
        help='Target platform(s)'
    )
    
    # Import assets command
    import_parser = subparsers.add_parser(
        'import-assets',
        help='Import and optimize game assets'
    )
    import_parser.add_argument(
        'assets_dir',
        help='Directory containing assets to import'
    )
    import_parser.add_argument(
        '--no-optimize',
        action='store_true',
        help='Skip asset optimization'
    )
    
    # Add monetization command
    monetization_parser = subparsers.add_parser(
        'add-monetization',
        help='Add monetization features to project'
    )
    monetization_parser.add_argument(
        'type',
        choices=['admob', 'unity-ads', 'iap', 'analytics'],
        help='Type of monetization to add'
    )
    monetization_parser.add_argument(
        '--config',
        help='Configuration file for monetization setup'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    # Execute command
    try:
        if args.command == 'scaffold':
            return create_project(args.project_name, args.template)
        
        elif args.command == 'run':
            return run_game(args.game_file, args.debug, args.hot_reload)
        
        elif args.command == 'build-android':
            return build_android(args.game_file, args.output, args.release)
        
        elif args.command == 'build-desktop':
            return build_desktop(args.game_file, args.output, args.platform)
        
        elif args.command == 'import-assets':
            return import_assets(args.assets_dir, not args.no_optimize)
        
        elif args.command == 'add-monetization':
            from .monetization import add_monetization_feature
            return add_monetization_feature(args.type, args.config)
        
        else:
            print(f"Error: Unknown command '{args.command}'")
            return 1
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())