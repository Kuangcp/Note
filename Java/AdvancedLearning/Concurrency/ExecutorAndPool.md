---
title: 线程池
date: 2019-04-19 12:42:09
tags: 
categories: 
---

💠

- 1. [线程池](#线程池)
    - 1.1. [基础概念](#基础概念)
        - 1.1.1. [Executor 框架层级](#executor-框架层级)
        - 1.1.2. [核心参数](#核心参数)
        - 1.1.3. [队列选型](#队列选型)
        - 1.1.4. [拒绝策略](#拒绝策略)
        - 1.1.5. [线程池状态与 ctl 设计](#线程池状态与-ctl-设计)
    - 1.2. [ThreadPoolExecutor 源码分析](#threadpoolexecutor-源码分析)
        - 1.2.1. [execute() 主流程](#execute-主流程)
        - 1.2.2. [Worker 内部类](#worker-内部类)
        - 1.2.3. [钩子方法](#钩子方法)
        - 1.2.4. [其他方法](#其他方法)
    - 1.3. [ScheduledThreadPoolExecutor](#scheduledthreadpoolexecutor)
        - 1.3.1. [STPE 实现原理](#stpe-实现原理)
    - 1.4. [ForkJoinPool](#forkjoinpool)
    - 1.5. [Executors 工厂方法](#executors-工厂方法)
    - 1.6. [CompletionService](#completionservice)
    - 1.7. [虚拟线程](#虚拟线程)
- 2. [扩展](#扩展)
    - 2.1. [Spring ThreadPoolTaskExecutor](#spring-threadpooltaskexecutor)
    - 2.2. [Alibaba TransmittableThreadLocal](#alibaba-transmittablethreadlocal)
- 3. [实践](#实践)
    - 3.1. [线程池 参数优化 监控](#线程池-参数优化-监控)
    - 3.2. [业务线程池](#业务线程池)
    - 3.3. [停止线程池](#停止线程池)

💠 2026-07-06 19:57:28
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

## 基础概念



### Executor 框架层级

> 是对以上线程池类型的一个基础封装，但是通常不会直接用ExecutorService 仅在单元测试类场景用起来方便，业务上还是用原始的线程池对象，精细的控制线程池的参数，因为业务是复杂多变的。

顶层接口与核心方法：

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

### 核心参数

```java
new ThreadPoolExecutor(
    int corePoolSize,           // 核心线程数，即使空闲也不会回收（allowCoreThreadTimeOut=true 除外）
    int maximumPoolSize,        // 最大线程数，超出 core 的线程在 keepAliveTime 内空闲则回收
    long keepAliveTime,         // 非核心线程的空闲存活时间
    TimeUnit unit,              // 时间单位
    BlockingQueue<Runnable> workQueue,   // 任务队列（核心线程忙时任务先入队）
    ThreadFactory threadFactory,         // 线程工厂，务必自定义命名，方便排查
    RejectedExecutionHandler handler     // 队列满且线程数达 maximumPoolSize 时触发
)
```

- **任务提交流程**：新任务到来 → 线程数 < corePoolSize ? 创建核心线程 : 尝试入队 → 入队成功 ? 等待执行 : 线程数 < maximumPoolSize ? 创建非核心线程 : 执行拒绝策略
- **核心线程 vs 非核心线程**：本质没有区别，只是核心线程在空闲时默认不回收。`prestartAllCoreThreads()` 可提前预热全部核心线程
- **keepAliveTime 作用边界**：只对非核心线程生效；若开启 `allowCoreThreadTimeOut(true)`，核心线程空闲超时后同样回收

### 队列选型

| 队列 | 有界 | 容量行为 | 适用场景 |
|------|------|----------|----------|
| `ArrayBlockingQueue` | 是 | 必须指定 capacity，满后阻塞 | 资源有限、需背压控制的固定负载 |
| `LinkedBlockingQueue` | 可选 | 不指定则为 `Integer.MAX_VALUE`（近似无界） | 量大但能自控速率，JDK Executors 默认选用 |
| `SynchronousQueue` | 是 | 容量为 0，没有缓存，生产必须等待消费 | `newCachedThreadPool` 所用，任务瞬时配对执行 |
| `PriorityBlockingQueue` | 无界 | 按优先级出队（任务需实现 Comparable） | 任务有优先顺序的场景 |
| `DelayedWorkQueue` | 无界 | 二叉堆实现，按延迟时间出队 | `ScheduledThreadPoolExecutor` 专用 |

- **选型核心原则**：队列越有界越安全（快速失败），队列越无界越危险（OOM）
- **搭配规律**：
  - 无界队列 + corePoolSize = maximumPoolSize → 等效固定线程数，队列无限堆积
  - 有界队列 + maximumPoolSize > corePoolSize → 队列满后扩容线程，兼顾吞吐和资源
  - SynchronousQueue + large maximumPoolSize → 来一个任务立刻创建/借用线程，即时响应但消耗大

### 拒绝策略

当 队列满 + 线程数达到 maximumPoolSize 时触发：

| 策略 | 行为 | 适用场景 |
|------|------|----------|
| `AbortPolicy`（默认） | 抛出 `RejectedExecutionException` | 必须感知失败，上游可重试或告警 |
| `CallerRunsPolicy` | 由提交任务的线程（调用方）直接执行 | 自然削峰，降低提交速率（注意调用方线程阻塞风险） |
| `DiscardPolicy` | 静默丢弃新任务，无异常 | 不重要的非关键任务（日志、统计） |
| `DiscardOldestPolicy` | 丢弃队列中最旧的任务，重试提交新任务 | 偏向新任务的场景（如实时数据刷新） |

- **自定义策略**：实现 `RejectedExecutionHandler` 接口，可结合监控打点、告警通知、降级到备用线程池
- **常见思路**：`CallerRunsPolicy` + 有界队列 是实现背压的最轻量方案，配合监控可在系统过载时自然降速

### 线程池状态与 ctl 设计

`ThreadPoolExecutor` 用 `AtomicInteger ctl` 打包两个量——**高 3 位存线程池状态，低 29 位存 worker 数量**，通过 CAS 保证原子性，避免额外锁。

| 状态 | 值(高3位) | 含义 |
|------|-----------|------|
| RUNNING | 111 | 接收新任务 + 处理队列任务 |
| SHUTDOWN | 000 | 不接收新任务，但处理队列中剩余任务 |
| STOP | 001 | 不接收新任务，不处理队列，中断正在执行的任务 |
| TIDYING | 010 | 过渡态，worker 为 0，即将调用 `terminated()` |
| TERMINATED | 011 | `terminated()` 执行完毕，线程池彻底终止 |

- **状态流转**：`RUNNING → SHUTDOWN (shutdown())` / `RUNNING → STOP (shutdownNow())` → `TIDYING → TERMINATED`
- **设计意图**：将状态和计数压缩到一个 int，用 CAS 一次操作即可同时判断状态和增减线程数，避免多变量竞争

## ThreadPoolExecutor 源码分析
> 最常用的线程池对象

### execute() 主流程

三步判断，源码精简如下：

```java
int c = ctl.get();
// 1. 工作线程 < corePoolSize → 创建核心线程
if (workerCountOf(c) < corePoolSize) {
    if (addWorker(command, true)) return;
    c = ctl.get();
}
// 2. 线程池 RUNNING 且入队成功
if (isRunning(c) && workQueue.offer(command)) {
    int recheck = ctl.get();
    // 二次检查：防止入队期间线程池被 shutdown，此时拒绝任务
    if (!isRunning(recheck) && remove(command))
        reject(command);
    // 线程池可能刚好线程数为 0，需要兜底补一个线程
    else if (workerCountOf(recheck) == 0)
        addWorker(null, false);
}
// 3. 入队失败（队列满）→ 尝试创建非核心线程，失败则拒绝
else if (!addWorker(command, false))
    reject(command);
```

关键 ctl 位运算常量：`CAPACITY = (1<<29)-1`, `COUNT_BITS=29`, `workerCountOf(c) = c & CAPACITY`, `runStateOf(c) = c & ~CAPACITY`。

### Worker 内部类

```java
private final class Worker extends AbstractQueuedSynchronizer implements Runnable {
    final Thread thread;       // Worker 绑定的线程
    Runnable firstTask;        // 初始任务，可 null（从队列取）
    volatile long completedTasks; // 已完成任务计数
}
```

- **AQS 的作用**：不是控制任务互斥，而是标记 Worker 线程自身的运行状态（`lock()` = 正在执行任务，`unlock()` = 空闲）。`interruptIdleWorkers()` 只中断未持有锁的空闲线程。
- **生命周期**：
  1. `addWorker()` 创建 Worker 并 `thread.start()`
  2. 线程调用 `runWorker(this)`：先执行 `firstTask`，再循环 `getTask()` 从队列取任务
  3. `getTask()` 返回 null 或任务执行异常 → `processWorkerExit()` 退出，后续根据条件决定是否补新线程
- `getTask()` 的核心逻辑：根据 `allowCoreThreadTimeOut` 和当前 worker 数量，决定用 `poll(keepAliveTime)` 还是 `take()` 取任务，返回 null 则触发线程回收

### 钩子方法

`ThreadPoolExecutor` 提供了三个 protected 钩子，继承后覆盖即可无侵入注入逻辑：

```java
beforeExecute(Thread t, Runnable r)  // 任务执行前，可注入 TraceId、记录开始时间
afterExecute(Runnable r, Throwable t) // 任务执行后（即使任务抛异常也会调用，t 可能为 null）
terminated()                          // 线程池完全终止后回调，适合资源清理、告警通知
```

- `afterExecute` 的 `Throwable t` 参数在任务正常返回时为 null，任务被中断时也可能为 null，要获取原始异常需从 `submit` 返回的 Future 中手动捕获
- 典型用法：`beforeExecute` 设上下文 + 开始计时；`afterExecute` 算耗时、清上下文、记录慢任务或异常

### 其他方法

- allowCoreThreadTimeOut() 允许idle的核心线程回收（依赖 keepAliveTime 值 ），默认false
- prestartAllCoreThreads 和 prestartAllCoreThreads 创建线程池对象时预热创建出所有core线程，默认是收到任务才逐步创建

****************************************

## ScheduledThreadPoolExecutor
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

**注意**: 
- 定时的这些API上有注释说明：当某次任务抛出异常时，后续的调度会取消，所以异步任务需要完全 try catch，自行处理单次任务的异常
- 如果想在某次任务时取消后续所有调度，可以通过直接抛出异常，或者通过 ScheduledFuture 来更优雅控制，例如
```java
    AtomicInteger cnt = new AtomicInteger();
    // 需要在声明完之前就引用，所以需要借助AtomicReference来 逆时序传递 对象
    AtomicReference<ScheduledFuture<?>> monitorFutureRef = new AtomicReference<>();
    ScheduledFuture<?> monitorFuture = sche.scheduleAtFixedRate(() -> {
        int i = cnt.incrementAndGet();
        if (i > 5) {
            // 取消定时任务
            ScheduledFuture<?> future = monitorFutureRef.get();
            if (future != null) {
                future.cancel(false);
            }
            // 关闭线程池
            sche.shutdown();
        }
        System.out.println("run " + i);
    }, 2, 1, TimeUnit.SECONDS);
    monitorFutureRef.set(monitorFuture);
```

### STPE 实现原理
> 如何实现调度: [ScheduledThreadPoolExecutor实现原理](https://juejin.cn/post/7035415187783942152) | [验证单元测试](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/test/java/thread/schdule/SchedulerPoolTest.java)
- 核心依赖 DelayedWorkQueue （二叉堆（优先级队列）+ Leader-Follower 模式）实现延迟调度，默认容量的最大值为Integer.MAX_VALUE
- JDK 没有用时间轮（如 Netty 的 HashedWheelTimer），因为时间轮适合海量细粒度定时任务（几十万级别），而二叉堆对于一般场景的插入/删除 O(log n)已经足够。

```java
    // 简化逻辑，实际在 java.util.concurrent.ScheduledThreadPoolExecutor 内部
    public RunnableScheduledFuture<?> take() throws InterruptedException {
        for (;;) {
            RunnableScheduledFuture<?> first = queue[0]; // 二叉堆堆顶，最近要执行的任
            if (first == null)
                available.await();      // 队列空，所有线程都
            else {
                long delay = first.getDelay(NANOSECONDS)
                if (delay <= 0)
                    return finishPoll(first);  // 到期了，出队执
                if (leader != null)
                    available.await();  // 已经有个 leader 在等，我是 follower，无限
                else {
                    thisThread = Thread.currentThread()
                    leader = thisThread;
                    available.awaitNanos(delay);  // 我是 leader，精确等 delay 纳
                    leader = null;
                }
            }
        }
    }
```

- 当全部线程都繁忙时，计划的周期任务会*依次延迟执行*，也就是说如果有一个期望1S后执行的任务，由于前序任务的阻塞和耗时会导致后续任务不可控的延迟执行
- 所以这个线程池适合 调度周期间隔远大于 任务执行时间，相较于直接开线程池进行sleep做任务的周期执行可以节省大量的线程资源
- 但是 如果有场景是高频又高IO耗时的任务执行，为了任务的调度执行不出现明显的延迟：
    - 如果任务的特点是IO型的话可以调大核心线程数解决或者上虚拟线程
    - 但是如果是CPU型就只能水平扩展节点了做分布式任务消费

****************************************

## ForkJoinPool
> 分支合并框架
> [详情: Fork Join](/Java/AdvancedLearning/Concurrency/ForkAndJoin.md)

****************************************

## Executors 工厂方法
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

- `unconfigurableExecutorService()` 将线程池包装为不可修改参数，只能提交和停止的线程池对象

> ⚠️ 安全陷阱：`newFixedThreadPool` / `newSingleThreadExecutor` 内部使用无界 `LinkedBlockingQueue`，任务堆积可能导致 OOM；`newCachedThreadPool` 线程数无上限，高并发下可能创建大量线程导致 OOM。**生产环境建议直接使用 `ThreadPoolExecutor` 构造器显式指定有界队列和拒绝策略。**

****************************************

## CompletionService
> 实现类 ExecutorCompletionService JavaDoc上有使用示例

- submit：提交任务
- take：阻塞获取下一个完成的任务结果
- poll：非阻塞获取下一个完成的任务结果

> [TimeoutExecPoolTest](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/test/java/situation/timoutpool/TimeoutExecPoolTest.java)`限时并行消费任务获取结果，时间到期则丢弃所有未完成的任务`

****************************************

## 虚拟线程
> JDK21 `Executors.newVirtualThreadPerTaskExecutor()`

- 每个任务创建一个轻量级虚拟线程，适合 IO 密集型高并发场景
- 与平台线程池的本质差异：虚拟线程由 JVM 调度而非 OS，阻塞不占据平台线程
- TODO 展开：适用场景对比、与 ThreadPoolExecutor 的选型决策

****************************************

# 扩展

## Spring ThreadPoolTaskExecutor
> Spring的线程池封装实现

- setTaskDecorator: 线程池装饰器，通常用来ThreadLocal值的传递，例如 TraceId，授权对象
- setWaitForTasksToCompleteOnShutdown 等待线程正常执行完才退出全部线程

## Alibaba TransmittableThreadLocal
> [alibaba/transmittable-thread-local](https://github.com/alibaba/transmittable-thread-local)

> Tips
- TTL 2.12.x 池内线程抛出 NoSuchMethodError时， log.error 看不到异常栈，只有message ，debug断点住 在IDE才看到栈

****************************************

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

****************************************

- [Java线程池实现原理及其在美团业务中的实践](https://tech.meituan.com/2020/04/02/java-pooling-pratice-in-meituan.html)
    - 场景设计具有一定的开拓性，将无法预估的业务负载通过监控和动态伸缩来及时发现和应对异常。
    - [线程池动态监控](https://github.com/dromara/dynamic-tp)`支持动态修改和监控告警`

[根据CPU核心数确定线程池并发线程数](https://www.cnblogs.com/dennyzhangdd/p/6909771.html)
[如何设置线程池参数？](https://www.cnblogs.com/thisiswhy/p/12690630.html)
[线程池实时管理与监控工具的实现与思考](https://www.jianshu.com/p/6f6e2bcb8128)

[线程池如何监控，才能帮助开发者快速定位线上错误？](https://heapdump.cn/article/4012121)`将基准数据采集到数据库表里`

****************************************

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
    - 事务传递问题： 线程池跨线程时，Spring 的 `TransactionSynchronizationManager` 默认以 ThreadLocal 存储事务上下文，切换线程后事务状态丢失。
        - 方案： 
            1. 通过 `TransactionTemplate` 在提交任务前解绑事务上下文，进入线程后重新绑定；或将事务边界收缩到单线程内，跨线程部分采用最终一致性方案（本地消息表、事务消息、Saga 等）。
            2. Spring 的 `DelegatingTransactionRunnable` 模式：自定义 Runnable 在构造时捕获当前事务的 `TransactionSynchronization` 并在 `run()` 中恢复回调。
            3. 结合 TTL 包装 `TransactionSynchronizationManager` 的资源对象，在跨线程时自动复制，但需注意隔离级别和回滚行为的语义差异。

1. 随着业务需求的变化，线程池边界会模糊，导致吞吐量大的服务被低并发参数的线程池产生短板效应，吞吐量低的服务被高并发参数的线程池任务失败量突增甚至被打垮。 
    - 例如HTTP请求任务被提交到了缓存同步线程池，大量的HTTP请求任务占用了很多资源导致系统缓存的实时性大大降低。
    - 方案：
        1. **编码规范约束**：在线程池 Bean 上标注 `@Qualifier`（如 `@Qualifier("httpPool")`、`@Qualifier("cachePool")`），注入时强制按业务名选择，禁止用 `@Autowired` + 类型匹配注入；通过 ArchUnit 单元测试在 CI 阶段校验依赖规则。
        2. **运行时熔断隔离**：结合 Sentinel / Resilience4j 对每个线程池设置信号量熔断，当某业务大量超出线程池容量时快速失败，避免饥饿扩散。
        3. **定期 review 线程池职责矩阵**：建立一张「线程池 → 业务模块 → 核心参数 → 所属服务」的映射表，在需求变更时同步审视是否有跨池混用的风险。

****************************************

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
