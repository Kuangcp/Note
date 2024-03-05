---
title: Java11
date: 2018-11-21 10:56:52
tags: 
categories: 
    - Java
---

**目录 start**

1. [Java11](#java11)
    1. [安装配置](#安装配置)
        1. [Linux](#linux)
    1. [新特性](#新特性)
        1. [ZGC](#zgc)
        1. [部分API转为内部API](#部分api转为内部api)

**目录 end**|_2021-05-17 00:15_|
****************************************
# Java11 
> [Official: JDK 11 Documentation](https://docs.oracle.com/en/java/javase/11/) | [Official:api](https://docs.oracle.com/en/java/javase/11/docs/api/index.html)

> [Tool reference](https://docs.oracle.com/en/java/javase/11/tools/tools-and-command-reference.html)

应该就是真正意义上的 Java9 了, 原先发布的 9 和 10 都不是 LTS, 并且很多原先属于9的特性也是推迟到了这个版本

## 安装配置
> [Official site](https://www.oracle.com/technetwork/java/javase/downloads/index.html)

> [ZGC](https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html#JDK-8197831)

通过 JVM 参数启用 ZGC
```
-XX:+UnlockExperimentalVMOptions
-XX:+UseZGC
```

### Linux
```sh
JAVA_HOME=/path/to/java11
export CLASSPATH=.:${JAVA_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
```

## 新特性
> [Official: migrate guide](https://docs.oracle.com/en/java/javase/11/migrate/index.html)  
> [JDK 11 Release Notes](https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html#JDK-8197831)

### ZGC
> [ZGC](/Java/AdvancedLearning/JvmGC.md#ZGC)  

*******************************
> [参考: Java 11 Tutorial](https://winterbe.com/posts/2018/09/24/java-11-tutorial/)

> [参考: Java 11 正式发布，带来ZGC、Http Client等重要特性！ ](https://mp.weixin.qq.com/s/CA_snRZ0kw9i-p1YCnHRKA)

> [Java11](https://blog.csdn.net/weixin_38055381/article/details/82865385)


### 部分API转为内部API
> [Compile Your Application if Needed](https://docs.oracle.com/en/java/javase/11/migrate/index.html#JSMIG-GUID-77874D97-46F3-4DB5-85E4-2ACB5F8D760B)

例如 sun.misc.Unsafe , 如果应用有引用, 在 JDK11 中编译会报错 加 `--add-exports` 可避免报错
