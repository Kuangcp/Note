---
title: Java的JDK以及JRE
date: 2018-11-21 10:56:52
tags: 
    - JDK
categories: 
    - Java
---

**目录 start**
 
1. [JDK And JRE](#jdk-and-jre)
1. [Oracle](#oracle)
    1. [Oracle JDK](#oracle-jdk)
    1. [Oracle JRE](#oracle-jre)
1. [OpenJDK](#openjdk)

**目录 end**|_2020-02-23 22:33_|
****************************************
# JDK And JRE

但是11发布后, Oracle修改了使用协议, JDK商用需付费, 仅个人开发演示免费 [License](https://www.oracle.com/technetwork/java/javase/terms/license/javase-license.html)

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
