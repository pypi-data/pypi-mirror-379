"""
Face Enhancement SDK Client
Easy-to-use Python client for the Face Enhancement API
"""

import base64
import requests
import time
from typing import Optional, Dict, Any
from dataclasses import dataclass
import cv2
import numpy as np

@dataclass
class EnhancementConfig:
    """Configuration for face enhancement"""
    smoothing: float = 0.6
    brightness: float = 0.3
    whiteness: float = 0.4
    acne_removal: float = 0.7
    under_eye_brightening: float = 0.0
    soft_focus: float = 0.0
    virtual_contouring: float = 0.0
    color_temperature: float = 0.0
    texture_preservation: float = 0.8

class FaceEnhancerClient:
    """Client for Face Enhancement API"""
    
    def __init__(self, base_url: str = "http://localhost:8000", api_key: Optional[str] = None):
        """
        Initialize the client
        
        Args:
            base_url: API base URL
            api_key: Optional API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        
        # Set default headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'FaceEnhancerSDK/1.0.0'
        })
        
        if api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}'
            })
    
    def health_check(self) -> Dict[str, Any]:
        """Check API health"""
        response = self.session.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()
    
    def enhance_image(self, image_path: str, config: Optional[EnhancementConfig] = None) -> str:
        """
        Enhance an image from file path
        
        Args:
            image_path: Path to the image file
            config: Enhancement configuration
            
        Returns:
            Base64 encoded enhanced image
        """
        # Read and encode image
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        return self.enhance_image_base64(image_base64, config)
    
    def enhance_image_base64(self, image_base64: str, config: Optional[EnhancementConfig] = None) -> str:
        """
        Enhance an image from base64 string
        
        Args:
            image_base64: Base64 encoded image
            config: Enhancement configuration
            
        Returns:
            Base64 encoded enhanced image
        """
        if config is None:
            config = EnhancementConfig()
        
        # Prepare request
        request_data = {
            "image": image_base64,
            "config": {
                "smoothing": config.smoothing,
                "brightness": config.brightness,
                "whiteness": config.whiteness,
                "acne_removal": config.acne_removal,
                "under_eye_brightening": config.under_eye_brightening,
                "soft_focus": config.soft_focus,
                "virtual_contouring": config.virtual_contouring,
                "color_temperature": config.color_temperature,
                "texture_preservation": config.texture_preservation
            }
        }
        
        # Make request
        response = self.session.post(f"{self.base_url}/enhance", json=request_data)
        response.raise_for_status()
        
        result = response.json()
        if not result['success']:
            raise Exception(f"Enhancement failed: {result.get('message', 'Unknown error')}")
        
        return result['enhanced_image']
    
    def enhance_cv2_image(self, image: np.ndarray, config: Optional[EnhancementConfig] = None) -> np.ndarray:
        """
        Enhance an OpenCV image
        
        Args:
            image: OpenCV image (numpy array)
            config: Enhancement configuration
            
        Returns:
            Enhanced OpenCV image
        """
        # Encode image
        _, buffer = cv2.imencode('.jpg', image)
        image_base64 = base64.b64encode(buffer).decode('utf-8')
        
        # Enhance
        enhanced_base64 = self.enhance_image_base64(image_base64, config)
        
        # Decode enhanced image
        enhanced_data = base64.b64decode(enhanced_base64)
        enhanced_array = np.frombuffer(enhanced_data, dtype=np.uint8)
        enhanced_image = cv2.imdecode(enhanced_array, cv2.IMREAD_COLOR)
        
        return enhanced_image
    
    def get_rate_limit_status(self) -> Dict[str, Any]:
        """Get rate limit status"""
        response = self.session.get(f"{self.base_url}/rate-limit")
        response.raise_for_status()
        return response.json()
    
    def authenticate(self, username: str, password: str) -> str:
        """
        Authenticate and get API key
        
        Args:
            username: Username
            password: Password
            
        Returns:
            API key
        """
        response = self.session.post(
            f"{self.base_url}/auth/token",
            data={"username": username, "password": password}
        )
        response.raise_for_status()
        
        result = response.json()
        api_key = result['access_token']
        
        # Update session with new API key
        self.api_key = api_key
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}'
        })
        
        return api_key

# Convenience functions
def enhance_image(image_path: str, base_url: str = "http://localhost:8000", **kwargs) -> str:
    """
    Quick function to enhance an image
    
    Args:
        image_path: Path to the image file
        base_url: API base URL
        **kwargs: Enhancement parameters
        
    Returns:
        Base64 encoded enhanced image
    """
    client = FaceEnhancerClient(base_url)
    config = EnhancementConfig(**kwargs)
    return client.enhance_image(image_path, config)

def enhance_cv2_image(image: np.ndarray, base_url: str = "http://localhost:8000", **kwargs) -> np.ndarray:
    """
    Quick function to enhance an OpenCV image
    
    Args:
        image: OpenCV image (numpy array)
        base_url: API base URL
        **kwargs: Enhancement parameters
        
    Returns:
        Enhanced OpenCV image
    """
    client = FaceEnhancerClient(base_url)
    config = EnhancementConfig(**kwargs)
    return client.enhance_cv2_image(image, config)

# Example usage
if __name__ == "__main__":
    # Example 1: Enhance image from file
    client = FaceEnhancerClient("http://localhost:8000")
    
    # Check health
    health = client.health_check()
    print(f"API Health: {health}")
    
    # Enhance image
    config = EnhancementConfig(
        smoothing=0.8,
        brightness=0.5,
        whiteness=0.3
    )
    
    try:
        enhanced_image = client.enhance_image("input.jpg", config)
        
        # Save enhanced image
        with open("enhanced.jpg", "wb") as f:
            f.write(base64.b64decode(enhanced_image))
        
        print("Image enhanced successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Quick enhancement
    try:
        enhanced = enhance_image("input.jpg", smoothing=0.7, brightness=0.4)
        print("Quick enhancement completed!")
    except Exception as e:
        print(f"Quick enhancement failed: {e}")
