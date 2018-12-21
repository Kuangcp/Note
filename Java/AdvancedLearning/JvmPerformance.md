---
title: Jvm 性能调优
date: 2018-11-21 10:56:52
tags: 
    - JDK
    - JVM
categories: 
    - Java
---

**目录 start**
 
1. [Java的性能调优](#java的性能调优)
    1. [JVM参数配置](#jvm参数配置)
    1. [内存优化](#内存优化)
        1. [堆外内存](#堆外内存)
1. [主要指标分析](#主要指标分析)
    1. [JDK自带工具](#jdk自带工具)
        1. [jps](#jps)
        1. [jstat](#jstat)
        1. [jinfo](#jinfo)
        1. [jmap](#jmap)
        1. [jstack](#jstack)
    1. [开源项目](#开源项目)
    1. [图形化](#图形化)
        1. [jvisualvm](#jvisualvm)
        1. [MAT](#mat)
        1. [IBM Heap Analyzer](#ibm-heap-analyzer)

**目录 end**|_2018-12-14 20:38_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************

# Java的性能调优
> 调优, 分析

## JVM参数配置

*********************

## 内存优化

- [Blog:java优化占用内存的方法(一)](http://blog.csdn.net/zheng0518/article/details/48182437)

- [GC 性能优化 专栏](https://blog.csdn.net/column/details/14851.html)
- [Java调优经验谈](http://www.importnew.com/22336.html)
- [你能不能谈谈，java GC是在什么时候，对什么东西，做了什么事情？” ](http://itindex.net/detail/54188-java-gc-%E4%B8%9C%E8%A5%BF)

### 堆外内存

堆外内存堆外内存主要是JNI、Deflater/Inflater、DirectByteBuffer（nio中会用到）使用的。

- [how to see memory useage of nio buffers](https://stackoverflow.com/questions/2689914/how-to-see-the-memory-usage-of-nio-buffers)

*********************
# 主要指标分析
## JDK自带工具
> 都是jdk的bin目录下的工具

### jps
> 主要用来输出JVM中运行的进程状态信息
- option:
    - -q 忽略输出的类名、Jar名以及传递给main方法的参数，只输出pid。
    - -m 输出传递给main方法的参数，如果是内嵌的JVM则输出为null。
    - -l 输出应用程序主类的完整包名，或者是应用程序JAR文件的完整路径。
    - -v 输出传给JVM的参数。
    - -V 输出通过标记的文件传递给JVM的参数（.hotspotrc文件，或者是通过参数-XX:Flags=指定的文件）

### jstat
- option:
    - -gcutil 统计heap的gc情况
    - -t 在第一列输出时间戳。该时间戳从jvm启动开始
    - -h3 每隔N行输出一次列表头
    - $PID 进程号
    - interval 输出间隔时间，单位毫秒
    - count 输出次数

- Demo:
    - jstat -gcutil -t -h5 7919 1000 50

### jinfo 
> 观察运行中的java程序的运行环境参数：参数包括Java System属性和JVM命令行参数
- Demo:
    - jinfo 14352
    - jinfo -sysprops 14352
    - jinfo -flags 14352
    - jinfo -flag MaxPermSize 14352

### jmap 
> 用来查看堆内存使用状况
- Demo:
    - jmap -histo $PID 展示class的内存情况
    - jmap -heap $PID 展示Java堆详细信息
    - jmap -dump:live,format=b,file=heapLive.hprof 2576

### jstack 
> jstack [option] pid  主要用来查看某个Java进程内的线程堆栈信息
- Option:
    - -F: 强制产生一个线程dump
    - -m: 打印java和native frames
    - -l: 打印关于锁的附加信息
- Demo:
    - jstack -F $PID

********************

## 开源项目

> [arthas](https://github.com/alibaba/arthas)
> [vjtools](https://github.com/vipshop/vjtools)

************************

## 图形化
### jvisualvm
> [参考博客: java内存泄漏的定位与分析](https://blog.csdn.net/lc0817/article/details/67014499)

> Local

> [使用 VisualVM 进行性能分析及调优](https://www.ibm.com/developerworks/cn/java/j-lo-visualvm/index.html)
> [参考博客: JVisualVM简介与内存泄漏实战分析](http://www.cnblogs.com/belen/p/5573501.html)

********************

> Remote 
-  通常使用两种方式连接远程JVM: JMX jstatd

> [参考博客: JVisualVM远程监控](https://blog.csdn.net/ericzx2008/article/details/23097403)

**`jmx`**

**`jstatd`**

1. vim jstatd.all.policy 
    ```
    grant codebase "file:${java.home}/../lib/tools.jar" {
       permission java.security.AllPermission;

    };
    ```
1. jstatd -J-Djava.security.policy=jstatd.all.policy  -p 12028 -J-Djava.rmi.server.logCalls=true
1. open jvisualvm create a remote with jstatd by above port 12028

**************

### MAT
> Memory Analyzer tool(MAT) | [Official Site](http://www.eclipse.org/mat/)

> [参考博客: JAVA Shallow heap & Retained heap](http://www.cnblogs.com/lipeineng/p/5824799.html)

> [ Official Doc: OQL Syntax](https://help.eclipse.org/neon/index.jsp?topic=%2Forg.eclipse.mat.ui.help%2Freference%2Foqlsyntax.html)

他的 OQL 比较方便, 像写 SQL 一样去查询对象

### IBM Heap Analyzer
> [Official Site](https://www.ibm.com/developerworks/community/alphaworks/tech/heapanalyzer)

**************

