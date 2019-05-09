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
1. [五层模型](#五层模型)
    1. [物理层](#物理层)
    1. [数据链路层](#数据链路层)
    1. [网络层](#网络层)
        1. [IP](#ip)
        1. [ARP](#arp)
    1. [传输层](#传输层)
        1. [TCP](#tcp)
        1. [UDP](#udp)
        1. [对比](#对比)
    1. [应用层](#应用层)
        1. [HTTP](#http)
        1. [Websocket](#websocket)
        1. [网络延迟](#网络延迟)
        1. [TTFB](#ttfb)
        1. [URL](#url)
        1. [DNS](#dns)
1. [Socket](#socket)
1. [单播 多播 组播](#单播-多播-组播)
    1. [组播](#组播)
1. [代理](#代理)
    1. [正向代理](#正向代理)
    1. [反向代理](#反向代理)
    1. [透明代理](#透明代理)
    1. [WebDAV](#webdav)
    1. [WebAssembly](#webassembly)
1. [工具](#工具)
    1. [Fiddler](#fiddler)
    1. [Wireshark](#wireshark)
1. [Tips](#tips)
    1. [移动通信技术规格](#移动通信技术规格)

**目录 end**|_2019-05-09 20:31_|
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

# 五层模型

开放系统互连基本参考模型 OSI/RM  Open Systems Interconnection Reference Model, 简称 OSI  
OSI制定的OSI七层参考模型的过于庞大、复杂。与此对照，由技术人员自己开发的TCP/IP协议栈(四层)获得了更为广泛的应用。  

谢希仁所著的 计算机网络 书中 为了教学, 融合成了 `五层模型`: 网络接口层 => 物理层+数据链路层 

事实上, 现在的应用不是严格按照OSI分层的, 应用层可以使用 传输层(TCP UDP), 也可以直接使用网络层(IP),甚至直接使用网络接口层

> [参考博客: 以太网帧结构](https://blog.csdn.net/wdkirchhoff/article/details/43915825)

*****************

## 物理层

## 数据链路层

## 网络层

### IP

> IPv4 & IPv6
> [参考博客: 浏览器访问IPv6地址](http://www.cnblogs.com/cuihongyu3503319/p/7422877.html)

### ARP
> 将IP和MAC对应起来的协议

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
### 对比
> [参考博客: TCP和UDP的最完整的区别](https://blog.csdn.net/li_ning_/article/details/52117463)  
> [参考博客: TCP和UDP的区别和优缺点](https://blog.csdn.net/xiaobangkuaipao/article/details/76793702)


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

## 应用层

### HTTP
> [HTTP](Skills/CS/Network/HTTP.md)

### Websocket
> Websocket协议 本质就是TCP的简单封装, 不像HTTP那样应答模式, 而是一次连接后就保持全双工模式

1. 单一的TCP连接, 采用全双工模式通信
2. 对代理, 防火墙和路由器透明
3. 无头部信息, Cookie, 身份验证
4. 无安全开销
5. 通过 ping/pong 帧 保持链路激活
6. 服务器可以主动传递消息给客户端, 不需要客户端轮询

> [参考博客: WebSocket 和 Socket 的区别](http://blog.jobbole.com/106009/)  
**************

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

> [Wikipedia: DNS](https://en.wikipedia.org/wiki/Domain_Name_System)

- 解析域名的顺序一般是， 先在本机找，找不到去找上连DNS服务器， 然后根域DNS服务器
     - 这时候就有了几种方式，递归， 迭代， 递归加迭代（为了减轻全球13台根的压力）
     - 假设是访问这个域名 scs.bupt.edu.cn （bupt.三级 机构域名， edu 二级行业域名， cn 一级国家域名）
     - 递归： 本机->上连->根->cn->edu.cn->bupt.deu.cn 然后得到解析结果后，递归返回到上连，上连DNS服务器会进行缓存该结果，再返回本机
     - 迭代：本机->上连，上连->根，根->cn cn->edu.cn, edu.cn->bupt.deu.cn 最终返回了结果 到上连
     - 递归加迭代， 区别在于，先迭代根， 得到下级一级服务器节点后，下级就是递归的入口和出口
- 授权和非授权， 还是上面那个URL， 其他的都不是授权的， 只有离URL最近的DNS才是授权的 即 `bupt.edu.cn` 

*******************************

# Socket
> [参考博客: TCP/IP、Http、Socket的区别](https://blog.csdn.net/Pk_zsq/article/details/6087367)  
> [what is socket](https://unix.stackexchange.com/questions/16311/what-is-a-socket)

Socket是应用层与TCP/IP协议族通信的中间软件抽象层，是对TCP/IP协议的封装，Socket本身并不是协议，而是一个调用接口（API），通过Socket，我们才能使用TCP/IP协议

在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。而我们所说的socket编程指的是利用soket接口来实现自己的业务和协议。

Socke接口属于软件抽象层，而sokcket编程却是标准的应用层开发

> [参考博客: Socket编程](http://www.cnblogs.com/skynet/archive/2010/12/12/1903949.html)  
> [参考博客: Linux socket 编程](https://www.ibm.com/developerworks/cn/education/linux/l-sock/l-sock.html)

********************************
# 单播 多播 组播

## 组播

> [参考博客: 组播（Multicast）传输](http://www.cnblogs.com/ghj1976/p/5276452.html)  

************************

# 代理
## 正向代理
> 客户端使用代理隐藏自身, 去访问明确的服务端

- 应用: 科学上网, VPN, 
- 安全: 正向代理允许客户端通过它访问任意网站并且隐蔽客户端自身，因此你必须采取安全措施来确保仅为经过授权的客户端提供服务

## 反向代理
> 服务端使用代理隐藏自身, 客户端明确访问的实际上是代理

- 应用: 保护和隐藏原始资源服务器, 负载均衡, 加密和SSL加速, 缓存静态内容, 安全(DDos的防护)
- 安全: 对外是透明的，访问者并不知道自己访问的是代理。对访问者而言，他以为访问的就是原始服务器

## 透明代理
> 客户端根本不需要知道有代理服务器的存在，它改变你的request fields（报文），并会传送真实IP，多用于路由器的NAT转发中

**********************************

## WebDAV

WebDAV （Web-based Distributed Authoring and Versioning） 一种基于 HTTP 1.1协议的通信协议.它扩展了HTTP 1.1，在GET、POST、HEAD等几个HTTP标准方法以外添加了一些新的方法，使应用程序可直接对Web Server直接读写，并支持写文件锁定(Locking)及解锁(Unlock)，还可以支持文件的版本控制。

## WebAssembly
> 字节码技术
> [ WebAssembly 实践：如何写代码 ](https://segmentfault.com/a/1190000008402872)
> [MDN](https://developer.mozilla.org/en-US/docs/WebAssembly)

************************

# 工具
## Fiddler 
> [fiddler](https://www.telerik.com/fiddler)  
> [fiddler-everywhere](https://www.telerik.com/fiddler-everywhere)

## Wireshark
> [Official Site](https://www.wireshark.org/)  

************************

> 问题
- `Error during loading:[string "/usr/wireshark/init.lua"]:44:`
    - 这是由于Wireshark为了防止以root用户身份执行Lua脚本，避免对系统造成损坏，而显示警告弹窗。通常，用户只需要确认 
    - 如果不想每次都看到 修改 `/usr/wireshark/init.lua` 第一行（非注释，有效代码） 改成 `disable_lua = true`

************************

# Tips
## 移动通信技术规格
> 1g 2g 2.5g 2.75g 3g 4g 5g

> [参考: 1G, 2G, 3G, 4G, & 5G Explained ](https://www.lifewire.com/1g-vs-2g-vs-2-5g-vs-3g-vs-4g-578681)
> [参考: Difference Between 1G, 2G, 3G vs. 4G and 5G](Difference Between 1G, 2G, 3G vs. 4G and 5G)
