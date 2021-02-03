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
    1. [/boot](#boot)
    1. [/bin 和 /sbin](#bin-和-sbin)
    1. [/root](#root)
    1. [/run](#run)
    1. [/home](#home)
    1. [/lost+found](#lost+found)
    1. [/proc](#proc)
        1. [网络](#网络)
    1. [/usr](#usr)
        1. [/usr/local](#usrlocal)
    1. [/etc](#etc)
        1. [/etc/passwd](#etcpasswd)
        1. [/etc/shadow](#etcshadow)
        1. [/etc/alternatives](#etcalternatives)
        1. [/etc/apt](#etcapt)
        1. [/etc/fstab](#etcfstab)
        1. [/etc/systemd](#etcsystemd)
    1. [/lib](#lib)
    1. [/dev](#dev)
    1. [/tmp](#tmp)
    1. [/usr](#usr)
    1. [/var](#var)
1. [使用](#使用)
    1. [查看发行版](#查看发行版)
    1. [查看系统所有用户信息](#查看系统所有用户信息)

**目录 end**|_2021-02-03 17:25_|
****************************************
# Linux 目录结构
> Linux 系统目录结构的大致分布以及说明

## /boot

> 该目录存放的是启动Linux是的核心文件，具体包含一些镜像文件和链接文件，因此这个目录非常重要，，如果遭到破坏，系统将无法启动

- 查看引导项 `sudo efibootmgr -v`

## /bin 和 /sbin

> 这两个目录存放的是可执行的二进制文件。bin其实是binary的缩写，/bin目录下存放的就是我们经常使用的Linux命令。sbin中的s其实是Super User的意思，也就是，只有超级用户才可以执行这些命令

## /root
> root用户的默认用户目录

## /run

> 该目录是外在设备的自动挂载点目录，用来自动挂载光驱和U盘。另外还有一个/media目录，与/run目录作用基本类似，在CentOS 7之前使用。还有一个/mnt目录，主要用来手动挂载一些移动设备

## /home
> 非root用户的默认用户目录的父目录  

## /lost+found

> 该目录用于保存丢失的文件。不恰当的关机操作和磁盘错误均会导致文件丢失，这些丢失的文件会临时放在/lost+found下，系统重启后，引导进程会运行fsck程序，该程序就会发现这些文件爱你。除了’/‘分区上的这个目录外，在每个分区上均有一个lost+found目录

************************

## /proc
> 此目录是虚拟目录，目录中所有信息都是内存的映射，通过这个虚拟的内存映射目录，可以和内核内部数据结构进行交互，获取有关进程的有用信息，同时也可以在系统运行中修改内核参数。与其他目录不同，/proc存在于内存中，而不是硬盘上

| 文件或目录       | 说明                                |
| ----------- | --------------------------------- |
| cpuinfo     | 关于系统CPU的详细信息，包含CPU名称、型号和类型        |
| meninfo     | 内存信息，包含物理内存和虚拟内存                  |
| filesystems | 当前系统支持的文件系统类型                     |
| devices     | 内核中的设备驱动程序列表                      |
| net         | 网络使用协议以及状态信息                      |
| dma         | 当前使用的dma通道                        |
| ioports     | 当前使用的I/O端口                        |
| modules     | 当前系统加载的内核模块信息                     |
| stat        | 系统的各种状态信息                         |
| uptime      | 系统总的启动时间和空闲时间，以秒为单位               |
| version     | 内核版本信息                            |
| loadavg     | 系统平均负载                            |
| kcore       | 系统物理内存的映像，与物理内存大小完全一样，但实际不占用那么大空间 |
| kmsg        | 内核输出信息，同时被输出到rsyslog              |

- `/proc/sys/fs/inotify/max_user_watches`
- `/proc/sys/kernel/threads-max` 
- `/proc/sys/kernel/pid_max`

### 网络
1. ARP: /proc/net/arp 若该文件内有重复的mac地址, 并且有机器伪装成了网关的mac 就说明遭受了ARP攻击 `或者 arp -a`
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
> 主要用于存放系统管理相关的配置文件以及子目录。其中比较重要的有系统初始化文件/etc/rc、用户信息文件/etc/passwd等，相关网络配置文件和服务启动文件也在该目录下

| 文件名和目录                             | 主要作用                                     
| -------------------------------------- | ---------------------------------------- 
| hosts                                  | 设定用户自己的IP与名字的对应表                         |
| resolv.conf                            | 客户端DNS配置文件                               |
| systemd/system/*.wants                 | 此目录包含所有服务启动脚本，开机时系统将自动启动这些服务（CentOS 7新增） |
| sysconfig/network-scrripts/ifcfg--eth0 | IP地址配置文件（CentOS 7后网卡名从类似eth0、eth1的标识变为enp0s3、enps4标识） |
| X11                                    | X-Window的配置文件                            |
| rsyslog.conf                           | 系统日志输出配置文件                               |
| crontab                                | 系统级别的守护进程配置文件                            |
| services                               | 定义系统服务与端口的对应关系                           |
| profile                                | 系统全局环境变量配置文件                             |
| sysctl.conf                            | 系统内核参数配置文件（在CentOS 7后，内核参数配置文件转移到了/usr/lib/sysctl.d目录下，但sysctl.conf文件仍有效，并且可覆盖/usr/lib/sysctl.d中的配置） |

### /etc/passwd
> 用户的组，权限, Home目录, 默认shell 相关配置

- 禁止 Shell 登录, 将原有默认 shell `/bin/bash` 改为 `/sbin/nologin`

### /etc/shadow 
> 存放用户密码的文件，每个用户的密码加密后都放入此文件  

### /etc/alternatives
alternative是可选项的意思.
首先，因为依赖关系的存在，一个软件包在系统里面可能出现新旧版本并存的情况.
在以前，要想用旧版本作为默认值就必须要手动修改配置文件，有些软件比较简单，有些却要修改很多文件，甚至一些相关软件的配置文件也要相应修改。

update-alternatives 命令就是操作的这个目录, 实现的步骤往往是在该目录建立一个软链接, 然后又从这里建立软链接到 /usr/bin 下, 实现将命令加入到 PATH 中的目的

### /etc/apt
> Debian 系 apt 包管理器的配置目录

1. /etc/apt/sources.list.d/ 这个目录是放别的应用需要的软件列表

### /etc/fstab
> static file system infomation

> [A complete fstab guide ](http://www.linuxstall.com/fstab/)

Use 'blkid' to print the universally unique identifier for a device;   
this may be used with UUID= as a more robust way to name devices that  works even if disks are added and removed. 

行内容结构 `<file system>  <mount point>  <type>  <options>  <dump>  <pass> `

### /etc/systemd
systemd的配置文件目录，此目录是Linux启动的重要部分，用来完成对整个系统的基本初始化配置

************************

## /lib

> 该目录存放的是共享程序库和映像问津，，可供很多程序使用。通过这些共享映射文件，每个程序就不必分别保存自己的库文件，Linux提供一组可供所有程序使用的文件。在该目录中，还包含引导进程所需的静态库文件

## /dev
> 包含系统所有的设备文件

| 设备名     | 具体含义                                     |
| ------- | ---------------------------------------- |
| fd*     | 代表软盘设备，fd0代表第一个软盘设备，fd1代表第二个软盘设备         |
| audio*  | 代表声卡设备                                   |
| hd*     | 代表IDE硬盘设备。hda代表第一块IDE硬盘，hdb代表第二块IDE硬盘    |
| sd*     | 代表SCSI设备，sda代表第一块SCSI硬盘，sdb代表第二块SCSI硬盘   |
| lp*     | 代表并行串口                                   |
| pty*    | 代表网络中登录的远程终端设备                           |
| ram*    | 代表系统内存                                   |
| tty*    | 代表Linux上的虚拟控制台，也叫字符控制台。tty1代表第一个虚拟控制台，tty2代表第二个虚拟控制台，以此类推，Linux上一共有6个虚拟控制台 |
| ttyS*   | 代表串行端口。                                  |
| console | 代表系统控制台，也就是桌面控制台，可以直接连接到显示器              |
| null    | 输出空设备                                    |

***************************

## /tmp
> 应用缓存目录, 存放缓存文件, 在系统重启后就会被清理 

- 在安装Linux时如果没有明确的分区, 就会属于 / 分区, 那么就要给 / 留有足够的大小, 不然 /tmp 分区不足会导致应用运行异常
    - 例如 Tomcat 在运行时就需要使用
- 清理的机制
    - 如果新建文件在 /tmp 目录下， 文件的内容会随着系统重启而消失 但是文件依旧存在(空文件)

## /usr

> 主要用于存放应用程序和文件。如果在系统安装的时候选择了很多安装软件包，那么这些软件包默认会安装到该目录下，平时安装的一些软件默认情况下也会安装在该目录内

| 文件或目录              | 主要作用                            |
| ------------------ | ------------------------------- |
| lib64以及local/lib64 | 64位操作系统中的函数库目录                  |
| src                | 该目录包含所有程序的源代码，其中主要是Linux核心程序源代码 |
| local              | 该目录存放本地安装的软件和其他文件，与LInux无关      |
| bin以及local/bin     | 使用者可执行的二进制文件目录                  |
| lib以及local/lib     | 32位操作系统使用的函数库目录                 |
| sbin以及local/sbin   | 该目录存放系统管理员才能执行的指令               |
| include            | 此目录包含c语言的头文件，文件扩展名大多数为.h        |
| share              | 该目录存放共享的文件和数据库                  |

## /var
> 主要用于存放系统运行以及软件运行的日志信息

| 文件或目录 | 主要作用                                     |
| -------  | ---------------------------------------- |
| log      | 该目录存放各种应用程序的日志文件，这里的文件是经常变动的，因此需要定期清理    |
| lib      | 该目录存放系统正常运行时需要改变的库文件                     |
| spool    | 该目录是mail、new、打印机队列和其他队列输入、输出的缓冲目录        |
| tmp      | 该目录允许比/tmp存放更大的文件                        |
| lock     | 该目录存放被锁定的文件，很多程序都会在/var/lock下产生一个锁文件，以保证其他程序不能同时使用这个设备或文件 |
| local    | 该目录存放/usr/local中所安装程序的可变数据               |
| account  | 该目录存放已经格式化的man页                          |
| run      | 该目录包含到下次系统启动前的系统信息                       |


************************

# 使用
> 具体配置文件的使用

## 查看发行版

1. `cat /etc/issue` 通用
1. `cat /etc/redhat-release` redhat系
1. screenfetch `先安装`
1. lsb_release -a

_查看内核版本_
- `cat /proc/version`
- `uname -a`

## 查看系统所有用户信息
> /etc/passwd 包含了用户,用户组,用户home目录 shell类型等信息  
> 看第三个参数:500以上的,就是后面建的用户了.其它则为系统的用户.
