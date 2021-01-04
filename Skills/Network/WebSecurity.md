---
title: 网络安全
date: 2018-11-21 10:56:52
tags: 
    - 网络
categories: 
    - 计算机基础
---

**目录 start**

1. [网络安全](#网络安全)
    1. [中间人攻击](#中间人攻击)
1. [Web安全](#web安全)
    1. [Authenticate](#authenticate)
        1. [OAuth 2.0](#oauth-20)
        1. [JWT](#jwt)
    1. [Verfication](#verfication)
    1. [SSL TLS](#ssl-tls)
        1. [数字证书](#数字证书)
    1. [盗链与防盗链](#盗链与防盗链)
    1. [工具或平台](#工具或平台)
1. [攻击手段](#攻击手段)
    1. [ARP断网攻击](#arp断网攻击)
    1. [SYNFlood攻击](#synflood攻击)
    1. [ClickJacking](#clickjacking)
    1. [CSRF](#csrf)
        1. [解决方案](#解决方案)
    1. [XSS](#xss)

**目录 end**|_2021-01-04 10:29_|
****************************************

# 网络安全
> [PHP安全新闻早8点](https://github.com/Micropoor/Micro8)

## 中间人攻击
> [Man in the middle](/Skills/Network/MITM.md)

************************

# Web安全
> 关注常见的比如 XSS CSRF SQL注入 上传等问题的原理和修复方案。还有密码安全也基本上是面试必考点。
> 作为开发人员，需要详细了解安全问题的原理。 比如XSS的原理是因为用户将它的数据变成了代码，在页面中跑起来了，所以就可以为所欲为。 CSRF则是当用户不知情时，被黑客的网页通过图片、表单等请求时，
> 用户的登录态（Cookies）在不知情的情况下会被发送到服务器，导致用户在不知情的情况下被利用身份。 点击支持则是网页被嵌入到了其他网站中，并通过视觉隐藏的方式引导用户进行一些不知情的操作。 
> 上传导致的漏洞是因为用户的文件没有做好判断和处理，导致传上来的文件被当成程序执行了。 SQL注入是用户的数据被当成了表示SQL语义的部分，改变了原来的查询语句的语义，从而产生意料之外的结果。
> 反向代理服务器，构建在web服务器与 客户端之间，保护web服务器，服务器发送到客户端的请求被代理

## Authenticate
> [WWW-Authenticate](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate)

> [参考: 设计安全的账号系统的正确姿势](https://blog.coderzh.com/2016/01/03/security-design/)  
> [参考: 即使被拖库，也可以保证密码不泄露](https://blog.coderzh.com/2016/01/10/a-password-security-design-example/)  

### OAuth 2.0
- [OAuth 2.0授权框架](https://github.com/jeansfish/RFC6749.zh-cn/blob/master/index.md)

> [参考: 理解OAuth 2.0](http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html)  

************************

### JWT
> [jwt](https://jwt.io)`JSON WEB TOKEN`

> [理解JWT的使用场景和优劣](http://www.qingpingshan.com/rjbc/java/384762.html)

- [Blog:通过使用JWT来防御CSRF](https://segmentfault.com/a/1190000003716037)  
- [Blog:介绍JWT](blog.leapoahead.com/2015/09/06/understanding-jwt/)`其实JWT还经常用于设计用户认证和授权系统，甚至实现Web应用的单点登录。`  
- [Blog:单点登录](http://blog.leapoahead.com/2015/09/07/user-authentication-with-jwt/)  
- [Web 安全之 XSS、CSRF 和 JWT](https://juejin.im/entry/58e67673a22b9d00588e7148)

> [参考: 开箱即用 - jwt 无状态分布式授权](http://www.cnblogs.com/grissom007/p/6294746.html)

> 需要注意的是，不是什么数据都适合放在 Cookie、localStorage 和 sessionStorage 中的。使用它们的时候，需要时刻注意是否有代码存在 XSS 注入的风险。  
> 因为只要打开控制台，你就随意修改它们的值，也就是说如果你的网站中有 XSS 的风险，它们就能对你的 localStorage 肆意妄为。所以千万不要用它们存储你系统中的敏感数据

如何在无状态下，实现修改密码，过期时间等功能的思路，Token中存入: userId 过期时间 密码的部分Hash值

************************

## Verfication 
> 最常见和简单的就是 数字验证码, 通常能在一些公共服务的API中发现校验码的存在

**`CAPTCHA`**
> CAPTCHA 全称 “全自动区分计算机和人类的图灵测试”（Completely Automated Public Turing Test to Tell Computers and Humans Apart）  
> 它是一种区分用户是计算机还是人的计算程序，这种程序生成人类能很容易通过但计算机通不过的测试，并进行判定，人/机进行测试的过程称为一次“挑战”。

************************

## SSL TLS
> [SSL/TLS协议运行机制的概述](http://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)
> [SSL，TLS，HTTPS](https://www.cnblogs.com/songhan/archive/2012/08/01/2617970.html)


- [ ] 完善 SSL

### 数字证书
1. 基本概念：
    1. `CA (Certificate Authority)`  证书授权中心，是数字证书发放和管理的机构
    1. `根证书` 根证书是CA认证中心给自己颁发的证书,是信任链的起始点。安装根证书意味着对这个CA认证中心的信任。
    1. `数字证书` 数字证书颁发过程一般为：
        1. 用户首先产生自己的密钥对，并将公共密钥及部分个人身份信息传送给认证中心。
        1. 认证中心在核实身份后，将执行一些必要的步骤，以确信请求确实由用户发送而来。
        1. 认证中心将发给用户一个数字证书，该证书内包含用户的个人信息和他的公钥信息，同时还附有认证中心的签名信息。

- [Githhub:mkcert](https://github.com/FiloSottile/mkcert)`签发证书工具`

************************
## 盗链与防盗链
> [referer 教程](https://www.ruanyifeng.com/blog/2019/06/http-referer.html)

> [防盗链](https://www.jianshu.com/p/c02064db8b5b)

1. 利用 referer 来控制
    1. 实现简单，绕过也简单
1. 设想 中间使用一个认证中间件(请求静态文件需要携带token，token需要js方式计算获取，且有有效期)，提高盗链难度

************************


## 工具或平台
> [Official Site](https://www.zaproxy.org/)  

************************
# 攻击手段
## ARP断网攻击
> [ARP 断网攻击的原理是什么？如何完全防护？](https://www.zhihu.com/question/20338649)

************************

## SYNFlood攻击
> 洪水攻击 [参考博客](http://xfocus.net/articles/200106/208.html) SYN Flood是当前最流行的DoS（拒绝服务攻击）与DDoS（分布式拒绝服务攻击）的方式之一，这是一种利用TCP协议缺陷，发送大量伪造的TCP连接请求，从而使得被攻击方资源耗尽（CPU满负荷或内存不足）的攻击方式。  

> [参考博客 什么是SYN Flood攻击?](http://www.cnblogs.com/popduke/p/5823801.html)  

- Linux:
    - 修改文件 `sudo vim /etc/sysctl.conf `
    - 将注释取消 修改值: `net.ipv4.tcp_syncookies = 0`
    - 就能提高并发总量,但是并发量还是不能提高
```conf
    net.ipv4.tcp_syncookies = 0  
    #此参数是为了防止洪水攻击的，但对于大并发系统，要禁用此设置
    net.ipv4.tcp_max_syn_backlog=1024
    #参数决定了SYN_RECV状态队列的数量，一般默认值为512或者1024，即超过这个数量，系统将不再接受新的TCP连接请求，一定程度上可以防止系统资源耗尽。可根据情况增加该值以接受更多的连接请求。
    net.ipv4.tcp_tw_recycle=0
    #参数决定是否加速TIME_WAIT的sockets的回收，默认为0。
    net.ipv4.tcp_tw_reuse=0
    #参数决定是否可将TIME_WAIT状态的sockets用于新的TCP连接，默认为0。
    net.ipv4.tcp_max_tw_buckets
    #参数决定TIME_WAIT状态的sockets总数量，可根据连接数和系统资源需要进行设置。 
```

************************
## ClickJacking
点击劫持是一种视觉上的欺骗手段。攻击者使用一个透明的iframe，覆盖在一个网页上，然后诱使用户在网页上进行操作，此时用户将在不知情的情况下点击透明的iframe页面。通过调整iframe页面的位置，可以诱使用户恰好点击在iframe页面的一些功能性按钮上。

> [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)  

1. DENY：不能被嵌入到任何iframe或者frame中。
1. SAMEORIGIN：页面只能被本站页面嵌入到iframe或者frame中
1. ALLOW-FROM uri：只能被嵌入到指定域名的框架中

## CSRF
> CSRF (Cross Site Request Forgery) `跨站请求伪造` 

指在一个浏览器中打开了两个标签页，其中一个页面通过窃取另一个页面的 cookie 来发送伪造的请求  

例如: A站点某网页 a.html 有一个 image 标签 其 url 是B站点的URL，利用 cookie 会随着当前页面的请求自动发送到服务端的特性，A站点的cookie会发送至B站点

> [维基百科定义 CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery) |
> [百度百科 CSRF](https://baike.baidu.com/item/CSRF)

> [[Web 安全] 如何通过JWT防御CSRF](https://segmentfault.com/a/1190000003716037)
> [web安全之token和CSRF攻击](https://blog.csdn.net/qq_15096707/article/details/51307024)  
> [博客:CSRF漏洞的原理](https://www.zhuyingda.com/blog/b5.html)  
> [浅谈CSRF攻击方式](http://www.cnblogs.com/hyddd/archive/2009/04/09/1432744.html)  
> [参考提问下的回答](https://segmentfault.com/q/1010000000713614)

### 解决方案
> token
- 打开当前页面时服务端先传递一个token给前端，前端后续的请求都需要携带该token(作请求参数或者Header)，否则拒绝请求，这样能避免img标签方式的 CSRF

> Cookie 中的 SameSite属性 [Cookie详情](/Skills/Network/HTTP.md#Cookie)

************************

## XSS
> Cross Site Scripting `跨站脚本攻击` 

> [xss攻击入门](http://www.cnblogs.com/bangerlee/archive/2013/04/06/3002142.html)  
> [ XSS攻击及防御 ](https://blog.csdn.net/ghsau/article/details/17027893)  
> [最新的黑客技术：详解XSS跨站脚本攻击 ](http://soft.yesky.com/security/hkjj/136/2233136.shtml) 
