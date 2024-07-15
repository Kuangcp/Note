---
title: JavaPGO
date: 2024-04-30 22:26:23
tags: 
categories: 
---

💠

- 1. [Java 中的 PGO](#java-中的-pgo)
    - 1.1. [HotSpot](#hotspot)

💠 2024-04-30 23:06:06
****************************************
# Java 中的 PGO

> [Note: PGO base](/Skills/Councurrency/PGO.md)  

- HotSpot 虚拟机默认会在运行期启用PGO。
- GraalVM 企业版本的NativeImage中才能应用PGO技术 `社区版不支持`
    - [Profile-Guided Optimizations ](https://www.graalvm.org/22.0/reference-manual/native-image/PGO/)
    - [Optimize a Native Executable with Profile-Guided Optimizations](https://www.graalvm.org/latest/reference-manual/native-image/guides/optimize-native-executable-with-pgo/)`样例`

> [在Java应用程序中释放峰值性能：配置文件引导优化(PGO)概述](https://www.51cto.com/article/783879.html) [原文](https://dzone.com/articles/unleash-peak-performance-in-java-applications-over)  

## HotSpot
- 方法内联
- 循环展开
- 内存访问模式优化  将内存访问模式与硬件功能相结合来显著提高缓存性能

虽然已经支持在运行期实时收集信息做PGO，但是预先PGO可以省去这个预热过程，但是也有弊端业务变化频繁也就意味着代码变更频繁profile是否准确是否带来负优化是比较难衡量的。  
大型应用启动后做预热的话，可以避免出现应用刚启动时大量的接口或操作的延迟相较于长期运行时高出很多的问题。  

> 采集Profiling
- VisualVM
- YourKit
- Java Flight Recorder
- Async Profiler

> 预热/训练

通过进行全面的训练运行，可以捕获应用程序可能显示广泛的运行时行为。
- 模拟代表常见用户操作的用户交互和工作流。
- 模拟高负载条件的压力测试。
- 探索性测试以覆盖不同的代码路径。
- 负载测试以评估可扩展性。

> Profile文件

Profiling工具从训练运行中收集数据，并将其存储在配置文件数据库或日志文件中， 配置文件数据可能包括如下指标：
- 方法调用计数
- 内存分配和垃圾收集统计
- 线程活动和同步详细信息
- 异常发生和处理
- CPU和内存使用情况

> JIT使用

HotSpot JVM是使用最广泛的Java运行时环境，它通过“分层编译”机制支持PGO， `-XX:+UseProfiledCode` 和`-XX:ProfiledCodeGenerate`控制HotSpot中的PGO。

> 分析与调优
- 识别性能瓶颈：分析性能分析数据以识别性能瓶颈，例如频繁调用的方法、热代码路径或内存密集型操作。
- 优化决策：基于分析数据，做出关于代码优化的明智决策。常见的优化包括方法内联、循环展开、内存访问模式改进和线程同步增强。
- 优化技术：使用适当的技术和编码实践实现所选的优化。
- 基准测试：在进行优化后，对应用程序进行基准测试，以衡量性能改进。使用分析工具来验证优化是否对分析期间确定的瓶颈产生了积极影响。

> 定期重新分析和优化
- 性能优化是一个持续的过程。随着应用程序的技术设计和业务需求的变化，定期重新分析和优化对于保持峰值性能至关重要。在应用程序生命周期的不同阶段继续收集配置文件数据，并相应地调整优化。
- 一个思路便是每次需求升级时，考虑技术和业务变化的影响面，重新生成Profile文件。

