---
title: Caffeine
date: 2019-05-13 11:15:40
tags: 
categories: 
---

💠

- 1. [Caffeine](#caffeine)
    - 1.1. [使用](#使用)
        - 1.1.1. [SpringBoot集成](#springboot集成)
    - 1.2. [设计](#设计)
        - 1.2.1. [缓存类型](#缓存类型)
        - 1.2.2. [驱逐策略](#驱逐策略)
        - 1.2.3. [持久化](#持久化)
        - 1.2.4. [统计](#统计)

💠 2024-09-20 11:10:09
****************************************
# Caffeine
> [Github](https://github.com/ben-manes/caffeine)  

> [本地缓存无冕之王Caffeine Cache ](https://mp.weixin.qq.com/s?__biz=Mzg4Nzc3NjkzOA==&mid=2247486885&idx=1&sn=37c7a9461402bd97822295cf51361777&chksm=cf847e60f8f3f776eb3b477decfbac55dc8b7ae1cf607ef68fbee89dbe02d40a800a92fabec7#rd)

## 使用

> [Introduction to Caffeine](https://www.baeldung.com/java-caching-caffeine)  

### SpringBoot集成
配置文件方式
```yml
spring:
  cache:
    type: caffeine
    cache-names:
    - userCache
    caffeine:
      spec: maximumSize=1024,refreshAfterWrite=60s
```

Bean方式
```java
    @Bean
    public CacheManager cacheManager() {
        CaffeineCacheManager cacheManager = new CaffeineCacheManager();
        cacheManager.setCaffeine(caffeineCacheBuilder());
        return cacheManager;
    }

    Caffeine<Object, Object> caffeineCacheBuilder() {
        return Caffeine.newBuilder()
                .initialCapacity(100)
                .maximumSize(500)
                .expireAfterAccess(10, TimeUnit.MINUTES)
                .recordStats();
    }
```

```java
    Cache<Integer, String> flowNameCache = Caffeine.newBuilder()
            .initialCapacity(100)
            .maximumSize(1000)
            .expireAfterAccess(10, TimeUnit.MINUTES)
            .recordStats().build();
```

************************

## 设计
> [基于 W-TinyLFU 缓存淘汰算法](/Skills/Cache/Cache.md#缓存淘汰算法)  
> [Caffeine Efficiency](https://github.com/ben-manes/caffeine/wiki/Efficiency)  

### 缓存类型
- Cache 单纯实现缓存 写入和读取
    - 在获取缓存值时如果想要原子性实现 不存在就创建 则调用 `get(key, key -> value)` 方法，并发调用时后续的线程会阻塞等待，如果不想感知此类阻塞就调用`getIfPresent()`即刻返回
    - 可以据此实现缓存过期时一个线程去加载缓存，其他线程等待值的常见场景。
- Loading Cache
    - 缓存不存在时，调用get时将会触发调用指定的Loader逻辑去加载缓存`类似于CDN中的回源操作`。并发调用get时阻塞后续线程
    - 可以据此实现多级缓存。Loader逻辑实现去DB等源去获取数据再写入缓存
- Async Cache
    - 是Cache的一个变体，其响应结果均为CompletableFuture
    - 默认情况下，缓存计算使用`ForkJoinPool.commonPool()`作为线程池，如果想要指定线程池，则可以覆盖并实现Caffeine.executor(Executor)方法。
        - 如果缓存的数据是`纯CPU计算`得到的，推荐默认的FJ线程池，如果是需要通过网络IO获取的数据，`建议使用独立的IO线程池`
    - 并发调用 `get(key, k -> value)`时，会返回 **同一个CompletableFuture对象**
    - 由于返回结果本身不进行阻塞，可以根据业务设计自行选择阻塞等待或者非阻塞。
- Async Loading Cache
    - Loading Cache和Async Cache的功能组合。
    - Async Loading Cache支持以异步的方式，对缓存进行自动加载。线程池设置同上

### 驱逐策略
- 基于容量回收 `W-TinyLFU`
- 基于时间回收 
- 基于引用回收 

### 持久化


### 统计
Caffeine内置了数据收集功能，通过Caffeine.recordStats()方法，可以打开数据收集。这样Cache.stats()方法将会返回当前缓存的一些统计指标，例如：
- hitRate：查询缓存的命中率。
- evictionCount：被驱逐的缓存数量。
- averageLoadPenalty：新值被载入的平均耗时

