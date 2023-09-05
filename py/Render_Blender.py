import subprocess
import glob
import platform
import os
import json
from datetime import datetime

# 检测操作系统类型
os_type = platform.system()
blender_exe = ''

# 读取Conf
def Read_Conf():
    with open('conf.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    alarm_start = config.get('alarm_start', None)
    alarm_finish = config.get('alarm_finish', None)
    return alarm_start, alarm_finish


# 询问Blender路径
def Get_Path():

    if os_type == 'Windows':
        Conf_Path = Get_Conf_Path()
        check_path = checkpath(Conf_Path)
        if check_path == True:
            Blender_Path = Conf_Path
            print(f'你的Blender路径：')
            print(Blender_Path)
        else:
            print('')
            print('')
            print(f'-----------------')
            print(f'未在conf.json中检测到有效路径')
            print(f'接下来请设置Blender路径')
            print(f'右键点击Blender快捷方式，复制属性中的路径')
            print(f'请不要复制引号')
            print(f'-----------------')
            print(f'你的路径应该类似这样：')
            print(r'D:\Program Files\Blender Foundation\Blender 3.4\blender-launcher.exe')
            print(f'-----------------')
            while True:  # 无限循环，直到找到有效的路径
                user_input = input('请输入你复制的路径：')
                check_path = checkpath(user_input)

                if check_path:  # 如果路径有效
                    Blender_Path = user_input
                    Write_Conf_Path(Blender_Path)
                    print(f"设置成功，你的Blender路径是 {Blender_Path}")
                    break  # 跳出循环
                else:  # 如果路径无效
                    print("路径无效或文件不存在，请重新输入.")
    elif os_type == 'Darwin':
        Blender_Path = "/Applications/Blender.app/Contents/MacOS/Blender"
    else:
        print("不支持的操作系统类型。")
        exit()

    return Blender_Path



# 检查conf中的Blender路径
def Get_Conf_Path():
    # 检查conf.json，若是空，返回0
    with open('conf.json', 'r', encoding='utf-8') as f:
        conf_data = json.load(f)

    Blender_Path = conf_data.get('blender_path','')
    is_valid_path = checkpath(Blender_Path)
    if is_valid_path:
        return Blender_Path
    else:
        return False

# 写入路径到conf.json
def Write_Conf_Path(path):
    with open('conf.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    config['blender_path'] = path

    with open('conf.json', 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4)



# 检查Blenderpath是否合法
def checkpath(path):
    if path == False:
        return False
    elif os.path.exists(path):
        return True
    else:
        return False




# 菜单
menu_list = {
    1: '渲染到【.blend文件同名文件夹】',
    2: '渲染到【Blender工程目标文件夹】'
}


# 用户输入菜单
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
    start = []
    finish = []

    print('以下Blender文件将被渲染：')
    for blend_file in blend_files:
        print(blend_file)


    print(f'-----------------')

    for blend_file in blend_files:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f' ')
        print(f'-----------------')
        print(f'正在渲染{blend_file} at {now}')

        #发送消息
        alarm_start, alarm_finish = Read_Conf()
        if alarm_start == 'True':
            start.append({'提示': '渲染开始！', 'Blender工程': blend_file, '开始时间': now})

        SendWebhook(start)

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
    start = []
    finish = []

    print('以下Blender文件将被渲染：')
    for blend_file in blend_files:
        print(blend_file)

    print(f'-----------------')

    for blend_file in blend_files:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f' ')
        print(f'-----------------')
        print(f'正在渲染{blend_file} at {now}')

        #发送消息
        alarm_start, alarm_finish = Read_Conf()
        if alarm_start == 'True':
            start.append({'提示': '渲染开始！', 'Blender工程': blend_file, '开始时间': now})

        SendWebhook(start)

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





blender_exe = Get_Path()
func_id = menu()
blend_and_render_path, blend_files = Render_Path()


if func_id == '1':
    finish = Render_to_Folder(blender_exe, blend_files, blend_and_render_path)
    SendWebhook(finish)
if func_id == '2':
    finish = Render_to_Setting(blender_exe, blend_files)
    SendWebhook(finish)


