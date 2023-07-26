import os
import sys


# 获取路径信息
current_file_path = os.path.abspath(sys.argv[0])  #py所在路径
current_dir = os.path.dirname(current_file_path)  #py所在文件夹
parent_dir = os.path.dirname(current_dir)  #py上一级文件夹

#询问用户
def ask_user():
    print(f'[1] Start.bat与Blender工程在同一目录 *推荐')
    print(f'[2] 输入路径')
    id = input(f'请输入序号：')
    return int(id)

def create_folders(path):
    new_folders = []
    for name in os.listdir(path):
        if name.endswith('.blend'):
            filename_without_ext = os.path.splitext(name)[0]
            new_folders.append(filename_without_ext)
            new_folder_path = os.path.join(path, filename_without_ext)
            os.makedirs(new_folder_path, exist_ok=True)
    if new_folders == []:
        print(f'未找到blender文件')
    else:
        for folder in new_folders:
            print(f'已创建文件夹：{folder}')

id = ask_user()

if id ==1 :
    path = parent_dir
elif id ==2:
    print(f'输入示例：D:/Render')
    path = input(f'请输入路径：')
else:
    print(f'输入有误，请重新输入')
    ask_user()

create_folders(path)

import Menu
Menu.backtoMenu()

