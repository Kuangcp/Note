---
title: HTTP
date: 2019-03-17 14:23:29
tags: 
    - 网络
categories: 
    - 计算机科学
---

**目录 start**

1. [HTTP](#http)
    1. [请求方法](#请求方法)
    1. [HTTP的返回码](#http的返回码)
    1. [HTTP的缓存](#http的缓存)
    1. [Session和Cookie](#session和cookie)
1. [HTTP各个实现版本](#http各个实现版本)
    1. [HTTP/0.9](#http09)
    1. [HTTP/1.0](#http10)
    1. [HTTP/1.1](#http11)
    1. [HTTP/2](#http2)
    1. [HTTP/3](#http3)
1. [HTTPS](#https)
    1. [HTTPS 认证流程](#https-认证流程)
    1. [HSTS](#hsts)
1. [CORS](#cors)

**目录 end**|_2020-04-26 21:27_|
****************************************
# HTTP
> HyperText Transfer Protocol 超文本传输协议 他是一种用于分布式、协作式和超媒体信息系统的应用层协议

> [参考博客: HTTP详解](https://mp.weixin.qq.com/s?__biz=MzI3NzE0NjcwMg==&mid=2650123318&idx=1&sn=a0b20cfeda4bf0445de8c981533aca1b&chksm=f36bb117c41c3801a951407743aa9e850aa2d5e834fb87ecdc472c871b74d60254fe7d03cd4d&mpshare=1&scene=1&srcid=&pass_ticket=C2ojewcjO3f%2B94ARPux0b29jNh%2BTyGIKOzdhalFniunqbWndDpBOllbB79D9AqM0#rd)

- 其实HTTP协议主要就是用来进行客户端和服务器之间进行通信的标准协议。
- HTTP主要规定了客户端如何与服务器建立链接、客户端如何从服务器请求数据、服务器如何响应请求，以及最后连接如何关闭

> 整个流程: 建立连接 进行请求 响应 关闭连接

`建立连接`
根据用户输入的URL地址，通过DNS、负载均衡等技术找到一台服务器，客户端与服务器的80端口建立一个TCP链接。
`进行请求`
客户端向服务器发送消息，请求URL中指定的页面，要求执行指定的操作
`响应`
服务器向客户端发送响应。响应以状态码开头。常见的状态码有：200、302、404、500等。
`关闭连接`
客户端或服务端都可以关闭连接。每个请求都是用一个单独的网络连接。

> 服务器不回记忆前面一次连接或者其结果，这种不记忆过去请求的协议被称为无状态(stateless)协议

## 请求方法
- HTTP/1.1协议中共定义了八种方法（有时也叫“动作”）来表明Request-URI指定的资源的不同操作方式：
    - `OPTIONS` 返回服务器针对特定资源所支持的HTTP请求方法。也可以利用向Web服务器发送'*'的请求来测试服务器的功能性。　
    - `GET` 向特定的资源发出请求。注意：GET方法不应当被用于产生“副作用”的操作中，例如在web app.中。其中一个原因是GET可能会被网络蜘蛛等随意访问。　
    - `HEAD` 向服务器索要与GET请求相一致的响应，只不过响应体将不会被返回。这一方法可以在获取包含在响应消息头中的元信息而不传输内容。
    - `POST` 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。　
    - `PUT` 向指定资源位置上传其最新内容。　
    - `DELETE` 请求服务器删除Request-URI所标识的资源。　
    - `TRACE` 回显服务器收到的请求，主要用于测试或诊断。　
    - `CONNECT` HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。　
    
> 方法名称是区分大小写的。当某个请求所针对的资源不支持对应的请求方法的时候，服务器应当返回状态码405（Method Not Allowed）；当服务器不认识或者不支持对应的请求方法的时候，应当返回状态码501（Not Implemented）。

- [ ] Header中一些主要属性的含义和使用场景

## HTTP的返回码
> [完整列表 ](/FrontEnd/ResponseCode.md)

## HTTP的缓存

## Session和Cookie

# HTTP各个实现版本
HTTP协议主要的版本有3个，分别是HTTP/1.0、HTTP/1.1和HTTP/2

## HTTP/0.9
> HTTP于1990年问世，那时候HTTP非常简单：只支持GET方法；没有首部；只能获取纯文本。

## HTTP/1.0
> 1996年5月，HTTP/1.0 版本发布，为了提高系统的效率，HTTP/1.0规定浏览器与服务器只保持短暂的连接

- 浏览器的每次请求都需要与服务器建立一个TCP连接，服务器完成请求处理后立即断开TCP连接，服务器不跟踪每个客户也不记录过去的请求。  
- HTTP/1.0中浏览器与服务器只保持短暂的连接，连接无法复用。也就是说每个TCP连接只能发送一个请求。发送数据完毕，连接就关闭，如果还要请求其他资源，就必须再新建一个连接。  
- 我们知道TCP连接的建立需要三次握手，是很耗费时间的一个过程。所以，HTTP/1.0版本的性能比较差。
- 对于同一个tcp连接，所有的http1.0请求放入队列中，只有前一个请求的响应收到了，然后才能发送下一个请求。可见，http1.0的队首组塞发生在客户端。

## HTTP/1.1
> HTTP/1.1于1999年诞生。相比较于HTTP/1.0来说，最主要的改进就是引入了持久连接(PersistentConnection)和请求的流水线（Pipelining）处理 

1. 还提供了与身份认证、状态管理和Cache缓存等机制相关的请求头和响应头。
1. 强制客户端提供 host 头域 
1. 加入了一个新的状态码100(Continue) : 为了节约带宽
    - 客户端事先发送一个只带头域的请求，如果服务器因为权限拒绝了请求，就回送响应码401（Unauthorized）；
    - 如果服务器接收此请求就回送响应码100，客户端就可以继续发送带实体的完整请求了。
    - 100 状态代码的使用，允许客户端在发request消息body之前先用request header试探一下server，看server要不要接收request body，再决定要不要发request body。
1. HTTP/1.1在1.0的基础上加入了一些cache的新特性，当缓存对象的Age超过Expire时变为stale对象，cache不需要直接抛弃stale对象，而是与源服务器进行重新激活（revalidation）

> 存在的问题:   
>1. 队首阻塞：TCP连接上只能发送一个请求，前面的请求未完成前，后续的请求都在排队等待  
>1. 多个TCP连接: 虽然HTTP/1.1管线化可以支持请求并发，但是浏览器很难实现，chrome、firefox等都禁用了管线化。所以1.1版本请求并发依赖于多个TCP连接，建立TCP连接成本很高，还会存在慢启动的问题。  
>1. 头部冗余，采用文本格式 HTTP/1.X版本是采用文本格式，首部未压缩，而且每一个请求都会带上cookie、user-agent等完全相同的首部。  
>1. 客户端需要主动请求

*****************

`持久连接` 即TCP连接默认不关闭，可以被多个请求复用。HTTP 1.1的持久连接，也需要增加新的请求头来帮助实现 例如
- Connection请求头的值为Keep-Alive时，客户端通知服务器返回本次请求结果后保持连接；
    - 使用 Keep-Avlive 方式时， 在传送数据时要么响应头指定 Content-Length，要么用 chunked 编码，这两种方法都可以判断一次请求的数据发送完成。
    - 在一次请求结束之后，TCP 链接才可被复用进行下一次请求，否则根本无法判断当前传送的数据属于哪次请求的
- Connection请求头的值为close时，客户端通知服务器返回本次请求结果后关闭连接。

****************************

请求的流水线（Pipelining）处理，在一个TCP连接上可以传送多个HTTP请求和响应，减少了建立和关闭连接的消耗和延迟。例如：
> 一个包含有许多图像的网页文件上的多个资源请求和应答可以在一个连接中传输  
> 但每个单独的网页文件的请求和应答仍然需要使用各自的连接。  

- 对于同一个 tcp 连接，http1.1 允许一次发送多个 http1.1 请求，也就是说，不必等前一个响应收到，就可以发送下一个请求.   
- 这样就解决了 http1.0 的客户端的队首阻塞。但是，http1.1 规定，服务器端的响应的发送要根据请求被接收的顺序排队.  
- 也就是说，先接收到的请求的响应也要先发送。这样造成的问题是，如果最先收到的请求的处理时间长的话，响应生成也慢，就会阻塞已经生成了的响应的发送。  
- 也会造成队首阻塞。队首阻塞是发生在服务端的

********************

## HTTP/2
> HTTP/2 是 HTTP 协议自 1999 年 HTTP 1.1 发布后的首个更新，主要基于 SPDY 协议(2012年google提出)  
> [wiki HTTP/2](https://en.wikipedia.org/wiki/HTTP/2)

> [参考博客: 面试官问：你了解HTTP2.0吗？](https://juejin.im/post/5c0ce870f265da61171c8c66)
> [参考博客: HTTP/2 幕后原理](https://www.ibm.com/developerworks/cn/web/wa-http2-under-the-hood/index.html)
> [参考博客: HTTP/2](http://www.hollischuang.com/archives/2066)
> [参考博客: HTTP/2 服务器推送（Server Push）教程](http://www.ruanyifeng.com/blog/2018/03/http2_server_push.html)  

> 新概念： 
1. 流（Stream）：已建立的TCP连接上的双向字节流，可以承载一个或多个消息。 一个TCP连接上可以有任意数量的流。
1. 消息（Message）：一个完整的HTTP请求或响应，由一个或多个帧组成。特定消息的帧在同一个流上发送，这意味着一个HTTP请求或响应只能在一个流上发送。
1. 帧（Frame）：通信的基本单位。

> 新实现
1. 二进制格式（Binary Format） 
    - HTTP2性能提升的核心就在于二进制分帧层。HTTP2是二进制协议
    - 1.1响应是文本格式，而2.0把响应划分成了两个帧，HEADERS（首部）和DATA（消息负载） 是帧的类型

1. 多路复用（MultiPlexing）
    - HTTP2建立一个TCP连接，一个连接上面可以有任意多个流（stream），消息分割成一个或多个帧在流里面传输。帧传输过去以后，再进行重组，形成一个完整的请求或响应。这使得所有的请求或响应都无法阻塞。

1. header压缩 (HPACK算法实现)
    - 在1.X版本中，首部用文本格式传输，通常会给每个传输增加500-800字节的开销。现在打开一个网页上百个请求已是常态
    - 而每个请求带的一些首部字段都是相同的，例如cookie、user-agent等。HTTP2为此采用HPACK压缩格式来压缩首部。头部压缩需要在浏览器和服务器端之间：
        - 维护一份相同的静态字典([Static Table Definition](https://httpwg.org/specs/rfc7541.html#static.table.definition))，包含常见的头部名称，以及常见的头部名称和值的组合
        - 维护一份相同的动态字典，可以动态的添加内容
        - 通过静态Huffman编码对传输的首部字段进行编码

1. 服务端推送（server push）
    - 服务器端推送使得服务器可以预测客户端需要的资源，主动推送到客户端。
    - 例如：客户端请求index.html，服务器端能够额外推送script.js和style.css。
    - 实现原理就是客户端发出页面请求时，服务器端能够分析这个页面所依赖的其他资源，主动推送到客户端的缓存，当客户端收到原始网页的请求时，它需要的资源已经位于缓存。
    - [Github: http2-chat-example](https://github.com/ebakhtarov/http2-chat-example )

> HTTP 2.0 才是正常的 ISO 七层协议的实现，增加了第六层表示层  
> 如果一开始就接触 HTTP 2.0，也就不会有所谓的“粘包”问题了，因为TCP发送数据时，数据本身就是结构化数据，实现了自我的边界定位

Java: JDK9 才正式支持

************************

## HTTP/3
> [wiki: HTTP/3](https://en.wikipedia.org/wiki/HTTP/3)

************************

# HTTPS
> [SSL & TLS](/Skills/Network/WebSecurity.md#ssl-tls)

## HTTPS 认证流程
1. 服务器生成一对密钥，私钥自己留着，公钥交给数字证书认证机构（CA）
1. CA进行审核，并用CA自己的私钥对服务器提供的公钥进行签名生成数字证书
1. 在 HTTPS 建立连接时，客户端从服务器获取数字证书，用CA的公钥（根证书）对数字证书进行验证，比对一致，说明该数字证书确实是CA颁发的
    - 得此结论有一个前提就是：客户端的CA公钥确实是CA的公钥(反例：中间人攻击)，即该CA的公钥与CA对服务器提供的公钥进行签名的私钥确实是一对。
    - 而CA又作为权威机构保证该公钥的确是服务器端提供的，从而可以确认该证书中的公钥确实是合法服务器端提供的。

注：为保证第3步中提到的前提条件，CA的公钥必须要安全地转交给客户端（CA根证书必须先安装在客户端）  
因此，CA的公钥一般来说由浏览器开发商内置在浏览器的内部。于是，该前提条件在各种信任机制上，基本保证成立。

## HSTS
> HTTP `Strict Transport Security` 强制让客户端使用HTTPS进行通信 

通常能在请求的 Response 的 Header 中看到 `Strict-Transport-Security: max-age=`	

> [MDN HSTS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)

************************

# CORS
> 跨域

> [mozilla CORS](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS)
> [阮一峰 跨域资源共享 CORS 详解](http://www.ruanyifeng.com/blog/2016/04/cors.html)
> [CORS详解.md](https://github.com/hstarorg/HstarDoc/blob/master/%E5%89%8D%E7%AB%AF%E7%9B%B8%E5%85%B3/CORS%E8%AF%A6%E8%A7%A3.md)
