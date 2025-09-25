"""
PFAGD Asset Manager
Handles loading, caching, and optimization of game assets
"""

import os
import json
import hashlib
from typing import Dict, Any, Optional
from pathlib import Path

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("Warning: PIL/Pillow not available. Image optimization disabled.")


class AssetManager:
    """Manages game assets (images, audio, data files)"""
    
    def __init__(self, assets_dir: str = "assets"):
        self.assets_dir = Path(assets_dir)
        self.cache_dir = self.assets_dir / ".cache"
        self.loaded_assets: Dict[str, Any] = {}
        self.asset_registry: Dict[str, Dict] = {}
        
        # Create directories if they don't exist
        self.assets_dir.mkdir(exist_ok=True)
        self.cache_dir.mkdir(exist_ok=True)
        
        # Load asset registry
        self._load_registry()
    
    def _load_registry(self):
        """Load asset registry from disk"""
        registry_file = self.cache_dir / "registry.json"
        if registry_file.exists():
            try:
                with open(registry_file, 'r') as f:
                    self.asset_registry = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.asset_registry = {}
    
    def _save_registry(self):
        """Save asset registry to disk"""
        registry_file = self.cache_dir / "registry.json"
        try:
            with open(registry_file, 'w') as f:
                json.dump(self.asset_registry, f, indent=2)
        except IOError:
            print("Warning: Could not save asset registry")
    
    def _get_file_hash(self, filepath: Path) -> str:
        """Get MD5 hash of a file"""
        hash_md5 = hashlib.md5()
        try:
            with open(filepath, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except IOError:
            return ""
    
    def load_image(self, image_path: str, optimize: bool = True) -> Optional[str]:
        """Load and optionally optimize an image asset"""
        full_path = self.assets_dir / image_path
        
        if not full_path.exists():
            print(f"Warning: Image {image_path} not found")
            return None
        
        # Check cache
        cache_key = f"image_{image_path}"
        if cache_key in self.loaded_assets:
            return self.loaded_assets[cache_key]
        
        # Check if optimization is needed
        if optimize and PIL_AVAILABLE:
            optimized_path = self._optimize_image(full_path, image_path)
            if optimized_path:
                self.loaded_assets[cache_key] = str(optimized_path)
                return str(optimized_path)
        
        # Return original path
        self.loaded_assets[cache_key] = str(full_path)
        return str(full_path)
    
    def _optimize_image(self, source_path: Path, relative_path: str) -> Optional[Path]:
        """Optimize image for mobile/web deployment"""
        file_hash = self._get_file_hash(source_path)
        
        # Check if already optimized
        if relative_path in self.asset_registry:
            cached_info = self.asset_registry[relative_path]
            if cached_info.get('hash') == file_hash:
                cached_path = Path(cached_info['optimized_path'])
                if cached_path.exists():
                    return cached_path
        
        try:
            # Open and optimize image
            with Image.open(source_path) as img:
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize if too large (optional)
                max_size = 2048
                if max(img.size) > max_size:
                    img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                
                # Save optimized version
                optimized_filename = f"opt_{file_hash[:8]}_{source_path.name}"
                optimized_path = self.cache_dir / optimized_filename
                
                img.save(optimized_path, 'JPEG', quality=85, optimize=True)
                
                # Update registry
                self.asset_registry[relative_path] = {
                    'original_path': str(source_path),
                    'optimized_path': str(optimized_path),
                    'hash': file_hash,
                    'optimized': True
                }
                self._save_registry()
                
                return optimized_path
        
        except Exception as e:
            print(f"Warning: Could not optimize image {relative_path}: {e}")
            return None
    
    def load_audio(self, audio_path: str) -> Optional[str]:
        """Load audio asset"""
        full_path = self.assets_dir / audio_path
        
        if not full_path.exists():
            print(f"Warning: Audio {audio_path} not found")
            return None
        
        # For now, just return the path
        # In a full implementation, this would handle audio format conversion
        cache_key = f"audio_{audio_path}"
        self.loaded_assets[cache_key] = str(full_path)
        return str(full_path)
    
    def load_data(self, data_path: str) -> Optional[Any]:
        """Load data file (JSON, text, etc.)"""
        full_path = self.assets_dir / data_path
        
        if not full_path.exists():
            print(f"Warning: Data file {data_path} not found")
            return None
        
        cache_key = f"data_{data_path}"
        if cache_key in self.loaded_assets:
            return self.loaded_assets[cache_key]
        
        try:
            if data_path.endswith('.json'):
                with open(full_path, 'r') as f:
                    data = json.load(f)
            else:
                with open(full_path, 'r') as f:
                    data = f.read()
            
            self.loaded_assets[cache_key] = data
            return data
        
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load data file {data_path}: {e}")
            return None
    
    def preload_assets(self, asset_list: list):
        """Preload a list of assets"""
        print(f"Preloading {len(asset_list)} assets...")
        
        for asset_path in asset_list:
            if asset_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                self.load_image(asset_path)
            elif asset_path.lower().endswith(('.wav', '.mp3', '.ogg', '.aac')):
                self.load_audio(asset_path)
            elif asset_path.lower().endswith(('.json', '.txt', '.xml')):
                self.load_data(asset_path)
            else:
                print(f"Warning: Unknown asset type: {asset_path}")
    
    def clear_cache(self):
        """Clear asset cache"""
        self.loaded_assets.clear()
        
        # Optionally remove cached files
        for file in self.cache_dir.glob("opt_*"):
            try:
                file.unlink()
            except OSError:
                pass
    
    def get_asset_info(self) -> Dict[str, Any]:
        """Get information about loaded assets"""
        return {
            'loaded_count': len(self.loaded_assets),
            'assets_dir': str(self.assets_dir),
            'cache_dir': str(self.cache_dir),
            'registry_size': len(self.asset_registry)
        }