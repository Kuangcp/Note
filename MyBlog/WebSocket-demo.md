---
title: WebSocket Demo
date: 2019-07-07 11:43:37
tags: 
    - Websocket
categories: 
    - Java 
---

**目录 start**
 
1. [一个简单的WebSocket示例](#一个简单的websocket示例)
    1. [建立WebSocket端点](#建立websocket端点)
        1. [4个生命周期在注解式端点中的事件处理](#4个生命周期在注解式端点中的事件处理)
        1. [Java端发送消息](#java端发送消息)
    1. [前端连接端点](#前端连接端点)
1. [Demo](#demo)

**目录 end**|_2019-10-19 17:04_|
****************************************
#  一个简单的WebSocket示例

## 建立WebSocket端点

1. 创建一个Java类
2. 使用类级别注解`@ServerEndpoint("uri路径")`，将类标注为一个WebSocket端点
3. 使用方法级别注解`@OnMessage`，使方法在WebSocket事件发生，而不在WebSocket消息发生时被调用

```java
@ServerEndpoint("/echo")
public class EchoServer {

    @OnMessage
    public String echo(String s) {
        return "你好：" + s;
    }
}
```

### 4个生命周期在注解式端点中的事件处理

| 注解         | 方法中可使用的形参                   |
| ---------- | ---------------------------------------- |
| @OnOpen    | WebSocket Session对象，EndpointConfig对象，URI中的参数(需使用@PathParam) |
| @OnMessage | WebSocket Session对象，EndpointConfig对象，URI中的参数(需使用@PathParam)，消息 |
| @OnError   | Throwable对象，Session，URI中的参数(需使用@PathParam) |
| @OnClose   | CloseReason，URI中的参数(需使用@PathParam)       |

### Java端发送消息

WebSocket中 RemoteEndpoint 接口和它的子类( RemoteEndpoint.Basic 和 RemoteEndpoint.Async )提供了发送消息的所有方法，我们可以从Session中获取到RemoteEndpoint实例，从而发送消息  
如：`session.getBasicRemote().sendText(text);`

## 前端连接端点
```js
    var ws = new WebSocket("WebSocket端点URL");
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
# Demo

WebSocket服务器

```java
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
