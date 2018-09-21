`目录 start`
 
- [Linux操作压缩文档](#linux操作压缩文档)
    - [tar](#tar)
        - [tar归档和压缩](#tar归档和压缩)
    - [rar](#rar)
    - [zip](#zip)
    - [gz](#gz)
    - [7Z](#7z)
    - [总结](#总结)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Linux操作压缩文档
> Linux默认自带ZIP压缩，最大支持4GB压缩，RAR的压缩比大于4GB.

## tar

1  `这五个是独立的参数, 五个参数之间互斥`
- c : 打包 压缩
- x : 解压
- t : 查看内容 不解压
- r : 向压缩归档文件末尾追加文件
- u : 更新原压缩包中的文件

2 `可选参数`  
2.1 `下面的参数是根据需要在压缩或解压档案时可选的。`
- z：有gzip属性的
- j：有bz2属性的
- Z：有compress属性的
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
> 压缩
- tar -cf a.tar *.txt **仅仅归档,没有压缩**
    1. `-czf` tar.gz **gz压缩**
    1. `-cjf` tar.bz2 
    1. `-cZf` tar.Z
    1. `-cJf` tar.xz

> 解压
- `tar -xf file.tar`      // 解压 tar
- `tar -xzf file.tar.gz`  // 解压 tar.gz
- `tar -xjf file.tar.bz2` // 解压 tar.bz2
- `tar -xZf file.tar.Z `  // 解压 tar.Z

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
## gz
> gunzip 

- [ ] gunzip 命令的学习
***************************
## 7Z
> 安装 apt install p7zip-full 或者 p7zip 
> man 7z 查看帮助文档  
-  `7z <command> [<switches>... ] <archive_name> [<file_names>... ] [<@listfiles>... ]`
    - b benchmark 评测分数 [个人电脑评测](https://gitee.com/kcp1104/codes/0r72axdcp1yewmnljhi8g38)
    
> 压缩
- a 压缩包名 文件名 

> 解压
- 7z x file
    - -o 路径

- [ ] 7z命令的 学习使用

***************
## 总结
| 文件名模式 | 解压方式 |
|:----|:----|
| *.tar |  用 tar -xvf 解压 |
| *.gz|用 gzip -d或者gunzip 解压|
|*.tar.gz和*.tgz| 用 tar -xzf 解压|
|*.bz2|用 bzip2 -d或者用bunzip2 解压|
|*.tar.bz2|用tar -xjf 解压|
|*.Z|用 uncompress 解压|
|*.tar.Z| 用tar -xZf 解压|
|*.rar|用 unrar e 解压|
|*.zip|用 unzip 解压|
