---
title: Java问题排查手册
date: 2023-08-25 15:51:12
tags: 
categories: 
---

💠

- 1. [Troubleshoot](#troubleshoot)
    - 1.1. [GC](#gc)
        - 1.1.1. [主要关注指标](#主要关注指标)
    - 1.2. [Memory](#memory)
    - 1.3. [CPU](#cpu)
        - 1.3.1. [线程](#线程)
    - 1.4. [ClassLoader](#classloader)

💠 2024-06-01 13:47:36
****************************************
# Troubleshoot
当遇到需要对某个Java应用性能调优，故障处理时的技能或思路汇总

> Troubleshooting: [Oracle: Java8](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/) | [Oracle: Java11](https://docs.oracle.com/en/java/javase/11/troubleshoot/general-java-troubleshooting.html)  

> [目前最全的Java服务问题排查套路](https://juejin.cn/post/6844903816379236360)  
> [完蛋，我被故障包围了](https://www.bilibili.com/video/BV1vc411U78U/?buvid=XXF1096F78012CCE01D64B283450438CC6206)`采用各种工具分析和排查`  

************************

![](./img/mind.drawio.svg)

`不可用故障处理` **重要且紧急**

> 基础设施层：寻求方式快速搭建新的一层（例如K8S的命名空间下全部服务重建），立马切换解析或网关流量  
> JVM层：记录好后续排查分析故障现场的必要信息后（dump，日志，linux系统日志），立马重启，释放本该释放的资源或中断已经异常的流程  

排查思路：
- `Delta` 正式环境可复现问题，测试或灰度无法出现，且不能轻易重启正式环境，通过对生产的JVM做各类指标的记录，对比某个业务操作前后或故障前后的指标差异分析出问题的触发点
    - 限制：不能做太影响性能的指标记录和分析
- `Debug` 在测试或灰度环境上可复现问题，可直接Debug接入调试代码，或本地采用高耗能的方式debug分析`抓包，strace，CPU火焰图，等方式`
    - 限制：**可复现**，通常能有这个条件已经能直接通过debug代码就能解决问题了

************************

`性能调优`
> [Linux 性能分析](/Linux/Base/LinuxPerformance.md)  
> [Linux 网络](/Linux/Base/LinuxNetwork.md)  
> [JVM 分析工具](/Java/AdvancedLearning/JvmTool.md)  

## GC
> [Java GC](/Java/AdvancedLearning/JvmGC.md)

> [Java中9种常见的CMS GC问题分析与解决](https://tech.meituan.com/2020/11/12/java-9-cms-gc.html)

> [大量类加载器创建导致诡异FullGC](https://heapdump.cn/article/1924890)
> [参考: 译：谁是 JDK8 中最快的 GC](https://club.perfma.com/article/233480)  
> [《沙盘模拟系列》JVM如何调优](https://my.oschina.net/u/4030990/blog/3149182)  
> [深入浅出GC问题排查](https://blog.ysboke.cn/archives/242.html)
> [参考: CMS Deprecated. Next Steps?](https://dzone.com/articles/cms-deprecated-next-steps)  

- [Oracle JDK8 GC调优指南](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/toc.html)
- [Oracle JDK11 GC调优指南](https://docs.oracle.com/en/java/javase/11/gctuning/introduction-garbage-collection-tuning.html)

`工具`
> [gceasy.io](https://gceasy.io)  
> [GCViewer](https://github.com/chewiebug/GCViewer)  

`实践`
> [从实际案例聊聊Java应用的GC优化](https://tech.meituan.com/2017/12/29/jvm-optimize.html)`观察监控指标调整JVM参数： 年轻代 晋升阈值等`  
> 根本原则是每一次GC都回收尽可能多的对象，降低GC次数减少无用的扫描和暂停开销

### 主要关注指标
> [garbage-collection-kpi](https://blog.gceasy.io/2016/10/01/garbage-collection-kpi/)  
> [What are Throughput Performance, Latency Performance, and Memory Footprint in Java Programming? ](https://www.h2kinfosys.com/blog/what-are-throughput-performance-latency-performance-and-memory-footprint-in-java-programming/)  

> 三者不可兼得，通常兼顾两者舍弃另一方
- `延迟（Latency）`： 也可以理解为最大停顿时间，即垃圾收集过程中单次 STW 的最长时间，越短越好，一定程度上可以接受频次的增多，是 GC 技术的主要发展方向。
- `吞吐量（Throughput）`： 应用系统的生命周期内，由于 GC 线程会占用 Mutator 当前可用的 CPU 时钟周期，吞吐量即为 Mutator 有效花费的时间占系统总运行时间的百分比
    - 例如应用系统运行了 100 min，GC 累计耗时 1 min，则系统吞吐量为 99%，通常目标是**超过95%**。
    - 吞吐量优先的垃圾收集器会倾向于接受`单次耗时较长`的停顿，`累计停顿耗时短`的GC策略。
- `内存占用（Footprint）`： 取决于不同的GC算法和内存设置，通常来说 Parallel CMS会消耗更多，Serial会消耗更少

延迟

- 响应时间目标是平均目标吗？是否以百分位数表示，例如第50、90、95 或 99 个百分位数的响应时间？ `常见为使用后者`
- 响应时间目标是否是一个永远不应该被超越的绝对最小值？ 是否有可能超过响应时间目标？ 如果可以的话，可以添加多少？ 又可以超过多长时间呢？ `完全取决于业务，不过在产品学上400ms是肉眼感知的最慢阈值`
- 如何评估响应时间？ 在哪里进行响应时间测量？ `APM类系统实现监控和告警`

吞吐量

- Java 编程性能目标是否被视为峰值性能目标？ 或者吞吐量目标是应用程序必须始终满足的性能目标吗？`主要取决于业务（目前横向扩展成本很低，此项的考虑优先级通常会更低）`
- 应用程序预期处理的最高负载是多少？例如，预计有多少并发或活动用户、并发或活动事务？`业务预估，建立在完善的监控和稳定业务基础上`
- 如果应用程序的负载超过预计负载，吞吐量是否会下降到性能目标以下？ 
    - 如果可以的话，它能低于绩效目标多久？或者，应用程序应在其最大容量或负载增加的情况下继续运行多长时间？`极限值的边界问题`
- 应用程序在不同负载级别下是否有可以消耗的最大 CPU 量，或者是否有预期的 CPU 量？如果 CPU 使用有上限，超出该限制还可以使用多少 CPU，允许使用多长时间？
- 如何评估应用程序的吞吐量？ 吞吐量的计算在哪里进行？ `APM系统`

内存占用

- 应用程序中预期使用的内存量是否仅包含 Java 堆大小？或者这个总和是否也考虑了 JVM 或应用程序消耗的本机 RAM？ 
    - 使用的 RAM 量如何计算？ 该统计信息是否会考虑操作系统报告的 JVM 进程驻留内存大小？Java堆上当前数据的数量是否也包括在内？`RAM量严格来说包含 堆，堆外，元空间，二进制库`
- 有没有可能永远不会超过预期的内存消耗？如果有的话，可能会超过预期的内存消耗多少？ 又可以超过多长时间呢？`取决于宿主机，通常不建议超限制运行，不利于容器调度`
- 何时评估内存使用情况？ 是否会测量应用程序的空闲时间？当程序运行在稳定状态时？ 负载何时达到峰值？ `APM`

************************

## Memory 
- [Blog:java优化占用内存的方法(一)](http://blog.csdn.net/zheng0518/article/details/48182437)

- [GC 性能优化 专栏](https://blog.csdn.net/column/details/14851.html)
- [Java调优经验谈](http://www.importnew.com/22336.html)

- [Memory Footprint of A Java Process](https://zhuanlan.zhihu.com/p/158712025)

> [Java OOM](/Java/AdvancedLearning/Tuning/JavaOOM.md)

************************

## CPU

> 问题：优化一个业务方法延迟，找出CPU成本高的点
- Arthas trace 指定的方法 
    - `偶现或者高并发时才出现怎么办` 考虑使用脚本将捕获的调用信息存入日志，在手动解析产生的大量日志统计分析
- JMC，JProfiler，Visualvm 等工具捕获CPU火焰图
- APM类监控系统。例如：CAT

### 线程
> [jstack.review Analyze java thread dumps](https://jstack.review)

************************

## ClassLoader

**加载错误的类**

由于开源项目的 groupId  artifactId 可能发生变化`asm netty commons-io 等`，且类结构和设计也有调整，容易引发隐式的类加载错误

> [【踩坑】 Maven中依赖的隐式冲突 可能导致的 NoClassDefFoundError NoSuchMethodException 等问题](https://blog.csdn.net/kcp606/article/details/92245936?spm=1001.2014.3001.5502)
> [使用easyexcel时遇到Could not initialize class cglib.beans.BeanMap怎么解决 ](https://mp.weixin.qq.com/s?__biz=MzAwMjk5NTY3Mw==&mid=2247483950&idx=1&sn=47c6c1fed54b134f46f6dedafd34db0c&chksm=9ac0a698adb72f8e769bcfbff5a4fb0450f181bb754a2ad615dc17002f14d7ec039c0e24a1d7&token=395785991&lang=zh_CN#rd)

> 思路
- `Maven Helper` IDE 插件检查依赖冲突
- `lsof -p PID | grep jar` 项目启动后查看加载到进程的jar
- `-verbose:class` 输出运行期加载的class信息

************************

**类加载阻塞业务线程**

由于类加载是JVM层面同步执行，如果业务行为中会高频用到类加载器的话会大大降低吞吐量，例如 [druid连接池引起的线程blocked](https://segmentfault.com/a/1190000041500544)


