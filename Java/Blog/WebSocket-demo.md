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
    - 1.1. [WebSocket服务端](#websocket服务端)
        - 1.1.1. [Tomcat 方式](#tomcat-方式)
            - 1.1.1.1. [4个生命周期在注解式端点中的事件处理](#4个生命周期在注解式端点中的事件处理)
            - 1.1.1.2. [服务端推送消息](#服务端推送消息)
        - 1.1.2. [Spring-WebSocket](#spring-websocket)
        - 1.1.3. [Undertow](#undertow)
        - 1.1.4. [Netty](#netty)
        - 1.1.5. [Reactor Netty](#reactor-netty)
    - 1.2. [性能测试对比](#性能测试对比)
    - 1.3. [Websocket集群设计](#websocket集群设计)
    - 1.4. [客户端](#客户端)
        - 1.4.1. [Java](#java)
        - 1.4.2. [JS](#js)

💠 2023-10-10 12:10
****************************************
# Java中的Websocket
JSR-356

## WebSocket服务端

### Tomcat 方式

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

#### 4个生命周期在注解式端点中的事件处理

| 注解         | 方法中可使用的形参                   |
| ---------- | ---------------------------------------- |
| @OnOpen    | WebSocket Session对象，EndpointConfig对象，URI中的参数(需使用@PathParam) |
| @OnMessage | WebSocket Session对象，EndpointConfig对象，URI中的参数(需使用@PathParam)，消息 |
| @OnError   | Throwable对象，Session，URI中的参数(需使用@PathParam) |
| @OnClose   | CloseReason，URI中的参数(需使用@PathParam)       |

#### 服务端推送消息

WebSocket中 RemoteEndpoint 接口和它的子类( RemoteEndpoint.Basic 和 RemoteEndpoint.Async )提供了发送消息的所有方法，我们可以从Session中获取到RemoteEndpoint实例，从而发送消息  
如：`session.getBasicRemote().sendText(text);`

************************

### Spring-WebSocket

```java
@Slf4j
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    @Autowired
    private MyWebSocketHandler MyWebSocketHandler;
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(MyWebSocketHandler, "/ws/*/").setAllowedOrigins("*");
    }

    @Bean
    public ServletServerContainerFactoryBean createWebSocketContainer() {
        ServletServerContainerFactoryBean container = new ServletServerContainerFactoryBean();
        // ws 传输数据的时候，数据过大有时候会接收不到，所以在此处设置bufferSize
        // 注意： 这里设置的大小是每个连接初始化 HeapByteBuffer 的实际大小，也就是设置多大每个连接就会占用多大内存，要慎重考虑
        // https://my.oschina.net/xiaoshushu/blog/1586349
        // org.apache.tomcat.websocket.WsFrameBase#WsFrameBase 
        container.setMaxTextMessageBufferSize(512000);
        container.setMaxBinaryMessageBufferSize(512000);
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
1. 推送消息 session.sendMessage(new TextMessage("text"));

### Undertow

> [doc](http://undertow.io/undertow-docs/undertow-docs-2.0.0/index.html#websockets)

### Netty
> [Gitee： Demo](https://gitee.com/gin9/JavaBase/tree/master/netty/src/main/java/netty/websocket)

通过go开发的客户端在多个Docker容器中运行（解决65535个端口限制），16G电脑可以轻松发起和支撑百万级ws活跃连接。

### Reactor Netty
> [Official Doc](https://projectreactor.io/docs/netty/release/reference/index.html#http-server)

************************

## 性能测试对比
TODO 
- 相同JVM参数，处理逻辑 
- 指标：最大连接数，请求应答模型 延迟分布情况、吞吐量
- 多次测试：

> 遇到的问题和调整
1. 客户端发起连接需要设置最大打开文件数 ulimit -n 80000 
1. 服务端建立到 28232 个连接后 遇到 Cannot assign requested address 
    - `cat /proc/sys/net/ipv4/ip_local_port_range` 设置项代表Linux作为客户端(与服务端建立连接时会在区间内随机分配一个端口给客户端进程)可分配的端口范围（防止耗尽端口）
    - 临时修改 `echo 1024 65000 > /proc/sys/net/ipv4/ip_local_port_range`
    - 如果客户端在Docker容器中，需在 docker run 时加上 `--sysctl net.ipv4.ip_local_port_range="1024 65000"`

> 结论 Netty 更有优势

| 类型 | 内存 | 连接数 |
|:---|:---|:---|
| Tomcat |  |  |
| Netty |  |  |

## Websocket集群设计
TODO

核心矛盾在于长连接是有状态且无法共享，但是业务处理端都是无状态的集群

简单实现就是用Redis或者Nacos等注册中心，发送接收消息都从注册中心拿到ws连接所在服务器，再转发过去

************************

## 客户端
### Java
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

### JS
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
