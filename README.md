# WOE_Blender_RenderTool
A Blender rendering command line targeted at users with no coding background. 
It enables batch rendering, batch specifying of locations, and automatic organization of rendering folders.
一个Blender渲染命令行，针对无代码基础使用者。
可实现批量渲染、批量指定位置、自动组织渲染文件夹功能。


# 1.0功能
- 快速为Blender工程，创建空文件夹，用于存放渲染成果
- 批量工程渲染
- 快速指定渲染位置到各自空文件夹，还是到Blender工程设置
- 渲染完成后发送WOE团队飞书提示

# 未来功能
- 用户可自定义飞书机器人的Webhook地址
- 用户无需每次运行时选择Blender软件路径

# 使用方法
0 下载本仓库，解压到【你的Blender工程所在文件夹】

    *确保Start.bat与blender文件在同一目录
    *示例
    C:/Render
        |-py/
        |-Start.bat
        |-1.blend
        |-2.blend
        |-3.blend

1 点击Start.bat，首次运行，可能会安装python环境

2 选择对应功能：
    [0]扫描文件夹内所有的Blender工程，并创建同名空文件夹
    [1]启动渲染程序
        -自动创建空文件夹，用于存储渲染成果
        -用户指定Blender安装位置
        -用户指定渲染位置
        -无人监管批量渲染
        -渲染完成后发送飞书消息提示渲染完成




