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
    - 2.1. [WebSocket 拆包问题分析](#websocket-拆包问题分析)
- 3. [衍生框架](#衍生框架)
- 4. [Reactor Netty](#reactor-netty)

💠 2026-01-16 16:05:24
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

## WebSocket 拆包问题分析

**文本数据达到多大，会遇到拆包问题？**

WebSocket的拆包问题主要受以下因素影响：

1. **WebSocket协议层面的分片（Fragmentation）**
   - WebSocket协议本身支持分片传输，单个消息可以分成多个帧（Frame）
   - 分片由FIN标志位控制：FIN=0表示还有后续帧，FIN=1表示最后一帧
   - **理论上没有大小限制**，可以无限分片

2. **Netty缓冲区大小限制**
   - Netty使用`AdaptiveRecvByteBufAllocator`动态调整接收缓冲区大小
   - 初始大小：`AdaptiveRecvByteBufAllocator.DEFAULT_INITIAL` = **64字节**
   - 最大大小：`AdaptiveRecvByteBufAllocator.DEFAULT_MAXIMUM` = **65536字节（64KB）**
   - 缓冲区大小会根据读取情况在`SIZE_TABLE`中动态调整

3. **实际拆包触发条件**

```java
// WebSocket08FrameDecoder 解码逻辑
// 当接收到的数据不足以构成完整帧时，会等待更多数据
// 关键代码：io.netty.handler.codec.http.websocketx.WebSocket08FrameDecoder#decode

// 拆包发生的场景：
// 1. 单个WebSocket帧大小超过当前缓冲区大小
// 2. 多个帧在同一个TCP包中（粘包）
// 3. 单个帧被分割到多个TCP包中（拆包）
```

**具体数值分析：**

- **小数据（< 64字节）**：通常不会拆包，单次读取即可完成
- **中等数据（64字节 ~ 64KB）**：可能发生拆包，取决于：
  - 当前缓冲区大小（AdaptiveRecvByteBufAllocator动态调整）
  - TCP接收窗口大小
  - 网络MTU（通常1500字节）
- **大数据（> 64KB）**：**一定会发生拆包**，因为：
  - Netty默认最大接收缓冲区为64KB
  - 超过64KB的数据必须分多次读取
  - WebSocket帧会被分割到多个ByteBuf中

**WebSocket帧结构（RFC 6455）：**

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-------+-+-------------+-------------------------------+
|F|R|R|R| opcode|M| Payload len |    Extended payload length    |
|I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
|N|V|V|V|       |S|             |   (if payload len==126/127)   |
| |1|2|3|       |K|             |                               |
+-+-+-+-+-------+-+-------------+-------------------------------+
```

- **Payload长度字段**：
  - 0-125字节：直接编码在第二个字节的低7位
  - 126字节：后续2字节表示长度（最大65535字节）
  - 127字节：后续8字节表示长度（最大2^63-1字节）

**实际测试建议：**

```java
// 测试不同大小的数据是否会拆包
// 1. 小数据测试（< 1KB）
String smallData = "a".repeat(100);  // 100字节，通常不拆包

// 2. 中等数据测试（1KB ~ 64KB）
String mediumData = "a".repeat(10 * 1024);  // 10KB，可能拆包

// 3. 大数据测试（> 64KB）
String largeData = "a".repeat(100 * 1024);  // 100KB，一定会拆包
```

**解决方案：**

1. **调整缓冲区大小**（不推荐，影响内存）
   ```java
   // 在ChannelPipeline中设置
   channel.config().setRecvByteBufAllocator(
       new AdaptiveRecvByteBufAllocator(64, 1024, 65536 * 2)  // 增大最大缓冲区
   );
   ```

2. **使用WebSocket协议的分片机制**（推荐）
   - WebSocket08FrameDecoder已经支持分片
   - 确保正确处理FIN标志位
   - 在应用层组装完整消息

3. **应用层处理**
   ```java
   // 在WebSocketFrameAggregator中聚合分片
   pipeline.addLast(new WebSocketFrameAggregator(65536));  // 最大聚合64KB
   
   // 或自定义处理
   public class WebSocketFrameHandler extends SimpleChannelInboundHandler<WebSocketFrame> {
       private StringBuilder frameBuffer = new StringBuilder();
       
       @Override
       protected void channelRead0(ChannelHandlerContext ctx, WebSocketFrame frame) {
           if (frame instanceof TextWebSocketFrame) {
               TextWebSocketFrame textFrame = (TextWebSocketFrame) frame;
               frameBuffer.append(textFrame.text());
               
               // FIN=1表示最后一帧
               if (frame.isFinalFragment()) {
                   String completeMessage = frameBuffer.toString();
                   // 处理完整消息
                   processMessage(completeMessage);
                   frameBuffer.setLength(0);  // 清空缓冲区
               }
           }
       }
   }
   ```

**总结：**

- **理论上**：WebSocket协议支持无限大小的消息（通过分片）
- **实际上**：当数据**超过64KB**时，Netty的接收缓冲区限制会导致拆包
- **建议**：使用`WebSocketFrameAggregator`或自定义Handler处理分片，而不是增大缓冲区
- **最佳实践**：单条消息控制在64KB以内，或使用分片机制传输大数据

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

