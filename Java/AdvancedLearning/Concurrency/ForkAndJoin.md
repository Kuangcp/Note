---
title: Fork/Join
date: 2023-09-25 13:22:47
tags: 
categories: 
---

💠

- 1. [Fork Join](#fork-join)
    - 1.1. [最佳实践](#最佳实践)
    - 1.2. [设计](#设计)
    - 1.3. [使用](#使用)

💠 2024-03-18 13:54:06
****************************************
# Fork Join
> 自 Java7 引入，业务开发时存在感不怎么高，但实际上很多地方用到的一个库(`Stream`，`VirtualThread`)

> [Guide to the Fork/Join Framework in Java](https://www.baeldung.com/java-fork-join)   

## 最佳实践
- 目的是为了CPU密集型任务的利用CPU全部资源全速执行（核心线程数应越少越好），应避免IO阻塞任务提交执行
- 如无必要，应使用JVM内公共Pool 即 commonPool()
- 任务拆分时需要考虑合理阈值，避免子任务拆分的过大或过小

## 设计

ForkJoinPool 服务处理一种比线程更小的并发单元 ForkJoinTask
- ForkJoinTask 是一种由ForkJoinPool以更轻量的方式所调度的抽象

- 通常使用两种任务
    - 小型 无需处理器耗时太久的任务
    - 大型 需要在直接执行前进行分解（可能多次）的任务
- 提供了支持大型任务分解的基本方法，还有自动调度和重新调度的能力

- 这个框架的关键特性之一就是：这些轻量的任务都能够生成新的ForkJoinTask实例，而这些实例仍然由执行他们父任务的线程池来安排调度，这就是分而治之
- 工作窃取： [简单样例：Groovy 实现](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/main/java/com/github/kuangcp/forkjoin/ForkJoinEasyDemo.groovy)

- 由 RecursiveAction 或者 RecursiveTask 派生出来的才能作为任务单元 这俩也是派生ForkJoinTask而来
    - RecursiveAction 要重写的方法：`protected void compute()`  
    - RecursiveTask 要重写的的方法：`protected Object compute()`
- ForkJoinTask里的 invoke 和 invokeAll 
    - `public final V invoke()`
    - invoke  执行此任务的开始，如果有必要，等待它的完成，并返回其结果，或者在底层计算完成时抛出一个(未检查的)RuntimeException或错误。
    - `public static <T extends ForkJoinTask<?>> Collection<T> invokeAll(Collection<T> tasks)`
    - invokeAll 方法的特点是多个执行，但是只有其中有一个是出现了异常，就会取消所有的task

`ForkJoinTask和工作窃取`
- ForkJoinTask作为RecursiveAction的超类，他是从动作中返回结果的泛型类型，所以这个类扩展了ForkJoinTask<Void> 
    - 这使得ForkJoinTask非常适合用MapReduce方式（Google踢出的软件架构，用于大规模数据集的并行计算）返回数据集中归结出的结果
- ForkJoinTask由ForkJoinPool调度安排，这个池是一个特殊的执行者服务。这个服务维护每个线程的任务列表，并且当某个任务完成的时候，
    - 他能把挂在满负荷线程上的任务重新安排到空闲线程上去 这就是 `工作窃取`

`并行问题`
- 可以使用分支合并方法解决的问题：
    - 模拟大量简单对象的运动，例如粒子效果
    - 日志文件分析
    - 从输入中计数的数据操作，比如mapreduce操作
- 以下的列表检查当前问题及其子任务是一个切实有效的方法，确认是否能用分支合并来解决问题
    - 问题的子任务是否无需与其他子任务有显式的协作或同步也可以工作？
    - 子任务是不是不会对数据进行修改，只是经过计算得出些结果？
    - 对于子任务来说，分而治之是不是很自然的事？子任务是不是会创建更多的子任务，而且他们要比派生出他们的任务粒度更细？
    - 如果思考的结果是肯定的，就可以适用，如果思考结果是不确定的，用其他的同步方式更合适

## 使用

