---
title: OKHTTP
date: 2024-02-02 14:22:14
tags: 
categories: 
---

💠

- 1. [OKHTTP](#okhttp)

💠 2026-02-06 16:03:43
****************************************
# OKHTTP
> [Official Site](https://square.github.io/okhttp/)  

https://square.github.io/okhttp/
https://square.github.io/okhttp/calls/
https://blog.csdn.net/sinat_36553913/article/details/104054028
https://blog.csdn.net/sinat_36553913/article/details/104054160
https://www.jianshu.com/p/da5c303d1df4?tdsourcetag=s_pcqq_aiomsg
https://blog.csdn.net/hdu2013/article/details/109229625
https://zhuanlan.zhihu.com/p/116777864

https://www.jianshu.com/p/f038d2438fcf
https://www.jianshu.com/p/132733115f95

https://www.jianshu.com/p/d7eced552553

> 核心源码流程
- okhttp3.Dispatcher 异步请求调度
    - maxRequests：默认 64（全域名总并发数）。
    - maxRequestsPerHost：默认 5（单个域名下的最大并发数）。
- okhttp3.internal.connection.RealConnectionPool TCP连接池 
    - okhttp3.ConnectionPool 默认最大空闲连接数为 5 个，存活时间为 5 分钟


> SSE 场景

```java
// 1. 定义连接池：增加空闲连接数以备复用
ConnectionPool connectionPool = new ConnectionPool(100, 5, TimeUnit.MINUTES);

// 2. 定义调度器：这是支持高并发长连接的关键
Dispatcher dispatcher = new Dispatcher();
dispatcher.setMaxRequests(200);         // 整体最大并发
dispatcher.setMaxRequestsPerHost(100);  // 单个域名的最大并发（需大于你的 SSE 数量）

// 3. 构建 OkHttpClient
OkHttpClient client = new OkHttpClient.Builder()
        .connectionPool(connectionPool)
        .dispatcher(dispatcher)
        .readTimeout(0, TimeUnit.MILLISECONDS) // SSE 场景通常需要取消读取超时
        .build();
```