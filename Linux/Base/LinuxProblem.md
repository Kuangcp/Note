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
    1. [驱动问题](#驱动问题)
        1. [显卡](#显卡)
            1. [Nvidia](#nvidia)
            1. [Deepin的NVIDIA驱动问题](#deepin的nvidia驱动问题)
    1. [配置问题](#配置问题)
        1. [Ubuntu与Windows10时间相差8小时的解决](#ubuntu与windows10时间相差8小时的解决)
        1. [终端开启慢](#终端开启慢)
    1. [数据问题](#数据问题)
        1. [笔记本突然断电导致开机报错](#笔记本突然断电导致开机报错)
    1. [系统问题](#系统问题)
        1. [突然掉电关机](#突然掉电关机)

**目录 end**|_2019-10-19 17:04_|
****************************************
# 遇到的常见问题

## 软件问题
### 命令找不到
- `sudo找不到` 安装 sudo
- `locale-gen 找不到` 安装 locales 使用`locale-gen --purge`命令进行更新编码

> Linux上的报错, 提示说找不到共享库 | [参考解决方式 ](http://www.cnblogs.com/Anker/p/3209876.html)

### 终端响铃
> [参考博客: Linux中关闭响铃](https://blog.csdn.net/u010691256/article/details/9048729)

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

### Flash
- 点击[官网下载地址](https://get.adobe.com/cn/flashplayer/)下载,然后解压,
- 将文件复制进火狐插件目录:`sudo cp libflashplayer.so  /usr/lib64/mozilla/plugins`
- 添加其他用户可执行权限`chmod 755 /usr/lib64/mozilla/plugins/libflashplayer.so`

******************************************************

## 驱动问题
### 显卡
- 查看显卡列表  `lspci -vnn | grep '\''[030[02]\]'`
- 测试显卡 FPS `glxgears`

#### Nvidia
> [NVIDIA](https://wiki.archlinux.org/index.php/NVIDIA_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#.E5.AE.89.E8.A3.85)

驱动有: Nouveau, bumblebee, NV_Prime  

> [Bumblebee ](https://wiki.archlinux.org/index.php/Bumblebee_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))  

大多数笔记本都是 Intel集显和 Nvidia 或者 AMD 双显卡, 双显卡的管理就成了问题(指的是Linux下)
> [参考博客: 使用 Bumblebee 控制 NVIDIA 双显卡](https://www.cnblogs.com/congbo/archive/2012/09/12/2682105.html)



#### Deepin的NVIDIA驱动问题
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
### 笔记本突然断电导致开机报错
> 报错信息: fsck exited with status code 4

1. 根据报错提示的分区, 进行修复, 由于我的Linux是ext3文件系统
1. `fsck.ext3 -y /dev/sda9` **分区根据实际情况**
1. 完成后重启即可

************************

## 系统问题
### 突然掉电关机
> 导致了 Git 仓库都损坏了 `fatal: loose object`  

> ZSH: corrupt history file

```shell
mv .zsh_history .zsh_history_bad
strings .zsh_history_bad > .zsh_history
fc -R .zsh_history
```
两天发生了两次...
