# Flink 中的批处理

## 为何有这次分享
最近实现的需求是采用的该架构设计实现, 也是一边学习一边思考整理

https://www.cnblogs.com/ken-io/p/knowledge-or-technology-share-guide.html

https://blog.csdn.net/wenxueliu/article/details/89484375
************************

## Flink 是什么
> [官网](https://flink.apache.org/)

Flink 是一个批处理和流处理结合的统一计算框架，其核心是一个提供了数据分发以及并行化计算的流数据处理引擎。

>> 同类框架还有 经典的 Hadoop Map-Reduce, 架构简单, 不能支持复杂的应用逻辑, 需要应用逻辑 适配到 map-reduce算法, 仅支持批处理, 

Spark批处理, 流处理的实现是将批处理的批次分割成若干小

Flink基于每个事件一行一行地流式处理，真正的流式计算，流式计算跟Storm性能差不多，支持毫秒级计算，而Spark则只能支持秒级计算。

> [美团: 流计算框架 Flink 与 Storm 的性能对比](https://tech.meituan.com/2017/11/17/flink-benchmark.html)

### 流处理和批处理
批处理主要操作大容量静态数据集，并在计算过程完成后返回结果。

- 批处理模式中使用的数据集通常符合下列特征：
    1. 有界：批处理数据集代表数据的有限集合
    1. 持久：数据通常始终存储在某种类型的持久存储位置中
    1. 大量：批处理操作通常是处理极为海量数据集的唯一方法

批处理非常适合需要访问全套记录才能完成的计算工作。例如在计算总数和平均数时

- 流处理中的数据集是“无边界”的，这就产生了几个重要的影响：
    1. 完整数据集只能代表截至目前已经进入到系统中的数据总量。
    1. 工作数据集也许更相关，在特定时间只能代表某个单一数据项。
    1. 处理工作是基于事件的，除非明确停止否则没有“尽头”。处理结果立刻可用，并会随着新数据的抵达继续更新。

流处理系统可以处理几乎无限量的数据，但同一时间只能处理一条（真正的流处理）或很少量（微批处理，Micro-batch Processing）数据，不同记录间只维持最少量的状态。虽然大部分系统提供了用于维持某些状态的方法，但流处理主要针对副作用更少，更加功能性的处理（Functional processing）进行优化。

## 基础概念和原理
https://blog.csdn.net/kamroselee/article/details/84102035

https://www.ibm.com/developerworks/cn/opensource/os-cn-apache-flink/

https://www.jianshu.com/p/ca3c1c73eed9

https://www.cnblogs.com/frankdeng/p/9400622.html

![](https://www.ibm.com/developerworks/cn/opensource/os-cn-apache-flink/img001.png)

我们可以了解到 Flink 几个最基础的概念，Client、JobManager 和 TaskManager。Client 用来提交任务给 JobManager，JobManager 分发任务给 TaskManager 去执行，然后 TaskManager 会心跳的汇报任务状态。

在 Flink 集群中，计算资源被定义为 Task Slot。每个 TaskManager 会拥有一个或多个 Slots。JobManager 会以 Slot 为单位调度 Task。

Flink 最适合的应用场景是低时延的数据处理场景：高并发处理数据，时延毫秒级，且兼具可靠性。

- 典型应用场景有：
    1. 互联网金融业务。
    1. 点击流日志处理。
    1. 舆情（舆论情绪）监控。 Flink 的特点有以下几种：
    1. 低时延：提供 ms 级时延的处理能力。
    1. Exactly Once：提供异步快照机制，保证所有数据真正只处理一次
    1. HA：JobManager 支持主备模式，保证无单点故障。
    1. 水平扩展能力：TaskManager 支持手动水平扩展。

对于应用开发层面的基础概念有

- Source（源）是指数据流进入系统的入口点
- Stream（流）是指在系统中流转的，永恒不变的无边界数据集
- Operator（操作方）是指针对数据流执行操作以产生其他数据流的功能
- Sink（槽）是指数据流离开Flink系统后进入到的位置，槽可以是数据库或到其他系统的连接器


### 部署
> Local, Standalone Cluster

- Local 模式的 JobManager 和 TaskManager 只使用一个 JVM 来完成整个计算, 常用于小数据量的开发测试

- Standalone Cluster 模式的 JobManager 和 TaskManager 都是单点且各自独立的, 例如以下通过 docker-compose 部署的案例

#### Rest API
> [](https://ci.apache.org/projects/flink/flink-docs-stable/monitoring/rest_api.html)

## 批处理应用场景
> [Doc](https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/batch/)

也被称为离线计算 实时性要求不高, 可以分割任务提高效率

## 展望
Docker 或者 k8s 统一环境, 方便开发测试
