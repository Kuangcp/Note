# Netty
RocketMQ、Elasticsearch、gRPC、Apache Dubbo、Spring5、HSF、 Zookeeper、Spark、Hadoop等等 的网络层均使用到Netty。

> 常见优势

开发门槛低：API 使用简单；  
定制能力强：可以通过 ChannelHandler对通信框架进行灵活地扩展；  
Handler强大：预置了多种编解码器，支持多种主流协议，对传输中粘包和拆包有现成解决方案，有完善的断连，idle(心跳检测)等异常处理；  
高性能：与其他业界主流的 NIO 框架对比，Netty  的综合性能最优；  
社区活跃，版本迭代周期短，发现的 BUG 可以被及时修复，同时更多的新功能会加入；经历了大规模的商业应用考验，质量有验证；  

> 实践

1. Tomcat 也有web连接组件 和 Netty 做的事情是类似的，是否可以替代?
