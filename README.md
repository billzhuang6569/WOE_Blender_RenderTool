# WOE_Blender_RenderTool


A Blender rendering command line targeted at users with no coding background.

It enables batch rendering, batch specifying of locations, and automatic organization of rendering folders.

一个Blender渲染命令行，针对无代码基础使用者。

可实现批量渲染、批量指定位置、自动组织渲染文件夹功能。

# 1.0功能

- 快速为Blender工程，创建空文件夹，用于存放渲染成果
- 批量工程渲染
- 快速指定渲染位置到各自空文件夹，还是到Blender工程设置
- 用户可自定义飞书机器人的Webhook地址
- 渲染完成后发送WOE团队飞书提示

# 未来功能

- 用户无需每次运行时选择Blender软件路径

# 使用方法

> 请注意：只能在Win运行

> 1下载本仓库，解压到【你的Blender工程所在文件夹】


	*确保Start.bat与blender文件在同一目录  
*示例  
C:/Render  
|-py/  
|-Start.bat  
|-1.blend  
|-2.blend  
|-3.blend
> 2 打开/py/conf.json，在双引号里填写你的webhook地址


	*webhook url可以在【飞书机器人助手】的【webhook】步骤里看到  
*你可以在飞书，自定义配置渲染完成后的操作
> 3点击Start.bat，首次运行，可能会安装python环境

> 4 选择对应功能


	[0] 扫描文件夹内所有的Blender工程，并创建同名空文件夹

	[1] 启动渲染程序  
- 自动创建空文件夹，用于存储渲染成果  
- 用户指定Blender安装位置  
- 指定渲染位置  
- 无人监管批量渲染  
- 渲染完成后发送飞书消息提示渲染完成

# 为啥做这个


团队已经被某汽车的3D片折磨很久了，十多个Blender文件每次渲染贼费劲。 

一个个打开选择渲染位置，啥时候渲染完了你也不知道。

最近正好在学python，作为练习搞了个程序，无需任何代码基础即可使用。

这是我们的科普视频频道，WhatOnEarth一探究竟：

[https://space.bilibili.com/410527811](https://space.bilibili.com/410527811)

我们也为客户制作各种创意动画视频，请查看官网：

[https://www.woe.show](https://www.woe.show)
