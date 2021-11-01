---
title: Java中的Debug
date: 2019-07-21 18:08:40
tags: 
categories: 
    - Java
---

**目录 start**

1. [Debug](#debug)
    1. [远程调试](#远程调试)

**目录 end**|_2021-05-17 00:15_|
****************************************
# Debug

> [参考: 深入 Java 调试体系](https://www.ibm.com/developerworks/cn/views/java/libraryview.jsp?search_by=%E6%B7%B1%E5%85%A5%20Java%20%E8%B0%83%E8%AF%95%E4%BD%93%E7%B3%BB)  

1. [jdb](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/jdb.html)

> [参考: IDEA 的 debug 怎么实现？](https://club.perfma.com/article/2405747)  

## 方案
### 应用方法CPU耗时或线程异常
表现： 

应用启动慢，业务方法运行慢等等

思路： 

1. jstack 分析方法 在业务进入前，执行中，执行完毕后 等若干个节点上的线程差别，找出可能异常的线程和方法栈
1. profile 查看CPU火焰图，找出耗时高的栈
1. arthas 的 monitor 指令进行分析方法栈耗时监控，找出异常方法

> 项目启动慢

1. 场景： Linux系统 hostname 没有配置到 /etc/hosts 文件中， 启动过程中频繁jstack能看出某线程被 getLocalHost 方法所阻塞
    - 方案： hostname配置到 /etc/hosts

## 远程调试

