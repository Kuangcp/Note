---
title: Linux目录结构
date: 2018-12-15 11:14:08
tags: 
    - 基础
categories: 
    - Linux
---

**目录 start**
 
1. [Linux 目录结构](#linux-目录结构)
    1. [/root](#root)
    1. [/home](#home)
    1. [/proc](#proc)
        1. [网络](#网络)
    1. [/usr](#usr)
        1. [/usr/local](#usrlocal)
    1. [/etc](#etc)
        1. [/etc/passwd](#etcpasswd)
        1. [/etc/alternatives](#etcalternatives)
        1. [/etc/apt](#etcapt)
        1. [/etc/fstab](#etcfstab)
    1. [/tmp](#tmp)
1. [使用](#使用)
    1. [查看发行版](#查看发行版)
    1. [查看系统所有用户信息](#查看系统所有用户信息)

**目录 end**|_2019-12-06 18:19_|
****************************************
# Linux 目录结构
> Linux 系统目录结构的大致分布以及说明

## /root
> root用户的默认用户目录

## /home
> 非root用户的默认用户目录  

********************************
## /proc
> 进程的目录, 一个个进程看起来是一个个目录(并不是真正的目录,这是一个虚拟文件系统), 使用进程号作为目录名

- `/proc/sys/fs/inotify/max_user_watches`


### 网络
1. ARP: /proc/net/arp cat该文件, 如果发现里面有重复的mac地址, 并且有机器伪装成了网关的mac 就说明遭受了ARP攻击 `或者 arp -a`
    - arping 10.91.255.254 能查看到真实的mac地址

***************

## /usr

### /usr/local
> 全局配置, 对应的局部配置目录是 `~/.local`, 惯例是局部覆盖全局配置

```
    ├── bin 可执行文件(Python安装应用的目录)
    ├── lib 库
    └── share 应用的配置
```

- share 目录下 存放大量应用配置: 主题,图标,字体,desktop文件 什么的

************************
## /etc
> 系统以及应用的配置目录

### /etc/passwd
> 用户的组，权限, Home目录, 默认shell 相关配置

- 禁止 Shell 登录, 将原有默认 shell `/bin/bash` 改为 `/sbin/nologin`

### /etc/alternatives
alternative是可选项的意思.
首先，因为依赖关系的存在，一个软件包在系统里面可能出现新旧版本并存的情况.
在以前，要想用旧版本作为默认值就必须要手动修改配置文件，有些软件比较简单，有些却要修改很多文件，甚至一些相关软件的配置文件也要相应修改。

update-alternatives 命令就是操作的这个目录, 实现的步骤往往是在该目录建立一个软链接, 然后又从这里建立软链接到 /usr/bin 下, 实现将命令加入到 PATH 中的目的

- [ ] 学习

### /etc/apt
> Debian 系 apt 包管理器的配置目录

1. /etc/apt/sources.list.d/ 这个目录是放别的应用需要的软件列表

### /etc/fstab
> static file system infomation

> [A complete fstab guide ](http://www.linuxstall.com/fstab/)

Use 'blkid' to print the universally unique identifier for a device;   
this may be used with UUID= as a more robust way to name devices that  
  works even if disks are added and removed. 

`<file system>  <mount point>  <type>  <options>  <dump>  <pass> `

***************************

## /tmp
> 应用缓存目录, 在使用时存放缓存文件, 在计算机重启后就会被清理 

- 在安装Linux时如果没有明确的分区, 就会属于 / 分区, 那么就要给 / 留有足够的大小, 不然 /tmp 分区不足会导致应用运行异常
- 例如 Tomcat 在运行时就需要使用, 然后Deepin的截图也会将截图缓存到该目录下 ...

************************

# 使用
> 具体配置文件的使用

## 查看发行版

1. `cat /etc/issue` 通用
1. `cat /etc/redhat-release` redhat系
1. screenfetch `先安装`
1. lsb_release -a

_查看内核版本_
`cat /proc/version`
`uname -a`

## 查看系统所有用户信息
> /etc/passwd 包含了用户,用户组,用户home目录 shell类型等信息  
> 看第三个参数:500以上的,就是后面建的用户了.其它则为系统的用户.
