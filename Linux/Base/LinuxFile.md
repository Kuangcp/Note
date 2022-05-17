---
title: Linux文件系统
date: 2018-12-15 11:14:54
tags: 
    - 基础
categories: 
    - Linux
---

**目录 start**

1. [文件管理](#文件管理)
    1. [查找文件](#查找文件)
        1. [find](#find)
        1. [locate](#locate)
        1. [Anything](#anything)
        1. [Synapse](#synapse)
    1. [查看文件](#查看文件)
        1. [stat](#stat)
        1. [file](#file)
        1. [tree](#tree)
        1. [ls](#ls)
        1. [wc](#wc)
        1. [cat](#cat)
        1. [nl](#nl)
        1. [less](#less)
        1. [tail](#tail)
        1. [head](#head)
    1. [比较文件内容](#比较文件内容)
        1. [diff](#diff)
        1. [meld](#meld)
        1. [kdiff3](#kdiff3)
        1. [vimdiff](#vimdiff)
    1. [文件变更命令](#文件变更命令)
        1. [rename](#rename)
        1. [chown](#chown)
        1. [chgrp](#chgrp)
        1. [ln](#ln)
        1. [cp](#cp)
        1. [rm](#rm)
        1. [mv](#mv)
        1. [文件的分割与合并](#文件的分割与合并)
        1. [监控文件变更](#监控文件变更)
    1. [默认字符编码](#默认字符编码)
1. [磁盘](#磁盘)
    1. [文件系统](#文件系统)
        1. [fsck](#fsck)
    1. [安装系统时基本分区](#安装系统时基本分区)
    1. [设备列表](#设备列表)
    1. [常用命令](#常用命令)
        1. [dd](#dd)
        1. [mount](#mount)
        1. [fdisk](#fdisk)
        1. [df](#df)
        1. [du](#du)
1. [日志](#日志)
    1. [Systemd](#systemd)
    1. [应用日志](#应用日志)
1. [文件共享](#文件共享)
    1. [Samba](#samba)
        1. [搭建匿名Samba服务器](#搭建匿名samba服务器)
    1. [WebDAV](#webdav)
1. [Tips](#tips)
    1. [设置交换内存文件](#设置交换内存文件)
        1. [清空交换内存](#清空交换内存)
    1. [清除缓存](#清除缓存)
    1. [善用*shrc文件](#善用shrc文件)
        1. [善用alias](#善用alias)
    1. [desktop文件](#desktop文件)

**目录 end**|_2022-05-17 22:56_|
****************************************
# 文件管理
> Linux中认为万物皆文件

- `cd - ` 跳转到上一个目录
- `cd !$` 把上个命令的参数作为cd参数使用。

> [用文件头标识判断文件类型](https://blog.mythsman.com/post/5d301940976abc05b345469f/)`而不是Windows那样默认以文件后缀来判断`  

## 查找文件

> silversearcher-ag `快速搜索文件的内容`

### find
- `find . -name "*.txt"` 查找当前目录的txt后缀的文件
- `sudo find / -name a.java` 全盘查找
- `find -type f -name README.md` 默认当前目录查找
    - d 文件夹 f 普通文件 l 符号链接文件 b 块设备 c 字符设备 p 管道文件 s 套接字

- **exec** 嵌入一个命令
    1. 找到所有pdf移动到指定目录 `find . -name "*.pdf" -exec mv {} /home/test \;`
    1. 把当前目录下面的file（不包括目录)，移动到/opt/shell 
        - `find .  -type f  -exec mv {}   /opt/shell   \;`
        - `find .  -type f  |  xargs  -I  '{}'  mv  {}  /opt/shell`
    1. 解压目录下所有zip文件 `find . -name "*.zip" -exec unzip  {}  \;`

**实践**
1. 递归删除目录下所有run后缀的文件 `find . -name "*.run"  | xargs rm -f`
    - 递归当前文件夹下所有 log 找到 ERROR日志 `find -name "*.log" | xargs grep ERROR`
1. 查找文件内容 `find etc/  |xargs grep -i java`

### locate
> 预先建立数据库，依此查询 速度较快，但是有时效问题

### Anything
> 图形化 搜索文件 工具，也是预先建立数据库

### Synapse
> 搜索文件 启动应用等功能

************************

## 查看文件
### stat
- 查看文件详细信息 `stat filename `

### file
- file a.txt 查看文件类型
    - -i 输出文件的MIME类型
    - -F "#" 修改输出分隔符

### tree
- 展示目录结构
    - -p 匹配
    - -h 可读的显示文件大小
    - -F 和ls一样
    - -L 目录深度

### ls
- `参数`
    - `i` 详情 
    - `a` 全部包含隐藏文件 <> `A` 不显示当前目录和上级目录 `.` `..` 
    - `l` 使用较长格式列出信息 详细信息
    - `h` 人类可阅读
    - `F` 标明文件夹,文件,可执行文件 
    - `w` 100 限制输出每行的字符长度 0 则是无限制 和 l 共用就则无视该限制
    - `R` 递归显示所有子文件夹
    - `r` 逆序
    - `B` 不列出以〜结尾的隐含条目
    - `t` 按修改时间从顶至下,一般不单用,和 g|l 结合一起用
    - `c` 按ctime(创建时间)一般是文件夹,文件则是修改时间排列
        - 和 lt|gt 一起用 即 `ls -clt` 同上的排列顺序
- `执行ls -l 命令后的输出`
    1. 输出类型：d 目录 l 软链接 b 块设备 c 字符设备 s socket p 管道 - 普通文件
    1. 输出权限信息：r 读权限 w 写权限 x 执行权限
        - rwx有三个，是因为 `拥有者，所属用户组 其他用户` 代表的rwx权限
        - ![权限输出图](https://dn-anything-about-doc.qbox.me/linux_base/3-10.png/logoblackfont)
        - ![权限计算图](https://dn-anything-about-doc.qbox.me/linux_base/3-14.png/logoblackfont)
        - `chmod 700 文件` 就是只设置拥有者具有读写权限
        - 加减权限操作 `chmod go-rw 文件` `g group` `o others` `u user` `+- 增减权限`
    1. 硬链接数 一般你可以理解成子目录数（对于普通文件，总是1，对于目录来说，为对应目录的 _下一级子目录的个数_ +2 (+2是由于 . 和 .. 的原因））
    1. 最后是归属用户和用户组, 大小, 最后修改日期

- `ls -lFh` 列出所有文件的详细信息, 并且文件大小是人类可阅读的

ls * | xargs md5sum > b.log
find . | xargs md5sum > b.log
le b.log | awk '{print $1}'| kp.count  | head -n 17 > re.log
cat re.log | awk '{print $2}' | xargs -I {} grep  {} b.log  > fin.log

le fin.log | awk '{print $2}' | xargs -I {} mv {} ../
le fin.log | grep -v VID | awk '{print $2}' | xargs rm -f

### wc
- `wc [-lmw] ` 参数说明： -l :多少行-m:多少字符 -w:多少字
- cat mul.sh | wc -l
- wc -l mul.sh

### cat
- 类似的还有 nl more less

带行号输出 `cat -n file` 或者 `nl file`但是空行不会编号, 除非这样: `nl -b a file`

### nl
- [参考: 每天一个linux命令(11)：nl命令](http://www.cnblogs.com/peida/archive/2012/11/01/2749048.html#/)

### less
- 该命令的导航是和Vi体系一样的, 建议打开大文件使用less或者more 如果用vim,文件全加载到内存了  
- 诸多软件使用到了分页, 怀疑就是借助less实现的, 因为快捷键一模一样, 例如 man命令, 各个软件的-h, git的log 等等..优点很多
- [ less命令简介](https://blog.csdn.net/caihaijiang/article/details/6113419)
- h 查看帮助文档 z/b 上下翻页 g/G 文件首/尾 
- F 监听文件

- 当打开多个文件时 `:n`和`:p` 表示 next pre　也就是　下一个，上一个文件

> [syntax-highlighting](https://unix.stackexchange.com/questions/90990/less-command-and-syntax-highlighting)  
> [Make the less Command More Powerful](https://www.topbug.net/blog/2016/09/27/make-gnu-less-more-powerful/)

1. install  source-highlight
1. append to  *sh.rc
    ```sh
    # sh 在不同的系统 路径和名字都有可能不一样
    export LESSOPEN="| /usr/bin/source-highlight-esc.sh %s"
    export LESS=' -R'
    ```

### tail
- tail命令用于输入文件中的尾部内容。tail命令默认在屏幕上显示指定文件的末尾10行。 来自: http://man.linuxde.net/tail

- `--retry`：即是在tail命令启动时，文件不可访问或者文件稍后变得不可访问，都始终尝试打开文件。此选项需要与选项“——follow=name”连用； 
- `-c或——bytes=`：输出文件尾部的N（N为整数）个字节内容； 
- `-f或；--follow`：显示文件最新追加的内容。“name”表示以文件名的方式监视文件的变化。“-f”与“-fdescriptor”等效； 
- `-F`：与选项“-follow=name”和“--retry"连用时功能相同； 
- `-n或——line=`：输出文件的尾部N（N位数字）行内容。 
- `--pid=<进程号>`：与“-f”选项连用，当指定的进程号的进程终止后，自动退出tail命令； 
- `-q或——quiet或——silent`：当有多个文件参数时，不输出各个文件名； 
- `-s<秒数>或——sleep-interal=<秒数>`：与“-f”选项连用，指定监视文件变化时间隔的秒数；
- `-v或——verbose`：当有多个文件参数时，总是输出各个文件名；

```
    tail file （显示文件file的最后10行） 
    tail +20 file （显示文件file的内容，从第20行至文件末尾） 
    tail -c 10 file （显示文件file的最后10个字符）
```
### head  
- 查看文件头部, 默认前十行 使用 -n 指定行数

## 比较文件内容
- `grep -vwf 文件1 文件2`

> [阮一峰: 读懂diff](http://www.ruanyifeng.com/blog/2012/08/how_to_read_diff.html)

### diff
> [参考博客 linux下比较两个文本文件的不同——diff命令](http://www.cnblogs.com/chenjianhong/archive/2012/09/26/4144940.html)

### meld
> [Github: meld](https://github.com/GNOME/meld)

> 可用于 git svn 查看差异, 或者简单的两个文件查看差异

### kdiff3

### vimdiff

## 文件变更命令
### rename
`rename命令的使用(基于perl)`
- `rename "s/.html/.php/" * ` //把.html 后缀的改成 .php后缀
- `rename "s/$/.txt/" *  `   //把所有的文件名都以txt结尾
- `rename "s/.txt//" *  `   //把所有以.txt结尾的文件名的.txt删掉
- `rename "s/AA/aa/" * `  //把文件名中的AA替换成aa
- `rename "s/ - 副本/_bak/" *` 将文件`-副本`结尾改成`_bak`结尾

### chown
- `chown [-R] 账号名称 文件或目录`
- `chown [-R] 账号名称:用户组名称 文件或目录`

### chgrp
- 更改文件所属用户组 `chgrp group file`
    - -R 递归子目录
    
### ln
- `ln -s 源文件或目录 目标绝对路径` 生成软链接（快捷方式）
```sh
    ln -s `pwd`/a.md ~/a.md 
```

### cp
- cp   `cp -ri 目录或正则 目录` 目录所有文件复制过去
    - a 该选项通常在拷贝目录时使用。它保留链接、文件属性，并递归地拷贝目录，其作用等于dpR选项的组合。
    - d 拷贝时保留链接。
    - f 删除已经存在的目标文件而不提示。
    - i 和f选项相反，在覆盖目标文件之前将给出提示要求用户确认。回答y时目标文件将被覆盖，是交互式拷贝。
    - p 此时cp除复制源文件的内容外，还将把其修改时间和访问权限也复制到新文件中。
    - r 若给出的源文件是一目录文件，此时cp将递归复制该目录下所有的子目录和文件。此时目标文件必须为一个目录名。
    - l 不作拷贝，只是链接文件。

### rm
- rm  `rm -rf 目录` 不提示性删除
    - f 忽略不存在的文件，从不给出提示。
    - r 指示rm将参数中列出的全部目录和子目录均递归地删除。
    - i 进行交互式删除(y/n的询问)。 

> 特别注意 rm -rf link 文件时, 如果只是想删除link文件 那么就不要在link文件后加上 / 例如:  
> `rm -rf linkDir/ ` 这个命令是将 link到的目录下的文件全部删除而不是 删除link文件本身 

### mv
- mv `mv 目录或正则 目录` 移动
    - I 交互方式操作。如果mv操作将导致对已存在的目标文件的覆盖，此时系统询问要求用户回答y或n，这样可以避免误覆盖文件。
    - f 禁止交互操作。在mv操作要覆盖某已有的目标文件时不给任何指示，指定此选项后，i选项将不再起作用。

### 文件的分割与合并
> [参考: 文件过滤分割与合并](http://man.linuxde.net/sub/%e6%96%87%e4%bb%b6%e8%bf%87%e6%bb%a4%e5%88%86%e5%89%b2%e4%b8%8e%e5%90%88%e5%b9%b6)

> 分割

- split
    1. 指定行数分割 `split -l 300 log.txt newfile`
    1. 指定文件大小 `split -b 500m log.txt newfile`

> 合并

1. 最简单就是 `cat file1 file2 > result`

### 监控文件变更
> 原理是通过监听文件变更时发出的 signal

- 借助 inotify-tool 包更容易使用
    - inotifywait
    - inotifywatch

- 持续监听某目录变更 `inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format '%T %w%f%e' -e modify,delete,create,attrib /home/kcp/test/git-test`

************************

## 默认字符编码
> 查看当前编码  locale 或者 echo $LANG

1. 修改编码 `/etc/profile` 
```sh
LC_ALL="zh_CN.UTF-8"
export LANG="zh_CN.UTF-8"
```

************************

# 磁盘
> [Linux系统基本目录结构](/Linux/Base/LinuxDirectoryStructure.md)

> [参考: 在 Linux 上检测硬盘上的坏道和坏块 ](https://linux.cn/article-7961-1.html)  

- bleachbit 应用占用磁盘 清理

## 文件系统
> [参考: Linux 文件系统剖析](https://www.ibm.com/developerworks/cn/linux/l-linux-filesystem/index.htmlQ)
> [参考: 详解NTFS文件系统](http://www.blogfshare.com/detail-ntfs-filesys.html)
> [参考: 使用 FUSE 开发自己的文件系统](https://www.ibm.com/developerworks/cn/linux/l-fuse/)

> tmpfs [wiki](https://wiki.archlinux.org/index.php/Tmpfs)

### fsck
> check and repair a Linux filesystem

当系统突然断电而导致文件系统不一致时, 可使用该命令进行修复, 例如:`fsck.ext4 -vy /dev/sdaXX`

## 安装系统时基本分区
- / 根目录, 操作系统安装的目录
- /home 普通用户的主目录分配路径
- /boot 系统引导目录

********************
## 设备列表
- /dev/random 产生随机数的设备

**********************
## 常用命令
1. 将虚拟磁盘镜像格式化为指定的文件系统 `sudo mkfs.ext4 virtual.img`
1. 查看支持的文件系统 `ls -l /lib/modules/$(uname -r)/kernel/fs`
1. [重命名USB磁盘挂载分区卷标](http://wiki.ubuntu.org.cn/%E9%87%8D%E5%91%BD%E5%90%8DUSB%E7%A3%81%E7%9B%98%E6%8C%82%E8%BD%BD%E5%88%86%E5%8C%BA%E5%8D%B7%E6%A0%87)

> 格式化分区
1. 格式化为ext4 `mkfs -t ext4 /dev/sdc1`

### dd
> [使用 dd 命令进行硬盘 I/O 性能检测 ](https://linux.cn/article-6104-1.html)

- 例如创建一个空4G文件: `dd if=/dev/zero of=/testfile bs=1024k count=4096`

### mount
- `mount [options] [source] [directory] `
- `mount [-o [操作选项]] [-t 文件系统类型] [-w|--rw|--ro] [文件系统源] [挂载点]`
- 查看已挂载信息 `mount`

- 挂载这个镜像到 /mnt ：`mount -o loop -t ext4 virtual.img /mnt`
- 只读方式挂载 `mount -o loop --ro virtual.img /mnt`
- 卸载挂载的磁盘 `sudo umount /mnt`

> 设置自动挂载某分区 (root身份运行命令)
1. `blkid` 查看设备详情, 找到要挂载的硬盘的 UUID 以及 文件系统类型
1. `vim /etc/fstab` 在文件中添加, 记得要 先创建该目录 `/media/kcp/Data1`
    - `UUID=42168DE83BC5EDAD /media/kcp/Data1 ntfs defaults 0 1` 类似配置
    - `mount -a` 切记要先用该命令测试下该文件是否正确, 如果有错误, 系统关机后就开不了机了(但是可以使用U盘进系统 修改该文件)

### fdisk
- 查看磁盘分区表信息 ：`sudo fdisk -l `

### df 
> 报告文件系统磁盘空间使用情况 

- -h 可读性 human readable
- -T 查看挂载文件系统的类型信息
- -a 所有文件系统
- -l 只显示本地文件系统

### du
- `du -sh 目录` 查看磁盘占用总大小 h 自动搭配单位（human read ）
- `du --max-depth` 一级子目录使用情况
- `du -sm * | sort -n` 统计当前目录大小 并按大小(mib)排序 `-sk`则是换算成kib
- `du -m | cut -d "/" -f 2` 看第二个`/`字符前的文字

- 案例： 获取当前目录最大的6个目录或文件 `du -hsx * | sort -rfh | head -6` 
    - -hsx – （-h）更易读的格式，（-s）汇总输出，（-x）跳过其他文件系统的文件
    - sort – 对文本文件按行排序 （-r）将比较的结果逆序输出，（-f）忽略大小写 -h 可读
    - head – 输出文件的前几行
- [ncdu](https://dev.yorhel.nl/ncdu)

************************

# 日志
> 基本都在 `/var/log` 下

- last 查看用户最后登录时间
- logrotate 日志处理工具（切分，压缩，邮件通知等功能）

## Systemd
> 通常使用 journalctl 查询 Systemd 的日志

- message catalog: `journalctl -xe` 
- 内核模块的日志 `journalctl -u systemd-modules-load.service`
- **/var/log/journal**
    - `journalctl --vacuum-time=1w` 只保留1周日志

## 应用日志
> [处理Apache日志的Bash脚本](http://www.ruanyifeng.com/blog/2012/01/a_bash_script_of_apache_log_analysis.html)

************************
# 文件共享
## Samba 
> [参考: ](https://www.jianshu.com/p/b0fcf29a857a)  


### 搭建匿名Samba服务器

1. /etc/samba/smb.conf
    ```ini
        [global]
        workgroup = WORKGROUP       
        #所要加入的工作组或者域
        netbios name = Manjaro      
        #用于在 Windows 网上邻居上显示的主机名
        security = user             
        #定义安全级别
        map to guest = bad user     
        #将所有samba系统主机所不能正确识别的用户都映射成guest用户
        dns proxy = no              
        #是否开启dns代理服务

        [share]                    
        #共享显示的目录名 注意每级目录samba用户都要有权限 最简单就放最高层级的目录上
        path = /share
        #实际共享路径
        browsable = yes             
        #共享的目录是否让所有人可见
        writable = yes              
        #是否可写
        guest ok = yes              
        #是否允许匿名(guest)访问,等同于public
        create mask = 0777          
        #客户端上传文件的默认权限
        directory mask = 0777       
        #客户端创建目录的默认权限
        #注意共享文件在系统本地的权限不能低于以上设置的共享权限。
    ```
1. smbpasswd -a share #共享显示的目录名
1. pdbedit -L 查看所有Samba用户
1. chmod 777 -R /share
1. systemctl restart smb nmb
1. 测试可用性 smbclient //192.168.0.10/share

## WebDAV
- [Wiki](https://en.wikipedia.org/wiki/WebDAV)

Windows 客户端 RaiDrive

- [go开发WebDAV服务端](https://pkg.go.dev/golang.org/x/net/webdav)

************************

# Tips
- 清空文件内容 `true > a.txt ` 
- 安装上传下载文件的工具 `sudo apt install lrzsz`
- `cat ~/.ssh/id_rsa.pub | xsel -b` 将文件复制到剪贴板

## 设置交换内存文件
- 查看内存 `free -h` 
- 创建一个4g 交换文件 `dd if=/dev/zero of=/swapfile bs=1024k count=4096` 
- 格式化成交换文件的格式 `mkswap /swapfile` 
- 启用该文件作为交换分区的文件 ` swapon /swapfile` 
- `/swapfile swap swap defaults 0 0` 写入`/etc/fstab`文件中，让交换分区的设置开机自启

- 修改交换内存开始使用的阈值
    - `sudo sysctl vm.swappiness=15` 临时修改重启注销失效， 查看：`cat /proc/sys/vm/swappiness`
    - 永久修改：`/etc/sysctl.conf ` 文件中设置开始使用交换分区的触发值： `vm.swappiness=10`
    - 表示物理内存剩余`10%` 才会开始使用交换分区
    - `建议，笔记本的硬盘低于 7200 转的不要设置太高的交换分区使用，大大影响性能，因为交换分区就是在硬盘上，频繁的交换数据`

```sh
    # 完整命令: root身份运行
    dd if=/dev/zero of=/swapfile bs=1024k count=4096 && mkswap /swapfile && swapon /swapfile && echo "/swapfile swap swap defaults 0 0" >> /etc/fstab
```
### 清空交换内存
- 1.关闭交换分区 `sudo swapoff 交换分区文件`
    - 2.开启交换分区 `sudo swapon 交换分区文件`
- 或者 `swapoff -a && swapon -a`

## 清除缓存
> [参考: 如何在 Linux 中清除缓存（Cache）？](https://linux.cn/article-5627-1.html) `注意要切换到root再运行命令`  
> [参考: Linux 内存中的Cache，真的能被回收么？](https://www.cnblogs.com/276815076/p/5478966.html)  

> `/proc/sys/vm/drop_caches`
> 设置值 `sync; echo 1 > /proc/sys/vm/drop_caches`

| 值 | 作用 |
|:----|:----|
| 1 | 仅清除 page cache |
| 2 | 表示清除回收slab分配器中的对象（包括目录项缓存和inode缓存） |
| 3 | 表示清除page cache和slab分配器中的缓存对象 |

- 曾经因为缓存的问题会引发一些很诡异的问题
    - 例如构建工具Maven, 也会因为在一个项目空间下, 多个同名项目的缓存问题 
        - 巨诡异 `if(true){}` 都能不执行, if 和 else 同时执行

## 善用*shrc文件
> 注意加载顺序 /etc/profile -> ~/.*shrc `各种sh的rc文件` bash zsh ash

### 善用alias

```sh
    if [ -f ~/.bash_aliases ]; then
        . ~/.bash_aliases
    fi
```
- 在`~/.bashrc`添加这段，然后在 `.bash_aliases` 文件中设置别名
    - 例如 ： `alias Kg.notes='cd ~/Documents/Notes/Code_Notes/'` 
    - 更改文件后，想当前终端就生效就 `source ~/.bashrc` 不执行命令就重启终端即可
> 注意_
> 你会发现 当前用户 下 Kg.notes 是正常运行的, 但是 sudo Kg.note 就会报错说找不到命令  
> 神奇的是 配置一个别名 `alias sudo='sudo '` 就可以解决这个问题了 [stackoverflow](https://askubuntu.com/questions/22037/aliases-not-available-when-using-sudo)
> 官方说明如下_
```
    The first word of each simple command, if unquoted, is checked to see if it has an alias. If so, that word is replaced by the text of the alias. 
    The characters ‘/’, ‘$’, ‘`’, ‘=’ and any of the shell metacharacters or quoting characters listed above may not appear in an alias name. 
    The replacement text may contain any valid shell input, including shell metacharacters. The first word of the replacement text is tested for aliases, 
    but a word that is identical to an alias being expanded is not expanded a second time. This means that one may alias ls to "ls -F", for instance, 
    and Bash does not try to recursively expand the replacement text. If the last character of the alias value is a space or tab character, 
    then the next command word following the alias is also checked for alias expansion. 
```
- 如[我的配置文件](https://github.com/Kuangcp/Configs/tree/master/Linux/init) `将配置文件分类放`
    - K.h就能显示出每个命令的说明 其实现脚本： [python3脚本](https://github.com/Kuangcp/Script/blob/master/python/show_alias_help.py) 
    - 在别名文件目录时, 建立链接就可以用了 `ln -s `pwd`/.bash_aliases ~/.bash_aliases` 

*************************

## desktop文件
> [freedesktop](https://www.freedesktop.org/wiki/)

```conf
	[Desktop Entry] #每个desktop文件都以这个标签开始，说明这是一个Desktop Entry文件
	Version = 1.0 #标明Desktop Entry的版本（可选）
	Name = Firefox #程序名称（必须），这里以创建一个Firefox的快捷方式为例
	GenericName = Web Browser #程序通用名称（可选）
	Comment = A Web Browser #程序描述（可选）
	Exec = firefox %u #程序的启动命令（必选），可以带参数运行,当下面的Type为Application，此项有效
	Icon = firefox #设置快捷方式的图标 svg(更好) png
	Terminal = false #是否在终端中运行（可选），当Type为Application，此项有效
	Type = Application #desktop的类型（必选），常见值有“Application”和“Link”
	Categories = GNOME;Application;Network; #注明在菜单栏中显示的类别（可选）
```
- [示例文件](https://github.com/Kuangcp/Configs/blob/master/Linux/desktop/VSCode.desktop)
- 如要将快捷方式放在启动菜单内 将 desktop 文件复制到 `/usr/share/applications/` 目录下即可
    - 注意：目录不能有空格 等特殊字符
