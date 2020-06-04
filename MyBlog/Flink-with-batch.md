---
title: Flink-with-batch
date: 2019-06-17 17:00:27
tags: 
categories: 
    - Blog
---

**目录 start**

1. [Flink 中的批处理](#flink-中的批处理)
    1. [为何有这次分享](#为何有这次分享)
    1. [Flink 是什么](#flink-是什么)
    1. [为何选用Flink](#为何选用flink)
    1. [基础概念和原理](#基础概念和原理)
        1. [流处理和批处理](#流处理和批处理)
        1. [部署](#部署)
    1. [批处理](#批处理)
        1. [Rest API](#rest-api)

**目录 end**|_2020-06-04 19:41_|
****************************************
# Flink 中的批处理

## 为何有这次分享
最近实现的需求是采用的该架构设计实现, 也是一边学习一边思考整理

https://www.cnblogs.com/ken-io/p/knowledge-or-technology-share-guide.html

https://blog.csdn.net/wenxueliu/article/details/89484375

************************

## Flink 是什么
> [官网](https://flink.apache.org/)

Flink 是一个批处理和流处理结合的统一计算框架，其核心是一个提供了数据分发以及并行化计算的流数据处理引擎。

最开始08年是柏林理工大学的一个研究项目，14年成为Apache孵化项目, 15年阿里fork并开发了Blink分支, 之后又并入社区  
在实践中做了诸多优化 例如 增量 checkpoint, 重构调度和资源管理, 以支持 Yarn K8s

## 为何选用Flink
> 阿里, 滴滴,美团,字节跳动 等公司使用和开发, 其中在阿里双十一大屏的应用场景上达到了 4.72亿次/秒.

`State`

Flink的优势是支持有状态的计算, 如果一个事件或一条数据处理结果只与本身内容有关, 那么就是无状态的, 反之则是与之前处理过的事件有关, 称为有状态, 最常用的应用场景就是有状态的处理 比如 聚合,关联 等操作

`Checkpoint`

利用了经典的 Chandy-Lamport 算法, 核心思想是 把这个流计算看成一个流式的拓扑, 定期从这个拓扑的头部 source 节点, 开始插入特殊的屏障, 从上游开始不断往下游广播这个屏障, 每一个节点收到屏障后, 会将State做一次快照, 当每个节点都做完了快照, 整个拓扑就算是完成了一次 CheckPoint

Flink的容错机制的核心部分是生成分布式数据流和算子状态的一致快照。从而提供了 exactly-once 的语义(输入的数据作用在最终结果上有且仅有一次), 能更容易的管理状态, 就像操作普通集合

![](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/stream_barriers.svg)

`Windows`

因为不可能计算流中的所有元素，因为流通常是无限的（无界）。所以流计算一般都会基于窗口来计算 
Flink提供了一套开箱即用的窗口操作, 例如翻滚窗口（没有重叠），滑动窗口（具有重叠）和会话窗口（由不活动间隙打断）, 还支持自定义窗口。


************************

>> 同类框架还有 经典的 Hadoop Map-Reduce, 架构简单, 不能支持复杂的应用逻辑, 需要应用逻辑 适配到 map-reduce算法, 仅支持批处理, 

Spark批处理, 流处理的实现是将批处理的批次分割成若干小

Flink基于每个事件一行一行地流式处理，真正的流式计算，流式计算跟Storm性能差不多，支持毫秒级计算，而Spark则只能支持秒级计算。

> [美团: 流计算框架 Flink 与 Storm 的性能对比](https://tech.meituan.com/2017/11/17/flink-benchmark.html)

## 基础概念和原理

### 流处理和批处理

![](https://ci.apache.org/projects/flink/flink-docs-release-1.8/fig/levels_of_abstraction.svg)

批处理主要操作大容量静态数据集，并在计算过程完成后返回结果。

- 批处理模式中使用的数据集通常符合下列特征：
    1. 有界：批处理数据集代表数据的有限集合
    1. 持久：数据通常始终存储在某种类型的持久存储位置中
    1. 大量：批处理操作通常是处理极为海量数据集的唯一方法

批处理非常适合需要访问全套记录才能完成的计算工作。例如在计算总数和平均数时

- 流处理中的数据集是“无边界”的：
    1. 完整数据集只能代表截至目前已经进入到系统中的数据总量。
    1. 工作数据集也许更相关，在特定时间只能代表某个单一数据项。
    1. 处理工作是基于事件的，除非明确停止否则没有“尽头”。处理结果立刻可用，并会随着新数据的抵达继续更新。

流处理系统可以处理几乎无限量的数据，但同一时间只能处理一条（真正的流处理）或很少量（微批处理，Micro-batch Processing）数据，不同记录间只维持最少量的状态。虽然大部分系统提供了用于维持某些状态的方法，但流处理主要针对副作用更少，更加功能性的处理（Functional processing）进行优化。

************************

### 部署
> Local, Standalone Cluster, YARN Cluster

- Local 模式的 JobManager 和 TaskManager 只使用一个 JVM 来完成整个计算, 常用于小数据量的开发测试
- Standalone Cluster 模式的 JobManager 和 TaskManager 都是单点且各自独立的, 例如以下通过 docker-compose 部署的案例
- Yarn Cluster 也就是完全没有单点问题

```yml
    version: "2.1"
    services:
    jobmanager:
        image: ${FLINK_DOCKER_IMAGE_NAME:-flink}
        expose:
        - "6123"
        ports:
        - "8081:8081"
        command: jobmanager
        environment:
        - JOB_MANAGER_RPC_ADDRESS=jobmanager

    taskmanager:
        image: ${FLINK_DOCKER_IMAGE_NAME:-flink}
        expose:
        - "6121"
        - "6122"
        depends_on:
        - jobmanager
        command: taskmanager
        links:
        - "jobmanager:jobmanager"
        environment:
        - JOB_MANAGER_RPC_ADDRESS=jobmanager
```

![](https://www.ibm.com/developerworks/cn/opensource/os-cn-apache-flink/img001.png)


- 我们可以了解到 Flink 几个最基础的概念，Client、JobManager 和 TaskManager。  
    - Client 用来提交任务给 JobManager，JobManager 分发任务给 TaskManager 去执行，然后 TaskManager 会心跳的汇报任务状态。

- 在 Flink 集群中，计算资源被定义为 Task Slot。每个 TaskManager 会拥有一个或多个 Slots。JobManager 会以 Slot 为单位调度 Task。
    - 这里可以将 Slot 类比为线程池中的 Worker, 都是资源的抽象, 但是 Slot 更关注内存 

对于应用开发层面的基础概念有

- Source（源）是指数据流进入系统的入口点
- Stream（流）是指在系统中流转的，永恒不变的无边界数据集
- Operator（操作方）是指针对数据流执行操作以产生其他数据流的功能
- Sink（槽）是指数据流离开Flink系统后进入到的位置，槽可以是数据库或到其他系统的连接器

- Flink 最适合的应用场景是低时延的数据处理场景：高并发处理数据，时延毫秒级，且兼具可靠性: 
    1. 低时延：提供 ms 级时延的处理能力。
    1. Exactly Once：提供异步快照机制，保证所有数据真正只处理一次
    1. HA：JobManager 支持主备模式，保证无单点故障。
    1. 水平扩展能力：TaskManager 支持手动水平扩展。

## 批处理
> [Doc](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/)

> [数据转换接口](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/#dataset-transformations)

批处理也被称为离线计算 实时性要求不高 但是数据量大

大致工作流程, 首先 JobManager 生成执行计划的 DAG , 然后发布 Task 给 TaskManager 并行执行
由于是有状态的计算,数据不加以同步的话, 就会混乱, 所以 Flink 通过 [超级步骤同步来保证结果的正确](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/iterations.html#superstep-synchronization) 类似于 Java 并发类中的 CountDownLatch 

其中 这个同步就要求我们应用代码中的 Source Sink 组件中的成员属性 是必须为序列化的, 且不含 transient 关键字修饰的属性
否则 就会报错, 因为无法做到 Task Slots 之间同步数据了, 后续的计算也就无意义了

### Rest API
> [Doc: REST](https://ci.apache.org/projects/flink/flink-docs-stable/monitoring/rest_api.html)

由于批处理不需要实时处理, 所以设计上是按需使用 而不是常驻进程, 所以需要一种机制来调起批处理来执行, 因此有了Rest接口, 但是Rest接口还提供简单的监控

> 上传

- `/jars/upload`
    - 返回结果  {"filename":"/tmp/flink-web-5f9f59f8-9f60-4ccc-a5ae-360cdde7f618/flink-web-upload/ae0dd296-b4ee-4667-9ba8-1c7b374d694c_flink-1.0.0-SNAPSHOT-all-dependency.jar","status":"success"}
    - `curl -X POST -H "Expect:" -F "jarfile=@filepath" http://127.0.0.1:8081/jars/upload`

> 启动

- post: `/jars/{jarid}/run`
    - 参数可选  entry-class program-args/programArg
    - curl -X POST http://127.0.0.1:8081/jars/ae0dd296-b4ee-4667-9ba8-1c7b374d694c_flink-1.0.0-SNAPSHOT-all-dependency.jar/run\?entry-class\=com.github.kuangcp.hi.SimpleStatistic

> 注意: 这里的 参数 只能为单个字符串 或者逗号分割的参数列表, 不能传入 JSON 格式的字符串, 最后解决是用BASE64编码处理

