---
title: Jvm 性能调优
date: 2018-11-21 10:56:52
tags: 
    - JVM
categories: 
    - Java
---

**目录 start**

1. [Java的性能调优](#java的性能调优)
    1. [JVM参数调优](#jvm参数调优)
        1. [GC调优](#gc调优)
    1. [内存优化](#内存优化)
        1. [堆外内存](#堆外内存)
        1. [Metaspace](#metaspace)
1. [JDK自带工具](#jdk自带工具)
    1. [java](#java)
        1. [环境变量的使用](#环境变量的使用)
    1. [jps](#jps)
    1. [jstat](#jstat)
    1. [jinfo](#jinfo)
    1. [jmap](#jmap)
    1. [jhat](#jhat)
    1. [jstack](#jstack)
    1. [jcmd](#jcmd)
1. [终端类工具](#终端类工具)
    1. [Arthas](#arthas)
    1. [async-profiler](#async-profiler)
1. [图形化工具](#图形化工具)
    1. [JProfiler](#jprofiler)
    1. [GCViewer](#gcviewer)
    1. [jvisualvm](#jvisualvm)
    1. [MAT](#mat)
    1. [IBM Heap Analyzer](#ibm-heap-analyzer)

**目录 end**|_2021-05-18 21:48_|
****************************************

# Java的性能调优

## JVM参数调优
> [参考: JVM实用参数（一）JVM类型以及编译器模式](http://ifeve.com/useful-jvm-flags-part-1-jvm-types-and-compiler-modes-2/)

- [xxfox](http://xxfox.perfma.com/)`Jvm参数辅助工具`

> [参考: JVM动态反优化](https://blog.mythsman.com/post/5d2c12cc67f841464434a3ec/)   
> [General Java Troubleshooting ](https://docs.oracle.com/en/java/javase/11/troubleshoot/general-java-troubleshooting.html)  
> [目前最全的Java服务问题排查套路](https://juejin.cn/post/6844903816379236360)  

************************
> 工具

命令行终端
- 标准终端类：jps、jinfo、jstat、jstack、jmap
- 功能整合类：jcmd、vjtools、arthas、greys

可视化界面
- 简易：JConsole、JVisualvm、HA、GCHisto、GCViewer
- 进阶：MAT、JProfiler

命令行推荐 arthas ，可视化界面推荐 JProfiler，此外还有一些在线的平台 [gceasy](https://gceasy.io/)、heaphero、fastthread 。

************************
> IDEA调优
```conf
    -server
    -Xms600m  # 最小堆
    -Xmx600m  # 最大堆 配成一样是为了避免扩容
    -Xmn256m  # 新生代
    -XX:MetaspaceSize=350m # 只是一个阈值, 达到该阈值才进行 GC
    -XX:MaxMetaspaceSize=350m # 最大值

    -Xnoclassgc 
    -Xverify:none # 不进行字节码校验
    -XX:+AggressiveOpts # 激进式优化

    -XX:ReservedCodeCacheSize=320m # 编译时代码缓存 IDEA 警告不能低于240M
```

> [参考: Java’s -XX:+AggressiveOpts: Can it slow you down?](https://www.opsian.com/blog/aggressive-opts/)  
> [参考: JVM参数MetaspaceSize的误解 ](https://mp.weixin.qq.com/s/jqfppqqd98DfAJHZhFbmxA?)

************************

### GC调优
> [Java GC](/Java/AdvancedLearning/JavaGC.md)

*********************

## 内存优化

- [Blog:java优化占用内存的方法(一)](http://blog.csdn.net/zheng0518/article/details/48182437)

- [GC 性能优化 专栏](https://blog.csdn.net/column/details/14851.html)
- [Java调优经验谈](http://www.importnew.com/22336.html)

- [Memory Footprint of A Java Process](https://zhuanlan.zhihu.com/p/158712025)

### 堆外内存

堆外内存堆外内存主要是JNI、Deflater/Inflater、DirectByteBuffer（nio中会用到）使用的。

- [Github: 测试代码](https://github.com/Kuangcp/JavaBase/blob/master/class/src/test/java/jvm/oom/DirectMemoryOOMTest.java)
- [how to see memory useage of nio buffers](https://stackoverflow.com/questions/2689914/how-to-see-the-memory-usage-of-nio-buffers)

> [参考: 聊聊JVM 堆外内存泄露的BUG是如何查找的](https://cloud.tencent.com/developer/article/1129904)  
> [JAVA堆外内存排查小结](https://zhuanlan.zhihu.com/p/60976273)  

### Metaspace
> [参考: Metaspace 之一：Metaspace整体介绍](https://www.cnblogs.com/duanxz/p/3520829.html)  

************************

# JDK自带工具
> 都是jdk的bin目录下的工具

## java
### 环境变量的使用
> java [-options] -jar jarfile [args...]

> [What is the java -D command-line option good for? ](https://coderanch.com/t/178539/certification/java-command-line-option-good)
- 传入 `java -Dkey=true -jar xxx.jar`
    - *-D 参数* 要前于 -jar
- 获取 `System.getProperty("key", "defaultvalue");`

> 执行含main方法的类
- `java -cp jarfile[:jarfile2] className`

## jps
> 主要用来输出JVM中运行的进程状态信息
- option:
    - -q 忽略输出的类名、Jar名以及传递给main方法的参数，只输出pid。
    - -m 输出传递给main方法的参数，如果是内嵌的JVM则输出为null。
    - -l 输出应用程序主类的完整包名，或者是应用程序JAR文件的完整路径。
    - -v 输出传给JVM的参数。
    - -V 输出通过标记的文件传递给JVM的参数（.hotspotrc文件，或者是通过参数-XX:Flags=指定的文件）

## jstat
> [Oracle Doc](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstat.html)

- option:
    - -gcutil 统计heap的gc情况
    - -t 在第一列输出时间戳。该时间戳从jvm启动开始
    - -h3 每隔N行输出一次列表头
    - $PID 进程号
    - interval 输出间隔时间，单位毫秒
    - count 输出次数

- Demo:
    - `jstat -gcutil -t -h5 7919 1000 50`

## jinfo 
> 观察运行中的 java 进程的运行环境参数：参数包括 Java System 属性和 JVM 命令行参数
- Demo:
    - jinfo 14352
    - jinfo -sysprops 14352
    - jinfo -flags 14352
    - jinfo -flag MaxPermSize 14352

## jmap 
> 用来查看堆内存使用状况
- Demo:
    - `jmap -histo $PID` 展示实例和占用内存情况
    - `jmap -heap $PID` 展示Java堆详细信息
    - `jmap -dump:live,format=b,file=heapLive.hprof $PID` dump堆

## jhat
>  Java Head Analyse Tool

用于分析 jmap 转储出来的堆文件, 分析完后启动一个WebServer 通过浏览器查看

## jstack 
> jstack [option] pid  主要用来查看某个Java进程内的线程堆栈信息
- Option:
    - -F: 强制产生一个线程dump
    - -m: 打印java和native frames
    - -l: 打印关于锁的附加信息

> 找出占用CPU最高的线程:
1. `jps 或者 ps aux | grep xxx` 得到对应Java进程id
1. `top -Hp 进程id` 查看 time 占用最长 或者 CPU占用最高 的线程id
1. `printf %x 线程id` 得到 16进制线程id
1. `jstack 进程id | grep -A 20 16进制线程id` 查看该线程的栈,进而分析到代码

## jcmd

********************

# 终端类工具

## Arthas
> [Github: Arthas](https://github.com/alibaba/arthas)`阿里巴巴`

## async-profiler
> [async-profiler](https://github.com/jvm-profiling-tools/async-profiler)

**********************

> [vjtools](https://github.com/vipshop/vjtools)`唯品会`

************************

# 图形化工具
## JProfiler
> [Official Site](https://www.ej-technologies.com/products/jprofiler/overview.html)  

## GCViewer
> [Github: GCViewer](https://github.com/chewiebug/GCViewer)

## jvisualvm
> [Github:visualvm](https://github.com/oracle/visualvm)  
> [visualgc plugin](https://www.oracle.com/technetwork/java/visualgc-136680.html)  

> [参考: java内存泄漏的定位与分析](https://blog.csdn.net/lc0817/article/details/67014499)
> [使用 VisualVM 进行性能分析及调优](https://www.ibm.com/developerworks/cn/java/j-lo-visualvm/index.html)  
> [参考: JVisualVM简介与内存泄漏实战分析](http://www.cnblogs.com/belen/p/5573501.html)

- `Local`
- `Remote`
    -  通常使用两种方式连接远程JVM: JMX jstatd
    
    - **`jmx`**
        - [JMX](/Java/AdvancedLearning/JMX.md)

    - **`jstatd`**
        1. vim jstatd.all.policy 
            ```
                grant codebase "file:${java.home}/../lib/tools.jar" {
                    permission java.security.AllPermission;

                };
            ```
        1. jstatd -J-Djava.security.policy=jstatd.all.policy  -p 12028 -J-Djava.rmi.server.logCalls=true
        1. open jvisualvm create a remote with jstatd by above port 12028

> 应用开发时的使用
1. 可以使用 Profiler 下的JDBC，操作业务流程，获取所有执行的SQL，用来优化索引，或者排查问题

## MAT
> Memory Analyzer tool(MAT) | [Official Site](http://www.eclipse.org/mat/)

> [参考: JAVA Shallow heap & Retained heap](http://www.cnblogs.com/lipeineng/p/5824799.html)  
> [参考:  利用MAT分析JVM内存问题，从入门到精通](https://www.cnblogs.com/javaadu/p/11161380.html)  
> [ Official Doc: OQL Syntax](https://help.eclipse.org/neon/index.jsp?topic=%2Forg.eclipse.mat.ui.help%2Freference%2Foqlsyntax.html)  

他的 OQL 比较方便, 像写 SQL 一样去查询对象

注意: 有这样的一种场景, 从数据库获取大量的数据创建为对象, 导致瞬间的OOM 这时候即使使用 jmap 去 dump 了快照, 也看不到占用大量内存的对象, 很有可能这些对象就是gc不可达的, 而mat只能分析可达对象

## IBM Heap Analyzer
> [Official Site](https://www.ibm.com/developerworks/community/alphaworks/tech/heapanalyzer)

