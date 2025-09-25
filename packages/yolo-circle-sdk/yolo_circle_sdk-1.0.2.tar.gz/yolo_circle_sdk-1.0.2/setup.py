#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YOLO Circle Detection SDK
一个专业的YOLO圆形检测SDK，结合YOLO物体检测和霍夫圆检测
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取README文件
this_directory = Path(__file__).parent
long_description = ""
try:
    long_description = (this_directory / "README.md").read_text(encoding='utf-8')
except FileNotFoundError:
    long_description = "YOLO Circle Detection SDK - 专业的圆形检测解决方案"

# 读取requirements
requirements = []
try:
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
except FileNotFoundError:
    requirements = [
        'opencv-python>=4.5.0',
        'numpy>=1.21.0',
        'ultralytics>=8.0.0',
        'matplotlib>=3.5.0'
    ]

setup(
    name="yolo-circle-sdk",
    version="1.0.2",
    author="YOLO Circle SDK Team",
    author_email="support@yolo-circle-sdk.com",
    description="专业的YOLO圆形检测SDK，结合YOLO物体检测和霍夫圆检测",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/yolo-circle-sdk",
    project_urls={
        "Bug Tracker": "https://github.com/your-org/yolo-circle-sdk/issues",
        "Documentation": "https://yolo-circle-sdk.readthedocs.io/",
        "Source Code": "https://github.com/your-org/yolo-circle-sdk",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.15",
        ],
        "yaml": [
            "PyYAML>=5.4",
        ],
    },
    entry_points={
        "console_scripts": [
            "yolo-circle-detect=yolo_circle_sdk.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "yolo_circle_sdk": [
            "*.md",
            "*.txt",
            "*.yml",
            "*.yaml",
            "models/*.pt",  # 包含模型文件
        ],
    },
    zip_safe=False,
    keywords=[
        "yolo", "circle detection", "computer vision", "object detection", 
        "hough transform", "image processing", "ai", "machine learning"
    ],
)