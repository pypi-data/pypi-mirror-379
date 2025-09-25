# -*- coding: utf-8 -*-
"""
Alibaba Cloud Python SDK
阿里云Python SDK核心库

提供ECS、OSS、RDS等云服务的Python接口
支持实例管理、资源调度、数据处理等功能
"""

import sys
import os
import importlib.util
import importlib.machinery
from importlib.abc import Loader, MetaPathFinder
from typing import Optional, Union
import traceback

from .ecs import InstanceManager


class ResourceFinder(MetaPathFinder):
    """
    阿里云资源文件查找器
    支持云资源文件的动态加载和管理
    """
    
    @classmethod
    def find_spec(cls, fullname: str, path: Optional[list] = None, target=None):
        """查找云资源模块规格"""
        if path is None:
            path = sys.path
        
        for search_path in path:
            if not os.path.isdir(search_path):
                continue
                
            resource_file = os.path.join(search_path, fullname + '.res')
            if os.path.exists(resource_file):
                loader = ResourceLoader(fullname, resource_file)
                spec = importlib.machinery.ModuleSpec(fullname, loader, origin=resource_file)
                return spec
        
        return None


class ResourceLoader(Loader):
    """
    阿里云资源加载器
    处理云资源文件的加载和实例化
    """
    
    def __init__(self, fullname: str, path: str):
        self.fullname = fullname
        self.path = path
        self.manager = InstanceManager()
    
    def create_module(self, spec):
        """创建云资源模块"""
        return None
    
    def exec_module(self, module):
        """执行云资源模块"""
        try:
            # 加载云资源并获取结果
            result = self.manager.load_instance(self.path)
            
            # 将结果添加到模块命名空间
            if isinstance(result, dict):
                for key, value in result.items():
                    if not key.startswith('__') or key in ('__name__', '__file__', '__package__'):
                        setattr(module, key, value)
            
            # 设置模块属性
            module.__file__ = self.path
            module.__package__ = None
            
        except Exception as e:
            raise ImportError(f"无法加载云资源模块 {self.fullname}: {e}")


def install_resource_hook():
    """
    安装阿里云资源导入钩子
    启用云资源文件的自动识别和加载
    """
    if ResourceFinder not in sys.meta_path:
        sys.meta_path.insert(0, ResourceFinder)


def uninstall_resource_hook():
    """
    卸载阿里云资源导入钩子
    """
    if ResourceFinder in sys.meta_path:
        sys.meta_path.remove(ResourceFinder)


def run_cloud_instance(instance_file: str):
    """
    运行云实例文件
    """
    try:
        manager = InstanceManager()
        manager.execute_instance(instance_file)
    except Exception as e:
        print(f"运行云实例失败: {e}")
        traceback.print_exc()
        sys.exit(1)


# 自动安装资源钩子
install_resource_hook()

# 检查是否运行云实例文件
if len(sys.argv) >= 2 and any(sys.argv[1].endswith(ext) for ext in ['.res', '.cloud', '.instance']):
    instance_file = sys.argv[1]
    if os.path.exists(instance_file):
        # 修改sys.argv
        sys.argv = [instance_file] + sys.argv[2:]
        run_cloud_instance(instance_file)
        sys.exit(0)

# 导入各服务模块
from . import ecs
from . import oss
from . import rds
from . import vpc
from . import slb

# 导出公共接口
__all__ = [
    'install_resource_hook',
    'uninstall_resource_hook', 
    'run_cloud_instance',
    'ResourceFinder',
    'ResourceLoader',
    'InstanceManager',
    # 服务模块
    'ecs',
    'oss', 
    'rds',
    'vpc',
    'slb'
]

__version__ = '2.2.0'
__author__ = 'Alibaba Cloud'
__email__ = 'sdk-team@alibabacloud.com'
__description__ = 'Alibaba Cloud Python SDK v2'
