---
title: Java网络编程
date: 2018-11-21 10:56:52
tags: 
    - 网络
categories: 
    - Java
---

💠

- 1. [Java网络编程](#java网络编程)
    - 1.1. [基础](#基础)
        - 1.1.1. [代理](#代理)
            - 1.1.1.1. [JVM 级别代理](#jvm-级别代理)
            - 1.1.1.2. [操作系统代理](#操作系统代理)
            - 1.1.1.3. [OkHttp](#okhttp)
            - 1.1.1.4. [Apache HttpClient (5.x)](#apache-httpclient-5x)
            - 1.1.1.5. [Java 内置 HttpClient (JDK 11+)](#java-内置-httpclient-jdk-11)
            - 1.1.1.6. [代理层级总结](#代理层级总结)
    - 1.2. [Socket](#socket)
        - 1.2.1. [Tuning](#tuning)
    - 1.3. [Tips](#tips)

💠 2026-07-09 20:10:35
****************************************
# Java网络编程

> [参考: Java网络教程](http://ifeve.com/java-network/)
> [java proxy](https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html)

## 基础
> 获取主机网络信息

- [获取本地ip](https://github.com/looly/hutool/issues/428)  
- [Getting the IP address of the current machine using Java](http://stackoverflow.com/questions/9481865/getting-the-ip-address-of-the-current-machine-using-java)  

### 代理

#### JVM 级别代理

通过系统属性设置，作用于 `java.net` 包下的网络连接（`URLConnection`、`Socket` 等）：

```ini
# HTTP 代理
-Dhttp.proxyHost=proxy.example.com
-Dhttp.proxyPort=8080
-Dhttp.nonProxyHosts=localhost|127.0.0.1|*.local

# HTTPS 代理（JDK 1.5+ 独立配置）
-Dhttps.proxyHost=proxy.example.com
-Dhttps.proxyPort=8443

# SOCKS 代理（作用于 TCP 层，优先级低于 HTTP/HTTPS 代理）
-DsocksProxyHost=socks.example.com
-DsocksProxyPort=1080
```

或通过代码设置：

```java
System.setProperty("http.proxyHost", "proxy.example.com");
System.setProperty("http.proxyPort", "8080");
```

**可用 `ProxySelector` 统一管理：**

```java
ProxySelector.setDefault(new ProxySelector() {
    @Override
    public List<Proxy> select(URI uri) {
        if (uri.getHost().contains("internal")) {
            return Collections.singletonList(Proxy.NO_PROXY);
        }
        return Collections.singletonList(
            new Proxy(Proxy.Type.HTTP, new InetSocketAddress("proxy.example.com", 8080)));
    }

    @Override
    public void connectFailed(URI uri, SocketAddress sa, IOException ioe) {
        // 代理失败回调
    }
});
```

> 参考：[Java Networking and Proxies](https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html)

#### 操作系统代理

操作系统代理是桌面环境/系统级配置（Windows 注册表、macOS 网络偏好设置、Linux 环境变量 `http_proxy`/`https_proxy`），**JVM 不会自动读取**。

Java 标准库 **不感知** 系统代理设置。如需使用系统代理，有以下方式：

| 方式 | 说明 |
|------|------|
| `System.setProperty("java.net.useSystemProxies", "true")` | JDK 内置，仅 Windows/macOS 有效，Linux 无效 |
| 启动时读取环境变量手动注入 | `-Dhttp.proxyHost=$http_proxy` |
| 第三方库自动检测 | OkHttp/HttpClient 等工具内置系统代理探测 |

```java
// Windows/macOS 上启用系统代理探测
System.setProperty("java.net.useSystemProxies", "true");
// 之后 URLConnection 会自动使用系统代理配置（含 PAC 脚本）
```

**注意：** `java.net.useSystemProxies` 的局限性：
- Linux 下不生效
- 只能探测"默认代理"，复杂的 PAC/代理规则可能适配不完整
- 仅对 `java.net.URLConnection` 生效，Socket 直连不生效

#### OkHttp

OkHttp 代理配置层级（优先级从高到低）：

| 层级 | 配置方式 | 说明 |
|------|----------|------|
| 1. 代码显式指定 | `builder.proxy(Proxy.NO_PROXY)` 或 `builder.proxySelector(...)` | 最高优先级 |
| 2. `ProxySelector.getDefault()` | JVM 全局 `ProxySelector` | 默认会读取 JVM 系统属性代理或自定义 Selector |
| 3. `java.net.useSystemProxies` | 配合系统属性 | OkHttp 3.x 中通过 `proxySelector` 返回系统代理列表（`ProxyInfo`） |

```java
// 方式一：显式指定代理
OkHttpClient client = new OkHttpClient.Builder()
    .proxy(new Proxy(Proxy.Type.HTTP, new InetSocketAddress("proxy.example.com", 8080)))
    .build();

// 方式二：自定义 ProxySelector（可混合直连和代理）
OkHttpClient client2 = new OkHttpClient.Builder()
    .proxySelector(new ProxySelector() {
        @Override
        public List<Proxy> select(URI uri) {
            return Collections.singletonList(uri.getHost().contains("internal")
                ? Proxy.NO_PROXY
                : new Proxy(Proxy.Type.HTTP, new InetSocketAddress("proxy.example.com", 8080)));
        }
        @Override
        public void connectFailed(URI uri, SocketAddress sa, IOException ioe) {}
    })
    .build();

// 方式三：不设定，OkHttp 默认使用 ProxySelector.getDefault()
OkHttpClient client3 = new OkHttpClient();
```

**认证代理：**

```java
// 方式一：Authenticator
Authenticator.setDefault(new Authenticator() {
    @Override
    protected PasswordAuthentication getPasswordAuthentication() {
        if (getRequestorType() == RequestorType.PROXY) {
            return new PasswordAuthentication("user", "pass".toCharArray());
        }
        return null;
    }
});

// 方式二：OkHttp 拦截器添加 Proxy-Authorization 头
OkHttpClient client = new OkHttpClient.Builder()
    .proxyAuthenticator((route, response) -> {
        String credential = Credentials.basic("user", "pass");
        return response.request().newBuilder()
            .header("Proxy-Authorization", credential)
            .build();
    })
    .build();
```

#### Apache HttpClient (5.x)

```java
// 显式代理
HttpHost proxy = new HttpHost("proxy.example.com", 8080);
try (CloseableHttpClient client = HttpClients.custom()
        .setProxy(proxy)
        .build()) { ... }

// 使用系统代理（自动读取 JVM 属性或系统设置）
try (CloseableHttpClient client = HttpClients.createSystem()) { ... }
// createSystem() 内部会：
//   1. 读取 JVM 系统属性（http.proxyHost 等）
//   2. 读取 java.net.useSystemProxies（Windows/macOS）
//   3. 读取环境变量 http_proxy/https_proxy

// 路由级代理（不同目标用不同代理）
try (CloseableHttpClient client = HttpClients.custom()
        .setRoutePlanner((target, request, context) -> {
            if (target.getHostName().endsWith(".internal")) {
                return null; // 直连
            }
            return new HttpRoute(target, null, proxy, "https".equals(target.getSchemeName()));
        })
        .build()) { ... }
```

**认证代理（CredentialsProvider）：**

```java
CredentialsProvider credsProvider = new BasicCredentialsProvider();
credsProvider.setCredentials(
    new AuthScope("proxy.example.com", 8080),
    new UsernamePasswordCredentials("user", "pass".toCharArray()));

try (CloseableHttpClient client = HttpClients.custom()
        .setProxy(new HttpHost("proxy.example.com", 8080))
        .setDefaultCredentialsProvider(credsProvider)
        .build()) { ... }
```

#### Java 内置 HttpClient (JDK 11+)

```java
HttpClient client = HttpClient.newBuilder()
    .proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 8080)))
    .build();

// 使用系统属性代理
HttpClient client2 = HttpClient.newBuilder()
    .proxy(ProxySelector.getDefault())
    .build();

// 直连（绕过代理）
HttpClient client3 = HttpClient.newBuilder()
    .proxy(ProxySelector.of(InetSocketAddress.createUnresolved("proxy.example.com", 8080)))
    .build();

// 认证代理
HttpClient client4 = HttpClient.newBuilder()
    .proxy(ProxySelector.of(new InetSocketAddress("proxy.example.com", 8080)))
    .authenticator(new Authenticator() {
        @Override
        protected PasswordAuthentication getPasswordAuthentication() {
            if (getRequestorType() == RequestorType.PROXY) {
                return new PasswordAuthentication("user", "pass".toCharArray());
            }
            return null;
        }
    })
    .build();
```

#### 代理层级总结

```
应用层 ─ OkHttp / HttpClient ──── 1. 代码显式指定 proxy (最高优先级)
              │                    2. 自定义 ProxySelector
              │                    3. ProxySelector.getDefault()
              ▼
        ProxySelector ──────────── java.net.ProxySelector (全局)
              │
              ▼
        JVM 系统属性 ────────────── http.proxyHost / socksProxyHost 等
              │
              ▼
        操作系统代理 ────────────── useSystemProxies=true (非Linux)
                                    或手动传入环境变量
```

**关键原则：**
- 代码显式配置的代理优先级最高，覆盖其他所有设置
- JVM 系统属性代理作用于 `java.net` 层，但会被自定义 `ProxySelector` 覆盖
- `useSystemProxies` 需要显式开启，且跨平台表现不一致，生产环境建议显式配置
- OkHttp/HttpClient 默认行为是委托到 `ProxySelector.getDefault()`，间接使用 JVM 系统属性
- Apache HttpClient 的 `createSystem()` 能同时读取 JVM 属性和环境变量，最为完整

## Socket
> [码农翻身:张大胖的socket ](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513387&idx=1&sn=99665948d0b968cf15c5e7a01ffe166c&chksm=80d679e8b7a1f0febad077b57e8ad73bfb4b08de74814c45e1b1bd61ab4017b5041942403afb&scene=21#wechat_redirect)


### Tuning
> Connection reset
服务器关闭了Connection会返回“RST”而不是返回“FIN”标志。原因在于Socket.close()方法的语义和TCP的“FIN”标志语义不一样：
- 发送TCP的“FIN” 标志表示 我不再发送数据了
- Socket.close() 表示我不再发送也不接受数据了。
问题就出在“我不接受数据” 上，如果此时客户端还往服务器发送数据，服务器内核接收到数据，但是发现此时Socket已经close了，则会返回“RST”标志给客户端。
此时客户端就会提示：“Connection reset”。

> [Orderly (and Abortive) Connection Release in Java](https://docs.oracle.com/javase/1.5.0/docs/guide/net/articles/connection_release.html)  

************************

## Tips

- 得到URL指向文件的输入流
    - `new URL(url).openStream()`

