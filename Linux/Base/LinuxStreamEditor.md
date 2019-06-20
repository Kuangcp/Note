---
title: Linux流编辑器
date: 2018-12-15 11:17:35
tags: 
    - 工具
categories: 
    - Linux
---

**目录 start**
 
1. [流编辑器](#流编辑器)
    1. [tr](#tr)
    1. [cut](#cut)
    1. [paste](#paste)
    1. [sed](#sed)
    1. [awk](#awk)

**目录 end**|_2019-06-20 21:02_|
****************************************
# 流编辑器
> [参考博客: 比较linux下各种流编辑器的用法](https://blog.csdn.net/havedream_one/article/details/45007449)

## tr
> 转换字符
- 替换：可以使用字符集的形式。如tr [a-z] [A-Z] 或者 tr a-z A-Z
- 压缩：-s   如echo “you are        a    man   ”|tr -s ' ' ' '   结果you are a man
- 删除：-d   如echo "you     are    a man"|  tr -d ' '结果youareaman

## cut
> man cut

## paste
> 粘贴，也就是合并文件用的
使用制表符来合并多个文件对应的行，也可以使用 -d 指定合并符
实例：
默认制表符
paste p3.txt p2.txt p1.txt
指定
paste -d ‘*‘ p3.txt p2.txt p1.txt
so，也不需要和其他的对比了，其他都是拆分，而paste是合并。

## sed
> 组成模式: `参数 命令 文件` | sed --help 查看详细

- [参考：sed 查找与替换](http://wiki.jikexueyuan.com/project/shell-learning/sed-search-and-replace.html)
- [sed 正则的精确控制](http://wiki.jikexueyuan.com/project/shell-learning/sed-accurate-control-of-regular.html)
    - `echo Tolstoy is worldly | sed 's/T.*y/Camus/'` 这里的pattern就有问题， 会把整行替换掉
    - `echo Tolstoy is worldly | sed 's/T[a-z]*y/Camus/'` 只把第一个单词替换

> 处理管道流 `echo syx is a good body | sed 's/syx/zsf/'`

- `参数`
    - `-n` suppress automatic printing of pattern space
    - `-e` 只在控制台输出的操作的结果内容(全部)，源文件不变 
    - `-i` 直接在源文件中进行修改
    - `-f file` 执行一个 sed 脚本文件中的指令

- `命令`
    - p 打印 `sed -n Np 文件名`
    - a 新增 在下一行
    - i 插入 在上一行 将hello插入到第4行：`sed -in "4i hello" test.md`
    - c 替换 整行
    - s 替换 行内字符串的替换 
        - 命令结构为: `'s/pattern/relacement/flags'`
            - pattern 是正则的 pattern 写法 **注意会匹配到首尾的空字符** `echo abc | sed 's/a*/l/g'` 就很费解
            - replacement 是需要替换成的内容
            - flags 是动作(可以为空)
                - 整数: 一行中的第几处符合 pattern 将被替换
                - g : 全部替换
                - p : 输出修改的行内容
                - w filename : 替换后的文件写入到新文件
        - 将文件中所有aaa换为bbb, `sed -e "s/aaa/bbb/g" test.md`
    - d 删除 行级别, 删除2-4行 `sed -i "2,4d" test.md`

| 命令 | 效果 |
|:----:|:----|
| b | label 将执行的指令跳至由 : 建立的参考位置。 |
| D | 删除 pattern space 内第一个 newline 字母 前的资料。 |
| g | 拷贝资料从 hold space。 |
| G | 添加资料从 hold space 至 pattern space |
| h | 拷贝资料从 pattern space 至 hold space |
| H | 添加资料从 pattern space 至 hold space |
| l | 印出 l 资料中的 nonprinting character 用 ASCII 码。 |
| i | 插入添加使用者输入的资料行。 |
| n | 读入下一笔资料。 |
| N | 添加下一笔资料到 pattern space。 |
| p | 印出资料。 |
| P | 印出 pattern space 内第一个 newline 字母 前的资料。 |
| q | 跳出 sed 编辑。 |
| r | 读入它档内容。 |
| w | 写资料到它档内。 |
| x | 交换 hold space 与 pattern space 内容。 |
| y | 转换（transform）字元。 |

>1. 截取指定行数到新文件 `sed -n ‘开始行数，结束行数p’ info.log > newFile.log`
>1. 修改配置文件中name的值为123 `sed -i "s/name=.*/name=123/g" config.conf`
>1. CRLF -> LF `sed -i 's/\r//g' file` 配合git 就是 `git ls-files| xargs sed -i 's/\r//g'`
>1. 去除换行符 `sed ':label;N;s/\n/ /;b label'` [参考](http://www.cnblogs.com/lykm02/p/4479098.html)
>1. 注意特殊字符的转义 `git ls-files | xargs  sed -i 's/@a.*/\//g'`

> [参考博客: linux sed 命令单行任务快速参考](http://www.techug.com/post/linux-sed1line.html)

> 替换满足特定条件的一行里面的多个字符串 `log.debug("who={}", who);` 把这个Java的log 里面的 who删除

## awk
> awk有多个不同版本: awk、mawk nawk和gawk，未作特别说明，一般指gawk，gawk 是 AWK 的 GNU 版本。`在 Deepin 上 awk nawk 都最终是 gawk 的软链接`

1. 截取输出 cat log.log | awk '{print $2}' 
1. 只输出某列之后的列 忽略第一列:`awk '{$1="";print $0}'` 忽略1到4: `awk '{ for(i=1; i<=4; i++){ $i="" }; print $0 }'`
1. 按列求和 `awk '{sum += $1};END {print sum}'`

> [参考博客: awk 入门教程](http://www.ruanyifeng.com/blog/2018/11/awk.html)

