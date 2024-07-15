---
title: EhCache
date: 2024-05-04 22:06:19
tags: 
categories: 
---

💠

- 1. [EhCache](#ehcache)

💠 2024-05-04 23:18:27
****************************************
# EhCache
[Ehcache](https://www.ehcache.org/)被Hibernate选中的默认缓存实现框架

特性：
- 多级缓存，相较于GuavaCache Caffeine纯内存框架，Ehcache支持内存，堆外内存，磁盘 
    - 堆外内存是为了`规避GC扫描成本`，但是相较于堆内存可以通过引用直接读取值，堆外内存则需要`序列化反序列化`来读写
- 支持集群
- 支持持久化
- 支持分布式缓存
    - RMI 组播
    - JMS 消息
    - JGroups
    - Terracotta
- 支持 `JSR107标准`以及使用非常广泛的`Spring Cache标准`

> [JAVA中使用最广泛的本地缓存？Ehcache的自信从何而来](https://juejin.cn/post/7167259989826863112)  

