"""
Face Enhancement API Package
Cross-platform REST API for real-time face enhancement
"""

from .face_enhancer_api import app, FaceEnhancerConfig, EnhancementRequest, EnhancementResponse
from .face_enhancer_client import FaceEnhancerClient, EnhancementConfig
from .config import config, APIConfig

__version__ = "1.0.0"
__author__ = "Face Enhancement Team"
__email__ = "info@livlyv.com"
__description__ = "High-performance REST API for real-time face enhancement"

__all__ = [
    "app",
    "FaceEnhancerConfig", 
    "EnhancementRequest",
    "EnhancementResponse",
    "FaceEnhancerClient",
    "EnhancementConfig",
    "config",
    "APIConfig"
]
