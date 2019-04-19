#  1、一个简单的WebSocket实例

## Java后台的建立一个简单的WebSocket端点

1. 创建一个Java类
2. 使用类级别注解`@ServerEndpoint("uri路径")`，将类标注为一个WebSocket端点
3. 使用方法级别注解`@OnMessage`，使方法在WebSocket事件发生，而不在WebSocket消息发生时被调用

### 具体代码如下：

```
@ServerEndpoint("/echo")
public class EchoServer {

    @OnMessage
    public String echo(String s) {
        return "你好：" + s;
    }
}
```



## 前端使用WebSocket

代码如下：

```
<script>
    var ws = new WebSocket("WebSocket端点路径");
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

</script>
```



# 2、WebSocket的生命周期

### 4个生命周期事件

1. 打开事件：此事件发生在端点建立新连接时并且在任意其他事件发生之前
2. 消息事件：此事件接收WebSocket对话中另一端发送的消息。他可以发生在WebSocket端点接收了打开事件之后并且在接收关闭事件关闭连接之前的任意时刻
3. 错误事件：此事件在WebSocket连接或者端点发生错误时产生
4. 关闭事件：此事件表示WebSocket端点的连接目前正在部分的关闭，他可以有参与连接的任意一个端点发出

### 4个生命周期在注解式端点中的事件处理

| 注解         | 方法中可使用的形参                                |
| ---------- | ---------------------------------------- |
| @OnOpen    | WebSocket Session对象，EndpointConfig对象，URI中的参数(需使用@PathParam) |
| @OnMessage | WebSocket Session对象，EndpointConfig对象，URI中的参数(需使用@PathParam)，消息 |
| @OnError   | Throwable对象，Session，URI中的参数(需使用@PathParam) |
| @OnClose   | CloseReason，URI中的参数(需使用@PathParam)       |

# 3、WebSocket发送消息

WebSocket中RemoteEndpoint接口和它的子类(RemoteEndpoint.Basic和RemoteEndpoint.Async)提供了发送消息的所有方法，我们可以从Session中获取到RemoteEndpoint实例，从而发送消息，如：`session.getBasicRemote().sendText(text);`



# 4、我的一对一的例子

- WebSocket服务器端点

```
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



- Java WebSocket客户端端点

```
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

# 5、Spring Boot使用原生的WebSocket

-   定义端点

    ```kotlin
    @Component
    @ServerEndpoint("/end/point/{id}")
    class ReceiveEndpoint {

        @Reference
        lateinit var sendService : SendService

        /**
        * 连接开启时.
        */
        @OnOpen
        fun onOpen(session: Session) {
            println("open")
        }

        /**
        * 消息接收.
        */
        @OnMessage
        fun onMessage(text : String) {
            println("message: " + text)
        }

        /**
        * 错误发生时.
        */
        @OnError
        fun onError(throwable: Throwable) {

        }

        /**
        * 连接关闭.
        */
        @OnClose
        fun onClose() {
            println("close")
        }

    }
    ```

-   配置WebSocket

    ```kotlin
    @Configuration
    open class WebSocketConfig {

        @Bean
        open fun serverEndpointExporter() : ServerEndpointExporter {
            return ServerEndpointExporter()
        }

    }
    ```
