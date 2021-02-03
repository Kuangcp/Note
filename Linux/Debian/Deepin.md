---
title: Deepin
date: 2019-10-19 17:04:29
tags: 
    - Deepin
categories: 
    - Linux
---

**目录 start**

1. [Deepin](#deepin)
    1. [关于显卡](#关于显卡)
    1. [电源管理](#电源管理)
        1. [系统休眠](#系统休眠)
    1. [双系统安装](#双系统安装)

**目录 end**|_2021-02-03 17:25_|
****************************************
# Deepin

> [官方wiki](wiki.deepin.org)
> [参考: 一些工具](https://bbs.deepin.org/forum.php?mod=viewthread&tid=143022z)
- [FAQ](https://bbs.deepin.org/forum.php?mod=viewthread&tid=146921&extra=page%3D1)

- 优点:
    - 界面美观,自带CrossOver深度家族的软件也挺好用,自定义命令的快捷键
- 缺点:
    - 基本是Linux的共性了,就是驱动问题, NVIDIA 显卡 因为驱动问题重装四五次系统,重启就不知道多少次了
    - 输入法现在这几天也在作妖 fcitxCPU占用高,输入窗口消失等问题
    - 蓝牙模块时隐时现

`遇到的bug记录`
- 休眠结束系统卡死,然后重启输入法没有窗口 2018-01-09 19:29:25 
    - 杀掉搜狗进程再启动解决

- 2018-03-15 09:25:47 
    [公司电脑安装Windows10 和 Deepin双系统](/MyBlog/2018-3-15-install-deepin.md)

- `Gtk-WARNING **: 无法在模块路径中找到主题引擎：“adwaita”` 2018-05-24 15:08:49 
    - 安装 这个包 gnome-themes-standard

- 2018-06-15 19:50:40 deepin-wm 进程, 也就是Deepin的桌面管理器, 启动久了之后就会发生内存占用非常大的情况, 关闭窗口特效, 再打开就好了

- 2018-08-21 20:34:07 更新到15.7, 然后就是一堆的小问题, 任务栏和屏幕边缘有空隙, 多任务切换方式的变化, 原先用Wine安装的企业QQ不能启动... 但是确实Deepin 现在更快了
    - 使用闭源驱动方案, 休眠一会就卡死了, 只能强制关机, 尝试了开源驱动后, 也是一样 显卡是 Nvidia GTX1050

- 2018-08-23 09:55:15 遭遇用过的最大问题, 笔记本升级到15.7后有显卡明显不兼容, 各种显示上的卡顿, 切换Prime解决方案后, 内核load不进来, 启动不了了
    - 配置是 显卡 NVIDIA 840m 也许重装Deepin15.7, 也许装Manjaro-KDE
    - 最终是进的恢复模式, 卸载了无用的包就成功进入了, 但是发现自动挂载分区的文件都被注释了, 如果手动添加, 即使mount -a 没有报错, 但是启动时就加载不了分区
    - 又得进恢复模式注释掉, 才能进入系统

- 2018-09-02 21:44:21 ` Driver 'pcspkr' is already registered, aborting,`
    >- [参考: 社区帖子](https://bbs.deepin.org/forum.php?mod=viewthread&tid=166517&highlight=pcspkr)

- 2018-11-22 10:19:27 
    - 升级到 15.8 后 xorg 和 deepin-wm 内存泄露, 显卡是 GTX1060x 笔记本的 820m 没有这种情况出现
    - 用上半天, 这俩内存能占用到 3个g

- 2019-01-07 10:45:37
    - 因为公司周末断电,系统没有关机, 导致无法开机, 直接黑屏, 原因应该是突然断电导致文件系统不一致 
    - 解决方案, 用U盘进系统, 挂载系统分区, 使用 fsck 工具修复文件系统 `fsck.ext4 -vy /dev/sdaXXX`
    - 由于我装了三个系统, windows10 deepin manjaro, 所以直接进manjaro, 执行的命令

- deepin-wm 有内存泄露, 打算关闭开启窗口效果来解决, 但是关掉后就打不开了 failed to enable... 2019-03-20 17:20:07
    - [issue](https://github.com/linuxdeepin/developer-center/issues/444)
    - `(killall deepin-wm-switcher; deepin-wm --replace &)` 这样就能守护进程方式在运行了

## 关于显卡
> [参考: 显卡驱动作死录](https://www.jianshu.com/p/f53c8223bac6)

> 个人折腾的整理
当前系统为 Deepin15.7 已经支持多种解决方案了, 还有一个 `深度显卡驱动管理器`
1. Intel默认驱动(也就是集显) 
1. NVIDIA开源驱动 性能不好, 解析闭源驱动而来
1. 大黄蜂方案 采用闭源驱动, 省电
1. PRIME方案 高性能

但是和我笔记本完美兼容的是 大黄蜂方案, 也就是之前安装的 `nvidia-driver`, `nvidia-setting`, `bumblebee-nvidia` 这一系列软件包， PRIME方案切换后差点把内核挂了, U盘进系统切换会原有方案才把系统救活了

> Enable Window effect 失败
尝试切换显卡驱动方案为闭源驱动, 重启下就挂掉了, [社区相关问题](https://bbs.deepin.org/forum.php?mod=viewthread&tid=159333) 
```
    Failed to find module 'mincores'
    Failed to insert 'bbswitch': No such device
```
最后的解决方案是从 4.2 内核启动, 切换回了开源驱动  
版本: Deepin15.9.1 , 不知道哪一个版本升级了内核, 而且新旧内核都保留下来了, 所以有两个内核 4.16 4.2 , 幸好有两个内核

## 电源管理
- [电源管理状态](https://wiki.deepin.org/index.php?title=Power_management&language=en)
    - 睡眠：电源只给内存供电, 内存中数据仍保持。
    - 休眠：内存中数据保存到硬盘中，电源全部断开。
    - 重启：内存数据清除, 冷启动系统
    - 关机：开启快速启动时，所有当前的用户数据关闭，只保存系统核心数据到硬盘中方便下次快速启动系统，电源全部断开；
        - 关闭快速启动时，等同于重启。

### 系统休眠
分为 睡眠 Suspend 和 休眠 Hibernate

> [How to enable hibernate in Deepin? ](https://bbs.deepin.org/forum.php?mod=viewthread&tid=145013)
> [ PowerManagement/Hibernate](https://help.ubuntu.com/community/PowerManagement/Hibernate)

> [Hibernate without swap partition](https://wiki.debian.org/Hibernation/Hibernate_Without_Swap_Partition)`仅使用交换文件达到休眠效果`  
> [Hibernation](https://wiki.archlinux.org/index.php/Power_management/Suspend_and_hibernate#Hibernation_into_swap_file)
> [Hibernate from swap file](https://askubuntu.com/questions/6769/hibernate-and-resume-from-a-swap-file)

## 双系统安装
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
