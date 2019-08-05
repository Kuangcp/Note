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
    1. [终端模拟器对比](#终端模拟器对比)
    1. [效率工具](#效率工具)
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
        1. [剪贴板管理](#剪贴板管理)
        1. [资源管理](#资源管理)
1. [Tips](#tips)

**目录 end**|_2019-08-05 19:27_|
****************************************
# 高效的Linux
> [Linux Desktop Setup](https://hookrace.net/blog/linux-desktop-setup/)`一整套工具`

> [命令行：增强版 ](https://linux.cn/article-10171-1.html)  
> [工具](https://www.lulinux.com/archives/2787)  

## 终端模拟器对比
> 列举出系统可安装终端 `sudo apt search terminal | grep -E terminal.+amd64`

- `qterminal` 可定制标签页位置以及透明度，很简洁,挺好用,但是不能内容和窗体大小自适配, 0.7.1已没有这个bug, 还是很好用的模拟器, 但是多标签的时候, 会有内存泄露
- `mate-terminal` 和gnome-terminal 基本配置什么的几乎一样，只是标题栏简洁一丢丢，如果使用选择即复制,那么在跨标签页复制粘贴有bug
- `gnome-terminal` 很简洁，但是多标签时，标签栏太大,标签页底部有白边
- `sakura` 外观上和前两个几乎一样，标签页可以更简洁，但是设置不好调, 而且不能自定义快捷键
- `deepin-terminal` 功能很多，主题很多，功能最为强大，但是字体可以选的很少
- `terminator` 可以定制背景图片，但是在我这deppin系统里有bug，多标签是假的，命令全是在共享的，不能用。。
- `tilda` 内嵌于桌面上, 小命令方便, 需要查看文件就不方便了
- `terminology` 看起来很炫酷, 仅此而已

> [更多可安装终端](https://gitee.com/kcp1104/codes/gca14wtqvm67l9j5r0deb56#Terminals.md)
> 终极工具 `tmux` 运维必备软件 远离终端模拟器的对比和选择, 一个就够了

## 效率工具
> 提高工作和开发效率

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

************
## 文本处理
`wc`
> 单词 行数 统计

## 文件操作
`iconv`
> 可以将一种已知的字符集文件转换成另一种已知的字符集文件

`zssh`
> 便捷的文件传输

- [参考博客](http://blog.csdn.net/ygm_linux/article/details/32321729)

***********
## 分享
### asciinema
- [asciinema](https://asciinema.org) `终端屏幕录制和分享网`

- 执行 `asciinema`或`asciinema rec` 即可开始录制
- 要注册就运行 `asciinema auth` 进入输出的网址，填邮箱和名字即可（每次登录都要这样。或者使用邮件来确认，麻烦ing）

## 图形化工具
### 剪贴板管理
> [参考博客: 面向 Linux 的 10 款最佳剪贴板管理器](https://linux.cn/article-7329-1.html)

- CopyQ 比较好用

> [参考博客: 这9个Linux命令非常危险 请大家慎用](https://www.jb51.net/LINUXjishu/498660.html)

> [参考博客: 关于 Linux 你可能不是非常了解的七件事](https://linux.cn/article-8934-1.html)

### 资源管理
> gnome-system-monitor

************************

# Tips

> `sudo echo "Text I want to write" > /path/to/file` not work
> [参考博客: "sudo echo" does not work together in Ubuntu ](https://blogs.oracle.com/joshis/sudo-echo-does-not-work-together-in-ubuntu-another-waste-of-time-issue)
> [stack over flow](https://stackoverflow.com/questions/84882/sudo-echo-something-etc-privilegedfile-doesnt-work-is-there-an-alterna)

- `sudo sh -c 'echo "Text I want to write" >> /path/to/file'`
- `echo "Text I want to write" | sudo tee -a /path/to/file > /dev/null`

************************

