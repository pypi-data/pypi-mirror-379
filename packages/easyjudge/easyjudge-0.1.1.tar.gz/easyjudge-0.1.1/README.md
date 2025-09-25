# EasyJudge

体脂率检测模型评估系统 - 用于评估和比较不同机器学习模型在体脂率预测任务上的性能

## 项目简介

EasyJudge 是一个基于 Flask 的通用机器学习测评平台。系统支持学生下载教师提供的数据与模板、训练后上传模型与推理脚本，平台会自动运行推理脚本并计算 RMSE，记录排行榜。

## 功能特点

- 用户认证系统
- 模型文件和推理脚本上传
- 自动运行用户提交的推理代码
- 模型性能评估（计算RMSE）
- 排行榜功能，展示不同模型的性能比较
- 支持用户多次提交，只保留最新结果

## 安装指南

### 使用pip安装

```bash
pip install easyjudge
```

### 从源代码安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/easyjudge.git
cd easyjudge

# 安装依赖
pip install -r requirements.txt

# 安装项目
pip install -e .
```

## 使用方法

### 启动应用

```bash
# 方法1：通过命令行工具
easyjudge

# 方法2：直接运行Python文件
python app.py
```

应用启动后，在浏览器中访问 http://localhost:5000 即可使用。

### 用户操作流程

1. 使用预设的用户名和手机号登录系统
2. 上传模型文件（.pkl格式）和Python推理脚本（.py格式）
3. 系统自动运行推理代码并评估模型性能
4. 查看个人成绩和排行榜

## 项目结构

```
easyjudge/
├── app.py                 # 主应用程序（也作为入口）
├── templates/             # HTML模板
│   └── index.html         # 主页模板
├── data/                  # 数据文件夹
│   └── testB.csv          # 测试数据集
├── uploads/               # 用户上传文件存储
├── requirements.txt       # 项目依赖
├── setup.py               # 打包配置文件
└── README.md              # 项目说明文档
```

## 依赖项

- Flask==2.3.3
- pandas==2.0.3
- numpy==1.24.4
- jinja2==3.1.2
- Werkzeug==2.3.7
- itsdangerous==2.1.2
- MarkupSafe==2.1.3
- python-dateutil==2.8.2
- pytz==2023.3
- six==1.16.0
- click>=8.1.3
- blinker>=1.6.2

## 开发者说明

### 项目配置

- 默认主机：0.0.0.0
- 默认端口：5000
- 调试模式：开启

### 注意事项

1. 用户提交的代码有60秒的运行时间限制
2. 系统会自动替换推理脚本中的测试集路径
3. 请确保上传的推理脚本能够正确生成`data/预测结果.csv`文件

## 许可证

本项目采用MIT许可证 - 详见LICENSE文件

## 作者

Your Name - your.email@example.com