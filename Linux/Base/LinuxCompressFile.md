---
title: Linux平台上压缩和解压工具
date: 2018-12-15 11:12:34
tags: 
    - 工具
categories: 
    - Linux
---

**目录 start**
 
1. [Linux操作压缩文档](#linux操作压缩文档)
    1. [tar](#tar)
        1. [tar归档和压缩](#tar归档和压缩)
    1. [rar](#rar)
    1. [zip](#zip)
    1. [gzip](#gzip)
    1. [xz](#xz)
    1. [7Z](#7z)
1. [压缩文件内容预览搜索](#压缩文件内容预览搜索)
1. [压缩文件密码](#压缩文件密码)

**目录 end**|_2020-02-29 01:11_|
****************************************
# Linux操作压缩文档
> Linux默认自带ZIP压缩，最大支持4GB压缩，RAR的压缩比大于4GB.

| 文件名模式 | 解压方式 |
|:----|:----|
| *.tar             | tar -xvf 解压 |
| *.tar.gz 和 *.tgz | tar -xzf 解压|
| *.tar.xz          | tar -xJf 解压|
| *.tar.Z           | tar -xZf 解压|
| *.tar.bz2         | tar -xjf 解压|
|-|-|
| *.gz              | gzip -d 或者 gunzip 解压|
| *.bz2             | bzip2 -d或者用bunzip2 解压|
| *.Z               | uncompress 解压|
| *.xz              | xz -d 解压|
| *.rar             | unrar e 解压|
| *.zip             | unzip 解压|

*********************************

## tar

1  `这五个是独立的参数, 五个参数 有且仅有一个`
- c : 打包 压缩
- x : 解压
- t : 查看内容 不解压
- r : 向压缩归档文件末尾追加文件
- u : 更新原压缩包中的文件

2 `可选参数`  
2.1 `下面的参数是根据需要在压缩或解压档案时可选的。`
- v：显示所有过程
- O：将文件解开到标准输出

2.2 `其他可选参数`
- `-p` 保留绝对路径符
- `-v` 将压缩或解压的过程输出

3 `最后`
- `-f 是必须的,-f: 使用档案名字，切记，这个参数是最后一个参数，后面只能接文件或目录`

> 以上则组合出了 tar 的所有使用场景

***************************
**示例 :**
- `tar -rf all.tar *.gif`这条命令是将所有.gif的文件增加到all.tar的包里面去。
- `tar -uf all.tar logo.gif`这条命令是更新原来tar包all.tar中logo.gif文件，
- `tar -tf all.tar` 这条命令是列出all.tar包中所有文件，
- `tar -xf all.tar` 这条命令是解出all.tar包中所有文件，

- 保留文件属性和跟随链接， -p 保留属性 -h 备份的源文件而不是链接本身
    - `tar -cphf etc.tar /etc`

********************
### tar归档和压缩

| 字母 | 压缩方式 |
|:----:|:----:|
| z | gz |
| Z | Z |
| j | bz2 |
| J | xz |

**************************
本质上 tar 的压缩和解压都是调用对应的软件完成的, 例如 `tar cJf a.tar.xz a/` 就是先tar归档一下, 然后调用 xz 完成压缩

> 压缩
- tar -cf a.tar *.txt **仅仅归档,没有压缩**
    - tar -czf a.tar.gz *.txt`归档, 并使用gz格式压缩归档包, 以此类推`

> 解压
- `tar -xf file.tar`      // 解压 .tar 归档文件
    - tar -xzf a.tar.gz `解压使用gz格式压缩的压缩包, 以此类推`

****************
## rar
> 压缩
- `rar a jpg.rar *.jpg`    // rar格式的压缩

> 解压
- `unrar x file.rar`       // 解压 rar
    - `e` 不保留目录结构,平铺解压

********************
## zip
> 压缩
- `zip images.zip *.jpg` //zip格式的压缩
- `zip -r file.zip code/*` 压缩code目录下所有文件
    - `zip -r ./a.zip ./*` 压缩当前目录所有文件
    - `-q`安静模式, 终端不输出
    - `-o` 输出文件`
    - `-r` 表示递归
    - `-l` 兼容Windows的换行符
    - `-e` 加密
    - `-d filename` 在zip中删除某文件 删除某目录`dir/*`
        - _注意_: 所有的文件和目录都是相对于zip的根目录的完整路径

> 解压
- `unzip file.zip `//解压zip
    - -q 终端不输出 
    - -d 指定解压目录 
    - -l 不解压,查看所有文件 
    - -O 指定编码

***************************
## gzip
> gzip gunzip. 常见压缩包格式: .tar.gz .tgz 

由于只能操作单个文件, 所以一般是借助于 tar 归档后再压缩

> 压缩
- gzip 文件

> 解压
- gzip -d 文件 或者 gunzip 文件

## xz 
> xz. 常见压缩包格式: .xz .txz .lzma .tlz

和 gzip 类似, 只能操作单个文件, 但是压缩率高于 gzip, 伴随的是压缩时间要长一些

> 压缩
- xz 文件

> 解压
- xz -d 文件

***************************
## 7Z
> 安装 apt install p7zip-full 或者 p7zip 
> man 7z 查看帮助文档  
-  `7z <command> [<switches>... ] <archive_name> [<file_names>... ] [<@listfiles>... ]`
    - `b`: benchmark 评测压缩和解压速率
    
> 压缩
- a 压缩包名 文件名 

> 解压
- 7z x file
    - `-o` 路径

# 压缩文件内容预览搜索
> [参考博客: Unix Z Commands – Zcat, Zless, Zgrep, Zegrep and Zdiff Examples ](https://linoxide.com/linux-how-to/z-commands-zcat-zless-zgrepzegrep-zdiff-examples/)  

- `zcat log.tgz | grep -a "pattern"` 等价于 `zgrep "pattern" log.tgz`
    - 相关参数说明 man 文档

# 压缩文件密码
- rarcrack 暴力破解
