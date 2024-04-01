---
title: APM
date: 2024-03-23 17:52:21
tags: 
categories: 
---

💠

- 1. [APM](#apm)
    - 1.1. [SkyWalking](#skywalking)
    - 1.2. [Sentry](#sentry)
    - 1.3. [CAT](#cat)

💠 2024-04-01 18:38:23
****************************************
# APM
> Application performance Management

SkyWalking、Zipkin、Pinpoint、CAT

> [Github: APM](https://github.com/topics/apm)

## SkyWalking
> [Official Site](http://skywalking.apache.org/)  | [Downloads](https://skywalking.apache.org/downloads/)]

[server](https://hub.docker.com/r/apache/skywalking-oap-server) | [ui](https://hub.docker.com/r/apache/skywalking-ui)

```sh
docker run --name oap -p 12340:1234 -p 11800:11800 -p 12800:12800  -d apache/skywalking-oap-server:8.3.0-es6
docker run --name oap-ui -p 8080:8080 -d -e SW_OAP_ADDRESS=http://192.168.7.54:12800 apache/skywalking-ui
```

应用启动 java -javaagent:/opt/apache-skywalking-apm-bin/agent/skywalking-agent.jar -Dskywalking.agent.service_name=xxxtest -Dskywalking.collector.backend_service=127.0.0.1:11800 -jar application.jar

## Sentry 
[Github](https://github.com/getsentry/sentry)

[Docker compose 部署](https://github.com/getsentry/self-hosted)

感知应用异常:

[UncaughtExceptionHandlerIntegration](https://github.com/getsentry/sentry-java/blob/main/sentry/src/main/java/io/sentry/UncaughtExceptionHandlerIntegration.java) + LogAppender

************************

## CAT
> [陆金所 CAT 优化实践](https://www.infoq.cn/article/XvGZcW312MdatCKFMR8b)

> [Github: cat-docker](https://github.com/lghuntfor/cat-docker)  
> [深度剖析开源分布式监控CAT](https://tech.meituan.com/2018/11/01/cat-in-depth-java-application-monitoring.html)

感知应用异常： 

1. 实现日志框架的Appender基类，捕获Error到 `Cat.logError`，并手动声明该Appender到配置文件中
2. 手动设置**静态**的默认全局异常处理`Thread.setDefaultUncaughtExceptionHandler`，防止异常漏捕获。
    - SpringBoot项目里发生机率较小,因为基本都有Controller层的全局异常处理，且大部分请和逻辑从web端进入。
    - 只有自定义线程池,Scheduler线程池,Junit等地方，未捕获运行时异常，才会走默认逻辑异常栈被输出到标准错误 System.err 中。
