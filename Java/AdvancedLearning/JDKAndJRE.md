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
        1. [java](#java)
            1. [环境变量的使用](#环境变量的使用)
    1. [Oracle JRE](#oracle-jre)
1. [OpenJDK](#openjdk)

**目录 end**|_2019-04-19 15:38_|
****************************************
# JDK And JRE
> LTS: 8 11

但是11发布后, Oracle修改了使用协议, JDK商用需付费, 仅个人开发演示免费 [License](https://www.oracle.com/technetwork/java/javase/terms/license/javase-license.html)

# Oracle
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

- bin目录下常用工具: 
    - java javac javap jar 
    - jconsole jmap jmc jps jstack jstat jstatd jvisualvm

>  [Useage: Java 性能分析](/Java/AdvancedLearning/JavaPerformance.md)

### java

#### 环境变量的使用
> java [-options] -jar jarfile [args...]

> [What is the java -D command-line option good for? ](https://coderanch.com/t/178539/certification/java-command-line-option-good)

- 传入 `java -Dkey=true -jar xxx.jar` -D 参数先于 -jar
- 获取 `System.getProperty("key", "defaultvalue");`

*******************
## Oracle JRE
> Java11 开始, 已去掉了JRE

> 以下是Java8的结构
```
    ├── bin/
    ├── COPYRIGHT
    ├── lib/
    ├── LICENSE
    ├── plugin/
    ├── README
    ├── THIRDPARTYLICENSEREADME-JAVAFX.txt
    ├── THIRDPARTYLICENSEREADME.txt
    └── Welcome.html
```

*********************************************************

# OpenJDK
> [Official Site](http://openjdk.java.net/) | [Open JDK下载地址](https://adoptopenjdk.net/nightly.html)

> [Open JDK 11: Download](http://jdk.java.net/11/)
