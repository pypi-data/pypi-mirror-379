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

# 包内根目录（安装后指向 site-packages/easyjudge）
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 显式指定模板目录，避免 TemplateNotFound
app = Flask(__name__, template_folder=os.path.join(ROOT_DIR, 'templates'))
app.secret_key = 'easyjudge_secret_key_2023'

# 运行期可写目录：将用户上传与评测放到工作目录下的 uploads/
# 若工作目录不可写，可以改为使用临时目录或用户家目录。
WORKDIR = os.getcwd()
UPLOAD_FOLDER = os.path.join(WORKDIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 包内默认下载资源目录（教师上传的默认放到工作目录的 download/，如果不存在则回退到包内）
PKG_DOWNLOAD_DIR = os.path.join(ROOT_DIR, 'download')
DOWNLOAD_FOLDER = os.path.join(WORKDIR, 'download')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# 将包内默认资源在首次运行时拷贝到工作目录（若不存在）
for name in ['数据集A.csv', '数据集B.csv', 'inference_template.py', 'BaseML库推理模板.py']:
    src = os.path.join(PKG_DOWNLOAD_DIR, name)
    dst = os.path.join(DOWNLOAD_FOLDER, name)
    if os.path.exists(src) and not os.path.exists(dst):
        try:
            shutil.copy(src, dst)
        except Exception:
            pass

# 配置文件与参与者存储在工作目录
PARTICIPANTS_FILE = os.path.join(WORKDIR, 'participants.json')
CONFIG_FILE = os.path.join(WORKDIR, 'config.json')

DEFAULT_CONFIG = {
    'training_data_path': '数据集A.csv',
    'test_data_path': '数据集B.csv',
    'inference_template_path': 'BaseML库推理模板.py',
    'admin_password': 'XEduPro'
}

def get_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=4)
        return DEFAULT_CONFIG
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def update_config(new_config):
    current_config = get_config()
    current_config.update(new_config)
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(current_config, f, ensure_ascii=False, indent=4)

def get_participants():
    if not os.path.exists(PARTICIPANTS_FILE):
        with open(PARTICIPANTS_FILE, 'w', encoding='utf-8') as f:
            json.dump({'admin': 'XEduPro'}, f, ensure_ascii=False, indent=4)
        return {'admin': 'XEduPro'}
    with open(PARTICIPANTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def update_participants(participants):
    with open(PARTICIPANTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(participants, f, ensure_ascii=False, indent=4)

def add_participant(username, password):
    participants = get_participants()
    participants[username] = password
    update_participants(participants)

def delete_participant(username):
    participants = get_participants()
    if username in participants:
        del participants[username]
        update_participants(participants)

leaderboard_file = os.path.join(WORKDIR, 'leaderboard.csv')
if not os.path.exists(leaderboard_file):
    pd.DataFrame(columns=['username', 'phone', 'rmse', 'timestamp']).to_csv(leaderboard_file, index=False)

@app.route('/')
def index():
    leaderboard = pd.read_csv(leaderboard_file)
    leaderboard = leaderboard.sort_values('rmse', ascending=True)
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

    user_folder = os.path.join(UPLOAD_FOLDER, username)
    os.makedirs(user_folder, exist_ok=True)

    dst_data_dir = os.path.join(user_folder, 'data')
    os.makedirs(dst_data_dir, exist_ok=True)

    config = get_config()
    test_filename = os.path.basename(config.get('test_data_path', ''))
    if not test_filename:
        return jsonify({'success': False, 'message': '系统未配置测试数据集文件名'}), 400

    src_test_path = os.path.join(DOWNLOAD_FOLDER, test_filename)
    if not os.path.exists(src_test_path):
        # 回退到包内默认
        fallback = os.path.join(PKG_DOWNLOAD_DIR, test_filename)
        if os.path.exists(fallback):
            src_test_path = fallback
    if not os.path.exists(src_test_path):
        return jsonify({'success': False, 'message': f'测试数据集不存在: {src_test_path}'}), 400

    try:
        shutil.copy(src_test_path, os.path.join(dst_data_dir, 'testB.csv'))
        # 兼容旧模板
        try:
            shutil.copy(src_test_path, os.path.join(dst_data_dir, '测试集A.csv'))
        except Exception:
            pass
    except Exception as e:
        return jsonify({'success': False, 'message': f'复制测试数据集失败: {str(e)}'}), 500

    model_path = os.path.join(user_folder, model_file.filename)
    python_path = os.path.join(user_folder, python_file.filename)
    model_file.save(model_path)
    python_file.save(python_path)

    try:
        if os.path.basename(model_path) != 'model.pkl':
            shutil.copy(model_path, os.path.join(user_folder, 'model.pkl'))
    except Exception as e:
        return jsonify({'success': False, 'message': f'准备兼容模型文件失败: {str(e)}'}), 500

    try:
        original_dir = os.getcwd()
        os.chdir(user_folder)

        if not os.path.exists('data/testB.csv'):
            raise FileNotFoundError('测试集文件 data/testB.csv 不存在，请检查路径！')

        try:
            result = subprocess.run(
                ['python', os.path.basename(python_path)],
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.returncode != 0:
                raise RuntimeError(f"用户代码运行出错：\n{result.stderr}")
        except subprocess.TimeoutExpired:
            raise TimeoutError("用户代码运行超时（超过60秒），请检查代码是否有死循环或效率问题。")
        except Exception as sub_e:
            raise RuntimeError(f"运行用户代码时发生异常：{str(sub_e)}")

        test_data_path = 'data/testB.csv'
        rmse = 999.999
        if os.path.exists("data/预测结果.csv"):
            try:
                y_pred_loaded = pd.read_csv("data/预测结果.csv")["预测值"].values
                test_df = pd.read_csv(test_data_path)
                y_true = test_df.iloc[:, -1].values
                rmse = np.sqrt(np.mean((y_true - y_pred_loaded) ** 2))
            except Exception:
                rmse = 999.999
        else:
            raise FileNotFoundError("未生成 data/预测结果.csv，请检查推理代码是否正确输出。")

        leaderboard = pd.read_csv(leaderboard_file)
        new_entry = pd.DataFrame({
            'username': [username],
            'phone': [''],
            'rmse': [rmse],
            'timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        })
        leaderboard = pd.concat([leaderboard, new_entry], ignore_index=True)
        leaderboard = leaderboard.sort_values('timestamp').drop_duplicates(['username'], keep='last')
        leaderboard.to_csv(leaderboard_file, index=False)

        return jsonify({'success': True, 'rmse': rmse, 'message': '提交成功，后续会按照排名赋分'})

    except Exception as e:
        print('推理异常:', str(e))
        print(traceback.format_exc())
        return jsonify({'success': False, 'message': f'处理文件时出错: {str(e)}'})
    finally:
        try:
            os.chdir(original_dir)
        except Exception:
            pass

@app.route('/download/training_data')
def download_training_data():
    config = get_config()
    filename = os.path.basename(config.get('training_data_path', ''))
    if not filename:
        return jsonify({'success': False, 'message': '训练数据集路径未配置'}), 404
    preferred = os.path.join(DOWNLOAD_FOLDER, filename)
    fallback = os.path.join(PKG_DOWNLOAD_DIR, filename)
    file_path = preferred if os.path.exists(preferred) else fallback
    if not os.path.exists(file_path):
        return jsonify({'success': False, 'message': '文件不存在'}), 404
    return send_file(file_path, as_attachment=True, download_name=filename)

@app.route('/download/inference_template')
def download_inference_template():
    config = get_config()
    filename = os.path.basename(config.get('inference_template_path', ''))
    if not filename:
        return jsonify({'success': False, 'message': '推理模板路径未配置'}), 404
    preferred = os.path.join(DOWNLOAD_FOLDER, filename)
    fallback = os.path.join(PKG_DOWNLOAD_DIR, filename)
    file_path = preferred if os.path.exists(preferred) else fallback
    if not os.path.exists(file_path):
        return jsonify({'success': False, 'message': '文件不存在'}), 404
    return send_file(file_path, as_attachment=True, download_name=filename)

# 管理端简化：仅保留获取/更新配置示例（可按你的原版拓展）
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return render_template('admin.html', need_login=True)
        return f(*args, **kwargs)
    return decorated_function

@app.route('/admin')
def admin():
    if session.get('admin_logged_in'):
        return render_template('admin.html', need_login=False)
    return render_template('admin.html', need_login=True)

@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    password = data.get('password')
    config = get_config()
    if password == config['admin_password']:
        session['admin_logged_in'] = True
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': '密码错误'})

@app.route('/admin/get_config')
@admin_required
def admin_get_config():
    return jsonify(get_config())

@app.route('/admin/update_config', methods=['POST'])
@admin_required
def admin_update_config():
    try:
        uploaded_files = []
        new_config = {}
        if 'training_data_file' in request.files:
            f = request.files['training_data_file']
            if f.filename:
                safe = os.path.basename(f.filename)
                f.save(os.path.join(DOWNLOAD_FOLDER, safe))
                uploaded_files.append(safe)
                new_config['training_data_path'] = safe
        if 'test_data_file' in request.files:
            f = request.files['test_data_file']
            if f.filename:
                safe = os.path.basename(f.filename)
                f.save(os.path.join(DOWNLOAD_FOLDER, safe))
                uploaded_files.append(safe)
                new_config['test_data_path'] = safe
        if 'inference_template_file' in request.files:
            f = request.files['inference_template_file']
            if f.filename:
                safe = os.path.basename(f.filename)
                f.save(os.path.join(DOWNLOAD_FOLDER, safe))
                uploaded_files.append(safe)
                new_config['inference_template_path'] = safe
        if new_config:
            update_config(new_config)
            return jsonify({'success': True, 'uploaded_files': uploaded_files})
        return jsonify({'success': True, 'uploaded_files': []})
    except Exception as e:
        return jsonify({'success': False, 'message': f'更新配置失败: {str(e)}'}), 500

def run():
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)


