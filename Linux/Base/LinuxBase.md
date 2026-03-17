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
    - 1.3. [Terminal 终端](#terminal-终端)
        - 1.3.1. [终端对比](#终端对比)
        - 1.3.2. [终端中渲染图片](#终端中渲染图片)
        - 1.3.3. [终端的彩色输出](#终端的彩色输出)
            - 1.3.3.1. [ls配置彩色输出](#ls配置彩色输出)
        - 1.3.4. [终端快捷键](#终端快捷键)
    - 1.4. [环境变量](#环境变量)
    - 1.5. [进程](#进程)
        - 1.5.1. [信号 Signal](#信号-signal)
        - 1.5.2. [信号量 Semaphore](#信号量-semaphore)
        - 1.5.3. [孤儿进程和僵死进程](#孤儿进程和僵死进程)
            - 1.5.3.1. [孤儿进程](#孤儿进程)
            - 1.5.3.2. [僵死进程 defunct](#僵死进程-defunct)
        - 1.5.4. [守护进程](#守护进程)
        - 1.5.5. [文件描述符 FD](#文件描述符-fd)
        - 1.5.6. [线程](#线程)
    - 1.6. [时间](#时间)
    - 1.7. [服务管理](#服务管理)
        - 1.7.1. [init进程](#init进程)
        - 1.7.2. [systemd 方式服务管理](#systemd-方式服务管理)
        - 1.7.3. [service 方式管理](#service-方式管理)
            - 1.7.3.1. [自定义 service](#自定义-service)
        - 1.7.4. [update-rc.d 方式管理](#update-rcd-方式管理)
    - 1.8. [内核](#内核)
- 2. [系统资源管理](#系统资源管理)
    - 2.1. [ulimit](#ulimit)
    - 2.2. [CPU](#cpu)
    - 2.3. [内存](#内存)
        - 2.3.1. [overcommit](#overcommit)
        - 2.3.2. [OOM Killer](#oom-killer)
            - 2.3.2.1. [容器OOM](#容器oom)
        - 2.3.3. [虚拟内存](#虚拟内存)
        - 2.3.4. [交换内存](#交换内存)
        - 2.3.5. [缓存 cache buffer](#缓存-cache-buffer)
    - 2.4. [内存管理](#内存管理)
        - 2.4.1. [glibc ptmalloc2](#glibc-ptmalloc2)
            - 2.4.1.1. [thread arena](#thread-arena)
            - 2.4.1.2. [thread arena 数量较多](#thread-arena-数量较多)
        - 2.4.2. [jemalloc](#jemalloc)
        - 2.4.3. [tcmalloc](#tcmalloc)
        - 2.4.4. [musl malloc](#musl-malloc)
- 3. [常见对比](#常见对比)
    - 3.1. [文件系统对比](#文件系统对比)
    - 3.2. [桌面环境对比](#桌面环境对比)
    - 3.3. [窗口管理器对比](#窗口管理器对比)
    - 3.4. [文件管理器对比](#文件管理器对比)
    - 3.5. [包管理](#包管理)
        - 3.5.1. [AppImage](#appimage)
        - 3.5.2. [snap](#snap)
        - 3.5.3. [flatpak](#flatpak)
- 4. [Tips](#tips)
    - 4.1. [一行执行多条命令](#一行执行多条命令)
    - 4.2. [让命令在后台运行](#让命令在后台运行)
    - 4.3. [修改主机名](#修改主机名)
    - 4.4. [文件类型默认打开方式 MIME](#文件类型默认打开方式-mime)
    - 4.5. [熵池](#熵池)

💠 2026-03-17 21:18:55
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
- `/etc/security/faillock.conf` deny 输错密码次数锁定，unlock_time 锁定的时长单位秒

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

添加用户 test1 到sudo组  注意： *将用户加入sudo组，debian系有效 alpine和arch无效 只能改文件*  
包括当用户执行sudo命令，输入正确密码，仍提示不正确，切root用户改了密码也是提示不正确，这个时候也需要检查是否在sudoers配置文件中有这个用户，虽然不知道为什么这个配置就消失了。。
1. 将用户加入 sudo 组 `sudo gpasswd -a test1 sudo`  *或* `usermod -G sudo test1`
2. 使用修改文件的方式：（不推荐）
    - `chmod 777 /etc/sudoers`  然后直接 `sudo visudo`就是调用vi来打开文件的简写
    - 添加一行 Debian: `test1  ALL=(ALL:ALL)ALL` 注意 Centos:`test1   ALL=(ALL)       ALL`
      - 设置sudo无需密码 `test1 ALL=(ALL) NOPASSWD: ALL`
    - `chmod 440 /etc/sudoers`

> 绝对路径执行shell报错无权限

环境：  a 和 b 用户都属于用户组 b 。当前工作目录是 /home/b/app/
现象： 
1. sudo -u a sh run.sh 正常执行
2. sudo -u a sh /home/b/app/run.sh 报错无权限
原因：
1. /home/b/ 目录对于用户组b没有任何权限，chmod 740 b 加上组的读权限后仍报错，改成750后正常了
2. [Commands don&#39;t have permission when using absolute path](https://askubuntu.com/questions/367176/commands-dont-have-permission-when-using-absolute-path)

方案： 逐级排查shell所有父目录对于 `sudo指定用户`是否有执行权限

> sudo: 没有终端存在,且未指定 askpass 程序

- 设置用户为NOPASSWD

## Terminal 终端

> [参考: linux终端相关概念解释及描述](https://www.cnblogs.com/xiangtingshen/p/10889195.html)
> [参考: 终端基本概念&amp;终端登录过程详解](https://blog.csdn.net/summy_j/article/details/73870353)

通常Linux平台的终端模拟器新建tab时都是新建 pty， 但是Mac平台上则是新建tty

1. tty 终端设备的统称
    - 通常使用tty来简称各种类型的终端设备
2. pty 虚拟终端
    - 远程登录，图形化终端模拟器等操作使用
    - pts(pseudo-terminal slave)是pty的实现方法，与ptmx(pseudo-terminal master)配合使用实现pty。

> [ibraheemdev/modern-unix](https://github.com/ibraheemdev/modern-unix)`现代工具合集`  
> [cli · GitHub Topics](https://github.com/topics/cli)`Github 终端工具合集`  
> [Making Terminal Applications in Rust with Termion](http://ticki.github.io/blog/making-terminal-applications-in-rust-with-termion/)  
> [Terminals Are Sexy](https://github.com/k4m4/terminals-are-sexy)  

- [terminalizer](https://github.com/faressoft/terminalizer)`录制终端`
- [Goph](https://github.com/Gogh-Co/Gogh)`切换配色方案`  
- [Sampler](https://github.com/sqshq/sampler)`终端可视化监控面板`  
- [charmbracelet/vhs: Your CLI home video recorder 📼](https://github.com/charmbracelet/vhs)  
- [wtfutil/wtf: The personal information dashboard for your terminal](https://github.com/wtfutil/wtf)  

> Web页面提供远程服务器的终端能力

- [ttyd](https://github.com/tsl0922/ttyd)  
- [sshx](https://github.com/ekzhang/sshx)  

### 终端对比

> 列举出系统可安装终端  
>  
> 1. Debian: `sudo apt search terminal | grep -E terminal.+amd64`  
> 2. Arch: `yay terminal`  
> 3. [Github Topic: terminal-emulator ](https://github.com/topics/terminal-emulator)  

终端可参考功能点： 终端透明化，终端背景图，快捷键设置，终端内颜色自定义，下拉式，标签水平垂直拆分，鼠标键盘交互性，资源占用少
终极工具 [Tmux](/Linux/Tool/Tmux.md) 可以摆脱终端模拟器的对比和选择，选择最简单省资源的模拟器即可

| 终端                | 优点                                            | 缺点                                                | 备注                                    |
| :------------------ | :---------------------------------------------- | :-------------------------------------------------- | :-------------------------------------- |
| `xiki`            | 鼠标和键盘高度交互 <br> 交互性和复杂度比较高 |                                                     |                                         |
| `qterminal`       | 设置设计清晰，功能完备                   | 终端内容显示兼容性略有问题 资源消耗中等             |                                         |
| `xfce4-terminal`  | 配合Xfce启动快，资源消耗少               | 配置繁琐                                            |                                         |
| `gnome-terminal`  | 简洁 资源消耗少                         | 多标签时，标签栏太大,标签页底部有白边；无法透明化 | 鼠标中键无法复制时需安装 `parcellite` |
| `mate-terminal`   | 标签栏更简洁，和 `gnome-terminal` 一致   |                                                     |                                         |
| `sakura`          | 外观上和前两个几乎一样，标签页可以更简洁    | 配置复杂 繁琐                                       |                                         |
| `deepin-terminal` | 功能很多，主题很多，功能最为强大           | 字体仅可选择内置不可自定义                          |                                         |
| `tilda`           | 内嵌于桌面上, 小命令方便                 | 需要查看文件时不方便                                |                                         |
| `terminology`     | 样式高度自定义                          |                                                     |                                         |

- tilix
- vte 支持复制终端输出内容为HTML
- st 不支持中文，unicode字符支持良好
- black box 
- [Alacritty - A cross-platform, OpenGL terminal emulator](https://alacritty.org/index.html)  

> 备注 sakura xfce4-terminal 快捷键配置
- `~/.config/xfce4/terminal/accels.scm`
- 配置语法： [doc](http://troubleshooters.com/linux/sakura.htm) | [config shortcut](https://unix.stackexchange.com/questions/102474/configuring-shortcuts-for-sakura)
- 例如 [修改 Ctrl C V 为复制快捷键](https://bbs.archlinux.org/viewtopic.php?id=260755) `Gtk3起 不支持所谓的鼠标悬浮改快捷键`
```lua
  (gtk_accel_path "<Actions>/terminal-window/copy" "<Primary>c")
  (gtk_accel_path "<Actions>/terminal-window/paste" "<Primary>v")
```

> 现代终端
- [wezterm](https://wezfurlong.org/wezterm/index.html)
- [Warp](https://github.com/warpdotdev/Warp) `Rust+AI`
- Tabby
- WindTerm
- [zellij](https://github.com/zellij-org/zellij)
- [kitty](https://sw.kovidgoyal.net/kitty/) `GPU渲染`
- [darktile](https://github.com/liamg/darktile)`GPU渲染，通过游戏引擎制作`

### 终端中渲染图片
- [sixel](https://en.wikipedia.org/wiki/Sixel)  | [libsixel](https://saitoha.github.io/libsixel/) | [Are We Sixel Yet?](https://www.arewesixelyet.com/)
  - [Why Sixel? ](https://www.reddit.com/r/commandline/comments/zkg75e/why_sixel/)

Manjaro Xfce 使用 sixel： 使用 mlterm 或者 konsole 终端模拟器，不支持 xfce4-terminal
1. yay libsixel, yay mlterm， mlterm -b '#292B2E' 安装和启动mlterm
  1. 查看图片 img2sixel xx.jpg `ImageMagick`
  1. 渲染结果图 [jagger](https://github.com/rs/jaggr) **konsole不支持**

### 终端的彩色输出

> [参考博客,比较详细](http://blog.csdn.net/magiclyj/article/details/72637666)
> [Linux Terminal Color](https://blog.csdn.net/y2701310012/article/details/40142809)

```sh
  red='\033[0;31m'
  green='\033[0;32m'
  yellow='\033[0;33m'
  blue='\033[0;34m'
  purple='\033[0;35m'
  cyan='\033[0;36m'
  white='\033[0;37m'
  default='\033[0m'
```

> 256 color

```sh
    # 测试 terminal 是否支持 256
    for i in {0..255} ; do
        printf "\x1b[48;5;%sm%3d\e[0m " "$i" "$i"
        if (( i == 15 )) || (( i > 15 )) && (( (i-15) % 6 == 0 )); then
            printf "\n";
        fi
    done
```

#### ls配置彩色输出

[Gihub: LS_COLORS](https://github.com/trapd00r/LS_COLORS)[customize bash prompt](https://www.howtogeek.com/307701/how-to-customize-and-colorize-your-bash-prompt/)

1. `curl https://raw.githubusercontent.com/trapd00r/LS_COLORS/master/LS_COLORS -o /etc/lscolor-256color`
2. 追加到 `*sh.rc`
   ```sh
   if [[ ("$TERM" = *256color || "$TERM" = screen* || "$TERM" = xterm* ) && -f /etc/lscolor-256color ]]; then
           eval $(dircolors -b /etc/lscolor-256color)
       else
               eval $(dircolors)
   fi
   ```

### 终端快捷键

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

> Delete

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

> Convert

| Controller | Key | comment                                            |
| :--------- | :-- | :------------------------------------------------- |
| Ctrl       | T   | 互换当前字符,光标后移                              |
| Alt        | T   | 互换当前单词与前一个单词,光标后移 等价于 `Esc T` |
| Alt        | D   | 将当前单词全部转为大写,光标后移                    |
| Alt        | C   | 将当前单词首字母转为大写,光标后移                  |
| Alt        | L   | 将当前单词全部转为小写,光标后移(zsh无效)           |

************************

> Jump

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

> Search

| Controller | Key | comment                                                            |
| :--------- | :-- | :----------------------------------------------------------------- |
| Ctrl       | P   | 调出命令历史中的前一条（Previous）命令，相当于通常的上箭头         |
| Ctrl       | N   | 调出命令历史中的下一条（Next）命令，相当于通常的下箭头             |
| Ctrl       | O   | 运行上翻下翻出来的命令, 并且自动将下一条命令填入                   |
| Ctrl       | R   | 向上搜索相关命令（reverse-i-search）继续按 Ctrl R 则继续搜索上一条 |
| Ctrl       | S   | 与 Ctrl R 类似, 但是是向下搜索                                     |

************************

> Control

| Controller | Key | comment           |
| :--------- | :-- | :---------------- |
| Ctrl       | Z   | 暂停程序          |
| Ctrl       | S   | 停止回显当前Shell |
| Ctrl       | Q   | 恢复回显当前Shell |

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
> [ssh连接远程主机执行脚本的环境变量问题](https://blog.csdn.net/whitehack/article/details/51705889)

alpine 里的sh和ash 默认是不登录shell 需要使用 sh -l 或者 ash -l 才会加载对应的文件

```sh
    # 通常声明环境变量时, 注意=左右无空格，变量名不能包含.符号
    export host='127.0.0.1'
```

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
  - 如果是Alpine这种ntp是busybox裁减版，执行命令后不会有输出，而是看退出码 `echo $?` 如果是0小于128ms 142反之

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

实际上服务注册在了 /etc/systemd/system/ 目录下的 serviceName.service 文件

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
| systemctl soft-reboot  | 软重启系统 254+版本支持 |
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

## 内核

> [Linux内核版本升级，性能到底提升多少？拿数据说话 | plantegg](https://plantegg.github.io/2019/12/24/Linux%E5%86%85%E6%A0%B8%E7%89%88%E6%9C%AC%E5%8D%87%E7%BA%A7%EF%BC%8C%E6%80%A7%E8%83%BD%E5%88%B0%E5%BA%95%E6%8F%90%E5%8D%87%E5%A4%9A%E5%B0%91%EF%BC%9F%E6%8B%BF%E6%95%B0%E6%8D%AE%E8%AF%B4%E8%AF%9D/#%E7%BB%A7%E7%BB%AD%E5%88%86%E6%9E%90%E4%B8%BA%E4%BB%80%E4%B9%884-19%E6%AF%944-9%E5%B7%AE%E4%BA%86%E8%BF%99%E4%B9%88%E5%A4%9A)  

> Minio启动时有警告说内核低于4.0 

这个警告是因为 MinIO 针对高性能存储进行了深度优化，而 Linux Kernel 4.0 之前（常见于 CentOS 7 的 3.10 内核）缺乏一些关键的现代文件系统和网络特性。
以下是内核过旧对 MinIO 的具体影响：

1. 文件系统性能限制 (XFS/ext4)

* Direct I/O 效率低：旧内核在处理高并发、大文件的直接读写时，容易产生 CPU 软中断瓶颈。
* 分配延迟：现代内核支持更高效的 fallocate（预分配空间），旧内核在高负载下可能会导致磁盘分配阻塞。

2. 网络栈性能 (TCP/UDP)

* TCP 吞吐限制：4.0+ 内核优化了 TCP 快恢复（Fast Recovery）和 TSO（分段偏移），旧内核在万兆网络环境下很难跑满带宽。
* 缺乏 Reuseport 优化：旧内核在处理海量并发连接时，多线程监听同一个端口的效率远低于现代内核。

3. 数据一致性风险 (O_DIRECT)

* MinIO 强依赖 O_DIRECT 来确保数据直接落盘而不经过内核缓存。在 3.x 内核中，特定情况下 O_DIRECT 与文件系统索引（Metadata）的同步存在已知的边缘 Bug，可能导致极端断电情况下的数据损坏风险。

4. 缺乏 OverlayFS 优化

* 如果你是在 Docker 里跑 MinIO，旧内核的 Overlay 驱动性能非常差，且存在 inode 耗尽的风险，直接影响 MinIO 的小文件写入速度。

```
    # Higress Gateway 尝试优化内核网络参数，但宿主机 Linux 内核版本过低（低于 4.11）或者该内核特性未开启
      securityContext:
        # Safe since 1.22: https://github.com/kubernetes/kubernetes/pull/103326
        sysctls:
        - name: net.ipv4.ip_unprivileged_port_start
          value: "0"
```

************************

# 系统资源管理

- 查看系统PCI设备：`lspci`
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

查看CPU信息：`more /proc/cpuinfo`
- 查看物理CPU数：`cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l`
- 查看每个物理CPU中的内核的个数：`cat /proc/cpuinfo | grep "cpu cores"`
- 查看系统所有逻辑CPU个数：`cat /proc/cpuinfo | grep "processor" | wc -l`


Usage 和 Load 的区别， 使用率针对于Cpu 时间，负载针对于等待和进行中的线程
- 使用uptime、top或者 `cat /proc/loadavg`都可以看到CPU的load 1 5 15 分钟的负载。
    - LOAD AVERAGE：一段时间内处于可运行状态和不可中断状态的进程平均数量,它是从另外一个角度体现CPU的使用状态。
        - 可运行分为正在`运行进程`和`正在等待CPU`的进程，**状态为R**
        - 不可中断则是它正在做某些工作不能被中断比如等待磁盘IO等，**其状态为D**
    > 注意: 一个逻辑核且负载为1时表示有线程一直在等待或运行（满载），四个逻辑核且负载为4时表示四个核心都一直有线程在等待或运行（满载）
- lscpu 展示CPU信息

- taskset 将任务绑定在指定cpu核心上
  - `taskset -c 0,1,2,3,4 command`

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
通过glibc内置的 memusage 查看进程运行过程 malloc free 调用次数和资源情况  

### overcommit 
> [参考: Linux Overcommit Modes](https://www.baeldung.com/linux/overcommit-modes)  

Linux下允许程序申请比系统可用内存更多的内存，这个特性叫Overcommit。  
这样做是出于优化系统考虑，因为不是所有的程序申请了内存就立刻使用的，当你使用的时候说不定系统已经回收了一些资源了。
不幸的是，当你用到这个Overcommit给你的内存的时候，系统还没有空闲内存的资源的话，OOM killer就跳出来了。

- 内核参数： vm.overcommit_memory 
    - 0 允许overcommit但是算法判断是否合理，不合理会拒绝对应进程的内存申请
    - 1 允许overcommit
    - 2 禁止overcommit

- `cat /proc/meminfo | grep commit`
    - CommitLimit 就是overcommit的阈值，申请的内存总数超过CommitLimit的话就算是overcommit。
        - CommitLimit = (Physical RAM * vm.overcommit_ratio / 100) + Swap
    - Committed_AS 表示所有进程已经申请的内存总大小，（注意是已经申请的，不是已经分配的），如果 Committed_AS 超过 CommitLimit 就表示发生了 overcommit
        - 超出越多表示 overcommit 越严重。Committed_AS 的含义换一种说法就是，如果要绝对保证不发生OOM (out of memory) 需要多少物理内存。

### OOM Killer
oom-killer

当操作系统认为内存不足时，会选择分数值较高的进程kill掉（用户进程，非内核进程）
- /proc/pid/oom_score 操作系统所计算值
- /proc/pid/oom_score_adj 可以修改的值，当前值加上oom_score后才是最终值
    - 降低分值 echo -50 > /proc/pid/oom_score_adj
- /proc/pid/oom_adj 对应进程的优先级 

内核参数
- vm.panic_on_oom 

> [深入了解Linux OOM Killer：一次可怕的内核事件-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2309788)  
> [OOM相关参数配置与原因排查_Huawei Cloud EulerOS_华为云](https://support.huaweicloud.com/hce_faq/hce_03_0008.html)  

#### 容器OOM
[Pod资源控制](/Linux/Container/Kubernetes.md#pod资源控制)  

> [Kubernetes 触发 OOMKilled(内存杀手)如何排除故障-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2314583)  
> [Alibaba Cloud Linux出现OOM Killer强制释放进程占用内存的原因及解决方案_Alibaba Cloud Linux(Alinux)-阿里云帮助中心](https://help.aliyun.com/zh/alinux/support/causes-of-and-solutions-to-the-issue-of-oom-killer-being-triggered)  


### 虚拟内存
很重要的设计，隔离了物理内存，降低应用端负担。

- cat /proc/pid/maps 或者 pmap -x pid 命令来查看进程的 用户态虚拟内存空间的实际分布。
  - Address：表示此内存段的起始地址
  - Kbytes：表示此内存段的大小(ps：这是虚拟内存)
  - RSS：表示此内存段实际分配的物理内存，这是由于Linux是延迟分配内存的，进程调用malloc时Linux只是分配了一段虚拟内存块，直到进程实际读写此内存块中部分时，Linux会通过缺页中断真正分配物理内存。
  - Dirty：此内存段中被修改过的内存大小，使用mmap系统调用申请虚拟内存时，可以关联到某个文件，也可不关联，当关联了文件的内存段被访问时，会自动读取此文件的数据到内存中，若此段某一页内存数据后被更改，即为Dirty，而对于非文件映射的匿名内存段(anon)，此列与RSS相等。
  - Mode：内存段是否可读(r)可写(w)可执行(x)
  - Mapping：内存段映射的文件，匿名内存段显示为anon，非匿名内存段显示文件名(加-p可显示全路径)。
- cat /proc/iomem 命令来查看进程的 内核态虚拟内存空间的的实际分布。

> [参考: What does Virtual memory size in top mean?](https://serverfault.com/questions/138427/what-does-virtual-memory-size-in-top-mean)  
> [参考: The Right Way to Monitor Virtual Memory on Linux](https://www.logicmonitor.com/blog/the-right-way-to-monitor-virtual-memory-on-linux/)  

> [4.6 深入理解 Linux 虚拟内存管理 | 小林coding](https://www.xiaolincoding.com/os/3_memory/linux_mem.html)  

************************

### 交换内存
> swapon, swapoff - enable/disable devices and files for paging and swapping

> [交换内存文件](/Linux/Base/LinuxDirectoryStructure.md#设置交换内存文件)

- 修改交换内存开始使用的阈值
    - `sudo sysctl vm.swappiness=15` 临时修改重启注销失效， 查看：`cat /proc/sys/vm/swappiness`
    - 永久修改：`/etc/sysctl.conf ` 文件中设置开始使用交换分区的触发值： `vm.swappiness=10`
    - 表示物理内存剩余`10%` 才会开始使用交换分区
    - `建议，笔记本的硬盘低于 7200 转的不要设置太高的交换分区使用，会大大影响性能，因为交换分区就是在硬盘上，频繁的交换数据`

> 交换内存分析
VIRT = SWAP + RES or equal
SWAP = VIRT - RES

- 查看进程使用交换内存 `grep -i VmSwap /proc/*/status` 
- 进程按交换内存使用大小排序`for file in /proc/*/status ; do awk '/VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; done | sort -k 2 -n -r | less`
- `smem`  Report memory usage with shared memory divided proportionally

> 清空交换内存
- 1.关闭交换分区 `sudo swapoff 交换分区文件`
    - 2.开启交换分区 `sudo swapon 交换分区文件`
- `swapoff -a && swapon -a`
    - 前提是交换分区已在 `/etc/fstab` 中配置

### 缓存 cache buffer
注意： 读 cache 写 buffer， 设计是为了提高读写效率，如果内存不足时可以考虑释放这部分内存，但是也会带来读写缓存失效重新读磁盘的性能问题，需慎重考虑。

> [参考: 如何在 Linux 中清除缓存（Cache）？](https://linux.cn/article-5627-1.html) `注意要切换到root再运行命令`  
> [参考: Linux 内存中的Cache，真的能被回收么？](https://www.cnblogs.com/276815076/p/5478966.html)  

> [silenceshell/hcache: showing top X biggest cache files global](https://github.com/silenceshell/hcache)`按进程查看cache和buff使用量`  

************************

设置值 `sync; echo 1 > /proc/sys/vm/drop_caches`

| 设置值 | 作用 |
|:----|:----|
| 1 | 仅清除 page cache |
| 2 | 表示清除回收 slab 分配器中的对象（包括目录项缓存和 inode 缓存） |
| 3 | 表示清除 page cache 和 slab 分配器中的缓存对象 |

> 注意sync命令是为了将内存中buffer写入磁盘，避免这部分内存被直接释放导致数据不一致

## 内存管理
glibc, musl, jemalloc, System Alloc, mimalloc, tcmalloc, rpmalloc 等等实现

> [Optimizing Rust Binaries: Observation of Musl versus Glibc and Jemalloc versus System Alloc](https://users.rust-lang.org/t/optimizing-rust-binaries-observation-of-musl-versus-glibc-and-jemalloc-versus-system-alloc/8499)  

### glibc ptmalloc2
> [glibc - Wikipedia](https://en.wikipedia.org/wiki/Glibc)  

glibc本身是C的实现，封装了系统调用，大部分Linux发行版的默认内存管理都是glibc中的malloc
[一篇文章彻底讲懂malloc的实现（ptmalloc） - yooooooo - 博客园](https://www.cnblogs.com/linhaostudy/p/18028054)  

查看glibc 版本 ldd --version

#### thread arena
注意 ptmalloc 来源 dlmalloc，不支持多线程，使用全局锁来对一个arena分配， ptmalloc2 改进支持多线程，引入 thread arena。`glibc2.11开始支持` 

> [Malloc per-thread arenas in glibc](https://gotplt.org/posts/malloc-per-thread-arenas-in-glibc.html)  
> [Understanding glibc malloc – sploitF-U-N](https://sploitfun.wordpress.com/2015/02/10/understanding-glibc-malloc/)  
> [深入理解glibc malloc | BruceFan's Blog](http://pwn4.fun/2016/04/11/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3glibc-malloc/)  

> [Tuning glibc Memory Behavior | Heroku Dev Center](https://devcenter.heroku.com/articles/tuning-glibc-memory-behavior)  

glibc 对具有大量并发线程的程序进行了优化，通过避免竞争来提升吞吐量。而竞争规避是通过为每一个核来维护一个内存池实现的。  
这种优化方式的本质是：操作系统会为给定的进程捕获（抢占）内存，每个内存块的大小为 64MB，这样的内存块被叫做 thread arena  
当一个线程需要分配内存时，先找当前核最近使用的内存池分配，如果锁定失败或者不够连续内存用于分配申请的大小，则找池内其他arena，否则新建一个（看起来像JVM垃圾回收领域的碎片问题）。


#### thread arena 数量较多
该设计是为了在高并发的场景申请内存时直接从Arena内存申请，而不需要再通过 mmap sbrk等系统调用，并且为了降低多线程申请时的竞争，会最多创建cpucore*8个Arena，此类可以称为 thread arena ，进程只有一个 main arena 作为兜底空间  

thread arena 的最大数量：32位系统是 2倍CPU，64位是8倍CPU。  即 10核CPU的系统，理论上最大会占用 10 X 8 X 64 Mib  

- 列出内存块 pmap -x $pid | sort -nrk3
  - pmap -x $pid 注意不排序时，看到相邻地址大小之合是65536，Mapping是anon时，怀疑
- 求和 thread arena 的RSS总量 `pmap -x $pid | sort -nrk 3 |  grep -E '[0-9]+' | grep 'anon' | awk '{print $3}' | awk '{sum+=$1}; END {print sum}'`

[MALLOC_ARENA_MAX=1 与 MALLOC_ARENA_MAX=4有什么区别？ | easyice](https://www.easyice.cn/archives/341)`极端情况下设置了MAX也不生效，需设置为1直接关闭thread arena`
高并发场景下，存在很多生命周期比较长的对象，如果这些对象能够及时释放，虽然进程可能会在短时间创建许多 thread arena，但实际上并不占据 RES，所以根本问题还是那些具有长生命周期的对象
当只使用 main arena 的情况下，虽然具有长生命周期的对象不变，但是内存池中的空间被重用的几率比多个 thread arena 更高，进程占据的的 RES 要相对少一些

注意： 这里只是为了降低虚拟内存申请的块，实际物理内存高导致pod被kill， 不是glibc的问题，根本问题不在glibc
[Java in K8s: how we’ve reduced memory usage without changing any code | by Mickael Jeanroy | malt-engineering](https://blog.malt.engineering/java-in-k8s-how-weve-reduced-memory-usage-without-changing-any-code-cbef5d740ad)`如何理解` 

优化方案：
1. 将 glibc 替换为对碎片整理更友好的 jemalloc 或者tcmalloc `java -Djava.library.path=/path/to/jemalloc -jar YourApplication.jar`
2. 限制 glibc 的内存池 `export MALLOC_ARENA_MAX=4` 一般建议不要超过 CPU 核心数的 4 倍， **glib2.12以下可能该变量无效**
    - 注意这个参数是限制的总量，假如设定为4，那最终arena数量是4个thread arena+1个main arena
    - grep MALLOC_ARENA_MAX /proc/$pid/environ 确认进程生效了这个环境变量
    - thread arena 的内存需要等待 arena内的所有内存释放才会返还系统，本质上是系统内有长生命周期的对象存在而导致
      - 奇怪点： Java对象的内存都在堆里，为何会放在thread arena

> [当Java虚拟机遇上Linux Arena内存池_禁用per thread arenas-CSDN博客](https://blog.csdn.net/zsd_31/article/details/82183953)  
> [Arena "leak" in glibc](https://codearcana.com/posts/2016/07/11/arena-leak-in-glibc.html)  
 

### jemalloc
> [jemalloc/jemalloc](https://github.com/jemalloc/jemalloc)`Facebook`   

> [为什么说jemalloc比系统带的malloc快，怎么写个简单的测试程序来证明？ - 知乎](https://www.zhihu.com/question/54823155)  
> [Change skip list P value to 1/e, which improves search times by sean-public · Pull Request #3889 · redis/redis](https://github.com/redis/redis/pull/3889)  


```sh
    # Java 应用替换 jemalloc
    export LD_PRELOAD=/usr/lib/libjemalloc.so
    export MALLOC_CONF="background_thread:true,metadata_thp:auto,dirty_decay_ms:30000,muzzy_decay_ms:30000"
    java -jar xxx.jar
```

### tcmalloc
> [google/tcmalloc](https://github.com/google/tcmalloc)`Google`  

### musl malloc
Alpine发行版所使用

[从一次 CTF 出题谈 musl libc 堆漏洞利用本文通过一道 CTF 题目展示 musl libc 堆溢出漏洞的利 - 掘金](https://juejin.cn/post/6844903574154002445)  

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
- 其次是绑定发行版的包，常分为两类 Debian系的deb包 对应apt管理，REHL系的rpm包 对应yum dnf管理
- 然后就是最近推行的 snap flatpak AppImage 等通用包格式，大致逻辑都是将软件包所有动态依赖项打包进去避免运行时对外部的依赖
    - 类似静态编译以支持跨发行版，当然缺点就是包的大小，但是相比于软件包的通用性，存储也是小问题了。

### AppImage 
> [AppImage | 让 Linux 应用随处运行](https://appimage.org/)  
> [AppImage中文文档](https://doc.appimage.cn/docs/home/)  

简单来说类似于Windows平台的Exe，一个文件就是一个应用程序，通过静态链接和低版本系统打包来解决各发行版的兼容问题。

> [Packaging Guide — AppImage documentation](https://docs.appimage.org/packaging-guide/index.html)  

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
