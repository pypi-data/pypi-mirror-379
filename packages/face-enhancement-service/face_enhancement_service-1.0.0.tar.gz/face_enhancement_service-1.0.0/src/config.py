"""
Face Enhancement Service Configuration
Cross-platform compatibility settings
"""

import os
import platform
from typing import Dict, Any

class APIConfig:
    """Configuration class for cross-platform compatibility"""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.is_windows = self.system == "windows"
        self.is_linux = self.system == "linux"
        self.is_mac = self.system == "darwin"
        
        # Platform-specific settings
        self.settings = self._get_platform_settings()
    
    def _get_platform_settings(self) -> Dict[str, Any]:
        """Get platform-specific settings"""
        if self.is_windows:
            return {
                "uvicorn_config": {
                    "workers": 1,  # Single worker for Windows
                    "loop": None,  # Default event loop
                    "http": None,  # Default HTTP parser
                },
                "performance": {
                    "max_workers": 20,  # Reduced for Windows
                    "thread_pool_size": 10,
                },
                "paths": {
                    "separator": "\\",
                    "temp_dir": os.environ.get("TEMP", "C:\\temp"),
                }
            }
        else:  # Linux/Mac
            return {
                "uvicorn_config": {
                    "workers": 4,  # Multiple workers for Linux/Mac
                    "loop": "uvloop",  # Faster event loop
                    "http": "httptools",  # Faster HTTP parser
                },
                "performance": {
                    "max_workers": 50,  # Full performance
                    "thread_pool_size": 25,
                },
                "paths": {
                    "separator": "/",
                    "temp_dir": "/tmp",
                }
            }
    
    def get_uvicorn_config(self) -> Dict[str, Any]:
        """Get uvicorn configuration for current platform"""
        base_config = {
            "host": "0.0.0.0",
            "port": 8000,
            "access_log": True,
            "log_level": "info"
        }
        
        # Add platform-specific config
        platform_config = self.settings["uvicorn_config"]
        
        # Only add non-None values to avoid uvicorn errors
        for key, value in platform_config.items():
            if value is not None:
                base_config[key] = value
        
        return base_config
    
    def get_performance_config(self) -> Dict[str, Any]:
        """Get performance configuration for current platform"""
        return self.settings["performance"]
    
    def get_path_config(self) -> Dict[str, Any]:
        """Get path configuration for current platform"""
        return self.settings["paths"]
    
    def is_feature_enabled(self, feature: str) -> bool:
        """Check if a feature is enabled for current platform"""
        feature_map = {
            "uvloop": not self.is_windows,
            "httptools": not self.is_windows,
            "multi_worker": not self.is_windows,
            "high_performance": not self.is_windows,
        }
        return feature_map.get(feature, True)
    
    def get_requirements_file(self) -> str:
        """Get appropriate requirements file for current platform"""
        if self.is_windows:
            return "requirements_windows.txt"
        else:
            return "requirements_api.txt"
    
    def get_startup_script(self) -> str:
        """Get appropriate startup script for current platform"""
        if self.is_windows:
            return "start.bat"
        else:
            return "start.sh"

# Global configuration instance
config = APIConfig()
