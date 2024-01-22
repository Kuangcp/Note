---
title: Java初始化环境搭建
date: 2018-12-15 12:01:26
tags: 
    - 工具使用经验
categories: 
---

💠

- 1. [配置Deepin的Java开发环境](#配置deepin的java开发环境)
    - 1.1. [新增用户](#新增用户)
    - 1.2. [安装Docker](#安装docker)
- 2. [在Linux上配置Java环境](#在linux上配置java环境)
    - 2.1. [配置JDK](#配置jdk)
        - 2.1.1. [解压配置](#解压配置)
    - 2.2. [配置MySQL](#配置mysql)
    - 2.3. [配置Redis](#配置redis)
    - 2.4. [问题以及解决方案](#问题以及解决方案)

💠 2024-01-22 09:40:06
****************************************
# 配置Deepin的Java开发环境

修改Hostname需要重启, 设置默认java需要重启, docker添加用户组需要重启
## 新增用户
> [详细文档](/Linux/Base/LinuxBase.md#用户管理)

## 安装Docker
> [详细文档](/Linux/Container/Docker.md#安装与卸载)

# 在Linux上配置Java环境
> [SDK Man 方式安装](/Skills/AppManual.md#sdkman)

## 配置JDK
### 解压配置
- [下载地址](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
- 在文件 `/etc/profile` 中添加

```sh
    export JAVA_HOME= 绝对路径例如： /home/kcp/Application/sdk/jdk1.8.0_131
    export JRE_HOME=${JAVA_HOME}/jre
    export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
    export PATH=${JAVA_HOME}/bin:$PATH
```
> 让修改立即生效`source /etc/profile` 或者修改 `.bashrc` 文件, 就会在当前用户的终端生效

**root用户的环境**
- 指定默认的jdk，因为系统预装了openJdk ,为了稳妥建议先进入JDK的bin目录,然后执行
```sh
    sudo update-alternatives --install /usr/bin/java java `pwd`/java 300
    sudo update-alternatives --install /usr/bin/javac javac `pwd`/javac 300
```
- 或者不执行命令, 直接修改链接文件即可完成同样的目的
> 后期更新JDK版本, 普通用户的话, 就只是需要更改 `.bashrc` 文件, root用户就执行以上命令, 或者直接重建软链接文件
>> root 用户下 `which java` 然后 `ls -l 显示的路径` 一直往下找, 找到 `/etc/alternatives/java` 和 `/etc/alternatives/javac` 重建这两个软链接.

************************

## 配置MySQL
> [安装MySQL](/Database/MySQL.md#安装)

************************
## 配置Redis
> [安装Redis](/Database/Redis.md#安装和配置)

## 问题以及解决方案
> QQ
- `sudo apt-get install deepin-crossover deepinwine-qq`
- [安装QQ](https://www.findhao.net/easycoding/1748)

> 显卡问题
- 联想G4070 安装 deepin 15.4.1 显卡兼容失败（15.4还能正常用）, 15.5 15.6 是正常使用的 15.7 有点缺陷
- 因为合上盖子休眠就会导致打开电脑直接死机， 找了半天原因是驱动问题
    - 安装 `nvidia-driver`, `nvidia-setting`, `bumblebee-nvidia` 即可解决

手残，按到关闭窗口特效后，就无法打开了，各种用着不爽， 然后重装了最新版系统，然后就装驱动，重启就不能开特效了。。。。。
虽然各种小bug, 也花费了很多时间来解决这些问题(因为自己有强迫症), 但是还是学到了很多东西

********************

> [双硬盘的折腾记录](/MyBlog/2018-3-15-install-deepin.md)
