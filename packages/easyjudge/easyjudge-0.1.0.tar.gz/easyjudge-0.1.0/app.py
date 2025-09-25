from flask import Flask, render_template, request, jsonify, send_file, session
import os
import pandas as pd
import numpy as np
import subprocess
from datetime import datetime
import shutil
import traceback
import json
from functools import wraps

# 设置根目录为当前文件所在目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_DIR)

app = Flask(__name__)
# 设置SECRET_KEY以支持session
app.secret_key = 'easyjudge_secret_key_2023'  # 生产环境应该使用更安全的密钥

# 配置上传文件夹
UPLOAD_FOLDER = os.path.join(ROOT_DIR, 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 下载文件夹（用于存储教师上传的数据文件）
DOWNLOAD_FOLDER = os.path.join(ROOT_DIR, 'download')
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)
    print(f"创建下载文件夹: {DOWNLOAD_FOLDER}")

# 存储参加者名单
PARTICIPANTS_FILE = os.path.join(ROOT_DIR, 'participants.json')

# 配置文件路径
CONFIG_FILE = os.path.join(ROOT_DIR, 'config.json')

# 初始化默认配置
DEFAULT_CONFIG = {
    'training_data_path': '数据集A.csv',  # 直接使用文件名，因为文件会被放在download文件夹中
    'test_data_path': '数据集B.csv',  # 使用文件名，文件实际保存在 download 目录中
    'inference_template_path': 'BaseML库推理模板.py',
    'admin_password': 'XEduPro'  # 默认密码，教师可以修改
}

# 读取或创建配置文件
def get_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=4)
        return DEFAULT_CONFIG
    
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# 更新配置文件
def update_config(new_config):
    current_config = get_config()
    current_config.update(new_config)
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(current_config, f, ensure_ascii=False, indent=4)

# 读取或创建参加者名单
def get_participants():
    if not os.path.exists(PARTICIPANTS_FILE):
        # 默认添加一些示例用户
        default_users = {
            'admin': 'XEduPro',  # 管理员账号（虽然单独管理，但也可以在这里保留）
            'user1': 'password1',
            'user2': 'password2'
        }
        with open(PARTICIPANTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_users, f, ensure_ascii=False, indent=4)
        return default_users
    
    with open(PARTICIPANTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# 更新参加者名单
def update_participants(participants):
    with open(PARTICIPANTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(participants, f, ensure_ascii=False, indent=4)

# 添加参加者
def add_participant(username, password):
    participants = get_participants()
    participants[username] = password
    update_participants(participants)



# 删除参加者
def delete_participant(username):
    participants = get_participants()
    if username in participants:
        del participants[username]
        update_participants(participants)


# 存储排行榜数据
leaderboard_file = os.path.join(ROOT_DIR, 'leaderboard.csv')
if not os.path.exists(leaderboard_file):
    pd.DataFrame(columns=['username', 'phone', 'rmse', 'timestamp']).to_csv(leaderboard_file, index=False)


@app.route('/')
def index():
    leaderboard = pd.read_csv(leaderboard_file)
    leaderboard = leaderboard.sort_values('rmse', ascending=True)  # 按RMSE升序排序
    leaderboard = leaderboard.drop(columns=['phone'])
    return render_template('index.html', leaderboard=leaderboard.to_dict('records'))

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    participants = get_participants()
    if username in participants and participants[username] == password:
        return jsonify({'success': True, 'username': username})
    return jsonify({'success': False, 'message': '账号或密码错误'})

@app.route('/upload', methods=['POST'])
def upload():
    if 'model_file' not in request.files or 'python_file' not in request.files:
        return jsonify({'success': False, 'message': '请上传模型文件和Python文件'})
    
    model_file = request.files['model_file']
    python_file = request.files['python_file']
    username = request.form.get('username')
    
    if model_file.filename == '' or python_file.filename == '':
        return jsonify({'success': False, 'message': '请选择所有必需的文件'})
    
    if not python_file.filename.endswith('.py'):
        return jsonify({'success': False, 'message': 'Python文件必须以.py结尾'})
    
    if not username:
        return jsonify({'success': False, 'message': '用户信息不完整'})
    
    # 创建用户专属文件夹
    user_folder = os.path.join(UPLOAD_FOLDER, username)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    # 创建/确保 data 目录存在，并从配置复制测试集到 data/testB.csv（每次覆盖）
    dst_data_dir = os.path.join(user_folder, 'data')
    os.makedirs(dst_data_dir, exist_ok=True)

    config = get_config()
    test_filename = os.path.basename(config.get('test_data_path', ''))
    if not test_filename:
        return jsonify({'success': False, 'message': '系统未配置测试数据集文件名'}), 400

    src_test_path = os.path.join(DOWNLOAD_FOLDER, test_filename)
    dst_test_path = os.path.join(dst_data_dir, 'testB.csv')

    if not os.path.exists(src_test_path):
        return jsonify({'success': False, 'message': f'测试数据集不存在: {src_test_path}'}), 400

    try:
        shutil.copy(src_test_path, dst_test_path)
        # 兼容旧模板硬编码路径 data/测试集A.csv
        legacy_test_path = os.path.join(dst_data_dir, '测试集A.csv')
        try:
            shutil.copy(src_test_path, legacy_test_path)
        except Exception:
            pass
    except Exception as e:
        return jsonify({'success': False, 'message': f'复制测试数据集失败: {str(e)}'}), 500
    
    # 保存上传的文件（保留原始文件名）
    model_path = os.path.join(user_folder, model_file.filename)
    python_path = os.path.join(user_folder, python_file.filename)
    
    model_file.save(model_path)
    python_file.save(python_path)
    
    # 兼容部分模板固定查找 model.pkl：如果用户上传的模型文件名不是 model.pkl，则复制一份为 model.pkl
    try:
        if os.path.basename(model_path) != 'model.pkl':
            compat_model_path = os.path.join(user_folder, 'model.pkl')
            shutil.copy(model_path, compat_model_path)
    except Exception as e:
        return jsonify({'success': False, 'message': f'准备兼容模型文件失败: {str(e)}'}), 500
    
    try:
        # 切换到用户目录运行代码
        original_dir = os.getcwd()
        os.chdir(user_folder)

        # 检查必要文件是否存在
        if not os.path.exists('data/testB.csv'):
            raise FileNotFoundError('测试集文件 data/testB.csv 不存在，请检查路径！')

        # 运行推理代码，增加超时和异常捕获
        try:
            result = subprocess.run(
                ['python', os.path.basename(python_path)],
                capture_output=True,
                text=True,
                timeout=60  # 最多运行60秒
            )
            if result.returncode != 0:
                # 用户代码报错，返回stderr
                raise RuntimeError(f"用户代码运行出错：\n{result.stderr}")
        except subprocess.TimeoutExpired:
            raise TimeoutError("用户代码运行超时（超过60秒），请检查代码是否有死循环或效率问题。")
        except Exception as sub_e:
            raise RuntimeError(f"运行用户代码时发生异常：{str(sub_e)}")

        # 使用硬编码的测试数据路径
        test_data_path = 'data/testB.csv'
        
        rmse = 999.999  # 默认值
        if os.path.exists("data/预测结果.csv"):
            try:
                # 读取预测值
                y_pred_loaded = pd.read_csv("data/预测结果.csv")['预测值'].values
                # 读取真实值（使用测试集的最后一列）
                test_df = pd.read_csv(test_data_path)
                y_true = test_df.iloc[:, -1].values
                # 计算RMSE
                rmse = np.sqrt(np.mean((y_true - y_pred_loaded) ** 2))
            except Exception as e:
                print(f"计算RMSE时出错: {str(e)}")
                rmse = 999.999
        else:
            raise FileNotFoundError("未生成 data/预测结果.csv，请检查推理代码是否正确输出。")

        # 先将新结果加入排行榜
        leaderboard = pd.read_csv(leaderboard_file)
        new_entry = pd.DataFrame({
            'username': [username],
            'phone': [''],  # 确保包含phone字段
            'rmse': [rmse],
            'timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        })
        leaderboard = pd.concat([leaderboard, new_entry], ignore_index=True)

        # 只保留每个用户最新一次提交
        leaderboard = leaderboard.sort_values('timestamp').drop_duplicates(['username'], keep='last')
        leaderboard.to_csv(leaderboard_file, index=False)

        return jsonify({
            'success': True,
            'rmse': rmse,
            'message': '提交成功，后续会按照排名赋分'
        })

    except Exception as e:
        # 捕获所有异常，返回详细错误信息
        print('推理异常:', str(e))
        print(traceback.format_exc())
        return jsonify({'success': False, 'message': f'处理文件时出错: {str(e)}'})

    finally:
        # 无论如何都切回原目录，避免影响后续请求
        try:
            os.chdir(original_dir)
        except Exception:
            pass

# 下载参会者模板文件
@app.route('/admin/download_participants_template')
def download_participants_template():
    try:
        # 创建临时CSV文件
        import tempfile
        import csv
        
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', newline='', delete=False) as temp_file:
            writer = csv.writer(temp_file)
            # 写入表头
            writer.writerow(['账号', '密码'])
            # 写入示例数据
            writer.writerow(['student1', 'password1'])
            writer.writerow(['student2', 'password2'])
            temp_file_path = temp_file.name
        
        # 提供文件下载
        return send_file(temp_file_path, as_attachment=True, download_name='参会者模板.csv')
        
    except Exception as e:
        print('下载模板文件失败:', str(e))
        return jsonify({'success': False, 'message': '下载模板文件失败'}), 500

# 上传参会者文件
@app.route('/admin/upload_participants', methods=['POST'])
def upload_participants():
    if 'participants_file' not in request.files:
        return jsonify({'success': False, 'message': '请选择文件'})
    
    file = request.files['participants_file']
    if file.filename == '':
        return jsonify({'success': False, 'message': '请选择文件'})
    
    if not file.filename.endswith('.csv'):
        return jsonify({'success': False, 'message': '请选择CSV格式的文件'})
    
    try:
        # 读取CSV文件
        import csv
        from io import StringIO
        
        # 读取文件内容，尝试多种编码格式以增加兼容性
        file_content_bytes = file.read()
        file_content = None
        
        # 尝试UTF-8编码
        try:
            file_content = file_content_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # 如果UTF-8失败，尝试GBK编码（Excel默认导出的CSV编码）
            try:
                file_content = file_content_bytes.decode('gbk')
            except UnicodeDecodeError:
                # 如果GBK也失败，尝试其他常见编码
                try:
                    file_content = file_content_bytes.decode('latin-1')
                except:
                    return jsonify({'success': False, 'message': '文件编码格式不支持，请确保是UTF-8或GBK编码的CSV文件'})
        
        csv_data = csv.reader(StringIO(file_content))
        
        # 获取表头
        headers = next(csv_data)
        
        # 检查是否包含必要的列
        if '账号' not in headers or '密码' not in headers:
            return jsonify({'success': False, 'message': 'CSV文件必须包含"账号"和"密码"列'})
        
        # 获取列索引
        username_index = headers.index('账号')
        password_index = headers.index('密码')
        
        # 读取数据并添加参加者
        added_count = 0
        participants = get_participants()
        
        for row in csv_data:
            if len(row) <= max(username_index, password_index):
                continue  # 跳过不完整的行
            
            username = row[username_index].strip()
            password = row[password_index].strip()
            
            if username and password:
                participants[username] = password
                added_count += 1
        
        # 更新参加者文件
        update_participants(participants)
        
        return jsonify({'success': True, 'message': f'成功添加{added_count}个参加者'})
        
    except Exception as e:
        print('上传参会者文件失败:', str(e))
        print(traceback.format_exc())
        return jsonify({'success': False, 'message': f'处理文件时出错: {str(e)}'})

# 下载路由
@app.route('/download/training_data')
def download_training_data():
    config = get_config()
    file_path = config.get('training_data_path')
    if not file_path:
        return jsonify({'success': False, 'message': '训练数据集路径未配置'}), 404
    
    # 获取文件名并优先从download文件夹中查找
    filename = os.path.basename(file_path)
    download_folder_path = os.path.join(DOWNLOAD_FOLDER, filename)
    
    # 优先使用download文件夹中的文件
    if os.path.exists(download_folder_path):
        file_path = download_folder_path
    elif not os.path.exists(file_path):
        return jsonify({'success': False, 'message': '文件不存在'}), 404
    
    try:
        # 在学生下载文件时打印具体文件下载位置
        print(f"学生下载训练数据文件位置: {file_path}")
        return send_file(file_path, as_attachment=True, download_name=filename)
    except Exception as e:
        print(f"下载训练数据出错: {str(e)}")
        return jsonify({'success': False, 'message': f'下载失败: {str(e)}'}), 500

@app.route('/download/inference_template')
def download_inference_template():
    config = get_config()
    file_path = config.get('inference_template_path')
    if not file_path:
        return jsonify({'success': False, 'message': '推理模板路径未配置'}), 404
    
    # 获取文件名并优先从download文件夹中查找
    filename = os.path.basename(file_path)
    download_folder_path = os.path.join(DOWNLOAD_FOLDER, filename)
    
    # 优先使用download文件夹中的文件
    if os.path.exists(download_folder_path):
        file_path = download_folder_path
    elif not os.path.exists(file_path):
        return jsonify({'success': False, 'message': '文件不存在'}), 404
    
    try:
        # 在学生下载文件时打印具体文件下载位置
        print(f"学生下载推理模板文件位置: {file_path}")
        return send_file(file_path, as_attachment=True, download_name=filename)
    except Exception as e:
        print(f"下载推理模板出错: {str(e)}")
        return jsonify({'success': False, 'message': f'下载失败: {str(e)}'}), 500

# Admin界面路由
# 管理员登录验证装饰器
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 检查session中是否有admin_logged_in标记
        if not session.get('admin_logged_in'):
            # 如果未登录，重定向到登录页面
            return render_template('admin.html', need_login=True)
        return f(*args, **kwargs)
    return decorated_function

@app.route('/admin')
def admin():
    # 检查是否已登录
    if session.get('admin_logged_in'):
        return render_template('admin.html', need_login=False)
    else:
        return render_template('admin.html', need_login=True)

@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    password = data.get('password')
    config = get_config()
    
    if password == config['admin_password']:
        # 使用session保存登录状态
        session['admin_logged_in'] = True
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': '密码错误'})

@app.route('/admin/get_config')
@admin_required
def admin_get_config():
    config = get_config()
    return jsonify(config)

@app.route('/admin/update_config', methods=['POST'])
@admin_required
def admin_update_config():
    try:
        print("收到配置更新请求")
        print(f"请求方法: {request.method}")
        print(f"是否包含文件: {len(request.files) > 0}")
        print(f"所有文件字段: {list(request.files.keys())}")
        print(f"表单字段: {list(request.form.keys())}")
        
        # 确保download文件夹存在
        if not os.path.exists(DOWNLOAD_FOLDER):
            os.makedirs(DOWNLOAD_FOLDER)
            print(f"创建下载文件夹: {DOWNLOAD_FOLDER}")
        
        print(f"当前下载文件夹路径: {DOWNLOAD_FOLDER}")
        print(f"下载文件夹是否存在: {os.path.exists(DOWNLOAD_FOLDER)}")
        
        uploaded_files = []
        new_config = {}
        
        # 处理训练数据集文件
        if 'training_data_file' in request.files:
            training_file = request.files['training_data_file']
            print(f"训练数据文件存在: {training_file.filename}")
            if training_file.filename:
                # 确保文件名合法
                safe_filename = os.path.basename(training_file.filename)
                training_file_path = os.path.join(DOWNLOAD_FOLDER, safe_filename)
                print(f"训练数据文件保存路径: {training_file_path}")
                
                try:
                    # 保存文件
                    training_file.save(training_file_path)
                    print(f"尝试保存训练数据文件到: {training_file_path}")
                    
                    # 验证文件是否保存成功
                    if os.path.exists(training_file_path):
                        print(f"验证: 训练数据文件保存成功，文件大小: {os.path.getsize(training_file_path)} 字节")
                        uploaded_files.append(safe_filename)
                        new_config['training_data_path'] = safe_filename
                    else:
                        print(f"警告: 训练数据文件保存失败，文件不存在")
                except Exception as e:
                    print(f"保存训练数据文件时发生错误: {str(e)}")
        
        # 处理测试数据集文件
        if 'test_data_file' in request.files:
            test_file = request.files['test_data_file']
            print(f"测试数据文件存在: {test_file.filename}")
            if test_file.filename:
                safe_filename = os.path.basename(test_file.filename)
                test_file_path = os.path.join(DOWNLOAD_FOLDER, safe_filename)
                print(f"测试数据文件保存路径: {test_file_path}")
                
                try:
                    test_file.save(test_file_path)
                    print(f"尝试保存测试数据文件到: {test_file_path}")
                    
                    if os.path.exists(test_file_path):
                        print(f"验证: 测试数据文件保存成功，文件大小: {os.path.getsize(test_file_path)} 字节")
                        uploaded_files.append(safe_filename)
                        new_config['test_data_path'] = safe_filename
                    else:
                        print(f"警告: 测试数据文件保存失败，文件不存在")
                except Exception as e:
                    print(f"保存测试数据文件时发生错误: {str(e)}")
        
        # 处理推理模板文件
        if 'inference_template_file' in request.files:
            template_file = request.files['inference_template_file']
            print(f"推理模板文件存在: {template_file.filename}")
            if template_file.filename:
                safe_filename = os.path.basename(template_file.filename)
                template_file_path = os.path.join(DOWNLOAD_FOLDER, safe_filename)
                print(f"推理模板文件保存路径: {template_file_path}")
                
                try:
                    template_file.save(template_file_path)
                    print(f"尝试保存推理模板文件到: {template_file_path}")
                    
                    if os.path.exists(template_file_path):
                        print(f"验证: 推理模板文件保存成功，文件大小: {os.path.getsize(template_file_path)} 字节")
                        uploaded_files.append(safe_filename)
                        new_config['inference_template_path'] = safe_filename
                    else:
                        print(f"警告: 推理模板文件保存失败，文件不存在")
                except Exception as e:
                    print(f"保存推理模板文件时发生错误: {str(e)}")
        
        # 只有在有新配置时才更新
        if new_config:
            update_config(new_config)
            print(f"成功更新配置: {new_config}")
            return jsonify({
                'success': True, 
                'message': f'配置已更新，成功上传 {len(uploaded_files)} 个文件', 
                'uploaded_files': uploaded_files
            })
        else:
            print("没有检测到有效的文件上传")
            return jsonify({'success': True, 'message': '未检测到有效文件上传', 'uploaded_files': []})
    
    except Exception as e:
        print(f"配置更新过程中出错: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            'success': False, 
            'message': f'更新配置失败: {str(e)}',
            'error_details': traceback.format_exc()
        }), 500

@app.route('/admin/get_leaderboard')
@admin_required
def admin_get_leaderboard():
    try:
        # 读取排行榜数据
        leaderboard = pd.read_csv(leaderboard_file)
        leaderboard = leaderboard.sort_values('rmse', ascending=True)
        
        # 处理NaN值，确保生成有效的JSON
        # 填充NaN值：phone字段为空字符串，rmse字段为999.999
        leaderboard = leaderboard.fillna({
            'phone': '',
            'rmse': 999.999,
            'username': '未知用户',
            'timestamp': '未知时间'
        })
        
        # 确保rmse是数值类型
        if 'rmse' in leaderboard.columns:
            leaderboard['rmse'] = pd.to_numeric(leaderboard['rmse'], errors='coerce').fillna(999.999)
        
        # 转换为字典列表并返回
        records = leaderboard.to_dict('records')
        return jsonify(records)
    except Exception as e:
        print(f'获取排行榜时出错: {str(e)}')
        # 返回空列表而不是抛出异常
        return jsonify([])

# 参加者管理路由
@app.route('/admin/get_participants')
@admin_required
def admin_get_participants():
    participants = get_participants()
    # 转换为列表格式，便于前端显示
    participants_list = [{'username': k, 'password': v} for k, v in participants.items()]
    return jsonify(participants_list)

@app.route('/admin/add_participant', methods=['POST'])
@admin_required
def admin_add_participant():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'success': False, 'message': '账号和密码不能为空'})
    
    try:
        add_participant(username, password)
        return jsonify({'success': True, 'message': '参加者添加成功'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'添加失败: {str(e)}'})

@app.route('/admin/delete_participant', methods=['POST'])
@admin_required
def admin_delete_participant():
    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify({'success': False, 'message': '请指定要删除的账号'})
    
    try:
        delete_participant(username)
        return jsonify({'success': True, 'message': '参加者删除成功'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'删除失败: {str(e)}'})



if __name__ == '__main__':
    # 运行在端口9009上
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

def main():
    """Console-script entrypoint for running EasyJudge."""
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)