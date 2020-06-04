---
title: install manjaro20 with windows10 
date: 2020-06-04 19:42:04
tags: 
categories: 
    - Blog
---

**目录 start**

1. [安装Manjaro20](#安装manjaro20)

**目录 end**|_2020-06-04 19:42_|
****************************************
# 安装Manjaro20

前提；首先系统已经安装Win10, 固态硬盘

1. 先做U盘(原先都是使用Deepin的制作器，这次不灵了，还尝试了 dd ImgWriter，最终使用rufus成功)
1. 确认BIOS关闭 Fast Boot
1. 按以往经验(曾安装Win10 Deepin Manjaro三系统均正常使用)直接以UEFI模式启动安装 进行到最后一步失败了 [和该楼主问题基本一致](https://forum.manjaro.org/t/manjaro-20-0-installation-failed-on-tongfang-s41b-boost-python-error-in-job-bootloader/138889)
    1. 但是通过该楼主的方式，能通过U盘启动系统后，手动找引导，进入在固态上安装引导失败的Manjaro系统 [Using livecd v17.0.1 (and above) as grub to boot OS with broken bootloader](https://forum.manjaro.org/t/using-livecd-v17-0-1-and-above-as-grub-to-boot-os-with-broken-bootloader/24916) 虽然这是不符合需求的。
    1.  一些命令记下备用： `init -Fxxxz` 查看硬件和分区信息 partd -l 查看分区模式 
1. 最终发现不应该使用UEFI模式安装[Installation of msdos disk in UEFI - A Warning](https://forum.manjaro.org/t/installation-of-msdos-disk-in-uefi-a-warning/15120) 楼主比较熟悉 grub，因为Windows10使用的MBR方式安装 坑啊
1. 所以只能使用legacy模式安装，一切重来，按部就班.. 分区 /boot 512M 其余都给 /
1. 安装成功

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020051717181055.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tjcDYwNg==,size_16,color_FFFFFF,t_70)

************************


- 顺带一提，公司电脑也是主力使用Manajro，某次滚动升级了内核到5.4后，由于没有升级virtualbox的对应包，导致virtualbox一运行就假死，然后尝试了多次后整个系统无任何响应  
- 然后就强制关机了，没想到这个强制关机引起了BIOS的错误，BIOS莫名其妙被设置成了 legacy  
- 引导项直接就默认Win10了，Deepin和Manjaro引导都不见了，但是通过u盘进入Linux系统后能通过chroot-找到对应的Deepin和Manjaro系统 学习到了 以后修复系统用  
    ```bash
        mkdir /mnt/deepin 
        mount /dev/sda1 /mnt/deepin
        # bash 语法
        for dir in dev proc sys etc bin sbin var usr lib lib64; do 
            mkdir /mnt/deepin/$dir && mount --bind /$dir /mnt/deepin/$dir
        done
        chroot /mnt/deepin
    ```
- 在Windows下EasyBCD瞎折腾了几下，没有生效，仔细看BIOS设置才发现原因  
Linux 掉电或者强制关机是个大坑！！
