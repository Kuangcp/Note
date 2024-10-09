---
title: Linux性能分析
date: 2018-12-15 11:16:27
tags: 
    - 基础
categories: 
    - Linux
---

💠

- 1. [Linux性能分析和管理](#linux性能分析和管理)
- 2. [基准测试](#基准测试)
- 3. [运行状况信息](#运行状况信息)
    - 3.1. [分析工具](#分析工具)
- 4. [内核参数](#内核参数)
- 5. [内存情况](#内存情况)
    - 5.1. [free](#free)
    - 5.2. [smem](#smem)
- 6. [性能监测](#性能监测)
    - 6.1. [perf](#perf)
    - 6.2. [top](#top)
    - 6.3. [smem](#smem)
    - 6.4. [vmstat](#vmstat)
    - 6.5. [pidstat](#pidstat)
    - 6.6. [mpstat](#mpstat)
    - 6.7. [iostat](#iostat)
    - 6.8. [ifstat](#ifstat)
- 7. [进程管理](#进程管理)
    - 7.1. [pidof](#pidof)
    - 7.2. [pgrep](#pgrep)
    - 7.3. [sar](#sar)
    - 7.4. [lsof](#lsof)
        - 7.4.1. [删除文件](#删除文件)
    - 7.5. [fuser](#fuser)
    - 7.6. [ps](#ps)
        - 7.6.1. [procs](#procs)
        - 7.6.2. [pstree](#pstree)
    - 7.7. [kill](#kill)
        - 7.7.1. [killall](#killall)
    - 7.8. [trap](#trap)
    - 7.9. [作业控制](#作业控制)
    - 7.10. [守护进程](#守护进程)
        - 7.10.1. [nohup](#nohup)
        - 7.10.2. [disown](#disown)
        - 7.10.3. [setid](#setid)
        - 7.10.4. [screen](#screen)
    - 7.11. [IPC](#ipc)
- 8. [系统管理](#系统管理)
    - 8.1. [uname](#uname)
    - 8.2. [who](#who)
    - 8.3. [service](#service)
    - 8.4. [chkconfig](#chkconfig)
    - 8.5. [dmidecode](#dmidecode)
    - 8.6. [lsmod](#lsmod)
    - 8.7. [chroot](#chroot)
- 9. [关机/重启](#关机重启)

💠 2024-10-09 16:33:39
****************************************
# Linux性能分析和管理

# 基准测试
目的：通过一致的工具及配置，跑不同的测试工具，看性能表现，对比不同设备间性能差异

> [几款优秀的Linux基准测试工具](https://blog.csdn.net/gatieme/article/details/54296440)  
> [Arch wiki: Improving performance](https://wiki.archlinux.org/title/Improving_performance)  

1. [byte-unixbench](https://github.com/kdlucas/byte-unixbench)
1. [geekbench](https://www.geekbench.com)

> 高负载测试
1. [stress](https://github.com/cirocosta/stress)
1. [stress-ng](https://github.com/ColinIanKing/stress-ng)
- stress-ng --cpu 16 --timeout 180 `占满CPU`
- stress-ng --vm 4 --vm-bytes 10G --vm-hang 180 --timeout 180s
- stress-ng --hdd 5 --hdd-bytes 10G --timeout 180s

> 简易评测
- 单核CPU: `time echo "scale=9000; 4*a(1)" | bc -l -q` 

| 设备 | 耗时 |
|:----|:----|
| Mac Book Pro 2023 32G: | **4s** |
| i5-10400F CPU @ 2.90GHz: | **60s** |
| 笔记本 AMD Ryzen 7 6800H: | **59s** |
| 阿里云99年费双核服务器 2.5GHz | **79s** |
| Redmi K60 | **57s** |
| AMD 3700X 8-Core @ 16x 3.6GHz | **53s** | 

> 3700x 和 10400F 和 K60 的 8+ Gen 1 单核性能是差不多的 😅

************************

# 运行状况信息
> 系统实时状态信息

- top
- [htop](https://github.com/hishamhm/htop)`Htop更好用`
    - [你一定用過 htop，但你有看懂每個欄位嗎？](https://medium.com/starbugs/do-you-understand-htop-ffb72b3d5629)
    - CPU: Task 进程 thr 线程 kthr 内核线程 running 执行中的线程
- gotop 
- ytop
- ctop 
- [Glances](https://github.com/nicolargo/glances) `信息全面 资源消耗大些`
- nmon

- `uptime ` 执行结果
    - 系统当前时间 | 主机已运行时间 | 用户连接数 | 1,5,15,分钟的系统平均负载
- `cat /proc/loadavg ` 
    - 运行结果 : 1,5,15分钟的平均负载 | 当前运行的进程/总进程 | 最近一个启动的进程的id 
> 常规: 单核:平均负载0.7以下是安全的,大于就需要优化了,多核则是 0.7*N(核心数)  
> [从源码看Load计算方式](http://www.penglixun.com/tech/system/how_to_calc_load_cpu.html)  

- `lm-sensors` CPU等硬件温度等信息检测 [参考](https://www.ostechnix.com/view-cpu-temperature-linux/)

## 分析工具
> [vector](https://github.com/Netflix/vector)
> [CPU-X ](http://x0rg.github.io/CPU-X/) | [Github:repo](https://github.com/X0rg/CPU-X)`简洁而详细`    


************************

# 内核参数
- sysctl -n name 读取配置
- sysctl -w name value 写入配置
- sysctl -p 不重启的情况下reload配置

************************

# 内存情况
## free
- 直接运行得到的就是内存情况,默认是kb为单位,可以指定 -b -m -g (后两种不推荐,因为向下取整的特性)
    - -h 人类可读形式 推荐,能快速看到大略,精准的话还是用 -b

**`输出解析`**

- `used` 内存已使用量(不含buff/cache), `free` 空闲内存, `available` 可用内存
- buffers,cached:
    - `buffers` 是为了写时,解决内存和硬盘巨大速度差存在的缓冲区(块设备IO相关的缓存页)
    - `cache` 是为了读时,为了尽量减少内存从硬盘读数据的次数,缓冲区(普通文件相关的缓存页)
    - `cached` 就是cache内存区域已经使用量

>- 注意: 如果是新版的free, shared 那一栏总是为0, 因为shared本就是说明进程共享内存容量, free认为不能显示数有效信息, 就抛弃了这个指标,总是显示为0

## smem
较精准展示进程使用的内存和swap内存

**************************

# 性能监测
> 通过各类软件的输出，快速定位问题点

1. 监测CPU利用率 top,sysstat,mpstat,iostat,sar

sysstat软件包：sysstat，mpstat vmstat iostat

************************
> 工程化管理多个Linux主机

[wgcloud](https://github.com/tianshiyeben/wgcloud)  
[netdata](https://github.com/netdata/netdata)  

## perf
> [参考: Perf 使用说明](https://yoc.docs.t-head.cn/linuxbook/Chapter4/perf.html)  

> arch: yay linux-tools 选择 perf 进行安装

> [FlameGraph](https://github.com/brendangregg/FlameGraph)  `结合使用`  

## top
> 来源 procps, 用于查看 进程详细信息, CPU占用率 内存 网络等...

## smem
> Report memory usage with shared memory divided proportionally.  

## vmstat
> Report virtual memory statistics

- 最初是设计为查看虚拟内存的,现在常用于性能监测
- `vmstat 1 4` 输出信息,间隔1s 共4次 特别注意第一行数据是指开机以来的平均值,后面的才是当前值
    - procs 区域:
        - r 进程运行队列中的进程个数
        - b 处于不可中断的睡眠状态的进程个数
    - memory 区域:
        - swpd 虚拟内存使用量
        - free 空闲内存,不含buffer cache
        - buff 
        - cache
    - swap 区域:
        - si 每秒从交换分区写入内存的量
        - so 每秒从内存写入交换分区的量
    - io 区域:
        - bi 每秒从块设备读取的块数量
        - bo 每秒向块设备写入的块数量
    - system 区域:
        - in 每秒中断数(含时钟中断)
        - cs 每秒上下文切换次数 context switch
    - cpu 区域:
        - us 用户进程 cpu消耗时间百分比
        - sy 内核进程 cpu消耗百分比
        - id cpu空闲状态时间百分比
        - wa IO等待消耗时间百分比
        - st 虚拟管理程序占用时间百分比

- 更多参数用法:
    - `-a` 输出中,原来的 buff 和cache 被 inact 和 active 取代了
        - inact (inactive memory) 非活跃内存, 一段时间没有使用的内存(优先置换到交换分区的内存)
        - active 活跃内存, 正在被使用的内存
    - `-f` 查看启动以来创建的fork(或者称为task)总数
    - `-m` 展示内存 slabinfo
    - `-s` 展示内存指标以及系统事件
    - `-d` 展示各磁盘的统计信息
    - `-p /dev/sda1` 展示某一特定分区的 IO信息

- ![p135](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p135.jpg)
- ![p136](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p136.jpg)

> 但是数值大一点就会列错位，可以用column来格式化 `vmstat  1 5 | column -t` 但是等到执行完了才能看到结果，此时可以输出到文件里，看的时候格式化
> `vmstat  4 > run.log &` 然后 `less run.log | column -t` . 或者 `watch 'tail -n 20 run.log| column -t '`

> 安装： apk add procps， pacman -S procps-ng

## pidstat
> Report statistics for Linux tasks.

- 当使用vmstat发现cs值很高时可以查看是哪些进程引起的 `pidstat -w 5`

## mpstat
> 对多处理器的统计

- `mpstat -P ALL 1 1` 查询所有CPU信息,后两个参数是和vmstat一样的, `如果只看0号CPU 就ALL改成0即可`
    - 运行结果:
        - %user 用户进程 %
        - %nice 进程降级时CPU %
        - %sys 内核进程 %
        - %iowait 等待IO的CPU时间 %
        - %irq 处理系统中断 %
        - %soft 软件中断 %
        - %steal 虚机管理程序占用的 CPU %
        - %guest 运行虚拟处理器占用的CPU %
        - %idle CPU空闲时间
- 参数
    - `-I ` 值可选, SUM CPU ALL 
    - 分别表示 CPU总的中断数, 展示每一个CPU的中断数 SUM和CPU数据综合展示

## iostat
- 执行`iostat`输出信息:
    - 第一部分, 系统信息
    - 第二部分, CPU信息
    - 第三部分, 磁盘信息
- 参数:
    - -d 只显示磁盘信息,不显示CPU信息
    - -k 统计使用KB为单位
    - 最后两个数值参数和vmstat一样 例如`iostat -d -k 1 3`
    - 输出结果:
        - tps: 每秒进程的IO读写请求总数
        - KB_read/s, KB_wrtn/s 每秒读取,写入的字节数单位KB
        - KB_read, KB_wrtn 写入读取的总数
    - 同样的, 第一行数据是系统启动到现在的统计结果 `-y` 可以去除第一行
    - -x 显示更多信息

- ![p162](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p162.jpg)   
- ![p163](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p163.jpg)
- ![p164](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p164.jpg)

************************

## ifstat
> handy utility to read network interface statistics

- -a 全部统计信息
- -t sec 过去时间内流量信息

****************************

# 进程管理
> 按程序名字找到id `ps -ef | grep "$NAME" | grep -v "grep" | awk '{print $2}'`

## pidof
> find the process ID of a running program

- 查询ssh服务启动的进程的pid `pidof sshd`
- 找出shell脚本执行的pid, `pidof -x 脚本文件名`
- -s 只显示一个pid, 有的软件会有多个进程,就有多个pid
- 忽略指定的pid `-o pid`
- ![p167](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p167.jpg)

## pgrep 
> pgrep, pkill - look up or signal processes based on name and other attributes

1. pgrep java 查看Java `进程`

## sar
> Collect, report, or save system activity information.

**需要安装和启动 sysstat 服务 才能使用**

> [ksar](https://sourceforge.net/projects/ksar/)

- 默认持续执行除非Ctrl C退出,指定参数后就和vmstat一样 `sar 2 3` 
- 输出到指定文件中: `-o filename` 注意这个不是文本结构,是特殊的结构化方式, 查看需要 `sar -f filename`
- 多核的支持:`sar -P ALL 1 1 ` 与mpstat 大致相同
- 指定结束时间 `-e 18:00:00` 一般和 -o -f一起用
    - 搭配 -o 指定存储结束的时间点
    - 搭配 -f 指定从文件读取的数据的结束时间点

- 查看网络信息 -n 参数有: DEV EDEV SOCK FULL

- ![p172](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p172.jpg)
- ![p173](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p173.jpg)
- ![p174](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p174.jpg)
- ![p175](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p175.jpg)
- ![p176](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p176.jpg)

## lsof
> list open files  
> 这个命令使用时最好使用sudo或者root用户, 不然就会提示因权限问题导致显示信息不全  

1. `lsof -d 3` 查看打开标准错误输出的进程 (标准错误输出是3) `正在报错的进程`
1. `lsof file/dir` 查看打开某文件或目录(不关注子文件夹)的进程 
1. `sudo lsof -p pid` **通过进程查询打开的fd**
1. `sudo lsof -u username` 查看某一用户打开的文件 输出结果说明:
    - Command 进程名过长会简略显示, PID 进程标识符, USER 进程拥有者
    - FD 一般是文件描述符:
        - 两类: 一.文件描述符,二.描述文件特征的标识
        - 第一类:
            - 0 表示标准输入, 1 标准输出, 2 标准错误输出, n 其他文件描述符
        - 第二类:
            - cwd 应用程序的当前工作目录
            - txt 程序代码或是数据
            - mem 内存映射文件
            - pd 父目录
            - rtd 根目录
            - DEL 文件已经被进程删除, 但是还在内存中存在
    - TYPE 文件类型:
        - DIR 目录, REG 普通文件, CHR 字符类型, BLK 块设备
        - UNIX unix域套接字
        - FIFO 先进先出 pipe队列
        - IPv4/Ipv6 网络socket
    - DEVICE 磁盘的名称, SIZE 文件大小, NODE 索引节点(文件在磁盘上的标识), NAME 打开文件的确切名字

> socket使用情况

`lsof -Pni` 列出所有socket和 `netstat -pant` 类似
`lsof -i [4/6] [protocol][@hostname|hostaddr] [:service|port]`  按条件列出所有socket
- 4/6 IPv4/Ipv6
- protocol TCP/UDP 缺省TCP
- :service 服务名 可以多个 逗号分隔
- :port 端口 可以多个 逗号分隔

************************

- `lsof -i -a -p pid` 列出指定进程打开的socket
- `lsof +L1` 查看 已删除 但是**未被回收磁盘空间的文件**见下文删除文件

### 删除文件

> 真正删除文件
- 创建一个0填充的1g文件 `dd if=/dev/zero bs=1024 count=1000000 of=./1gb.file` 
    - 就能看到硬盘的被占用了1GB `df -h`
- 然后用一个简单的程序一直占用他, 例如 less
    - 删除`rm -f 1gb.file` 再 ls 下能发现文件不见了, 但是对硬盘的占用还在
    - 原因就是,Linux系统中, rm命令删除文件实际上只是减少文件的link数, 当link数为0时,文件才会被删掉。
    - 当进程打开某文件,该文件link就加1, 因为脚本一直占用着文件, 所以删除没有看到硬盘的占用下降,只是目录中找不到该文件而已
- `lsof | grep 1gb.file`或者 `lsof 1gb.file` 就能找到占用该文件的进程了,杀掉就能真正的删除文件了
    - 可以试试两个多个Python脚本同时占用, 那要将进程全部杀掉,才有用

> 恢复删除的文件 (前提是仍被其他进程引用)  

1. echo "1 2 3" >> test.log
1. less test.log `打开后不退出`
1. rm test.log
1. sudo lsof | grep test.log `找出持有该文件的进程id`
    > less      12008                    kcp    4r      REG                8,3        40239    4990940 /home/kcp/test/test.log (deleted)
1. ls -l /proc/12008/fd/ `查询持有的文件,找到对应的数字软链接,这里找到的是4`
1. cp /proc/12008/fd/4 test.log.save `复制回来`

## fuser
> identify processes using files or sockets  
> 和 lsof 功能差不多,但 fuser 是符合 POSIX 标准的命令 (POSIX:可移植操作系统接口)

- `fuser -v /path/to/sdk` 列出正在打开这个目录的进程(和lsof一样不关注子文件夹)
- 输出信息 详解:
    - USER 用户, PID 进程号, COMMAND 程序名
    - ACCESS 访问关系:
        - c 作为当前目录使用， e 作为可执行对象使用， r 作为根目录使用， s 作为共享库或其他装载对象 使用
        - m 作为映射文件或共享库使用，  f 打开文件, 默认不显示， F 打开文件,用于写操作 默认不显示

`常用选项`
1. -a 显示所有命令行中指定的文件，默认情况下被访问的文件才会被显示。 
1. -c 和-m一样，用于POSIX兼容。 
1. -k 杀掉访问文件的进程。如果没有指定-signal就会发送SIGKILL信号。 
1. -i 杀掉进程之前询问用户，如果没有-k这个选项会被忽略。 
1. -l 列出所有已知的信号名称。 
1. -m name 指定一个挂载文件系统上的文件或者被挂载的块设备（名称name）
    - 所有访问这个文件或者文件系统的进程都会被列出来。
    - 如果指定的是一个目录会自动转换成"name/",并使用所有挂载在那个目录下面的文件系统。 
1. -n space 指定一个不同的命名空间(space).这里支持不同的空间文件(文件名，此处默认)、tcp(本地tcp端口)、udp(本地udp端口)。
    - 对于端口， 可以指定端口号或者名称，如果不会引起歧义那么可以使用简单表示的形式
    - 例如：name/space (即形如:80/tcp之类的表示)。 
1. -s 静默模式，这时候-u,-v会被忽略。-a不能和-s一起使用。 
1. -signal 使用指定的信号，而不是用SIGKILL来杀掉进程。可以通过名称或者号码来表示信号(例如-HUP,-1),这个选项要和-k一起使用，否则会被忽略。 
1. -u 在每个PID后面添加进程拥有者的用户名称。 
1. -v 详细模式。输出似ps命令的输出，包含PID,USER,COMMAND等许多域,如果是内核访问的那么PID为kernel. -V 输出版本号。 
1. -4 使用IPV4套接字,不能和-6一起应用，只在-n的tcp和udp的命名存在时不被忽略。 
1. -6 使用IPV6套接字,不能和-4一起应用，只在-n的tcp和udp的命名存在时不被忽略。 
1. `-` 重置所有的选项，把信号设置为SIGKILL. 

- 查询占用端口 `fuser -v -n tcp 22` 或者 `fuser -v 22/tcp` fuser中含三种协议： file 默认, tcp, udp
    - 得到一些进程信息 `fuser -v -n tcp 0`
- 发送信号量 `fuser -v -k /home/kuang/sdk` 会把占用该文件夹的进程全部杀掉 (如果是ssh登录的服务器,当前目录就是这个的话, 会掉线)

## ps
> [参考: ps命令输出](http://www.cnblogs.com/lidabo/p/5505610.html) `输出的信息解释`

- 直接运行 `ps` 就会显示当前会话中的进程

- `ps aux` 显示系统中所有进程的状态信息 `可根据需要自由组合`
    - a 显示各终端(会话)上的所有进程, u 会展示进程所属用户, x 对于没有关联到终端运行的进程也展示出来
    - 输出列
        - VSZ
        - RSS
        - STAT
            - `D` 无法中断的休眠状态（通常 IO 的进程）； 
            - `R` 正在运行可中在队列中可过行的； 
            - `S` 处于休眠状态； 
            - `T` 停止或被追踪； 
            - `W` 进入内存交换 （从内核2.6开始无效）； 
            - `X` 死掉的进程 （基本很少见）； 
            - `Z` 僵尸进程； 
            - `<` 优先级高的进程 
            - `N` 优先级较低的进程 
            - `L` 有些页被锁进内存； 
            - `s` 进程的领导者（在它之下有子进程）； 
            - `l` 多线程，克隆线程（使用 CLONE_THREAD, 类似 NPTL pthreads）； 
            - `+` 位于后台的进程组；
- `ps aux`和`ps -aux`的区别:
    - 虽然执行结果看起来是一模一样的, 但是 `ps -aux ` 其实应该理解为 `ps -a -u x` 显示用户名为 x 的用户的所有进程
    - 当 x 用户不存在时ps就将其理解为 `ps aux`
    - 原因,因为他的三种格式:  BSD 选项前 不加短横线 `ps aux`  UNIX 选项前 加短横线 `ps -aux `  GNU 选项前 加双短横线  `ps --format`
    - BSD格式的 `ps aux` 等价于 `ps -eF`  e 显示全部进程, 包含了未在终端运行的进程 F 显示详尽的进程信息
    - Debian 上 `ps -ef` 和 `ps ef` 执行效果不一样

- `-o` 输出指定列 `ps -eo pid,user,cmd,start ... ` 更多需要查看手册 `man ps`
    - [p200](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p200.jpg)
    - 查看进程启动日期，时间，时间差 `ps -eo pid,start,lstart,%cpu,start_time,etime,cmd`

- 对范围进行筛选 
    - 根据用户 `ps -u root`
    - `ps -U root -u root u`
        - -U 实际用户 RUID 
        - -u 有效用户 EUID
        - u 按用户名和进程号的顺序来显示进程, 多列构成
    - 根据命令名称查找pid `ps -C sshd` 

> 排序 :  
- `ps aux --sort -pcpu/+pcpu/` 按CPU使用率,进行降序/升序排列  
- 多个条件 `--sort=+pcpu, -pmem` CPU升序,内存降序排列  

>查询线程信息:
- `ps -ef | grep mysql` 
- `ps -L pid` 显示某id的线程的具体信息 其中的LWP (轻量级进程, 可以理解为用户进程) Light Weight Process
    - `ps aux -L` 查看全部线程
- `ps -T pid` 显示 将-L的LWP替换为SPID (系统中的线程ID)
- 查看进程下的线程 `ps huH p pid`

> 进程树:  
- BSD格式 : `ps axjf` a 所有进程 x 显示没有控制终端的进程 j 任务格式显示进程  f ascaii字符显示树状结果  
- UNIX : `ps -ejH` e 显示所有进程  j 任务格式来显示进程  H 显示数状结构  

**实践**
1. 列出Java进程 `ps aux | grep RSS | grep -v "grep" && ps aux | egrep -v "grep" | grep -i java` 
1. 统计所有Java进程的内存 `ps aux | grep java | grep -v grep | awk '{sum+=$6};END {print sum "K " sum/1024"M "}'` 
    - `ps -a -x -o rss,comm | grep java | awk '{sum+=$1};END {print sum "K " sum/1024"M "}'`
1. 统计某个用户下进程所有内存 `ps -o pid,ppid,pgid,rss,comm  -u deployer | awk '{sum+=$4};END {print sum "K " sum/1024"M "}'`
1. 统计某个应用进程所有内存（自己和所有子进程） ` `

1. 按内存排序 列出所有进程 `ps aux | grep -v RSS | awk "{print $6 "\t" $11 }" | sort --human-numeric-sort -r | less`
1. 按实际执行的二进制命令展示 `ps -ely`

- [Difference Between Resident Set Size and Virtual Memory Size](https://www.baeldung.com/linux/resident-set-vs-virtual-memory-size)
    - RSS 驻留内存（共享库+堆+栈） 注意当前进程可能共用别的进程已加载的共享库，所以这部分内存是被重复计算了
    - VSZ 虚拟内存

### procs 
Rust 编写的 现代 ps

### pstree
> 顾名思义 树状图展示进程 线程关系

> [参考: Linux下查看线程数的几种方法汇总](https://www.cnblogs.com/yinzhengjie/p/9998771.html)  

************************

## kill
- `kill -l` 或者 `trap -l`： 输出kill命令可向进程发送的信号
    - kill是通过发送信号让进程自己决定做什么，而不是kill去做什么
    - 那要是有恶意屏蔽信号的进程怎么办？ `9号无法屏蔽`

- kill命令格式`kill [选项] [进程号]`
- 选项:
    - -l 列出所有的信号,如果-l后加上信号名称看到对应的数字,反之亦然
    - -s 可以指定发出的信号,等同于 -信号 向目标进程发送指定的信号类型
    - 缺省会发送默认的终止信号 **SIGTERM 15**
- 进程号:
    - 大于0: 向目标进程发送指定信号,多个逗号隔开
    - 等于0: 向当前进程组的所有进程发送信号
    - 等于-1: 向除kill进程和init进程(1)之外的所有进程发送信号
    - 小于-1: 向进程组对应的PGID的所有进程发送信号

> 常用信号量

| 信号名称 | 信号编号 | 说明
|:---:|:---:|:---|
|HUP  |1 | 终端会话断开，关闭所有其从属的子进程|
|INT  |2 | 中断 同`Ctrl+C` 结束前台进程,输入阻塞的程序应该退出(自己做清理)并清除阻塞状态|
|QUIT |3 | 退出 同`Ctrl+\` 也有点强制退出的意思|
|FPE  |8 | 发生算术运算错误时发出|
|KILL |9 | 强制终止 退出|
|TERM |15| 终止 程序自己做清理工作,然后退出 **缺省的信号值**|
|CONT |18| 继续 `fg/bg` 命令|
|STOP |19| 暂停/停止 同 `Ctrl+Z`|

> [中文释义：全部信号](https://wker.com/linux-command/kill.html) `或者直接 man kill`
- 9号信号:
    - 能对所有的进程起作用, 除了1号init进程
    - 副作用:进程运行中,突然终止,可能会导致系统资源无法释放, 数据没有同步到磁盘等情况(3号就好点)
    - 杀掉指定id（需要sudo）`kill -9 pid`
- 0号信号:
    - 测试信号,测试目标进程是否存在,测试是否具有向指定进程发送信号的权限

************************
`Tips`

> 例如 reids的服务端:  
- INT/TERM 信号就相当于在客户端的shutdown命令,是正常的退出  
- QUIT/KILL 信号是强制退出  
- STOP 信号就是暂停挂在后台  

>- 终结后台作业: 命令格式: `kill -信号 %作业号`  作业号就是运行`jobs`后方括号内数字  
>- dmesg 可以查看被Kill的进程的日志  

### killall
> 通过名字来发送信号,其他和kill是一致的

- 杀掉指定名字 不需要sudo `killall -9 name` 要十分谨慎的使用, 避免误杀进程

## trap
> 捕捉信号并响应
`trap "commands" signal-list`

> 用途
- 动态读取并更新配置文件
- 忽略信号对程序可能的影响 `trap "" 2`: 忽略 `Ctrl+C`
- 可以针对用户的退出操作做hook，询问用户是否真的确认要退出，或者关闭资源，清除临时文件等等

- 屏蔽信号
    - `trap "" INT` 屏蔽中断信号
    - `trap INT` 恢复

- 监控文件的变化，当按下快捷键Ctrl+C 就会执行trap中的命令
    ```sh
        #!/bin/bash
        trap 'echo "hello"' 2
        tail -f ~/.bashrc
    ```

************************

## 作业控制
> 在Linux中, 作业是由一个或多个进程构成的, 作业控制就是对作业的行为进行控制, 前后台的切换, 终止等操作

- 常用的操作:
    - 命令后的`&`: 让作业后台运行 作业如果是多个命令构成,会返回最后一个命令对应进程的pid和作业号
    - Ctrl Z: 作业转到后台并暂停 STOP状态
    - jobs: 列出当前作业列表
    - fg: 将一个作业切换到前台并运行
    - bg: 将一个作业切换到后台并运行
    - kill: 终止一个作业
- 前台和后台: 从标准输入读取用户输入, 标准输出展示数据, 后台就是脱离了标准输入和标准输出
    - fg bg 都是会发送具有继续执行的信号
    - 前台切换到后台:
        - `Ctrl Z` 切换到后台,但是会暂停的状态,可以使用`jobs`查看作业号
        - 再`kill -18 %作业` 或者 `bg %作业号`
    - 后台切回前台:
        - `fg %作业` 

`指定作业`

| 符号 | 含义 | 示例|
|:---|:---|:---|
| %Number  | 根据编号来指定作业 | fg %1 |
| %String  | 匹配命令以String开头的作业,如果匹配到多个就会报错 | kill %deng |
| %?String |命令行中含有String字符串的作业,如果是通过管道连接的多个命令,则仅匹配第一个命令| kill %?ng |
|  %%      |指代作业列表中最近一个被切换到后台的作业| kill %% |
|  %+      |和%%作用完全相同| kill %+ |
|  %-      |排在%%所指代的作业前面的那个作业| kill %- |

> 也就是说,这个匹配也是只能匹配一个作业,不能通配使用

## 守护进程
> 使得普通命令启动的进程变成类似于守护进程的工具

两种方案: 
- 让进程对hup信号免疫 nohup disown
- 让进程在新的会话中运行 setid screen

### nohup
- 在命令前 加上hohup 
    - 忽略所有hup信号 并将标准输出重定向到 nohup.out 若当前目录不可写，就会重定向到 $HOME/nohup.out 
- nohup 命令>result.txt 2>&1
    - `2>&1` 表示将标准错误(2)重定向到标准输出(1)
    - 将标准输出(1)重定向到 result.txt
    - 等同于 `nohup 命令>result.txt 2>/dev/null 1>&2 &`
    - 命令运行到后台， PID=$! 得到子进程ID
    - 得到ID后 通过执行这两条命令得到原命令的返回值`wait $PID` `echo $?`
    - 一般返回值就是原命令的返回值，但是特殊：
    - 125 nohup命令失败，并且POSIXLY_CORRECT环境变量没有设置
    - 126 指定命令能找到，但是不能调用
    - 127 找不到指定命令

### disown
- 执行中的命令，Ctrl+Z 暂停到后台去了 jobs查看作业编号
- `disown %作业号` 就能在后台运行，且屏蔽hup信号了

### setid
- 命令前 `setid 命令` 就会让进程在一个新的会话运行

### screen
> 在一个真实的终端运行多个伪终端，认为是开启了多个新会话 [命令参考](http://man.linuxde.net/screen)

- 会话恢复
    - 只要Screen本身没有终止，在其内部运行的会话都可以恢复。这一点对于远程登录的用户特别有用——即使网络连接中断，用户也不会失去对已经打开的命令行会话的控制。
    - 只要再次登录到主机上执行screen -r就可以恢复会话的运行。同样在暂时离开的时候，也可以执行分离命令detach，在保证里面的程序正常运行的情况下让Screen挂起（切换到后台）。这一点和图形界面下的VNC很相似。
- 多窗口
    - 在Screen环境下，所有的会话都独立的运行，并拥有各自的编号、输入、输出和窗口缓存。用户可以通过快捷键在不同的窗口下切换，并可以自由的重定向各个窗口的输入和输出。Screen实现了基本的文本操作，如复制粘贴等；
    - 还提供了类似滚动条的功能，可以查看窗口状况的历史记录。窗口还可以被分区和命名，还可以监视后台窗口的活动。 会话共享 Screen可以让一个或多个用户从不同终端多次登录一个会话，
    - 并共享会话的所有特性（比如可以看到完全相同的输出）。它同时提供了窗口访问权限的机制，可以对窗口进行密码保护。

| verb | param | comment |
|:----:|:----:|:----|
|-A | 　        |  将所有的视窗都调整为目前终端机的大小。 
|-d | <作业名称> |　将指定的screen作业离线。 
|-h | <行数> 　  |指定视窗的缓冲区行数。 
|-m | 　        | 即使目前已在作业中的screen作业，仍强制建立新的screen作业。 
|-r | <作业名称>| 　恢复离线的screen作业。 
|-R | 　|先试图恢复离线的作业。若找不到离线的作业，即建立新的screen作业。 
|-s | 　|指定建立新视窗时，所要执行的shell。 
|-S | <作业名称> |　指定screen作业的名称。 
|-v | 　|显示版本信息。 
|-x | 　|恢复之前离线的screen作业。 
|-ls或--list | |　显示目前所有的screen作业。 
|-wipe |　| 检查目前所有的screen作业，并删除已经无法使用的screen作业。

## IPC
> 进程间通信: 管道/信号量/共享内存/Socket

****************
# 系统管理
## uname 
- `uname -a` 输出所有信息
    - -s 内核名称
    - -n 主机名称
    - -r 内核发行版号
    - -v 操作系统具体版本
    - -m 机器硬件名称
    - -p 处理器名称
    - -i 硬件平台名称
    - -o 操作系统名称

## who
- `who` 和 `w`  who是按照不同tty来显示信息
    - 查看系统的真实用户，
    - 例如当普通用户 使用su 切换用户，这条命令就显示了真正的用户，而不是su切换后的用户

- `whoami` 查看有效用户，就是当前会话的拥有者
- `groups` 查看所有组

## service
- `service 服务名 status/start/stop/restart`
-  查看所有service掌控的服务 `cd /etc/init.d/ && ls -F`

- `which service` 结果显示这是个脚本 
- `service 服务名 stop` 等价于 `/etc/init.d/服务名 stop`

## chkconfig
> 掌控等级制度 LSB 

## dmidecode 
> 输出机器的 BIOS CPU 内存等硬件信息 （DMTF DMI）

- 运行 `dmidecode -t `就会提示你后接类别

## lsmod
> Show the status of modules in the Linux Kernel

## chroot
> change root directory 更改root目录 最古老的容器技术

- `mkdir 目录 ` 复制相关目录过来，就能把系统迁移过来了
- ![p262](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p262.jpg)
- ![p263](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p263.jpg)
- ![p264](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p264.jpg)
- ![p265](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Linux_DaPeng_mingling100/p265.jpg)

# 关机/重启
> shutdown | reboot | halt | poweroff | init

|命令|作用|
|:---|:---|
|shutdown | 可用于关机，重启，支持定时和通知|
|reboot   | 重启系统|
|halt     | 停止系统|

