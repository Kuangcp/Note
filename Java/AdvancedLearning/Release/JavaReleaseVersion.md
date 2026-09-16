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
    - 1.22. [Java26](#java26)
    - 1.23. [Java27](#java27)

💠 2026-09-16 20:52:46
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
1. ZGC: 分代模式成为ZGC的默认策略

## Java24
> [OpenJDK 24](https://openjdk.org/projects/jdk/24/)  
> [Oracle 正式发布 Java 24 | Oracle 中国](https://www.oracle.com/cn/news/announcement/oracle-releases-java-24-2025-03-18/)  

1. Late Barrier Expansion for G1 G1 延迟屏障扩展
1. Stream Gatherers (三次预览)
1. Flexible Constructor Bodies (三次预览)
1. Structured Concurrency (四次预览)
1. Scoped Values (四次预览)
1. Module Import Declarations (二次预览)
1. Vector API (八次孵化)
1. [JEP 491: Synchronize Virtual Threads without Pinning](https://openjdk.org/jeps/491)`修复了pinned问题`  

## Java25 LTS
> [详情](/Java/AdvancedLearning/Release/Java25.md)

> [OpenJDK 25](https://openjdk.org/projects/jdk/25/)   
> [Oracle 正式发布 Java 25 | Oracle 中国](https://www.oracle.com/cn/news/announcement/oracle-releases-java-25-2025-09-16/)  

> [JDK25更新了哪些特性？一文全部掌握-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2539734)  

语言特性
1. [JEP 511: Module Import Declarations](https://openjdk.org/jeps/511) 模块导入声明，用一条 import 语句简洁地导入模块导出的所有包
1. [JEP 512: Compact Source Files and Instance Main Methods](https://openjdk.org/jeps/512) 紧凑源文件与实例 main 方法，让初学者无需理解 public/static 等复杂修饰符即可编写第一个程序
1. [JEP 513: Flexible Constructor Bodies](https://openjdk.org/jeps/513) 灵活的构造函数体，允许在构造器中显式 super() 调用之前出现语句
1. [JEP 507: Primitive Types in Patterns, instanceof, and switch (Third Preview)](https://openjdk.org/jeps/507) 模式、instanceof 和 switch 中的基元类型（第三次预览）

库
1. [JEP 506: Scoped Values](https://openjdk.org/jeps/506) 作用域值（正式版），在线程及其子线程间共享不可变数据，比 ThreadLocal 更易理解、开销更低
1. [JEP 505: Structured Concurrency (Fifth Preview)](https://openjdk.org/jeps/505) 结构化并发（第五次预览），把相关多线程任务组视作整体工作单元，简化错误处理与取消
1. [JEP 502: Stable Values (Preview)](https://openjdk.org/jeps/502) 稳定值（预览），持有不可变数据并被 JVM 视为常量，初始化时机比 final 字段更灵活
1. [JEP 508: Vector API (Tenth Incubator)](https://openjdk.org/jeps/508) 向量 API（第十次孵化），在支持的 CPU 上编译为最优向量指令
1. [JEP 510: Key Derivation Function API](https://openjdk.org/jeps/510) 密钥派生函数（KDF）API，从密钥和其他数据派生新密钥

安全库
1. [JEP 470: PEM Encodings of Cryptographic Objects (Preview)](https://openjdk.org/jeps/470) 加密对象的 PEM 编码 API（预览），简化密钥、证书和证书吊销列表的编码与解码

性能更新
1. [JEP 521: Generational Shenandoah](https://openjdk.org/jeps/521) 分代 Shenandoah GC 从实验性转为产品特性
1. [JEP 519: Compact Object Headers](https://openjdk.org/jeps/519) 紧凑对象头从实验性转为产品特性，减少堆内存占用、提升数据局部性

诊断与观测（JFR）
1. [JEP 509: JFR CPU-Time Profiling (Experimental)](https://openjdk.org/jeps/509) JFR CPU 时间剖析（实验性），在 Linux 上捕获更精确的 CPU 时间分析信息
1. [JEP 518: JFR Cooperative Sampling](https://openjdk.org/jeps/518) JFR 协作式采样，仅在安全点遍历调用栈，提升异步采样 Java 线程栈的稳定性
1. [JEP 520: JFR Method Timing & Tracing](https://openjdk.org/jeps/520) JFR 方法计时与跟踪，借助字节码插桩实现方法级计时和跟踪

Project Leyden 特性
1. [JEP 514: Ahead-of-Time Command-Line Ergonomics](https://openjdk.org/jeps/514) AOT 命令行易用性，简化常用场景下创建提前缓存以加速启动的命令
1. [JEP 515: Ahead-of-Time Method Profiling](https://openjdk.org/jeps/515) AOT 方法剖析，让上一次运行的方法执行档案在 JVM 启动时立即可用，加快预热

清理特性
1. [JEP 503: Remove the 32-bit x86 Port](https://openjdk.org/jeps/503) 移除 32 位 x86 端口的源码和构建支持（JDK 24 已标记弃用）

## Java26 
> [OpenJDK 26](https://openjdk.org/projects/jdk/26/)
> [Oracle 正式发布 Java 26 | Oracle 中国](https://www.oracle.com/cn/news/announcement/oracle-releases-java-26-2026-03-17/)  

语言特性
1. [JEP 530: Primitive Types in Patterns, instanceof, and switch (Fourth Preview)](https://openjdk.org/jeps/530) 模式、instanceof 和 switch 中的基元类型（第四预览版），消除基元类型在模式匹配中的限制，增强编译器错误检测

性能更新
1. [JEP 522: G1 GC — Improve Throughput by Reducing Synchronization](https://openjdk.org/jeps/522) 通过双卡表减少写屏障的同步开销，提高 G1 垃圾收集器的吞吐量

Project Leyden 特性
1. [JEP 516: Ahead-of-Time Object Cache for Any GC](https://openjdk.org/jeps/516) 支持任意 GC 的提前对象高速缓存，加快 Java 应用启动速度

库
1. [JEP 500: Prepare to Make `final` Meaningful](https://openjdk.org/jeps/500) 对通过深度反射修改 final 字段发出警告，强化 Java 的"默认完整性"原则
1. [JEP 517: HTTP/3 Support for the HTTP Client API](https://openjdk.org/jeps/517) 为 HTTP 客户端 API 新增 HTTP/3 协议支持，降低延迟
1. [JEP 526: Lazy Constants (Second Preview)](https://openjdk.org/jeps/526) 延迟常量 API，JVM 将其视为真正常量以实现 final 字段级别的性能
1. [JEP 525: Structured Concurrency (Sixth Preview)](https://openjdk.org/jeps/525) 结构化并发，将多线程任务组视作整体工作单元，降低线程泄漏和取消延迟风险
1. [JEP 529: Vector API (Eleventh Incubator)](https://openjdk.org/jeps/529) 向量 API，编译为 CPU 最优向量指令，加速数据分析、AI 推理

安全库
1. [JEP 524: PEM Encoding of Cryptographic Objects (Second Preview)](https://openjdk.org/jeps/524) 加密对象的 PEM 编码 API，简化加密设置和集成

清理特性
1. [JEP 504: Remove the Applet API](https://openjdk.org/jeps/504) 正式移除 Applet API（JDK 17 标记待移除）

## Java27
> [OpenJDK 27](https://openjdk.org/projects/jdk/27/)  
> [Oracle 正式发布 Java 27 | Oracle](https://www.oracle.com/news/announcement/oracle-releases-java-27-and-strengthens-post-quantum-cryptography-support-2026-09-15/)  

语言特性
1. [JEP 532: Primitive Types in Patterns, instanceof, and switch (Fifth Preview)](https://openjdk.org/jeps/532) 模式、instanceof 和 switch 中的基元类型（第五预览版），允许基元类型出现在所有模式上下文，并扩展 instanceof 与 switch 支持全部基元类型

性能更新
1. [JEP 523: Make G1 the Default Garbage Collector in All Environments](https://openjdk.org/jeps/523) 让 G1 在所有环境（而不只是服务器环境）中成为默认垃圾收集器
1. [JEP 534: Compact Object Headers by Default](https://openjdk.org/jeps/534) 默认启用紧凑对象头，在 64 位架构上将对象头从 96 位降至 64 位，减少堆占用、提升部署密度和数据局部性

诊断与观测（JFR）
1. [JEP 536: JFR In-Process Data Redaction](https://openjdk.org/jeps/536) JFR 进程内数据脱敏，在数据离开进程前对命令行参数、环境变量和系统属性的初始值进行脱敏，避免敏感信息泄露

库
1. [JEP 531: Lazy Constants (Third Preview)](https://openjdk.org/jeps/531) 延迟常量（第三次预览），JVM 将其视为真正常量以获得 final 字段级别的性能，同时初始化时机更灵活
1. [JEP 533: Structured Concurrency (Seventh Preview)](https://openjdk.org/jeps/533) 结构化并发（第七次预览），将多线程任务组视作整体工作单元，简化错误处理与取消，提高可靠性与可观测性
1. [JEP 537: Vector API (Twelfth Incubator)](https://openjdk.org/jeps/537) 向量 API（第十二次孵化），在支持的 CPU 上编译为最优向量指令，加速数值计算

安全库
1. [JEP 527: Post-Quantum Hybrid Key Exchange for TLS 1.3](https://openjdk.org/jeps/527) TLS 1.3 后量子混合密钥交换，将抗量子算法与传统算法结合，默认抵御未来量子计算攻击
1. [JEP 538: PEM Encodings of Cryptographic Objects (Third Preview)](https://openjdk.org/jeps/538) 加密对象的 PEM 编码 API（第三次预览），简化密钥、证书和证书吊销列表的编码与解码

