`目录 start`
 
- [Web安全](#web安全)
    - [Authenticate](#authenticate)
    - [SSL和TSL](#ssl和tsl)
    - [ARP断网攻击](#arp断网攻击)
    - [SYNFlood攻击](#synflood攻击)
        - [CSRF](#csrf)
        - [XSS](#xss)
    - [JWT](#jwt)

`目录 end` |_2018-09-12_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Web安全
> 关注常见的比如 XSS CSRF SQL注入 上传等问题的原理和修复方案。还有密码安全也基本上是面试必考点。
> 作为开发人员，需要详细了解安全问题的原理。 比如XSS的原理是因为用户将它的数据变成了代码，在页面中跑起来了，所以就可以为所欲为。 CSRF则是当用户不知情时，被黑客的网页通过图片、表单等请求时，
> 用户的登录态（Cookies）在不知情的情况下会被发送到服务器，导致用户在不知情的情况下被利用身份。 点击支持则是网页被嵌入到了其他网站中，并通过视觉隐藏的方式引导用户进行一些不知情的操作。 
> 上传导致的漏洞是因为用户的文件没有做好判断和处理，导致传上来的文件被当成程序执行了。 SQL注入是用户的数据被当成了表示SQL语义的部分，改变了原来的查询语句的语义，从而产生意料之外的结果。
> 反向代理服务器，构建在web服务器与 客户端之间，保护web服务器，服务器发送到客户端的请求被代理

## Authenticate

> [WWW-Authenticate](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate)

## SSL和TSL
> [SSL/TLS协议运行机制的概述](http://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)

## ARP断网攻击
> [ARP 断网攻击的原理是什么？如何完全防护？](https://www.zhihu.com/question/20338649)

********************
## SYNFlood攻击
> 洪水攻击 [参考博客](http://xfocus.net/articles/200106/208.html) SYN Flood是当前最流行的DoS（拒绝服务攻击）与DDoS（分布式拒绝服务攻击）的方式之一，这是一种利用TCP协议缺陷，发送大量伪造的TCP连接请求，从而使得被攻击方资源耗尽（CPU满负荷或内存不足）的攻击方式。  
> [参考博客](http://www.cnblogs.com/popduke/p/5823801.html)  

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
### CSRF
> CSRF (Cross Site Request Forgery) `跨站请求伪造` ，它讲的是你在一个浏览器中打开了两个标签页，其中一个页面通过窃取另一个页面的 cookie 来发送伪造的请求，
> 因为 cookie 是随着请求自动发送到服务端的。  

> [维基百科定义 CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery) |
> [百度百科 CSRF](https://baike.baidu.com/item/CSRF)

> [[Web 安全] 如何通过JWT防御CSRF](https://segmentfault.com/a/1190000003716037)
> [web安全之token和CSRF攻击](https://blog.csdn.net/qq_15096707/article/details/51307024)  
> [博客:CSRF漏洞的原理](https://www.zhuyingda.com/blog/b5.html)  
> [浅谈CSRF攻击方式](http://www.cnblogs.com/hyddd/archive/2009/04/09/1432744.html)  
> [参考提问下的回答](https://segmentfault.com/q/1010000000713614)

- [ ] 问题是 CSRF 只是非法获取Cookie做操作么, 自己用Nginx配置两个域名的web页面试试 CSRF 

### XSS
> Cross Site Scripting `跨站脚本攻击` 

> [xss攻击入门](http://www.cnblogs.com/bangerlee/archive/2013/04/06/3002142.html)  
> [ XSS攻击及防御 ](https://blog.csdn.net/ghsau/article/details/17027893)  
> [最新的黑客技术：详解XSS跨站脚本攻击 ](http://soft.yesky.com/security/hkjj/136/2233136.shtml) 


## JWT
> [理解JWT的使用场景和优劣](http://www.qingpingshan.com/rjbc/java/384762.html)

- [Blog:通过使用JWT来防御CSRF](https://segmentfault.com/a/1190000003716037)  
- [Blog:介绍JWT](blog.leapoahead.com/2015/09/06/understanding-jwt/)`其实JWT还经常用于设计用户认证和授权系统，甚至实现Web应用的单点登录。`  
- [Blog:单点登录](http://blog.leapoahead.com/2015/09/07/user-authentication-with-jwt/)  
- [Web 安全之 XSS、CSRF 和 JWT](https://juejin.im/entry/58e67673a22b9d00588e7148)

> [参考博客: 开箱即用 - jwt 无状态分布式授权](http://www.cnblogs.com/grissom007/p/6294746.html)

> 需要注意的是，不是什么数据都适合放在 Cookie、localStorage 和 sessionStorage 中的。使用它们的时候，需要时刻注意是否有代码存在 XSS 注入的风险。  
> 因为只要打开控制台，你就随意修改它们的值，也就是说如果你的网站中有 XSS 的风险，它们就能对你的 localStorage 肆意妄为。所以千万不要用它们存储你系统中的敏感数据



