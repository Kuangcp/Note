---
title: TCP
date: 2025-03-13 10:34:00
tags: 
categories: 
---

💠

- 1. [TCP](#tcp)
    - 1.1. [TCP UDP 对比](#tcp-udp-对比)
    - 1.2. [Tuning](#tuning)

💠 2025-03-13 10:41:25
****************************************
# TCP

> 传输控制协议（英语：Transmission Control Protocol，缩写为 TCP, 是一种面向连接的、可靠的、基于**字节流**的传输层通信协议，由IETF的RFC 793定义。

- [wireshark tcp](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvTCPAnalysis.html)

> TCP 段的头部信息 20字节 也就是160位
```
    16位源端口号,16位目的端口号
    32位序列号
    32位确认序列号
    4位首部长度, 保留6位, URG, ACK, PSH, PST, SYN, FIN, 16位窗口大小
    16位校验和, 16位紧急指针
    选项
    数据...
```

> [Why do we need a 3-way handshake? Why not just 2-way?](https://networkengineering.stackexchange.com/questions/24068/why-do-we-need-a-3-way-handshake-why-not-just-2-way)

> [TCP 重传、滑动窗口、流量控制、拥塞控制](https://www.xiaolincoding.com/network/3_tcp/tcp_feature.html) | [TCP congestion control](https://en.wikipedia.org/wiki/TCP_congestion_control)

************************

TCP状态 [详解TCP的11种状态](https://cloud.tencent.com/developer/article/1648432)

握手阶段 CLOSED， LISTEN， SYN_RCVD， SYN_SENT， ESTABLISHED
挥手阶段 FIN_WAIT_1, FIN_WAIT_2, CLOSE_WAIT, LAST_ACK, TIME_WAIT, CLOSING 

************************

> [漫画 | 一台Linux服务器最多能支撑多少个TCP连接？ ](https://mp.weixin.qq.com/s/RdsNsanjeyVIkY6UuaJS4w)
- TCP连接四元组是源IP地址、源端口、目的IP地址和目的端口。只要任一元素发生了改变，那么就代表的是一条完全不同的连接。
    - 拿Nginx开启的80端口举例，目的IP地址、目的端口都是固定的。剩下源IP地址、源端口是可变的。  
    - 所以理论上Nginx上最多可以建立 2的32次方（ip数） × 2的16次方（port数） 个连接。
- 这是`两百多万亿`的一个大数字，想要建立这个量级的连接数，首先会被 可打开文件句柄，可用内存，CPU等资源制约。  

************************

> KeepAlive
- [聊聊 TCP 长连接和心跳那些事 ](https://juejin.cn/post/6844903765674295309)
    - HTTP 协议的 KeepAlive 意图在于tcp的连接复用，同一个连接上串行方式传递请求-响应数据。 
    - TCP 的 KeepAlive 机制意图在于保活、心跳，检测连接错误。

## TCP UDP 对比
> [参考: TCP和UDP的最完整的区别](https://blog.csdn.net/li_ning_/article/details/52117463)  
> [参考: TCP和UDP的区别和优缺点](https://blog.csdn.net/xiaobangkuaipao/article/details/76793702)  
> [参考: TCP、UDP数据包大小的限制](https://blog.csdn.net/caoshangpa/article/details/51530685)  

- 可使用 wireshark 抓包对比的方式进行学习: 基于udp(默认)的dns方式，对比 基于tcp的dns方式 更直观看出 tcp 三次握手 四次挥手 -- 《Wireshark 网络分析就这么简单》

- TCP与UDP基本区别
  1. 面向连接 与 无连接
  1. TCP要求系统资源较多，UDP较少
  1. UDP程序结构较简单 
  1. 流模式（TCP）与数据报模式(UDP); 
    - 开发者在使用TCP服务的时候，不必去关心数据包的大小，只需将SOCKET看作一条数据流的入口，直接传入数据，TCP协议本身会进行拥塞/流量控制
        - 但是也因此要处理粘包拆包的问题（此处属于概念混淆，正确描述应该是**应用层**上数据正确的序列化反序列化，包的概念仅处于网络层）
    - UDP的最大包长度是2^16-1的个字节。由于udp包头占8个字节，而在ip层进行封装后的ip包头占去20字节，所以这个是udp数据包的最大理论长度是2^16-1-8-20=65507。 
        - UDP包的大小受限于 操作系统中 MTU 的值（单位字节byte） 。
            - 查看lo设备：`cat /sys/class/net/lo/mtu`
            - 试探出口MTU `ping -s 1472 jd.com`
        - UDP数据报的数据区通常小于等于1472字节（通常设备MTU为1500，同样减去28）
        - 如果超过1472很可能被分包，而其中一部分丢包，会导致整体无法被接受方组合数据被丢失，整体看来丢包概率会大大升高
  1. TCP保证数据正确性，UDP 需要自己处理丢包和数据值被干扰 
  1. TCP保证数据顺序，UDP不保证 
　　
- UDP应用场景：
  1. 面向数据报方式
  1. 网络数据大多为短消息 
  1. 拥有大量Client
  1. 对数据安全性无特殊要求
  1. 网络负担非常重，但对响应速度要求高

> Tips
- TCP和UDP可以共用一个接口，由于TCP和UDP对于IP层来说是不同的协议，因此五元组不冲突

## Tuning
- 异常状态多时可以查看Linux内核参数以及 连接队列和半连接队列

************************

> [大量的 TIME_WAIT 状态连接怎么处理？](https://cloud.tencent.com/developer/article/1675933)
- TIME_WAIT 由于需要等待 2ML（Maximum Segment Life，报文段最大生存时间） 时间才能关闭TCP连接， 频繁请求会导致创建出大量TIME_WAIT的TCP连接
    - 会占用一个IP层五元组：（协议，本地IP，本地端口，远程IP，远程端口）
    - 对于 Web 服务器，协议是 TCP，本地 IP 通常也只有一个，本地端口默认的 80 或者 443。只剩下远程 IP 和远程端口可以变了。
    - 如果远程 IP 是相同的话，就只有远程端口可以变了。这个只有几万个，所以当同一客户端向服务器建立了大量连接之后，会耗尽可用的五元组导致无法建立连接。

************************

> 大量 CLOSE_WAIT 如何处理
- 表示正在等待关闭，该状态只在被动端出现，即当主动断开的一端调用close()后发送FIN报文给被动端，被动段必然会回应一个ACK(这是由TCP协议层决定的)，这个时候，TCP连接状态就进入到CLOSE_WAIT
- 出现大量close_wait的原因就是：server接收到了client的FIN信号后进入close_wait状态，但后续并未发送FIN信号给client而是长期滞留在close_wait状态当中，而client一般会设置超时时间，所以即便最终server发出了FIN信号，此时很大概率client已经判断超时导致TCP连接异常。更严重的是，如果client还设置了重试策略，就会在server内部产生更多close_wait。
- 那么server在什么情况下FIN包会发送失败?
- 程序问题：如果代码层面忘记了 close 相应的 socket 连接，那么自然不会发出 FIN 包，从而导致 CLOSE_WAIT 累积；或者代码不严谨，出现死循环之类的问题，导致即便后面写了 close 也永远执行不到。
- 响应太慢或者超时设置过小：如果连接双方不和谐，一方不耐烦直接 timeout，另一方却还在忙于耗时逻辑，就会导致 close 被延后。响应太慢是首要问题，不过换个角度看，也可能是 timeout 设置过小。
- BACKLOG 太大：此处的 backlog 不是 syn backlog，而是 accept 的 backlog，如果 backlog 太大的话，设想突然遭遇大访问量的话，即便响应速度不慢，也可能出现来不及消费的情况，导致多余的请求还在队列里就被对方关闭了。

