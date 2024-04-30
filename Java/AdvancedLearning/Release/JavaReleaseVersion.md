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
    - 1.4. [Java8 LST](#java8-lst)
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
    - 1.15. [Java21 LTS](#java21-lts)

💠 2024-04-30 23:06:06
****************************************
# Java主要发行版本
> [官网 Release Note](http://www.oracle.com/technetwork/java/javase/jdk-relnotes-index-2162236.html)

> [Java语言特性系列 5-最新](https://segmentfault.com/a/1190000004417288)

> [参考: JDK的版本号解惑](https://blog.csdn.net/bisal/article/details/118947676)  

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

## Java8 LST
> [详情](/Java/AdvancedLearning/Release/Java8.md)

1. 接口中新增 静态方法,默认方法
1. 新增 Optional
1. 新增 Lambda
1. 新增 Stream
1. java.time 包 增强了日期时间的处理

- 181 版本移除了 Derby 

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

> [Jdk8到jdk11 Springboot 踩坑指南](https://blog.csdn.net/ab601026460/article/details/86062991)  

> Illegal reflective access by org.springframework.cglib.core.ReflectUtils
- 增加JVM参数 --add-opens java.base/java.lang=ALL-UNNAMED

## Java12 
1. Shenandoah GC
1. Switch Expressions

## Java13 

## Java14

## Java15 

## Java16 

## Java17 LTS

> [从JDK 8升级到JDK 17踩坑全过程](https://cloud.tencent.com/developer/article/2240195)  

`jdeps --jdk-internals --multi-release 17 --class-path . encloud-api.jar` 分析依赖的废弃api

## Java18

## Java21 LTS
> [OpenJDK  21](https://openjdk.org/projects/jdk/21/)

1. 分代ZGC 
1. 虚拟线程`协程 轻量级线程 用户级线程` 总结：如果要引入生产，需要关注整个JEP的文档，调试确认细节后才能使用，不然就会陷入到各种诡异的问题上。
    - 同样是依赖一个共用的ForkJoin线程池执行代码 即 不推荐执行CPU耗时代码，只建议用来执行io等待类代码（21对有可能阻塞的api都加上了特定处理代码），提高吞吐量
    - 正常代码无法感知 协程内代码的异常，反之也是一样，局部变量也是隔离的
    - 协程的线程栈存储在堆内存中，为了规避大量协程导致的栈溢出


> [Java21新特性](https://segmentfault.com/a/1190000044238496)
