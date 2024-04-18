---
title: Cache
date: 2019-05-13 11:15:40
tags: 
categories: 
---

💠

- 1. [缓存](#缓存)
- 2. [类型](#类型)
    - 2.1. [客户端](#客户端)
    - 2.2. [服务端](#服务端)
    - 2.3. [数据库](#数据库)
    - 2.4. [分布式缓存](#分布式缓存)
        - 2.4.1. [Redis cluster](#redis-cluster)
- 3. [场景](#场景)
    - 3.1. [缓存雪崩 Cache Avalanche](#缓存雪崩-cache-avalanche)
    - 3.2. [缓存穿透 Cache Penetration](#缓存穿透-cache-penetration)
    - 3.3. [缓存击穿/崩溃 Cache Breakdown](#缓存击穿崩溃-cache-breakdown)
    - 3.4. [缓存一致性](#缓存一致性)

💠 2024-04-19 01:14:48
****************************************
# 缓存
> 用时效和空间换时间

> 从Web应用系统的流程上可分为 客户端 服务端 数据库

# 类型
## 客户端
> 浏览器
- 静态资源缓存，Cookie，各种 *Storage， IndexDB

> PC端原生
- 配置文件，SQLite，LevelDB

## 服务端

- 应用内存: Java的 GuavaCache Caffeine 

- [Redis](/Database/Redis.md)
- [Memcache](/Database/Memcache.md)

************************

## 数据库
会话缓存

************************

## 分布式缓存
> 使用分布式共识算法构建出一个集群，将读写压力摊分到集群内节点上。

### Redis cluster 


************************

# 场景

## 缓存雪崩 Cache Avalanche
缓存层大量缓存过期，或者整个缓存层崩溃， 导致大量流量直接访问上游资源层

## 缓存穿透 Cache Penetration
缓存层和上游资源层都没有查询的数据

## 缓存击穿/崩溃 Cache Breakdown
缓存层部分数据过期了，并且突增大量流量直接访问上游资源层，去查询这部分过期的数据

## 缓存一致性
> [缓存和数据库一致性问题，看这篇就够了 ](http://kaito-kidd.com/2021/09/08/how-to-keep-cache-and-consistency-of-db/)
