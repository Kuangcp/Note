---
title: VirtualBox
date: 2018-12-15 12:11:48
tags: 
    - VirtualBox
categories: 
    - 工具
---

**目录 start**

1. [VirtualBox](#virtualbox)
    1. [网络管理](#网络管理)
    1. [硬盘管理](#硬盘管理)
    1. [安装Linux](#安装linux)
        1. [Manjaro](#manjaro)
        1. [Deepin](#deepin)
    1. [安装Windows](#安装windows)
        1. [Windows7](#windows7)
    1. [安装 Android](#安装-android)
        1. [Android-x86](#android-x86)

**目录 end**|_2020-04-27 23:42_|
****************************************
# VirtualBox

## 网络管理
> [How to configure port forwarding in VirtualBox](https://www.simplified.guide/virtualbox/port-forwarding)

- Network -> Advanced -> Port forwarding -> host ip port(宿主机) guest ip port (虚拟机内系统)

************************

## 硬盘管理

> 添加新分区到虚拟机
1. Storge -> add Hard Dish ->  create Disk 选择大小, 创建完成后, 启动虚拟机就能看到挂载了, 再改下 /etc/fstab 就能自动挂载了

************************

## 安装Linux

### Manjaro
> 官网下载好对应的镜像文件

### Deepin

## 安装Windows

### Windows7

************************

## 安装 Android
> [参考: 5 Best Android Emulators for Linux](https://beebom.com/android-emulators-linux/)  

### Android-x86
> [下载](https://www.fosshub.com/Android-x86.html)  
> [参考: ](https://www.cnblogs.com/wynn0123/p/6288344.html)  

> 启动后不进图形化:
1. `mount –o remount,rw /mnt`
1. vi /mnt/grub/menu.lst  第一个块 kernel /android-8.1-rc2/kernel quiet 后空格，加上 nomodeset
1. 修改分辨率也是在这一行 UVESA_MODE 的值
