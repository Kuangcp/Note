---
title: Guava
date: 2018-11-21 10:56:52
tags: 
categories: 
    - 工具类库
---

💠

- 1. [Guava](#guava)
    - 1.1. [基础部分](#基础部分)
    - 1.2. [集合](#集合)
- 2. [独立组件](#独立组件)
    - 2.1. [RateLimiter](#ratelimiter)
    - 2.2. [EventBus](#eventbus)

💠 2024-04-22 00:47:57
****************************************
# Guava
> [Github地址](https://github.com/google/guava)  
> [官方手册](https://github.com/google/guava/wiki) `git clone https://github.com/google/guava.wiki.git`  
> [翻译版](http://ifeve.com/google-guava/)  
> [Guava Guide](https://www.baeldung.com/guava-guide)  

Guava工程包含了若干被Google的 Java项目广泛依赖 的核心库，例如：集合 collections 、缓存 caching 、原生类型支持 [primitives support] 、并发库 concurrency libraries 、通用注解 common annotations 、字符串处理 string processing 、I/O 等等。 所有这些工具每天都在被Google的工程师应用在产品服务中。

_包结构_
```
    com.google.common.annotations
    com.google.common.base
    com.google.common.collect
    com.google.common.io
    com.google.common.net
    com.google.common.primitives
    com.google.common.util.concurrent
```

## 基础部分
> Optional的设计和Java8的Optional是差不多的,Java8可能是参考的Guava。

## 集合

************************

# 独立组件
## RateLimiter
> 令牌桶算法实现

Beta 状态，官方TODO优化为nano级别，降低存储成本

> [RateLimiter限流原理解析](https://zhuanlan.zhihu.com/p/60979444)

## EventBus
> [官方文档](https://github.com/google/guava/wiki/EventBusExplained) | [Guava学习笔记：EventBus](http://www.cnblogs.com/peida/p/EventBus.html)
> [并发编程网 event bus](http://ifeve.com/google-guava-eventbus/) | [走进Guava](https://www.yeetrack.com/?p=1177)

```java
    // 快速使用
    EventBus eventBus = new EventBus();
    eventBus.register(new Object() {
        @Subscribe
        public void hehe(Integer num) throws InterruptedException {
            System.out.println(num + ":" + System.currentTimeMillis());
            Thread.currentThread().sleep(100);
        }
    });

    eventBus.post(1);
```
> 注意 只使用 `@Subscribe`注解的话，如果有两个同类事件触发，也是要排队执行的，因为包装的是 `Subscriber.SynchronizedSubscriber` 实现，同类事件并发执行需要加上 `@AllowConcurrentEvents`

基础组件

- Executor ： EventBus#executor 默认是当前线程，通常指定自定义线程池
- SubscriberRegistry ： Subscriber注册器，每个带有@Subscribe的方法会被注册到该类中
- Dispatcher ： 调度器，负责将事件，分发给事件对应的Subscriber，使用Executor执行这些Subscriber
    - PerThreadQueuedDispatcher 执行线程内将会按事件发布顺序进行消费， 执行线程间仍异步乱序。`ThreadLocal<Queue>` 实现线程间队列隔离
    - LegacyAsyncDispatcher 默认用于 AsyncEventBus，异步实现即可能出现不同的线程不同的事件消费顺序，同一线程对先后发布的事件消费顺序也可能不一致，注释都说这个有没有必要用队列 emmm
    - ImmediateDispatcher 无队列，立即投送事件给Subscriber，积压在Executor的队列中， 事件的消费可能有序可能无序取决于不同的Subscriber实现
- SubscriberExceptionHandler ： 异常处理器

