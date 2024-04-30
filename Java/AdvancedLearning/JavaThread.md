---
title: Java线程
date: 2018-11-21 10:56:52
tags: 
    - Thread
categories: 
    - Java
---

💠

- 1. [Java线程](#java线程)
- 2. [生命周期](#生命周期)
    - 2.1. [创建](#创建)
    - 2.2. [控制](#控制)
        - 2.2.1. [yield](#yield)
        - 2.2.2. [join](#join)
        - 2.2.3. [interrupt](#interrupt)
        - 2.2.4. [Signal](#signal)
    - 2.3. [销毁](#销毁)
        - 2.3.1. [观测异常](#观测异常)
- 3. [ThreadLocal](#threadlocal)
    - 3.1. [Hook](#hook)
    - 3.2. [优雅关机](#优雅关机)
- 4. [线程池](#线程池)
- 5. [协程](#协程)
    - 5.1. [Loom](#loom)
    - 5.2. [Quasar](#quasar)

💠 2024-04-30 14:07:24
****************************************
# Java线程
> [个人相关代码](https://github.com/Kuangcp/JavaBase/tree/thread/src/main/java/com/github/kuangcp)

- [码农翻身:我是一个线程](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=416915373&idx=1&sn=f80a13b099237534a3ef777d511d831a&scene=21#wechat_redirect) | [码农翻身:编程世界的那把锁](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513653&idx=1&sn=e30c18c0c1780fb3ef0cdb858ee5201e&chksm=80d67af6b7a1f3e059466302c2c04c14d097c1a5de01cf986df84d4677299542f12b974dfde3&scene=21#wechat_redirect) | [码农翻身:加锁还是不加锁，这是一个问题 ](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513692&idx=1&sn=ef2416a4bb96d64db77e32d5b4c7967e&chksm=80d67a9fb7a1f3898e513cc1d9e96841610bb84aed2dc24cab2d403e74e317e3c447e45e7611&scene=21#wechat_redirect)

> 线程优先级： 多个线程同时运行时,由线程调度器来决定哪些线程运行,哪些等待以及线程切换的时间点. 由于各个操作系统的线程调度器的实现各不相同, 所以依赖JDK来设置线程优先级策略是错误和平台不可移植性的.

# 生命周期
> [参考博客](https://segmentfault.com/a/1190000005006079) | [Blog: 线程详解](http://www.cnblogs.com/riskyer/p/3263032.html) | [参考Java-learning仓库](https://github.com/brianway/java-learning)

> java.lang.Thread.State
- NEW
- RUNNABLE
- BLOCKED
- WAITING
    - Object.wait()
    - Thread.join()
    - LockSupport.park()
- TIMED_WAITING
    - Thread.sleep()
    - Object.wait(timeout)
    - Thread.join(timeout)
    - LockSupport.parkNanos()
    - LockSupport.parkUntil()
- TERMINATED
    - 终止态，不管是正常执行结束还是异常中断。

## 创建
- 创建线程有三种创建方式： 继承，实现接口，实例化匿名方法。[示例代码](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/main/java/thread/HowToCreateThread.java)

> Thread类源码 Runnable，target，run，start 关系
- Runnable是一个接口
- target是Thread类中类型为Runnable，名为target的属性
- run是Thread类实现了Runnable的接口，重写的方法。
- start是启动线程的方法 `native`
- 在Thread类中，调用关系为：_start->start0->run->target.run_

_Thread类的run方法源码_
```java
    public void run() {
        if (target != null) {
            target.run();
        }
    }
```
_Thread类的target属性_
```java
    /* What will be run. */
    private Runnable target;
```
- target属性由 `private void init(ThreadGroup g, Runnable target, String name,long stackSize, AccessControlContext acc)`方法初始化。
    - init方法在Thread类的构造方法里被调用

## 控制
- 当调用 `join()` 时，`当前调用线程`将会阻塞，直到`目标线程`完成为止。 

Object.wait 转为两种Waiting状态

LockSupport.park

[Can LockSupport.park() replace Object.wait()?](https://stackoverflow.com/questions/39415636/can-locksupport-park-replace-object-wait)

[thread states](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/tooldescr034.html)

### yield

### join

### interrupt
> [Oracle interrupt](https://docs.oracle.com/javase/tutorial/essential/concurrency/interrupt.html)

- java.lang.Thread#interrupt
    - 这个方法仅仅是标记下状态，在一些阻塞类方法调用时会检查该状态值（sleep wait join yield 等等）， 如果线程一直在循环跑CPU计算，那这个线程不会停止
- java.lang.InterruptedException
    ```java
        // 判断当前线程是否已发生中断
       if (Thread. interrupted())  // Clears interrupted status!
       throw new InterruptedException();
    ```

中断机制是通过一个称为中断状态的内部标志来实现的。调用 Thread.interrupt 会设置该标志。当线程通过调用静态方法 Thread.interrupted 检查中断时，中断状态会被清除。一个线程用来查询另一个线程中断状态的非静态 isInterrupted 方法不会改变中断状态标志。  
按照惯例，任何通过抛出 InterruptedException 而退出的方法在退出时都会清除中断状态。不过，中断状态总是有可能被另一个调用中断的线程立即再次设置。

************************

### Signal
> 由于Java是跨平台语言，主要考虑Window和unix系平台，后者在生产中使用居多，因此重点关注

[Linux的Signal](/Linux/Base/LinuxPerformance.md#kill)   
快速理解：
- Kill 9信号： 无法监听和屏蔽 
- TERM 15信号：默认退出进程信号
- INT 2信号：  IDEA中停止JVM时发出的就是该信号

相关JVM参数 -Xrs 忽略（1,2,3,4,5,6,7,8,11,15） [oracle java command](https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html)`注意Linux和Windows实现及信号量不一样`
- 忽略的逻辑实现为：JVM接收信号量然后什么都不做。
- 注意此时Java应用代码无法手动监听对应的信号量，注册监听时会报错

************************

## 销毁

### 观测异常
> java.lang.Thread.UncaughtExceptionHandler `Interface for handlers invoked when a Thread abruptly terminates due to an uncaught exception.`

通过设置静态属性 `Thread.setDefaultUncaughtExceptionHandler()`，可以观测由于未捕获的异常导致Thread被销毁的情况，可加入监控和告警的逻辑

************************

# ThreadLocal
> [Oracle: ThreadLocal](https://docs.oracle.com/javase/8/docs/api/java/lang/ThreadLocal.html)  

设计： ThreadLocalMap 线程对象做key的一个封装Map(但是未实现Map接口)，一个线程可以有多个ThreadLocal

> [Alibaba TTL 使用场景](https://github.com/alibaba/transmittable-threalocal/issues/123)`可看作ThreadLocal的一种特殊实现`
- 主要流程： com.alibaba.ttl.TtlRunnable#run
    - 提交任务时对run方法封装，先复制当前 TransmittableThreadLocal
    - 等待要调度执行时，重放复制的TransmittableThreadLocal值，从而实现父子线程间上下文的传递
    - **注意**：因为只是处理了TransmittableThreadLocal，所以其他ThreadLocal值需要做传递时，需要通过装饰器去手动复制，例如SpringSecurity的SecurityContextHolder， slf4j的MDC

> [一次「找回」TraceId的问题分析与过程思考](https://tech.meituan.com/2023/04/20/traceid-google-dapper-mtrace.html)

************************
## Hook  
- 注册Hook：`Runtime.getRuntime().addShutdownHook(Thread thread)`
- 在JVM正常退出时会调用已注册的Hook逻辑
    1. 例如 System.exit(), 或者 Java 进程收到退出的信号 SIGTERM SIGINT SIGQUIT 等等
    1. 但是 SIGKILL、 Runtime.halt()、断电、系统Crash 等情况下， `没有时机执行Hook`。
    1. 不能在Hook逻辑中调用`System.exit()`, 否则会阻塞JVM退出，但是可以调用`Runtime.halt()`
    1. 不能在Hook逻辑中增删Hook
    1. 在`System.exit()`执行后才注册的Hook逻辑不会被执行
    1. `Hook逻辑执行时完整性不可控` 操作系统可控制当对JVM发出`TERM(15)`信号后一段时间未结束时可强制结束`KILL（9）`，此时Hook逻辑可能才执行了一半
    1. 注册的Hook是按先后执行的，但是其中任意一个Hook抛出未处理的异常时会中断自身及后续Hook逻辑

## 优雅关机
> Java层面
1. 线程池设置关闭时等待已有任务线程执行完成
    - 但是通常等待是会有限制（容器的健康检查等）的，所以还是会造成任务的中断，队列中任务的丢失
1. 手动接收信号量 追加资源关闭逻辑：MQ，缓存，数据库

> 环境层面  

当关闭服务器A时，先将该服务器的入口流量屏蔽，防止新的请求进入，然后等服务器完成原有请求的响应，以及一些资源清理行为后，完全关闭。

[参考: Kubernetes 中如何保证优雅地停止 Pod](https://cloud.tencent.com/developer/article/1409225)  
[参考: JVM安全退出（如何优雅的关闭java服务）](https://www.cnblogs.com/yuandluck/p/9517700.html)  

************************

# 线程池
> [Note: 线程池](/Java/AdvancedLearning/Concurrency/ExecutorAndPool.md)  

************************

# 协程
## Loom
> [OpenJDK: Loom](https://openjdk.java.net/projects/loom/)

> [OpenJDK Project Loom](https://www.baeldung.com/openjdk-project-loom)

## Quasar
> [Github: Quasar](https://github.com/puniverse/quasar)

