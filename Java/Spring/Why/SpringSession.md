---
title: SpringSession
date: 2020-08-26 18:30:37
tags: 
    - Spring
categories: 
---

**目录 start**

1. [Spring-Session](#spring-session)
    1. [Websocket](#websocket)
        1. [Websocket 共享](#websocket-共享)

**目录 end**|_2020-08-26 18:31_|
****************************************
# Spring-Session 
- TODO 查看源码实现

## Websocket

> [websocket session](https://docs.spring.io/spring-session/docs/current/reference/html5/guides/boot-websocket.html) 

`可实现 websocket session 原始的 http session 超时等管理功能，无法实现 websocket 共享` 

### Websocket 共享

1. nginx 分发 redis 共享 如何实现
    - WebsocketSession 无法序列化，所以无法像普通WebSession那样做共享
