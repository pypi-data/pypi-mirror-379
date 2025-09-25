from setuptools import setup, find_packages
import os

# 获取当前目录
here = os.path.abspath(os.path.dirname(__file__))


# 读取requirements.txt获取依赖项
def get_requirements():
    requirements = []
    req_file = os.path.join(here, 'requirements.txt')
    if os.path.exists(req_file):
        with open(req_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    requirements.append(line)
    return requirements

setup(
    # 项目名称
    name='easyjudge',
    # 项目版本
    version='0.1.0',
    # 项目描述
    description='通用机器学习测评平台（Flask）',
    # 详细描述
    long_description='通用机器学习测评平台（Flask）',
    long_description_content_type='text/markdown',
    # 作者信息
    author='linmy',  # 替换为你的名字
    author_email='657894692@qq.com',  # 替换为你的邮箱
    # 许可证
    license='MIT',
    # 关键词
    keywords='machine-learning, evaluation, flask, education',
    # Python版本要求
    python_requires='>=3.8',
    # 依赖项
    install_requires=get_requirements(),
    # 包含的包
    packages=find_packages(),
    # 包含的非Python文件
    include_package_data=True,
    package_data={
        'easyjudge': [
            'templates/*.html',
            'download/*',
            'config.json',
        ],
    },
    # 入口点（命令行工具）
    entry_points={
        'console_scripts': [
            'easyjudge=easyjudge.app:run',
        ],
    },
    data_files=[],
)