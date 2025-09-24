# Cross-Platform Dependency Installation Guide

## 🔧 How Dependency Installation is Toggled

### **📋 Current System Overview**

The `face-enhancement-service` package uses **multiple layers** of cross-platform dependency management:

### **1. 🎯 Primary Method: `extras_require`**

```python
# In setup.py
extras_require={
    "linux": [
        "uvloop>=0.19.0",      # Linux/Mac only
        "httptools>=0.6.1",    # Linux/Mac only
    ],
    "windows": [
        # Windows-specific packages (if any)
    ],
    "dev": [
        "pytest>=7.0.0",
        "black>=22.0.0",
    ],
}
```

**Installation Commands:**
```bash
# Windows (default - no extras)
pip install face-enhancement-service

# Linux/Mac (with performance optimizations)
pip install face-enhancement-service[linux]

# Development (all platforms)
pip install face-enhancement-service[dev]

# Everything (all platforms)
pip install face-enhancement-service[all]
```

### **2. 🖥️ Platform-Specific Requirements Files**

#### **File Structure:**
```
face-enhancement-service/
├── requirements.txt              # Base dependencies (all platforms)
├── requirements_windows.txt      # Windows-specific
├── requirements_api.txt          # Linux/Mac specific
└── src/config.py                 # Runtime platform detection
```

#### **Windows (`requirements_windows.txt`):**
```txt
# Core dependencies (Windows-compatible)
fastapi==0.104.1
uvicorn[standard]==0.24.0
opencv-python==4.8.1.78
# ... other packages
# Note: uvloop and httptools are NOT included
```

#### **Linux/Mac (`requirements_api.txt`):**
```txt
# Core dependencies + performance optimizations
fastapi==0.104.1
uvicorn[standard]==0.24.0
# uvloop==0.19.0  # Commented for Windows compatibility
# httptools==0.6.1  # Commented for Windows compatibility
opencv-python==4.8.1.78
# ... other packages
```

### **3. 🔄 Runtime Platform Detection**

#### **In `src/config.py`:**
```python
import platform

class APIConfig:
    def __init__(self):
        self.system = platform.system().lower()
        self.is_windows = self.system == "windows"
        
        if self.is_windows:
            # Windows configuration
            self.settings = {
                "workers": 1,
                "loop": None,      # No uvloop
                "http": None,      # No httptools
                "max_workers": 20,
            }
        else:
            # Linux/Mac configuration
            self.settings = {
                "workers": 4,
                "loop": "uvloop",     # Performance optimization
                "http": "httptools",  # Performance optimization
                "max_workers": 50,
            }
```

### **4. 🚀 Installation Methods**

#### **Method 1: PyPI Installation (Recommended)**
```bash
# Windows (default)
pip install face-enhancement-service

# Linux/Mac (with optimizations)
pip install face-enhancement-service[linux]

# Development
pip install face-enhancement-service[dev]
```
#### **Method 2: Manual Platform-Specific**
```bash
# Windows
pip install -r requirements_windows.txt

# Linux/Mac
pip install -r requirements_api.txt
```

#### **Method 3: PyPI with Extras**
```bash
# Windows (default)
pip install face-enhancement-service

# Linux/Mac (optimized)
pip install face-enhancement-service[linux]

# Development
pip install face-enhancement-service[dev]
```

### **5. 🔍 How It Works**

#### **Step 1: Package Installation**
- User runs `pip install face-enhancement-service`
- PyPI downloads the package
- `setup.py` determines platform-specific dependencies

#### **Step 2: Runtime Detection**
- Package imports `src.config`
- `APIConfig` detects the platform
- Sets appropriate configuration

#### **Step 3: Dynamic Configuration**
- Windows: Uses standard Python libraries
- Linux/Mac: Uses optimized libraries (uvloop, httptools)

### **6. 📊 Platform-Specific Features**

#### **Windows:**
- ✅ Single worker configuration
- ✅ Standard event loop
- ✅ Standard HTTP parser
- ✅ Reduced thread pool (20 workers)
- ❌ No uvloop/httptools

#### **Linux/Mac:**
- ✅ Multi-worker configuration (4 workers)
- ✅ uvloop event loop (faster)
- ✅ httptools HTTP parser (faster)
- ✅ Full thread pool (50 workers)
- ✅ All performance optimizations

### **7. 🛠️ Customization**

#### **For Users:**
```bash
# Install with specific extras
pip install face-enhancement-service[linux,dev]

# Install everything
pip install face-enhancement-service[all]
```

#### **For Developers:**
```python
# In setup.py, you can add more platform-specific extras
extras_require={
    "linux": ["uvloop>=0.19.0", "httptools>=0.6.1"],
    "windows": ["pywin32>=300"],  # Windows-specific
    "mac": ["pyobjc>=8.0"],      # macOS-specific
}
```

### **8. 🎯 Benefits**

- ✅ **Automatic Detection**: No manual configuration needed
- ✅ **Performance Optimization**: Platform-specific optimizations
- ✅ **Compatibility**: Works on all platforms
- ✅ **Flexibility**: Users can choose installation method
- ✅ **Maintenance**: Easy to update platform-specific dependencies

### **9. 🔧 Troubleshooting**

#### **If uvloop/httptools fail on Windows:**
```bash
# Install without Linux extras
pip install face-enhancement-service
```

#### **If performance is slow on Linux:**
```bash
# Install with optimizations
pip install face-enhancement-service[linux]
```

#### **For development:**
```bash
# Install with all extras
pip install face-enhancement-service[all]
```

---

## 🎉 Summary

The package automatically handles cross-platform dependencies through:
1. **`extras_require`** for optional platform-specific packages
2. **Multiple requirements files** for different platforms
3. **Runtime detection** for dynamic configuration
4. **Flexible installation methods** for different use cases

This ensures optimal performance on each platform while maintaining compatibility! 🚀
