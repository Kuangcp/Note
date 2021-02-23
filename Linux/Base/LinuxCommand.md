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
    1. [系统内置命令](#系统内置命令)
        1. [Shell内建命令](#shell内建命令)
    1. [输入输出](#输入输出)
        1. [重定向](#重定向)
    1. [管道](#管道)
        1. [xargs](#xargs)
    1. [time](#time)
    1. [date](#date)
    1. [grep](#grep)
    1. [script](#script)
    1. [定时任务](#定时任务)
        1. [crontab](#crontab)
        1. [Systemd](#systemd)

**目录 end**|_2021-02-23 20:53_|
****************************************
# 系统常用基础命令
> [Linux 命令大全](http://man.linuxde.net/)

> [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) `高效优美的工具`

## 系统内置命令
> /bin/* 系统自带命令

- false 以失败码退出程序
- `stty -a` 查看快捷键映射

- 终端内执行循环
    - `for i in $(seq 1 10); do echo $i; done` 语法和Shell差不多, 但是需要在循环体的每一句加上`;`

### Shell内建命令
- whence 查看命令的真实面貌 (zsh中的内建命令)
- where 查找命令的位置 (Zsh中内建命令)
- which 寻找命令的位置
- type 展示命令的描述

************************

## 输入输出

### 重定向
- 输出重定向  `> a.log 2>&1` 表示为将2也输出到标准输出 **为了方便记忆也可以将 &1 理解为C语言中的取地址符:2重定向到1的地址**
    - 2 是错误输出 1 是标准输出

******************

## 管道
> [参考: linux 管道 ](http://www.cnblogs.com/davidwang456/p/3839874.html)
> [参考: linux shell 管道命令(pipe)使用及与shell重定向区别](http://www.cnblogs.com/chengmo/archive/2010/10/21/1856577.html)

- 接收输入流且输出流 类似于 Java8 中的 peek() 函数
    - `cat README.md | grep Java | tee > java.log | grep -v Maven`

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
- 设置日期或时间 `date -s '2020-12-01'` 或 `date -s '23:00:20'`

## grep
> g (globally) search for a re (regular expression ) and p (print ) the results.

> egrep [相关网页](http://man.linuxde.net/grep) 与 grep -E 等价

- 正则 `grep -E "[1-9]+"` 注意 `[]` 是里面单个字符 `()`是里面所有字符一起 用于匹配

- -o 一行内多次匹配 
    - 统计所有 `main` 数量 `grep -o main test.log | wc -l` 
- -i 忽略大小写

- 匹配中文
    1. `-P '[\p{Han}]'`

## script
>  make typescript of terminal session

录制终端

************************

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

- * 表示所有值； 
- ? 表示未说明的值，即不关心它为何值； 
- - 表示一个指定的范围； 
- , 表示附加一个可能值； 
- / 符号前表示开始时间，符号后表示每次递增的值； 

> 注意  
>> 如果command是shell脚本，注意执行环境和权限问题

### Systemd
> [参考: Systemd 定时器教程](http://www.ruanyifeng.com/blog/2018/03/systemd-timer.html) `配置和使用上比Crontab更繁杂, 但是有更多的可控制项`
