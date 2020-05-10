---
title: Java ClassLoad Confuse
date: 2020-04-29 01:06:35
tags: 
categories: 
---

**目录 start**

1. [类加载导致的迷惑](#类加载导致的迷惑)
    1. [主题](#主题)
    1. [解决方案](#解决方案)
    1. [场景](#场景)

**目录 end**|_2020-04-29 11:57_|
****************************************

# 类加载导致的迷惑
> 记录一次因Jar包冲突导致的类加载问题 

> [参考: 为什么SpringBoot的 jar 可以直接运行？](https://blog.csdn.net/b644ROfP20z37485O35M/article/details/105671696)  
> [参考: 重新看待Jar包冲突问题及解决方案](https://www.jianshu.com/p/100439269148)  
> [参考: jar包冲突与inode](https://www.bbsmax.com/A/gVdnYM985W/)  

> [Maven: Introduction to the Dependency Mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)  

## 主题
1. Java 类加载
1. Linux inode
1. Jenkins Maven package

## 解决方案
1. 借助 Maven Helper 插件尽量避免Maven中依赖的冲突 maven-enforcer-plugin 插件 配合extra-enforcer-rules工具
1. 或者 使用脚本等工具分析出 不同jar包里 限定名一致的类

## 场景
1. SpringBoot项目 本身已经依赖了servlet3.1 因二方依赖被动引入了 servlet 2.5 版本
1. 上线途中项目启动失败，抛出 NoSuchMethodError 可知加载了低版本的 servlet
1. 经过分析可知依赖冲突导致，但是测试在未经排除依赖冲突时又做了重新上线，项目竟正常启动，因此分析底层原因

> 项目依赖 `mvn dependency:tree -Dverbose -Dincludes=javax.servlet:`
```log
[INFO] --- maven-dependency-plugin:3.0.2:tree (default-cli) @ project---
[INFO] Verbose not supported since maven-dependency-plugin 3.0
[INFO] com.project:war:1.0.0-SNAPSHOT
[INFO] +- com.xuxueli:xxl-job-core:jar:1.9.0:compile
[INFO] |  \- javax.servlet:javax.servlet-api:jar:3.1.0:compile
[INFO] \- com.xxx2:jar:2.1.3-RELEASE:compile
[INFO]    \- com.xxx3:xx-api:jar:1.3:compile
[INFO]       \- javax.servlet:servlet-api:jar:2.5:compile
```
