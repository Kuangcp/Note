---
title: Java Readme
date: 2020-03-27 15:28:15
tags: 
    - Readme
categories: 
    - Java
---

💠

- 1. [计算机基础](#计算机基础)
- 2. [Java](#java)
    - 2.1. [JDK](#jdk)
    - 2.2. [JavaFX](#javafx)
- 3. [相关资源](#相关资源)
    - 3.1. [Java Programer Suggestion](#java-programer-suggestion)
- 4. [环境配置](#环境配置)

💠 2024-02-03 10:54:46
****************************************
# 计算机基础

>- [算法](/Algorithm/Algorithm.md)  
>- [计算机基础](/Skills/CS/Computer.md)  
>- [并发基础](/Skills/Councurrency/)  
>- [计算机网络](/Skills/Network/)  
>- [测试理论](/Skills/Test/TestTheory.md)  

*************************************
# Java
[Oracle JavaSE Overview](http://www.oracle.com/technetwork/java/javase/overview/index.html) | [openjdk ](http://openjdk.java.net/) | [AdoptOpenJDK mirrors](https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/)   

> [Oracle: java tutorial](https://docs.oracle.com/javase/tutorial/java/) `入门时首先通读一遍`  
> [java turtorials](https://www.geeksforgeeks.org/java-tutorials/) `能在线运行简易Java代码`

> [wiki: java language](https://en.wikipedia.org/wiki/Java_%28programming_language%29)  

> [如何快速打好Java基础？](https://www.zhihu.com/question/50904128)  
> [tutorials](https://github.com/eugenp/tutorials)  
> [Java 故障处理](/Java/AdvancedLearning/Tuning/Readme.md)  
> [JSRs: Java Specification Requests](https://jcp.org/en/jsr/all)`社区确认的标准`  

********************

| 基础 | 进阶 |
|:----|:----|
| [基础语法](/Java/AdvancedLearning/JavaBasicSyntax.md)  | [反射](/Java/AdvancedLearning/JavaReflection.md) |
| [继承和接口](/Java/AdvancedLearning/JavaInheritedAndInterface.md)  | [JVM](/Java/AdvancedLearning/JVM.md) |
| [异常](/Java/AdvancedLearning/JavaException.md)  | [字节码](/Java/AdvancedLearning/JavaClass.md) |
| [泛型](/Java/AdvancedLearning/JavaGenerics.md)  | [测试](/Java/Test/JavaTest.md) | 
| [集合](/Java/AdvancedLearning/JavaCollection.md)  | [打包部署](/Java/AdvancedLearning/JavaDeploy.md) |
| [线程](/Java/AdvancedLearning/JavaThread.md)  | [持续集成 CI](/Skills/DevOps/ContinuousIntegration.md) |
| [并发](/Java/AdvancedLearning/JavaConcurrency.md)  | [网络编程](/Java/AdvancedLearning/JavaNetwork.md) |
| [IO](/Java/AdvancedLearning/JavaIO.md)  |  |
| [注解](/Java/AdvancedLearning/JavaAnnotation.md)  |  |
| [JDBC](/Java/AdvancedLearning/JDBC.md) | |

## JDK
>- [JDK and JRE](/Java/AdvancedLearning/JDKAndJRE.md)
>- [Java 发行版大致特性](/Java/AdvancedLearning/JavaReleaseVersion.md)
>- [Java7](/Java/AdvancedLearning/Java7.md)
>- [Java8](/Java/AdvancedLearning/Java8.md)
>- [Java11](/Java/AdvancedLearning/Java11.md)

## JavaFX
> [OpenJFX](https://wiki.openjdk.java.net/display/OpenJFX) | [official site](https://openjfx.io)

# 相关资源
> [Java核心知识思维导图](https://gitee.com/gin9/MindMap)  
> [阿里巴巴Java开发手册](https://github.com/alibaba/p3c) | [阿里巴巴Java开发手册](/Java/AlibabaJavaStandard.md)  

> [effective-java-3rd ](https://github.com/sjsdfg/effective-java-3rd-chinese)  

>- [Github Topic: Java](https://github.com/topics/java)

>- [Java成神之路](https://github.com/hollischuang/toBeTopJavaer)
>- [JCSprout](https://github.com/crossoverJie/JCSprout)
>- [awesome-java](https://github.com/akullpp/awesome-java)
>- [awesome-java-cn](https://github.com/jobbole/awesome-java-cn)
>- [architect-awesome](https://github.com/xingshaocheng/architect-awesome)
>- [advanced-java](https://github.com/doocs/advanced-java)
>- [java-learning](https://github.com/brianway/java-learning)
>- [tutorials](https://github.com/eugenp/tutorials)`Java生态Demo集`
>- [Java guide](https://github.com/Snailclimb/JavaGuide)
>- [LearningNotes](https://github.com/francistao/LearningNotes)`安卓`
>- [Java思维导图](https://gitee.com/java-mindmap/mapSource)

>- [google: style guide](https://google.github.io/styleguide/javaguide.html)
>- [Java8 api 中文版 Google翻译](https://blog.fondme.cn/posts/21004/)
>- [唯品会的规范文档](https://github.com/vipshop/vjtools)`规范这种东西, 各有各家的说法, 适合自己就好`
>- [daydayup](https://github.com/ITDragonBlog/daydayup)`Java架构师成长之路`

>- [99 Problems](https://github.com/shekhargulati/99-problems)

>- [模式之禅](/Java/DesignPattern.md)
>- [Google: GWT](https://www.gwtproject.org/doc/latest/tutorial/index.html)`Java写前端，邪教`  

## 前辈建议
Java 中有三大支柱（多线程、网络和安全），在 java.util.concurrent、java.security、javax.cropty、javax.security 四个包中就占了两个（多线程、安全）  
还有一个网络在 java.net、javax.net 中  掌握了上面 6 个包及其子包中内容的话，那 Java 水平可以说达到了另一种境界。

**多线程（multi-threading and concurrent）**

1. 关键词：volatile, sychronized
2. 传统的线程 API：java.lang.Thread, java.lang.Runnable, java.lang.ThreadGroup, Object#wait, Object#notify, Object#notifyAll
3. JDK 5 并发包（java.util.concurrent）API：线程池、任务执行器、计数信号量、倒计数门闩、并发集合（并发 Map、阻塞队列等）、基于 CPU CAS 指令的原子 API（java.util.concurrent.atomic）、锁 API（java.util.concurrent.lock）和条件对象等。
4. 作为个人知识提升，还需要理解诸如自旋锁、分离锁、分拆锁、读写锁等的同步锁策略，以及可重入锁、锁的公平性的意义。以及各种并发锁的算法，比如：Peterson锁、Bakery锁 等等，以及现代 CPU 体系结构

涉及多线程及并发的 API 在 java.lang 中及 java.util.concurrent.* 中。

**网络（network communication）**

1. 阻塞 TCP 通信、阻塞 UDP 通信、组播
2. 非阻塞 TCP 通信、非阻塞 UDP 通信
3. 客户端通信 API（java.net.URL, java.net.URLConnection 等类库）

涉及网络通信的 API 都在 java.net 和 java.nio.channels 包中。这里的网络已经将 RMI 相关包 java.rmi, javax.rmi 都排除了。

**安全（security, cryptography and AAA）**

1. Java 加密类库 JCA
2. Java 加密类库扩展 JCE
3. 涉及密码学知识点的消息摘要、消息认证码、对称加密、非对称加密、数字签名
4. 涉及网络通信证书管理工具（keytool）及 API（PKI、X.509证书）
5. 基于 SSL/TLS 的安全网络通信 API（JSSE），包括：密钥库管理、信任库管理、阻塞 SSL 通信和非阻塞 SSL 通信等等
6. Java 认证及授权服务（JAAS）API

涉及安全的东西都在：

- java.security（JCA、JCE、数字证书，以及 JCE 的 SPI）
- javax.net（SSL/TLS）
- javax.security（JAAS）
- javax.crypto（密码学）
- keytool 的 JDK 工具 


# 环境配置
> [Linux搭建Java开发环境](/Linux/JavaDevInit.md)
