---
title: Wsl
date: 2024-09-05 11:52:54
tags: 
categories: 
---

💠

- 1. [WSL](#wsl)
- 2. [WSL2](#wsl2)
    - 2.1. [GUI](#gui)
- 3. [WSA](#wsa)

💠 2024-10-15 09:56:12
****************************************
# WSL 
> [Official Doc](https://learn.microsoft.com/zh-cn/windows/wsl/install)

> [利用WSL打造Arch开发环境](https://zhuanlan.zhihu.com/p/51270874)

# WSL2
- `启动发行版` wsl -d Name

> 更换磁盘地址

- 导出已有发行版 `wsl --export Ubuntu D:/wsl/Ubuntu-disk.tar` 
- 导入成为新的发行版并设置数据存放目录 `wsl --import Ubuntu2 D:/wsl/Ubuntu2 D:/wsl/Ubuntu-disk.tar`
- 删除旧发行版 `wsl --unregister Ubuntu`

## 实践

有个很大的困境, 假如想同时享用Linux和Windows的工具链 就会很麻烦, 困境来自 WSL2访问Windows文件系统是走9P网络协议的,IO慢10倍, Windows读WSL2的文件系统也是特殊协议, 需要每个软件都支持才可以

例如: 有一个Java项目, 想在Linux里完成 镜像打包分发 tmux 多终端 运行,和调试jvm,看日志,docker搭环境 一系列工作, 但是又想在IDEA里调试代码, 就会有个问题, 项目文件放在哪里
- 放在WSL2里 命令行的交互会和Linux一模一样,但是 Windows的 IDEA 浏览器等各种工具需要兼容文件协议才可以
- 放在Windows, IO性能暴跌, Windows不支持文件级别权限, WSL2 内打开都是777的权限, git做代码管理会乱套.

如果文件还是放在Windows上, 用MSYS2 当做更好的终端来调用Windows的所有工具(但是需要配置环境变量共享等一系列配置), 体验会更好, 然后WSL就可以用来跑Docker等强Linux的依赖. 

## GUI
> [wslg](https://github.com/microsoft/wslg)  
> [Run Linux GUI apps with WSL | Microsoft Learn](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)  


# WSA
[适用于 Android™️ 的 Windows 子系统](https://learn.microsoft.com/zh-cn/windows/android/wsa/)
