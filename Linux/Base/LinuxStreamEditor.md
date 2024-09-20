---
title: Linux流编辑器
date: 2018-12-15 11:17:35
tags: 
    - 工具
categories: 
    - Linux
---

💠

- 1. [流编辑器](#流编辑器)
    - 1.1. [tr](#tr)
    - 1.2. [colrm](#colrm)
    - 1.3. [cut](#cut)
    - 1.4. [paste](#paste)
    - 1.5. [sed](#sed)
    - 1.6. [awk](#awk)

💠 2024-09-20 11:10:09
****************************************
# 流编辑器
> [参考: 比较linux下各种流编辑器的用法](https://blog.csdn.net/havedream_one/article/details/45007449)

## tr
> 转换字符
- 替换：可以使用字符集的形式如tr `[a-z]` `[A-Z]` 或者 tr a-z A-Z
- 压缩：-s 如 `echo “you are        a    man   ” | tr -s ' ' ' '`
    - 结果 `you are a man`
- 删除：-d 如 `echo "you     are    a man"|  tr -d ' ' `
    - 结果 `youareaman`
- 合并多行 `ps aux | grep firefox | grep -v PID | awk '{print $2}'  | tr '\n' ','`

## colrm

## cut
> man cut

md5sum | cut -c 1-8

## paste
> 粘贴，合并文件用

使用制表符来合并多个文件对应的行，也可以使用 -d 指定合并符

实例： 默认制表符  paste p3.txt p2.txt p1.txt

指定 paste -d ‘*‘ p3.txt p2.txt p1.txt

## sed
> 使用方式: `操作类型 命令 文件` | sed --help 查看详细

`操作类型`
- `-n` suppress automatic printing of pattern space
- `-e` 只在控制台输出的操作的结果内容(全部)，源文件不变 **缺省选项**
- `-i` 直接在源文件中进行修改
- `-f file` 执行一个 sed 脚本文件中的指令

`命令`

| 命令 | 效果 |
|:----:|:----|
| b | label 将执行的指令跳至由 : 建立的参考位置 
| d | 删除行  删除2-4行 `sed -i "2,4d" file` 
| D | 删除 pattern space 内第一个 newline 字母 前的资料 
| g | 拷贝资料从 hold space 
| G | 添加资料从 hold space 至 pattern space 
| h | 拷贝资料从 pattern space 至 hold space 
| H | 添加资料从 pattern space 至 hold space 
| l | 印出 l 资料中的 nonprinting character 用 ASCII 码 
| a | 新增 在下一
| i | 插入添加使用者输入的行  将hello插入到第4行：`sed -in "4i hello" test.md` 
| n | 读入下一笔资料 
| N | 添加下一笔资料到 pattern space 
| p | 打印 `sed -n 1p file` 
| P | 印出 pattern space 内第一个 newline 字母 前的资料 
| q | 跳出 sed 编辑 
| r | 读入它档内容 
| w | 写资料到它档内 
| x | 交换 hold space 与 pattern space 内容 
| y | 转换（transform）字元 

- c 替换 整行
- s 替换 行内字符串的替换  命令结构: `'s/pattern/relacement/flags'`
    - 当替换内容含 / 时需要转义，或者更换分隔符为@ 即 `s@ab@12/g`
    - pattern 是正则的 pattern 写法 
        - **注意会匹配到首尾的空字符** `echo abc | sed 's/a*/l/g'` 会输出lblcl
        - 分组匹配 `sed 's/\([0-9]\)\s/\1,/g' `
        - 边界符 `\b` 代表空格字符
        - 正则匹配 `sed 's/\b[0-9]\{2\}\b/number/g` 注意 {}\的转义 , 不支持\d \A \Z 等。

    - replacement 是需要替换成的内容
        - 此处可以使用&表示匹配到的内容，例如对a字符后追加b字符 `sed 's/a/&b/g'`
    - flags 是动作(可以为空)
        - 数值: 一行中的第几处符合 pattern 将被替换
        - g : 全部替换 ； `3g` 第三处到最后
        - p : 输出修改的行内容
        - w filename : 替换后的文件写入到新文件
        - I : 忽略大小写； 例如 `gI`

- 多指令执行
    - `sed 's/a//g;s/b//g'`
    - `sed -e '' -e ''`

>1. 截取指定行数到新文件 `sed -n ‘开始行数，结束行数p’ info.log > newFile.log`
>1. 文件内容倒置 `sed -i '1!G;h;$!d' filename`
>1. 新增内容到第一行 `sed -i '1 i\any text' file`

>1. 修改配置文件中name的值为123 `sed -i "s/name=.*/name=123/g" config.conf`
>1. 修改第3行 `sed -i '3 s/name/1/g'`

>1. 匹配行的行尾追加 `sed -i 's/end.*/& ;/g' file`
>1. 匹配行后第三行行尾追加`sed -i '/gradle/{n;n;n; s/.*/& 6.0/;}' file`
>1. CRLF -> LF `sed -i 's/\r//g' file`  
    > 配合 git 使用: `git ls-files| xargs sed -i 's/\r//g'`
>1. 注意特殊字符的转义 `git ls-files | xargs  sed -i 's/@a.*/\//g'`
>1. 去除换行符 `sed -i ':label;N;s/\n/ /;b label'` [参考](http://www.cnblogs.com/lykm02/p/4479098.html)
>1. 处理管道流 `echo syx is a good body | sed 's/syx/zsf/'`  

- [Linux Sed 教程：有趣的 Sed 替换示例](https://bbs.huaweicloud.com/blogs/325484)
- [参考: linux sed 命令单行任务快速参考](http://www.techug.com/post/linux-sed1line.html)
- [sed 正则的精确控制](http://wiki.jikexueyuan.com/project/shell-learning/sed-accurate-control-of-regular.html)
    - `echo Tolstoy is worldly | sed 's/T.*y/Camus/'` 这里的 pattern 就有问题， 会把整行替换掉
    - `echo Tolstoy is worldly | sed 's/T[a-z]*y/Camus/'` 只把第一个单词替换

************************
> [sokoban sed](https://github.com/aureliojargas/sokoban.sed) `sed 写的推箱子游戏`

************************

## awk

> awk有多个不同版本: awk、mawk nawk和gawk，若未作特别说明，通常指gawk (gawk 是 AWK 的 GNU 版本)

1. 输出指定列 `cat log.log | awk '{print $2}'`
    1. 忽略第一列:`awk '{$1="";print $0}'` 
    1. 忽略1到4: `awk '{ for(i=1; i<=4; i++){ $i="" }; print $0 }'`
1. 按列求和 `awk '{sum += $1};END {print sum}'`
1. 添加行号  `awk '{printf("%2d %s\n", NR, $0);`
1. 读取标准输出 `awk '{print $0}' - `

> [参考: awk 入门教程](http://www.ruanyifeng.com/blog/2018/11/awk.html)

- 别名中双引号转义问题处理： `awk '\''{}'\'`
    - `alias count.csv='sort | uniq -c | sort -hr | awk '\''{print $1","$2}'\'` 