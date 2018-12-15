---
title: Linux发行版
date: 2018-12-15 11:19:21
tags: 
    - 工具使用经验
categories: 
    - Linux
---

**目录 start**
 
1. [Linux各个发行版本使用体验](#linux各个发行版本使用体验)
    1. [基础知识](#基础知识)
        1. [安装系统](#安装系统)
    1. [服务器系统之争](#服务器系统之争)
    1. [Debian系](#debian系)
        1. [Debian](#debian)
        1. [Ubuntu](#ubuntu)
        1. [Ubuntu Mint](#ubuntu-mint)
        1. [Deepin](#deepin)
            1. [关于显卡](#关于显卡)
            1. [双系统安装](#双系统安装)
        1. [raspberry-pi](#raspberry-pi)
    1. [arch系](#arch系)
        1. [manjaro](#manjaro)
    1. [redhat系](#redhat系)
        1. [Fedora](#fedora)
        1. [Centos](#centos)
        1. [openSUSE](#opensuse)
    1. [FreeBSD](#freebsd)
    1. [Solaris](#solaris)
    1. [alpine](#alpine)
    1. [Gentoo](#gentoo)
    1. [Mageia](#mageia)
    1. [CDLinux](#cdlinux)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Linux各个发行版本使用体验

> [论最适合开发用的几款Linux桌面系统](https://www.lulinux.com/archives/3614)
> [发行版热度对比](https://distrowatch.com/dwres.php?resource=popularity)
> [Linux的发行版本及不同版本的联系和区别。](https://www.jianshu.com/p/c88a62ac8ca3?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)
> [Linux十大顶级发行版本](https://www.jianshu.com/p/13d399608880?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)
> [linux 的不同的发行版区别和联系](https://www.jianshu.com/p/b796ead65995?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)

- [谈 Linux，Windows 和 Mac](http://www.yinwang.org/blog-cn/2013/03/07/linux-windows-mac)

## 基础知识
> 下载安装时要选平台 参考[相关博客](http://downtoearthlinux.com/posts/x86-i386-x86-64-x64-and-amd64-oh-my/)
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

## 服务器系统之争
> [服务器操作系统应该选择 Debian/Ubuntu 还是 CentOS？](https://www.zhihu.com/question/19599986)  
> [CentOS vs CoreOS – Which OS to choose for your Docker web hosting services](https://bobcares.com/blog/centos-vs-coreos-os-for-docker-web-hosting/2/)

> 2018-04-01 17:17:19  
> 个人来讲, 菜鸡一个,但是习惯了Ubuntu16,也尝试过centos7, 还行之匆匆的两个服务器都装了centos, 然后俩都出问题了,都不想去百度找解决方案了,正常操作都能报错? 很棒棒
> 正在尝试Debian8 还是debian系习惯了

**********************************************

## Debian系
### Debian
> 很古老但是很好用的系统 [官网](https://www.debian.org/index.zh-cn.html)

> [参考博客: Debian8最小安装](https://www.howtoforge.com/tutorial/debian-8-jessie-minimal-server/)
- 奇怪的是我在虚拟机里装了好几个好几次装不上, 装完一登录就只有壁纸

_服务器_
- 2018-04-01 17:19:50 作为服务器系统安装完Debian8.2 85M内存占用 docker 是1.6
- 2018-04-10 10:35:54 服务器安装Ubuntu16.04 71M内存 docker是1.13

### Ubuntu
> 很多人的入门系统, 作为个人服务器也是首选, 软件比较新

> [Ubuntu Server Tutorial](https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-server#0) | [网易镜像源](http://mirrors.163.com/ubuntu-releases/)`只有网易有server版的镜像`

### Ubuntu Mint
> 作为桌面版系统, 该有的都有了, 个人比较喜欢

### Deepin
> [官方wiki](wiki.deepin.org)
> [参考博客: 一些工具](https://bbs.deepin.org/forum.php?mod=viewthread&tid=143022z)
- [FAQ](https://bbs.deepin.org/forum.php?mod=viewthread&tid=146921&extra=page%3D1)

- 优点:
    - 界面美观,自带CrossOver深度家族的软件也挺好用,自定义命令的快捷键
- 缺点:
    - 基本是Linux的共性了,就是驱动问题, NVIDIA 显卡 因为驱动问题重装四五次系统,重启就不知道多少次了
    - 输入法现在这几天也在作妖 fcitxCPU占用高,输入窗口消失等问题
    - 蓝牙模块时隐时现

`遇到的bug记录`
- 2018-01-09 19:29:25 休眠结束系统卡死,然后重启输入法没有窗口,然后升级到最新重启还是没有,杀掉搜狗进程再启动解决

- 2018-03-15 09:25:47 [公司电脑安装Windows10 和 Deepin双系统](/MyBlog/2018-3-15-install-deepin.md)

- 2018-05-24 15:08:49 `Gtk-WARNING **: 无法在模块路径中找到主题引擎：“adwaita”`， 安装 这个包 gnome-themes-standard

- 2018-06-15 19:50:40 deepin-wm 进程, 也就是Deepin的桌面管理器, 启动久了之后就会发生内存占用非常大的情况, 关闭窗口特效, 再打开就好了

- 2018-08-21 20:34:07 更新到15.7, 然后就是一堆的小问题, 任务栏和屏幕边缘有空隙, 多任务切换方式的变化, 原先用Wine安装的企业QQ不能启动... 但是确实Deepin 现在更快了
    - 使用闭源驱动方案, 休眠一会就卡死了, 只能强制关机, 尝试了开源驱动后, 也是一样 显卡是 Nvidia GTX1050

- 2018-08-23 09:55:15 遭遇用过的最大问题, 笔记本升级到15.7后有显卡明显不兼容, 各种显示上的卡顿, 切换Prime解决方案后, 内核load不进来, 启动不了了
    - 配置是 显卡 NVIDIA 840m 也许重装Deepin15.7, 也许装Manjaro-KDE
    - 最终是进的恢复模式, 卸载了无用的包就成功进入了, 但是发现自动挂载分区的文件都被注释了, 如果手动添加, 即使mount -a 没有报错, 但是启动时就加载不了分区
    - 又得进恢复模式注释掉, 才能进入系统

- 2018-09-02 21:44:21 ` Driver 'pcspkr' is already registered, aborting,`
    >- [参考博客: 社区帖子](https://bbs.deepin.org/forum.php?mod=viewthread&tid=166517&highlight=pcspkr)

- 2018-11-22 10:19:27 
    - 升级到 15.8 后 xorg 和 deepin-wm 内存泄露, 显卡是 GTX1060x 笔记本的 820m 没有这种情况出现
    - 用上半天, 这俩内存能占用到 3个g

#### 关于显卡
> [参考博客: 显卡驱动作死录](https://www.jianshu.com/p/f53c8223bac6)

> 个人折腾的整理
当前系统为 Deepin15.7 已经支持多种解决方案了, 还有一个 `深度显卡驱动管理器`
1. Intel默认驱动(也就是集显) 
1. NVIDIA开源驱动 性能不好, 解析闭源驱动而来
1. 大黄蜂方案 采用闭源驱动, 省电
1. PRIME方案 高性能

但是和我笔记本完美兼容的是 大黄蜂方案, 也就是之前安装的 `nvidia-driver`, `nvidia-setting`, `bumblebee-nvidia` 这一系列包
PRIME方案切换后差点把内核挂了, 一顿瞎操作把系统救活了

#### 双系统安装
- 首先进入BIOS关闭 安全启动, 选择引导方式为Legacy关闭UEFI win8以上则要关闭快速启动, 
    - 制作启动U盘, 然后选择从U盘启动, 进行安装, 分区 / 和 /home / 30-40g就足够, 如果你所用的软件都习惯性解压运行的话
    - 安装完成后一般是Deepin的默认引导取代了winsows引导, 即可正常使用, 进入windows,Deepin的引导也有该入口
    - 如果想默认进windows, 那么修改BIOS 改回UEFI即可

- 固态加机械的电脑:
    - 一样的关闭 安全启动, UEFI 
    - 在固态中划分出300M左右的空间出来, 在安装的时候设为 /Boot 然后将 / 和 /home照常放在机械上即可
    - 在启动时, 打开引导菜单, 选择固态即可正常启动Deepin
    - 同样的修改BIOS 回 UEFI 就默认进WIndows了

> 但是有时候有的电脑打开UEFI也能正常安装, 所以装系统要大胆的尝试, Deepin安装没有造成过数据损失

### raspberry-pi
- [树莓派桌面版下载](https://www.raspberrypi.org/downloads/raspberry-pi-desktop/) `分辨率不知道怎么调, 资源的消耗倒是低`

******************
## arch系
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
## redhat系
> 大厂支持
### Fedora
> redhat的试验场 不太感冒

### Centos
> 在阿里云上装了一个, 开机82M Centos7.4 然后装个nginx就挂了 稳定?  
> 不管,就是要黑一波, 命令都没有提示

### openSUSE
************************
## FreeBSD

*******************
## Solaris

**********************
## alpine
> 特别小，在docker中使用有优势

## Gentoo
> 入门难度大，适合资深玩家，据说是特能折腾的系统，处于鄙视链顶端

## Mageia
> [官网](http://www.mageia.org/zh-cn/)

## CDLinux
> 小巧的Linux发行版, 带有很多工具 
