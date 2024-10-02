---
title: Java的JDK以及JRE
date: 2018-11-21 10:56:52
tags: 
    - JVM
categories: 
    - Java
---

💠

- 1. [JDK And JRE](#jdk-and-jre)
- 2. [Oracle](#oracle)
    - 2.1. [Oracle JDK](#oracle-jdk)
    - 2.2. [Oracle JRE](#oracle-jre)
- 3. [OpenJDK](#openjdk)
- 4. [商业组织JDK](#商业组织jdk)
    - 4.1. [Corretto](#corretto)
- 5. [JDK源码](#jdk源码)

💠 2024-10-02 22:33:00
****************************************
# JDK And JRE

但是11发布后, Oracle修改了使用协议, JDK商用需付费, 仅个人开发演示免费 [License](https://www.oracle.com/technetwork/java/javase/terms/license/javase-license.html)

- [www.injdk.cn](https://www.injdk.cn/)`镜像站`

> [Java 有哪些不好的设计？](https://www.zhihu.com/question/25372706/answer/30589125)

# Oracle
> [roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)

## Oracle JDK

> 以下是Java8的结构
```
    ├── bin/
    ├── COPYRIGHT
    ├── include/
    ├── javafx-src.zip
    ├── jre/
    ├── lib/
    ├── LICENSE
    ├── man/
    ├── README.html
    ├── release
    ├── src.zip
    ├── THIRDPARTYLICENSEREADME-JAVAFX.txt
    └── THIRDPARTYLICENSEREADME.txt
```

> 以下是Java11的目录结构
```
    ├── bin
    ├── conf
    ├── include
    ├── jmods
    ├── legal
    ├── lib
    ├── README.html
    └── release
```

- bin目录下常用工具 [Useage: Java 性能分析](/Java/AdvancedLearning/JavaPerformance.md): 
    - java javac javap jar 
    - jconsole jmap jmc jps jstack jstat jstatd jvisualvm

************************

## Oracle JRE
> Java运行时环境

Java11 开始, JDK内去掉了JRE模块

************************

# OpenJDK
> [Official Site](http://openjdk.java.net/) |  [OpenJDK Source](http://hg.openjdk.java.net/jdk) | [Github:source](https://github.com/openjdk/jdk)

> [Open JDK 11: Download](http://jdk.java.net/11/)
> [Issues](https://bugs.openjdk.org/projects/JDK/issues)  

# 商业组织JDK
## Corretto
[aws corretto](https://aws.amazon.com/corretto/)


************************

- 阿里 Dragonwell
- 华为 毕昇 JDK
- 腾讯 Kona
- 美团 MJDK
    - [MJDK 如何实现压缩速率的 5 倍提升？](https://tech.meituan.com/2023/08/31/meituan-mjdk-mzlib.html)

# JDK源码
> [ 不瞒你说，我最近跟Java源码杠上了 ](https://mp.weixin.qq.com/s?__biz=MzU4ODI1MjA3NQ==&mid=2247485421&idx=1&sn=c4543020e3d347267dbd8491ee48d2d5&chksm=fdded129caa9583fefb160e091d741e40fa24da4f3f14aa46bd4fc9b0d77dee9b98583a6c68b&mpshare=1&scene=1&srcid=0411IUXF6tTOYRaj5I6ebZj8&sharer_sharetime=1586571385813&sharer_shareid=246c4b52c1cb45eaa580c985c95107f3#rd)  

