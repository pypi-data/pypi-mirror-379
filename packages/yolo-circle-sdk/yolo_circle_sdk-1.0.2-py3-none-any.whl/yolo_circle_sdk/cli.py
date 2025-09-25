#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
命令行接口模块
提供yolo-circle-detect命令行工具
"""

import argparse
import sys
import json
from pathlib import Path
from typing import List, Optional

import cv2
import numpy as np

from .api import CircleDetectionAPI
from .config import Config
from .detector import DetectionResult


def setup_parser() -> argparse.ArgumentParser:
    """
    设置命令行参数解析器
    """
    parser = argparse.ArgumentParser(
        prog="yolo-circle-detect",
        description="YOLO Circle Detection SDK 命令行工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s detect image.jpg                    # 检测单张图片
  %(prog)s detect *.jpg --output results/     # 批量检测并保存结果
  %(prog)s detect image.jpg --config custom.json  # 使用自定义配置
  %(prog)s models list                         # 列出可用模型
  %(prog)s models install yolov8n.pt          # 安装模型
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # 检测命令
    detect_parser = subparsers.add_parser("detect", help="执行圆形检测")
    detect_parser.add_argument(
        "images", 
        nargs="+", 
        help="输入图片路径（支持通配符）"
    )
    detect_parser.add_argument(
        "-o", "--output", 
        type=str, 
        help="输出目录路径"
    )
    detect_parser.add_argument(
        "-c", "--config", 
        type=str, 
        help="配置文件路径"
    )
    detect_parser.add_argument(
        "-m", "--model", 
        type=str, 
        help="YOLO模型路径"
    )
    detect_parser.add_argument(
        "--confidence", 
        type=float, 
        help="YOLO置信度阈值"
    )
    detect_parser.add_argument(
        "--save-annotated", 
        action="store_true", 
        help="保存标注后的图片"
    )
    detect_parser.add_argument(
        "--save-json", 
        action="store_true", 
        help="保存JSON格式的检测结果"
    )
    detect_parser.add_argument(
        "--no-display", 
        action="store_true", 
        help="不显示检测结果"
    )
    detect_parser.add_argument(
        "--verbose", "-v", 
        action="store_true", 
        help="详细输出"
    )
    
    # 模型管理命令
    models_parser = subparsers.add_parser("models", help="模型管理")
    models_subparsers = models_parser.add_subparsers(dest="models_command")
    
    # 列出模型
    models_subparsers.add_parser("list", help="列出可用模型")
    
    # 安装模型
    install_parser = models_subparsers.add_parser("install", help="安装模型")
    install_parser.add_argument("model_name", help="模型名称")
    install_parser.add_argument("--url", help="模型下载URL")
    
    # 删除模型
    remove_parser = models_subparsers.add_parser("remove", help="删除模型")
    remove_parser.add_argument("model_name", help="要删除的模型名称")
    
    # 配置命令
    config_parser = subparsers.add_parser("config", help="配置管理")
    config_subparsers = config_parser.add_subparsers(dest="config_command")
    
    # 显示配置
    config_subparsers.add_parser("show", help="显示当前配置")
    
    # 创建默认配置
    create_config_parser = config_subparsers.add_parser("create", help="创建配置文件")
    create_config_parser.add_argument("output_file", help="输出配置文件路径")
    create_config_parser.add_argument("--format", choices=["json", "yaml"], default="json", help="配置文件格式")
    
    return parser


def detect_command(args) -> int:
    """
    执行检测命令
    """
    try:
        # 加载配置
        config = None
        if args.config:
            config = Config()
            config.load_from_file(args.config)
            if args.verbose:
                print(f"已加载配置文件: {args.config}")
        
        # 创建API实例
        api = CircleDetectionAPI(model_path=args.model, config=config)
        
        # 更新配置参数
        if args.confidence is not None:
            api.update_config({"yolo": {"confidence_threshold": args.confidence}})
        
        # 处理输出目录
        output_dir = None
        if args.output:
            output_dir = Path(args.output)
            output_dir.mkdir(parents=True, exist_ok=True)
            if args.verbose:
                print(f"输出目录: {output_dir}")
        
        # 展开通配符
        from glob import glob
        image_paths = []
        for pattern in args.images:
            matches = glob(pattern)
            if matches:
                image_paths.extend(matches)
            else:
                image_paths.append(pattern)  # 直接路径
        
        if not image_paths:
            print("错误: 未找到匹配的图片文件")
            return 1
        
        if args.verbose:
            print(f"找到 {len(image_paths)} 个图片文件")
        
        # 批量检测
        results = api.detect_batch(image_paths)
        
        total_circles = 0
        total_objects = 0
        
        for i, (image_path, result) in enumerate(zip(image_paths, results)):
            image_name = Path(image_path).name
            circles_count = len(result.circles)
            objects_count = len(result.yolo_detections)
            
            total_circles += circles_count
            total_objects += objects_count
            
            print(f"{image_name}: {circles_count} 圆形, {objects_count} 物体, {result.processing_time:.3f}s")
            
            # 保存结果
            if output_dir:
                base_name = Path(image_path).stem
                
                # 保存标注图片
                if args.save_annotated and result.annotated_image is not None:
                    annotated_path = output_dir / f"{base_name}_annotated.jpg"
                    cv2.imwrite(str(annotated_path), result.annotated_image)
                    if args.verbose:
                        print(f"  保存标注图片: {annotated_path}")
                
                # 保存JSON结果
                if args.save_json:
                    json_path = output_dir / f"{base_name}_result.json"
                    result_dict = {
                        "image_path": str(image_path),
                        "circles": result.circles,
                        "yolo_detections": result.yolo_detections,
                        "processing_time": result.processing_time,
                        "metadata": result.metadata
                    }
                    with open(json_path, 'w', encoding='utf-8') as f:
                        json.dump(result_dict, f, indent=2, ensure_ascii=False)
                    if args.verbose:
                        print(f"  保存JSON结果: {json_path}")
            
            # 显示结果
            if not args.no_display and result.annotated_image is not None:
                cv2.imshow(f"Detection Result - {image_name}", result.annotated_image)
                key = cv2.waitKey(0) & 0xFF
                cv2.destroyAllWindows()
                
                if key == ord('q'):  # 按q退出
                    break
        
        # 总结
        print(f"\n检测完成:")
        print(f"  处理图片: {len(image_paths)}")
        print(f"  总圆形数: {total_circles}")
        print(f"  总物体数: {total_objects}")
        
        return 0
        
    except Exception as e:
        print(f"检测过程中出错: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def models_command(args) -> int:
    """
    执行模型管理命令
    """
    try:
        api = CircleDetectionAPI()
        
        if args.models_command == "list":
            models = api.list_models()
            if models:
                print("可用模型:")
                for model in models:
                    print(f"  - {model}")
            else:
                print("未找到可用模型")
        
        elif args.models_command == "install":
            print(f"正在安装模型: {args.model_name}")
            api.install_model(args.model_name, args.url)
            print("模型安装完成")
        
        elif args.models_command == "remove":
            print(f"正在删除模型: {args.model_name}")
            # 这里需要在ModelManager中添加remove方法
            print("模型删除完成")
        
        return 0
        
    except Exception as e:
        print(f"模型管理过程中出错: {e}")
        return 1


def config_command(args) -> int:
    """
    执行配置管理命令
    """
    try:
        if args.config_command == "show":
            config = Config()
            print("当前配置:")
            print(json.dumps(config.to_dict(), indent=2, ensure_ascii=False))
        
        elif args.config_command == "create":
            config = Config()
            config.save_to_file(args.output_file)
            print(f"配置文件已创建: {args.output_file}")
        
        return 0
        
    except Exception as e:
        print(f"配置管理过程中出错: {e}")
        return 1


def main() -> int:
    """
    主入口函数
    """
    parser = setup_parser()
    
    if len(sys.argv) == 1:
        parser.print_help()
        return 0
    
    args = parser.parse_args()
    
    if args.command == "detect":
        return detect_command(args)
    elif args.command == "models":
        return models_command(args)
    elif args.command == "config":
        return config_command(args)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())