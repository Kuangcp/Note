---
title: Java WebSocket Demo
date: 2019-07-07 11:43:37
tags: 
    - Websocket
categories: 
    - Java 
---

**目录 start**

1. [简单 SpringBoot Websocket 示例](#简单-springboot-websocket-示例)
    1. [WebSocket服务端](#websocket服务端)
        1. [Tomcat 方式](#tomcat-方式)
            1. [4个生命周期在注解式端点中的事件处理](#4个生命周期在注解式端点中的事件处理)
            1. [服务端推送消息](#服务端推送消息)
        1. [Spring-WebSocket](#spring-websocket)
        1. [Undertow](#undertow)
        1. [Netty](#netty)
    1. [客户端](#客户端)
        1. [Java](#java)
        1. [JS](#js)

**目录 end**|_2021-05-18 21:48_|
****************************************
#  简单 SpringBoot Websocket 示例
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
