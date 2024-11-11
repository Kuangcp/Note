---
title: SPI
date: 2019-05-19 16:53:19
tags: 
categories: 
    - Java
---

💠

- 1. [Java中的SPI](#java中的spi)
- 2. [实践项目](#实践项目)
    - 2.1. [JDBC](#jdbc)
    - 2.2. [Lombok](#lombok)
    - 2.3. [SLF4J](#slf4j)
    - 2.4. [Dubbo](#dubbo)
    - 2.5. [Jigsaw](#jigsaw)

💠 2024-11-11 13:59:04
****************************************
# Java中的SPI
> Service Provider Interface

> [Offcial Tutorials](https://docs.oracle.com/javase/tutorial/ext/basics/spi.html)  
> [参考: Java SPI思想梳理](https://zhuanlan.zhihu.com/p/28909673)  
> [参考: SPI 概述](https://zhoukaibo.com/2019/03/16/java-spi/)  

Java spi的具体约定如下：

当服务的提供者，提供了服务接口的一种实现之后，在jar包的`META-INF/services/`目录里同时创建一个**以服务接口命名**的文件。  
该文件的内容是实现该服务接口的具体实现类（一行一个类）。而当外部程序装配这个模块的时候，就能通过模块内`META-INF/services/`的配置文件找到具体的实现类名  
并装载实例化，完成模块的注入, 基于这样一个约定就能很好的找到服务接口的实现类，而不需要再代码里显式指定，完成解耦。  

JDK提供服务查找的工具类：java.util.ServiceLoader

# 实践项目
例如一个对加密算法封装的工具类，为支持的加密算法写了代理类，然后引入支持的加密算法依赖，但是配置为 `<optional>true</optional>`  
然后配置 SPI文件 为所有支持的算法库，应用使用该工具类时，可按需加载实际选择的算法库。

> 例如：[表达式引擎封装-ExpressionUtil | Hutool](https://doc.hutool.cn/pages/ExpressionUtil/#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%BC%95%E6%93%8E%E6%89%A7%E8%A1%8C)  

## JDBC
我们在入门的时候都学过用jdbc包，用的时候我们都被要求写这行代码, 加载驱动类 `Class.forName("com.mysql.cj.jdbc.Driver");`  
但是从JDBC4.0后，就不用显式加载了，因为 DriverManager 自动加载了该驱动类，有个特例：Tomcat的原生Servlet模式（打破了委派机制）需要手动加载驱动类。

我们去查 mysql-connector-java 这个包就会发现，SPI定义 将 com.mysql.cj.jdbc.Driver 这个类注册给了 java.sql.Driver 这个接口。加载的时候用的其实也是 ServiceLoader 。

## Lombok
lombok的原理也是类似，他用自己写的 AnnotationProcessor 去实现 javax.annotation.processing.Processor ，从而做到在编译期进行注解处理。

## SLF4J
> [参考: Slf4j框架理解与分析 ](https://blog.mythsman.com/2018/02/04/1/)  

## Dubbo
> [参考: SPI Loading](http://dubbo.apache.org/zh-cn/docs/dev/SPI.html)  

## Jigsaw
Java9推出的模块化系统 JPMS Java Platform Module System

通过改进的SPI机制来实现模块的依赖注入
