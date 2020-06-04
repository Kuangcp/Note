---
title: 双硬盘安装Deepin15.5
date: 2018-03-15 16:11:42
tags: 
    - 工具使用经验
categories: 
    - Blog
---

**目录 start**

1. [在公司电脑上安装deepin](#在公司电脑上安装deepin)

**目录 end**|_2020-06-04 19:41_|
****************************************
# 在公司电脑上安装deepin
> 由于是全新的电脑, 默认开机在配置Windows10, 然后也配置用了下windows10, 被他的卡顿吓到了

> 前奏: 先进Windows10 关闭快速启动(电源设置, 电源按钮设置这里), 进入BIOS 关闭安全启动, 选择引导为完全关闭UEFI 只设置为Legacy

- 由于习惯Deepin, 所以一直备有一个Deepin15.4的安装盘, 然后试了一下, 发现U盘能进去, 点击安装Deepin就黑屏了 没有然后了
- 然后搜了一波一闪而过的报错信息, 朋友也和我提到了可能是内核版本太高 
    - [问题相关](https://www.systutorials.com/linux-kernels/95229/platform-x86-acer-wmi-only-supports-amw0_guid1-on-acer-family-linux-4-9-22/)

- 然后就刻录了Deepin15.1的启动盘, 最终完美安装, 但是还是想升到最新 
    - 分区: 因为该电脑是Intel的128固态加上1T的机械, 所以尝试了只在机械上放 / 和 /home失败后
        - 尝试在固态上压缩了500M出来, 挂载 /boot 然后在机械上挂载 / 和 /home
        - 选择引导时选择的固态

- 进入系统后, apt update apt upgrade 进行升级
    - 其中提到的所有询问, 都是默认, 然后说grub引导需要升级, 需要选引导设备, 选之前分的500M的那个 /boot 分区

- 然后就发现升级完进不去桌面了, 能进tty, 密码是正确的, 但是图形化窗口进不去了
    - 解决方案 `sudo apt-get update && sudo apt-get -f install && sudo apt-get dist-upgrade && sudo apt-get install dde` 
    - [社区帖子](https://bbs.deepin.org/forum.php?mod=viewthread&tid=134486)

- 进去之后分辨率很低, 搜了一波怎么改, 然后说要自己用 xrandr 等命令来设置 1080P
    - 在社区的官方帖子上找到了解决方案, 装个驱动就完了 [官方社区](https://wiki.deepin.org/index.php?title=%E6%98%BE%E5%8D%A1)

- 最后完美运行了15.5(现在已经是15.8), 和Windows10也完美兼容, 启动的话就需要进BIOS进行设置, 和我笔记本一样的方式
    - 开启UEFI 关闭 Legacy 就是默认进 Windows10 
    - 关闭UEFI  就是默认进Deepin
