---
title: 限流
date: 2022-08-03 10:33:45
tags: 
categories: 
---

💠

- 1. [限流](#限流)
    - 1.1. [算法](#算法)
        - 1.1.1. [令牌桶](#令牌桶)
        - 1.1.2. [漏桶](#漏桶)
        - 1.1.3. [固定窗口](#固定窗口)
        - 1.1.4. [滑动窗口](#滑动窗口)
- 2. [组件方案](#组件方案)
    - 2.1. [Nginx](#nginx)
    - 2.2. [Guava](#guava)
    - 2.3. [Redis](#redis)
    - 2.4. [Hystrix](#hystrix)
    - 2.5. [concurrency-limits](#concurrency-limits)
- 3. [分布式Semaphore](#分布式semaphore)
    - 3.1. [Redis 实现](#redis-实现)
    - 3.2. [Oracle Coherence](#oracle-coherence)

💠 2024-09-20 11:10:09
****************************************
# 限流

> 目的
- 保护系统稳定性：过多的并发请求可能导致服务器内存耗尽、CPU 使用率饱和，从而引发系统响应慢、无法正常服务的问题。
- 防止资源滥用：确保有限的服务资源被合理公平地分配给所有用户，防止个别用户或恶意程序过度消耗资源。
- 优化用户体验：对于网站和应用程序而言，如果任由高并发导致响应速度变慢，会影响所有用户的正常使用体验。
- 保障安全：在网络层面，限流有助于防范 DoS/DDoS 攻击，降低系统遭受恶意攻击的风险。
- 运维成本控制：合理的限流措施可以帮助企业减少不必要的硬件投入，节省运营成本。


## 算法
> 令牌桶,漏桶,固定窗口,滑动窗口 都是对流量整形，削峰填谷，适用于常见REST接口。


如果是任务调度类场景，单个任务执行时间很长（分钟级），则不适用，可以考虑分布式Semaphore的实现，限制整个集群上下游的并行任务数。

### 令牌桶
固定速率生成令牌放入桶中，并支持预取，通过是否获得令牌来实现限流
- 允许当前请求获取超量资源（大于并发限制），下一次请求需要等待超额的时间

> [Guava ratelimiter 实现原理](https://cloud.tencent.com/developer/article/1408819)

### 漏桶
不支持突发流量, 通过限制流出速率，丢弃突发的流入流量来实现限流

### 固定窗口
通过限制固定时间窗口（例如自然时间1分钟 10:00 到 10:01 ）内请求数，超出部分丢弃，实现限流。

### 滑动窗口
通过限制滑动时间窗口（例如过去1分钟）内请求数，超出部分丢弃，实现限流。

************************

# 组件方案

## Nginx 

## Guava
RateLimiter 令牌桶实现
- 支持平滑发放令牌（例如限制每秒5并发，每个令牌的获取间隔大概在200ms左右）

## Redis
简易：zset 使用时间戳值来做滑动窗口,如果服务器间时间不同步，会在边界情况下超出设定的最大阈值。

> [详解Redisson分布式限流的实现原理 ](https://juejin.cn/post/7199882882138898489)  
> [分布式限流：基于 Redis 实现](https://pandaychen.github.io/2020/09/21/A-DISTRIBUTE-GOREDIS-RATELIMITER-ANALYSIS/)  

## Hystrix

## concurrency-limits 
[concurrency-limits](https://github.com/Netflix/concurrency-limits) 类似于 TCP拥塞控制算法

************************

# 分布式Semaphore

作用类似于 [JDK中的Semaphore](/Java/AdvancedLearning/JavaConcurrency.md#semaphore)，但是资源限制是分布式的，而不是单机，实现可以依赖Redis或MySQL等中间存储。

> [Ignite: Semaphore](https://ignite.apache.org/docs/latest/data-structures/semaphore)

## Redis 实现
> [分布式Semaphore](https://cloud.tencent.com/developer/article/1805219)  

1. 使用 Redission 中的 RSemaphore
1. **Lua脚本实现**，加一（获取资源）,判断是否超阈值超过则撤销加一，减一(释放资源) `自旋等待`
    - 命令： `EVAL "local cnt = redis.call('incr', KEYS[1]);  if (tonumber(cnt) > tonumber(ARGV[1]) ) then redis.call('decr', KEYS[1]); return 0; else return 1; end " 1 lockA 3`
    ```java
    public static final String Judge = "local cnt = redis.call('incr', KEYS[1]);" +
            "  if (tonumber(cnt) > tonumber(ARGV[1]) ) then redis.call('decr', KEYS[1]); return 0;" +
            " else return 1; end";

    public boolean acquire() {
        // 指定 lua 脚本，并且指定返回值类型
        DefaultRedisScript<Integer> redisScript = new DefaultRedisScript<>(Judge, Integer.class);
        // 参数一：redisScript，参数二：key列表，参数三：arg（可多个）
        Object lockB = redisTemplate.execute(redisScript, Collections.singletonList("lockB"), 3);
        if (Objects.isNull(lockB)) {
            return false;
        }
        return Integer.parseInt(lockB.toString()) > 0;
    }

    public String release() {
        Long val = redisTemplate.opsForValue().decrement("lockB");
        return val + "";
    }
    ```

> [分布式限流——Redis版分布式信号量原理](https://www.skypyb.com/2020/06/jishu/1538/)`负面参考：实现复杂有缺陷`  

## Oracle Coherence
[Coherence](https://docs.oracle.com/en/middleware/standalone/coherence/14.1.1.2206/develop-applications/implementing-concurreny-distributed-environment.html#GUID-8C7BBF82-EBF8-47A9-8EDC-E725221C1054)
