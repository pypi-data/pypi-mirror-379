# 📱 Mobile Integration Guide

Complete guide for integrating the **face-enhancement-service** PyPI package with mobile applications.

## 🚀 Server-Side Deployment

### **1. Install from PyPI**

```bash
# Install the package
pip install face-enhancement-service

# For Linux/Mac (high performance)
pip install face-enhancement-service[linux]

# For Windows
pip install face-enhancement-service
```

### **2. Start the Server**

#### **Option A: Simple Launch (Recommended)**
```bash
# Automatic platform detection and configuration
python -c "from face_enhancement_service import app; import uvicorn; uvicorn.run(app, host='0.0.0.0', port=8000)"
```

#### **Option B: Using Launch Script**
```bash
# If you have the source code
python launch.py
```

#### **Option C: Direct FastAPI**
```bash
# Using uvicorn directly
uvicorn face_enhancement_service.src.face_enhancer_api:app --host 0.0.0.0 --port 8000
```

### **3. Verify Server is Running**

```bash
# Health check
curl http://localhost:8000/health

# API documentation
open http://localhost:8000/docs
```

## 📱 Mobile App Integration

### **REST API Endpoints**

The server exposes these endpoints for mobile integration:

#### **Base URL**: `http://your-server-ip:8000`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Server health check |
| `/enhance` | POST | Enhance face image |
| `/auth/token` | POST | Get authentication token |
| `/protected/enhance` | POST | Enhanced face with auth |
| `/rate-limit` | GET | Check rate limit status |

### **Authentication**

#### **Get Token**
```bash
curl -X POST "http://your-server-ip:8000/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=your_username&password=your_password"
```

#### **Use Token**
```bash
curl -X POST "http://your-server-ip:8000/protected/enhance" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"image": "base64_image", "config": {...}}'
```

## 🔧 Mobile Implementation Examples

### **iOS (Swift)**

```swift
import Foundation
import UIKit

class FaceEnhancementService {
    private let baseURL = "http://your-server-ip:8000"
    private var authToken: String?
    
    // Get authentication token
    func authenticate(username: String, password: String, completion: @escaping (Bool) -> Void) {
        let url = URL(string: "\(baseURL)/auth/token")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
        
        let body = "username=\(username)&password=\(password)"
        request.httpBody = body.data(using: .utf8)
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let data = data,
               let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
               let token = json["access_token"] as? String {
                self.authToken = token
                completion(true)
            } else {
                completion(false)
            }
        }.resume()
    }
    
    // Enhance face image
    func enhanceFace(image: UIImage, config: [String: Double], completion: @escaping (UIImage?) -> Void) {
        guard let imageData = image.jpegData(compressionQuality: 0.8) else {
            completion(nil)
            return
        }
        
        let base64Image = imageData.base64EncodedString()
        let url = URL(string: "\(baseURL)/enhance")!
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        if let token = authToken {
            request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        }
        
        let requestBody: [String: Any] = [
            "image": base64Image,
            "config": config
        ]
        
        request.httpBody = try? JSONSerialization.data(withJSONObject: requestBody)
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let data = data,
               let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
               let enhancedImageBase64 = json["enhanced_image"] as? String,
               let imageData = Data(base64Encoded: enhancedImageBase64),
               let enhancedImage = UIImage(data: imageData) {
                DispatchQueue.main.async {
                    completion(enhancedImage)
                }
            } else {
                DispatchQueue.main.async {
                    completion(nil)
                }
            }
        }.resume()
    }
}

// Usage
let service = FaceEnhancementService()
service.authenticate(username: "user", password: "pass") { success in
    if success {
        service.enhanceFace(image: originalImage, config: [
            "smoothing": 0.8,
            "brightness": 0.5,
            "whiteness": 0.3,
            "acne_removal": 0.7,
            "under_eye_brightening": 0.6,
            "soft_focus": 0.4,
            "virtual_contouring": 0.5,
            "color_temperature": 0.2
        ]) { enhancedImage in
            // Use enhanced image
        }
    }
}
```

### **Android (Kotlin)**

```kotlin
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.util.Base64
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.io.ByteArrayOutputStream

class FaceEnhancementService {
    private val baseURL = "http://your-server-ip:8000"
    private val client = OkHttpClient()
    private var authToken: String? = null
    
    // Get authentication token
    suspend fun authenticate(username: String, password: String): Boolean = withContext(Dispatchers.IO) {
        try {
            val requestBody = FormBody.Builder()
                .add("username", username)
                .add("password", password)
                .build()
            
            val request = Request.Builder()
                .url("$baseURL/auth/token")
                .post(requestBody)
                .build()
            
            val response = client.newCall(request).execute()
            val responseBody = response.body?.string()
            
            if (response.isSuccessful && responseBody != null) {
                val json = JSONObject(responseBody)
                authToken = json.getString("access_token")
                true
            } else {
                false
            }
        } catch (e: Exception) {
            false
        }
    }
    
    // Enhance face image
    suspend fun enhanceFace(bitmap: Bitmap, config: Map<String, Double>): Bitmap? = withContext(Dispatchers.IO) {
        try {
            val base64Image = bitmapToBase64(bitmap)
            
            val requestBody = JSONObject().apply {
                put("image", base64Image)
                put("config", JSONObject(config))
            }.toString()
            
            val request = Request.Builder()
                .url("$baseURL/enhance")
                .post(requestBody.toRequestBody("application/json".toMediaType()))
                .apply {
                    authToken?.let { token ->
                        addHeader("Authorization", "Bearer $token")
                    }
                }
                .build()
            
            val response = client.newCall(request).execute()
            val responseBody = response.body?.string()
            
            if (response.isSuccessful && responseBody != null) {
                val json = JSONObject(responseBody)
                val enhancedImageBase64 = json.getString("enhanced_image")
                base64ToBitmap(enhancedImageBase64)
            } else {
                null
            }
        } catch (e: Exception) {
            null
        }
    }
    
    private fun bitmapToBase64(bitmap: Bitmap): String {
        val outputStream = ByteArrayOutputStream()
        bitmap.compress(Bitmap.CompressFormat.JPEG, 80, outputStream)
        val byteArray = outputStream.toByteArray()
        return Base64.encodeToString(byteArray, Base64.DEFAULT)
    }
    
    private fun base64ToBitmap(base64: String): Bitmap? {
        val decodedBytes = Base64.decode(base64, Base64.DEFAULT)
        return BitmapFactory.decodeByteArray(decodedBytes, 0, decodedBytes.size)
    }
}

// Usage
class MainActivity : AppCompatActivity() {
    private val service = FaceEnhancementService()
    
    private fun enhanceImage(originalBitmap: Bitmap) {
        lifecycleScope.launch {
            val success = service.authenticate("user", "pass")
            if (success) {
                val enhancedBitmap = service.enhanceFace(originalBitmap, mapOf(
                    "smoothing" to 0.8,
                    "brightness" to 0.5,
                    "whiteness" to 0.3,
                    "acne_removal" to 0.7,
                    "under_eye_brightening" to 0.6,
                    "soft_focus" to 0.4,
                    "virtual_contouring" to 0.5,
                    "color_temperature" to 0.2
                ))
                
                enhancedBitmap?.let { bitmap ->
                    // Use enhanced bitmap
                    runOnUiThread {
                        imageView.setImageBitmap(bitmap)
                    }
                }
            }
        }
    }
}
```

### **React Native (JavaScript)**

```javascript
import { Platform } from 'react-native';

class FaceEnhancementService {
    constructor(serverUrl = 'http://your-server-ip:8000') {
        this.baseURL = serverUrl;
        this.authToken = null;
    }
    
    // Get authentication token
    async authenticate(username, password) {
        try {
            const formData = new FormData();
            formData.append('username', username);
            formData.append('password', password);
            
            const response = await fetch(`${this.baseURL}/auth/token`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `username=${username}&password=${password}`,
            });
            
            if (response.ok) {
                const data = await response.json();
                this.authToken = data.access_token;
                return true;
            }
            return false;
        } catch (error) {
            console.error('Authentication failed:', error);
            return false;
        }
    }
    
    // Convert image to base64
    imageToBase64(imageUri) {
        return new Promise((resolve, reject) => {
            const xhr = new XMLHttpRequest();
            xhr.onload = function() {
                const reader = new FileReader();
                reader.onloadend = function() {
                    resolve(reader.result.split(',')[1]); // Remove data:image/jpeg;base64, prefix
                };
                reader.readAsDataURL(xhr.response);
            };
            xhr.onerror = reject;
            xhr.open('GET', imageUri);
            xhr.responseType = 'blob';
            xhr.send();
        });
    }
    
    // Enhance face image
    async enhanceFace(imageUri, config) {
        try {
            const base64Image = await this.imageToBase64(imageUri);
            
            const requestBody = {
                image: base64Image,
                config: config
            };
            
            const headers = {
                'Content-Type': 'application/json',
            };
            
            if (this.authToken) {
                headers['Authorization'] = `Bearer ${this.authToken}`;
            }
            
            const response = await fetch(`${this.baseURL}/enhance`, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify(requestBody),
            });
            
            if (response.ok) {
                const data = await response.json();
                return `data:image/jpeg;base64,${data.enhanced_image}`;
            }
            return null;
        } catch (error) {
            console.error('Enhancement failed:', error);
            return null;
        }
    }
}

// Usage
const service = new FaceEnhancementService();

const enhanceImage = async (imageUri) => {
    const success = await service.authenticate('user', 'pass');
    if (success) {
        const enhancedImageUri = await service.enhanceFace(imageUri, {
            smoothing: 0.8,
            brightness: 0.5,
            whiteness: 0.3,
            acne_removal: 0.7,
            under_eye_brightening: 0.6,
            soft_focus: 0.4,
            virtual_contouring: 0.5,
            color_temperature: 0.2
        });
        
        if (enhancedImageUri) {
            // Use enhanced image
            setImage(enhancedImageUri);
        }
    }
};
```

## 🔧 Configuration Options

### **Enhancement Parameters**

| Parameter | Range | Description |
|-----------|-------|-------------|
| `smoothing` | 0.0 - 1.0 | Skin smoothing intensity |
| `brightness` | 0.0 - 1.0 | Overall brightness adjustment |
| `whiteness` | 0.0 - 1.0 | Skin whitening effect |
| `acne_removal` | 0.0 - 1.0 | Acne and blemish removal |
| `under_eye_brightening` | 0.0 - 1.0 | Under-eye dark circle reduction |
| `soft_focus` | 0.0 - 1.0 | Soft focus effect |
| `virtual_contouring` | 0.0 - 1.0 | Face contouring enhancement |
| `color_temperature` | 0.0 - 1.0 | Color temperature adjustment |

### **Server Configuration**

#### **Production Deployment**
```bash
# For high-traffic production servers
pip install face-enhancement-service[linux]
uvicorn face_enhancement_service.src.face_enhancer_api:app \
  --host 0.0.0.0 \
  --port 8000 \
  --workers 4 \
  --loop uvloop \
  --http httptools
```

#### **Development/Testing**
```bash
# For development and testing
pip install face-enhancement-service
uvicorn face_enhancement_service.src.face_enhancer_api:app \
  --host 0.0.0.0 \
  --port 8000 \
  --reload
```

## 🚀 Deployment Options

### **1. Cloud Deployment**

#### **AWS EC2**
```bash
# Install on EC2 instance
pip install face-enhancement-service[linux]

# Start with systemd
sudo systemctl enable face-enhancement-service
sudo systemctl start face-enhancement-service
```

#### **Google Cloud Run**
```dockerfile
FROM python:3.9-slim
RUN pip install face-enhancement-service
CMD ["uvicorn", "face_enhancement_service.src.face_enhancer_api:app", "--host", "0.0.0.0", "--port", "8080"]
```

#### **Azure Container Instances**
```bash
# Deploy container
az container create \
  --resource-group myResourceGroup \
  --name face-enhancement-api \
  --image python:3.9-slim \
  --command-line "pip install face-enhancement-service && uvicorn face_enhancement_service.src.face_enhancer_api:app --host 0.0.0.0 --port 8000"
```

### **2. Docker Deployment**

```dockerfile
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python package
RUN pip install face-enhancement-service

# Expose port
EXPOSE 8000

# Start the API
CMD ["uvicorn", "face_enhancement_service.src.face_enhancer_api:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build and run
docker build -t face-enhancement-api .
docker run -p 8000:8000 face-enhancement-api
```

## 📊 Performance Optimization

### **Mobile App Best Practices**

1. **Image Compression**: Compress images before sending (JPEG quality 80-90%)
2. **Caching**: Cache enhanced images locally
3. **Background Processing**: Use background threads for API calls
4. **Error Handling**: Implement proper error handling and retry logic
5. **Progress Indicators**: Show loading states during processing

### **Server Optimization**

1. **Load Balancing**: Use multiple server instances
2. **CDN**: Serve static assets through CDN
3. **Caching**: Implement Redis caching for frequent requests
4. **Monitoring**: Monitor server performance and health

## 🔒 Security Considerations

1. **HTTPS**: Always use HTTPS in production
2. **Authentication**: Implement proper user authentication
3. **Rate Limiting**: Respect server rate limits
4. **Input Validation**: Validate images and parameters
5. **Error Handling**: Don't expose sensitive information in errors

## 📞 Support

- **API Documentation**: `http://your-server-ip:8000/docs`
- **Health Check**: `http://your-server-ip:8000/health`
- **Rate Limit Status**: `http://your-server-ip:8000/rate-limit`
- **GitHub Issues**: https://github.com/livlyv/face-enhancement-service/issues

---

**Ready to enhance faces in your mobile app! 🚀📱**
