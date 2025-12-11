---
title: 线程池
date: 2019-04-19 12:42:09
tags: 
categories: 
---

💠

- 1. [线程池](#线程池)
    - 1.1. [ThreadPoolExecutor](#threadpoolexecutor)
    - 1.2. [ScheduledThreadPoolExecutor STPE](#scheduledthreadpoolexecutor-stpe)
    - 1.3. [分支合并框架 Fork/Join](#分支合并框架-forkjoin)
    - 1.4. [ExecutorService 接口](#executorservice-接口)
    - 1.5. [Executors](#executors)
    - 1.6. [CompletionService 接口](#completionservice-接口)
- 2. [Spring](#spring)
    - 2.1. [ThreadPoolTaskExecutor](#threadpooltaskexecutor)
- 3. [实践](#实践)
    - 3.1. [线程池 参数优化 监控](#线程池-参数优化-监控)
    - 3.2. [业务线程池](#业务线程池)
    - 3.3. [停止线程池](#停止线程池)

💠 2025-12-11 15:32:16
****************************************
# 线程池

> [Java线程池实现原理及其在美团业务中的实践](https://tech.meituan.com/2020/04/02/java-pooling-pratice-in-meituan.html)
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

## ThreadPoolExecutor
> 最常用的线程池对象

- allowCoreThreadTimeOut() 允许idle的核心线程回收（依赖 keepAliveTime 值 ），默认false
- prestartAllCoreThreads 和 prestartAllCoreThreads 创建线程池对象时预热创建出所有core线程，默认是收到任务才逐步创建

## ScheduledThreadPoolExecutor STPE
- 线程池的大小可以预定义， 也可自适应
- 所安排的任务可以定期执行，也可只运行一次
- STPE 扩展了 ThreadPoolExecutor 类，很相似但不具备定期调度能力
    - STPE 和并发包里的类结合使用是常见的模式之一

> 核心API： 提交任务
- 单次 `schedule(Runnable command, long delay, TimeUnit unit)`
- 单次 `schedule(Callable<V> callable, long delay, TimeUnit unit)`

- 定时 `scheduleAtFixedRate(Runnable command, long initialDelay, long period, TimeUnit unit)`
    - 不管上一次Runnable执行结束的时间，总是以固定延迟时间执行 即 上一个Runnable执行开始时候 + 延时时间 = 下一个Runnable执行的时间点
- 定时 `scheduleWithFixedDelay(Runnable command, long initialDelay, long delay, TimeUnit unit)`
    - 当上一个Runnable执行结束后+固定延迟 = 下一个Runnable执行的时间点

**注意**: 定时的这些API上有注释说明：当某次任务抛出异常时，后续的调度会挂起，所以异步任务需要大范围的 try catch，业务自己处理异常

> 如何实现调度: [ScheduledThreadPoolExecutor实现原理](https://juejin.cn/post/7035415187783942152) | [验证单元测试](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/test/java/thread/schdule/SchedulerPoolTest.java)
- 核心依赖 DelayedWorkQueue 实现延迟调度
    - 全部线程繁忙时，调度会发生什么问题？ 

************************
## 分支合并框架 Fork/Join
> [Note： Fork Join](/Java/AdvancedLearning/Concurrency/ForkAndJoin.md)

## ExecutorService 接口
> [Github Demo](https://github.com/Kuangcp/JavaBase/tree/master/concurrency/src/main/java/thread/pool)

> 是对以上线程池类型的一个基础封装，但是通常不会直接用ExecutorService 仅在单元测试类场景用起来方便，业务上还是用原始的线程池对象，精细的控制线程池的参数，因为业务是复杂多变的。

- `execute`：用于将任务提交给执行器执行
    - 参数为Runable
    - 无返回，对于调用方来说无法感知异常，但是异常栈会被输出到 System.err ，依然有迹可查
- `submit`：功能同`execute`，但该方法可以返回值或抛出异常 Future 对象
    - 参数为Callable
    - 返回的Future对象如果不调用get方法，任务的异常栈在系统中**没有任何痕迹**

- `shutdown()`：用于关闭执行器资源，执行器会拒绝后面的任务提交，并等待线程池中的任务结束后关闭资源
    - 应用关闭前尽量显式调用该方法关闭所有的线程池，避免资源泄漏
- `shutdownNow()`：立即关闭执行器，返回等待队列的任务，正在执行的线程将收到interupt但是不一定会停止
- `isShutdown()`：是否调用过`shutdown()`
- `awaitTermination(long timeout, TimeUnit unit)`：该方法会阻塞调用线程，等待执行器内任务完成直到超时

- `invokeAny(Collection<? extends Callable<T>> tasks)`：返回 任意的第一个完成任务的返回值
- `invokeAll(Collection<? extends Callable<T>> tasks)`：返回所有任务对应的Future对象

> 注意

上述的 execute 和 submit 行为只针对 `ThreadPoolExecutor`. 对于 ScheduledThreadPoolExecutor 来说，execute行为不一样， execute提交的任务 抛出异常时也是**没有任何痕迹**  

## Executors
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
    - 该线程池的`工作线程的创建数量没有限制`
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
- `unconfigurableExecutorService` 将线程池包装为不可修改参数，只能提交和停止的线程池对象

## CompletionService 接口
> 实现类 ExecutorCompletionService JavaDoc上有使用示例

- submit
- take
- poll

> [TimeoutExecPoolTest](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/test/java/situation/timoutpool/TimeoutExecPoolTest.java)`限时并行消费任务获取结果，时间到期则丢弃所有未完成的任务`  

************************

# Spring 
## ThreadPoolTaskExecutor
> Spring的线程池封装实现

- setTaskDecorator: 线程池装饰器，通常用来ThreadLocal值的传递，例如 TraceId，授权对象
- setWaitForTasksToCompleteOnShutdown 等待线程正常执行完才退出全部线程

************************
# 实践
目标： 合理利用资源，让线程池安全可控的消费任务

> [About Pool Sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) | [About Pool Sizing in distributed environments / microservices](https://github.com/brettwooldridge/HikariCP/issues/1023)`如何设置数据库连接池线程数`  

> [ 合理使用线程池以及线程变量 ](https://mp.weixin.qq.com/s/BdVqvm2wLNv05vMTieevMg)  
> [ExecutorService - 10 tips and tricks](https://nurkiewicz.com/2014/11/executorservice-10-tips-and-tricks.html)  

[Tomcat 线程池](/Java/Ecosystem/Servlet/TomcatDesign.md#线程池)  

- 增加全局异常处理 `Thread.setUncaughtExceptionHandler()`, 或手动catch任务块全部代码 避免异常被吞 [测试代码](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/test/java/thread/pool/PoolExceptionTest.java)
- 避免局部线程池，容易遗忘线程资源回收，注意线程是GCRoot对象
- 依据业务和监控合理设置参数，动态调整
    - 监控指标核心诉求是 忙不忙，在忙什么，还有多少要忙。
    - 设置参数值（核心，最大，队列大小等等），活跃线程数，任务执行量，等待队列大小，执行拒绝策略次数。
- 管理好上下文参数

## 线程池 参数优化 监控
目的：观测线程池运行情况，优化吞吐量和延迟，规避资源分配不合理导致瓶颈甚至宕机

```
    Ncpu = cpu的核心数
    Ucpu = cpu的利用率
    W = 线程等待时间
    C = 线程执行计算时间
```

> 公式1：Nthreads = Ncpu * Ucpu * W/C
- 此方案偏理论化，cpu的实际利用率（即分配多少cpu给线程池使用）和线程的计算，等待时间非常难评估，并且最后计算出来的结果也很容易偏离实际应用场景。

> 公式2：coreSize = 2 * Ncpu , maxSize = 25 * Ncpu
- 实际使用过程中不同的业务对线程池的需求不一样，所以统一采用cpu核心数来配置显然不太合理

> 公式3：coreSize = tps * C , maxSize = tps * C * (1.7~2)
- 依据tps和耗时来计算时刻内需要占用多少线程，这种适合资源充足时为了尽量降低等待时间

************************

- [Java线程池实现原理及其在美团业务中的实践](https://tech.meituan.com/2020/04/02/java-pooling-pratice-in-meituan.html)
    - 场景设计具有一定的开拓性，将无法预估的业务负载通过监控和动态伸缩来及时发现和应对异常。
    - [线程池动态监控](https://github.com/dromara/dynamic-tp)`支持动态修改和监控告警`

[根据CPU核心数确定线程池并发线程数](https://www.cnblogs.com/dennyzhangdd/p/6909771.html)  
[如何设置线程池参数？](https://www.cnblogs.com/thisiswhy/p/12690630.html)
[线程池实时管理与监控工具的实现与思考](https://www.jianshu.com/p/6f6e2bcb8128)

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

************************

## 停止线程池
> 如何实现JVM停止时等待线程池中任务执行完成 即 优雅停机

为了实现优雅停机的目标，应当先调用shutdown方法，调用这个方法也就意味着，这个线程池不会再接收任何新的任务，但是已经提交的任务还会继续执行。
之后还应当调用awaitTermination方法，这个方法可以设定线程池在关闭之前的最大超时时间，如果在超时时间结束之前线程池能够正常关闭则会返回true，否则，超时会返回false。
通常需要根据业务场景预估一个合理的超时时间。

如果awaitTermination方法返回false，但又希望尽可能在线程池关闭之后再做其他资源回收工作，可以考虑再调用一次shutdownNow方法，此时队列中所有尚未被处理的任务都会被丢弃，同时会设置线程池中每个线程的中断标志位。
shutdownNow **并不保证**一定会让正在运行的线程停止工作，除非提交给线程的任务能够正确响应中断。

> 线程池停止时，如何感知到 被中断的 运行中和等待中的任务
- 默认的shutdown接口返回的是Runnable匿名实例，无法明确获取业务特征
    - 可以自己实现 Runnable 附带业务信息进去
    ```java
        public class Task implements Runnable {
            private String id;
            private Runnable task;
            public Task(String id, Runnable task) {
                this.id = id;
                this.task = task;
            }
            @Override
            public void run() {
                this.task.run();
            }
        }
    ```
