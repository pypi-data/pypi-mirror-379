"""
PFAGD Monetization Module
Add monetization features to PFAGD games
"""

import os
import json
from pathlib import Path
from typing import Dict, Any


MONETIZATION_CONFIGS = {
    'admob': {
        'name': 'Google AdMob',
        'description': 'Add Google AdMob banner and interstitial ads',
        'files': {
            'monetization/ads.py': '''"""
Google AdMob Integration for PFAGD
"""

try:
    from kivy.logger import Logger
    from plyer import unique_id
    MOBILE_AVAILABLE = True
except ImportError:
    MOBILE_AVAILABLE = False
    print("Warning: Mobile features not available in desktop mode")


class AdMobManager:
    """Manages AdMob advertisements"""
    
    def __init__(self, app_id: str, banner_id: str, interstitial_id: str):
        self.app_id = app_id
        self.banner_id = banner_id
        self.interstitial_id = interstitial_id
        self.banner_loaded = False
        self.interstitial_loaded = False
        
        if MOBILE_AVAILABLE:
            self._initialize_admob()
    
    def _initialize_admob(self):
        """Initialize AdMob SDK"""
        try:
            # This would integrate with actual AdMob SDK
            # For now, it's a placeholder
            Logger.info("AdMob: Initializing with app ID: " + self.app_id)
            self.banner_loaded = True
            self.interstitial_loaded = True
        except Exception as e:
            Logger.error(f"AdMob: Failed to initialize: {e}")
    
    def show_banner(self, position: str = "bottom"):
        """Show banner ad"""
        if not self.banner_loaded:
            print("AdMob: Banner not loaded")
            return
        
        if MOBILE_AVAILABLE:
            Logger.info(f"AdMob: Showing banner ad at {position}")
            # Actual AdMob banner implementation would go here
        else:
            print(f"AdMob: [DEMO] Showing banner ad at {position}")
    
    def hide_banner(self):
        """Hide banner ad"""
        if MOBILE_AVAILABLE:
            Logger.info("AdMob: Hiding banner ad")
            # Actual AdMob banner hide implementation
        else:
            print("AdMob: [DEMO] Hiding banner ad")
    
    def show_interstitial(self):
        """Show interstitial ad"""
        if not self.interstitial_loaded:
            print("AdMob: Interstitial not loaded")
            return
        
        if MOBILE_AVAILABLE:
            Logger.info("AdMob: Showing interstitial ad")
            # Actual AdMob interstitial implementation would go here
        else:
            print("AdMob: [DEMO] Showing full-screen interstitial ad")
    
    def load_interstitial(self):
        """Load a new interstitial ad"""
        if MOBILE_AVAILABLE:
            Logger.info("AdMob: Loading interstitial ad")
            # Actual loading logic
            self.interstitial_loaded = True
        else:
            print("AdMob: [DEMO] Loading interstitial ad")
            self.interstitial_loaded = True
''',
            'monetization/__init__.py': '# PFAGD Monetization Module',
            'config/admob_config.json': '''{
    "app_id": "ca-app-pub-YOUR_APP_ID",
    "banner_id": "ca-app-pub-YOUR_BANNER_ID",
    "interstitial_id": "ca-app-pub-YOUR_INTERSTITIAL_ID",
    "test_mode": true,
    "test_device_ids": []
}'''
        }
    },
    
    'iap': {
        'name': 'In-App Purchases',
        'description': 'Add in-app purchases and subscriptions',
        'files': {
            'monetization/iap.py': '''"""
In-App Purchase Integration for PFAGD
"""

try:
    from kivy.logger import Logger
    MOBILE_AVAILABLE = True
except ImportError:
    MOBILE_AVAILABLE = False


class IAPManager:
    """Manages in-app purchases"""
    
    def __init__(self, products: list):
        self.products = products
        self.purchased_items = set()
        
        if MOBILE_AVAILABLE:
            self._initialize_iap()
    
    def _initialize_iap(self):
        """Initialize IAP system"""
        try:
            Logger.info("IAP: Initializing in-app purchases")
            # Actual IAP initialization would go here
        except Exception as e:
            Logger.error(f"IAP: Failed to initialize: {e}")
    
    def purchase_product(self, product_id: str):
        """Purchase a product"""
        if product_id not in self.products:
            print(f"IAP: Unknown product: {product_id}")
            return False
        
        if MOBILE_AVAILABLE:
            Logger.info(f"IAP: Purchasing product: {product_id}")
            # Actual purchase logic would go here
        else:
            print(f"IAP: [DEMO] Purchasing product: {product_id}")
        
        self.purchased_items.add(product_id)
        return True
    
    def is_purchased(self, product_id: str) -> bool:
        """Check if product is purchased"""
        return product_id in self.purchased_items
    
    def restore_purchases(self):
        """Restore previous purchases"""
        if MOBILE_AVAILABLE:
            Logger.info("IAP: Restoring purchases")
            # Actual restore logic
        else:
            print("IAP: [DEMO] Restoring purchases")
''',
            'config/iap_config.json': '''{
    "products": [
        {
            "id": "remove_ads",
            "name": "Remove Ads",
            "price": "$1.99",
            "type": "non_consumable"
        },
        {
            "id": "premium_character",
            "name": "Premium Character Pack",
            "price": "$4.99", 
            "type": "non_consumable"
        },
        {
            "id": "coins_100",
            "name": "100 Coins",
            "price": "$0.99",
            "type": "consumable"
        }
    ]
}'''
        }
    },
    
    'analytics': {
        'name': 'Game Analytics',
        'description': 'Add game analytics and user tracking',
        'files': {
            'monetization/analytics.py': '''"""
Game Analytics for PFAGD
"""

import json
import time
from typing import Dict, Any

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class AnalyticsManager:
    """Manages game analytics and tracking"""
    
    def __init__(self, api_key: str = None, endpoint: str = None):
        self.api_key = api_key or "demo_api_key"
        self.endpoint = endpoint or "https://api.example-analytics.com/events"
        self.session_id = str(int(time.time()))
        self.events_queue = []
        
    def track_event(self, event_name: str, properties: Dict[str, Any] = None):
        """Track a custom event"""
        event_data = {
            'event_name': event_name,
            'properties': properties or {},
            'timestamp': time.time(),
            'session_id': self.session_id
        }
        
        self.events_queue.append(event_data)
        print(f"Analytics: Tracked event '{event_name}' with properties: {properties}")
        
        # In a real implementation, batch send events
        if len(self.events_queue) >= 10:
            self._send_events()
    
    def track_level_start(self, level_name: str):
        """Track level start"""
        self.track_event('level_start', {'level': level_name})
    
    def track_level_complete(self, level_name: str, score: int, time_taken: float):
        """Track level completion"""
        self.track_event('level_complete', {
            'level': level_name,
            'score': score,
            'time_taken': time_taken
        })
    
    def track_purchase(self, product_id: str, price: float):
        """Track in-app purchase"""
        self.track_event('purchase', {
            'product_id': product_id,
            'price': price,
            'currency': 'USD'
        })
    
    def track_ad_shown(self, ad_type: str):
        """Track advertisement shown"""
        self.track_event('ad_shown', {'ad_type': ad_type})
    
    def _send_events(self):
        """Send queued events to analytics server"""
        if not REQUESTS_AVAILABLE:
            print("Analytics: Would send events (requests not available)")
            self.events_queue.clear()
            return
        
        try:
            payload = {
                'api_key': self.api_key,
                'events': self.events_queue
            }
            
            # This would send to actual analytics service
            print(f"Analytics: Sending {len(self.events_queue)} events")
            # response = requests.post(self.endpoint, json=payload)
            
            self.events_queue.clear()
            
        except Exception as e:
            print(f"Analytics: Failed to send events: {e}")
''',
            'config/analytics_config.json': '''{
    "api_key": "your_analytics_api_key_here",
    "endpoint": "https://api.your-analytics-service.com/events",
    "batch_size": 10,
    "auto_track_sessions": true,
    "auto_track_crashes": true
}'''
        }
    }
}


def add_monetization_feature(feature_type: str, config_file: str = None) -> int:
    """Add monetization feature to current project"""
    
    if feature_type not in MONETIZATION_CONFIGS:
        print(f"Error: Unknown monetization type '{feature_type}'")
        print(f"Available types: {', '.join(MONETIZATION_CONFIGS.keys())}")
        return 1
    
    feature_config = MONETIZATION_CONFIGS[feature_type]
    
    print(f"Adding {feature_config['name']} to project...")
    print(f"Description: {feature_config['description']}")
    
    # Create monetization files
    for file_path, content in feature_config['files'].items():
        full_path = Path(file_path)
        
        # Create parent directories
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Check if file already exists
        if full_path.exists():
            response = input(f"File {file_path} already exists. Overwrite? (y/N): ")
            if response.lower() != 'y':
                print(f"Skipped {file_path}")
                continue
        
        # Write file
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created {file_path}")
    
    # Update main.py to include monetization imports (basic example)
    _update_main_for_monetization(feature_type)
    
    print(f"✓ {feature_config['name']} added successfully!")
    print()
    print("Next steps:")
    
    if feature_type == 'admob':
        print("1. Update config/admob_config.json with your AdMob IDs")
        print("2. Add AdMobManager to your game scenes")
        print("3. Test ads in development mode")
    elif feature_type == 'iap':
        print("1. Configure products in config/iap_config.json")
        print("2. Add IAPManager to your game")
        print("3. Test purchases in sandbox mode")
    elif feature_type == 'analytics':
        print("1. Update config/analytics_config.json with your API key")
        print("2. Add AnalyticsManager to track events")
        print("3. View analytics in your dashboard")
    
    return 0


def _update_main_for_monetization(feature_type: str):
    """Add basic monetization imports to main.py"""
    
    main_file = Path("main.py")
    if not main_file.exists():
        print("Warning: main.py not found - skipping auto-import")
        return
    
    try:
        with open(main_file, 'r') as f:
            content = f.read()
        
        # Add import at the top (simple approach)
        if feature_type == 'admob' and 'from monetization.ads import AdMobManager' not in content:
            import_line = "\n# Added by PFAGD monetization\nfrom monetization.ads import AdMobManager\n"
            content = content.replace('"""', '"""' + import_line, 1)
        
        elif feature_type == 'iap' and 'from monetization.iap import IAPManager' not in content:
            import_line = "\n# Added by PFAGD monetization\nfrom monetization.iap import IAPManager\n"
            content = content.replace('"""', '"""' + import_line, 1)
            
        elif feature_type == 'analytics' and 'from monetization.analytics import AnalyticsManager' not in content:
            import_line = "\n# Added by PFAGD monetization\nfrom monetization.analytics import AnalyticsManager\n"
            content = content.replace('"""', '"""' + import_line, 1)
        
        with open(main_file, 'w') as f:
            f.write(content)
        
        print("✓ Updated main.py with monetization imports")
    
    except Exception as e:
        print(f"Warning: Could not auto-update main.py: {e}")


if __name__ == '__main__':
    # Test monetization features
    import sys
    
    if len(sys.argv) > 1:
        add_monetization_feature(sys.argv[1])
    else:
        print("Available monetization features:")
        for feature_id, config in MONETIZATION_CONFIGS.items():
            print(f"  {feature_id}: {config['name']}")
            print(f"    {config['description']}")
            print()