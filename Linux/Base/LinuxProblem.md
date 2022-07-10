---
title: Linux遇到问题总结
date: 2018-12-15 11:16:42
tags: 
    - 工具使用经验
categories: 
    - Linux
---

**目录 start**

1. [遇到的常见问题](#遇到的常见问题)
    1. [软件问题](#软件问题)
        1. [命令找不到](#命令找不到)
        1. [终端响铃](#终端响铃)
        1. [输入法](#输入法)
            1. [fcitx](#fcitx)
        1. [Flash](#flash)
        1. [tracker-extract 高CPU内存占用](#tracker-extract-高cpu内存占用)
    1. [驱动问题](#驱动问题)
        1. [显卡](#显卡)
            1. [Nvidia](#nvidia)
            1. [Manjaro 的NVIDIA驱动问题](#manjaro-的nvidia驱动问题)
            1. [Deepin 的NVIDIA驱动问题](#deepin-的nvidia驱动问题)
    1. [配置问题](#配置问题)
        1. [Ubuntu与Windows10时间相差8小时的解决](#ubuntu与windows10时间相差8小时的解决)
        1. [终端开启慢](#终端开启慢)
    1. [数据问题](#数据问题)
        1. [突然断电](#突然断电)

**目录 end**|_2021-02-03 17:25_|
****************************************
# 遇到的常见问题

## 软件问题
### 命令找不到
- `sudo找不到` 安装 sudo
- `locale-gen 找不到` 安装 locales 使用`locale-gen --purge`命令进行更新编码

> Linux上的报错, 提示说找不到共享库 | [参考解决方式 ](http://www.cnblogs.com/Anker/p/3209876.html)

### 终端响铃
> [参考: Linux中关闭响铃](https://blog.csdn.net/u010691256/article/details/9048729)

1. 临时关闭：`rmmod pcspkr` 临时开启：`modprobe pcspkr`
1. 编辑 `/etc/inputrc`，找到`#set bell-style none`这一行，去掉前面的注释符号
1. xset -b

`下面的方法不敢试`
- 对于Debian/Ubuntu系统，使用root身份执行：
    - `sudo echo "blacklist pcspkr" >> /etc/modprobe.d/blacklist`
- 对于CentOS/Redhat/RHEL/Fedora系统，使用root身份执行：
    - `echo "alias pcspkr off" >> /etc/modprobe.conf `

### 输入法
#### fcitx
- fcitx单核满载:三种（搜狗拼音导致）
    - 杀掉，fcitx -r
    - 先把进程杀掉再fcitx-autostart &
    - fcitx再fcitx-qimpanel
`相关网页：`
- [某引擎搜索结果页](https://ausdn.com/s/ubuntu+cpu+fcitx)| [几种方式](https://www.findhao.net/res/786)| [卸载搜狗安装拼音](http://tieba.baidu.com/p/3863217434)
- [知乎问题](https://www.zhihu.com/question/19839748) | [ubuntu论坛](http://forum.ubuntu.com.cn/viewtopic.php?f=122&t=173730&p=1299087) | [ubuntu论坛](http://forum.ubuntu.com.cn/viewtopic.php?f=8&t=194486&start=0)

- 输入法没有显示打字窗口
    - 直接杀掉 sogou-qimpanel 然后点击图标进行启动

- [ ] 部分终端(Qterminal)无法输入中文

### Flash
- 点击[官网下载地址](https://get.adobe.com/cn/flashplayer/)下载,然后解压,
- 将文件复制进火狐插件目录:`sudo cp libflashplayer.so  /usr/lib64/mozilla/plugins`
- 添加其他用户可执行权限`chmod 755 /usr/lib64/mozilla/plugins/libflashplayer.so`

### tracker-extract 高CPU内存占用
> [参考: Go Away, tracker-store](https://www.soimort.org/notes/171103/)  
> [参考: tracker store](https://askubuntu.com/questions/346211/tracker-store-and-tracker-miner-fs-eating-up-my-cpu-on-every-startup)  

1. 复制 `cp /etc/xdg/autostart/tracker-miner-fs-3.desktop ~/.config/autostart/` 等若干文件 并追加 `Hidden=true`
1. 禁用服务 : `systemctl --user mask tracker-store` 

******************************************************

## 驱动问题
### 显卡
- 查看显卡列表  `lspci -vnn | grep '\''[030[02]\]'`
- 测试显卡 FPS `glxgears`

休眠后的唤起 vscode vivaldi chrome 均出现假死半分钟后才恢复的情况，禁用硬件加速可避免

#### Nvidia
> [NVIDIA](https://wiki.archlinux.org/index.php/NVIDIA_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#.E5.AE.89.E8.A3.85)

常见驱动方案有: Nouveau, bumblebee, NV_Prime  

> [Bumblebee ](https://wiki.archlinux.org/index.php/Bumblebee_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))  

大多数笔记本都是 Intel集显和 Nvidia 或者 AMD 双显卡, 双显卡的管理就成了问题(指的是Linux下)
> [参考: 使用 Bumblebee 控制 NVIDIA 双显卡](https://www.cnblogs.com/congbo/archive/2012/09/12/2682105.html)

************************
#### Manjaro 的NVIDIA驱动问题
> [参考: Manjaro NVIDIA驱动问题的解决方案](https://blog.csdn.net/qq_39828850/article/details/87919188)  

1. `inxi -G` 检查已安装的驱动程序   
1. `sudo mhwd -a pci nonfree 0300` 安装NVIDIA驱动
1. 重启
1. `mhwd -li` 执行确认驱动程序(Bumbee)已安装并且正在运行,此时不要着急使用nvidia-settings

#### Deepin 的NVIDIA驱动问题
- [论坛博客](https://bbs.deepin.org/forum.php?mod=viewthread&tid=132312)
    - `sudo apt-get install bumblebee-nvidia nvidia-driver nvidia-settings`

************************************************

## 配置问题
### Ubuntu与Windows10时间相差8小时的解决
- `timedatectl set-local-rtc true `

### 终端开启慢
- 检查 .bashrc 文件 看是否有可疑脚本,
    - 这次就是因为 sdkman 的原因(总是在检查自动更新, 虽然说关掉就好了)导致巨慢, 打开终端要一分钟
    - 那上次搞得我新建用户,重装系统是什么原因呢?

*********************************************

## 数据问题
### 突然断电
> 开机报错信息: fsck exited with status code 4

1. 根据报错提示的分区, 进行修复, 由于我的Linux是ext3文件系统 ext4 则是 `fsck.ext4`
1. `fsck.ext3 -y /dev/sda9` **分区根据实际情况**
1. 完成后重启即可

************************

> 导致了 Git 仓库都损坏了 `fatal: loose object`  

ZSH: corrupt history file

```shell
mv .zsh_history .zsh_history_bad
strings .zsh_history_bad > .zsh_history
fc -R .zsh_history
```
