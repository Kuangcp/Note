---
title: 高效的Linux
date: 2019-04-18 22:04:15
tags: 
    - Effective
categories: 
    - Linux
---

**目录 start**

1. [高效的Linux](#高效的linux)
    1. [Terminal 对比](#terminal-对比)
    1. [效率工具](#效率工具)
        1. [协作工具](#协作工具)
        1. [目录跳转](#目录跳转)
    1. [网络工具](#网络工具)
    1. [其他工具](#其他工具)
    1. [检测工具](#检测工具)
        1. [硬盘](#硬盘)
            1. [smartmontools](#smartmontools)
    1. [文本处理](#文本处理)
    1. [文件操作](#文件操作)
    1. [分享](#分享)
        1. [asciinema](#asciinema)
    1. [图形化工具](#图形化工具)
        1. [图片管理](#图片管理)
        1. [剪贴板管理](#剪贴板管理)
        1. [截图](#截图)
        1. [资源管理](#资源管理)
1. [Tips](#tips)

**目录 end**|_2020-05-16 21:26_|
****************************************
# 高效的Linux
> [Linux Desktop Setup](https://hookrace.net/blog/linux-desktop-setup/)`一整套工具`

> [命令行：增强版 ](https://linux.cn/article-10171-1.html)  
> [工具](https://www.lulinux.com/archives/2787)  

## Terminal 对比
> 列举出系统可安装终端  
>1. Debian: `sudo apt search terminal | grep -E terminal.+amd64`
>1. Arch: `yay terminal`

终端可参考功能点： 终端透明化，终端背景图，快捷键设置，终端内颜色自定义，下拉式，标签水平垂直拆分，鼠标键盘交互性，资源占用少  
终极工具 [Tmux](/Linux/Tool/Tmux.md)  远离终端模拟器的对比和选择 

| 终端 | 优点 | 缺点 | 备注 |
|:---|:---|:---|:---|
|`xiki`           | 鼠标和键盘高度交互 <br> 交互性和复杂度比较高 | | |
|`qterminal`      | 设置设计清晰，功能完备 | 终端内容显示兼容性略有问题 资源消耗中等 | 
|`xfce4-terminal`  | | | |
|`gnome-terminal` | 简洁 资源消耗少 | 缺 多标签时，标签栏太大,标签页底部有白边 无法透明化 |  鼠标中键无法复制时需安装 `parcellite`|
|`mate-terminal`  | 标签栏更简洁，其余和 `gnome-terminal` 一致|||
|`sakura`         | 外观上和前两个几乎一样，标签页可以更简洁 | 配置复杂 繁琐 | |
|`deepin-terminal`| 功能很多，主题很多，功能最为强大 | 字体仅可选择内置不可自定义
|`tilda`          | 内嵌于桌面上, 小命令方便 | 需要查看文件时不方便
|`terminology`    | 样式高度自定义

> 备注
- sakura xfce4-terminal 快捷键配置
    - `~/.config/xfce4/terminal/accels.scm` 
    - [doc](http://troubleshooters.com/linux/sakura.htm) | [config shortcut](https://unix.stackexchange.com/questions/102474/configuring-shortcuts-for-sakura)  

************************

## 效率工具
> 提高工作和开发效率

> `通知提醒` 
[Desktop notifications](https://wiki.archlinux.org/index.php/Desktop_notifications) | [xfce notify-send ](https://docs.xfce.org/apps/notifyd/preferences) 
[Desktop Notifications Specification](https://developer.gnome.org/notification-spec/#protocol)  
[Notification Development Guidelines](https://wiki.ubuntu.com/NotificationDevelopmentGuidelines)

> [Github notify-send.sh](https://github.com/vlevit/notify-send.sh)

### 协作工具
**synergy**
> 多系统间共享键鼠

### 目录跳转
**`Autojump`**
> 统计cd 目录，方便目录跳转  *shrc 中要有 : `. /usr/share/autojump/autojump.sh`  

- `apt install autojump` 设置为自动运行 `echo '. /usr/share/autojump/autojump.sh' >> ~/.bashrc`
    - `j -v` 查看安装版本
    - `j --stat` 查看统计信息
    - `j --help`
    - `jo code` 打开code文件夹
    - `jco c` 打开子目录
- `ls -l ~/.local/share/autojump/` 统计信息的目录，清除就相当于卸载重装了

**`z.lua`**
> [Github](https://github.com/skywind3000/z.lua)   与 Autojump 类似, 性能更好

- `pip install qrcode` 
    - *qr --help* 终端内生成二维码

## 网络工具

************************

## 其他工具
> 最终都会安装到 /usr/bin/*  目录下

- sudo 是需要安装的
    1. `alias sudo='sudo'` 能够在别名上使用 sudo *神奇*

- md5sum 报文摘要算法 Message-Digest Algorithm 5 的实现 
    - `md5sum file` 计算出md5值
    - `md5sum -c file.md5` file 和 file.md5 在同一目录下, 执行这个命令就是检查md5是否匹配, 确保文件的完整性和正确性

- last _查看Linux登录信息_
    - last -n 5 最近五次登录

- w | uptime _查看启动情况_

- colrm
    - ps | clorm 20 30 `colrm` _删除输出的20 到30 列_

- xsel 
    - `cat a.md | xsel -b` _将文件所有内容复制到剪贴板_ 但是处理大文件时会失效 xclip 更有效

- htop _终端里的任务管理器_
- strace -p PID _查看系统调用_
- cmatrix _装13,字符雨_
- logkeys 记录键盘输入 [Github](https://github.com/kernc/logkeys)
- expect [用于自动输入密码](http://www.cnblogs.com/iloveyoucc/archive/2012/05/11/2496433.html)

- [WTF](https://wtfutil.com/posts/overview/) | [Github Repo](https://github.com/senorprogrammer/wtf)
    - 丰富的功能, 一个方便的终端控制面板

- ag `快速当前目录下, 全文内容搜索, 快到可怕` ubuntu:silversearcher-ag  alpine:the_silver_searcher
    - [The Silver Searcher](https://github.com/ggreer/the_silver_searcher)

- when-changed 监控文件变化 执行命令 pip install when-changed

- dircolors [Linux dircolors命令](http://www.runoob.com/linux/linux-comm-dircolors.html)`用于设置 ls 命令输出时的色彩`

- gtypist 用于练习打字

`xclip`
> 便捷的文本复制
- `cat README.md | xclip -sel clip` 将文件复制到剪贴板

`uniq`
> report or omit repeated lines

统计出现次数 `cat log.log | grep WARN | awk '{print $5}' | sort | uniq -c`

`notes`
> 管理笔记
> [Github](https://github.com/pimterry/notes)

`todo.txt-cli`
> 终端内的 todo 
> [Github](https://github.com/todotxt/todo.txt-cli)

`starDict`
> 终端内字典

***********

## 检测工具
### 硬盘
#### smartmontools

- 检测健康状况 `smartctl -Hc /dev/sda9`


************************

## 文本处理
`wc`
> 单词 行数 统计


************************

## 文件操作
`iconv`
> 可以将一种已知的字符集文件转换成另一种已知的字符集文件

`zssh`
> 便捷的文件传输

- [参考博客](http://blog.csdn.net/ygm_linux/article/details/32321729)

`pdfunite`
> Portable Document Format (PDF) page merger

- pdfunite 1.pdf 2.pdf merged.pdf

************************

## 分享
### asciinema
- [asciinema](https://asciinema.org) `终端屏幕录制和分享网`

- 执行 `asciinema`或`asciinema rec` 即可开始录制
- 要注册就运行 `asciinema auth` 进入输出的网址，填邮箱和名字即可（每次登录都要这样。或者使用邮件来确认，麻烦ing）

************************

## 图形化工具
### 图片管理
1. gthumb
1. Viewnior
1. webp
1. ImageMagick

### 剪贴板管理
> [参考: 面向 Linux 的 10 款最佳剪贴板管理器](https://linux.cn/article-7329-1.html)

- CopyQ 比较好用

> [参考: 这9个Linux命令非常危险 请大家慎用](https://www.jb51.net/LINUXjishu/498660.html)

> [参考: 关于 Linux 你可能不是非常了解的七件事](https://linux.cn/article-8934-1.html)

### 截图
- Flameshot 截图工具  类似于 snipaste
    - Ctrl 鼠标滚动 调整线条粗细
- deepin-screenshot

### 资源管理
> gnome-system-monitor

************************

# Tips

> `sudo echo "Text I want to write" > /path/to/file` not work  

> [参考: "sudo echo" does not work together in Ubuntu ](https://blogs.oracle.com/joshis/sudo-echo-does-not-work-together-in-ubuntu-another-waste-of-time-issue)
> [stack over flow](https://stackoverflow.com/questions/84882/sudo-echo-something-etc-privilegedfile-doesnt-work-is-there-an-alterna)

- `sudo sh -c 'echo "Text I want to write" >> /path/to/file'`
- `echo "Text I want to write" | sudo tee -a /path/to/file > /dev/null`

************************

