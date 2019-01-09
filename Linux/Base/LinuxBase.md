---
title: Linux基础
date: 2018-12-15 11:11:23
tags: 
    - 基础
categories: 
    - Linux
---

**目录 start**
 
1. [Linux系统](#linux系统)
    1. [用户](#用户)
    1. [用户组](#用户组)
    1. [进程](#进程)
        1. [孤儿进程](#孤儿进程)
        1. [僵尸进程](#僵尸进程)
    1. [时间](#时间)
    1. [服务](#服务)
        1. [自启服务](#自启服务)
    1. [终端命令](#终端命令)
        1. [Shell内建命令](#shell内建命令)
1. [终端快捷键](#终端快捷键)
    1. [Delete](#delete)
    1. [Convert](#convert)
    1. [Jump](#jump)
    1. [Search](#search)
    1. [Control](#control)
    1. [对比](#对比)
        1. [文件系统对比](#文件系统对比)
        1. [桌面环境对比](#桌面环境对比)
        1. [窗口管理器对比](#窗口管理器对比)
        1. [文件管理器对比](#文件管理器对比)
        1. [终端模拟器对比](#终端模拟器对比)
1. [Tips](#tips)
    1. [一行执行多条命令](#一行执行多条命令)
    1. [让命令在后台运行](#让命令在后台运行)
        1. [关闭ssh回话不能运行](#关闭ssh回话不能运行)
        1. [关闭ssh回话仍能运行](#关闭ssh回话仍能运行)
    1. [修改主机名](#修改主机名)

**目录 end**|_2019-01-10 00:10_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Linux系统
> 只是记录了debian系的Linux, 不过也是大同小异

> 新手的话特别注意不要随意用sudo然后更改配置文件，容易导致系统crash（除非你明确的知道这个更改操作的作用）

- [运维生存时间](http://www.ttlsa.com)`含大量运维干货`
- [撸Linux](https://www.lulinux.com/)`非理性言论?`
- [Linux命令大全](http://man.linuxde.net/) `Linux命令教程`
- [RUNOOB.COM](http://www.runoob.com) `各种技术学习 文档资源`
- [Linux中国开源社区](https://linux.cn/)
- [LinuxTOY 是一个致力于提供 Linux 相关资讯的专题站点。](https://linuxtoy.org/)
    - [内容Github源](https://github.com/LinuxTOY/linuxtoy.org)

> [笔记: 发行版之别](/Linux/ReleaseExperience.md)

**************************************
## 用户
- 添加用户 `sudo adduser username` 
    - 对比 `useradd`只是新建一个用户不会创建主目录
- 添加到sudo组 ，使用命令更安全：`sudo gpasswd -a $USER sudo` 但是要注销或者重启才生效貌似
- 或者：添加用户到用户组：`adduser user group`
    -  或者：使用修改文件的方式：（不推荐） 但是在docker中跑Ubuntu新建用户时很有用，也可以不用动文件，添加进组是有效的，看情况吧
    - `chmod 777 /etc/sudoers`  然后直接`sudo visudo`就是调用vi来打开文件的简写
        - 找不到文件说明没有安装sudo -> root用户 `apt install sudo `
    - 添加一行 `kuang  ALL=(ALL:ALL)ALL` Centos:`kuang   ALL=(ALL)       ALL`
    - `chmod 440 /etc/sudoers`
        - `rwx 对应一个三位的二进制数， 1/0 表示开关`
- 查看是否设置成功 ： `groups username`
- 删除用户以及对应的home目录：`sudo deluser username --remove-home` 

*****
- _切换用户_ `su` 
- `su -l username` 当前用户的环境下登录用户（当成一个程序一样可以退出登录）

*****
- _修改密码_ `passwd`
    - `passwd user`
    - `echo "root:caishi" | chpasswd` 如果是普通用户就是 sudo chpasswd
*****
- _修改相关信息_ `usermod` 

| verb | long verb | comment |
|:----:|:----|:----|
| -d | --home HOME_DIR          |  用户的新主目录 |
| -e | --expiredate EXPIRE_DATE |  设定帐户过期的日期为 EXPIRE_DATE |
| -f | --inactive INACTIVE      |  过期 INACTIVE 天数后，设定密码为失效状态 |
| -g | --gid GROUP              |  强制使用 GROUP 为新主组 |
| -G | --groups GROUPS          |  新的附加组列表 GROUPS |
| -a | --append GROUP           |  将用户追加至上边 -G 中提到的附加组中，并不从其它组中删除此用 |户
| -l | --login LOGIN            |  新的登录名称 |
| -L | --lock                   |  锁定用户帐号 |
| -m | --move-home              |  将家目录内容移至新位置 (仅于 -d 一起使用) |
| -p | --password PASSWORD      |  将加密过的密码 (PASSWORD) 设为新密码 |
| -R | --root CHROOT_DIR        |  chroot 到的目录 |
| -s | --shell SHELL            |  该用户帐号的新登录 shell |
| -U | --unlock                 |  解锁用户帐号 |

> [所有参数说明](https://gitee.com/kcp1104/codes/gca14wtqvm67l9j5r0deb56#usermod.md)

******
- `passwd 选项 用户名` 更改口令(密码)
    - `-l 锁定口令，禁用账号`  `-u 口令解锁` `-d 账号无口令` `-f 强迫用户下次登录时修改口令`
    - 当前用户 `passwd` 就是修改当前用户口令 超级用户就可以命令后接用户名，修改任意用户

******
- pwcov 注：同步用户从/etc/passwd 到/etc/shadow
- pwck 注：pwck是校验用户配置文件/etc/passwd 和/etc/shadow 文件内容是否合法或完整;
- pwunconv 注：是pwcov 的立逆向操作，是从/etc/shadow和 /etc/passwd 创建/etc/passwd ，然后会删除 /etc/shadow 文件;
- finger 注：查看用户信息工具
- id 注：查看用户的UID、GID及所归属的用户组
- chfn 注：更改用户信息工具
- visudo 注：visodo 是编辑 /etc/sudoers 的命令;也可以不用这个命令，直接用vi 来编辑 /etc/sudoers 的效果是一样的;

## 用户组
> [相关 博客](http://www.runoob.com/linux/linux-user-manage.html)

- 修改用户至指定组 `sudo usermod -G 用户组 用户`
- _显示用户所在组_ `groups`
    - 缺省是当前用户, 若指定即输出指定用户的用户组
- _添加用户组_ `groupadd`
    - 缺省参数 就是新建用户组
    - `-g GID` 指定新用户组的组标识号GID 
    - `-o` 一般和g共用 表示新用户组的GID可以与系统已有用户组的GID相同。

- _删除用户组_ `groupdel` 

- `groupmod 选项 用户组`
    - -g GID 为用户组指定新的组标识号。
    - -o 与-g选项同时使用，用户组的新GID可以与系统已有用户组的GID相同。
    - -n 新用户组 将用户组的名字改为新名字

- grpck 检查`/etc/group`文件是否正确
- grpconv 注：通过/etc/group和/etc/gshadow 的文件内容来同步或创建/etc/gshadow ，如果/etc/gshadow 不存在则创建;
-  注：通过/etc/group 和/etc/gshadow 文件内容来同步或创建/etc/group ，然后删除gshadow文件

****************************

## 进程
> 参考 深入理解计算机系统 书籍

> [参考博客: 孤儿进程与僵尸进程[总结]](http://www.cnblogs.com/Anker/p/3271773.html)

### 孤儿进程
> 一个父进程退出，而它的子进程还在运行，那么那些子进程将成为孤儿进程。孤儿进程将被init进程(进程号为1)所收养，并由init进程对它们完成状态收集工作。

> 注意, 也有意外, 并不总是被 init 进程收养 [Ubuntu15.04 删除/sbin/upstart与孤儿进程收养的问题](https://blog.csdn.net/chilumanxi/article/details/47066331)

### 僵尸进程
> 一个进程使用fork创建子进程，如果子进程退出，而父进程并没有调用wait或waitpid获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中, 这种进程称之为僵死进程。

- 危害:
    - 占用系统内存 pid等资源, 无法被回收

> 常规解决方案 [Github: 代码示例](https://github.com/Kuangcp/LearnC/tree/master/exception/process)
1. `处理信号`: 子进程退出时向父进程发送SIGCHILD信号，父进程处理SIGCHILD信号。在信号处理函数中调用wait进行处理僵尸进程。
1. `fork两次`: 原理是将子进程成为孤儿进程，从而其的父进程变为init进程，通过init进程可以处理僵尸进程。

> 暴力方案: 直接 kill 掉父进程, 父进程和僵死状态的子进程就一起被回收了
*******************************

## 时间
> [同步Linux服务器时间](http://www.cnblogs.com/chenmh/p/5485829.html)

- Linux 的时间由两部分组成, 时区和时间: /etc/timezone 和 /etc/localtime

**同步时间**
1. 修改时区 `cp -y /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`
2. 同步时间 `/usr/sbin/ntpdate -u cn.pool.ntp.org` | 没有就先安装 ntpdate 
3. 查看硬件时间 `hwclock -r`
    - 如果不同步就需要写入时间 `hwclock -w` _因为系统重启是参考硬件时间的_

**自动同步时间**
1. 配置开机自动校验 `vim /etc/rc.d/rc.local`
    - `/usr/sbin/ntpdate -u cn.pool.ntp.org> /dev/null 2>&1; /sbin/hwclock -w`
2. 配置定时任务 `crontab -e`
    - `00 10 * * * root /usr/sbin/ntpdate -u cn.pool.ntp.org > /dev/null 2>&1; /sbin/hwclock -w `

## 服务
> 采用 systemd 方式进行管理 [Arch Doc: systemd](https://wiki.archlinux.org/index.php/Systemd_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

- systemctl start/stop/restart/reload/edit ... 详情见 man systemctl

- 修改服务的配置 `systemctl edit docker.service` 当发现文件不存在时,这个是创建文件 对应的文件是 `/etc/systemd/system/docker.service.d/`

### 自启服务
> /etc/init.d/ 是服务的存放目录
1. 列出所有服务的状态 `service --status-all`

1. 移除MySQL的自启 `sudo update-rc.d -f mysql remove`
2. 设置MySQL随机启动 `sudo update-rc.d mysql defaults`
3. 设定MySQL启动顺序 `update-rc.d mysql defaults 90` 数字越小, 启动顺序越前

- sysv-rc-conf  略微图形化的管理服务的开机自启 
- chkconfig 简单的输出服务自启状态

_系统运行级别_
```
    0        系统停机状态
    1        单用户或系统维护状态
    2~5      多用户状态
    6        重新启动 
```
**********************************************
## 终端命令
> /bin/* 系统自带的命令  
例如 which命令, 查找到命令的位置

> /usr/bin/* 用户安装终端应用的目录 以下往往是系统自带的
- wc -l file _统计文件行数_
- md5sum 报文摘要算法 

1. sudo 命令是需要安装的... 
    1. `alias sudo='sudo'` 能够在别名上使用 sudo *神奇*

### Shell内建命令
> [更多常用工具列表](/Linux/Tool/Terminal.md)

*************************
# 终端快捷键

- `鼠标中键` 粘贴鼠标左键已选择的文本 **VSCode中也适用**
- `!num` history 中第 num 条命令
- `!!` 上一条命令
- `ls !$` 执行命令ls，并以上一条命令的参数为其参数
- `!?string?` 执行含有string字符串的最新命令
- `Ctrl L` 清屏等价于clear，清除所有这个 shell 提示屏幕中显示的数据。 `Mysql也适用`
- `reset` 刷新 shell 提示屏幕。如果字符不清晰或乱码的话，在 shell 提示下键入这个命令会刷新屏幕。
- `Ctrl ；` 显示最近五条剪贴板内容
- Ctrl Alt Backspace : 杀死你当前的 X 会话。杀死图形化桌面会话，把你返回到登录屏幕。如果正常退出步骤不起作用，你可以使用这种方法。
- Ctrl Alt Delete : 关机和重新引导 Red Hat Linux。关闭你当前的会话然后重新引导 OS。只有在正常关机步骤不起作用时才使用这种方法。
- Ctrl Alt Fn: 切换屏幕。 根据默认设置，从 [F1] 到 [F6] 是 shell 提示屏幕， [F7] 是图形化屏幕。`但是deepin是F1为图形化`

## Delete
| Controller | Key | comment |
|:---|:----|:----|
| Ctrl | D | 删除光标后字符,等价于Delete键（命令行若无任何字符，则相当于exit；处理 多行标准输入时也表示EOF） |
| Ctrl | H | 退格删除一个字符，相当于通常的Backspace键 |
| Ctrl | U | 删除光标之前到 行首 的字符 (Zsh中是删除整行)|
| Esc | W | 删除光标之前到 行首 的字符|
| Ctrl | K | 删除光标之前到 行尾 的字符 |
| Ctrl | W | 删除光标之前的一个单词 |
| Alt | D | 删除光标之后的一个单词 |
| Ctrl | Y | 粘贴上次删除的所有字符 |
| Ctrl | _ | 撤销修改 等价于 `Ctrl x u` |

**************************
## Convert
| Controller | Key | comment |
|:---|:----|:----|
| Ctrl | T | 互换当前字符,光标后移 |
| Alt | T | 互换当前单词与前一个单词,光标后移 等价于 `Esc T`|
| Alt | D | 将当前单词全部转为大写,光标后移 |
| Alt | C | 将当前单词首字母转为大写,光标后移 |
| Alt | L | 将当前单词全部转为小写,光标后移(zsh无效) |

*******************
## Jump
| Controller | Key | comment |
|:---|:----|:----|
| Ctrl | C | 取消运行当前行输入的命令，相当于Ctrl + Break |
| Ctrl | A | 光标移动到行首（Ahead of line），相当于通常的Home键 |
| Ctrl | E | 光标移动到行尾（End of line） |
| Ctrl | F | 光标向前(Forward)移动一个字符位置 |
| Ctrl | B | 光标往回(Backward)移动一个字符位置 |
| Alt | F | 光标向前(Forward)移动一个单词位置 |
| Alt | B | 光标往回(Backward)移动一个单词位置 |
| Esc | F | 光标向前(Forward)移动到当前单词的头部 |
| Esc | B | 光标往回(Backward)移动到当前单词的尾部 |

*****************************
## Search
| Controller | Key | comment |
|:---|:----|:----|
| Ctrl | P | 调出命令历史中的前一条（Previous）命令，相当于通常的上箭头 |
| Ctrl | N | 调出命令历史中的下一条（Next）命令，相当于通常的下箭头 |
| Ctrl | O | 运行上翻下翻出来的命令, 并且自动将下一条命令填入 |
| Ctrl | R | 向上搜索相关命令（reverse-i-search）继续按 Ctrl R 则继续搜索上一条 |
| Ctrl | S | 与 Ctrl R 类似, 但是是向下搜索 |

**************************
## Control
| Controller | Key | comment |
|:---|:----|:----|
|Ctrl |Z|暂停程序 |
| Ctrl | S | 停止回显当前Shell |
| Ctrl | Q | 恢复回显当前Shell |

## 对比
### 文件系统对比
> [参考博客: 如何选择文件系统：EXT4、Btrfs 和 XFS ](https://linux.cn/article-7083-1.html)

目前 Linux 大多采用 ext3,往 ext4 过渡

以及 zfs 的优劣

### 桌面环境对比
> [Arch Doc: desktop environment](https://wiki.archlinux.org/index.php/Desktop_environment_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
> [参考: Linux下15款桌面环境](https://www.lulinux.com/archives/444)

1. **gnome** 占用资源中等，个人对该桌面不感冒
1. **xfce** 占用资源少，操作类似于xp
1. **kde** 功能强大，占用资源中等
    - [Arch Doc: KDE](https://wiki.archlinux.org/index.php/KDE)
    - [知乎 KDE如何配置得漂亮大气？](https://www.zhihu.com/question/54147372)
1. **dde** deepin设计的桌面环境，小bug略多，但是美观操作方便

- [dde kde gnome](https://bbs.deepin.org/forum.php?mod=viewthread&tid=38498)

> [X窗口系统的协议和架构](http://www.cnblogs.com/noble/p/4144098.html)
> [Arch Doc: Xorg](https://wiki.archlinux.org/index.php/Xorg_(简体中文))

### 窗口管理器对比
> [Arch Doc: window manager](https://wiki.archlinux.org/index.php/Window_manager_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

- [awesome window manager](https://awesomewm.org/) `平铺式的`

***************************
### 文件管理器对比
> 有单窗口，双列，命令，简洁轻量，笨重完整 各种各样的选择

- `nautilus` Gnome默认 挺好用，但是不能自动挂载分区
- `deepin-filemanager` deepin默认，较为方便，但是打开手机会卡根本打不开
- `pcmanfm` 左边侧栏目录树 会同步nautilus的配置`5m`
- `rox-filer` 特别小，单击打开，迅速定位文件，适合找东西用
- `thunar` 解决了nautilus的缺点，内存也很省 `21M`
- `dolphin` 多标签页，目录树方式查看
- `nemo` mint默认的，功能齐全，会同步nautilus的配置，同样有目录树而且是两边都有 `21M`
- `tuxcmd` Tux Commander 双列，小，直接的目录树，学习成本高点 `2M`

*******************************
### 终端模拟器对比
> [详细](/Linux/Tool/Terminal.md)

*****************************************************

# Tips
> man help 后接使用的命令，就可以得到用户手册和帮助文档

## 一行执行多条命令 
- ` && ` 第2条命令只有在第1条命令成功执行之后才执行 根据命令产生的退出码判断是否执行成功（0成功，非0失败）
- `|| ` 执行不成功（产生了一个非0的退出码）时，才执行后面的命令
- ` ; ` 顺序执行多条命令，当;号前的命令执行完（不管是否执行成功），才执行;后的命令。 
- ` & `  并行执行命令，没有顺序

- [tty 虚拟终端等概念](https://www.ibm.com/developerworks/cn/linux/l-cn-termi-hanzi/)

- Centos上which并不是命令, 而是别名!
    - `which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'`

**************
## 让命令在后台运行
> [参考 Linux 技巧：让进程在后台可靠运行的几种方法 ](https://www.ibm.com/developerworks/cn/linux/l-cn-nohup/)

- 命令后接 & （只是让进程躲到当前终端的后台去了 hup信号仍然影响）

`nohup， disown, screen, setid `
- 运行的命令不因 用户注销，网络中断等因素而中断
    - 让进程对hup信号免疫 nohup disown
    - 让进程在新的会话中运行 setid screen

### 关闭ssh回话不能运行
1. 没有使用任何修饰原有命令  
1. 只在原有命令后加&

### 关闭ssh回话仍能运行
> 两种方式

1. 使用`nohup`就能屏蔽hup信号，标准输出会输出到当前目录下的nohup.out文件. `nohup 命令 &`
    1. 将所有输出重定向到空设备  `nohup 命令>/dev/null 2>&1`
    1. 例如 在当前目录后台打开文件管理器 `(dde-file-manager . &) >/dev/null 2>&1`
1. `(命令 &)` 屏蔽了hup信号

*************
## 修改主机名
- `sudo hostname linux` 重启终端即可看到修改
- 但是重启电脑会恢复原有名字修改如下文件永久： `sudo gedit /etc/hostname` 也许需要更改`/etc/hosts`
- 立即生效,也要重新登录 `hostname -F /etc/hostname `

