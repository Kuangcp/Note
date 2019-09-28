---
title: Executor框架
date: 2019-04-19 12:42:09
tags: 
categories: 
---

**目录 start**
 
1. [Executor框架](#executor框架)
    1. [线程池](#线程池)
        1. [常用方法](#常用方法)
    1. [创建线程池的方法](#创建线程池的方法)

**目录 end**|_2019-09-29 02:24_|
****************************************
# Executor框架
> 为什么要使用线程池? 为什么要使用该框架?

- [ ]  

1. 使用线程池能节省线程创建销毁的开销， 且能通过线程池的参数设置限流

## 线程池
> [使用默认的线程池策略](https://github.com/Kuangcp/JavaBase/blob/thread/src/main/java/com/github/kuangcp/UseThreadPool.java)

> [线程池 BlockingQueue synchronized volatile](https://segmentfault.com/a/1190000012916473)
> [参考博客: Java(Android)线程池](http://www.trinea.cn/android/java-android-thread-pool/)
> [参考博客: Java ThreadPoolExecutor线程池使用的一个误区](http://codefine.site/2941.html)
> [参考博客: 聊聊并发（三）Java线程池的分析和使用](http://ifeve.com/java-threadpool/)
> [参考博客: 线程池](http://ifeve.com/thread-pools/)


### 常用方法

- `execute`：用于将任务提交给执行器执行
    - (会吞异常) 参数为Runable
- `submit`：功能同`execute`，但该方法有返回值 
    - 参数为Callable
- `shutdown()`：用于关闭执行器资源，执行器会拒绝后面的任务提交，并等待线程池中的任务结束后关闭资源
    - 应用关闭前尽量显式调用该方法关闭所有的线程池，避免资源泄漏
- `shutdownNow()`：立即关闭执行器，不再执行线程池中等待执行的任务，正在执行的任务将会继续
- `isShutdown()`：调用了`shutdown()`后该方法将返回`true`
- `awaitTermination(long timeout, TimeUnit unit)`：该方法会阻塞调用执行器的线程，并等待执行器内任务完成会到达指定的时间
- `invokeAny(Collection<? extends Callable<T>> tasks)`：该方法返回到值为第一个完成的任务返回的值
- `invokeAll(Collection<? extends Callable<T>> tasks)`：该任务的返回值为所有任务完成的结果

## 创建线程池的方法
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

