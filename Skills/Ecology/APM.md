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

💠 2024-03-23 17:52:21
****************************************
# APM
> Application performance Management

SkyWalking、Zipkin、Pinpoint、CAT

> [Github: APM](https://github.com/topics/apm)

## SkyWalking
> [Official Site](http://skywalking.apache.org/)  | [Downloads](https://skywalking.apache.org/downloads/)]

[server](https://hub.docker.com/r/apache/skywalking-oap-server) | [ui](https://hub.docker.com/r/apache/skywalking-ui)

```
docker run --name oap -p 12340:1234 -p 11800:11800 -p 12800:12800  -d apache/skywalking-oap-server:8.3.0-es6
docker run --name oap-ui -p 8080:8080 -d -e SW_OAP_ADDRESS=http://192.168.7.54:12800 apache/skywalking-ui
```

应用启动 java -javaagent:/opt/apache-skywalking-apm-bin/agent/skywalking-agent.jar -Dskywalking.agent.service_name=xxxtest -Dskywalking.collector.backend_service=127.0.0.1:11800 -jar application.jar

## Sentry 
[Github](https://github.com/getsentry/sentry)

## CAT
> [陆金所 CAT 优化实践](https://www.infoq.cn/article/XvGZcW312MdatCKFMR8b)

> [Github: cat-docker](https://github.com/lghuntfor/cat-docker)  
