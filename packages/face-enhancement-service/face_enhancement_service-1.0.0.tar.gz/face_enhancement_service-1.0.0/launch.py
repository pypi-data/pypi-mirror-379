#!/usr/bin/env python3
"""
Cross-platform Face Enhancement API Launcher
Automatically detects platform and uses appropriate configuration
"""

import sys
import os
import platform
import subprocess
from pathlib import Path

def detect_platform():
    """Detect the current platform"""
    system = platform.system().lower()
    return {
        "windows": system == "windows",
        "linux": system == "linux", 
        "mac": system == "darwin",
        "name": system
    }

def get_requirements_file(platform_info):
    """Get the appropriate requirements file"""
    if platform_info["windows"]:
        return "requirements_windows.txt"
    else:
        return "requirements_api.txt"

def install_dependencies(requirements_file):
    """Install dependencies"""
    print(f"📦 Installing dependencies from {requirements_file}...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_file], 
                      check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def start_api():
    """Start the API server"""
    print("🚀 Starting Face Enhancement API...")
    try:
        # Import and run the API
        import sys
        sys.path.append('src')
        from src.face_enhancer_api import app
        import uvicorn
        
        # Get configuration
        from src.config import config
        uvicorn_config = config.get_uvicorn_config()
        
        print(f"🖥️  Platform: {config.system}")
        print(f"⚙️  Config: {uvicorn_config}")
        
        uvicorn.run("src.face_enhancer_api:app", **uvicorn_config)
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you're in the correct directory and dependencies are installed")
        return False
    except Exception as e:
        print(f"❌ Failed to start API: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main launcher function"""
    print("🎯 Face Enhancement API Cross-Platform Launcher")
    print("=" * 50)
    
    # Detect platform
    platform_info = detect_platform()
    print(f"🖥️  Detected platform: {platform_info['name'].title()}")
    
    # Get requirements file
    requirements_file = get_requirements_file(platform_info)
    print(f"📋 Using requirements: {requirements_file}")
    
    # Check if requirements file exists
    if not os.path.exists(requirements_file):
        print(f"❌ Requirements file not found: {requirements_file}")
        return False
    
    # Install dependencies
    if not install_dependencies(requirements_file):
        return False
    
    # Start API
    print("\n🎉 Starting API server...")
    start_api()

if __name__ == "__main__":
    main()
