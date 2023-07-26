import subprocess
import glob
import platform
import os
import json
from datetime import datetime

# 检测操作系统类型
os_type = platform.system()
blender_exe = ''

# 确认Blender路径
def ask_user_win():
    print('')
    print('')
    print(f'-----------------')
    print(f'[1] 输入Blender安装盘符(C/D/E/F)')
    print(f'[2] 自己输入完整路径')
    i = input(f'请输入序号：')
    print(f'-----------------')
    return int(i)

def checkpath(path):
    if not os.path.exists(path):
        print("路径不存在：", path)
        blender_exe = getBlender()
        return

    if not os.path.isfile(path):
        print("路径不是一个文件：", path)
        blender_exe = getBlender()
        return

def getBlender():
    if os_type == 'Windows':
        id = ask_user_win()
        if id == 1:
            print('')
            print('')
            print(f'-----------------')
            user_input= input(f'请输入Blender安装盘符：')
            file_path = r"Program Files\Blender Foundation\Blender 3.4\blender-launcher.exe"
            blender_exe = os.path.join(user_input + ':', file_path)
        elif id == 2:
            print('')
            print('')
            print(f'-----------------')
            print(r'路径示例：D:\Program Files\Blender Foundation\Blender 3.4\blender-launcher.exe')
            user_input = input(f'请输入完整路径：')
            blender_exe = user_input

    elif os_type == 'Darwin':  # Mac OS
        blender_exe = "/Applications/Blender.app/Contents/MacOS/Blender"
    else:
        print("不支持的操作系统类型。")
        exit()
    checkpath(blender_exe)
    return blender_exe

# 菜单
menu_list = {
    1: '开始渲染，输出位置：【工程同名文件夹】',
    2: '开始渲染，输出位置：【按Blender工程设置】'
}

def menu():
    print('')
    print('')
    print(f'-----------------')
    print(f'【开始渲染】')
    for key, value in menu_list.items():
        print(f'[{key}] {value}')
    func_id = input('请输入对应工具的序号：')
    return func_id

# 获取每个工程对应的渲染位置
def Render_Path():
    # 获取当前 py 脚本所在的目录
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # 获取上一级目录
    parent_dir = os.path.dirname(current_dir)
    # 搜索所有 .blend 文件
    search_file = os.path.join(parent_dir, "*.blend")
    blend_files = glob.glob(search_file, recursive=False)

    blend_and_render_path = {}
    for file in blend_files:
        # 获取 .blend 文件所在目录
        file_dir = os.path.dirname(file)
        # 获取 .blend 文件名（不含后缀）
        file_name = os.path.splitext(os.path.basename(file))[0]
        # 创建子目录路径
        sub_dir = os.path.join(file_dir, file_name)
        # 如果子目录不存在，创建子目录
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)
        # 更新字典
        blend_and_render_path[file] = sub_dir

    return blend_and_render_path, blend_files


# 开始渲染所有blender文件，并将渲染路径指定到同名文件夹
def Render_to_Folder(blender_exe, blend_files, blend_and_render_path):
    finish = []
    for blend_file in blend_files:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f' ')
        print(f'-----------------')
        print(f'正在渲染{blend_file} at {now}')

        # 获取渲染路径
        render_path = blend_and_render_path[blend_file]

        # 设置渲染命令
        command = [blender_exe, "-b", blend_file, "-o", os.path.join(render_path, "frame_#####"), "-a"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # 打印 Blender 的输出
        for line in process.stdout:
            print(line.decode().strip())

        # 等待 Blender 进程结束
        process.wait()

        # 获取当前时间
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'已侦测到渲染完成: {blend_file} at {now}')
        print(f'-----------------')
        print(f' ')
        finish.append({'Blender工程': blend_file, '完成时间': now})

    return finish

def Render_to_Setting(blender_exe, blend_files):
    finish = []
    for blend_file in blend_files:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f' ')
        print(f'-----------------')
        print(f'正在渲染{blend_file} at {now}')

        # 设置渲染命令
        command = [blender_exe, "-b", blend_file, "-a"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # 打印 Blender 的输出
        for line in process.stdout:
            print(line.decode().strip())

        # 等待 Blender 进程结束
        process.wait()

        # 获取当前时间
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'已侦测到渲染完成: {blend_file} at {now}')
        print(f'-----------------')
        print(f' ')
        finish.append({'Blender工程': blend_file, '完成时间': now})

    return finish

#发送Webhook
# 获取Menu.py的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构造0_Create_Folders.py的完整路径
SendWebhook_Path = os.path.join(current_dir, 'SendWebhook.py')
def SendWebhook(finish):
    for i in finish:
        print(i)

    with open('finish.json', 'w') as f:
        json.dump(finish, f)

    subprocess.run(['python', SendWebhook_Path])




# Main
blender_exe = getBlender()

func_id = menu()
blend_and_render_path, blend_files = Render_Path()
if func_id == '1':
    finish = Render_to_Folder(blender_exe, blend_files, blend_and_render_path)
    SendWebhook(finish)
if func_id == '2':
    finish = Render_to_Setting(blender_exe, blend_files)
    SendWebhook(finish)



