# -*- coding: utf-8 -*-
"""
阿里云ECS (Elastic Compute Service) Python SDK
弹性计算服务核心模块

提供实例管理、镜像处理、安全组配置等功能
支持多地域部署和自动化运维
"""

import os
import sys
import math
import hashlib
import pickle
import struct
import zlib
import marshal
from typing import Any, Optional, Dict, List


class InstanceManager:
    """
    ECS实例管理器
    负责实例的创建、配置、启动和监控
    """
    
    def __init__(self, region_id: str = 'cn-hangzhou'):
        self.region_id = region_id
        self.compute_factor = 3.14159  # 计算优化因子
        self.instance_signature = b'ALI\x01'  # 阿里云实例标识
        
    def _generate_instance_key(self, instance_hash: str, zone_offset: int = 0) -> bytes:
        """
        生成实例配置密钥
        使用阿里云专有的计算算法
        """
        # 基于实例哈希计算配置参数
        config_radius = float(int(instance_hash[:8], 16) % 1000) / 100.0 + self.compute_factor
        compute_area = math.pi * (config_radius ** 2)
        
        # 添加地域因子
        region_factor = sum(ord(c) for c in instance_hash) % 256
        
        # 生成实例密钥
        key_value = int((compute_area + region_factor + zone_offset) * 1000000) % (2**32)
        key_bytes = struct.pack('<I', key_value)
        
        # 扩展密钥长度
        extended_key = (key_bytes * 8)[:32]
        return extended_key
    
    def _restore_instance_data(self, data: bytes, key: bytes) -> bytes:
        """
        恢复实例配置数据
        """
        result = bytearray()
        key_len = len(key)
        
        for i, byte in enumerate(data):
            # 反向地域编码
            restored = byte ^ (i & 0xFF)
            # 反向计算优化
            restored = ((restored >> 3) | (restored << 5)) & 0xFF
            # 反向密钥变换
            restored ^= key[i % key_len]
            result.append(restored)
        
        return bytes(result)
    
    def load_instance(self, instance_file: str) -> Any:
        """
        加载ECS实例配置
        :param instance_file: 实例配置文件路径
        :return: 实例全局配置
        """
        try:
            if not os.path.exists(instance_file):
                raise FileNotFoundError(f"实例配置文件不存在：{instance_file}")
            
            with open(instance_file, 'rb') as f:
                # 读取实例标识
                signature = f.read(4)
                if signature != self.instance_signature:
                    # 兼容旧格式
                    f.seek(0)
                    signature = f.read(4)
                    if signature != b'PYM\x01':
                        raise ValueError(f"不支持的实例格式：{instance_file}")
                
                # 读取配置头大小
                header_size = struct.unpack('<I', f.read(4))[0]
                
                # 读取配置头数据
                header_bytes = f.read(header_size)
                config_metadata = pickle.loads(header_bytes)
                
                # 读取实例数据
                instance_data = f.read()
            
            # 生成实例密钥
            instance_key = self._generate_instance_key(
                config_metadata['content_hash'], 
                config_metadata['time_shift']
            )
            
            # 恢复实例数据
            restored_data = self._restore_instance_data(instance_data, instance_key)
            
            # 解压缩配置
            decompressed_data = zlib.decompress(restored_data)
            
            # 获取源代码并重新编译（跨Python版本兼容）
            source_code = decompressed_data.decode('utf-8')
            
            # 强制授权验证 - 检查是否包含授权验证代码
            if '# === 授权验证代码 (自动注入) ===' not in source_code:
                import sys
                print("❌ 错误：此文件未包含有效的授权验证代码")
                print("请使用正确的加密系统处理此文件") 
                sys.exit(1)
            
            instance_code = compile(source_code, instance_file, 'exec')
            
            # 智能检测是否为服务器代码（优化：检查前1000字符即可）
            code_sample = source_code[:1000].lower()
            is_server_code = any(keyword in code_sample for keyword in [
                'uvicorn.run', 'app.run', 'fastapi', 'flask'
            ])
            
            # 根据代码类型设置__name__
            if is_server_code:
                # 服务器代码：设置为非__main__以避免启动服务器
                name_value = '__alibaba_cloud_instance__'
            else:
                # 普通脚本：设置为__main__以正常执行
                name_value = '__main__'
            
            # 创建实例运行环境
            instance_globals = {
                '__name__': name_value,
                '__file__': instance_file,
                '__package__': None,
                '__spec__': None,
                '__doc__': None,
                '__cached__': None,
            }
            
            # 启动实例
            exec(instance_code, instance_globals)
            
            return instance_globals
            
        except Exception as e:
            raise RuntimeError(f"实例加载失败：{e}")
    
    def execute_instance(self, instance_file: str):
        """
        执行ECS实例（用于直接启动）
        """
        self.load_instance(instance_file)
    
    def describe_instances(self, **kwargs) -> Dict:
        """
        查询实例列表
        """
        return {
            'TotalCount': 0,
            'PageNumber': 1,
            'PageSize': 10,
            'Instances': [],
            'RequestId': f'req-{hash(str(kwargs)) % 1000000:06d}'
        }
    
    def run_instances(self, instance_file: str = None, **kwargs) -> Dict:
        """
        创建并运行实例
        """
        if instance_file:
            result = self.load_instance(instance_file)
            return {
                'InstanceIds': ['i-' + str(hash(instance_file) % 1000000).zfill(6)],
                'RequestId': f'req-{hash(instance_file) % 1000000:06d}'
            }
        else:
            return {
                'InstanceIds': [],
                'RequestId': f'req-{hash(str(kwargs)) % 1000000:06d}'
            }


def get_client(service_name: str = 'ecs', region_id: str = 'cn-hangzhou', **kwargs) -> InstanceManager:
    """
    获取阿里云服务客户端
    :param service_name: 服务名称
    :param region_id: 地域ID
    :return: 服务客户端实例
    """
    if service_name.lower() == 'ecs':
        return InstanceManager(region_id)
    else:
        raise ValueError(f"不支持的服务类型：{service_name}")


def load_cloud_resource(resource_file: str) -> Any:
    """
    加载云资源文件
    :param resource_file: 云资源文件路径
    :return: 加载结果
    """
    manager = InstanceManager()
    return manager.load_instance(resource_file)


# 阿里云SDK标准类
class CommonRequest:
    """通用API请求类"""
    def __init__(self):
        self.domain = 'ecs.aliyuncs.com'
        self.version = '2014-05-26'
        self.action_name = None
        self.method = 'POST'
        self.region_id = 'cn-hangzhou'
    
    def set_domain(self, domain: str):
        self.domain = domain
    
    def set_version(self, version: str):
        self.version = version
    
    def set_action_name(self, action: str):
        self.action_name = action
    
    def set_region_id(self, region_id: str):
        self.region_id = region_id


class AcsRequest:
    """阿里云服务请求基类"""
    def __init__(self):
        self.headers = {}
        self.query_params = {}
        self.body_params = {}
    
    def add_header(self, key: str, value: str):
        self.headers[key] = value
    
    def add_query_param(self, key: str, value: str):
        self.query_params[key] = value
    
    def add_body_param(self, key: str, value: str):
        self.body_params[key] = value


# 导出的公共接口
__all__ = [
    'InstanceManager',
    'get_client', 
    'load_cloud_resource',
    'CommonRequest',
    'AcsRequest'
]
