---
title: 计算机网络
date: 2018-11-21 10:56:52
tags: 
    - 基础
    - 网络
categories: 
    - 计算机科学
---

**目录 start**

1. [网络](#网络)
    1. [相关书籍和资源](#相关书籍和资源)
1. [网络分层架构](#网络分层架构)
    1. [物理层](#物理层)
    1. [数据链路层](#数据链路层)
    1. [网络层](#网络层)
        1. [IP协议](#ip协议)
            1. [IP地址分类](#ip地址分类)
            1. [无分类编址 CIDR](#无分类编址-cidr)
        1. [ARP协议](#arp协议)
        1. [ICMP协议](#icmp协议)
    1. [传输层](#传输层)
        1. [TCP](#tcp)
        1. [UDP](#udp)
        1. [TCP UDP 对比](#tcp-udp-对比)
    1. [应用层](#应用层)
        1. [HTTP & HTTPS](#http-&-https)
        1. [Websocket](#websocket)
        1. [WebDAV](#webdav)
        1. [网络延迟](#网络延迟)
        1. [TTFB](#ttfb)
        1. [URL](#url)
        1. [DNS](#dns)
        1. [VPN](#vpn)
        1. [SSDP](#ssdp)
1. [Socket](#socket)
1. [单播 组播 广播](#单播-组播-广播)
    1. [单播](#单播)
    1. [组播](#组播)
    1. [广播](#广播)
1. [代理 Proxy](#代理-proxy)
    1. [PAC](#pac)
    1. [正向代理](#正向代理)
    1. [反向代理](#反向代理)
    1. [透明代理](#透明代理)
    1. [代理工具](#代理工具)
        1. [Fiddler](#fiddler)
        1. [Wireshark](#wireshark)
        1. [Charles](#charles)
        1. [mitmproxy](#mitmproxy)
        1. [Mars](#mars)
        1. [camilla](#camilla)
1. [Tips](#tips)
    1. [移动通信技术规格](#移动通信技术规格)

**目录 end**|_2020-04-28 11:04_|
****************************************
# 网络

## 相关书籍和资源
> [Real time Webservice](http://ceur-ws.org/Vol-601/EOMAS10_paper13.pdf)

> [Beej's Guide to Network Programming](http://beej.us/guide/bgnet/)

- webapi的设计与开发
- 网络是怎样连接的
- 计算机网络 谢希仁

> [码农翻身:小白科普：从输入网址到最后浏览器呈现页面内容，中间发生了什么？](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665514196&idx=1&sn=ca26d258fcc4a35fc6d9a539b7d71dd7&chksm=80d67c97b7a1f58198b2e6ae436f73c677c0df4c05c2a8a4aad2b9e2d523da57dd5cd3d0a8ee&mpshare=1&scene=1&srcid=0122nnRpNb6OvRJubkSfKfsZ&pass_ticket=%2B%2FAmfhAaNv2sKw6192eqEL9hoW%2F6BrLxlzHIsKC0k6lPQsM4%2FFo08R%2FZowzw3821#rd) | 
> [码农翻身:我是一个路由器](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513173&idx=1&sn=6ec5281b12ed5195070fa4df22383595&scene=21#wechat_redirect) | 
> [码农翻身:我是一个网卡](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513160&idx=1&sn=d938db4f1a2d62514b57e92fd8d3d749&scene=21#wechat_redirect)

# 网络分层架构

开放系统互连基本参考模型 OSI/RM  Open Systems Interconnection Reference Model, 简称 OSI  

| OSI | TCP/IP |
|:----|:----:|
| 应用层 <br/> 表示层 <br/> 会话层 | 应用层 |
| 传输层                         | 传输层 |
| 网络层                         | 网络层 |
| 数据链路层 <br/> 物理层          | 链路层  |

OSI制定的OSI七层参考模型的过于庞大、复杂。与此对照，由技术人员设计的 TCP/IP协议栈(`四层`: 网络接口 网络层 传输层 应用层) 获得了更为广泛的应用。
谢希仁所著的 计算机网络 书中 为了教学, 融合成了 `五层模型`

事实上, 现在的应用不是严格按照OSI分层的, 应用层可以使用 传输层(TCP UDP), 也可以直接使用网络层(IP),甚至直接使用网络接口层

> [参考: 以太网帧结构](https://blog.csdn.net/wdkirchhoff/article/details/43915825)

************************

## 物理层
> 集线器 工作在这一层

## 数据链路层
> 常规交换机 工作在这一层

> 通常在帧的前面插入 8 字节，其中的第一个字段共 7 个字节，是前同步码，用来迅速实现 MAC帧的比特同步。第二个字段是帧开始定界符，表示后面的信息就是MAC帧

- MAC帧 组成为 `首部(MAC地址等信息) 数据(IP数据报) 尾部`
- 首部构成为
    1. 目的地址 **6字节**
    1. 源地址 **6字节**
    1. 类型 **2字节** 标志上一层使用的是什么协议
- 数据部分 (46-1500字节)
- 尾部：**4字节**长，包含的信息是帧校验序列FCS（使用CRC校验）

- PPP帧

************************

## 网络层
> 常规路由器 工作在这一层

### IP协议

> [IP数据报格式详解](https://blog.csdn.net/wangzhen209/article/details/74453548)

- IP数据报 组成为 `首部(IP地址等信息) 数据(TCP/UDP报文)` 
- 首部固定部分构成为:
    1.  `版本号`：占用**4位**二进制数，表示该IP数据报使用的IP协议版本。目前Internet中使用的主要是TCP/IP协议族中版本号为4的IP协议。
    1.  `首部长度`：占用**4位**二进制位，此域指出整个报头的长度（包括选项），该长度是以32位二进制数为一个计数单位的，
        - 接收端通过此域可以计算出报头在何处结束及从何处开始读数据。普通IP数据报（没有任何选项）该字段的值是5（即20个字节的长度）。
    1.  `服务类型（TOS、type of service）`：占用**8位**二进制位，用于规定本数据报的处理方式。
    1.  `总长度`：占用**16位**二进制位，总长度字段是指整个IP数据报的长度（报头区+数据区），以字节为单位。
        - 利用头部长度字段和总长度字段就可以计算出IP数据报中数据内容的起始位置和长度。由于该字段长度为16位二进制数，
        - 因此理论上IP数据报最长可达65536个字节（事实上受物理网络的限制，要比这个数值小很多）。
    1. `标识` **16位** IP软件在存储器中维持一个计数器，每产生一个数据报，计数器就加1，并将此值赋给标识字段。
        - 但这个“标识”并不是序号，因为IP是无连接服务，数据报不存在按序接收的问题。当数据报由于长度超过网络的MTU而必须分片时，
        - 这个标识字段的值就被复制到所有的数据报的标识字段中。相同的标识字段的值使分片后的各数据报片最后能正确地重装成为原来的数据报。
    1. `标志` **3位** 但只有2位有意义。
        - 标志字段中的最低位记为MF(More Fragment)。MF=1即表示后面“还有分片”的数据报。MF=0表示这已是若干数据报片中的最后一个。
        - 标志字段中间的一位记为DF(Don’t Fragment)，意思是“不能分片”。只有当DF=0时才允许分片。
    1. `片偏移` **13位** 片偏移指出：较长的分组在分片后，某片在原分组中的相对位置。也就是说，相对用户数据字段的起点，该片从何处开始。
        - 片偏移以8个字节为偏移单位。这就是说，除了最后一个分片，每个分片的长度一定是8字节（64位）的整数倍。
    1.  `生存时间（TTL，time to live）`：占用**8位**二进制位，它指定了数据报可以在网络中传输的最长时间。
        - 实际应用中把生存时间字段设置成了数据报可以经过的最大路由器数。TTL的初始值由源主机设置（通常为32、64、128或256），
            - 一旦经过一个处理它的路由器，它的值就减1。当该字段为0时，数据报就丢弃，并发送ICMP报文通知源主机，
            - 因此可以防止进入一个循环回路时，数据报无休止地传输下去。
    1.  `上层协议标识`：占用**8位**二进制位，IP协议可以承载各种上层协议，目标端根据协议标识就可以把收到的IP数据报送到TCP或UDP等处理此报文的上层协议了。
    1.  `校验和`：占用**16位**二进制数，用于协议头数据有效性的校验，可以保证IP报头区在传输时的正确性和完整性。
        - 头部检验和字段是根据IP协议头计算出的检验和，它不对头部后面的数据进行计算。
        - 原理：发送端首先将检验和字段置0，然后对头部中每16位二进制数进行反码求和的运算，并将结果存在校验和字段中。 
        - 由于接收方在计算过程中包含了发送方放在头部的校验和，因此，如果头部在传输过程中没有发生任何差错，那么接收方计算的结果应该是全1。
    1.  `源地址`：占用32位二进制数，表示发送端IP地址。
    1.  `目的地址`：占用32位二进制数，表述目的端IP地址。

- IPv4 & IPv6

> [参考: 浏览器访问IPv6地址](http://www.cnblogs.com/cuihongyu3503319/p/7422877.html)

#### IP地址分类
> IP地址的由 网络号 主机号 组成
- IP ::= {<网络号>, <主机号>}

IPv4 地址由 32 位标识符组成，目前由 ICANN 进行分配 且在 2011 年已经耗尽

| 类别 | 标识位 | 网络号 | 主机号 | 最大可分配网络数 | 最小可分配网络号 | 最大可分配网络号 
|:---|:---|:---|:---|:---|:---|:---|
| A | 0    | 8位  | 24位 | 126 2^7 - 2      | 1         | 126
| B | 10   | 16位 | 16位 | 16383 2^14 - 1   |  128.1    | 191.255
| C | 110  | 24位 | 8位  | 2097151 2^21 - 1 | 192.0.1   | 223.255.255
| D | 1110 |      |     |
| E | 1111 |      |     |

> 特殊IP地址

| 网络号  |  主机号   | 源地址使用 | 目的地址使用 | 含义 |
|:---|:---|:---|:---|:---|
| 0      | 0          | 可以   | 不可以 | 在本网络上的本主机 |
| 0      | host-id    | 可以   | 不可以 | 在本网络上的某个主机 host-id |
| 全1    | 全1         | 不可以 | 可以   | 只在本网络上进行广播 路由器不转发 |
| net-id | 全1         | 不可以 | 可以  | 对 net-id 的所有主机进行广播 |
| 127    | 非全0且非全1 | 可以   | 可以  | 作本地软件回环测试用 |

- A类
- B类
- C类
- D类 用于组播(多播)
- E类 保留地址

#### 无分类编址 CIDR
> 为了解决IPv4地址耗尽的问题

- IP ::= {<网络前缀>, <主机号>}

### ARP协议
> 同一局域网内，通过已知的IP地址和找到对应的硬件地址

1. 每个主机都会有一个 ARP高速缓存，存储本局域网内各主机和路由器的IP地址和硬件地址的映射
1. 当A要向主机B发送IP数据报就会查找该缓存，如果找不到
    1. ARP 进程在 本局域网广播 发送ARP请求分组 信息大致为我的IP地址A 硬件地址B，想知道IP地址C的硬件地址
    1. 本局域网内所有 ARP进程都会收到请求，IP地址与询问中的IP地址一致的才会响应请求，其他主机会丢弃
    1. C 响应内容大致为 我的IP地址 C 硬件地址 D，注意该响应是单播，显然此时只需要点对点通信即可无需发送广播而产生大量无用数据报占据网络
    1. A 收到响应后 将映射存入缓存

### ICMP协议

************

## 传输层
> TCP/IP 运输层的两个主要协议都是因特网的正式标准

用户数据报协议 UDP `User Datagram Protocol`
控制传输协议 TCP `Transmission Control Protocol`

按照 OSI 的术语, 两个对等运输实体在通信时传送的数据单位叫做 运输协议数据单元 TPDU Transport Protocol Data Unit.
但在 TCP/IP 体系中, 则根据使用的所使用的协议是 TCP 或 UDP, 分别称之为 TCP报文段 segment, UDP用户数据报

### TCP

> TCP 帧的头部信息 20字节 也就是160位
```
    16位源端口号,16位目的端口号
    32位序列号
    32位确认序列号
    4位首部长度, 保留6位, URG, ACK, PSH, PST, SYN, FIN, 16位窗口大小
    16位校验和, 16位紧急指针
    选项
    数据...
```

### UDP

> UDP 帧的头部信息 8 字节
```
    16位源端口号,16位目的端口号
    16位用户数据库包长度, 16位检查和
    数据...
```

### TCP UDP 对比
> [参考: TCP和UDP的最完整的区别](https://blog.csdn.net/li_ning_/article/details/52117463)  
> [参考: TCP和UDP的区别和优缺点](https://blog.csdn.net/xiaobangkuaipao/article/details/76793702)

- 可使用 wireshark 抓包对比的方式进行学习: 基于udp(默认)的dns方式，对比 基于tcp的dns方式 更直观看出 tcp 三次握手 四次挥手 -- 《Wireshark 网络分析就这么简单》

- TCP与UDP基本区别
  1. 基于连接与无连接
  1. TCP要求系统资源较多，UDP较少； 
  1. UDP程序结构较简单 
  1. 流模式（TCP）与数据报模式(UDP); 
  1. TCP保证数据正确性，UDP可能丢包 
  1. TCP保证数据顺序，UDP不保证 
　　
- UDP应用场景：
  1. 面向数据报方式
  1. 网络数据大多为短消息 
  1. 拥有大量Client
  1. 对数据安全性无特殊要求
  1. 网络负担非常重，但对响应速度要求高

************************

## 应用层

### HTTP & HTTPS
> [HTTP & HTTPS](/Skills/Network/HTTP.md)

************************

### Websocket
> Websocket协议 本质就是TCP的简单封装, 不像HTTP那样应答模式, 而是一次连接后就保持全双工模式


1. 单一的TCP连接, 采用全双工模式通信
2. 对代理, 防火墙和路由器透明
3. 无头部信息, Cookie, 身份验证
4. 无安全开销
5. 通过 ping/pong 帧 保持链路激活
6. 服务器可以主动传递消息给客户端, 不需要客户端轮询

> 4个生命周期事件
1. 打开事件：此事件发生在端点建立新连接时并且在任意其他事件发生之前
2. 消息事件：此事件接收WebSocket对话中另一端发送的消息。他可以发生在WebSocket端点接收了打开事件之后并且在接收关闭事件关闭连接之前的任意时刻
3. 错误事件：此事件在WebSocket连接或者端点发生错误时产生
4. 关闭事件：此事件表示WebSocket端点的连接目前正在部分的关闭，他可以有参与连接的任意一个端点发出

> [参考: WebSocket 和 Socket 的区别](http://blog.jobbole.com/106009/)  

************************

### WebDAV
> WebDAV （Web-based Distributed Authoring and Versioning） 一种基于 HTTP 1.1协议的通信协议.

它扩展了HTTP 1.1，在GET、POST、HEAD等几个HTTP标准方法以外添加了一些新的方法，使应用程序可直接对Web Server直接读写，并支持写文件锁定(Locking)及解锁(Unlock)，还可以支持文件的版本控制。

************************

### 网络延迟
> [如何彻底解决「网络延迟」这个问题？](https://www.zhihu.com/question/34689035)

- [MOBA类游戏是如何解决网络延迟同步的？](https://www.zhihu.com/question/36258781)
- [状态同步与帧同步](http://www.cnblogs.com/sevenyuan/p/5283265.html)

### TTFB
> `Time to first byte` 网络请求被发起到从服务器接收到第一个字节这段时间，它包含了 TCP连接时间，发送HTTP请求时间和获得响应消息第一个字节的时间。

### URL
> [维基百科](https://en.wikipedia.org/wiki/URL) | [百度百科](https://baike.baidu.com/item/URL)

- 统一资源定位符 特别注意URL的组成和编解码  [url中的特殊字符问题](http://www.cnblogs.com/xmphoenix/archive/2011/04/20/2022945.html)
    - 不能在URL的关键位置出现%号，作为参数的值是允许的。

### DNS
> 域名和资源转换的服务

> [www.ipaddress.com](https://www.ipaddress.com/)`查询域名的真实IP` 可协助解决DNS污染攻击

> [Wikipedia: DNS](https://en.wikipedia.org/wiki/Domain_Name_System)

- 解析域名的顺序一般是， 先在本机找，找不到去找上连DNS服务器， 然后根域DNS服务器
    - 这时候就有了几种方式，递归， 迭代， 递归加迭代（为了减轻全球13台根的压力）
    - 假设是访问这个域名 scs.bupt.edu.cn （bupt.三级 机构域名， edu 二级行业域名， cn 一级国家域名）
    - 递归： 本机->上连->根->cn->edu.cn->bupt.deu.cn 然后得到解析结果后，递归返回到上连，上连DNS服务器会进行缓存该结果，再返回本机
    - 迭代：本机->上连，上连->根，根->cn cn->edu.cn, edu.cn->bupt.deu.cn 最终返回了结果 到上连
    - 递归加迭代， 区别在于，先迭代根， 得到下级一级服务器节点后，下级就是递归的入口和出口
- 授权和非授权， 还是上面那个URL， 其他的都不是授权的， 只有离URL最近的DNS才是授权的 即 `bupt.edu.cn` 

************************

### VPN
>  Virtual Private Network (VPN) 

************************
### SSDP
> Simple Service Discovery Protocol

************************

# Socket
> [参考: TCP/IP、Http、Socket的区别](https://blog.csdn.net/Pk_zsq/article/details/6087367)  
> [what is socket](https://unix.stackexchange.com/questions/16311/what-is-a-socket)

Socket是应用层与TCP/IP协议族通信的中间软件抽象层，是对TCP/IP协议的封装，Socket本身并不是协议，而是一个调用接口（API），通过Socket，我们才能使用TCP/IP协议

在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。而我们所说的socket编程指的是利用soket接口来实现自己的业务和协议。

Socke接口属于软件抽象层，而sokcket编程却是标准的应用层开发

> [参考: Socket编程](http://www.cnblogs.com/skynet/archive/2010/12/12/1903949.html)  
> [参考: Linux socket 编程](https://www.ibm.com/developerworks/cn/education/linux/l-sock/l-sock.html)


************************

# 单播 组播 广播
广播通信只能在局域网内传播，组播通信能在公网内传播

组播通信相当于把主机与主机之间的通信压力转嫁到了路由器上面，所以要得到路由及网络的支持才能进行组播通信，整个传输过程中涉及的路由器或交换机都要支持组播通信，否则将无法使用组播通信

## 单播

## 组播

> [参考: 组播（Multicast）传输](http://www.cnblogs.com/ghj1976/p/5276452.html)  

## 广播

************************

# 代理 Proxy
> [wikipedia](https://en.wikipedia.org/wiki/Proxy) 


## PAC
> proxy auto config 

> [MDN: PAC File](https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_(PAC)_file)
```js
function FindProxyForURL(url, host) {
    return "PROXY 127.0.0.1:8080"; 
}
```

## 正向代理
> 隐藏 客户端 地址, 去访问地址明确的服务端

- 应用: 科学上网, VPN 
- 安全: 正向代理允许客户端通过它访问任意网站并且隐蔽客户端自身，因此你必须采取安全措施来确保仅为经过授权的客户端提供服务

## 反向代理
> 隐藏 服务端 地址, 客户端通过明确地址访问的实际上是代理

- 应用: 保护和隐藏原始资源服务器, 负载均衡, 加密和SSL加速, 缓存静态内容, 安全(DDos的防护)
- 安全: 对外是透明的，访问者并不知道自己访问的是代理。对访问者而言，他以为访问的就是原始服务器

## 透明代理
> 客户端根本不需要知道有代理服务器的存在，它改变你的 request fields（报文），并会传送客户端真实IP给服务端，多用于路由器的NAT转发中

能用缓存技术提高浏览速度，能用内存过滤提高安全性  

- eg: 内网中的硬件防火墙

************************

## 代理工具
> [Alternatives to Charles for Linux](https://alternativeto.net/software/charles/?platform=linux)

### Fiddler 
> [fiddler](https://www.telerik.com/fiddler)  

> [fiddler-everywhere](https://www.telerik.com/fiddler-everywhere) `Linux 免费`

### Wireshark
> [Official Site](https://www.wireshark.org/)  

> 问题  `Error during loading:[string "/usr/wireshark/init.lua"]:44:`  
- 这是由于Wireshark为了防止以root用户身份执行Lua脚本，避免对系统造成损坏，而显示警告弹窗。通常，用户只需要确认 
- 如果不想每次都看到 修改 `/usr/wireshark/init.lua` 第一行（非注释，有效代码） 改成 `disable_lua = true`

### Charles
> [Offcial Site](https://www.charlesproxy.com/)

### mitmproxy
> [Official Site](https://mitmproxy.org/) | [Docker Hub](https://hub.docker.com/r/mitmproxy/mitmproxy/)

- 启动 mit-web `docker run --name proxy -d -p 8888:8080 -p 8081:8081 mitmproxy/mitmproxy mitmweb --web-iface 0.0.0.0`
- 配置证书 访问 [mitm.it](mitm.it) 选择对应的平台即可
    - 实际上是安装了 mitmproxy-ca-cert.pem 文件 信任了 mitmproxy 这个CA

> [gomitproxy](https://github.com/zboya/gomitmproxy) `Go 实现`  
> 简评：过滤和搜索功能强大且支持重放但是用久了占用内存大，因为抓包的数据都在内存里

### Mars
> [Github](https://github.com/ouqiang/mars)

`虽然有使用LevelDB做存储，但是前端目前有BUG不能持久记录`  

### camilla
> [Offcial Site](https://www.camillaproxy.com/docs/)

> [docker-compose](https://gitee.com/gin9/DockerfileList/tree/master/docker-compose/camilla)

功能简单只能查看抓包的数据，数据只缓存浏览器，刷新就会消失，但是占用内存小

************************

# Tips
## 移动通信技术规格
> 1g 2g 2.5g 2.75g 3g 4g 5g

> [参考: 1G, 2G, 3G, 4G, & 5G Explained ](https://www.lifewire.com/1g-vs-2g-vs-2-5g-vs-3g-vs-4g-578681)
> [参考: Difference Between 1G, 2G, 3G vs. 4G and 5G](Difference Between 1G, 2G, 3G vs. 4G and 5G)
