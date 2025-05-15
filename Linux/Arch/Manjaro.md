---
title: Manjaro
date: 2018-12-21 10:55:08
tags: 
   - Arch
   - Manjaro
categories: 
   - Linux
---

💠

- 1. [Manjaro](#manjaro)
- 2. [安装](#安装)
    - 2.1. [显卡驱动](#显卡驱动)
    - 2.2. [多系统安装](#多系统安装)
- 3. [Tips](#tips)

💠 2025-05-15 15:33:14
****************************************
# Manjaro
> [Gitlab source code](https://gitlab.manjaro.org/explore/groups)  

> [Manjaro Controversies](https://rentry.co/manjaro-controversies)

> [Manjaro 安装体验小结 ](https://michael728.github.io/2019/08/03/linux-manjaro-install/)  
> [Manjaro 安装配置简要](https://blog.csdn.net/ouening/article/details/79633966)  
> [Manjaro安装后你需要这样做](https://www.cnblogs.com/haohao77/p/9034499.html)  
> [参考: Manjaro Deepin安装使用分享](https://zhuanlan.zhihu.com/p/43442012)  
> [参考: Manjaro Deepin 配置备忘](https://yifeitao.com/2019/06/xiaomi-pro-manjaro-deepin)  

> [参考: Manjaro 配置](https://blog.triplez.cn/manjaro-quick-start)  

# 安装
> [Installation Guides](https://wiki.manjaro.org/index.php?title=Installation_Guides)

参考 [Using livecd v17.0.1 (and above) as grub to boot OS with broken bootloader](https://forum.manjaro.org/t/using-livecd-v17-0-1-and-above-as-grub-to-boot-os-with-broken-bootloader/24916) 

## 显卡驱动

> [参考: Manjaro NVIDIA驱动问题的解决方案](https://blog.csdn.net/qq_39828850/article/details/87919188)  

1. `inxi -G` 检查已安装的驱动程序   
1. `sudo mhwd -a pci nonfree 0300` 安装NVIDIA闭源驱动
   - 或者 sudo manjaro-settings-manager 使用硬件设置，安装专有显卡驱动。
1. 重启
1. `mhwd -li` 执行确认驱动程序(Bumbee)已安装并且正在运行,此时不要着急使用 nvidia-settings

> [config NVIDIA](https://wiki.manjaro.org/index.php?title=Configure_NVIDIA_(non-free)_settings_and_load_them_on_Startup) `一键安装配置Nvidia显卡驱动`

> 升级驱动 
- pacman -R linux-latest-nvidia-440xx
- sudo mhwd -r pci video-nvidia-440xx 

- install video-nvidia-450xx drivers. 
- sudo mhwd -i pci video-nvidia-450xx 

nvidia-settings 修改抗锯齿，性能等，保存为配置文件
- sudo mhwd-gpu --setmod nvidia --setxorg test.nvidia-settings-rc

## 多系统安装
例如 Win10(先)和Majaro安装

1. 首先通过 rufus 制作器启动U盘[wiki](https://wiki.manjaro.org/index.php?title=Burn_an_ISO_File)，切记注意所下载ISO的正确性
1. `parted -l` 查看当前硬盘系统分区模式， 来判断安装Manjaro时BIOS配置和安装模式
   1. msdos => legacy 
   1. gpt   => uefi 

# Tips
> U盘启动盘运行Live系统时, 默认用户名和密码都为 manjaro

- 这次下载解压运行 VSCode 就是这样, 报错为 
   - `error while loading shared libraries: libgconf-2.so.4: cannot open shared object file: No such file or directory`
   - 尝试安装 libgconf libgconf2 ...
   - 其实真正的包是 gconf , 而这个也是尝试过的,  但是还是说找不到package, 更新了下系统,才找到了这个包

- `VirtualBox 和内核是高度耦合的`，需要内核驱动版本匹配才能正常运行，`yay virtualbox-host-modules` 选择对应内核版本安装即可
- 配置应用开机自启动 `sudo ln -s /usr/share/applications/xxx.desktop /etc/xdg/autostart/`
