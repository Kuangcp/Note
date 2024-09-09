---
title: NettyDesign
date: 2024-06-16 16:48:43
tags: 
categories: 
---

💠

- 1. [Netty Design](#netty-design)
    - 1.1. [线程模型](#线程模型)
    - 1.2. [内存设计](#内存设计)

💠 2024-09-09 10:22:38
****************************************
# Netty Design
> [Netty序章之BIO NIO AIO演变](https://segmentfault.com/a/1190000012976683)

> [ 大白话聊聊Netty ](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247538543&idx=1&sn=bc9d1575e21b42f215cf61e0a9da264e&scene=58&subscene=0)
> [Netty 实战(精髓)](https://github.com/waylau/essential-netty-in-action)

> 源码解读
> [官方Demo](https://github.com/netty/netty/tree/4.1/example/src/main/java/io/netty/example)
> [Netty实战配套源码](https://github.com/ReactivePlatform/netty-in-action-cn)
> [Netty权威指南2 源码](https://github.com/Kuangcp/NettyBook2)

## 线程模型
[主次Reactor多线程模型](/Skills/CS/IO.md#reactor)

> Netty 
![](/Java/Ecosystem/Netty/img/001-reactor-netty.drawio.svg)

> [参考: 从线程模型的角度看 Netty 为什么是高性能的？ ](https://crossoverjie.top/2018/07/04/netty/Netty(2)Thread-model/)  


## 内存设计

> 直接内存

- -Dio.netty.noPreferDirect 是否运行通过底层api直接访问直接内存，默认：允许
- -Dio.netty.noUnsafe 是否允许使用sun.misc.Unsafe，默认：允许
- -Dio.netty.maxDirectMemory 设置最大值

************************
