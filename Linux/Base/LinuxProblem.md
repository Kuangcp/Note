---
title: Linux桌面发行版遇到的问题
date: 2018-12-15 11:16:42
tags: 
    - 工具使用经验
categories: 
    - Linux
    - WIKI
---

💠

- 1. [Linux桌面发行版遇到的问题](#linux桌面发行版遇到的问题)
    - 1.1. [软件问题](#软件问题)
        - 1.1.1. [命令找不到](#命令找不到)
        - 1.1.2. [终端响铃](#终端响铃)
        - 1.1.3. [输入法](#输入法)
            - 1.1.3.1. [fcitx](#fcitx)
        - 1.1.4. [Flash](#flash)
        - 1.1.5. [tracker-extract 高CPU内存占用](#tracker-extract-高cpu内存占用)
    - 1.2. [驱动问题](#驱动问题)
        - 1.2.1. [显卡](#显卡)
            - 1.2.1.1. [Nvidia](#nvidia)
            - 1.2.1.2. [Manjaro 的NVIDIA驱动问题](#manjaro-的nvidia驱动问题)
            - 1.2.1.3. [Deepin 的NVIDIA驱动问题](#deepin-的nvidia驱动问题)
    - 1.3. [配置问题](#配置问题)
        - 1.3.1. [Ubuntu与Windows10时间相差8小时的解决](#ubuntu与windows10时间相差8小时的解决)
        - 1.3.2. [终端开启慢](#终端开启慢)
    - 1.4. [数据问题](#数据问题)
        - 1.4.1. [突然断电](#突然断电)
    - 1.5. [启动问题](#启动问题)
        - 1.5.1. [can't resume from suspend](#can't-resume-from-suspend)
        - 1.5.2. [i386-pc not found](#i386-pc-not-found)
    - 1.6. [崩溃](#崩溃)

💠 2025-05-14 11:55:13
****************************************
# Linux桌面发行版遇到的问题

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

大多数笔记本都是 Intel集显和 Nvidia/AMD 组成双显卡, 双显卡的管理就成了问题(指的是Linux下)
> [参考: 使用 Bumblebee 控制 NVIDIA 双显卡](https://www.cnblogs.com/congbo/archive/2012/09/12/2682105.html)

> [Serious Issue with NVIDIA Drivers: Compatibility Problems with Linux Kernel 6.10 | by Niemand | Aug, 2024 | Medium](https://medium.com/@TheNiemand/serious-issue-with-nvidia-drivers-compatibility-problems-with-linux-kernel-6-10-9cdb0791d204)`升级Manjaro到24.1后没注意到升级了内核和驱动，然后lightdm以及X都崩溃了`  
- 依据启动的内核，将驱动从 linux510 升级到 linux610-nvidia 550.120-6 问题就解决了，没有那么多奇奇怪怪的问题了（/boot分区加载失败，X启动失败找不到屏幕（nvidia内核模块加载失败），某个分区加载失败无法识别 ext4 文件系统）

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
> 由于Linux延迟写的特性，如果遇到操作系统突然断电，会导致文件损坏或缺失，从而引发各种诡异问题

************************

>1. 开机报错信息: fsck exited with status code 4

1. 根据报错提示的分区, 进行修复, 由于我的Linux是ext3文件系统 ext4 则是 `fsck.ext4`
1. `fsck.ext3 -y /dev/sda9` **分区根据实际情况**
1. 完成后重启即可

************************
>2. 导致了 Git 仓库都损坏了 `fatal: loose object`  

ZSH: corrupt history file

```shell
mv .zsh_history .zsh_history_bad
strings .zsh_history_bad > .zsh_history
fc -R .zsh_history
```

************************
>3. 导致了终端输出中文乱码 Unicode乱码，但是应用内(firefox vscode)中文输入正常，且粘贴板复制中文内容

## 启动问题
### can't resume from suspend 


### i386-pc not found
- /boot/grub/i386-pc BIOS 安装的引导
- /boot/grub/x86_64-efi EFI安装的引导

`/boot/grub/i386-pc/normal.mod` not found.

[gist](https://gist.github.com/AndersonIncorp/3acb1d657cb5eba285f4fb31f323d1c3?permalink_comment_id=3310958)


************************

## 崩溃

> 高内存占用，桌面管理器失去响应  journalctl -b -2 --since "2024-01-18" `重启过两次`
```log
    Jan 18 09:23:21 lightdm[2507179]: gkr-pam: unable to locate daemon control file
    Jan 18 09:23:21 lightdm[2507179]: gkr-pam: stashed password to try later in open session
    Jan 18 09:23:21 systemd[1]: Stopping Session c147 of User lightdm...
    Jan 18 09:23:21 lightdm[2507112]: pam_unix(lightdm-greeter:session): session closed for user lightdm
    Jan 18 09:23:21 systemd[1]: session-c147.scope: Deactivated successfully.
    Jan 18 09:23:21 systemd[1]: Stopped Session c147 of User lightdm.
    Jan 18 09:23:21 systemd[1]: session-c147.scope: Consumed 7.307s CPU time.
    Jan 18 09:23:21 systemd-logind[660]: Removed session c147.
    Jan 18 09:23:31 systemd[1]: Stopping User Manager for UID 966...
    Jan 18 09:23:31 systemd[2507120]: Activating special unit Exit the Session...
    Jan 18 09:23:31 systemd[2507120]: Stopped target Main User Target.
    Jan 18 09:23:31 systemd[2507120]: Stopping Accessibility services bus...
    Jan 18 09:23:31 gvfsd[2507153]: A connection to the bus can't be made
    Jan 18 09:23:31 systemd[2507120]: Stopping D-Bus User Message Bus...
    Jan 18 09:23:31 systemd[2507120]: Stopping Virtual filesystem service...
    Jan 18 09:23:31 systemd[2507120]: Stopped Accessibility services bus.
    Jan 18 09:23:31 systemd[2507120]: Stopped Virtual filesystem service.
    Jan 18 09:23:31 systemd[2507120]: Stopped target Basic System.
    Jan 18 09:23:31 systemd[2507120]: Stopped target Paths.
    Jan 18 09:23:31 systemd[2507120]: Stopped target Sockets.
    Jan 18 09:23:31 systemd[2507120]: Stopped target Timers.
    Jan 18 09:23:31 systemd[2507120]: Closed D-Bus User Message Bus Socket.
    Jan 18 09:23:31 systemd[2507120]: Closed GnuPG network certificate management daemon.
    Jan 18 09:23:31 systemd[2507120]: Closed GCR ssh-agent wrapper.
    Jan 18 09:23:31 systemd[2507120]: Closed GNOME Keyring daemon.
    Jan 18 09:23:31 systemd[2507120]: Closed GnuPG cryptographic agent and passphrase cache (access for web browsers).
    Jan 18 09:23:31 systemd[2507120]: Closed GnuPG cryptographic agent and passphrase cache (restricted).
    Jan 18 09:23:31 systemd[2507120]: Closed GnuPG cryptographic agent (ssh-agent emulation).
    Jan 18 09:23:31 systemd[2507120]: Closed GnuPG cryptographic agent and passphrase cache.
    Jan 18 09:23:31 systemd[2507120]: Closed p11-kit server.
    Jan 18 09:23:31 systemd[2507120]: Closed PipeWire Multimedia System Sockets.
    Jan 18 09:23:31 systemd[2507120]: Closed Sound System.
    Jan 18 09:23:31 systemd[2507120]: Removed slice User Application Slice.
    Jan 18 09:23:31 systemd[2507120]: Reached target Shutdown.
    Jan 18 09:23:31 systemd[2507120]: Finished Exit the Session.
    Jan 18 09:23:31 systemd[2507120]: Reached target Exit the Session.
```
- [System hangs on no input after "Reached system target shutdown"](https://www.reddit.com/r/archlinux/comments/16jimr2/system_hangs_on_no_input_after_reached_system/)`相近问题`



************************
> 崩溃，切换TTY5登录后终端疯狂输出日志无响应

Used+Cached高内存， `journalctl -b -1`查日志
```log
    Jan 29 11:28:49 zk-pc systemd[1]: Started Getty on tty5.
    Jan 29 11:28:53 zk-pc dbus-daemon[668]: [system] Activating via systemd: service name='org.freedesktop.home1' unit='dbus-org.freedesktop.home1.service' requested by ':1.3512' (uid=0 pid=3819>
    Jan 29 11:28:54 zk-pc dbus-daemon[668]: [system] Activation via systemd failed for unit 'dbus-org.freedesktop.home1.service': Unit dbus-org.freedesktop.home1.service not found.
    Jan 29 11:28:57 zk-pc login[3819083]: pam_unix(login:session): session opened for user zk(uid=1000) by zk(uid=0)
    Jan 29 11:29:01 zk-pc systemd-logind[671]: New session 279 of user zk.
    Jan 29 11:29:01 zk-pc systemd[1]: Started Session 279 of User zk.
    Jan 29 11:29:03 zk-pc login[3819083]: LOGIN ON tty5 BY zk
    Jan 29 11:29:05 zk-pc kernel: general protection fault, probably for non-canonical address 0xff00000000000010: 0000 [#1] PREEMPT SMP NOPTI
    Jan 29 11:29:06 zk-pc kernel: CPU: 8 PID: 3807890 Comm: Storage Diagnos Not tainted 5.15.139-1-MANJARO #1 096934fa2aab193b2a40cf54023e5b05e5276eb2
    Jan 29 11:29:07 zk-pc systemd-journald[375]: Missed 364 kernel messages
    Jan 29 11:29:07 zk-pc kernel: ---[ end trace 56f99a5ae8056f6e ]---
    Jan 29 11:29:08 zk-pc systemd-journald[375]: Missed 910 kernel messages
    Jan 29 11:29:08 zk-pc kernel: RSP: 002b:00007f6803a98590 EFLAGS: 00010217
    Jan 29 11:29:10 zk-pc systemd-journald[375]: Missed 1440 kernel messages
    Jan 29 11:29:10 zk-pc kernel: RSP: 0000:ffff9ee142597c30 EFLAGS: 00010246
```

```log
    Mar 19 14:46:19 zk-pc sudo[2511882]: pam_unix(sudo:session): session opened for user root(uid=0) by zk(uid=1000)
    Mar 19 14:46:19 zk-pc sudo[2511882]: pam_unix(sudo:session): session closed for user root
    Mar 19 14:46:25 zk-pc dbus-daemon[584]: [system] Activating via systemd: service name='org.freedesktop.home1' unit='dbus-org.freedesktop.home1.service' requested by ':1.2243' (uid=0 pid=2512>
    Mar 19 14:46:25 zk-pc dbus-daemon[584]: [system] Activation via systemd failed for unit 'dbus-org.freedesktop.home1.service': Unit dbus-org.freedesktop.home1.service not found.
    Mar 19 14:46:25 zk-pc sudo[2512066]:       zk : TTY=pts/47 ; PWD=/home/zk/Work/tg-assets-backend ; USER=root ; COMMAND=/bin/lsof -p 2453453
    Mar 19 14:46:25 zk-pc sudo[2512066]: pam_unix(sudo:session): session opened for user root(uid=0) by zk(uid=1000)
    Mar 19 14:46:25 zk-pc sudo[2512066]: pam_unix(sudo:session): session closed for user root
    Mar 19 14:48:49 zk-pc rtkit-daemon[1023]: Supervising 7 threads of 6 processes of 1 users.
    Mar 19 14:48:49 zk-pc rtkit-daemon[1023]: Supervising 7 threads of 6 processes of 1 users.
    Mar 19 14:49:33 zk-pc rtkit-daemon[1023]: Supervising 7 threads of 6 processes of 1 users.
    Mar 19 14:49:33 zk-pc rtkit-daemon[1023]: Supervising 7 threads of 6 processes of 1 users.
    Mar 19 14:49:33 zk-pc rtkit-daemon[1023]: Supervising 7 threads of 6 processes of 1 users.
    Mar 19 14:49:33 zk-pc rtkit-daemon[1023]: Supervising 7 threads of 6 processes of 1 users.
    Mar 19 14:49:33 zk-pc rtkit-daemon[1023]: Supervising 7 threads of 6 processes of 1 users.
    Mar 19 14:49:33 zk-pc rtkit-daemon[1023]: Supervising 7 threads of 6 processes of 1 users.
    Mar 19 14:51:35 zk-pc systemd-journald[375]: Under memory pressure, flushing caches.
    Mar 19 14:51:45 zk-pc systemd-journald[375]: Under memory pressure, flushing caches.
    Mar 19 14:51:46 zk-pc sshd[2517295]: ssh_dispatch_run_fatal: Connection from 192.168.131.11 port 9778: Broken pipe [preauth]
    Mar 19 14:53:45 zk-pc sshd[2517303]: fatal: Timeout before authentication for 192.168.131.11 port 9791
    Mar 19 14:53:51 zk-pc rtkit-daemon[1023]: Supervising 7 threads of 6 processes of 1 users.
```


************************
> ls 命令执行无结果，tmux内所有终端都卡住，无法执行命令，窗口假死，切换tty无法登录, 过一阵后，图形软件切换一个崩溃一个

重启后 找日志 `journalctl -r` 都无这次故障时间段的日志

怀疑磁盘满, 因为新开终端有报错  mkdir: cannot create directory ~/.cache/oh-my-zsh Read-only file system

> [修复super_block损坏 - 暴走的馒头 - 博客园](https://www.cnblogs.com/ggykx/p/10880563.html)  

- fsck -v /dev/sdb1 发现确实有十几个错误，修复后可以mount，但是存在部分配置数据丢失，大部分还在
