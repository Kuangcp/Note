`目录 start`
 
- [流编辑器](#流编辑器)
    - [grep](#grep)
    - [tr](#tr)
    - [cut](#cut)
    - [paste](#paste)
    - [sed](#sed)
    - [awk](#awk)

`目录 end` |_2018-08-10_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 流编辑器
> [参考博客: 比较linux下各种流编辑器的用法](https://blog.csdn.net/havedream_one/article/details/45007449)

## grep
> g (globally) search for a re (regular expression ) and p (print ) the results.

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
> 组成模式: `参数 命令 文件`

- `参数`
    - `-n` 直接在控制台输出的操作的结果，源文件不变 
    - `-i` 在源文件中进行修改
- `命令`
    - p 打印 `sed -n Np 文件名`
    - a 新增 在下一行
    - i 插入 在上一行 将hello插入到第4行：`sed -in "4i hello" test.md`
    - c 替换 整行
    - s 替换 字符串的替换
    - d 删除 行级别, 删除2-4行 `sed -i "2,4d" test.md`

> 1. 截取指定行数到新文件 `sed -n ‘开始行数，结束行数p’ info.log > newFile.log`
> 2. 修改配置文件中name的值为123 `sed -i "s/name=.*/name=123/g" config.conf`

> [参考博客: linux sed 命令单行任务快速参考](http://www.techug.com/post/linux-sed1line.html)
## awk
> awk有3个不同版本: awk、nawk和gawk，未作特别说明，一般指gawk，gawk 是 AWK 的 GNU 版本。


