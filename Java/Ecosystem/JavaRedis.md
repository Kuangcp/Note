---
title: JavaRedis
date: 2018-11-21 10:56:52
tags: 
categories: 
---

💠

- 1. [Java 使用 Redis](#java-使用-redis)
    - 1.1. [Jedis](#jedis)
        - 1.1.1. [jedis遇到的异常](#jedis遇到的异常)
    - 1.2. [Redisson](#redisson)
    - 1.3. [Lettuce](#lettuce)
    - 1.4. [vertx-redis-client](#vertx-redis-client)

💠 2024-09-14 11:51:16
****************************************
# Java 使用 Redis
> [Official List](https://redis.io/clients#java)

## Jedis
> [Github: Jedis](https://github.com/xetorthio/jedis) 简单直接 

[JedisUtilsTest.java](https://github.com/Kuangcp/Maven_SSM/blob/master/src/test/java/redis/JedisUtilTest.java)

- jedis 的事务 使用exec释放事务

### jedis遇到的异常
> Invocation of init method failed; nested exception is java.lang.NoSuchMethodError: org.springframework.core.serializer.support.DeserializingConverter
- 版本对不上，要Spring和Spring-data-redis 和 redis和commons-lang3对应
- 目前是4.1.7 + 1.6.0 + 2.9.0 + 3.3.2 编译通过了	

> [Jedis连接池 资源泄露](https://mistray.github.io/2020/08/21/Jedis%E8%BF%9E%E6%8E%A5%E6%B1%A0%E7%AB%9F%E7%84%B6%E4%BC%9A%E8%B5%84%E6%BA%90%E6%B3%84%E9%9C%B2/)`2.9.1版本bug`

************************

## Redisson
> [Github: Redisson](https://github.com/redisson/redisson)

优势
- 附带业务封装的API，限流(RSemaphore等)，分布式锁

> WatchDog机制
- org.redisson.RedissonBaseLock#renewExpiration 续约逻辑入口
    - 加锁时初始设置的过期时间为 异步线程续约的周期时间，所以不能设置太短，初始设置TTL后，异步线程来不及去续约key就过期删除了
    - Netty中的HashedWheelTimer实现定时调度 延时时使用的Lua脚本

- [watch dog](https://www.cnblogs.com/jelly12345/p/14699492.html)  
- [Redis分布式锁过期了但业务还没有执行完](https://www.51cto.com/article/679902.html)  


> 问题： 如果此时JVM发生大于TTL的FullGC，后续又恢复了，锁没有续约，被别的JVM进程抢到了锁
- 方案： 尽可能让锁TTL大于业务操作时间，释放锁时绑定线程或业务，避免误释放

*********************
## Lettuce
> [Official](https://lettuce.io/) | [Github:](https://github.com/lettuce-io/lettuce-core)

和 Spring 结合紧密，Spring Data Redis 的默认实现， 没有Jedis简洁

> 注意
- 当Redis集群节点信息变更时，默认的策略不保证会使用最新的节点数据，需要设置为周期更新节点信息 [Refreshing the cluster topology view](https://github.com/redis/lettuce/wiki/Redis-Cluster#user-content-refreshing-the-cluster-topology-view)
- 这个问题只会发生在Redis集群扩缩容，以及发生故障的时候，问题就会暴露出来，即使Redis集群保证了高可用，应用仍无法正常使用

## vertx-redis-client
> [Github: vertx-redis-client](https://github.com/vert-x3/vertx-redis-client)

