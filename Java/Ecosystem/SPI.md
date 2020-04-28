---
title: SPI
date: 2019-05-19 16:53:19
tags: 
categories: 
    - Java
---

**目录 start**

1. [Java中的SPI](#java中的spi)
    1. [项目中的实现](#项目中的实现)
        1. [JDBC](#jdbc)
        1. [Lombok](#lombok)
        1. [SLF4J](#slf4j)
        1. [Dubbo](#dubbo)
        1. [Jigsaw](#jigsaw)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Java中的SPI
> Service Provider Interface

> [Offcial Tutorials](https://docs.oracle.com/javase/tutorial/ext/basics/spi.html)  
> [参考: Java SPI思想梳理](https://zhuanlan.zhihu.com/p/28909673)  
> [参考: SPI 概述](https://zhoukaibo.com/2019/03/16/java-spi/)  


Java spi的具体约定如下：   
当服务的提供者，提供了服务接口的一种实现之后，在jar包的META-INF/services/目录里同时创建一个以服务接口命名的文件。  
该文件里就是实现该服务接口的具体实现类。而当外部程序装配这个模块的时候，就能通过该jar包META-INF/services/里的配置文件找到具体的实现类名  
并装载实例化，完成模块的注入, 基于这样一个约定就能很好的找到服务接口的实现类，而不需要再代码里制定。  

jdk提供服务实现查找的一个工具类：java.util.ServiceLoader

## 项目中的实现
> [参考: Slf4j框架理解与分析 ](https://blog.mythsman.com/2018/02/04/1/)  

### JDBC
我们在入门的时候都学过用jdbc包，用的时候我们都被要求写这行代码, 加载驱动类 `Class.forName("com.mysql.cj.jdbc.Driver");`  
其实这段代码没有任何实际意义，只是显式的加载了一个类，告诉我们记得添加这个jar包，实际上只要将这个jar包放在了类路径里面，这段话其实就没有必要了。  

我们去查 mysql-connector-java 这个包就会发现，他用的就是spi的方法，将自己的 com.mysql.cj.jdbc.Driver 这个类注册给了 java.sql.Driver 这个接口。加载的时候用的其实也是 ServiceLoader 。

### Lombok
lombok的原理也是类似，他用自己写的 AnnotationProcessor 去实现 javax.annotation.processing.Processor ，从而做到在编译期进行注解处理。

### SLF4J

### Dubbo
> [参考: SPI Loading](http://dubbo.apache.org/zh-cn/docs/dev/SPI.html)  

### Jigsaw
Java9推出的模块化系统 JPMS Java Platform Module System

通过改进的SPI机制来实现模块的依赖注入
