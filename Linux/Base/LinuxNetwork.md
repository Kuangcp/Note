---
title: Linux网络管理
date: 2018-12-15 11:15:55
tags: 
    - 基础
    - 网络
categories: 
    - Linux
---

💠

- 1. [Linux网络管理](#linux网络管理)
    - 1.1. [内核配置](#内核配置)
    - 1.2. [DNS](#dns)
        - 1.2.1. [nslookup](#nslookup)
        - 1.2.2. [dig](#dig)
        - 1.2.3. [修改DNS](#修改dns)
    - 1.3. [Route](#route)
        - 1.3.1. [traceroute](#traceroute)
    - 1.4. [IPv4和IPv6](#ipv4和ipv6)
    - 1.5. [Bridge](#bridge)
    - 1.6. [Socket](#socket)
    - 1.7. [TCP/UDP 工具](#tcpudp-工具)
        - 1.7.1. [进程和端口互查](#进程和端口互查)
        - 1.7.2. [tcpdump](#tcpdump)
    - 1.8. [复合工具](#复合工具)
        - 1.8.1. [ping](#ping)
        - 1.8.2. [tc 流量控制](#tc-流量控制)
        - 1.8.3. [netstat](#netstat)
        - 1.8.4. [iproute2](#iproute2)
        - 1.8.5. [nmap](#nmap)
        - 1.8.6. [netcat](#netcat)
        - 1.8.7. [scp](#scp)
        - 1.8.8. [rsync](#rsync)
        - 1.8.9. [curl](#curl)
        - 1.8.10. [wget](#wget)
- 2. [证书](#证书)
    - 2.1. [自签发证书](#自签发证书)
- 3. [常用服务](#常用服务)
    - 3.1. [邮件服务器](#邮件服务器)
    - 3.2. [FTP](#ftp)
        - 3.2.1. [客户端](#客户端)
            - 3.2.1.1. [命令行](#命令行)
            - 3.2.1.2. [Java](#java)
        - 3.2.2. [服务端](#服务端)
            - 3.2.2.1. [ftpserver](#ftpserver)
            - 3.2.2.2. [vsftpd](#vsftpd)
    - 3.3. [SSH](#ssh)
    - 3.4. [Telnet](#telnet)
    - 3.5. [VPN](#vpn)
        - 3.5.1. [tun/tap](#tuntap)
        - 3.5.2. [shadowsocks](#shadowsocks)
        - 3.5.3. [OpenVPN](#openvpn)
        - 3.5.4. [Fortivpn](#fortivpn)
    - 3.6. [代理](#代理)
        - 3.6.1. [proxychains](#proxychains)
    - 3.7. [防火墙](#防火墙)
        - 3.7.1. [iptables](#iptables)
            - 3.7.1.1. [四层协议端口转发](#四层协议端口转发)
    - 3.8. [远程桌面](#远程桌面)
        - 3.8.1. [VNC](#vnc)
        - 3.8.2. [Xrdp](#xrdp)
- 4. [Tips](#tips)

💠 2024-09-29 23:35:37
****************************************
# Linux网络管理

> [计算机网络基础](/Skills/Network/Network.md)

## 内核配置
> ip_local_port_range [Linux increase ip_local_port_range TCP port range](https://ma.ttias.be/linux-increase-ip_local_port_range-tcp-port-range/)

> [参考: Linux查看网络流量](https://tlanyan.me/linux-traffic-commands/)

iftop

- nethogs `流量监控`
- slurm 网卡带宽监控

************************

## DNS
> [Github: dns topic](https://github.com/topics/dns)
> [DnsServer](https://github.com/TechnitiumSoftware/DnsServer)

### nslookup
> 来自 dnsutils 包

快速使用 `nslookup jd.com 223.5.5.5`

- `nslookup - 8.8.8.8` 进入 REPL 方便调试, 8.8.8.8 是Google开放的DNS 备选 8.8.4.4
    - 结果解释：Non-authoritative answer: 表示这是从缓存得到的结果，不一定准确
    - Server：上连DNS服务器的IP， Address：`上连DNS的IP#端口` 通常是53
    - canonical name 即CNAME 别名

### dig
> 比 nslookup 更强大 **Domain Information Groper**

快速使用 `dig @8.8.8.8 www.baidu.com` 

> dig [option] @8.8.8.8 www.baidu.com
- @xxx 指定DNS服务器
- -p 53 指定DNS服务器端口
- +tcp 采用TCP进行DNS通信（默认UDP）
- +short 精简输出
- +nocmd+nocomment+nostat 输出最核心内容
- -p 

`dog` 类似dig

- `drill`
    - [doc](https://linux.die.net/man/1/drill)

- `host`
    - host domain

- `whois`
    - 查询域名详细信息
- `nali` [Github](https://github.com/zu1k/nali)

***************************

### 修改DNS
- 在 `/etc/resolv.conf` 中添加Google的DNS (阿里云 DNS 223.5.5.5 223.6.6.6)
```
    nameserver 8.8.8.8 
    nameserver 8.8.8.4
```

> 刷新本地缓存
1. sudo /etc/init.d/nscd restart 或者 service nscd restart , 其实就是重启 nscd 服务

**********************

## Route
> [参考: 路由表的建立算法和有关的刷新协议](https://blog.csdn.net/qq_34328833/article/details/60583183)

> [Linux-router](https://github.com/garywill/linux-router)`Linux作为路由器`

### traceroute
> 显示网络数据包传输到指定主机的路径信息，追踪数据传输路由状况

- `traceroute [选项] [远程主机名或IP地址] [数据包大小]`
    - -i<网络接口>	:	使用指定的网络接口发送数据包
    - -n	:	直接使用IP地址而不使用主机名
    - -v	:	详细显示命令的执行过程
    - -w<超时秒数>	:	设置等待远程主机回应的时间
    - -x	:	开启或者关闭对数据包的正确性校验
    - -s<来源IP>	:	设置本机主机发送数据包的IP地址
    - -g<网关地址>	：	设置来源的路由网关，最多可设置8个

1. `traceroute -I stackoverflow.com` icmp 查看路由表

> [NTrace-core ](https://github.com/nxtrace/NTrace-core)`可视化`

************************

## IPv4和IPv6
- IPv4 只有32bit IPv6 有128bit

`IPv6`
- 零省略 ：如果有一位是 000C 可以直接写C
- 零压缩 ：如果FE04:0:0:0:0:0:0:DA 写成 FE::DA

## Bridge
> 网桥, 通常使用 bridge-utils 的 brctl 进行管理

- [ ]  Learn 

**增加**

**删除**

**配置开机启动**

## Socket 
一个socket的五个必要元素： client_ip:client_port<----->server_ip:server_port + 协议

`/etc/sysctl.conf`
动态端口范围： net.ipv4.ip_local_port_range=32788 60000 `修改时不能超过[1024,65535]范围`

***************************
## TCP/UDP 工具

- [TCP 内网下载慢速分析](https://christmica.cc/archives/tcp-download-analysis)

- 强制关闭tcp连接： killcx tcpkill
- `iperf3`： TCP UDP 测速， 在两个节点上使用iperf启动服务端和客户端进程，从而计算TCP和UDP指标信息 [Ethr](https://github.com/microsoft/ethr) Golang 仿写


### 进程和端口互查
> netstat lsof fuser  

> [参考: linux下常用命令查看端口占用](http://blog.csdn.net/ws379374000/article/details/74218530)

- `lsof -i:端口号` 用于查看某一端口的占用情况，缺省端口号显示全部
    - 或者 `cat /etc/services` 查看系统以及使用的端口
- 查询占用端口 `fuser -v -n tcp 22` 或者 `fuser -v 22/tcp` fuser中含三种协议： file 默认, tcp, udp
    - 得到一些进程信息 `fuser -v -n tcp 0`

- whatportis 可以通过服务查询默认端口，或者是通过端口查询默认服务的工具

************************

### tcpdump
- `tcpdump -i eth0 -nn -X 'port 53' -c 1` root用户才有运行权限
    - -i 指定监听的网络接口（网卡）
    - -nn 将协议号或端口号，显示数字，而不是名称例如：21 而不显示 FTP
    - -X 将协议头和包内容完整的显示出来
    - port 53 过滤，只显示53端口相关的包
    - -c 抓包的数量
    - -e 输出以太网帧头部信息输出 （能看到mac地址）
    - -l 输出变为行缓冲
    - -t 输出不打印时间戳
    - -v 输出更详细信息
    - -F 指定过滤表达式所在的文件
    - -w 将流量保存到文件中
    - -r 读取raw packets 文件

- 列出可以选择的抓包对象 `tcpdump -D`（USB设备也能抓？）

************************

## 复合工具
> 参考书籍 《Linux 大棚命令百篇》

### ping
> inetutils-ping ICMP protocol

- ping URL ： Linux是默认无休止的
    - -c 次数
    - -q 安静模式 不输出
    - -s 默认64字节
    - -t 设定 TTL值，Linux默认是64或255 经过一个路由器就会减一
    - -i 每次ping的时间间隔 默认1s root用户才可以设置 0.2 以下
    - -f 暴力尽可能大量包的传送 至少每秒100个
        - 注意：得到的结果中的 mdev 表示ICMP包的RTT偏离平均值的程度，mdev 越大表示网速不稳定 Linux有，mac下叫stddev win系列没有
    - -r 记录经过的路由 （路由节点均支持ICMP协议）

> [prettyping](http://denilson.sa.nom.br/prettyping/)  
> [gping](https://github.com/orf/gping)  

- ping -s 1472 -M do 192.168.15.205 测试网络环境下最大可用MTU
- [Github: tcping](https://github.com/pouriyajamshidi/tcping) `测试tcp连接延迟`

### tc 流量控制
> Traffic Control

- 限速 `tc qdisc add dev eno1 root tbf rate 400kbit latency 1ms burst 1000`
- 解除 `tc qdisc del dev eno1 root tbf rate 400kbit latency 1ms burst 1000`
    - tbf : 令牌桶算法

- 网卡100%丢包 `tc qdisc add dev enp3s0 root netem loss 100%` 移除限制： add 换成 del
- 移除指定网卡添加的所有规则 `tc qdisc del dev enp3s0 root`
- 指定IP网段 丢包 
```sh
    #! /bin/sh
    interface=enp3s0
    ip=192.168.16.0/24
    delay=30ms
    loss=90%

    tc qdisc add dev $interface root handle 1: prio
    # 此命令立即创建了类: 1:1, 1:2, 1:3 ( 缺省三个子类 )
    tc filter add dev $interface parent 1:0 protocol ip prio 1 u32 match ip dst $ip flowid 2:1
    # 在 1:1 节点添加一个过滤规则 , 优先权 1: 凡是去往目的地址是 $ip( 精确匹配 ) 的 IP 数据包 , 发送到频道 2:1.
    tc qdisc add dev $interface parent 1:1 handle 2: netem delay $delay loss $loss
```

> [wondershaper](https://github.com/magnific0/wondershaper)

### netstat 
> 相关 [iproute2](#iproute2)

- `netstat -tunlp | grep 端口号` 用于查看指定的端口号的进程情况
- 参数
    - `-p` 显示建立相关连接的程序名和PID **需要root**
    - `-a` 显示本机所有连接和监听端口
    - `-n` 以网络IP地址的形式显示当前建立的有效连接和端口
    - `-r` 显示路由表信息
    - `-s` 显示协议的统计信息。
    - `-v` 显示当前的有效连接
    - `-t` 显示所有的TCP协议连接情况
    - `-u` 显示所有的UDP协议连接情况
    - `-c<秒数>` 后面跟的秒数，表示每个几秒就刷新一次显示
    - `-i` 显示自动配置接口的状态
    - `-l` 仅显示连接状态为“LISTEN”的服务的网络状态

- `netstat -an|awk '/tcp/ {print $6}'|sort|uniq -c| sort -hr` 查看TCP状态和数量

************************

### iproute2
> 代替 netstat ifconfig 的强大工具 [基于iproute命令集配置Linux网络](https://cloud.tencent.com/developer/article/1183389)

|   用途       | net-tool |     iproute2     |
| :-----      | :------  | :--------------  |
| 地址和链路配置 | ifconfig |  ip addr/link   |
|   路由表     |  route   |     ip route     |
|  ARP表       |   arp    |     ip neigh     |
|  VLAN       | vconfig  |     ip link      |
|   隧道       | iptunnel  |    ip tunnel    |
|   组播       | ipmaddr   |     ip maddr    |
|   统计       | netstat   |        ss       |

`net-tools 和 iproute 对应关系`

|      作用           |               net-tools用法                |                iproute2用法
| :----------        | :-------------------------------------- | :-------------------------------------- |
|  展示本机所有网络接口 |                 ifconfig                 |             ip link
| 开启/停止某个网络接口 |          ifconfig ech0 up/down           |           ip link set eth0 up/down
| 给网络接口设置/删除IP | ipconfig eth0 10.0.0.0.1/24 / ifconfig eth0 0 |   ip addr add/del 10.0.0.1/24 dev eth0
| 显示某个网络接口的IP  |              ifconfig eth0               |          ip addr show dev eth0
|    显示路由表        |                 route -n                 |              ip route show
|   添加删除默认网关    | route add/del default gw 192.168.1.2 eth0 | ip route add/del via 192.168.1.2 eth0 <br/> ip route replace default via 192.168.1.2 dev eth0
|    添加ARP          |  arp -s 192.168.1.100 00:0c:29:c5:5a:ed  | ip neigh add 192.168.1.100 lladdr 00:0c:29:c5:5a:ed dev eth0
|    删除ARP          |           arp -d 192.168.1.100           |   ip neigh del 192.168.1.100 dev eth0
|   展示套接字状态      |                netstat -l                |                  ss -l

- 默认网关： 如果主机找不到转发规则， 就把数据包发给默认的网关(家用网络一般是路由器的ip)
- 增加/删除一条路由规则 `ip route add/del 192.168.2.0/24 via 192.168.1.254`
    - 当使用 VPN 时，建立新的虚拟网卡 tun， 可以手动设置路由让指定ip走虚拟网卡 从而访问到VPN内局域网地址(网络号和真实网卡一样，默认会把数据包转发至本地局域网)
- 设置网卡 eno1 MAC 地址`ip link set eno1 address b4:xx:xx`

- 关闭 启用 `ifconfig name down/up`
- 修改IP `ifconfig eth0 192.168.1.200/24`

************************
_iproute-ss_

> [参考: Linux网络状态工具ss命令使用详解](http://www.ttlsa.com/linux-command/ss-replace-netstat/)

- 查看网络连接统计 `ss -s`
- 查看打开的端口 `ss -l`
- 查看打开的端口以及进程pid `ss -pl`
- 查看所有socket连接 `ss -a`
- 隧道术： 网络协议的数据包被封装在另一种网络协议的数据包之中 `这是VPN的技术理论基础`
- 按指定端口过滤 `ss -at '( dport = :3308 )'`

************************

### nmap

> 按主机扫描端口

> [参考博客](http://aaaxiang000.blog.163.com/blog/static/2063491220113284325531/)

- 主机扫描
  - nmap -sS 192.168.1.1   　//TCP、SYN扫描,使用最多，最快 `无参数扫描默认添加-sS参数`
  - nmap -Pn 192.168.1.1  　 //当目标主机禁ping时使用，假设主机存活扫描端口（耗时长）
  - nmap -p- 192.168.1.1  　 //扫描目标主机全部端口
  - nmap -sP 192.168.1.1   　//只对目标进行ping检测，快速
  - nmap 192.168.1.1/24   　 //对网段进行扫描

- 进阶用法
  - nmap -V 192.168.1.1    //显示扫描细节
  - nmap -A 192.168.1.1    //综合扫描
  - nmap -sT 192.168.1.1   //进行tcp扫描
  - nmap -sU 192.168.1.1   //进行udp扫描
  - nmap -sV 192.168.1.1   //对目标上的服务程序版本进行扫描
  - nmap -T4 192.168.1.1   //设置扫描速度1~5
  - nmap -sn 192.168.1.1   //相比sP检验存活使用更多方式
  - nmap -O 192.168.1.1    //对目标主机的操作系统进行扫描（-A获得更多信息）
  - nmap --data-length:55 192.168.1.1 //添加垃圾数据避免nmap被识别
  - nmap -D IP1,IP2... IP   //发送参杂着假ip的数据包检测

- 使用环境
  - 扫描网段存活IP：nmap -sP 192.168.1.1/24
  - 扫描所有端口开放情况：nmap -sS -p 1-65535 192.168.1.1
  - 当目标主机禁ping时：nmap -Pn 192.168.1.1
  - 当目标可能存在waf拦截时：nmap -sS --data-length:55 192.168.1.1
  - 尽可能收集目标主机信息：nmap -p 1-65535 -sV -A -V 192.168.1.1

> 按端口扫描 

masscan  
Zmap `在千兆网卡状态下，45 分钟内扫描全网络 IPv4 地址`


### netcat
> sudo apt install netcat  

- 监听端口 `nc -l 11044`
    - 建立连接 `nc 127.0.0.1 11044` 任一方退出 netcat 就终止了该连接

- 端口扫描 `nc -z -v -n -w 2 127.0.0.1 20-33` 扫描22-33端口
    - -z 一旦连接立马断开，不发送接收任何数据
    - -v 输出详细信息
    - -n 直接使用IP地址，不使用域名服务器来查询其域名
    - -w 设置连接超时时间 s
    - -u 使用UDP 默认缺省则是TCP
- 连接开放的端口 `nc -v host port`

- 传输文件 
    - 服务端发送文件 `nc -v -l -p port < temp_out.md`
    - 客户端接收文件 `nc -v -n host port > temp_in.md`
    - *注意*  仅单次连接，传输完毕自动断开, 没有进度提示,大文件也不支持。也可以服务端接收文件客户端发，将 `< >` 互换即可

- 传输文件夹 
    - 服务端 `tar -cvPf - /root/book/ | nc -l 12345`
    - 客户端 `nc -n host port | tar -xvPf -`
    - 这是未压缩的， 压缩再加上参数即可 例如 `gzip -czvPf -xzvPf`

### scp
> scp命令用于在Linux下进行远程拷贝文件的命令，和它类似的命令有cp，认证用的是ssh 所以也能使用sshpass

```
    -1：使用ssh协议版本1； 
    -2：使用ssh协议版本2； 
    -4：使用ipv4； 
    -6：使用ipv6； 
    -B：以批处理模式运行； 
    -C：使用压缩； 
    -F：指定ssh配置文件； 
    -l：指定宽带限制； 
    -o：指定使用的ssh选项； 
    -i: 指定私钥文件
    -P：指定远程主机的端口号； 
    -p：保留文件的最后修改时间，最后访问时间和权限模式； 
    -q：不显示复制进度； 
    -r：以递归方式复制。
```
- 远程到本地 `scp root@10.10.10.10:/opt/soft/nginx-0.5.38.tar.gz /opt/soft/`
- 本地到远程 `scp /opt/soft/nginx-0.5.38.tar.gz root@10.10.10.10:/opt/soft/scptest`

> 注: scp rcp wget rsync 几种传输文件的方式

### rsync 
> 同步命令 (个人倾向于本地和远程， 书上称为源端和目的端)  [命令参数详解](http://man.linuxde.net/rsync) | [本地和VPS0之间同步数据](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps)

- 同步到 `rsync file user@host:path` 上， 是将这里的file文件覆盖远程的目录下的file文件，不像git那样
    - 同步当前目录 将file 换成 \`ls\`
    - -t 不加该参数：不会同步文件的修改时间，采用的`quick check策略`。使用后：让修改时间也同步，如果修改时间一致，就不同步（它不考虑文件内容，这是个坑）。
    - -I 就能解决上面的问题，每个文件都进行同步，代价是速度慢
    - -v 输出更多信息 v可以多个，v越多输出的日志信息也越多
    - -r 文件夹递归同步，这种是采用`上面的I策略`的
    - -l 同步软链接文件，默认是忽略该类文件的
    - -L 同步软链接文件及其目标文件
    - -z 压缩数据，提高传输速度
    - -p 缺省该参数时，如果远程没有该文件，权限会和本地的文件一致， 如果远程已经有该文件，权限和本地的不同， 那么命令不作更改。使用参数后，就会让权限尽力保持一致
    - -a 这个命令等价于 -rlptgoD 归档选项，采用递归方式，尽可能保持各方面的一致，但是不能同步硬链接，得加上 `-H`

- 只要文件不一样，就会触发同步，该命令确保远程的是和本地的一致，本地的直接覆盖远程的   
- 只要rsync命令对本地有读权限，对远程有写权限，就能确保目录是一致的
- rsync只能以登录远程的账号来创建文件，它不可能将文件的组信息，用户信息也一致，除非是root用户可以做到

**【其他特别参数】**
- `--delete` 如果本地没有该文件 远程就会删掉
    - `--delete-exclude `删除远程指定的文件
    - `--delete-after` 默认是先清理远程文件再同步，使用该选项就相反了先同步再删除需要删除文件
    - 例如 `mkdir blackdir && rsync -a --delete blackdir/ test/` 删除目录内大量小文件时相较rm速度更快

- `--exclude` 排除掉某些文件不同步 可以使用多次
    - `--excule-from` 如果要排除的文件很多，可以将文件名放在一个文本文件里，然后使用该选项读取该文件
- `--partial` 断点续传 可以简写-P
- `--progress` 显示传输进度信息

************************

### curl
> [Official site](https://curl.haxx.se/)

1. 不输出，重定向到*黑洞设备*  ` curl -s -o /dev/null URL`
1. 使用基础认证 发送JSON数据 `curl -i -H "Content-Type:application/json" -u admin:secret -X POST --data '{"title":"1","content":"1"}' http://tomcat.kcp/email/content`
    - 如果没有认证则会收到 401 返回码

- 使用Cookie `curl -v --cookie "USER_TOKEN=Yes" http://127.0.0.1:5000/`
- 使用代理  `-x, --proxy [protocol://]host[:port]`
- 设置 Header `-H "xxx:xxx"` 例如 `-H "Content-Type:application/json" -H "token:xxx"`
- 设置POST请求 body `-d '{"title":"1","content":"1"}'`
    - 本地文件 `-d '@data.json'`
- 上传文件 `curl -X POST -H "Content-Type: multipart/form-data" -F "file=@index.html" URL` 

> [参考: curl返回常见错误码](http://www.cnblogs.com/wainiwann/p/3492939.html)
- [56错误码](https://stackoverflow.com/questions/10285700/curl-error-recv-failure-connection-reset-by-peer-php-curl)
> [参考: 使用cURL和用户名和密码？](http://www.cnblogs.com/seasonzone/p/7527218.html)

- httpie `python`
- curlie
- [bat](https://github.com/astaxie/bat) `go`
- [xh](https://github.com/ducaale/xh)`rust`
- [hurl](https://github.com/Orange-OpenSource/hurl)`rust` IDEA中Http插件一样，按HTTP协议写脚本 hurl运行

************************

### wget
> 特性和优势：支持 HTTP HTTPS FTP协议  
>1. 能够跟踪 HTML 和 XHTML 即可以下载整站，但是注意wget会不停的去下载HTML中的外链，无休无止  
>1. 遵守 robots.txt 标准的工具  
>1. 支持慢速网路和不稳定的下载，当下载失败就会不断重试，直到下载成功  
>1. 支持断点续传  

- wget 配置文件 `/etc/wgetrc` `~/.wgetrc` 两个文件配置（区别是全局和当前用户）wget的默认行为

- 例如 -X配置：`wget  -X js,css URL` 排除两个文件夹不下载
    - 如果要默认排除，到`.wgetrc`文件里配置 `exclude_directories=js,css` 
    - 这时候就出了一个问题，你不知道配置文件的情况时，发现总有目录下载不下来，就可以排除两个文件的作用：
    - `wget -X '' -X js,css URL`
    - 注意：`-X`，两个配置文件。这三者的配置，wget是取并集的， 使用了`-X ''` 后就只看后面的`-X 参数`   

- 参数:
    - 目录下载 `-r` 递归选项
    - 后台下载 `--background` 即使 你Ctrl D/exit也不会中断执行
    - `-o` 指定日志输出。默认当前目录的 wget-log
    - `--content-disposition` 支持HTTP Content-Disposition标头，通常包含文件名信息
    - `-O` 将下载的所有文件的内容追加到指定的文件
    - `-c` 断点续传 但是有潜在问题, 例如当源站的文件头部分或者已下载部分修改了，但wget只从上次下载的进度开始继续下载
    - 避开robots.txt 协议 `--execute robots=off`
        - 尝试使用 Tomcat 构建一个有robots协议的网站，然后wget还是绕过了协议
        - 对 Github 测试这个参数是正常的
    
    - 简化wget获取到的文件
        - -nH 去除wget将域名作为文件夹的情况,只得到域名下相对路径的文件
        - --cut-dirs=number 去除前缀路径 
        - 只用 `-r` : URL:a/b/c/
        - `-r` 再用上 `--cut-dirs=1` : URL:/b/c/
        - `-r` 再用上 `-nH` :a/b/c/
        - `-r` 再用上 `-nH --cut-dirs=1` : /b/c/
        - `-r` 再用上 `-nH --cut-dirs=2` : /c/
    
    - 平铺,不使用源站的目录结构: `-nd` 若有重名文件,自动重命名
    - 强制多层次文件夹 `-x` 例如:github.com/a/b/ --> github/com/a/b/
    - 协议命名的根文件夹 `--protocol-directories` 例如 ftp://baidu.com/a/b/
    - 自动重试 `--tries=number` 设置下载失败后重试的次数    
    - 拒绝重复下载同名文件,即使这个文件不是最新的 `-nc`, wget会先比较时间戳,然后下载,且多次下载同名文件会自动添加 .1 .2 这样的后缀
    - 自动分析是否下载同名文件, `-N` 会考虑时间戳以及文件大小,但是不能和 -nc 同时设置
 
    - 限速 `--limit-rate=N` 默认单位是b,可以指定单位 k m
        - 这个限速的实现原理是通过在进行一次网络读取后,就线程睡眠一会儿,将速度降下来,如果下载是超小文件就可能无法达到限速的效果  
    - 限制频率 -w 即 `--wait=seconds` 可以指定 m h d 等单位,效果是每两个请求间隔指定时间
    - 请求重试 `--waitretry` 设置请求重试的秒数, 如果设置的是10秒, 第一次失败后就会等1s,然后第二次失败就等2s...直到递增到10s,然后结束
        - 其效果 其实应该是 设置值的累加 (理解为重试次数似乎更好)
    
> [wget cookie](http://blog.csdn.net/adream307/article/details/47379149)  
> [参考: wget命令详解](http://blog.csdn.net/RichardYSteven/article/details/4565931)


- 镜像整站 `wget --mirror -p --convert-links -P . URL`
    - –miror: 镜像下载
    - -p: 下载所有为了html页面显示正常的文件
    - –convert-links: 下载后，转换成本地的链接
    - `-P .`： 保存所有文件和目录 到当前目录

- 镜像SPA等使用了前端动态路由的网站 `wget --mirror -w 2 -p --html-extension --tries=3 -k -P stackperl.html "https://docs.egret.com/uieditor/docs/api/eui/eui.AddItems"`
    - 但是下载后无法正常使用子页面，还需要web服务器处理应用动态路由到静态资源文件上去 有点麻烦
    - [参考: how-do-i-completely-mirror-a-web-page](https://stackoverflow.com/questions/400935/how-do-i-completely-mirror-a-web-page)  

- 获取API返回数据 `wget -q url -O -`

************************

> [axel](https://github.com/axel-download-accelerator/axel)  
> [aria2](https://github.com/aria2/aria2)  

************************

# 证书

## 自签发证书
```sh
  ############ 证书颁发机构
  # CA机构私钥
  openssl genrsa -out ca.key 2048
  # CA证书
  openssl req -x509 -new -key ca.key -out ca.crt
  ############ 服务端
  # 生成服务端私钥
  openssl genrsa -out server.key 2048
  # 生成服务端证书请求文件
  openssl req -new -key server.key -out server.csr
  # 使用CA证书生成服务端证书  关于sha256，默认使用的是sha1，在新版本的chrome中会被认为是不安全的，因为使用了过时的加密算法。
  openssl x509 -req -sha256 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -days 3650 -out server.crt    
  # 打包服务端的资料为pkcs12格式(非必要，只是换一种格式存储上一步生成的证书) 生成过程中，需要创建访问密码，请记录下来。
  openssl pkcs12 -export -in server.crt -inkey server.key -out server.pkcs12
```

> Manjaro 导入自定义证书

sudo trust anchor --store my-root.crt
sudo update-ca-trust

****************************
# 常用服务

## 邮件服务器

postfix和devecot

************************

## FTP

### 客户端
#### 命令行
> [FTP Commands](https://www.javatpoint.com/ftp-commands)

#### Java
> [Apache Commons Net](https://commons.apache.org/proper/commons-net/)

### 服务端

> [sftp](https://hub.docker.com/r/atmoz/sftp/)  
> [Filezilla](https://filezilla-project.org/)`服务端&客户端`  

#### ftpserver
> [ftpserver](https://github.com/fclairamb/ftpserver)`Golang`

#### vsftpd

- `sudo apt-get install vsftpd -y`
- `sudo systemctl start vsftpd.service`
- 创建用户 `sudo useradd -d /home/uftp -s /bin/bash uftp`
- 设置密码 `sudo passwd uftp`
- 删除掉 pam.d 中 vsftpd，因为该配置文件会导致使用用户名登录 ftp 失败：`sudo rm /etc/pam.d/vsftpd`
- 限制用户 uftp 只能通过 FTP 访问服务器，而不能直接登录服务器 `sudo usermod -s /sbin/nologin` uftp
- 修改配置文件 `sudo chmod a+w /etc/vsftpd.conf`

`/etc/vsftpd.conf `
```conf
    # 限制用户对主目录以外目录访问
    chroot_local_user=YES
    # 指定一个 userlist 存放允许访问 ftp 的用户列表
    userlist_deny=NO
    userlist_enable=YES
    # 记录允许访问 ftp 用户列表
    userlist_file=/etc/vsftpd.user_list
    # 不配置可能导致莫名的530问题
    seccomp_sandbox=NO
    # 允许文件上传
    write_enable=YES
    # 使用utf8编码
    utf8_filesystem=YES
```
1. 新建文件 sudo touch /etc/vsftpd.user_list
1. 修改权限 `sudo chmod a+w /etc/vsftpd.user_list`
1. 添加用户名 `uftp`
1. 设置用户目录只读 `sudo chmod a-w /home/common`
1. 新建公共目录 设置权限 `mkdir /home/common/public && sudo chmod 777 -R /home/common/public`
1. 重启服务 `sudo systemctl restart vsftpd.service`

```sh
    $ sudo mkdir /home/common
    $ sudo touch /home/common/welcome.txt
    $ sudo useradd -d /home/common -s /bin/bash common
    $ sudo passwd common
    $ sudo rm /etc/pam.d/vsftpd
    $ sudo usermod -s /sbin/nologin common
    $ sudo chmod a+w /etc/vsftpd.conf
    $ sudo vim /etc/vsftpd.conf
    $ sudo vim /etc/vsftpd.user_list
    $ sudo chmod a-w /home/common
    $ sudo mkdir /home/common/public && sudo chmod 777 -R /home/common/public
    $ sudo systemctl restart vsftpd.service
```

************************

## SSH
> [详细](/Linux/Base/SSH.md)

## Telnet

> [linux telnet命令参数](http://www.linuxso.com/command/telnet.html)  
> [每天一个linux命令（58）：telnet命令](http://www.cnblogs.com/peida/archive/2013/03/13/2956992.html)

- 测试端口连通性 `telnet ip port` 如果端口开放则提示 Connected, 否则会提示 refused 
    - netcat 具有同样效果 `nc -v -z -n ip port`

## VPN
### tun/tap
> [参考: linux下TUN/TAP虚拟网卡的使用](https://blog.csdn.net/bytxl/article/details/26586109)  

`TUN TAP 区别`

> TUN 
1. 工作在IP层 第三层 

> TAP
1. 工作在数据链路层，第二层 

### shadowsocks
_服务端_
- 安装服务端`sudo pip install shadowsocks`
- 启动服务`sudo ssserver -p 443 -k sd -m aes-256-cfb`     
- 后台运行`sudo ssserver -p 443 -k sd -m aes-256-cfb --user nobodu -d start`
- 停止 `sudo ssserver -d stop`
- 日志 `sudo less /var/log/shadowsocks.log`

_客户端_
- `sudo vim /etc/ss.json` 
```json
    { 
	    "server":"127.0.0.1",
	    "server_port":443,
	    "localport":1080,
	    "password":"password",
	    "timeout":600,
	    "method":"aes-256-cfb"
    }
```
- `sslocal -c /etc/ss/json`
- 设置代理是1080端口即可

### OpenVPN
> [arch wiki](https://wiki.archlinux.org/index.php/OpenVPN)

以下文件都在同一目录下
1. 服务端提供 ca 文件 
1. 配置文件 `connect.ovpn`
    ```
        client
        dev tun
        proto tcp
        remote IP PORT               # 服务端IP地址映射的公网IP地址 端口
        resolv-retry infinite
        nobind
        persist-key
        persist-tun

        ca ca.crt # ca 文件

        auth-user-pass # 可选 password 文件

        comp-lzo
        verb 3
    ```
1. 账户密码文件 `passwd`
    ```
    用户名
    密码
    ```
1. 启动 sudo openvpn --daemon --cd /etc/openvpn/client --config connect.ovpn --auth-user-pass /etc/openvpn/client/passwd --log-append /path/to/log.log

> ERROR: Cannot open TUN/TAP dev /dev/net/tun: No such device
1. modinfo tun 查看内核模块是否存在
1. 尝试 sudo pacman -S networkmanager-vpnc 并重启

### Fortivpn 
> [openfortivpn](https://github.com/adrienverge/openfortivpn)  对应于 [fortinet.com](https://fortinet.com/) 的开源版本

`yay openfortivpn`

1. 按官方文档新建配置文件 some_company.conf
    - 填写正确的 host,port,username,password 
    - 注意: trusted-cert 可以用仓库Readme文档的值，通过报错信息获得公司内的证书，然后反向填入配置文件。。。
        - 相比于官方的包 `forticlient-vpn` GUI配置完，不像Windows平台会提示导入证书，只有无尽的连接中。。
1. sudo openfortivpn -c some_company.conf
1. 手动追加dns `sudo sed -i '1 i\nameserver x.x.x.x' /etc/resolv.conf` 注意 dns的ip会从运行中的输出 ns 部分

************************

## 代理

### proxychains
- 安装
    - [编译安装](https://github.com/rofl0r/proxychains-ng)
    - 包管理器  
        ```shell
        sudo pacman -S community/proxychains-ng # Arch
        sudo apt install proxychains  # apt
        ```
- 配置文件 `/etc/proxychains.conf`
    ```conf
    [ProxyList]
    # add proxy here ...
    # meanwile
    # defaults set to "tor"
    # socks4        127.0.0.1 9050
    # socks5  127.0.0.1  1080
    http  127.0.0.1 7890
    ```

************************

## 防火墙

### iptables
> [参考: linux下IPTABLES配置详解](http://www.cnblogs.com/JemBai/archive/2009/03/19/1416364.html)

> 其主要配置文件为: `/etc/sysconfig/iptables`

- 查看配置情况 ` iptables -L -n`

- 开启/屏蔽 端口 `iptables -A INPUT -p tcp --dport 8000 -j ACCEPT`
    - -A 参数表示添加规则，此外-D表示删除规则
    - -p 表示协议，一般都是tcp
    - --dport 就是指定端口号
    - -j 指定 ACCEPT/DROP，接收还是抛弃

_问题场景_
1. 服务器的端口服务是正常启动的, 但是客户端连不上；使用curl 去访问那个端口, 报错说 curl: (7) Failed to connect to xxxx port 8080: 没有到主机的路由
1. curl 无响应

#### 四层协议端口转发

可实现场景：公网内服务器访问内网A域名（Nginx配置）。  
实现方案为公网服务器追加A域名的DNS到内网出口机的公网ip，出口机配置任意端口转发并修改上层应用层的请求头从而实现Nginx无感差异的访问（Nginx能正常匹配路由）  

************************
## 远程桌面
> [参考: 连接Linux远程桌面的四个方法](https://www.cnblogs.com/hw-1015/articles/5910969.html)  
> [参考: 你会在linux服务器上安装远程桌面吗？](https://www.zhihu.com/question/20301978)  

### VNC
> Virtual Network Computing 

> [参考: Ubuntu远程SSH及x11vnc远程桌面连接](https://blog.csdn.net/ywueoei/article/details/79952727)  

1. 服务端安装 `x11vnc`
1. 设置密码 `x11vnc -storepasswd`
1. 使用密码启动 `x11vnc -auth guess -once -loop -noxdamage -repeat -rfbauth ~/.vnc/passwd -rfbport 5900 -shared`
    - 设置分辨率 `-geometry 1280×1024`

1. 客户端 vnc-viewer(任意) 输入 ip 即可连接 

> [noVNC](https://github.com/novnc/noVNC) `VNC client web application`

************************

### Xrdp
> [参考: Xrdp - 通过Windows的RDP连接Linux远程桌面](https://www.linuxidc.com/Linux/2018-10/155073.htm)  

************************

# Tips

