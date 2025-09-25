"""高级API接口模块

提供简洁易用的函数式接口，隐藏底层复杂性
"""

import cv2
import numpy as np
from pathlib import Path
from typing import Union, Optional, Dict, Any, List, Tuple

from .detector import YOLOCircleDetector, DetectionResult
from .config import Config, default_config
from .model_manager import ModelManager


class CircleDetectionAPI:
    """圆形检测API类
    
    提供高级接口，简化SDK的使用
    """
    
    def __init__(self, model_name: str = 'best1.pt', 
                 model_path: Optional[str] = None,
                 config: Optional[Union[Config, Dict, str]] = None):
        """初始化API
        
        Args:
            model_name: 模型名称
            model_path: 模型文件路径（用于首次安装）
            config: 配置对象、配置字典或配置文件路径
        """
        # 处理配置
        if config is None:
            self.config = default_config
        elif isinstance(config, Config):
            self.config = config
        elif isinstance(config, dict):
            self.config = Config()
            self.config.update(config)
        elif isinstance(config, str):
            self.config = Config()
            self.config.load_from_file(config)
        else:
            raise ValueError("config参数必须是Config对象、字典或文件路径")
        
        # 初始化检测器
        self.detector = YOLOCircleDetector(model_name, model_path, self.config)
        self.model_manager = self.detector.model_manager
    
    def detect(self, image: Union[str, np.ndarray], 
               conf_threshold: Optional[float] = None,
               save_result: bool = False,
               result_path: Optional[str] = None,
               **kwargs) -> DetectionResult:
        """检测图像中的圆形
        
        Args:
            image: 图像路径或numpy数组
            conf_threshold: YOLO置信度阈值
            save_result: 是否保存可视化结果
            result_path: 结果保存路径
            **kwargs: 其他检测参数
            
        Returns:
            DetectionResult对象
        """
        # 执行检测
        result = self.detector.process_image(image, conf_threshold=conf_threshold, **kwargs)
        
        # 保存可视化结果
        if save_result:
            if result_path is None:
                if isinstance(image, str):
                    base_name = Path(image).stem
                    result_path = f"{base_name}_detection_result.jpg"
                else:
                    result_path = "detection_result.jpg"
            
            self.detector.visualize_results(image, result, result_path)
        
        return result
    
    def detect_batch(self, images: List[Union[str, np.ndarray]], 
                    **kwargs) -> List[DetectionResult]:
        """批量检测多张图像
        
        Args:
            images: 图像路径或数组列表
            **kwargs: 检测参数
            
        Returns:
            检测结果列表
        """
        results = []
        for i, image in enumerate(images):
            print(f"\n处理第 {i+1}/{len(images)} 张图像")
            try:
                result = self.detect(image, **kwargs)
                results.append(result)
            except Exception as e:
                print(f"处理图像失败: {e}")
                results.append(None)
        
        return results
    
    def install_model(self, model_path: str, model_name: Optional[str] = None) -> str:
        """安装新的模型文件
        
        Args:
            model_path: 模型文件路径
            model_name: 目标模型名称
            
        Returns:
            安装后的模型路径
        """
        return self.model_manager.install_model(model_path, model_name)
    
    def list_models(self) -> Dict[str, Any]:
        """列出所有可用模型
        
        Returns:
            模型信息字典
        """
        return self.model_manager.list_models()
    
    def get_config(self) -> Dict[str, Any]:
        """获取当前配置
        
        Returns:
            配置字典
        """
        return self.config.to_dict()
    
    def update_config(self, config_updates: Dict[str, Any]):
        """更新配置
        
        Args:
            config_updates: 配置更新字典
        """
        self.config.update(config_updates)


# 全局API实例（延迟初始化）
_global_api = None


def get_api(model_name: str = 'best1.pt', 
           model_path: Optional[str] = None,
           config: Optional[Union[Config, Dict, str]] = None) -> CircleDetectionAPI:
    """获取全局API实例
    
    Args:
        model_name: 模型名称
        model_path: 模型文件路径
        config: 配置
        
    Returns:
        CircleDetectionAPI实例
    """
    global _global_api
    if _global_api is None:
        _global_api = CircleDetectionAPI(model_name, model_path, config)
    return _global_api


# 便捷函数接口
def detect_circles(image: Union[str, np.ndarray], 
                  model_name: str = 'best1.pt',
                  model_path: Optional[str] = None,
                  conf_threshold: Optional[float] = None,
                  save_result: bool = False,
                  result_path: Optional[str] = None,
                  **kwargs) -> DetectionResult:
    """检测图像中的圆形（便捷函数）
    
    Args:
        image: 图像路径或numpy数组
        model_name: 模型名称
        model_path: 模型文件路径（首次使用时需要）
        conf_threshold: YOLO置信度阈值
        save_result: 是否保存可视化结果
        result_path: 结果保存路径
        **kwargs: 其他检测参数
        
    Returns:
        DetectionResult对象
        
    Example:
        >>> result = detect_circles('image.jpg', save_result=True)
        >>> print(f"检测到 {result.circle_count} 个圆形")
    """
    api = get_api(model_name, model_path)
    return api.detect(image, conf_threshold, save_result, result_path, **kwargs)


def detect_circles_batch(images: List[Union[str, np.ndarray]], 
                        model_name: str = 'best1.pt',
                        model_path: Optional[str] = None,
                        **kwargs) -> List[DetectionResult]:
    """批量检测多张图像中的圆形（便捷函数）
    
    Args:
        images: 图像路径或数组列表
        model_name: 模型名称
        model_path: 模型文件路径
        **kwargs: 检测参数
        
    Returns:
        检测结果列表
        
    Example:
        >>> images = ['img1.jpg', 'img2.jpg', 'img3.jpg']
        >>> results = detect_circles_batch(images, save_result=True)
        >>> total_circles = sum(r.circle_count for r in results if r)
    """
    api = get_api(model_name, model_path)
    return api.detect_batch(images, **kwargs)


def install_model(model_path: str, model_name: Optional[str] = None) -> str:
    """安装模型文件（便捷函数）
    
    Args:
        model_path: 模型文件路径
        model_name: 目标模型名称
        
    Returns:
        安装后的模型路径
        
    Example:
        >>> install_model('/path/to/my_model.pt', 'my_model.pt')
    """
    api = get_api()
    return api.install_model(model_path, model_name)


def list_models() -> Dict[str, Any]:
    """列出所有可用模型（便捷函数）
    
    Returns:
        模型信息字典
        
    Example:
        >>> models = list_models()
        >>> for name, info in models.items():
        ...     print(f"{name}: {info['size']}")
    """
    api = get_api()
    return api.list_models()


def set_config(config_updates: Dict[str, Any]):
    """更新全局配置（便捷函数）
    
    Args:
        config_updates: 配置更新字典
        
    Example:
        >>> set_config({
        ...     'yolo.conf_threshold': 0.7,
        ...     'hough_circle.min_radius': 5
        ... })
    """
    api = get_api()
    api.update_config(config_updates)


def get_config() -> Dict[str, Any]:
    """获取当前全局配置（便捷函数）
    
    Returns:
        配置字典
        
    Example:
        >>> config = get_config()
        >>> print(config['yolo']['conf_threshold'])
    """
    api = get_api()
    return api.get_config()


# 向后兼容的别名
detect = detect_circles
detect_batch = detect_circles_batch