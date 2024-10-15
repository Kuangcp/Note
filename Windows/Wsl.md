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

## GUI
> [wslg](https://github.com/microsoft/wslg)  
> [Run Linux GUI apps with WSL | Microsoft Learn](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)  


# WSA
[适用于 Android™️ 的 Windows 子系统](https://learn.microsoft.com/zh-cn/windows/android/wsa/)
