#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
阿里云Python SDK v2安装脚本
"""

from setuptools import setup, find_packages
import os

# 读取README文件
readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        long_description = f.read()
else:
    long_description = '阿里云Python SDK，支持ECS、OSS、RDS等云服务'

setup(
    name='alibabacloude',
    version='2.2.0',
    description='阿里云Python3 SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alibaba Cloud',
    author_email='admin@alibabacloud.com',
    url='https://github.com/aliyun/alibabacloud-python-sdk-v2',
    packages=find_packages(),
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
    ],
    keywords='alibaba-cloud, aliyun, sdk, ecs, oss, rds, vpc, slb, cloud-computing',
    install_requires=[
        # 无外部依赖，仅使用标准库
    ],
    entry_points={
        'console_scripts': [
            'aliyun=alibabacloud.__main__:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
