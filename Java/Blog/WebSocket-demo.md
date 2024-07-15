---
title: Java WebSocket Demo
date: 2019-07-07 11:43:37
tags: 
    - Websocket
categories: 
    - Java 
---

💠

- 1. [Java中的Websocket](#java中的websocket)
- 2. [服务端](#服务端)
    - 2.1. [Javax](#javax)
        - 2.1.1. [事件处理](#事件处理)
        - 2.1.2. [服务端推送消息](#服务端推送消息)
    - 2.2. [SpringMVC](#springmvc)
    - 2.3. [Netty](#netty)
        - 2.3.1. [Reactor Netty](#reactor-netty)
    - 2.4. [Undertow](#undertow)
- 3. [性能测试对比](#性能测试对比)
- 4. [集群设计](#集群设计)
- 5. [客户端](#客户端)
    - 5.1. [Java](#java)
    - 5.2. [JS](#js)

💠 2024-07-12 11:40:30
****************************************
# Java中的Websocket
JSR-356

> [【Spring Boot】WebSocket 的 6 种集成方式 ](https://juejin.cn/post/7111132777394733064)

# 服务端
先说结论： 生产尽量使用Netty实现，Javax 和 SpringMvc只适合少量连接时使用(`但开发是真简单`)，详情见下方[性能测试对比](#性能测试对比)。

## Javax
Javax规范，Tomcat Jetty等容器实现

```java
@Configuration
public class WebSocketAutoConfig {
  @Bean
  public ServerEndpointExporter endpointExporter() {
    return new ServerEndpointExporter();
  }
}

@Slf4j
@Component
@ServerEndpoint("/websocket/{id}")
public class WebsocketServer {

	// 用于存储所有连接的session对象，从而获取所有连接
    private static Map<String, Session> connections = new HashMap<>();
    private Session session;

    @OnOpen
    public void onOpen(Session session, @PathParam("id") String id) {
        this.session = session;
        // 将有客户端连接时将session保存起来
        connections.put(id, session);
    }

    @OnMessage
    public void onMessage(String text) throws IOException {
        log.info("WebSocket连接数：" + connections.size());
        String[] s = text.split("]#!]");
        // 获取指定连接的session
        Session ses = connections.get(s[0]);
        ses.getBasicRemote().sendText(s[1]);
    }

    @OnError
    public void onError(Throwable throwable) {
        log.error(throwable.getMessage());
    }

    @OnClose
    public void onClosing() throws IOException {
    	// 关闭时将连接的session去除
        connections.remove(session);
        session.close();
    }
}
```

1. 使用类级别注解`@ServerEndpoint("uri路径")`，将类标注为一个WebSocket端点
1. 使用方法级别注解`@OnMessage`，使方法在WebSocket事件发生，而不在WebSocket消息发生时被调用

### 事件处理

| 注解         | 方法中可使用的形参                   |
| ---------- | ---------------------------------------- |
| @OnOpen    | WebSocket Session对象，EndpointConfig对象，URI中的参数(需使用@PathParam) |
| @OnMessage | WebSocket Session对象，EndpointConfig对象，URI中的参数(需使用@PathParam)，消息 |
| @OnError   | Throwable对象，Session，URI中的参数(需使用@PathParam) |
| @OnClose   | CloseReason，URI中的参数(需使用@PathParam)       |

### 服务端推送消息

WebSocket中 RemoteEndpoint 接口和它的子类( RemoteEndpoint.Basic 和 RemoteEndpoint.Async )提供了发送消息的所有方法，我们可以从Session中获取到RemoteEndpoint实例，从而发送消息  
如：`session.getBasicRemote().sendText(text);`

************************

## SpringMVC
SpringMVC封装 Tomcat Jetty等容器实现

```java
@Slf4j
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    @Autowired
    private MyWebSocketHandler socketHandler;
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(socketHandler, "/ws/*/").setAllowedOrigins("*");
    }


    /**
     * 该设置对 Javax 方式也生效
     * @see org.apache.tomcat.websocket.WsFrameBase#WsFrameBase
     * @see java.nio.HeapByteBuffer
     * @see java.nio.HeapByteBuffer
     */
    @Bean
    public ServletServerContainerFactoryBean createWebSocketContainer() {
        ServletServerContainerFactoryBean container = new ServletServerContainerFactoryBean();
        // ws 传输数据的时候，单个消息过大会导致缓冲区溢出，接收不到该消息，所以按需设置bufferSize的大小
        // 注意： 这里设置的大小是每个连接初始化 HeapByteBuffer 的实际大小，也就是设置多大每个连接就会占用多大内存，要慎重考虑
        // https://my.oschina.net/xiaoshushu/blog/1586349

        // 此时一个Ws连接会申请4Kib堆内存
        int kib = 1024;
        int quota = 2;
        container.setMaxTextMessageBufferSize(quota * kib); // HeapCharBuffer
        container.setMaxBinaryMessageBufferSize(quota * kib); // HeapByteBuffer

        container.setMaxSessionIdleTimeout(15 * 60000L);
        return container;
    }
}

@Slf4j
@Service
public class MyWebSocketHandler extends TextWebSocketHandler {

    /**
     * ws建立连接
     * @param session websocket session
     */
    @Override
    public void afterConnectionEstablished(WebSocketSession session) {
    }

    /**
     * ws连接断开
     */
    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) {
    }

    /**
     * ws收到消息时的方法
     */
    @Override
    protected void handleTextMessage(WebSocketSession session, TextMessage message) {
    }
}
```
> 使用
1. 推送消息 session.sendMessage(new TextMessage("text"));

## Netty
> [Gitee： Demo](https://gitee.com/gin9/JavaBase/tree/master/netty/src/main/java/netty/websocket)  
> [Netty websocket springboot starter](https://gitee.com/gin9/netty-ws-starter)  

[SpringBoot整合Netty处理WebSocket（支持url参数）](https://blog.csdn.net/RisenMyth/article/details/104441155)

通过go开发的客户端压测`在多个Docker容器中运行（规避65535个数的端口限制）`, 16G电脑可以轻松发起和支撑百万级ws活跃连接。

### Reactor Netty
> [Official Doc](https://projectreactor.io/docs/netty/release/reference/index.html#http-server)

[Gitee： Demo](https://gitee.com/gin9/JavaBase/tree/master/netty/src/main/java/reactor/websocket) `设计和开发方式和传统Netty不一样，底层用的Netty`

## Undertow

> [doc](http://undertow.io/undertow-docs/undertow-docs-2.0.0/index.html#websockets)

************************

# 性能测试对比
- 相同的 JDK，JVM参数，处理逻辑 等。
- 指标：最大连接数，请求应答模型 延迟分布情况、吞吐量

> 压测过程中遇到的问题
1. 客户端发起连接需要设置最大打开文件数 ulimit -n 80000 
1. 服务端建立到 28232 个连接后 遇到 Cannot assign requested address 
    - `cat /proc/sys/net/ipv4/ip_local_port_range` 设置项代表Linux作为客户端(与服务端建立连接时会在区间内随机分配一个端口给客户端进程)可分配的端口范围（防止耗尽端口）
    - 临时修改 `echo 1024 65000 > /proc/sys/net/ipv4/ip_local_port_range`
    - 如果客户端在Docker容器中，需在 docker run 时加上 `--sysctl net.ipv4.ip_local_port_range="1024 65000"`

************************

> 结论 Netty性能更好，javax SpringMVC 实现成本更低
- 得益于Netty的IO架构，Buffer设计机制，资源占用和吞吐量远胜于Tomcat实现。
    - Tomcat 缓冲区实现为 `org.apache.tomcat.websocket.WsFrameBase#WsFrameBase` 使用的 ByteBuffer 直接按最大缓冲区分配容量 **堆内存**
        - 缺点：当某个ws业务偶尔会大数据收发，平时使用数据包很小（例如启动游戏时数据初始化和游戏过程），比较难配置最大容量。
        - 配置太大则支撑连接数会下降，配置太小读不到数据无法支撑业务 或 降低业务体验（如果容量很小数据要多轮，游戏初始化的等待时间就会更长）
    - Netty中使用到的是 池化内存`PooledByteBufAllocator` 和申请时扩缩容机制 `AdaptiveRecvByteBufAllocator` 大大降低了数据读取时占用的缓冲内存，平衡了缓存池利用率和数据读取效率 **堆外内存**
- javax MVC 这两种底层实现都是Tomcat等Web容器，性能没太大区别，优势是开发成本很低

> 基础环境
- 硬件 i5-10400F CPU @ 2.90GHz 
- JVM参数： -Xmx1000m
- 服务端：消息逻辑为收到文本ping返回文本pong， 设置最大读缓存大小为64K
- 客户端：连续创建连接，定时每分钟发送ping文本

> 结果
- Javax 约2500个后OOM 
- SpringMVC 约2600个后OOM 
- Netty 正常建立3000个连接

************************

> 资源对比

CPU占用都不高 0.5%以下波动

| 连接数 | Javax | Mvc | Netty | Jetty |
|:---|:---|:---|:---|:---|
| 1000 | 占用300M | 占用300M |  |  |
| 3000 | 占用850M | 占用850M | 占用150M内存 |  |

************************

# 集群设计
核心矛盾在于长连接是有状态的且无法共享，但通常应用服务端都是无状态的集群，方便横向快速扩容

> 简单实现 缺点：消息冗余推送
1. 用Redis或者Nacos等注册中心维护一份用户id和服务器ip的映射
1. 服务端主动推消息时从注册中心拿到用户id所在的服务器，再将消息转发过去做真正的推送

************************

# 客户端
## Java
Java WebSocket客户端端点

```java
@ClientEndpoint
public class WebSocketClient {

    private Session session;

    @OnOpen
    public void onOpen(Session session) {
        this.session = session;
    }

    @OnMessage
    public void onMessage(String text) throws IOException {
        session.getBasicRemote().sendText(text);
    }

    @OnError
    public void onError(Throwable throwable) {
        log.error(throwable.getMessage());
    }

    @OnClose
    public void onClosing() throws IOException {
        log.info("连接关闭");
        session.close();
    }

    public void sendMessage(String toId, String text) throws IOException {
        text = toId + "]#!]" + text;
        onMessage(text);
    }
	
	// 连接服务器端点
    public static WebSocketClient connect(String url) throws Exception {
        WebSocketContainer wsc = ContainerProvider.getWebSocketContainer();
        WebSocketClient client = new WebSocketClient();
        wsc.connectToServer(client, new URI(url));
        return client;
    }
}
```

## JS
```js
    var ws = new WebSocket("ws:localhost:8080/websocket");
    ws.onopen = function () {
        ws.send("hello");
    };

    ws.onmessage = function (evt) {
        console.log(evt.data)
    };

    ws.onclose = function (evt) {
        console.log("error");
    };

    ws.onerror = function (evt) {
        console.log("error");
    };
```
