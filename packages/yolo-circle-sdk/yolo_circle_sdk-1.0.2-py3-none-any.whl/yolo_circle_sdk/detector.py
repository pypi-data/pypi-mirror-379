"""YOLO圆形检测器核心模块"""

import cv2
import numpy as np
from ultralytics import YOLO
import time
from pathlib import Path
from typing import List, Tuple, Optional, Union, Dict, Any

from .config import Config, default_config
from .model_manager import ModelManager


class DetectionResult:
    """检测结果数据类"""
    
    def __init__(self, yolo_detections: List[Tuple], circle_results: List[Tuple], 
                 processing_time: float, image_shape: Tuple[int, int, int]):
        self.yolo_detections = yolo_detections
        self.circle_results = circle_results
        self.processing_time = processing_time
        self.image_shape = image_shape
        
        # 统计信息
        self.object_count = len(yolo_detections)
        self.circle_count = sum(len(circles) for _, circles in circle_results)
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            'yolo_detections': self.yolo_detections,
            'circle_results': self.circle_results,
            'processing_time': self.processing_time,
            'image_shape': self.image_shape,
            'object_count': self.object_count,
            'circle_count': self.circle_count
        }


class YOLOCircleDetector:
    """YOLO圆形检测器
    
    结合YOLO物体检测和霍夫圆检测的专业检测器，
    支持在YOLO检测区域内进行精确的圆形检测。
    """
    
    def __init__(self, model_name: str = 'best1.pt', 
                 model_path: Optional[str] = None,
                 config: Optional[Config] = None):
        """初始化检测器
        
        Args:
            model_name: 模型名称
            model_path: 模型文件路径（用于首次安装）
            config: 配置对象，如果为None则使用默认配置
        """
        self.config = config or default_config
        self.model_manager = ModelManager(self.config.get('yolo.model_cache_dir'))
        self.yolo_model = None
        self._load_model(model_name, model_path)
    
    def _load_model(self, model_name: str, model_path: Optional[str] = None):
        """加载YOLO模型
        
        Args:
            model_name: 模型名称
            model_path: 模型文件路径
        """
        try:
            # 获取模型路径
            actual_model_path = self.model_manager.get_model_path(model_name, model_path)
            
            print(f"正在加载YOLO模型: {actual_model_path}")
            self.yolo_model = YOLO(actual_model_path)
            print("YOLO模型加载成功")
            
        except Exception as e:
            print(f"YOLO模型加载失败: {e}")
            self.yolo_model = None
            raise RuntimeError(f"无法加载YOLO模型: {e}")
    
    def detect_objects_with_yolo(self, image: np.ndarray, 
                                conf_threshold: Optional[float] = None) -> List[Tuple]:
        """使用YOLO模型检测图像中的物体
        
        Args:
            image: 输入图像 (numpy数组)
            conf_threshold: 置信度阈值，如果为None则使用配置中的值
            
        Returns:
            检测结果列表，每个元素包含 (x1, y1, x2, y2, conf, class_id)
        """
        if self.yolo_model is None:
            raise RuntimeError("YOLO模型未加载")
        
        if conf_threshold is None:
            conf_threshold = self.config.get('yolo.conf_threshold', 0.5)
        
        print(f"\n=== YOLO物体检测 ===")
        print(f"输入图像尺寸: {image.shape}")
        print(f"置信度阈值: {conf_threshold}")
        
        try:
            # 进行推理
            yolo_start = time.time()
            results = self.yolo_model(image, conf=conf_threshold, verbose=False)
            inference_time = time.time() - yolo_start
            print(f"  YOLO推理耗时: {inference_time:.3f}秒")
            
            detections = []
            
            # 处理检测结果
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        # 获取边界框坐标
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        conf = box.conf[0].cpu().numpy()
                        class_id = int(box.cls[0].cpu().numpy())
                        
                        detections.append((int(x1), int(y1), int(x2), int(y2), float(conf), class_id))
            
            print(f"检测完成，用时: {inference_time:.3f}秒")
            print(f"检测到 {len(detections)} 个物体")
            
            # 显示检测结果详情
            for i, (x1, y1, x2, y2, conf, class_id) in enumerate(detections):
                w, h = x2 - x1, y2 - y1
                print(f"  物体 {i+1}: 位置({x1}, {y1}, {x2}, {y2}), 尺寸({w}x{h}), 置信度: {conf:.3f}, 类别: {class_id}")
            
            return detections
            
        except Exception as e:
            print(f"YOLO检测过程中出现错误: {e}")
            raise RuntimeError(f"YOLO检测失败: {e}")
    
    def detect_circles_in_region(self, image: np.ndarray, x1: int, y1: int, x2: int, y2: int,
                                **kwargs) -> List[Tuple[int, int, int]]:
        """在指定区域内检测圆形
        
        Args:
            image: 输入图像
            x1, y1, x2, y2: 检测区域边界框
            **kwargs: 霍夫圆检测参数，会覆盖配置中的默认值
            
        Returns:
            检测到的圆形列表，每个元素包含 (center_x, center_y, radius)
        """
        # 合并配置参数和传入参数
        hough_config = self.config.get('hough_circle', {})
        binary_config = self.config.get('binarization', {})
        
        params = {
            'dp': kwargs.get('dp', hough_config.get('dp', 1)),
            'min_dist': kwargs.get('min_dist', hough_config.get('min_dist', 15)),
            'param1': kwargs.get('param1', hough_config.get('param1', 15)),
            'param2': kwargs.get('param2', hough_config.get('param2', 8)),
            'min_radius': kwargs.get('min_radius', hough_config.get('min_radius', 3)),
            'max_radius': kwargs.get('max_radius', hough_config.get('max_radius', 50)),
            'binary_method': kwargs.get('binary_method', binary_config.get('method', 'adaptive'))
        }
        
        print(f"\n--- 在区域 ({x1}, {y1}, {x2}, {y2}) 内检测圆形 ---")
        
        # 确保边界框在图像范围内
        h, w = image.shape[:2]
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(w, x2)
        y2 = min(h, y2)
        
        # 提取感兴趣区域
        roi = image[y1:y2, x1:x2]
        
        if roi.size == 0:
            print("区域为空，跳过圆形检测")
            return []
        
        print(f"ROI尺寸: {roi.shape}")
        
        # 转换为灰度图像
        if len(roi.shape) == 3:
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        else:
            gray_roi = roi.copy()
        
        # 应用高斯模糊减少噪声
        blurred = cv2.GaussianBlur(gray_roi, (5, 5), 1)
        
        # 二值化处理
        binary = self._apply_binarization(blurred, params['binary_method'])
        
        # 使用霍夫圆检测
        circles = cv2.HoughCircles(
            binary,
            cv2.HOUGH_GRADIENT,
            dp=params['dp'],
            minDist=params['min_dist'],
            param1=params['param1'],
            param2=params['param2'],
            minRadius=params['min_radius'],
            maxRadius=params['max_radius']
        )
        
        detected_circles = []
        
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            
            for (cx, cy, r) in circles:
                # 将相对坐标转换为绝对坐标
                abs_cx = cx + x1
                abs_cy = cy + y1
                detected_circles.append((abs_cx, abs_cy, r))
            
            print(f"检测到 {len(detected_circles)} 个圆形")
            for i, (cx, cy, r) in enumerate(detected_circles):
                print(f"  圆形 {i+1}: 中心({cx}, {cy}), 半径: {r}")
        else:
            print("未检测到圆形")
        
        return detected_circles
    
    def _apply_binarization(self, gray_image: np.ndarray, method: str = 'adaptive') -> np.ndarray:
        """对灰度图像应用二值化
        
        Args:
            gray_image: 输入的灰度图像
            method: 二值化方法
            
        Returns:
            二值化后的图像
        """
        if method == 'adaptive':
            binary = cv2.adaptiveThreshold(
                gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                cv2.THRESH_BINARY, 11, 2
            )
            print("使用自适应阈值二值化")
        elif method == 'otsu':
            _, binary = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            print("使用OTSU阈值二值化")
        elif method == 'manual':
            threshold = self.config.get('binarization.manual_threshold', 200)
            _, binary = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
            print(f"使用手动阈值二值化 (阈值={threshold})")
        else:
            # 默认使用自适应阈值
            binary = cv2.adaptiveThreshold(
                gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                cv2.THRESH_BINARY, 11, 2
            )
            print("使用默认自适应阈值二值化")
        
        # 形态学操作优化
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        
        return binary
    
    def process_image(self, image: Union[str, np.ndarray], **kwargs) -> DetectionResult:
        """处理图像：YOLO检测 + 圆形检测
        
        Args:
            image: 图像路径或numpy数组
            **kwargs: 其他参数
            
        Returns:
            DetectionResult对象
        """
        start_time = time.time()
        
        # 读取图像
        if isinstance(image, str):
            image_array = cv2.imread(image)
            if image_array is None:
                raise ValueError(f"无法读取图像: {image}")
            print(f"\n{'='*80}")
            print(f"处理图像: {image}")
            print(f"{'='*80}")
        else:
            image_array = image
            print(f"\n{'='*80}")
            print(f"处理图像数组")
            print(f"{'='*80}")
        
        print(f"图像尺寸: {image_array.shape}")
        
        # 步骤1: YOLO物体检测
        conf_threshold = kwargs.get('conf_threshold')
        yolo_detections = self.detect_objects_with_yolo(image_array, conf_threshold)
        
        # 步骤2: 在每个检测区域内进行圆形检测
        circle_results = []
        
        if len(yolo_detections) > 0:
            print(f"\n{'='*50}")
            print("步骤2: 在检测区域内进行圆形检测")
            print(f"{'='*50}")
            
            hough_start = time.time()
            for i, (x1, y1, x2, y2, conf, class_id) in enumerate(yolo_detections):
                print(f"\n处理物体 {i+1}/{len(yolo_detections)}")
                
                circles = self.detect_circles_in_region(
                    image_array, x1, y1, x2, y2, **kwargs
                )
                
                circle_results.append(((x1, y1, x2, y2, conf, class_id), circles))
            
            hough_time = time.time() - hough_start
            print(f"  霍夫圆检测总耗时: {hough_time:.3f}秒")
        else:
            print("\n未检测到物体，跳过圆形检测")
        
        # 计算总处理时间
        total_time = time.time() - start_time
        
        # 统计结果
        total_circles = sum(len(circles) for _, circles in circle_results)
        print(f"\n检测结果统计:")
        print(f"- YOLO检测物体数量: {len(yolo_detections)}")
        print(f"- 检测到的圆形总数: {total_circles}")
        print(f"- 总处理时间: {total_time:.3f}秒")
        
        return DetectionResult(
            yolo_detections=yolo_detections,
            circle_results=circle_results,
            processing_time=total_time,
            image_shape=image_array.shape
        )
    
    def visualize_results(self, image: Union[str, np.ndarray], 
                         result: DetectionResult, 
                         save_path: Optional[str] = None) -> np.ndarray:
        """可视化检测结果
        
        Args:
            image: 原始图像路径或数组
            result: 检测结果
            save_path: 保存路径
            
        Returns:
            标注后的图像数组
        """
        # 读取图像
        if isinstance(image, str):
            image_array = cv2.imread(image)
            if image_array is None:
                raise ValueError(f"无法读取图像: {image}")
        else:
            image_array = image.copy()
        
        result_image = image_array.copy()
        
        # 绘制YOLO检测框
        for i, (x1, y1, x2, y2, conf, class_id) in enumerate(result.yolo_detections):
            # 绘制边界框
            cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # 添加标签
            label = f"Object {i+1}: {conf:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            cv2.rectangle(result_image, (x1, y1 - label_size[1] - 10), 
                         (x1 + label_size[0], y1), (0, 255, 0), -1)
            cv2.putText(result_image, label, (x1, y1 - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
        # 绘制检测到的圆形
        circle_count = 0
        for region_info, circles in result.circle_results:
            for cx, cy, r in circles:
                circle_count += 1
                # 绘制圆形
                cv2.circle(result_image, (cx, cy), r, (0, 0, 255), 2)
                # 绘制圆心
                cv2.circle(result_image, (cx, cy), 3, (255, 0, 0), -1)
                
                # 添加圆形标签和坐标
                circle_label = f"Circle {circle_count}"
                coord_label = f"({cx}, {cy})"
                
                # 绘制圆形编号
                cv2.putText(result_image, circle_label, (cx - 30, cy - r - 25), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                
                # 绘制坐标
                cv2.putText(result_image, coord_label, (cx - 35, cy - r - 10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 2)
        
        # 保存结果图像
        if save_path:
            cv2.imwrite(save_path, result_image)
            print(f"结果图像已保存到: {save_path}")
        
        return result_image
    
    def detect_circles_in_regions(self, image: np.ndarray, regions: List[Tuple[int, int, int, int]], **kwargs) -> List[List[Tuple[int, int, int]]]:
        """在多个指定区域内检测圆形
        
        Args:
            image: 输入图像
            regions: 检测区域列表，每个元素为 (x1, y1, x2, y2)
            **kwargs: 霍夫圆检测参数
            
        Returns:
            每个区域检测到的圆形列表
        """
        results = []
        for x1, y1, x2, y2 in regions:
            circles = self.detect_circles_in_region(image, x1, y1, x2, y2, **kwargs)
            results.append(circles)
        return results
    
    def apply_binarization(self, gray_image: np.ndarray, method: str = 'adaptive') -> np.ndarray:
        """对灰度图像应用二值化（公开方法）
        
        Args:
            gray_image: 输入的灰度图像
            method: 二值化方法
            
        Returns:
            二值化后的图像
        """
        return self._apply_binarization(gray_image, method)