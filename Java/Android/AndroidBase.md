---
title: Android基础
date: 2023-12-19 15:01:26
tags: 
categories: 
---

💠

- 1. [Android](#android)
    - 1.1. [adb](#adb)
- 2. [Tips](#tips)
    - 2.1. [Android和Linux传输文件](#android和linux传输文件)

💠 2023-12-19 15:01:38
****************************************
# Android 
> [developer.android.google.cn](https://developer.android.google.cn/)

1. [apktool](https://bitbucket.org/iBotPeaches/apktool/overview)

## adb
> Android Debug Bridge

> [Android 调试桥 (adb)](https://developer.android.com/studio/command-line/adb) | [Arch Wiki: Android Debug Bridge](https://wiki.archlinux.org/title/Android_Debug_Bridge)

- adb version
- adb devices 查看连接的设备 `前提安卓要开启开发者adb调试 和 确认授权的弹窗提示`
- adb pull 手机存储绝对路径 电脑绝对路径 `从手机拉文件到pc`
- adb push 电脑绝对路径 手机存储绝对路径


# Tips
## Android和Linux传输文件
- Termux 安装ssh
- adb 
- ftp webdav 协议互访问
