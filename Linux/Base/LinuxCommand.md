---
title: Linux基础命令
date: 2018-12-15 11:11:55
tags: 
    - 工具
categories: 
    - Linux
---

💠

- 1. [Linux 基础命令](#linux-基础命令)
    - 1.1. [系统内置命令](#系统内置命令)
        - 1.1.1. [Shell内建命令](#shell内建命令)
    - 1.2. [输入输出](#输入输出)
        - 1.2.1. [重定向](#重定向)
    - 1.3. [管道](#管道)
        - 1.3.1. [xargs](#xargs)
    - 1.4. [time](#time)
    - 1.5. [date](#date)
    - 1.6. [grep](#grep)
    - 1.7. [script](#script)
    - 1.8. [定时任务](#定时任务)
        - 1.8.1. [crontab](#crontab)
        - 1.8.2. [Systemd](#systemd)

💠 2026-07-14 12:48:21
****************************************
# Linux 基础命令
> [Linux 命令大全](http://man.linuxde.net/)

> [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) `高效优美的工具`

## 系统内置命令
> /bin/* 系统自带命令

- false 以失败码退出程序
- `stty -a` 查看快捷键映射
- for `for i in $(seq 1 10); do echo $i; done` 语法和Shell差不多, 但是需要在循环体内的每一句命令都加上`;`
- sort 
    - -k2 按指定的第二列进行排序
    - -n 字符串数值排序，例如 Mib大于Kib
    - -r 逆序

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
- 定义替换符 `xargs -I {} echo {}`
    - `xargs -I XX sh -c 'echo XX;touch XX'`
- `-r` --no-run-if-empty 如果接受到参数为空就不执行嵌套的命令

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
- 日期计算 `date -d "+10 days"`

## grep
> `g` (globally) search for a `re` (regular expression ) and `p` (print ) the results.

> egrep [相关网页](http://man.linuxde.net/grep) 与 grep -E 等价

- [正则表达式](/Skills/RegularExpression.md)
    - 标准正则  `grep -E "[1-9]+"` 注意 `[]` 是里面单个字符 `()`是里面所有字符一起 用于匹配
    - Perl正则 `grep -P ''`

- -o 只输出匹配值 `一行内多个匹配时多行输出`  
    - 统计所有main字符数量 `grep -o main test.log | wc -l` 
- -i 忽略大小写

> eg：
- 匹配中文 `-P '[\p{Han}]'`
- 截取字符 `ping jd.com | grep -oP '(?<=time=).*(?=ms)'` 提取出ms值。
- 两个文件的差异行 `grep -vwf 文件1 文件2`

************************

## script
>  make typescript of terminal session

录制终端

************************

## 定时任务
### crontab
`minute hour day-of-month month-of-year day-of-week commands  `

> [为什么crontab不执行](https://segmentfault.com/a/1190000020850932)  
- cron 脚本中的操作命令 都使用绝对路径, 必须注意环境变量问题
- 每行配置都需要以换行符结尾
- crontab -e 注册用户 有权限执行相应命令
- 环境变量差别，通过env命令进行确认
- crond 未服务正常运行

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

- 编辑配置文件 `crontab -e` 
    - 注意每个当前用户都是独立的crontab计划，所以设置定时命令需注意执行用户权限问题
- 时间配置格式
    - * 表示所有值； 
    - ? 表示未说明的值，即不关心它为何值； 
    - - 表示一个指定的范围； 
    - , 表示附加一个可能值； 
    - / 符号前表示开始时间，符号后表示每次递增的值； 
- 例如：
    - 每分钟执行二进制命令
    - 每分钟执行脚本 

- 执行日志： `/var/log/cron`

### Systemd
> [参考: Systemd 定时器教程](http://www.ruanyifeng.com/blog/2018/03/systemd-timer.html) `配置和使用上比Crontab更繁杂, 但是有更多的可控制项`
