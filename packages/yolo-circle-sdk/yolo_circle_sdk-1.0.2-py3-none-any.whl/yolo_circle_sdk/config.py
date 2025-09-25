"""配置管理模块"""

import os
from pathlib import Path
from typing import Dict, Any, Optional

class ConfigSection:
    """配置节类，支持属性访问"""
    
    def __init__(self, data: Dict[str, Any]):
        self._data = data
    
    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name: str, value: Any):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            if not hasattr(self, '_data'):
                super().__setattr__(name, value)
            else:
                self._data[name] = value
    
    def to_dict(self) -> Dict[str, Any]:
        return self._data.copy()


class Config:
    """SDK配置管理类"""
    
    def __init__(self):
        """初始化配置"""
        # 默认配置
        self._config = {
            # YOLO模型配置
            'yolo': {
                'confidence_threshold': 0.5,
                'iou_threshold': 0.5,
                'device': 'auto',
                'model_name': 'best1.pt',
                'model_cache_dir': self._get_cache_dir()
            },
            
            # 霍夫圆检测配置
            'hough': {
                'dp': 1,
                'min_dist': 15,
                'param1': 15,
                'param2': 8,
                'min_radius': 3,
                'max_radius': 50
            },
            
            # 二值化配置
            'binarization': {
                'threshold_value': 127,
                'max_value': 255,
                'threshold_type': 'THRESH_BINARY'
            },
            
            # 输出配置
            'output': {
                'save_results': False,
                'output_dir': './results',
                'save_annotated': True,
                'save_raw_results': False
            },
            
            # 环境配置
            'environment': {
                'kmp_duplicate_lib_ok': True,
                'matplotlib_backend': 'Agg'  # 非交互式后端
            }
        }
        
        # 创建配置节对象
        self.yolo = ConfigSection(self._config['yolo'])
        self.hough = ConfigSection(self._config['hough'])
        self.binarization = ConfigSection(self._config['binarization'])
        self.output = ConfigSection(self._config['output'])
        self.environment = ConfigSection(self._config['environment'])
        
        # 应用环境配置
        self._apply_environment_config()
    
    def _get_cache_dir(self) -> str:
        """获取缓存目录"""
        home_dir = Path.home()
        cache_dir = home_dir / '.yolo_circle_sdk' / 'models'
        cache_dir.mkdir(parents=True, exist_ok=True)
        return str(cache_dir)
    
    def _apply_environment_config(self):
        """应用环境配置"""
        env_config = self._config['environment']
        
        if env_config['kmp_duplicate_lib_ok']:
            os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
        
        # 设置matplotlib后端
        import matplotlib
        matplotlib.use(env_config['matplotlib_backend'])
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值
        
        Args:
            key: 配置键，支持点分隔的嵌套键，如 'yolo.conf_threshold'
            default: 默认值
            
        Returns:
            配置值
        """
        keys = key.split('.')
        value = self._config
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key: str, value: Any):
        """设置配置值
        
        Args:
            key: 配置键，支持点分隔的嵌套键
            value: 配置值
        """
        keys = key.split('.')
        config = self._config
        
        # 导航到最后一级
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        # 设置值
        config[keys[-1]] = value
    
    def update(self, config_dict: Dict[str, Any]):
        """批量更新配置
        
        Args:
            config_dict: 配置字典
        """
        def deep_update(base_dict, update_dict):
            for key, value in update_dict.items():
                if isinstance(value, dict) and key in base_dict and isinstance(base_dict[key], dict):
                    deep_update(base_dict[key], value)
                else:
                    base_dict[key] = value
        
        deep_update(self._config, config_dict)
        
        # 重新初始化ConfigSection对象
        self.yolo = ConfigSection(self._config['yolo'])
        self.hough = ConfigSection(self._config['hough'])
        self.binarization = ConfigSection(self._config['binarization'])
        self.output = ConfigSection(self._config['output'])
        self.environment = ConfigSection(self._config['environment'])
    
    def to_dict(self) -> Dict[str, Any]:
        """获取完整配置字典
        
        Returns:
            配置字典的深拷贝
        """
        import copy
        return copy.deepcopy(self._config)
    
    def load_from_file(self, config_path: str):
        """从文件加载配置
        
        Args:
            config_path: 配置文件路径，支持JSON和YAML格式
        """
        config_path = Path(config_path)
        
        if not config_path.exists():
            raise FileNotFoundError(f"配置文件不存在: {config_path}")
        
        if config_path.suffix.lower() == '.json':
            import json
            with open(config_path, 'r', encoding='utf-8') as f:
                config_dict = json.load(f)
        elif config_path.suffix.lower() in ['.yml', '.yaml']:
            try:
                import yaml
                with open(config_path, 'r', encoding='utf-8') as f:
                    config_dict = yaml.safe_load(f)
            except ImportError:
                raise ImportError("需要安装PyYAML来支持YAML配置文件: pip install PyYAML")
        else:
            raise ValueError(f"不支持的配置文件格式: {config_path.suffix}")
        
        self.update(config_dict)
    
    def save_to_file(self, config_path: str):
        """保存配置到文件
        
        Args:
            config_path: 配置文件路径
        """
        config_path = Path(config_path)
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        if config_path.suffix.lower() == '.json':
            import json
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, indent=2, ensure_ascii=False)
        elif config_path.suffix.lower() in ['.yml', '.yaml']:
            try:
                import yaml
                with open(config_path, 'w', encoding='utf-8') as f:
                    yaml.dump(self._config, f, default_flow_style=False, allow_unicode=True)
            except ImportError:
                raise ImportError("需要安装PyYAML来支持YAML配置文件: pip install PyYAML")
        else:
            raise ValueError(f"不支持的配置文件格式: {config_path.suffix}")


# 全局默认配置实例
default_config = Config()