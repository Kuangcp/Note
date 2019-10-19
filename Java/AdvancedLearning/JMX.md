---
title: JMX
date: 2018-11-21 10:56:52
tags: 
categories: 
    - Java
---

**目录 start**
 
1. [JMX](#jmx)
    1. [概念](#概念)
    1. [使用](#使用)
        1. [JVM参数](#jvm参数)

**目录 end**|_2019-10-19 17:04_|
****************************************

# JMX
> Java Management Extensions, 提供了一个可以动态修改资源的机制

> [Official Doc](https://www.oracle.com/technetwork/java/javase/tech/javamanagement-140525.html) | [wiki](https://en.wikipedia.org/wiki/Java_Management_Extensions) | [wici zh](https://zh.wikipedia.org/zh-hans/JMX)

> [参考博客: JMX学习笔记](https://www.jianshu.com/p/414647c1179e)
> [参考博客: java常见命令及Java Dump介绍](http://www.cnblogs.com/kongzhongqijing/articles/5534624.html)

> [What is JMX? 10 mins Quick Start JMX Tutorial](https://www.journaldev.com/1352/what-is-jmx-mbean-jconsole-tutorial)

## 概念

| 名称 | 含义 |
|:----|:----|
| MBean | 全称为Managed Bean, 你可以实现一个MBean来JMX提供管理内容 |
| MBean Server(也叫JMX Agent) | 提供集中注册管理MBean功能，允许远程通过他代理操作MBean |
| JMX Connectors | 通过实现不同的通讯协议，来允许远程访问 | 

简而言之　MBean就是存放了一堆属性的对象, 通过JMX技术, 可以远程动态修改这些MBean的状态

## 使用

### JVM参数

| 参数 | 类型 | 描述 |
|:---|:---|:---|
| -Dcom.sun.management.jmxremote | 布尔 | 是否支持远程JMX访问，默认true |
| -Dcom.sun.management.jmxremote.port | 数值 | 监听端口号，方便远程访问 |
| -Dcom.sun.management.jmxremote.authenticate | 布尔 |  是否需要开启用户认证,默认开启
| -Dcom.sun.management.jmxremote.ssl | 布尔| 是否对连接开启SSL加密，默认开启
| -Dcom.sun.management.jmxremote.access.file | 路径 | 对访问用户的权限授权的文件的路径，默认路径 `JRE_HOME/lib/management/jmxremote.access`
| -Dcom.sun.management.jmxremote. password.file | 路径 | 设置访问用户的用户名和密码，默认路径 `JRE_HOME/lib/management/jmxremote.password`
