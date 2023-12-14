---
title: Java中的Debug
date: 2019-07-21 18:08:40
tags: 
categories: 
    - Java
---

💠

- 1. [Debug](#debug)
    - 1.1. [技巧](#技巧)
    - 1.2. [方案](#方案)
        - 1.2.1. [应用方法CPU耗时或线程异常](#应用方法cpu耗时或线程异常)
    - 1.3. [远程调试](#远程调试)

💠 2023-12-14 14:36:07
****************************************
# Debug

> [参考: 深入 Java 调试体系](https://www.ibm.com/developerworks/cn/views/java/libraryview.jsp?search_by=%E6%B7%B1%E5%85%A5%20Java%20%E8%B0%83%E8%AF%95%E4%BD%93%E7%B3%BB)  

1. [jdb](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/jdb.html)

> [参考: IDEA 的 debug 怎么实现？](https://club.perfma.com/article/2405747)  

## 技巧
1. 需要尝试不停机去修改代码去寻找问题踪迹
    - 可通过Arthas动态替换class
1. 业务代码复杂，寻找资源泄漏点难以找到业务上的触发点
    - 可在创建资源的最底层入口实例化一个异常，但是不抛出，仅打印日志，观察每次资源被创建时的调用栈，辅助分析出是哪个业务入口导致


## 方案
### 应用方法CPU耗时或线程异常
表现：  应用启动慢，业务方法运行慢等等   

思路： 

1. jstack 分析方法 在业务进入前，执行中，执行完毕后 等若干个节点上的线程差别，找出可能异常的线程和方法栈
1. profile 查看CPU火焰图，找出耗时高的栈
1. arthas 的 monitor 指令进行分析方法栈耗时监控，找出异常方法

> 项目启动慢

1. 场景： Linux系统 hostname 没有配置到 /etc/hosts 文件中， 启动过程中频繁jstack能看出某线程被 getLocalHost 方法所阻塞
    - 方案： hostname配置到 /etc/hosts

## 远程调试

