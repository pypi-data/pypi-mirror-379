# YOLO Circle Detection SDK
# Version: 1.0.0
# Author: Auto-generated SDK

from .detector import YOLOCircleDetector
from .api import CircleDetectionAPI
from .config import Config

__version__ = "1.0.0"
__author__ = "YOLO Circle SDK"
__description__ = "A professional SDK for YOLO-based circle detection with Hough transform"

# 导出主要接口
__all__ = [
    'YOLOCircleDetector',
    'CircleDetectionAPI', 
    'Config'
]