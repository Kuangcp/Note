---
title: JavaRedis
date: 2018-11-21 10:56:52
tags: 
categories: 
---

**目录 start**

1. [Java使用redis](#java使用redis)
    1. [Jedis](#jedis)
        1. [jedis遇到的异常](#jedis遇到的异常)
    1. [Redisson](#redisson)
    1. [Lettuce](#lettuce)
    1. [vertx-redis-client](#vertx-redis-client)

**目录 end**|_2020-06-24 02:06_|
****************************************
# Java使用redis
> [Official List](https://redis.io/clients#java)

## Jedis
> [Github: Jedis](https://github.com/xetorthio/jedis) 简单直接 

- java实际测试类[JedisUtilsTest.java](https://github.com/Kuangcp/Maven_SSM/blob/master/src/test/java/redis/JedisUtilTest.java)

- jedis 使用后要disconnect释放连接,最新版本close就不用了，使用连接池就不用
- jedis 的事务 使用exec释放事务

### jedis遇到的异常
- Invocation of init method failed; nested exception is java.lang.NoSuchMethodError: org.springframework.core.serializer.support.DeserializingConverter
- 版本对不上，要Spring和Spring-data-redis 和 redis和commons-lang3对应
- 目前是4.1.7 + 1.6.0 + 2.9.0 + 3.3.2 编译通过了	

## Redisson
> [Github: Redisson](https://github.com/redisson/redisson)

> WatchDog机制
- org.redisson.RedissonBaseLock#renewExpiration 续约逻辑入口
    - 加锁时初始设置的过期时间为 异步线程续约的周期时间，所以不能设置太短，初始设置TTL后，异步线程来不及去续约key就过期删除了
    - Netty中的HashedWheelTimer实现定时调度 延时时使用的Lua脚本

- [watch dog](https://www.cnblogs.com/jelly12345/p/14699492.html)  
- [Redis分布式锁过期了但业务还没有执行完](https://www.51cto.com/article/679902.html)  

> 问题： 如果此时JVM发生大于TTL的FullGC，后续又恢复了，锁没有续约，被别的JVM进程抢到了锁
- 方案： 

*********************
## Lettuce
> [Official](https://lettuce.io/) | [Github:](https://github.com/lettuce-io/lettuce-core)

和 Spring Netty 结合紧密， 适合 Spring 系， 没有Jedis简洁

## vertx-redis-client
> [Github: vertx-redis-client](https://github.com/vert-x3/vertx-redis-client)

