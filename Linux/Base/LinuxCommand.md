---
title: Linux常用命令
date: 2018-12-15 11:11:55
tags: 
    - 工具
categories: 
    - Linux
---

**目录 start**
 
1. [系统常用基础命令](#系统常用基础命令)
    1. [输入输出](#输入输出)
        1. [重定向](#重定向)
    1. [管道](#管道)
        1. [xargs](#xargs)
    1. [time](#time)
    1. [date](#date)
    1. [grep](#grep)
    1. [定时任务](#定时任务)
        1. [crontab](#crontab)
        1. [Systemd](#systemd)
1. [实用的工具](#实用的工具)
    1. [终端模拟器对比](#终端模拟器对比)
    1. [效率工具](#效率工具)
        1. [目录跳转](#目录跳转)
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
    1. [系统内置命令](#系统内置命令)
        1. [Shell内建命令](#shell内建命令)
1. [Tips](#tips)

**目录 end**|_2019-04-05 15:25_| [Gitee](https://gitee.com/gin9/Memo) | [Github](https://github.com/Kuangcp/Memo)
****************************************
# 系统常用基础命令
> [Linux 命令大全](http://man.linuxde.net/)

## 输入输出

### 重定向
- 输出重定向  `> a.log 2>&1` 表示为将2也输出到标准输出 **为了方便记忆也可以将&理解为C中的取地址符:2重定向到1的地址**
    - 2是错误输出
    - 1是标准输出

******************
## 管道
> [参考博客: linux 管道 ](http://www.cnblogs.com/davidwang456/p/3839874.html)
> [参考博客: linux shell 管道命令(pipe)使用及与shell重定向区别](http://www.cnblogs.com/chengmo/archive/2010/10/21/1856577.html)
- [ ] 学习管道的使用

### xargs
> 常在管道中使用 能将输入流转为 命令 的参数

- 输出所有的md文件的内容 `find . -name "*.md" | xargs cat | less`

***************************
## time
> 可以用于统计命令运行消耗的时间

- bash内置简易time `time` 和 /usr/bin/time `\time`
    - `\time -v ls -al`

## date
> 获取日期和时间 `date +%Y_%m_%d_%H:%M:%S` 或者 `date +%F %T`

- 获取前一天日期 `date --date='1 day ago' -R`
- 将秒时间戳转换为日期 `date --date='@1524738626'`

## grep
> g (globally) search for a re (regular expression ) and p (print ) the results.

> egrep [相关网页](http://man.linuxde.net/grep) 与 grep -E 等价

- 正则 `grep -E "[1-9]+"` 注意 `[]` 是里面单个字符 `()`是里面所有字符一起 用于匹配

- -o 一行内多次匹配 
    - 统计所有 `main` 数量 `grep -o main test.log | wc -l` 
- -i 忽略大小写

## 定时任务
### crontab
> [参考博客 shell定时任务crontab](http://www.cnblogs.com/taosim/articles/2007056.html)
`minute hour day-of-month month-of-year day-of-week commands  `

> cron 脚本中的操作命令 最好都使用绝对路径, 必须注意环境变量问题

```sh
    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # Example of job definition:
    # .---------------- minute (0 - 59)
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    # |  |  |  |  |
    # *  *  *  *  * user-name command to be executed
```

### Systemd
> [参考博客: Systemd 定时器教程](http://www.ruanyifeng.com/blog/2018/03/systemd-timer.html) `配置和使用上比Crontab更繁杂, 但是有更多的可控制项`

*******************************************

# 实用的工具
> [命令行：增强版 ](https://linux.cn/article-10171-1.html)

## 终端模拟器对比
> 列举出系统可安装终端 `sudo apt search terminal | grep -E terminal.+amd64`

- `qterminal` 可定制标签页位置以及透明度，很简洁,挺好用,但是不能内容和窗体大小自适配, 0.7.1已没有这个bug, 还是很好用的模拟器, 但是多标签的时候, 会有内存泄露
- `mate-terminal` 和gnome-terminal 基本配置什么的几乎一样，只是标题栏简洁一丢丢，如果使用选择即复制,那么在跨标签页复制粘贴有bug
- `gnome-terminal` 很简洁，但是多标签时，标签栏太大,标签页底部有白边
- `sakura` 外观上和前两个几乎一样，标签页可以更简洁，但是设置不好调, 而且不能自定义快捷键
- `deepin-terminal` 功能很多，主题很多，功能最为强大，但是字体可以选的很少
- `terminator` 可以定制背景图片，但是在我这deppin系统里有bug，多标签是假的，命令全是在共享的，不能用。。
- `tmux` 运维必备软件，入门有些繁琐
- `tilda` 内嵌于桌面上, 小命令方便, 需要查看文件就不方便了

> [更多可安装终端](https://gitee.com/kcp1104/codes/gca14wtqvm67l9j5r0deb56#Terminals.md)

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

与 Autojump 类似, 性能更好

## 其他工具
> 最终都会安装到 /usr/bin/*  目录下

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

************************
## 系统内置命令
> /bin/* 系统自带命令

- which 命令的位置

- false 以失败码退出程序
- `stty -a` 查看键映射

- 终端内执行循环
    - `for i in $(seq 1 10); do echo $i; done` 语法和Shell差不多, 但是需要在循环体的每一句加上`;`

### Shell内建命令
- whence 查看命令的真实面貌 (zsh中的内建命令)
- where 查找命令的位置 (Zsh中内建命令)

# Tips

> `sudo echo "Text I want to write" > /path/to/file` not work
> [参考博客: "sudo echo" does not work together in Ubuntu ](https://blogs.oracle.com/joshis/sudo-echo-does-not-work-together-in-ubuntu-another-waste-of-time-issue)
> [stack over flow](https://stackoverflow.com/questions/84882/sudo-echo-something-etc-privilegedfile-doesnt-work-is-there-an-alterna)

- `sudo sh -c 'echo "Text I want to write" >> /path/to/file'`
- `echo "Text I want to write" | sudo tee -a /path/to/file > /dev/null`
