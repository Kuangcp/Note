# Netty
> [Trustlin](https://github.com/trustin) `Netty Mina 的作者`  

Netty是由JBOSS提供的一个java开源框架。Netty提供异步的、事件驱动的网络应用程序框架和工具，用以快速开发高性能、高可靠性的网络服务器和客户端程序。

> [Netty4.x官方文档](http://netty.io/wiki/user-guide-for-4.x.html)  
> [Netty权威指南](https://javablog.net/book/3/netty-authoritative-guide.html)  

> [Netty 实战(精髓)](https://klose911.github.io/html/netty/netty.html)  
> [《Netty 实战》 Netty In Action 中文版](https://github.com/ReactivePlatform/netty-in-action-cn)

************************

> [手淘、微博一直钟情的 Netty框架是个什么鬼？](https://yq.aliyun.com/roundtable/53346)
> [对于Netty的十一个疑问  ](https://news.cnblogs.com/n/205413/)  
> [知乎: 通俗地讲，Netty 能做什么？](https://www.zhihu.com/question/24322387)  
> [为什么选择Netty作为基础通信组件？ ](https://my.oschina.net/zhaky/blog/760469)

RocketMQ、Elasticsearch、gRPC、Apache Dubbo、Spring5、HSF、 Zookeeper、Spark、Hadoop等等 的网络层均使用到Netty。

> 常见优势

开发门槛低：API 使用简单；  
定制能力强：可以通过 ChannelHandler对通信框架进行灵活地扩展；  
Handler强大：预置了多种编解码器，支持多种主流协议，对传输中粘包和拆包有现成解决方案，有完善的断连，idle(心跳检测)等异常处理；  
高性能：与其他业界主流的 NIO 框架对比，Netty  的综合性能最优；  
社区活跃，版本迭代周期短，发现的 BUG 可以被及时修复，同时更多的新功能会加入；经历了大规模的商业应用考验，质量有验证；  

> 实践

1. Tomcat 也有web连接组件 和 Netty 做的事情是类似的，是否可以替代?
