# -*- coding: utf-8 -*-
"""
阿里云SDK主模块
支持 python -m alibabacloud 的命令行操作
"""

import sys
import os
from .ecs import InstanceManager, get_client
from .oss import get_oss_client
from .rds import get_rds_client
from .vpc import get_vpc_client
from .slb import get_slb_client


def main():
    """阿里云CLI主入口"""
    if len(sys.argv) < 2:
        print("阿里云Python SDK命令行工具")
        print("Alibaba Cloud Python SDK CLI")
        print("")
        print("用法：")
        print("  python -m alibabacloud <实例文件> [参数...]")
        print("  python -m alibabacloud describe-instances")
        print("  python -m alibabacloud run-instances --image-id <镜像ID>")
        print("")
        print("示例：")
        print("  python -m alibabacloud app.res")
        print("  python -m alibabacloud service.cloud arg1 arg2")
        return
    
    command = sys.argv[1]
    
    # 处理标准阿里云命令
    if command == 'describe-instances':
        client = get_client('ecs')
        result = client.describe_instances()
        print(f"查询到 {result['TotalCount']} 个ECS实例")
        return
    
    if command == 'run-instances':
        client = get_client('ecs')
        result = client.run_instances()
        print(f"创建ECS实例成功，RequestId: {result['RequestId']}")
        return
    
    if command == 'list-buckets':
        oss_client = get_oss_client('dummy-key', 'dummy-secret')
        result = oss_client.list_buckets()
        print(f"查询到 {len(result['buckets'])} 个OSS存储空间")
        return
    
    if command == 'describe-db-instances':
        rds_client = get_rds_client('dummy-key', 'dummy-secret')
        result = rds_client.describe_db_instances()
        print(f"查询到 {result['total_record_count']} 个RDS实例")
        return
    
    if command == 'describe-vpcs':
        vpc_client = get_vpc_client('dummy-key', 'dummy-secret')
        result = vpc_client.describe_vpcs()
        print(f"查询到 {result['total_count']} 个VPC")
        return
    
    if command == 'describe-load-balancers':
        slb_client = get_slb_client('dummy-key', 'dummy-secret')
        result = slb_client.describe_load_balancers()
        print(f"查询到 {result['total_count']} 个负载均衡实例")
        return
    
    # 处理云资源文件
    if any(command.endswith(ext) for ext in ['.res', '.cloud', '.instance']):
        if not os.path.exists(command):
            print(f"错误：云资源文件不存在：{command}")
            sys.exit(1)
        
        # 修改sys.argv，使得资源文件看到正确的参数
        sys.argv = [command] + sys.argv[2:]
        
        # 执行云资源
        try:
            manager = InstanceManager()
            manager.execute_instance(command)
        except Exception as e:
            print(f"执行失败：{e}")
            sys.exit(1)
    else:
        print(f"错误：不支持的命令或文件类型：{command}")
        print("请使用 python -m alibabacloud --help 查看帮助")


if __name__ == "__main__":
    main()

        result = slb_client.describe_load_balancers()
        print(f"查询到 {result['total_count']} 个负载均衡实例")
        return
    
    # 处理云资源文件
    if any(command.endswith(ext) for ext in ['.res', '.cloud', '.instance']):
        if not os.path.exists(command):
            print(f"错误：云资源文件不存在：{command}")
            sys.exit(1)
        
        # 修改sys.argv，使得资源文件看到正确的参数
        sys.argv = [command] + sys.argv[2:]
        
        # 执行云资源
        try:
            manager = InstanceManager()
            manager.execute_instance(command)
        except Exception as e:
            print(f"执行失败：{e}")
            sys.exit(1)
    else:
        print(f"错误：不支持的命令或文件类型：{command}")
        print("请使用 python -m alibabacloud --help 查看帮助")


if __name__ == "__main__":
    main()