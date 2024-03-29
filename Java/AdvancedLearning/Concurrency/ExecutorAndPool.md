---
title: 线程池
date: 2019-04-19 12:42:09
tags: 
categories: 
---

💠

- 1. [线程池](#线程池)
    - 1.1. [常用API](#常用api)
    - 1.2. [分支合并框架 Fork/Join](#分支合并框架-forkjoin)
    - 1.3. [ScheduledThreadPoolExecutor](#scheduledthreadpoolexecutor)
    - 1.4. [Executor框架](#executor框架)
    - 1.5. [Spring](#spring)
        - 1.5.1. [ThreadPoolTaskExecutor](#threadpooltaskexecutor)
- 2. [实践](#实践)
    - 2.1. [线程池 参数优化&监控](#线程池-参数优化&监控)
    - 2.2. [业务线程池](#业务线程池)

💠 2024-03-19 10:33:48
****************************************
# 线程池

> [Java线程池实现原理及其在美团业务中的实践](https://tech.meituan.com/2020/04/02/java-pooling-pratice-in-meituan.html)
> [使用默认的线程池策略](https://github.com/Kuangcp/JavaBase/blob/thread/src/main/java/com/github/kuangcp/UseThreadPool.java)
> [线程池 BlockingQueue synchronized volatile](https://segmentfault.com/a/1190000012916473)
> [参考: Java(Android)线程池](http://www.trinea.cn/android/java-android-thread-pool/)
> [参考: Java ThreadPoolExecutor线程池使用的一个误区](http://codefine.site/2941.html)
> [参考: 聊聊并发（三）Java线程池的分析和使用](http://ifeve.com/java-threadpool/)
> [参考: 线程池](http://ifeve.com/thread-pools/)

> 快速创建命名策略的线程池 `依赖common-lang3`
```java
new ThreadPoolExecutor(5, 5, 0L, TimeUnit.MILLISECONDS,
        new LinkedBlockingQueue<>(), new BasicThreadFactory.Builder().namingPattern("test-%d").build());
```

## 常用API
- `execute`：用于将任务提交给执行器执行
    - (对于会吞异常) 参数为Runable
- `submit`：功能同`execute`，但该方法有返回值 
    - 参数为Callable
- `shutdown()`：用于关闭执行器资源，执行器会拒绝后面的任务提交，并等待线程池中的任务结束后关闭资源
    - 应用关闭前尽量显式调用该方法关闭所有的线程池，避免资源泄漏
- `shutdownNow()`：立即关闭执行器，不再执行线程池中等待执行的任务，正在执行的任务将会继续
- `isShutdown()`：是否调用过`shutdown()`
- `awaitTermination(long timeout, TimeUnit unit)`：该方法会阻塞调用执行器的线程，并等待执行器内任务完成会到达指定的时间
- `invokeAny(Collection<? extends Callable<T>> tasks)`：该方法返回到值为第一个完成的任务返回的值
- `invokeAll(Collection<? extends Callable<T>> tasks)`：该任务的返回值为所有任务完成的结果

## 分支合并框架 Fork/Join
> [Fork Join](/Java/AdvancedLearning/Concurrency/ForkAndJoin.md)

## ScheduledThreadPoolExecutor
简称 STPE 线程池类中很重要的类

- 线程池的大小可以预定义， 也可自适应
- 所安排的任务可以定期执行，也可只运行一次
- STPE扩展了 ThreadPoolExecutor 类，很相似但不具备定期调度能力
    - STPE和并发包里的类结合使用是常见的模式之一

************************

## Executor框架
> 该处讲述的方法都为`java.util.concurrent.Executors`的方法 (静态工厂模式)

- `newFixedThreadPool(int nThreads)`：用于创建固定大小的线程池
    - 传入的参数表示为线程池中最大的线程数
    - 当发送的任务大于该数量时，线程池中只会创建该数量的线程，剩下的任务将会被阻塞，直到有空闲的线程可用
    - 创建方式: `ExecutorService executor = Executors.newFixedThreadPool(3);`

- `newSingleThreadExecutor()`：用于创建单线程化的线程池
    - 在该线程池中只有一个工作的线程
    - 该线程池可保证`任务会按任务的提交顺序进行`
    - 创建方式: `ExecutorService executor = Executors.newSingleThreadExecutor();`

- `newCachedThreadPool()`：用于创建一个可缓存的线程池
    - 该线程池的`工作线程的创建数量几乎没有限制`
    - 当线程池中没有可用的线程时，新添加的任务将会再创建一个线程运行
    - 运行完的任务，在任务运行完的`60s`内不会被回收，当有新任务时将会重用这些没被回收的线程
    - 创建方式: `ExecutorService executor = Executors.newCachedThreadPool();`

- `newScheduledThreadPool(int corePoolSize)`：用于创建一个定长的且支持定时及周期性运行任务的线程池
    - 传入的参数表示为线程池中最大的线程数
    - 创建方法: `ScheduledExecutorService executor = Executors.newScheduledThreadPool(3);`
    - 使用`schedule(Runnable command, long delay, TimeUnit unit)`方法提交任务时，可让任务延迟执行，如下延迟1分钟执行示例: 
        ```java
        // 定义执行器，创建一个缓存线程池
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(3);
        // 提交任务
        executor.schedule(() -> System.out.println("hello: " + new Date()), 1, TimeUnit.SECONDS);
        // 关闭执行器资源
        executor.shutdown();
        ```
    - 使用`scheduleAtFixedRate(Runnable command, long initialDelay, long period, TimeUnit unit)`方法提交任务，可让任务延迟并周期性执行，如下让任务延迟一秒后没3秒执行一次:
        ```java
        // 定义执行器，创建一个缓存线程池
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(3);
        // 提交任务
        executor.scheduleAtFixedRate(() -> System.out.println("hello: " + new Date()), 1, 3, TimeUnit.SECONDS);
        // 周期性执行任务时不要关闭执行器，否则不会周期性执行
        //executor.shutdown();
        ```

- `newSingleThreadScheduledExecutor()`：功能与`newScheduledThreadPool(int corePoolSize)`方法创建的线程池类似，只是该方法创建的是单例化的线程池，即在该线程池中只有一个工作的线程

- `newWorkStealingPool()`：可创建一个拥有多个任务队列的线程池
    - 该方法实在`Java1.8`增加的方法
    - 它是线程池类`ForkJoinPool`的扩展
    - 该线程池能够合理的使用CPU进行对任务操作（并行操作），所以适合使用在很耗时的任务中
    - 创建方式：`ExecutorService executor = Executors.newWorkStealingPool();`

************************
## Spring 
### ThreadPoolTaskExecutor
> Spring的线程池封装实现

- setTaskDecorator: 线程池装饰器，通常用来ThreadLocal值的传递，例如 TraceId，授权对象
- setWaitForTasksToCompleteOnShutdown 等待线程正常执行完才退出全部线程

************************
# 实践
## 线程池 参数优化&监控
> 公式1：Nthreads = Ncpu * Ucpu * W/C

```
    Ncpu = cpu的核心数， 
    Ucpu = cpu的利用率
    W = 线程等待时间
    C = 线程执行计算时间
```

此方案偏理论化，cpu的实际利用率（即分配多少cpu给线程池使用）和线程的计算，等待时间非常难评估，并且最后计算出来的结果也很容易偏离实际应用场景。

> 公式2：coreSize = 2 * Ncpu , maxSize = 25 * Ncpu

实际使用过程中不同的业务对线程池的需求不一样，所以统一采用cpu核心数来配置显然不太合理

> 公式3：coreSize = tps * time , maxSize = tps * time * (1.7~2)

[根据CPU核心数确定线程池并发线程数](https://www.cnblogs.com/dennyzhangdd/p/6909771.html)  
[如何设置线程池参数？](https://www.cnblogs.com/thisiswhy/p/12690630.html)
[线程池实时管理与监控工具的实现与思考](https://www.jianshu.com/p/6f6e2bcb8128)

- [美团 线程池动态监控](https://github.com/dromara/dynamic-tp)  
    - 场景设计具有一定的开拓性，将无法预估的业务负载通过监控和动态伸缩来及时发现异常应对异常。
[线程池如何监控，才能帮助开发者快速定位线上错误？](https://heapdump.cn/article/4012121)`将基准数据采集到数据库表里`  

************************

## 业务线程池
在实际业务系统中，出于不同业务的吞吐量能力，故障影响，保障优先级 等方面的考虑，通常会对不同的业务模块划分不同的线程池，并依据对应的需求设置不同的参数和策略。  
例如： HTTP客户端线程池，WEB服务器NIO线程池，缓存同步线程池，Websocket消息推送线程池 等等。  

基于以上的设计考量，会遇到一些问题
1. 固定的线程参数无法应对动态的业务变化。 
    - 方案： 上文的线程池监控告警以及动态参数调整，需要人为守护调整，或依据实际业务场景实现固定的动态扩缩容策略
1. 不同线程池，上下文传递以及事务问题, 以及异步交错问题。 
    - 异步交错问题： 例如一个业务方法需要做ABC先后完成，但是三件事在不同的线程池中，由于不同线程池的执行效率不同导致未能按期望顺序执行
        - 方案： 1. 通过 CompletableFuture 实现异步之间的依赖和组合
    - 上下文传递问题： 可以使用TTL线程池，或者在线程池使用装饰器，手动复制需要的上下文
    - 事务传递问题： TODO

1. 随着业务需求的变化，线程池边界会模糊，导致吞吐量大的服务被低并发参数的线程池产生短板效应，吞吐量低的服务被高并发参数的线程池任务失败量突增甚至被打垮。 
    - 例如HTTP请求任务被提交到了缓存同步线程池，大量的HTTP请求任务占用了很多资源导致系统缓存的实时性大大降低。
    - 方案： TODO

