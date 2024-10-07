---
title: Linux基础
date: 2018-12-15 11:11:23
tags: 
    - 基础
categories: 
    - Linux
---

💠

- 1. [Linux系统](#linux系统)
    - 1.1. [Boot](#boot)
        - 1.1.1. [grub](#grub)
    - 1.2. [用户管理](#用户管理)
        - 1.2.1. [用户](#用户)
        - 1.2.2. [用户组](#用户组)
        - 1.2.3. [sudo](#sudo)
        - 1.2.4. [终端和登录](#终端和登录)
    - 1.3. [环境变量](#环境变量)
    - 1.4. [进程](#进程)
        - 1.4.1. [信号 Signal](#信号-signal)
        - 1.4.2. [信号量 Semaphore](#信号量-semaphore)
        - 1.4.3. [孤儿进程和僵死进程](#孤儿进程和僵死进程)
            - 1.4.3.1. [孤儿进程](#孤儿进程)
            - 1.4.3.2. [僵死进程 defunct](#僵死进程-defunct)
        - 1.4.4. [守护进程](#守护进程)
        - 1.4.5. [文件描述符 FD](#文件描述符-fd)
        - 1.4.6. [线程](#线程)
    - 1.5. [时间](#时间)
    - 1.6. [服务管理](#服务管理)
        - 1.6.1. [init进程](#init进程)
        - 1.6.2. [systemd 方式服务管理](#systemd-方式服务管理)
        - 1.6.3. [service 方式管理](#service-方式管理)
            - 1.6.3.1. [自定义 service](#自定义-service)
        - 1.6.4. [update-rc.d 方式管理](#update-rcd-方式管理)
- 2. [系统资源管理](#系统资源管理)
    - 2.1. [ulimit](#ulimit)
    - 2.2. [CPU](#cpu)
    - 2.3. [内存](#内存)
        - 2.3.1. [overcommit](#overcommit)
        - 2.3.2. [oom](#oom)
        - 2.3.3. [虚拟内存](#虚拟内存)
        - 2.3.4. [交换内存](#交换内存)
            - 2.3.4.1. [清空交换内存](#清空交换内存)
        - 2.3.5. [清空读写缓存](#清空读写缓存)
- 3. [终端快捷键](#终端快捷键)
    - 3.1. [Delete](#delete)
    - 3.2. [Convert](#convert)
    - 3.3. [Jump](#jump)
    - 3.4. [Search](#search)
    - 3.5. [Control](#control)
- 4. [常见对比](#常见对比)
    - 4.1. [文件系统对比](#文件系统对比)
    - 4.2. [桌面环境对比](#桌面环境对比)
    - 4.3. [窗口管理器对比](#窗口管理器对比)
    - 4.4. [文件管理器对比](#文件管理器对比)
    - 4.5. [包管理](#包管理)
        - 4.5.1. [AppImage](#appimage)
        - 4.5.2. [snap](#snap)
        - 4.5.3. [flatpak](#flatpak)
- 5. [Tips](#tips)
    - 5.1. [一行执行多条命令](#一行执行多条命令)
    - 5.2. [让命令在后台运行](#让命令在后台运行)
    - 5.3. [修改主机名](#修改主机名)
    - 5.4. [文件类型默认打开方式 MIME](#文件类型默认打开方式-mime)
    - 5.5. [熵池](#熵池)

💠 2024-10-07 23:15:25
****************************************

# Linux系统

- [Arch wiki](https://wiki.archlinux.org/)
- [Deepin wiki](https://wiki.deepin.org/)
- [RUNOOB.COM](http://www.runoob.com) `各种技术学习 文档资源`
- [linux-tutorial](https://github.com/dunwu/linux-tutorial)
- [How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server)

- [Linux中国开源社区](https://linux.cn/)
- [LinuxTOY 是一个致力于提供 Linux 相关资讯的专题站点。](https://linuxtoy.org/)
  - [内容Github源](https://github.com/LinuxTOY/linuxtoy.org)
- [鳥哥的 Linux 私房菜](http://linux.vbird.org/linux_basic/)
- [阿里云系统组技术博客](https://kernel.taobao.org/)
- [Awesome Linux Software](https://github.com/luong-komorebi/Awesome-Linux-Software)

> 新手的话 特别注意不要随意 root权限 直接更改配置文件，容易导致系统crash（除非你明确的知道这个更改操作的作用， 即使如此也需要先备份原文件）

> [在线Linux终端](https://itsfoss.com/online-linux-terminals/) `有浏览器虚拟化，以及远程主机多种类型的实现`

> [闪客：品读 Linux 0.11 核心代码](https://github.com/dibingfa/flash-linux0.11-talk)

![](/Linux/Base/img/001-linux-base-cmd.km.svg)

## Boot
安装和启动Linux

> [Ventoy](https://github.com/ventoy/Ventoy)`无需烧录，复制ISO进U盘即可使用`

### grub 
> [GNU GRUB](https://www.gnu.org/software/grub/) *GRand Unified Bootloader*


- [ ] Windows 自动更新后的故障，开机需要手动指定boot分区后启动
```sh 
  set prefix=(hd0,msdos7)/grub
  insmod normal 
  normal 
```

************************

## 用户管理

### 用户

- 添加用户 test1 `sudo adduser test1`
    - 注意 `useradd` 只新建用户不会创建对应的主目录
- 删除用户以及对应的home目录：`sudo deluser username --remove-home`
- _切换用户_ `su`
- `su -l username` 当前用户的环境下登录用户（当成一个程序一样可以退出登录）
- `sudo su -` 相比于 sudo su 会加载root用户环境变量，切换到HOME工作目录[su &amp; su -](https://www.geeksforgeeks.org/difference-between-su-and-su-command-in-linux/)
- _修改密码_ `passwd`
  - `passwd user`
  - `echo "root:caishi" | chpasswd` 如果是普通用户就是 sudo chpasswd
- _修改相关信息_ `usermod`

| verb | long verb                | comment                                                      |
| :--: | :----------------------- | :----------------------------------------------------------- |
|  -d  | --home HOME_DIR          | 用户的新主目录                                               |
|  -e  | --expiredate EXPIRE_DATE | 设定帐户过期的日期为 EXPIRE_DATE                             |
|  -f  | --inactive INACTIVE      | 过期 INACTIVE 天数后，设定密码为失效状态                     |
|  -g  | --gid GROUP              | 强制使用 GROUP 为新主组                                      |
|  -G  | --groups GROUPS          | 新的附加组列表 GROUPS                                        |
|  -a  | --append GROUP           | 将用户追加至上边 -G 中提到的附加组中，并不从其它组中删除此用 |
|  -l  | --login LOGIN            | 新的登录名称                                                 |
|  -L  | --lock                   | 锁定用户账号                                                 |
|  -m  | --move-home              | 将家目录内容移至新位置 (仅于 -d 一起使用)                    |
|  -p  | --password PASSWORD      | 将加密过的密码 (PASSWORD) 设为新密码                         |
|  -R  | --root CHROOT_DIR        | chroot 到的目录                                              |
|  -s  | --shell SHELL            | 该用户账号的新登录 shell                                     |
|  -U  | --unlock                 | 解锁用户账号                                                 |

> [所有参数说明](https://gitee.com/kcp1104/codes/gca14wtqvm67l9j5r0deb56#usermod.md)

************************

- `less /etc/passwd` 查看全部用户及其用户组
- `passwd 选项 用户名` 更改口令(密码)
  - `-l 锁定口令，禁用账号`  `-u 口令解锁` `-d 账号无口令` `-f 强迫用户下次登录时修改口令`
  - 当前用户 `passwd` 就是修改当前用户口令 超级用户就可以命令后接用户名，修改任意用户

************************

- pwcov 注：同步用户从/etc/passwd 到/etc/shadow
- pwck 注：pwck是校验用户配置文件/etc/passwd 和/etc/shadow 文件内容是否合法或完整;
- pwunconv 注：是pwcov 的立逆向操作，是从/etc/shadow和 /etc/passwd 创建/etc/passwd ，然后会删除 /etc/shadow 文件;
- finger 注：查看用户信息工具
- id 注：查看用户的UID、GID及所归属的用户组
- chfn 注：更改用户信息工具
- `visudo` 注：visodo 是编辑 /etc/sudoers 的命令;也可以不用这个命令，直接用vi 来编辑 /etc/sudoers 的效果是一样的;
- `who /var/log/wtmp` 查看登录记录

### 用户组

> [相关 博客](http://www.runoob.com/linux/linux-user-manage.html)

- _添加用户组_ `groupadd`
  - 缺省参数 就是新建用户组
  - `-g GID` 指定新用户组的组标识号GID
  - `-o` 一般和g共用 表示新用户组的GID可以与系统已有用户组的GID相同。
- _显示用户所在组_ `groups [user]` 缺省是当前用户, 或输出指定用户的用户组
- _修改用户组_ `sudo usermod -G 用户组 用户`
- _删除用户组_ `groupdel`

- `groupmod 选项 用户组`
  - -g GID 为用户组指定新的组标识号。
  - -o 与-g选项同时使用，用户组的新GID可以与系统已有用户组的GID相同。
  - -n 新用户组 将用户组的名字改为新名字
  - -a `gpasswd -a user group`
- grpck 检查 `/etc/group`文件是否正确
- grpconv 注：通过/etc/group和/etc/gshadow 的文件内容来同步或创建/etc/gshadow ，如果/etc/gshadow 不存在则创建;
- 注：通过/etc/group 和/etc/gshadow 文件内容来同步或创建/etc/group ，然后删除gshadow文件

### sudo

- 添加用户 test1 到sudo组  注意： *将用户加入sudo组，debian系有效 alpine和arch无效 只能改文件*
  1. 将用户 testUser 加入 sudo 组 `sudo gpasswd -a test1 sudo`  *或者* `usermod -G sudo test1`
  2. *或者*：使用修改文件的方式：（不推荐）
     - `chmod 777 /etc/sudoers`  然后直接 `sudo visudo`就是调用vi来打开文件的简写
     - 添加一行 Debian: `test1  ALL=(ALL:ALL)ALL` 注意 Centos:`test1   ALL=(ALL)       ALL`
       - 设置sudo无需密码 `test1 ALL=(ALL) NOPASSWD: ALL`
     - `chmod 440 /etc/sudoers`

> 绝对路径执行shell报错无权限
> 环境：

- a 和 b 用户都属于用户组 b
- 当前工作目录是 /home/b/app/
  现象：

1. sudo -u a sh run.sh 正常执行
2. sudo -u a sh /home/b/app/run.sh 报错无权限

原因：

1. /home/b/ 目录对于用户组b没有任何权限，chmod 740 b 加上组的读权限后仍报错，改成750后正常了
2. [Commands don&#39;t have permission when using absolute path](https://askubuntu.com/questions/367176/commands-dont-have-permission-when-using-absolute-path)

方案：逐级排查shell所有父目录对于 `sudo指定用户`是否有执行权限

> sudo: 没有终端存在,且未指定 askpass 程序

- 设置用户为NOPASSWD

### 终端和登录

> [参考: linux终端相关概念解释及描述](https://www.cnblogs.com/xiangtingshen/p/10889195.html)
> [参考: 终端基本概念&amp;终端登录过程详解](https://blog.csdn.net/summy_j/article/details/73870353)

1. tty 终端设备的统称
   - 通常使用tty来简称各种类型的终端设备
2. pty 虚拟终端
   - 远程登录，图形化终端模拟器等操作使用
   - pts(pseudo-terminal slave)是pty的实现方法，与ptmx(pseudo-terminal master)配合使用实现pty。

> 通常Linux平台的终端模拟器新建tab时都是新建 pty， 但是Mac平台上则是新建tty

************************

## 环境变量

> [zsh 环境变量](http://zsh.sourceforge.net/Doc/Release/Files.html#Startup_002fShutdown-Files)
>
>> `.zshenv → [.zprofile if login] → [.zshrc if interactive] → [.zlogin if login] → [.zlogout sometimes].`
>>

> Bash 环境变量加载顺序

1. /etc/profile
2. $HOME/.bash_profile
3. $HOME/.bashrc
4. $HOME/.bash_login
5. $HOME/.profile

> [千万别混淆 Bash/Zsh 的四种运行模式](https://zhuanlan.zhihu.com/p/47819029)
> [
>     ssh连接远程主机执行脚本的环境变量问题](https://blog.csdn.net/whitehack/article/details/51705889)

alpine 里的sh和ash 默认是不登录shell 需要使用 sh -l 或者 ash -l 才会加载对应的文件

************************

## 进程

> 进程是由多个线程(至少有一个)以及持有资源的组合体， 线程可以理解为进程的执行单元

> 参考 深入理解计算机系统 书籍

1. pid_t 来表示一个进程的 pid，因此能表示的进程的范围一定不会超过 pid_t 数据类型的范围
   - 查看 pid 最大数量 `cat /proc/sys/kernel/pid_max`

> [doc: fork](http://pubs.opengroup.org/onlinepubs/7908799/xsh/fork.html)
> [wiki: fork bomb](https://en.wikipedia.org/wiki/Fork_bomb)

> [参考: linux常见进程与内核线程](https://www.cnblogs.com/createyuan/p/3979142.html) `0 1 2 等内核进程`

### 信号 Signal

`进程通信的一种标准化的方式`

> /bin/kill -L 可查看所有信号量

```
 1 HUP      2 INT      3 QUIT     4 ILL      5 TRAP     6 ABRT     7 BUS
 8 FPE      9 KILL    10 USR1    11 SEGV    12 USR2    13 PIPE    14 ALRM
15 TERM    16 STKFLT  17 CHLD    18 CONT    19 STOP    20 TSTP    21 TTIN
22 TTOU    23 URG     24 XCPU    25 XFSZ    26 VTALRM  27 PROF    28 WINCH
29 POLL    30 PWR     31 SYS
```

编号为 `1 ~ 31`的信号为传统UNIX支持的信号，是不可靠信号(非实时的)，编号为 `32 ~ 63`的信号是后来扩充的，称做可靠信号(实时信号)。不可靠信号和可靠信号的区别在于前者不支持排队，只是负责发送, 不负责存储和接收, 可能会造成信号丢失，而后者不会。

> [参考 Linux信号列表](https://blog.csdn.net/baobao8505/article/details/1115820)

> 常用信号

- 1 HUP
  - 终端关闭,Session 退出时会发出的信号
- 2 INT
  - interrupt 中断信号
- 9 KILL
  - kill 进程不可忽略该信号
- 15 TERM
  - terminate 终止信号

### 信号量 Semaphore

Linux内核的信号量用来操作系统进程间同步访问共享资源

信号量在创建时需要设置一个初始值，表示同时可以有几个任务可以访问该信号量保护的共享资源，当初始值为1时就变作互斥锁（Mutex），即同时只能有一个任务可以访问信号量保护的共享资源。

PV操作由P操作原语和V操作原语组成（原语是指不可中断的过程）
- P（S）：
    1. 将信号量S的值减1，即S=S-1；
    1. 如果S>=0，则该进程继续执行；否则该进程置为等待状态，排入等待队列
- V（S）：
    1. 将信号量S的值加1，即S=S+1；
    1. 如果S>0，则该进程继续执行；否则释放队列中第一个等待信号量的进程

PV操作的意义：我们用信号量及PV操作来实现进程的同步和互斥。PV操作属于进程的低级通信

使用PV操作实现进程互斥时应该注意的是：

    每个程序中用户实现互斥的P、V操作必须成对出现，先做P操作，进临界区，后做V操作，出临界区。若有多个分支，要认真检查其成对性
    P、V操作应分别紧靠临界区的头尾部，临界区的代码应尽可能短，不能有死循环
    互斥信号量的初值一般为1

### 孤儿进程和僵死进程

> [参考: 孤儿进程与僵死进程[总结]](http://www.cnblogs.com/Anker/p/3271773.html)

#### 孤儿进程

> 一个父进程退出，而它的子进程还在运行，那么那些子进程将成为孤儿进程。孤儿进程将被init进程(进程号为1)所收养，并由init进程对它们完成状态收集工作。

> 注意, 也有意外, 并不总是被 init 进程收养 [Ubuntu15.04 删除/sbin/upstart与孤儿进程收养的问题](https://blog.csdn.net/chilumanxi/article/details/47066331)

#### 僵死进程 defunct 

> 一个进程使用fork创建子进程，如果子进程退出，而父进程并没有调用wait或waitpid获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中, 这种进程称之为僵死进程。
> 因为直到父进程结束后, 该僵死子进程会成为孤儿进程且是僵死进程, 会被 init 收养, 从而被回收, 但是如果父进程一直没有结束, 僵死子进程会一直存在

- 危害:
  - 占用系统内存 pid等资源, 无法被回收

> 常规解决方案 [Github: 代码示例](https://github.com/Kuangcp/LearnC/tree/master/exception/process)

1. `处理信号`: 子进程退出时向父进程发送SIGCHILD信号，父进程处理SIGCHILD信号。在信号处理函数中调用wait进行处理僵死进程。
2. `fork两次`: 原理是将子进程成为孤儿进程，从而其的父进程变为init进程，通过init进程可以处理僵死进程。

> 暴力方案: 直接 kill 掉父进程, 父进程和僵死状态的子进程就一起被回收了

### 守护进程

> [参考: 守护进程](https://blog.csdn.net/lianghe_work/article/details/47659889)

### 文件描述符 FD
> [wikipedia: File descriptor](https://en.wikipedia.org/wiki/File_descriptor)  
> [参考: Linux下 文件描述符（fd）与 文件指针（FILE*）](https://blog.csdn.net/mm_hh/article/details/71374474)  

每一个进程在PCB（Process Control Block）即进程控制块中都保存着一分文件描述符表.  
文件描述符就是这个表的索引文件，描述符表中每个表项都有一个指向已打开文件的指针。现在我们明确一下：已打开的文件在内核中用file结构体表示，文件描述符表中的指针指向file结构体。

> FD方式管理的范畴
- 每个进程默认有的标准输入输出: 0标准输入 1标准输出 2错误输出
- 持有的文件(读/写)
- 网络连接 socket
- 管道 pipe

> 问题
- 线上的Centos7.9上运行的Java8进程，12月11日启动的进程，但是1月3日突然 /proc/pid/fd/下的fd都发生了更新`无法查看创建时间`，但是/proc/pid的目录时间是对的
   - 问题：为什么会发生修改，标准输入输出，以及依赖的jar的fd都发生了新创建和修改
   - 原因：proc是虚拟文件系统，属性值取决了查询或操作系统管理需要时构建出来

### 线程

1. 查看创建一个线程占用内存大小 `ulimit -s`
2. 查看进程下的线程 `ps -T pid`
3. 查看最大线程数 `cat /proc/sys/kernel/threads-max` 默认值 256287

************************

## 时间
> [ntpdate manual](https://linux.die.net/man/8/ntpdate)

- /etc/timezone 时区, /etc/localtime 时区及时间
- `/usr/sbin/ntpdate -q cn.pool.ntp.org` 查看差异

> **时间同步**

1. 修改时区 `cp -y /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`
2. 同步时间 `/usr/sbin/ntpdate -u cn.pool.ntp.org` | 没有就先安装 ntpdate
    - 注意返回值 offset 为正说明本地比远程慢，负数则相反，本地比远程快
3. 查看BIOS硬件时间 `hwclock -r`
    - 如果不同步就需要写入时间 `hwclock -w` _因为系统重启后用硬件时间初始化的_

> 同步时间 扩展

- chrony 比 ntpupdate 功能更多，可定时同步时间
- 服务器领域 ntpd 会更合适，因为 ntpupdate是立刻修改时钟 会带来时钟跃变的问题，但是ntpd是将误差的时间在一段时间内平缓的调整。[Linux 时间同步服务 -- ntp 和 chrony](https://blog.epurs.com/post/ntp-and-chrony/)

- **自动同步时间**
    1. 配置开机自动校验 `vim /etc/rc.d/rc.local`
    - `/usr/sbin/ntpdate -u cn.pool.ntp.org> /dev/null 2>&1; /sbin/hwclock -w`
    2. 配置定时任务 `crontab -e`
    - `00 10 * * * root /usr/sbin/ntpdate -u cn.pool.ntp.org > /dev/null 2>&1; /sbin/hwclock -w `

************************

## 服务管理

### init进程

> [参考: 服务相关命令](https://blog.csdn.net/qq_37993487/article/details/79868857)

### systemd 方式服务管理

> [Arch Doc: systemd](https://wiki.archlinux.org/index.php/Systemd_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

- systemctl start/stop/restart/reload/edit serviceName **例如 sshd docker 等服务**

| command        | 作用                                                   |
| :------------- | :----------------------------------------------------- |
| start/stop     | 启动/停止服务                                          |
| enable/disable | 开机启用/禁用                                          |
| restart        | 如果服务在运行中，则重启服务，若不在运行中，则将会启动 |
| try-restart    | 只在服务已存在运行的状态下启动服务                     |
| reload         | 重新加载配置文件                                       |
| edit           | 修改服务配置                                           |
| status         | 查看运行状态                                           |

> 系统电源管理

| systemctl 命令         | 作用             |
| ---------------------- | ---------------- |
| systemctl poweroff     | 关闭系统         |
| systemctl reboot       | 重启系统         |
| systemctl suspend      | 进入待机模式     |
| systemctl hibernate    | 进入休眠模式     |
| systemctl hybrid-sleep | 进入混合休眠模式 |

************************

### service 方式管理

> /etc/init.d/ 是服务的存放目录

1. 列出所有服务的状态 `service --status-all`
2. 启动/关闭服务 `service ssh start/stop`

#### 自定义 service

> [参考: Run a Java Application as a Service on Linux](https://www.baeldung.com/linux/run-java-application-as-service)

### update-rc.d 方式管理

1. 移除MySQL的自启   `sudo update-rc.d -f mysql remove`
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

************************

# 系统资源管理

- 查看系统PCI设备：`lspci`
- 查看CPU信息：`more /proc/cpuinfo`
  - 查看物理CPU数：`cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l`
  - 查看每个物理CPU中的内核的个数：`cat /proc/cpuinfo | grep "cpu cores"`
  - 查看系统所有逻辑CPU个数：`cat /proc/cpuinfo | grep "processor" | wc -l`
- 查看系统内存信息：`more /proc/meminfo`
- 查看磁盘分区信息：`df -l`

## ulimit

> [参考:  Linux下设置最大文件打开数nofile及nr_open、file-max](https://www.cnblogs.com/zengkefu/p/5635153.html)

1. 查看某进程limit状态 `cat /proc/xxxpid/limits`
2. 执行ulimit修改命令只对当前终端(tty)生效
3. 持久化修改设置： **/etc/security/limits.conf** 文件中添加，注销或重启后生效

   ```sh
   * soft nofile 4096
   * hard nofile 4096
   ```

## CPU

> [linux cpu load](https://www.scalyr.com/blog/linux-cpu-load/)

- Usage 和 Load 的区别， 使用率针对于Cpu 时间，负载针对于等待和进行中的线程
- 使用uptime、top或者 `cat /proc/loadavg`都可以看到CPU的load 1 5 15 分钟的负载。
    - LOAD AVERAGE：一段时间内处于可运行状态和不可中断状态的进程平均数量,它是从另外一个角度体现CPU的使用状态。
        - 可运行分为正在`运行进程`和`正在等待CPU`的进程，**状态为R**
        - 不可中断则是它正在做某些工作不能被中断比如等待磁盘IO等，**其状态为D**
    > 注意: 一个逻辑核且负载为1时表示有线程一直在等待或运行（满载），四个逻辑核且负载为4时表示四个核心都一直有线程在等待或运行（满载）
- lscpu 展示CPU信息

- taskset 将任务绑定在指定cpu核心上

************************

## 内存
对于Linux来说, 有内存就去分配使用, 只有内存不够申请的大小，才会去释放 buffer或cache, 对于服务器来说, 交换内存会带来性能的明显下降 一般是不会配置的  

内存组成
- 空闲内存, 已使用, buffers, cached
  - 读 cache 写 buffer

- Virtual Memory   虚拟内存
- Resident Memory  持久内存
- Shared Memory    共享内存(多进程间共享)

> [linux ate my ram](https://www.linuxatemyram.com/)  
> [Empty the Buffer and Cache in Linux](https://www.baeldung.com/linux/empty-buffer-cache)

查看内存大页设置 `cat /sys/kernel/mm/transparent_hugepage/enabled`  
关闭内存大页 `echo never > /sys/kernel/mm/transparent_hugepage/enabled`  

### overcommit 
> [参考: Linux Overcommit Modes](https://www.baeldung.com/linux/overcommit-modes)  

- 内核参数： vm.overcommit_memory 
    - 0 允许overcommit但是算法判断是否合理，不合理会拒绝对应进程的内存申请
    - 1 允许overcommit
    - 2 禁止overcommit

- `cat /proc/meminfo | grep commit`
    - CommitLimit 就是overcommit的阈值，申请的内存总数超过CommitLimit的话就算是overcommit。
        - CommitLimit = (Physical RAM * vm.overcommit_ratio / 100) + Swap
    - Committed_AS 表示所有进程已经申请的内存总大小，（注意是已经申请的，不是已经分配的），如果 Committed_AS 超过 CommitLimit 就表示发生了 overcommit
        - 超出越多表示 overcommit 越严重。Committed_AS 的含义换一种说法就是，如果要绝对保证不发生OOM (out of memory) 需要多少物理内存。

### oom
当操作系统认为内存不足时，会选择分数值较高的进程kill掉（用户进程，非内核进程）
- /proc/pid/oom_score 操作系统所计算值
- /proc/pid/oom_score_adj 可以修改的值，当前值加上oom_score后才是最终值
    - 降低分值 echo -50 > /proc/pid/oom_score_adj
- /proc/pid/oom_adj 对应进程的优先级 

### 虚拟内存

> [参考: What does Virtual memory size in top mean?](https://serverfault.com/questions/138427/what-does-virtual-memory-size-in-top-mean)  
> [参考: The Right Way to Monitor Virtual Memory on Linux](https://www.logicmonitor.com/blog/the-right-way-to-monitor-virtual-memory-on-linux/)  

### 交换内存
> swapon, swapoff - enable/disable devices and files for paging and swapping

> [交换内存文件](/Linux/Base/LinuxDirectoryStructure.md#设置交换内存文件)

> 交换内存分析
VIRT = SWAP + RES or equal
SWAP = VIRT - RES

- 查看进程使用交换内存 `grep -i VmSwap /proc/*/status` 
- 进程按交换内存使用大小排序`for file in /proc/*/status ; do awk '/VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; done | sort -k 2 -n -r | less`
- `smem`  Report memory usage with shared memory divided proportionally

#### 清空交换内存
- 1.关闭交换分区 `sudo swapoff 交换分区文件`
    - 2.开启交换分区 `sudo swapon 交换分区文件`
- `swapoff -a && swapon -a`
    - 前提是交换分区已在 `/etc/fstab` 中配置

### 清空读写缓存
注意： 读 cache 写 buffer， 设计是为了提高读写效率，如果内存不足时可以考虑释放这部分内存，但是也会带来读写缓存失效重新读磁盘的性能问题，需慎重考虑。

> [参考: 如何在 Linux 中清除缓存（Cache）？](https://linux.cn/article-5627-1.html) `注意要切换到root再运行命令`  
> [参考: Linux 内存中的Cache，真的能被回收么？](https://www.cnblogs.com/276815076/p/5478966.html)  

************************

设置值 `sync; echo 1 > /proc/sys/vm/drop_caches`

| 设置值 | 作用 |
|:----|:----|
| 1 | 仅清除 page cache |
| 2 | 表示清除回收 slab 分配器中的对象（包括目录项缓存和 inode 缓存） |
| 3 | 表示清除 page cache 和 slab 分配器中的缓存对象 |

> 注意sync命令是为了将内存中buffer写入磁盘，避免这部分内存被直接释放导致数据不一致

************************

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

| Controller | Key | comment                                                                                         |
| :--------- | :-- | :---------------------------------------------------------------------------------------------- |
| Ctrl       | D   | 删除光标后字符,等价于Delete键（命令行若无任何字符，则相当于exit；处理 多行标准输入时也表示EOF） |
| Ctrl       | H   | 退格删除一个字符，相当于通常的Backspace键                                                       |
| Ctrl       | U   | 删除光标之前到 行首 的字符 (Zsh中是删除整行)                                                    |
| Esc        | W   | 删除光标之前到 行首 的字符                                                                      |
| Ctrl       | K   | 删除光标之前到 行尾 的字符                                                                      |
| Ctrl       | W   | 删除光标之前的一个单词                                                                          |
| Alt        | D   | 删除光标之后的一个单词                                                                          |
| Ctrl       | Y   | 粘贴上次删除的所有字符                                                                          |
| Ctrl       | _   | 撤销修改 等价于 `Ctrl x u`                                                                    |

************************

## Convert

| Controller | Key | comment                                            |
| :--------- | :-- | :------------------------------------------------- |
| Ctrl       | T   | 互换当前字符,光标后移                              |
| Alt        | T   | 互换当前单词与前一个单词,光标后移 等价于 `Esc T` |
| Alt        | D   | 将当前单词全部转为大写,光标后移                    |
| Alt        | C   | 将当前单词首字母转为大写,光标后移                  |
| Alt        | L   | 将当前单词全部转为小写,光标后移(zsh无效)           |

************************

## Jump

| Controller | Key | comment                                             |
| :--------- | :-- | :-------------------------------------------------- |
| Ctrl       | C   | 取消运行当前行输入的命令，相当于Ctrl + Break        |
| Ctrl       | A   | 光标移动到行首（Ahead of line），相当于通常的Home键 |
| Ctrl       | E   | 光标移动到行尾（End of line）                       |
| Ctrl       | F   | 光标向前(Forward)移动一个字符位置                   |
| Ctrl       | B   | 光标往回(Backward)移动一个字符位置                  |
| Alt        | F   | 光标向前(Forward)移动一个单词位置                   |
| Alt        | B   | 光标往回(Backward)移动一个单词位置                  |
| Esc        | F   | 光标向前(Forward)移动到当前单词的头部               |
| Esc        | B   | 光标往回(Backward)移动到当前单词的尾部              |

************************

## Search

| Controller | Key | comment                                                            |
| :--------- | :-- | :----------------------------------------------------------------- |
| Ctrl       | P   | 调出命令历史中的前一条（Previous）命令，相当于通常的上箭头         |
| Ctrl       | N   | 调出命令历史中的下一条（Next）命令，相当于通常的下箭头             |
| Ctrl       | O   | 运行上翻下翻出来的命令, 并且自动将下一条命令填入                   |
| Ctrl       | R   | 向上搜索相关命令（reverse-i-search）继续按 Ctrl R 则继续搜索上一条 |
| Ctrl       | S   | 与 Ctrl R 类似, 但是是向下搜索                                     |

************************

## Control

| Controller | Key | comment           |
| :--------- | :-- | :---------------- |
| Ctrl       | Z   | 暂停程序          |
| Ctrl       | S   | 停止回显当前Shell |
| Ctrl       | Q   | 恢复回显当前Shell |

************************

# 常见对比

## 文件系统对比

> [参考: 如何选择文件系统：EXT4、Btrfs 和 XFS ](https://linux.cn/article-7083-1.html)

目前 Linux 大多采用 ext4, Btrfs

Btrfs 的快照功能很适合 Arch 系统，滚动更新挂掉的话可以通过历史快照恢复回来

## 桌面环境对比

> [Arch Doc: desktop environment](https://wiki.archlinux.org/index.php/Desktop_environment_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
> [参考: Linux下15款桌面环境](https://www.lulinux.com/archives/444)

1. **gnome** 占用资源中等，个人对该桌面不感冒
2. **xfce** 占用资源少且稳定，但是UI方面可定制的点较少，目前也是个人使用了5年+的桌面管理器
3. **kde** 功能强大，占用资源中等
   - [Arch Doc: KDE](https://wiki.archlinux.org/index.php/KDE)
   - [知乎 KDE如何配置得漂亮大气？](https://www.zhihu.com/question/54147372)
4. **dde-wm** Deepin 基于 `gnome mutter`设计的桌面环境，小bug略多，而且渲染会占用较多资源，容易卡顿，但是美观操作方便
   1. 后续Deepin基于kwin更换了窗口管理器 `dde-kwin`，流畅了一些，但是窗口顶部有个大的Title [隐藏Deppin大标题栏](https://www.jianshu.com/p/f90526bbe0c9)

- [dde kde gnome](https://bbs.deepin.org/forum.php?mod=viewthread&tid=38498)

> [X窗口系统的协议和架构](http://www.cnblogs.com/noble/p/4144098.html)
> [Arch Doc: Xorg](https://wiki.archlinux.org/index.php/Xorg_(简体中文))

## 窗口管理器对比

> [Arch Doc: window manager](https://wiki.archlinux.org/index.php/Window_manager_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

- [awesome window manager](https://awesomewm.org/) `平铺式的`

************************

## 文件管理器对比

> 有单窗口，双列，命令，简洁轻量，笨重完整 各种各样的选择

- `nautilus` Gnome默认 挺好用，但是不能自动挂载分区
- `deepin-filemanager` deepin默认，较为方便，但是打开手机会卡根本打不开
- `pcmanfm` 左边侧栏目录树 会同步nautilus的配置
- `rox-filer` 特别小，单击打开，迅速定位文件，适合找东西用
- `thunar` 解决了nautilus的缺点，内存也很省
- `dolphin` 多标签页，目录树方式查看
- `nemo` mint默认的，功能齐全，会同步nautilus的配置，同样有目录树而且是两边都有
- `tuxcmd` Tux Commander 双列，小，直接的目录树，学习成本高点
- `ranger` 命令行内文件浏览和操作
- [Sigma File Manager](https://github.com/aleksey-hoffman/sigma-file-manager)

## 包管理
- 最通用的方式是编译安装，但是有门槛和编译环境兼容性问题
- 其次是绑定发行版的包，常分为两类 Debian系的deb包对应apt管理，REHL系的rpm包对应yum dnf管理
- 然后就是最近推行的 snap flatpak AppImage 等通用包，大致逻辑都是将软件包所有动态依赖项打包进去隔离，类似静态编译以支持跨发行版，当然缺点就是包的大小，但是相比于软件可用，存储也是小问题了。

### AppImage 

### snap 
只能从Ubuntu公司私有运营的商店下载软件,且apt安装部分软件时会替换为snap安装，因此被抨击背离Linux文化。
snap应用都是整个打成压缩包并且将每个软件单独挂载在只读的squashfs格式的分区下，应用启动时解压再执行

- [A universal app store for Linux](https://snapcraft.io/)
- [如何在Ubuntu中完全移除Snap](https://cloud.tencent.com/developer/article/2168090)
- [snap 已经在污染 apt](https://v2ex.com/t/1037576)

### flatpak 
- [Bubble wrap](https://wiki.archlinux.org/title/Bubblewrap)  

************************

# Tips

> man help 后接使用的命令，就可以得到用户手册和帮助文档

## 一行执行多条命令

- `&&` 第2条命令只有在第1条命令成功执行之后才执行 根据命令产生的退出码判断是否执行成功（0成功，非0失败）
- `||` 执行不成功（产生了一个非0的退出码）时，才执行后面的命令
- `;`  顺序执行多条命令，当;号前的命令执行完（不管是否执行成功），才执行;后的命令。
- `&`  并行执行命令，没有顺序
- [tty 虚拟终端等概念](https://www.ibm.com/developerworks/cn/linux/l-cn-termi-hanzi/)
- Centos上which并不是命令, 而是别名!

  - `which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'`

************************

## 让命令在后台运行

> [参考 Linux 技巧：让进程在后台可靠运行的几种方法 ](https://www.ibm.com/developerworks/cn/linux/l-cn-nohup/)

- 命令后接 & （只是让进程成为job并在当前终端的后台执行 hup信号仍然能影响到）

运行的命令不因 用户注销，网络中断等因素而中断 `nohup， disown, screen, setid`

- 将进程对 hang up 信号免疫:
  - nohup, disown
- 将进程的父进程改为1号进程:
  - setid 或者 `(command &)`
- screen
  - 将进程托管给screen 类似tmux

> 示例
1. 使用 `nohup`就能屏蔽hup信号，标准输出会输出到当前目录下的nohup.out文件. `nohup 命令 &`
   1. 将标准输出重定向到空设备 并将错误输出重定向到标准输出  `nohup 命令>/dev/null 2>&1`
2. 例如 在当前目录后台打开文件管理器 `(dde-file-manager . &) >/dev/null 2>&1`

- ssh登录后 执行命令 (./xxx.sh &) 然后断开ssh连接，此时该脚本进程的 1 标准输出会显示 pst 被删除 例如 `1 -> /dev/pts/10 (deleted)`
  - 此时可使用 strace 命令得到标准输出 `strace -e write -p pid` (但局限于echo printf pwd等命令的输出，其他命令的输出不会被trace)

************************

## 修改主机名

- `sudo hostname linux` 重启终端即可看到修改
- 但是重启电脑会恢复原有名字修改如下文件永久： `sudo gedit /etc/hostname` 也许需要更改 `/etc/hosts`
- 立即生效,也要重新登录 `hostname -F /etc/hostname `

************************

## 文件类型默认打开方式 MIME

> xdg-open 命令

************************

## 熵池

> [参考: Linux下熵池大小导致的一些问题](https://blog.csdn.net/chinoukin/article/details/102566755)

机器的环境中充满了各种各样的噪声，如硬件设备发生中断的时间，用户点击鼠标的时间间隔等是完全随机的，事先无法预测，以此作为熵池来源。

查看当前熵池大小  cat /proc/sys/kernel/random/entropy_avail
熵池最大值 cat /proc/sys/kernel/random/poolsize

当熵池不够时，会导致 gpg tomcat 等应用出现阻塞

可使用 [rng-tools](https://wiki.archlinux.org/index.php/Rng-tools) [Github](https://github.com/nhorman/rng-tools)进行补充熵池

- [ ] 但是 rng 项目的实现原理呢
