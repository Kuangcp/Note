---
title: Netty
date: 2018-11-21 10:56:52
tags: 
categories: 
---

💠

- 1. [Netty 使用](#netty-使用)
    - 1.1. [基础构件](#基础构件)
    - 1.2. [编解码相关](#编解码相关)
        - 1.2.1. [Protobuf](#protobuf)
- 2. [Websocket](#websocket)
- 3. [衍生框架](#衍生框架)
- 4. [Reactor Netty](#reactor-netty)

💠 2024-07-24 17:28:31
****************************************
# Netty 使用
> [NettyServer与SpringBoot集成](https://segmentfault.com/a/1190000004919133)  
> [Netty NIO 框架性能压测-短链接-对比Tomcat ](http://www.oschina.net/question/12_8749)

> [Github: Netty Example](https://github.com/netty/netty/tree/4.1/example)

## 基础构件

- Channel
    - Channel 是 NIO 基本的结构：一个 用于连接到实体(硬件设备 、文件 、网络套接字或程序组件)，能够执行一个或多个不同的 I/O 操作（读或写）的开放连接。

- Callback
    - 回调方法，常用于通知其他模块操作已完成

- Future
    - 提供了一种 通知应用操作已经完成 的方式： 这个 对象 作为一个 **异步操作结果的占位符**， 它在 将来的某个时候 完成并提供结果。
    - JDK java.util.concurrent.Future 提供的实现只允许您手动检查操作是否完成或阻塞了， Netty自己开发了ChannelFuture
    - ChannelFuture 可注册多个 ChannelFutureListener
        - 在Future操作完成时会调用 Listener的operationComplete 
        - 如果Future有执行异常返回的值是CauseHolder的实例包住了产生的Throwable
    - ChannelFutureListener 提供的通知机制不需要手动检查操作是否完成的   每个 Netty 的 outbound I/O 操作都会返回一个 ChannelFuture，这样就不会阻塞
    - 这就是 Netty 所谓的 `自底向上的异步和事件驱动`

- Event和Handler
    - 事件驱动：使用不同的Event通知状态的变更，Handler响应不同的Event。
    - Event 大致分类： 活跃或非活跃连接，数据读取，用户事件，异常
    - Handler 大致分类： 日志，数据转换，流控制，应用程序逻辑
    - Netty 的 ChannelHandler 是各种 处理程序的基本抽象 。每个 处理器实例 就是一个 回调 ，用于 执行对各种事件的响应
    - Netty 也提供了一组丰富的预定义的处理程序， 比如，各种协议的编解码器包括 HTTP 和 SSL/TLS

> 组合使用
- Future, Callback 和 Handler
    - Netty 的异步编程模型是建立在 future 和 callback 的概念上的 
    - **拦截操作** 和 **转换入站或出站数据** 只需要 提供回调 或 获取 future 操作返回的数据
    - 一个 Netty 的设计的主要目标是促进 关注点分离 ： `使业务逻辑从网络基础设施应用程序中分离`

- Selector, Event, EventLoop 
    - 通过 触发事件 从 应用程序 中 抽象 出 Selector ，从而避免手写调度代码
    - EventLoop 分配给每个 Channel 来处理所有的事件 ，包括 
        - 被注册关注的事件
        - 调度事件给 ChannelHandler
    - EventLoop 本身是由**单线程**去处理 Channel 所有的 I/O 事件，并且在 EventLoop 的生命周期内不会改变
    - 这个简单而强大的线程模型，使得 ChannelHandler 无需关注线程同步问题

## 编解码相关
> [Netty 编解码技术 数据通信和心跳监控案例](https://segmentfault.com/a/1190000013122610)  
> [Netty 拆包粘包和服务启动流程分析](https://segmentfault.com/a/1190000013039327)  
> [参考: Netty(三) 什么是 TCP 拆、粘包？如何解决？](https://crossoverjie.top/2018/08/03/netty/Netty(3)TCP-Sticky/)  

### Protobuf
> [Protobuf基础](/Java/AdvancedLearning/ClassFile.md#protobuf) | 
> [Netty中的使用案例](https://github.com/Kuangcp/NettyBook2/blob/master/src/main/java/com/phei/netty/codec/protobuf/README.md)
>> 要搭配处理半包的解码器

1. 使用 ProtobufVarint32FrameDecoder 
2. 继承自 LengthFieldBasedFrameDecoder
3. 继承自 ByteToMessageDecoder 自己处理

*****************************

# Websocket

> 接收数据buffer读取流程： 优势是新连接申请的内存低，实际使用中会对申请的buffer扩缩容，平衡缓存池利用率和读取效率
1. 读取Socket中数据入口： `io.netty.channel.nio.AbstractNioByteChannel.NioByteUnsafe#read`
    - 在 byteBuf = allocHandle.allocate(allocator); 调用中会依据以往读取值 `AdaptiveRecvByteBufAllocator.HandleImpl#guess()` 一个大小并使用
        - 其中 allocHandle 是 `AdaptiveRecvByteBufAllocator` allocator 是 `PooledByteBufAllocator`
    - 每次读取完成后都会 `AdaptiveRecvByteBufAllocator.HandleImpl#record()` 方法记录,按 AdaptiveRecvByteBufAllocator.SIZE_TABLE 做梯度扩缩容

> [参考: Netty WebSocket 拆包浅析](https://www.jianshu.com/p/30c26a755a87)  
- io.netty.handler.codec.http.websocketx.WebSocket08FrameDecoder#decode
- [ ] 文本数据达到多大，会遇到拆包问题

************************

# 衍生框架
> [netty-socketio](https://github.com/mrniko/netty-socketio)  
> [kcp-netty](https://github.com/szhnet/kcp-netty)  
> [Reactive Extension (Rx) Adaptor for Netty ](https://github.com/ReactiveX/RxNetty) RxNetty
> [Netty Servlet](https://github.com/wangzihaogithub/spring-boot-protocol)  


************************

# Reactor Netty
> [Doc](https://projectreactor.io/docs/netty/release/reference/index.html#about-doc)

> [个人 样例代码](https://github.com/Kuangcp/JavaBase/tree/master/netty/src/main/java/reactor)

