`目录 start`
 
- [【网络管理】](#网络管理)
    - [DNS](#dns)
        - [修改DNS](#修改dns)
        - [刷新本地缓存](#刷新本地缓存)
    - [IPv4和IPv6](#ipv4和ipv6)
    - [Tips](#tips)
        - [查看端口占用情况](#查看端口占用情况)
    - [基础命令工具](#基础命令工具)
        - [1.ping](#1ping)
        - [2.curl](#2curl)
        - [3.iproute2](#3iproute2)
        - [4.tcpdump](#4tcpdump)
        - [5.netcat](#5netcat)
        - [6.scp](#6scp)
        - [7.rsync](#7rsync)
        - [8.wget](#8wget)
    - [【常用网络服务】](#常用网络服务)
        - [邮件服务器postfix和devecot](#邮件服务器postfix和devecot)
        - [FTP](#ftp)
            - [基础](#基础)
            - [使用](#使用)
            - [手机和电脑之间传输管理文件](#手机和电脑之间传输管理文件)
                - [手机](#手机)
                - [电脑](#电脑)
            - [配置FTP服务器](#配置ftp服务器)
        - [Ssh](#ssh)
        - [telnet](#telnet)
        - [VPN](#vpn)
            - [shadowsocks](#shadowsocks)
        - [防火墙](#防火墙)
            - [iptables](#iptables)

`目录 end` |_2018-09-13_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 【网络管理】
## DNS
- 域名和资源转换的服务
- 解析域名的顺序一般是， 先在本机找，找不到去找上连DNS服务器， 然后根域DNS服务器
     - 这时候就有了几种方式，递归， 迭代， 递归加迭代（为了减轻全球13台根的压力）
     - 假设是访问这个域名 scs.bupt.edu.cn （bupt.三级 机构域名， edu 二级行业域名， cn 一级国家域名）
     - 递归： 本机->上连->根->cn->edu.cn->bupt.deu.cn 然后得到解析结果后，递归返回到上连，上连DNS服务器会进行缓存该结果，再返回本机
     - 迭代：本机->上连，上连->根，根->cn cn->edu.cn, edu.cn->bupt.deu.cn 最终返回了结果 到上连
     - 递归加迭代， 区别在于，先迭代根， 得到下级一级服务器节点后，下级就是递归的入口和出口
- 授权和非授权， 还是上面那个URL， 其他的都不是授权的， 只有离URL最近的DNS才是授权的 即 `bupt.deu.cn` 

`nslookup ` 强大的调试DNS工具
- nslookup - 8.8.8.8 进入循环模式， 方便调试 8.8.8.8 是Google开放的DNS 备选 8.8.4.4
    - 结果解释：Non-authoritative answer: 表示这是从缓存得到的结果，不一定准确
    - Server：上连DNS服务器的IP， Address：`上连DNS的IP#端口` 通常是53
    - canonical name 即CNAME 别名
      `dig` 比nslookup更强大 Domain Information Groper
- 例如：`dig +tcp @8.8.8.8 www.baidu.com` 采用TCP进行DNS通信（默认UDP）
    - +short 精简输出
    - +nocmd+nocomment+nostat 输出最核心内容

`drill`
### 修改DNS
- `sudo vim /etc/resolv.conf` 添加Google的DNS 
```
    nameserver 8.8.8.8 
    nameserver 8.8.8.4
```

### 刷新本地缓存
> [参考博客](https://linux.cn/article-3341-1.html)
******************
## IPv4和IPv6
- IPv4 只有32bit IPv6 有128bit

`IPv6`
- 零省略 ：如果有一位是 000C 可以直接写C
- 零压缩 ：如果FE04:0:0:0:0:0:0:DA 写成 FE::DA

*******************
## Tips
### 查看端口占用情况
> netstat lsof fuser ps 都有一定效果 [ linux_performance ](./Linux/linux_performance.md)  

> [参考博客: linux下常用命令查看端口占用](http://blog.csdn.net/ws379374000/article/details/74218530)

_netstat工具_ 或者 更好用的 [iproute2](#3iproute2)

- `lsof -i:端口号` 用于查看某一端口的占用情况，缺省端口号显示全部
    - 或者 `cat /etc/services` 查看系统以及使用的端口

- `netstat -tunlp | grep 端口号` 用于查看指定的端口号的进程情况
    - `-t` (tcp) 仅显示tcp相关选项
    - `-u` (udp)仅显示udp相关选项
    - `-n` 拒绝显示别名，能显示数字的全部转化为数字
    - `-l` 仅列出在Listen(监听)的服务状态
    - `-p` 显示建立相关链接的程序名

- 查询端口占用的pid 三种：
    - `netstat -aonp |grep "^[a-z]\+[ ]\+0[ ]\+0[ ]\+[0-9\.]\+:80[ ]\+"|awk -F" "   {'print $0'}`
    - `netstat -aonp |grep ":80[ ]\+"|awk -F" "   {'print $0'}`
    - `sudo netstat -aonp |grep ":6379[ ]\+"|awk -F" "   {'print $0'}`
    - `sudo kill -9 pid` 杀掉指定pid
    - `ps aux` 查看当前执行中的程序

- 似乎能看到更多 `netstat -tpanl | grep 127.0.0.1` 

***************************
## 基础命令工具
> 参考书籍 《Linux 大棚命令百篇》

### 1.ping
- ping URL ： Linux是默认无休止的
    - -c 次数
    - -q 安静模式 不输出
    - -s 默认64字节， 可以指定大小
    - -t 设定 TTL值，Linux默认是64或255 经过一个路由器就会减一
    - -i 每次ping的时间间隔 默认1s root用户才可以设置 0.2 以下
    - -f 暴力尽可能大量包的传送 至少每秒100个
    - 注意：得到的结果中的 mdev 表示ICMP包的RTT偏离平均值的程度，mdev 越大表示网速不稳定 Linux有，mac下叫stddev win系列没有

### 2.curl
1. 不输出，重定向到*黑洞设备*  ` curl -s -o /dev/null URL`
1. 格式化返回的json数据：`curl xxxx|python -m json.tool `
1. 使用基础认证 发送JSON数据 `curl -i -H "Content-Type:application/json" -u admin:secret -X POST --data '{"title":"1","content":"1"}' http://tomcat.kcp/email/content`
```sh
    # 如果没有认证则会收到如下结果
$ curl -i -u admin:secret -X POST http://tomcat.kcp/email/content
    HTTP/1.1 401 
    Server: nginx/1.13.3
    Date: Thu, 26 Jul 2018 12:17:18 GMT
    Content-Length: 0
    Connection: keep-alive
    Set-Cookie: JSESSIONID=D863FC575140E9B1A0A2505410617487; Path=/; HttpOnly
    X-Content-Type-Options: nosniff
    X-XSS-Protection: 1; mode=block
    Cache-Control: no-cache, no-store, max-age=0, must-revalidate
    Pragma: no-cache
    Expires: 0
    X-Frame-Options: DENY
    WWW-Authenticate: Basic realm="Realm"
```

- [curl cookie](https://curl.haxx.se/docs/http-cookies.html) | [curl使用Cookie](https://aiezu.com/article/linux_curl_http_cookie.html)

> [参考博客: curl返回常见错误码](http://www.cnblogs.com/wainiwann/p/3492939.html)
- [56错误码](https://stackoverflow.com/questions/10285700/curl-error-recv-failure-connection-reset-by-peer-php-curl)
> [参考博客: 使用cURL和用户名和密码？](http://www.cnblogs.com/seasonzone/p/7527218.html)
### 3.iproute2
> 代替 netstat 的强大工具

`替代方案`

|   用途    | net-tool |     iproute2     |
| :-----: | :------: | :--------------: |
| 地址和链路配置 | ifconfig | ip addr, ip link |
|   路由表   |  route   |     ip route     |
|  ARP表   |   arp    |     ip neigh     |
|  VLAN   | vconfig  |     ip link      |
|   隧道    | iptunnel |    ip tunnel     |
|   组播    | ipmaddr  |     ip maddr     |
|   统计    | netstat  |        ss        |

_ss_
> [参考博客: Linux网络状态工具ss命令使用详解](http://www.ttlsa.com/linux-command/ss-replace-netstat/)

- 查看网络连接统计 `ss -s`
- 查看打开的端口 `ss -l`
- 查看打开的端口以及进程pid `ss -pl`
- 查看所有socket连接 `ss -a`
- 隧道术： 网络协议的数据包被封装在另一种网络协议的数据包之中 `这是VPN的技术理论基础`
> 别说的那么神乎其神, 用的时候, 连个Tomcat开的8080都查不到

`net-tools 和 iproute 对应关系`

|      作用      |               net-tools用法                |                iproute2用法                |
| :----------: | :--------------------------------------: | :--------------------------------------: |
|  展示本机所有网络接口  |                 ifconfig                 |              ip link [show]              |
| 开启/停止某个网络接口  |          ifconfig ech0 up/down           |           ip link up/down eth0           |
| 给网络接口设置/删除IP | ipconfig eth0 10.0.0.0.1/24 / ifconfig eth0 0 |   ip addr add/del 10.0.0.1/24 dev eth0   |
| 显示某个网络接口的IP  |              ifconfig eth0               |          ip addr show dev eth0           |
|    显示路由表     |                 route -n                 |              ip route show               |
|   添加删除默认网关   | route add/del default gw 192.168.1.2 eth0 | ip route default via 192.168.1.2 eth0 / ip route replace default via 192.168.1.2 dev eth0 |
|    添加ARP     |  arp -s 192.168.1.100 00:0c:29:c5:5a:ed  | ip neigh add 192.168.1.100 lladdr 00:0c:29:c5:5a:ed dev eth0 |
|    删除ARP     |           arp -d 192.168.1.100           |   ip neigh del 192.168.1.100 dev eth0    |
|   展示套接字状态    |                netstat -l                |                  ss -l                   |

- 默认网关： 如果主机找不到准发规则， 就把数据包发给默认的网关
- 增加/删除一条路由规则 `ip route add/del 192.168.2.0/24 via 192.168.1.254`

### 4.tcpdump
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

### 5.netcat
> sudo apt install netcat  

- 开始监听端口 ： `nc -l 11044`
    - 建立连接 `nc 127.0.0.1 11044` 任一方退出nc 就终止了连接

- 端口扫描 `nc -z -v -n -w 2 127.0.0.1 20-33`
    - 扫描22-33端口，
    - -z 一旦连接立马断开，不发送接收任何数据
    - -v 输出详细信息
    - -n 直接使用IP地址，不适用域名服务器来查询其域名
    - -w 设置连接超时时间 s
    - -u 使用UDP 默认缺省则是TCP
- 连接开放的端口 `nc -v host port`

- 传输文件 （相同的还有 ftp scp）
    - 服务端开启端口，准备好发送的文件 `nc -v -l 12345 < temp_out.md`
    - 客户端接收文件：`nc -v -n host port > temp_in.md`
    - 单次连接，传输完毕自动断开 服务端也可以是接收文件，将`< >`互换即可
    - 没有进度提示,大文件也不支持

- 传输文件夹 
    - 服务端 `tar -cvPf - /root/book/ | nc -l 12345`
    - 客户端 `nc -n host port | tar -xvPf -`
    - 这是未压缩的， 压缩再加上参数即可 例如 `gzip -czvPf -xzvPf`

### 6.scp
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

### 7.rsync 
> 同步命令 (个人倾向于本地和远程， 书上称为源端和目的端) [命令参数详解](http://man.linuxde.net/rsync)
> | [本地和VPS0之间同步数据](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps)

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

`【其他特别参数】`
- `--delete` 如果本地没有该文件 远程就会删掉
    - `--delete-exclude `删除远程指定的文件
    - ` --delete-after` 默认是先清理远程文件再同步，使用该选项就相反了先同步再删除需要删除文件
- `--exclude` 排除掉某些文件不同步 可以使用多次
    - `--excule-from` 如果要排除的文件很多，可以将文件名放在一个文本文件里，然后使用该选项读取该文件
- `--partial` 断点续传 可以简写-P
- `--progress` 显示传输进度信息

### 8.wget
> 特性和优势：支持 HTTP HTTPS FTP协议  
> - 能够跟踪 HTML 和 XHTML 即可以下载整站，但是注意wget会不停的去下载HTML中的外链，无休无止  
> - 遵守 robots.txt 标准的工具  
> - 支持慢速网路和不稳定的下载，当下载失败就会不断重试，直到下载成功  
> - 支持断点续传  

- wget 配置文件 `/etc/wgetrc` `~/.wgetrc` 两个文件配置（区别是全局和当前用户）wget的默认行为
- 例如 -X配置：`wget  -X js,css URL` 排除两个文件夹不下载
    - 如果要默认排除，到`.wgetrc`文件里配置 `exclude_directories=js,css` 
    - 这时候就出了一个问题，你不知道配置文件的情况时，发现总有目录下载不下来，就可以排除两个文件的作用：
    - `wget -X '' -X js,css URL`
    - 注意：`-X`，两个配置文件。这三者的配置，wget是取并集的， 使用了`-X ''` 后就只看后面的`-X 参数`   

- 参数:
    - 目录下载 `-r` 递归选项
    - 后台下载 `--background` 即使 你Ctrl D/exit也不会中断执行
    - -o 指定日志输出。默认当前目录的 wget-log
    - 避开robots.txt 协议 `--execute robots=off`
        - 尝试使用tomcat构建一个有robots协议的网站，然后wget还是绕过了协议。。。。。。
        - 对github测试这个参数是正常的
    - 简化wget获取到的文件
        - -nH 去除wget将域名作为文件夹的情况,只得到域名下相对路径的文件
        - --cut-dirs=number 去除前缀路径 
        - 只用 `-r` : URL:a/b/c/
        - `-r` 再用上 `--cut-dirs=1` : URL:/b/c/
        - `-r` 再用上 `-nH` :a/b/c/
        - `-r` 再用上 `-nH --cut-dirs=1` : /b/c/
        - `-r` 再用上 `-nH --cut-dirs=2` : /c/
    - 平铺,不使用源站的目录结构: `-nd` 若有重名文件,自动重命名
    - 强制处处文件夹 `-x` 例如:com.github.com/a/b/ --> com/github/com/a/b/
    - 协议命名的根文件夹 --protocol-directories 例如 ftp://baidu.com/a/b/
    - 自动重试 `--tries=number` 设置下载失败后重试的次数    
    - 输出到指定文件 `-O` 将下载的所有文件的内容追加到指定的文件,不会新建任何文件 和 -o 对比:这是是指定输出日志文件
    - 拒绝重复下载同名文件,即使这个文件不是最新的 `-nc`, wget会先比较时间戳,然后下载,且多次下载同名文件会自动添加.1.2这样的后缀
    - 自动分析是否下载同名文件, `-N` 会考虑时间戳以及文件大小,但是不能和 -nc 同时设置
    - 断点续传 -c 但是有潜在bug,当源站的文件头部分或者已下载部分修改了,wget是不知道的,只会继续下载之前没下载的内容
    - 限速 `--limit-rate=N` 默认单位是b,可以指定单位 k m , 
        - 这个限速的实现原理是通过在进行一次网络读取后,就线程睡眠一会儿,将速度降下来,如果下载是超小文件就可能无法达到限速的效果  
    - 限制频率 -w 即 --wait=seconds 可以指定m h d 等单位,效果是每两个请求间隔指定时间
    - 请求重试 `--waitretry` 设置请求重试的秒数, 如果设置的是10秒, 第一次失败后就会等1s,然后第二次失败就等2s...直到递增到10s,然后结束
        - 其效果 其实应该是 设置值的累加 (理解为重试次数似乎更好)
    
> [wget cookie](http://blog.csdn.net/adream307/article/details/47379149)  
> [参考博客: wget命令详解](http://blog.csdn.net/RichardYSteven/article/details/4565931)

- 镜像整站 `wget --mirror -p --convert-links -P . URL`
    - –miror:开户镜像下载
    - -p:下载所有为了html页面显示正常的文件
    - –convert-links:下载后，转换成本地的链接
    - -P .：保存所有文件和目录 到当前目录

****************************
## 【常用网络服务】
### 邮件服务器postfix和devecot

### FTP

#### 基础

#### 使用
- 登录`ftp host port`

#### 手机和电脑之间传输管理文件
> 前提是两个设备处于同一个局域网, 也就是说连同一个WIFI, 或者电脑开热点给手机连?

##### 手机
> 手机安装 FeelFTP , 然后设置编码为utf-8, 开启服务器  
> 或者安装ES文件浏览器, 也带有FTP服务器, 但是不稳定, 切出去就停了, 而且不能选择上SDK卡

##### 电脑
> 安装FileZila 建立连接, 然后就能方便的用鼠标进行传输了

#### 配置FTP服务器
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
- 新建文件 sudo touch /etc/vsftpd.user_list
- 修改权限 `sudo chmod a+w /etc/vsftpd.user_list`
- 添加用户名 `uftp`
- 设置用户目录只读 `sudo chmod a-w /home/common`
- 新建公共目录 设置权限 `mkdir /home/common/public && sudo chmod 777 -R /home/common/public`
- 重启服务 `sudo systemctl restart vsftpd.service`

```sh
     ~$ sudo mkdir /home/common
     ~$ sudo touch /home/common/welcome.txt
     ~$ sudo useradd -d /home/common -s /bin/bash common
     ~$ sudo passwd common
     ~$ sudo rm /etc/pam.d/vsftpd
     ~$ sudo usermod -s /sbin/nologin common
     ~$ sudo chmod a+w /etc/vsftpd.conf
     ~$ sudo vim /etc/vsftpd.conf
     ~$ sudo vim /etc/vsftpd.user_list
     ~$ sudo chmod a-w /home/common
     ~$ sudo mkdir /home/common/public && sudo chmod 777 -R /home/common/public
     ~$ sudo systemctl restart vsftpd.service
```

******************************
### Ssh
> [详细](/Linux/Base/Ssh.md)

### telnet
> [linux telnet命令参数](http://www.linuxso.com/command/telnet.html)  
> [每天一个linux命令（58）：telnet命令](http://www.cnblogs.com/peida/archive/2013/03/13/2956992.html)

***********
### VPN
#### shadowsocks
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

### 防火墙

#### iptables
> [参考博客: linux下IPTABLES配置详解](http://www.cnblogs.com/JemBai/archive/2009/03/19/1416364.html)

> 其主要配置文件为: `/etc/sysconfig/iptables`

- 查看配置情况 ` iptables -L -n`

- 开启端口 `iptables -A INPUT -p tcp --dport 8000 -j ACCEPT`
    - -A 参数表示添加规则，此外-D表示删除规则
    - -p 表示协议，一般都是tcp
    - --dport 就是指定端口号
    - -j 指定是ACCEPT还是DROP，接收还是抛弃

_有时候会发生这样的事情_
1. 服务器的服务是正常启动的, 但是客户端连不上, 然后使用curl 去访问那个端口, 报错说 curl: (7) Failed to connect to 192.168.10.201 port 16888: 没有到主机的路由
2. 那么这时候就要检查防火墙了



