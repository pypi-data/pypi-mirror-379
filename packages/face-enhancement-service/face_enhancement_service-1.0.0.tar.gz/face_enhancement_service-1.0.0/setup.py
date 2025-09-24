"""
Face Enhancement API Package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements_windows.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="face-enhancement-service",
    version="1.0.0",
    author="Face Enhancement Team",
    author_email="info@livlyv.com",
    description="High-performance REST API for real-time face enhancement",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/livlyv/face-enhancement-service",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
        "linux": [
            "uvloop>=0.19.0",
            "httptools>=0.6.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "face-enhancement-service=src.face_enhancer_api:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.yml", "*.yaml", "*.conf"],
    },
    keywords=[
        "face-enhancement",
        "rest-api",
        "fastapi",
        "computer-vision",
        "opencv",
        "mediapipe",
        "beauty-filter",
        "skin-smoothing",
        "real-time",
    ],
    project_urls={
        "Bug Reports": "https://github.com/livlyv/face-enhancement-service/issues",
        "Source": "https://github.com/livlyv/face-enhancement-service",
        "Documentation": "https://github.com/livlyv/face-enhancement-service#readme",
    },
)
