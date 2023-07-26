#全局设置
import os
import subprocess

#脚本信息
name = 'Render_Tool'
version = '1.0.0'
author = 'Bill Zhuang'
intro = '为WOE团队Blender渲染准备的工具包'

#菜单信息
menu_list = {
    0: '建立空文件夹',
    1: '开始Blender渲染',
}

#功能
# 获取Menu.py的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构造0_Create_Folders.py的完整路径
Create_Folders_Path = os.path.join(current_dir, 'Create_Folders.py')
Render_Blender_Path = os.path.join(current_dir, 'Render_Blender.py')
SendWebhook_Path = os.path.join(current_dir, 'SendWebhook.py')


def welcome():
    print(f'-----------------')
    print(f'Welcome!')
    print(f'This is a rendering tool made for WOE Team to render Blender files.')
    print(f'Please Contact Bill by E-mail billzhuang@woe.show')
    print(f'-----------------')
    print(f'[{name}] coded by [{author}]')
    print(version)
    print(intro)
    print(f'-----------------')


def menu():
    print(f'【功能菜单】')
    for key, value in menu_list.items():
        print(f'[{key}] {value}')
    func_id = input('请输入对应工具的序号：')
    return func_id

def backtoMenu():
    print('')
    print('')
    print(f'-----------------')
    print(f'[0]返回主菜单')
    print(f'[1]退出')
    i = input(f'请输入：')

    if i == '0':
        print('')
        print('')
        print(f'-----------------')
        menu()
    elif i =='1':
        exit()

if __name__ == '__main__':
    welcome()
    func_id = menu()
    if func_id == '0':
        subprocess.run(['python', Create_Folders_Path])
    if func_id == '1':
        subprocess.run(['python', Render_Blender_Path])
