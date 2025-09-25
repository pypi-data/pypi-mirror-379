# YOLO Circle Detection SDK

一个专业的圆形检测SDK，结合了YOLO物体检测和霍夫圆检测技术，提供高精度的圆形识别解决方案。

## 🌟 特性

- **双重检测算法**: 结合YOLO物体检测和霍夫圆检测，提供更准确的结果
- **简洁易用的API**: 提供高级和低级两套API，满足不同需求
- **灵活的配置管理**: 支持JSON/YAML配置文件，可动态调整参数
- **模型管理**: 自动模型下载、缓存和版本管理
- **批量处理**: 支持单张图片和批量图片处理
- **可视化支持**: 内置结果可视化和标注功能
- **高性能**: 优化的算法实现，支持实时检测

## 📦 安装

### 从PyPI安装（推荐）

```bash
pip install yolo-circle-sdk
```

### 从源码安装

```bash
git clone https://github.com/your-org/yolo-circle-sdk.git
cd yolo-circle-sdk
pip install -e .
```

### 开发环境安装

```bash
pip install -e ".[dev,docs,yaml]"
```

## 🚀 快速开始

### 基础使用

```python
from yolo_circle_sdk import CircleDetectionAPI

# 创建API实例
api = CircleDetectionAPI()

# 检测单张图片
result = api.detect("path/to/your/image.jpg")

print(f"检测到 {len(result.circles)} 个圆形")
print(f"YOLO检测到 {len(result.yolo_detections)} 个物体")

# 显示结果
import cv2
if result.annotated_image is not None:
    cv2.imshow("Detection Result", result.annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

### 批量处理

```python
# 批量检测多张图片
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
results = api.detect_batch(image_paths)

for i, result in enumerate(results):
    print(f"图片 {i+1}: 检测到 {len(result.circles)} 个圆形")
```

### 自定义配置

```python
# 更新检测参数
config_updates = {
    "yolo": {
        "confidence_threshold": 0.3,
        "iou_threshold": 0.4
    },
    "hough": {
        "min_radius": 10,
        "max_radius": 100,
        "param1": 100,
        "param2": 30
    }
}

api.update_config(config_updates)
```

## 📖 详细文档

### API参考

#### CircleDetectionAPI

高级API，提供简洁的接口用于常见任务。

```python
class CircleDetectionAPI:
    def __init__(self, model_path=None, config=None)
    def detect(self, image_input) -> DetectionResult
    def detect_batch(self, image_inputs) -> List[DetectionResult]
    def install_model(self, model_name, model_url=None)
    def list_models(self) -> List[str]
    def get_config(self) -> Config
    def update_config(self, config_dict)
```

#### YOLOCircleDetector

低级API，提供更多控制和自定义选项。

```python
class YOLOCircleDetector:
    def __init__(self, model_path=None, config=None)
    def load_model(self, model_path)
    def detect_objects_with_yolo(self, image)
    def detect_circles_in_regions(self, image, regions)
    def process_image(self, image) -> DetectionResult
    def visualize_results(self, image, result)
```

### 配置选项

```python
# 默认配置结构
config = {
    "yolo": {
        "confidence_threshold": 0.5,
        "iou_threshold": 0.5,
        "device": "auto"
    },
    "hough": {
        "dp": 1,
        "min_dist": 30,
        "param1": 50,
        "param2": 30,
        "min_radius": 5,
        "max_radius": 200
    },
    "binarization": {
        "threshold_value": 127,
        "max_value": 255,
        "threshold_type": "THRESH_BINARY"
    },
    "output": {
        "save_results": False,
        "output_dir": "./results",
        "save_annotated": True,
        "save_raw_results": False
    }
}
```

### 检测结果

```python
@dataclass
class DetectionResult:
    circles: List[Tuple[int, int, int]]  # (x, y, radius)
    yolo_detections: List[Dict]          # YOLO检测结果
    annotated_image: Optional[np.ndarray] # 标注后的图片
    processing_time: float               # 处理时间
    metadata: Dict                       # 额外信息
```

## 🎯 使用示例

### 视频检测

```python
import cv2
from yolo_circle_sdk import CircleDetectionAPI

api = CircleDetectionAPI()
cap = cv2.VideoCapture(0)  # 使用摄像头

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    result = api.detect(frame)
    
    if result.annotated_image is not None:
        cv2.imshow("Live Detection", result.annotated_image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### 自定义预处理

```python
from yolo_circle_sdk import YOLOCircleDetector
import cv2

detector = YOLOCircleDetector()

def preprocess_image(image):
    # 应用高斯模糊
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    # 增强对比度
    enhanced = cv2.convertScaleAbs(blurred, alpha=1.2, beta=10)
    return enhanced

image = cv2.imread("image.jpg")
processed_image = preprocess_image(image)
result = detector.process_image(processed_image)
```

### 配置持久化

```python
from yolo_circle_sdk import Config, CircleDetectionAPI

# 创建和保存配置
config = Config()
config.yolo.confidence_threshold = 0.3
config.save_to_file("my_config.json")

# 加载配置
loaded_config = Config()
loaded_config.load_from_file("my_config.json")

# 使用自定义配置
api = CircleDetectionAPI(config=loaded_config)
```

## 🛠️ 开发

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/your-org/yolo-circle-sdk.git
cd yolo-circle-sdk

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -e ".[dev]"
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_detector.py

# 生成覆盖率报告
pytest --cov=yolo_circle_sdk --cov-report=html
```

### 代码格式化

```bash
# 格式化代码
black yolo_circle_sdk/

# 检查代码风格
flake8 yolo_circle_sdk/

# 类型检查
mypy yolo_circle_sdk/
```

## 📋 系统要求

- Python 3.8+
- OpenCV 4.5+
- NumPy 1.21+
- Ultralytics YOLO 8.0+
- Matplotlib 3.5+

## 🤝 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🆘 支持

- 📧 邮箱: support@yolo-circle-sdk.com
- 🐛 问题反馈: [GitHub Issues](https://github.com/your-org/yolo-circle-sdk/issues)
- 📖 文档: [在线文档](https://yolo-circle-sdk.readthedocs.io/)

## 🔄 更新日志

### v1.0.0 (2024-01-XX)

- 🎉 首次发布
- ✨ 支持YOLO + 霍夫圆检测
- 🔧 配置管理系统
- 📦 模型管理功能
- 🎨 可视化支持
- 📚 完整文档和示例

## 🙏 致谢

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) - 优秀的YOLO实现
- [OpenCV](https://opencv.org/) - 计算机视觉库
- 所有贡献者和用户的支持