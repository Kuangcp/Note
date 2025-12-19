---
title: Java主要发行版概述
date: 2018-11-21 10:56:52
tags: 
categories: 
    - Java
---

💠

- 1. [Java主要发行版本](#java主要发行版本)
    - 1.1. [Java5](#java5)
    - 1.2. [Java6](#java6)
    - 1.3. [Java7](#java7)
    - 1.4. [Java8 LTS](#java8-lts)
    - 1.5. [Java9](#java9)
    - 1.6. [Java10](#java10)
    - 1.7. [Java11 LTS](#java11-lts)
    - 1.8. [Java12](#java12)
    - 1.9. [Java13](#java13)
    - 1.10. [Java14](#java14)
    - 1.11. [Java15](#java15)
    - 1.12. [Java16](#java16)
    - 1.13. [Java17 LTS](#java17-lts)
    - 1.14. [Java18](#java18)
    - 1.15. [Java19](#java19)
    - 1.16. [Java20](#java20)
    - 1.17. [Java21 LTS](#java21-lts)
    - 1.18. [Java22](#java22)
    - 1.19. [Java23](#java23)
    - 1.20. [Java24](#java24)
    - 1.21. [Java25 LTS](#java25-lts)

💠 2025-12-16 20:19:27
****************************************
# Java主要发行版本
> [官网 Release Note](http://www.oracle.com/technetwork/java/javase/jdk-relnotes-index-2162236.html)

> [Java语言特性系列 5-最新](https://segmentfault.com/a/1190000004417288)

> [参考: JDK的版本号解惑](https://blog.csdn.net/bisal/article/details/118947676)  

![](/Java/AdvancedLearning/Release/img/001-jdk-release.km.svg)

## Java5
泛型 枚举 装箱拆箱 静态导入 foreach

## Java6 
JDBC4.0  JAX-WS 2.0

## Java7
> [详情](/Java/AdvancedLearning/Release/Java7.md)

1. 语法糖:数字中的下划线
1. 新的语言小特性:TWR(try with resources)
1. 类文件格式的变化:注解
1. JVM的新特性: 动态调用
1. 引入G1收集器

## Java8 LTS
> [详情](/Java/AdvancedLearning/Release/Java8.md)

1. 接口中新增 静态方法,默认方法
1. 新增 Optional
1. 新增 Lambda
1. 新增 Stream
1. java.time 包 增强了日期时间的处理

- 181 子版本移除了 Derby 

## Java9
> [参考: Java 9 新特性概览 ](http://www.runoob.com/java/java9-new-features.html)

> [参考: Java9 新特性汇总](http://www.infoq.com/cn/news/2014/09/java9)  
> [参考: Java 9 新特性概述](https://www.ibm.com/developerworks/cn/java/the-new-features-of-Java-9/index.html)  
> [参考: 深入解读 Java 9 新特性 ](https://mp.weixin.qq.com/s?__biz=MzAwMDU1MTE1OQ==&mid=2653549131&idx=1&sn=77997b94cc91fb7cbead6b7888f26474&chksm=813a63d3b64deac5506a5c0080718eb759720ec17538223af71b865f260428cc7c644d2d97de&scene=21#wechat_redirect)  

1. Jigsaw 模块化
1. Stream Optional 改进
1. 内置 轻量级 JSON API
1. HTTP2 客户端
1. 云原生适配
1. 默认GC更换为G1

## Java10 
> [参考: Java10的新特性](https://segmentfault.com/a/1190000014076481)

1. 类型推断
1. String 类 API 增强
1. 集合 API 增强
1. Stream 增强
1. Optional 增强
1. java javac 合并

## Java11 LTS
> [详情](/Java/AdvancedLearning/Release/Java11.md)

> [参考: Java11的新特性](https://segmentfault.com/a/1190000016527932#articleHeader5)

1. Flight Recorder 开源
1. Epsilon 空gc实现： 用于性能测试
1. HttpClient 默认实现

> [Oracle JDK11 Migration Guide](https://docs.oracle.com/en/java/javase/11/migrate/index.html)  
> [Jdk8到jdk11 Springboot 踩坑指南](https://blog.csdn.net/ab601026460/article/details/86062991)  

> Illegal reflective access by org.springframework.cglib.core.ReflectUtils
- 增加JVM参数 --add-opens java.base/java.lang=ALL-UNNAMED

## Java12 
> [OpenJDK 12](https://openjdk.org/projects/jdk/12/)

1. Switch Expressions (预览)
1. Shenandoah GC: 低暂停时间垃圾收集器 (实验性)
1. JVM Constants API
1. 默认 CDS 归档
1. G1 增强: 
    - 可中止的混合收集
    - 及时返回未使用的已提交内存
1. 微基准测试套件
1. String API 增强: `indent()` `transform()`

## Java13 
1. Text Blocks (文本块) 预览版
1. Switch Expressions 改进
1. 重新实现 Socket API
1. Dynamic CDS Archives 动态归档
1. ZGC 增强: 取消提交未使用的内存

## Java14
1. Switch Expressions 正式版
1. instanceof 模式匹配 (预览)
1. Records 记录类型 (预览)
1. Text Blocks 改进
1. NullPointerException 增强: 更详细的异常信息
1. 删除 CMS 垃圾收集器

## Java15 
1. Text Blocks 正式版
1. Sealed Classes 密封类 (预览)
1. Hidden Classes 隐藏类
1. Records 改进 (二次预览)
1. instanceof 模式匹配 (二次预览)
1. ZGC 和 Shenandoah GC 转正
1. 移除 Nashorn JavaScript 引擎

## Java16 
1. Records 正式版
1. instanceof 模式匹配 正式版
1. Sealed Classes (二次预览)
1. Vector API (孵化器)
1. 启用 C++14 语言特性
1. ZGC 并发线程栈处理
1. Unix-Domain Socket Channels

## Java17 LTS
1. Sealed Classes 正式版
1. 恢复始终严格的浮点语义
1. Pattern Matching for switch (预览)
1. 移除 RMI Activation
1. 弃用 Applet API
1. 强封装 JDK 内部 API
1. Context-Specific Deserialization Filters

> [从JDK 8升级到JDK 17踩坑全过程](https://cloud.tencent.com/developer/article/2240195)  

`jdeps --jdk-internals --multi-release 17 --class-path . encloud-api.jar` 分析依赖的废弃api

## Java18
1. UTF-8 默认字符集
1. Simple Web Server 简单 Web 服务器
1. 代码片段 Javadoc 标签
1. Pattern Matching for switch (二次预览)
1. Vector API (三次孵化)
1. 弃用 Finalization 机制
1. 互联网地址解析 SPI

## Java19
1. Record Patterns (预览)
1. Pattern Matching for switch (三次预览)
1. Virtual Threads 虚拟线程 (预览)
1. Structured Concurrency 结构化并发 (孵化)
1. Vector API (四次孵化)
1. Foreign Function & Memory API (预览)

## Java20
1. Record Patterns (二次预览)
1. Pattern Matching for switch (四次预览)
1. Virtual Threads (二次预览)
1. Structured Concurrency (二次孵化)
1. Scoped Values (孵化)
1. Vector API (五次孵化)

## Java21 LTS
> [OpenJDK  21](https://openjdk.org/projects/jdk/21/)

1. 字符串模板 `语法糖` (预览)
1. 分代ZGC 
1. 虚拟线程 正式版 `协程 轻量级线程 用户级线程` 
1. Sequenced Collections 有序集合
1. Record Patterns 正式版
1. Pattern Matching for switch 正式版
1. Structured Concurrency (预览)
1. Scoped Values (预览)

> [Java21新特性](https://segmentfault.com/a/1190000044238496)

## Java22
> [OpenJDK 22](https://openjdk.org/projects/jdk/22/)

1. Unnamed Variables & Patterns 未命名变量和模式 (预览)
1. String Templates 字符串模板 (二次预览)
1. Statements before super() 构造函数中 super() 之前可以使用语句 (预览)
1. Foreign Function & Memory API (预览)
1. Region Pinning for G1 GC: G1 GC 区域固定
1. Structured Concurrency (二次预览)
1. Scoped Values (二次预览)
1. Stream Gatherers (预览)

## Java23
> [OpenJDK 23](https://openjdk.org/projects/jdk/23/)

1. Primitive Types in Patterns 模式中的基本类型 (预览)
1. Module Import Declarations 模块导入声明 (预览)
1. Markdown Documentation Comments Markdown 文档注释 (预览)
1. Flexible Constructor Bodies 灵活的构造函数体 (二次预览)
1. Stream Gatherers (二次预览)
1. Structured Concurrency (三次预览)
1. Scoped Values (三次预览)
1. Class-File API (预览)
1. ZGC: 分代模式成为默认

## Java24
> [OpenJDK 24](https://openjdk.org/projects/jdk/24/)

1. Late Barrier Expansion for G1 G1 延迟屏障扩展
1. Stream Gatherers (三次预览)
1. Flexible Constructor Bodies (三次预览)
1. Structured Concurrency (四次预览)
1. Scoped Values (四次预览)
1. Module Import Declarations (二次预览)
1. Vector API (八次孵化)

## Java25 LTS
> [OpenJDK 25](https://openjdk.org/projects/jdk/25/) (LTS预期)

> [JDK25更新了哪些特性？一文全部掌握-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2539734)  

1. 虚拟线程和并发模型的进一步优化
1. Loom 项目完善: 结构化并发预览
1. JEP 506: Scoped Values： 线程间共享变量，用来替换的ThreadLocal。

