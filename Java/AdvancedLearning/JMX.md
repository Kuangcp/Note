---
title: JMX
date: 2018-11-21 10:56:52
tags: 
categories: 
    - Java
---

💠

- 1. [JMX](#jmx)
    - 1.1. [概念](#概念)
    - 1.2. [使用](#使用)
        - 1.2.1. [远程JMX](#远程jmx)
        - 1.2.2. [工具](#工具)
- 2. [MXBean](#mxbean)
    - 2.1. [GarbageCollectorMXBean](#garbagecollectormxbean)
    - 2.2. [自定义MXBean](#自定义mxbean)

💠 2024-10-08 15:07:46
****************************************

# JMX
> Java Management Extensions, 提供了一个可以动态修改资源的机制

> [Official Doc](https://www.oracle.com/technetwork/java/javase/tech/javamanagement-140525.html) | [wiki](https://en.wikipedia.org/wiki/Java_Management_Extensions) | [wici zh](https://zh.wikipedia.org/zh-hans/JMX)

> [参考: JMX学习笔记](https://www.jianshu.com/p/414647c1179e)
> [参考: java常见命令及Java Dump介绍](http://www.cnblogs.com/kongzhongqijing/articles/5534624.html)

> [What is JMX? 10 mins Quick Start JMX Tutorial](https://www.journaldev.com/1352/what-is-jmx-mbean-jconsole-tutorial)

## 概念

| 名称 | 含义 |
|:----|:----|
| MBean | 全称为Managed Bean, 你可以实现一个MBean来JMX提供管理内容 |
| MBean Server(也叫JMX Agent) | 提供集中注册管理MBean功能，允许远程通过他代理操作MBean |
| JMX Connectors | 通过实现不同的通讯协议，来允许远程访问 | 

简而言之　MBean就是存放了一堆属性的对象, 通过JMX技术, 可以远程动态修改这些MBean的状态

## 使用
> [JMXTerm](https://www.baeldung.com/java-jmxterm-external-debugging)

### 远程JMX
JVM启动时追加参数启用，也可以对已存在的JVM进程启用 `jcmd $pid ManagementAgent.start [options]` [jcmd help](https://docs.oracle.com/en/java/javase/17/docs/specs/man/jcmd.html) 

| 参数 | 类型 | 描述 |
|:---|:---|:---|
| -Dcom.sun.management.jmxremote | 布尔 | 是否支持远程JMX访问，默认true |
| -Dcom.sun.management.jmxremote.port | 数值 | 监听端口号，方便远程访问 |
| -Dcom.sun.management.jmxremote.authenticate | 布尔 |  是否需要开启用户认证,默认开启
| -Dcom.sun.management.jmxremote.ssl | 布尔 | 是否对连接开启SSL加密，默认开启
| -Dcom.sun.management.jmxremote.access.file | 路径 | 对访问用户的权限授权的文件的路径，默认路径 `JRE_HOME/lib/management/jmxremote.access`
| -Dcom.sun.management.jmxremote.password.file | 路径 | 设置访问用户的用户名和密码，默认路径 `JRE_HOME/lib/management/jmxremote.password`

```ini
    -Dcom.sun.management.jmxremote.port=4433
    -Djava.rmi.server.hostname=192.168.9.155
    -Dcom.sun.management.jmxremote.ssl=false

    # 1. 不配置账户
    -Dcom.sun.management.jmxremote.authenticate=false

    # 2. 配置账户
    -Dcom.sun.management.jmxremote.authenticate=true
    -Dcom.sun.management.jmxremote.password.file=jmxremote.password
    -Dcom.sun.management.jmxremote.access.file=jmxremote.access
```

> jmxremote.password
```
username1 pwd1
username2 pwd2
```
> jmxremote.access
```
username1 readonly
username2 readwrite
```

### 工具
[Prometheus JMX Exporter](https://github.com/prometheus/jmx_exporter)

************************

# MXBean 
通过查看 `java.lang.management.PlatformManagedObject` 的子类可以快速预览所有的MXBean

- OperatingSystemMXBean 操作系统信息 获取最大和free内存，但是无法获取available内存，简单做法是直接读取 `/proc/meminfo`

## GarbageCollectorMXBean
> [Garbage Collection JMX Notifications](http://www.fasterj.com/articles/gcnotifs.shtml)

通过监听 GarbageCollectorMXBean，应用可感知JVM GC动作。

## 自定义MXBean
> [集成JMX](https://www.liaoxuefeng.com/wiki/1252599548343744/1282385687609378)

