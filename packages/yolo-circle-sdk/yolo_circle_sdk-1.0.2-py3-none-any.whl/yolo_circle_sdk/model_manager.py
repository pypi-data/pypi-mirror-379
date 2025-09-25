"""模型资源管理模块"""

import os
import shutil
from pathlib import Path
from typing import Optional, Union
import hashlib

class ModelManager:
    """模型文件管理器"""
    
    def __init__(self, cache_dir: Optional[str] = None):
        """初始化模型管理器
        
        Args:
            cache_dir: 模型缓存目录，如果为None则使用默认目录
        """
        if cache_dir is None:
            home_dir = Path.home()
            self.cache_dir = home_dir / '.yolo_circle_sdk' / 'models'
        else:
            self.cache_dir = Path(cache_dir)
        
        # 确保缓存目录存在
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # 内置模型信息
        self.builtin_models = {
            'best1.pt': {
                'filename': 'best1.pt',
                'description': 'YOLO圆形检测模型',
                'size': 'Unknown'
            }
        }
    
    def get_model_path(self, model_name: str, source_path: Optional[str] = None) -> str:
        """获取模型文件路径
        
        Args:
            model_name: 模型名称
            source_path: 源模型文件路径（用于首次复制）
            
        Returns:
            模型文件的完整路径
            
        Raises:
            FileNotFoundError: 模型文件不存在且无法获取
        """
        cached_path = self.cache_dir / model_name
        
        # 如果缓存中已存在，直接返回
        if cached_path.exists():
            return str(cached_path)
        
        # 如果提供了源路径，尝试复制到缓存
        if source_path and Path(source_path).exists():
            return self._copy_to_cache(source_path, model_name)
        
        # 尝试从当前工作目录查找
        local_path = Path.cwd() / model_name
        if local_path.exists():
            return self._copy_to_cache(str(local_path), model_name)
        
        # 尝试从相对路径查找
        relative_paths = [
            Path.cwd() / 'yolo' / model_name,
            Path.cwd() / 'models' / model_name,
            Path.cwd() / 'weights' / model_name
        ]
        
        for path in relative_paths:
            if path.exists():
                return self._copy_to_cache(str(path), model_name)
        
        raise FileNotFoundError(
            f"模型文件 '{model_name}' 未找到。请确保模型文件存在，或提供正确的source_path参数。\n"
            f"搜索路径包括：\n"
            f"- 缓存目录: {cached_path}\n"
            f"- 当前目录: {local_path}\n"
            f"- 相对路径: {[str(p) for p in relative_paths]}"
        )
    
    def _copy_to_cache(self, source_path: str, model_name: str) -> str:
        """复制模型文件到缓存目录
        
        Args:
            source_path: 源文件路径
            model_name: 目标模型名称
            
        Returns:
            缓存文件路径
        """
        source_path = Path(source_path)
        cached_path = self.cache_dir / model_name
        
        print(f"正在复制模型文件到缓存: {source_path} -> {cached_path}")
        
        try:
            shutil.copy2(source_path, cached_path)
            print(f"模型文件已缓存: {cached_path}")
            return str(cached_path)
        except Exception as e:
            raise RuntimeError(f"复制模型文件失败: {e}")
    
    def install_model(self, source_path: str, model_name: Optional[str] = None) -> str:
        """安装模型文件到SDK
        
        Args:
            source_path: 源模型文件路径
            model_name: 目标模型名称，如果为None则使用源文件名
            
        Returns:
            安装后的模型路径
        """
        source_path = Path(source_path)
        
        if not source_path.exists():
            raise FileNotFoundError(f"源模型文件不存在: {source_path}")
        
        if model_name is None:
            model_name = source_path.name
        
        return self._copy_to_cache(str(source_path), model_name)
    
    def list_models(self) -> dict:
        """列出所有可用的模型
        
        Returns:
            模型信息字典
        """
        models = {}
        
        # 添加缓存中的模型
        for model_file in self.cache_dir.glob('*.pt'):
            file_size = model_file.stat().st_size
            models[model_file.name] = {
                'filename': model_file.name,
                'path': str(model_file),
                'size': self._format_size(file_size),
                'cached': True
            }
        
        # 添加内置模型信息
        for name, info in self.builtin_models.items():
            if name not in models:
                models[name] = {
                    **info,
                    'cached': False
                }
        
        return models
    
    def _format_size(self, size_bytes: int) -> str:
        """格式化文件大小
        
        Args:
            size_bytes: 字节数
            
        Returns:
            格式化的大小字符串
        """
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def remove_model(self, model_name: str) -> bool:
        """删除缓存的模型文件
        
        Args:
            model_name: 模型名称
            
        Returns:
            是否成功删除
        """
        cached_path = self.cache_dir / model_name
        
        if cached_path.exists():
            try:
                cached_path.unlink()
                print(f"已删除模型文件: {cached_path}")
                return True
            except Exception as e:
                print(f"删除模型文件失败: {e}")
                return False
        else:
            print(f"模型文件不存在: {cached_path}")
            return False
    
    def clear_cache(self) -> int:
        """清空模型缓存
        
        Returns:
            删除的文件数量
        """
        count = 0
        for model_file in self.cache_dir.glob('*.pt'):
            try:
                model_file.unlink()
                count += 1
            except Exception as e:
                print(f"删除文件失败 {model_file}: {e}")
        
        print(f"已清空缓存，删除了 {count} 个模型文件")
        return count
    
    def get_cache_info(self) -> dict:
        """获取缓存信息
        
        Returns:
            缓存信息字典
        """
        model_files = list(self.cache_dir.glob('*.pt'))
        total_size_bytes = sum(f.stat().st_size for f in model_files)
        total_size_mb = total_size_bytes / (1024 * 1024)
        
        return {
            'cache_dir': str(self.cache_dir),
            'model_count': len(model_files),
            'total_size': self._format_size(total_size_bytes),
            'total_size_mb': total_size_mb,
            'models': [f.name for f in model_files]
        }