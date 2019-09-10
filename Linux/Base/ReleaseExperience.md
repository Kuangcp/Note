---
title: Linux发行版
date: 2018-12-15 11:19:21
tags: 
    - 工具使用经验
categories: 
    - Linux
---

**目录 start**
 
1. [Linux常见发行版](#linux常见发行版)
    1. [基础知识](#基础知识)
        1. [安装系统](#安装系统)
    1. [服务器系统之争](#服务器系统之争)
    1. [Debian](#debian)
        1. [Debain](#debain)
        1. [Ubuntu](#ubuntu)
        1. [Ubuntu Mint](#ubuntu-mint)
        1. [Deepin](#deepin)
        1. [raspberry-pi](#raspberry-pi)
    1. [Arch](#arch)
        1. [Arch](#arch)
        1. [manjaro](#manjaro)
    1. [RedHat](#redhat)
        1. [Fedora](#fedora)
        1. [Centos](#centos)
        1. [openSUSE](#opensuse)
    1. [FreeBSD](#freebsd)
    1. [Solaris](#solaris)
    1. [Alpine](#alpine)
    1. [Gentoo](#gentoo)
    1. [Mageia](#mageia)
    1. [CDLinux](#cdlinux)

**目录 end**|_2019-05-27 13:44_|
****************************************
# Linux常见发行版
> [Repology](https://repology.org/)

> [论最适合开发用的几款Linux桌面系统](https://www.lulinux.com/archives/3614)
> [发行版热度对比](https://distrowatch.com/dwres.php?resource=popularity)
> [Linux的发行版本及不同版本的联系和区别。](https://www.jianshu.com/p/c88a62ac8ca3?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)
> [Linux十大顶级发行版本](https://www.jianshu.com/p/13d399608880?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)
> [linux 的不同的发行版区别和联系](https://www.jianshu.com/p/b796ead65995?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)

- [谈 Linux，Windows 和 Mac](http://www.yinwang.org/blog-cn/2013/03/07/linux-windows-mac)

## 基础知识
> 下载安装时要选平台 [相关博客](http://downtoearthlinux.com/posts/x86-i386-x86-64-x64-and-amd64-oh-my/)
>> 64: x86-64 =  x64  =  amd64  
>> 32: x86  =  i386

> [查看发行版](/Linux/Base/LinuxDirectoryStructure.md#查看发行版)

- [2018年wine QQ最完美解决方案（多Linux发行版通过测试并稳定运行）](https://www.lulinux.com/archives/1319)

### 安装系统
> 制作U盘启动盘

- Manjaro
    - rufus: 在windows上制作, 选用dd模式
- Deepin
    1. 系统内置的 启动盘制作工具, 或者官网下Windows版
    2. 或者用软碟通
- Ubuntu
    1. 软碟通

> 系统安装
- 现在大多电脑都是预装win10, 所以为了方便, 双系统更好用
1. 首先一点就是引导模式 现在大多是 UEFI, 所以为了不影响 windows, 关闭 UEFI, 使用 Legacy模式安装Linux 这样的话, 打开UEFI就进了Windows 关闭就进了Linux 对Windows没造成任何影响
1. 在Windows上 我的电脑-> 硬盘管理 -> 选择一个分区,压缩出空闲空间出来 用于安装Linux(日常用最少80g 尽管系统最低占用大概10g左右)
1. 将U盘插上, 进入系统安装的引导, 选好语言, 用户 密码什么的
1. 分区 分为 / 和 /home 就行了, / 40g 其余给/home (个人分100g才够用) 千万注意不要选错分区
1. 引导会自动追加到硬盘引导分区, 不会覆盖原有系统, 目前 manjaro deepin windows10 三系统双硬盘并存
1. 安装完成, 重启前拔掉U盘 即可

> [参考博客: 迁移到 GRUB 2](https://www.ibm.com/developerworks/cn/linux/l-grub2/)

> UEFI  | [Doc](https://wiki.manjaro.org/index.php?title=UEFI_-_Install_Guide)

## 服务器系统之争
> [服务器操作系统应该选择 Debian/Ubuntu 还是 CentOS？](https://www.zhihu.com/question/19599986)  
> [CentOS vs CoreOS – Which OS to choose for your Docker web hosting services](https://bobcares.com/blog/centos-vs-coreos-os-for-docker-web-hosting/2/)

**********************************************

## Debian
> Debian系 包含 Debian *buntu Deepin 等等

### Debain
[Debian](/Linux/Debian/Debian.md)

### Ubuntu
[Ubuntu](/Linux/Debian/Ubuntu.md)

### Ubuntu Mint
> 作为桌面版系统, 基于Ubuntu, 使用更为简单 也有更多的窗口管理器可以选择

### Deepin
[Deepin](/Linux/Debian/Deepin.md)

### raspberry-pi
- [树莓派桌面版下载](https://www.raspberrypi.org/downloads/raspberry-pi-desktop/) `分辨率不知道怎么调, 资源的消耗倒是低`

******************
## Arch
### Arch
> 滚动发行，包管理机制优秀

- [打造完美的 Linux 桌面 — Arch Linux 2007.08-2 (1)](https://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-1.html)
    - [打造完美的 Linux 桌面 — Arch Linux 2007.08-2 (2)](https://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-2.html)
    - [打造完美的 Linux 桌面 — Arch Linux 2007.08-2 (3)](https://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-3.html)
    - [打造完美的 Linux 桌面 — Arch Linux 2007.08-2 (4)](https://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-4.html)
    
### manjaro
> [官网](https://manjaro.org/community-editions/)
> [人生苦短我用Manjaro](https://www.manjaro.cn/451) | [什么Linux发行版软件最多？](https://www.lulinux.com/archives/2787)
> | [Manjaro: 一种不同的野兽](https://www.manjaro.cn/195) | [为什么要用Manjaro？](https://www.manjaro.cn/150)

- 因为基于arch, 并且简化了很多操作, 还兼容了Deepin桌面, 真是稳了, 但是日常生活中
- 因为滚动更新的特性, 所以在安装一个新软件的时候, 需要更新到最新版, 这样就比较烦, 

****************************
## RedHat
> 大厂支持 侧重于服务器领域

### Fedora
> redhat的试验场 不太感冒

### Centos

### openSUSE

************************
## FreeBSD

*******************
## Solaris

**********************
## Alpine
> 特别小，在docker中使用有优势

## Gentoo
> 入门难度大，适合资深玩家，据说是特能折腾的系统，处于鄙视链顶端

## Mageia
> [官网](http://www.mageia.org/zh-cn/)

## CDLinux
> 小巧的Linux发行版, 带有很多工具 
