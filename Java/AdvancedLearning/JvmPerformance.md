---
title: Java性能调优
date: 2018-11-21 10:56:52
tags: 
    - JVM
categories: 
    - Java
---

💠

- 1. [Java性能调优](#java性能调优)
    - 1.1. [JVM参数调优](#jvm参数调优)
        - 1.1.1. [GC调优](#gc调优)
    - 1.2. [内存优化](#内存优化)
        - 1.2.1. [堆外内存](#堆外内存)
        - 1.2.2. [Metaspace](#metaspace)
- 2. [JDK自带工具](#jdk自带工具)
    - 2.1. [java](#java)
        - 2.1.1. [环境变量的使用](#环境变量的使用)
    - 2.2. [jps](#jps)
    - 2.3. [jstat](#jstat)
    - 2.4. [jinfo](#jinfo)
    - 2.5. [jmap](#jmap)
    - 2.6. [jhat](#jhat)
    - 2.7. [jstack](#jstack)
        - 2.7.1. [实现原理](#实现原理)
    - 2.8. [jcmd](#jcmd)
    - 2.9. [常见问题](#常见问题)
        - 2.9.1. [Unable to Open Socket File](#unable-to-open-socket-file)
- 3. [终端类工具](#终端类工具)
    - 3.1. [Arthas](#arthas)
    - 3.2. [async-profiler](#async-profiler)
- 4. [图形化工具](#图形化工具)
    - 4.1. [JProfiler](#jprofiler)
    - 4.2. [GCViewer](#gcviewer)
    - 4.3. [Visualvm](#visualvm)
    - 4.4. [MAT](#mat)
    - 4.5. [IntelliJ IDEA](#intellij-idea)
    - 4.6. [JMC](#jmc)
    - 4.7. [IBM Heap Analyzer](#ibm-heap-analyzer)
- 5. [Tuning](#tuning)
    - 5.1. [基本JVM参数](#基本jvm参数)
    - 5.2. [GC](#gc)
        - 5.2.1. [工具](#工具)
        - 5.2.2. [主要关注指标](#主要关注指标)
    - 5.3. [线程](#线程)
    - 5.4. [内存](#内存)

💠 2024-01-31 11:40:19
****************************************

# Java性能调优

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
    - -class 类加载情况
    - -compiler 编译统计
    - -printcompilation JVM编译方法统计
    - 查看内存相关指标
        - -gcutil 总gc统计情况
        - -gc gc统计情况
        - -gccapacity 堆内存空间
        - -gcnew 和 -gcnewcapacity 新生代gc和内存统计
        - -gcold 和 -gcoldcapacity 老年代gc和内存统计
        - -gcpermcapacity JDK7永久代 -gcmetacapacity JDK8+ 元空间
    - -t 在第一列输出时间戳。该时间戳从jvm启动开始
    - -h3 每隔N行输出一次列表头
    - $PID 进程号
    - interval 输出间隔时间，单位毫秒
    - count 输出次数

> [CSDN: jstat](https://blog.csdn.net/achuo/article/details/107793361)

> Demo:
- `jstat -gcutil -t -h5 7919 1000 50` 查看gc情况

## jinfo 
> 观察运行中的 java 进程的运行环境参数：参数包括 Java System 属性和 JVM 命令行参数
- Demo:
    - jinfo 14352
    - jinfo -sysprops 14352
    - 查看JVM参数 `jinfo -flags 14352`
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
- -J-mx16g 设置最大内存
- -J-d64 64位模式

## jstack 
> jstack [option] pid  主要用来查看某个Java进程内的线程堆栈信息
- Option:
    - -F: 强制产生一个线程dump 
        - `注意`此方式得到的dump**缺失很多信息**， 只有线程栈和操作系统线程id，没有线程名，线程cid，锁等信息
        - 而且相对于没有-F的方式，实现原理完全不一样，见下文链接
    - -m: 打印java和native frames
    - -l: 打印关于锁的附加信息
    - -J-d64: 64位模式

> 找出占用CPU最高的线程:
1. `jps 或者 ps aux | grep xxx` 得到对应Java进程id
1. `top -Hp 进程id` 查看 time 占用最长 或者 CPU占用最高 的线程id
1. `printf %x 线程id` 得到 16进制线程id
1. `jstack 进程id | grep -A 20 16进制线程id` 查看该线程的栈,进而分析到代码

> [How to Analyze Java Thread Dumps](https://www.baeldung.com/java-analyze-thread-dumps)
> [OpenJDK11 jstack output explanation](https://stackoverflow.com/questions/76476637/openjdk11-jstack-output-explanation)

### 实现原理
- [Jstack 源码分析](https://zhuanlan.zhihu.com/p/36224094)

[jmap -F and jstack -F](https://stackoverflow.com/questions/26140182/running-jmap-getting-unable-to-open-socket-file)`jmap和jstack 默认及加-F选项背后实现机制及优缺点`
- [Dynamic Attach Mechanism](http://openjdk.java.net/groups/hotspot/docs/Serviceability.html#battach)
- [HotSpot Serviceability Agent](http://openjdk.java.net/groups/hotspot/docs/Serviceability.html#bsa)

## jcmd

************************

## 常见问题
### Unable to Open Socket File
> [jmap Error “Unable to Open Socket File”](https://www.baeldung.com/linux/jmap-unable-to-open-socket-file-heap-dump)
- 不是同用户及用户组 uid和gid
- 目标JVM不健康
- 目标JVM使用了`-XX:+DisableAttachMechanism`JVM参数
- 执行工具的JVM和目标JVM不是同一个版本（最好保持一致，如果版本相差过大，内存布局设计不一样，就会无法正常解析结果）
- /tmp 目录下无法创建命令使用的临时文件，或是来不及使用就被`systemd-tmpfiles`清理了 `/tmp/.java_pidXXX`

查找JVMSocket泄漏
- [一次由于网络套接字文件描述符泄露导致线上服务事故原因的排查经历](https://www.wangbo.im/posts/a-production-bug-leaking-sockets-fd-reproducing-practice/)
- `strace -t -T -f -p pid -e trace=network,close -o strace.out`
    - 尝试找到创建socket并没有关闭socket的线程号， 然后进制转换后查看jstack找到线程持有栈关联到相关代码

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

## Visualvm
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

************************

## MAT
> Memory Analyzer tool(MAT) | [Official Site](http://www.eclipse.org/mat/) | [download](https://eclipse.dev/mat/downloads.php)

> [参考: JAVA Shallow heap & Retained heap](http://www.cnblogs.com/lipeineng/p/5824799.html)  
> [参考:  利用MAT分析JVM内存问题，从入门到精通](https://www.cnblogs.com/javaadu/p/11161380.html)  
> [ Official Doc: OQL Syntax](https://help.eclipse.org/neon/index.jsp?topic=%2Forg.eclipse.mat.ui.help%2Freference%2Foqlsyntax.html)  

他的 OQL 比较方便, 像写 SQL 一样去查询对象

注意: 有这样的一种场景, 从数据库获取大量的数据创建为对象, 导致瞬间的OOM 这时候即使使用 jmap 去 dump 了快照, 也看不到占用大量内存的对象, 因为MAT默认展示的是GC可达对象，需要在菜单选择看不可达对象

分析思路：
对象: histogram, Top ,
线程: 
类加载器： histogram -> basic -> merge classloader
不可达对象：

## IntelliJ IDEA
[Analyze the memory snapshot](https://www.jetbrains.com/help/idea/read-the-memory-snapshot.html)

************************
## JMC
> JDK Mission Control

通过对运行中的JVM进行飞行记录 Flight Recorder, 分析指定时间内代码的可优化点，指标值变化情况（内存，CPU，GC，类加载等等）

************************

## IBM Heap Analyzer
> [Official Site](https://www.ibm.com/developerworks/community/alphaworks/tech/heapanalyzer)

************************

# Tuning
排查思路：

- `Delta` 正式环境可复现问题，测试或灰度无法出现，且不能轻易重启正式环境，通过对生产的JVM做各类指标的记录，对比某个业务操作前后或故障前后的指标差异分析出问题的触发点
    - 限制：不能做太影响性能的指标记录和分析
- `Debug` 在测试或灰度环境上可复现问题，可直接Debug接入调试代码，或本地采用高耗能的方式debug分析`抓包，strace，CPU火焰图，等方式`
    - 限制：**可复现**，通常能有这个条件已经能直接通过debug代码就能解决问题了

## 基本JVM参数

## GC 
> [参考: 译：谁是 JDK8 中最快的 GC](https://club.perfma.com/article/233480)  
> [《沙盘模拟系列》JVM如何调优](https://my.oschina.net/u/4030990/blog/3149182)  
> [深入浅出GC问题排查](https://blog.ysboke.cn/archives/242.html)
> [参考: CMS Deprecated. Next Steps?](https://dzone.com/articles/cms-deprecated-next-steps)  

- [Oracle JDK8 GC调优指南](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/toc.html)
- [Oracle JDK11 GC调优指南](https://docs.oracle.com/en/java/javase/11/gctuning/introduction-garbage-collection-tuning.html)

### 工具
> [gceasy.io](https://gceasy.io)  
> [GCViewer](https://github.com/chewiebug/GCViewer)  

### 主要关注指标
> [garbage-collection-kpi](https://blog.gceasy.io/2016/10/01/garbage-collection-kpi/)`其中FootPrint定义应有误，JVM应指代内存占用而不是CPU资源`

- `延迟（Latency）`： 也可以理解为最大停顿时间，即垃圾收集过程中单次 STW 的最长时间，越短越好，一定程度上可以接受频次的增多，是 GC 技术的主要发展方向。
- `吞吐量（Throughput）`： 应用系统的生命周期内，由于 GC 线程会占用 Mutator 当前可用的 CPU 时钟周期，吞吐量即为 Mutator 有效花费的时间占系统总运行时间的百分比
    - 例如应用系统运行了 100 min，GC 累计耗时 1 min，则系统吞吐量为 99%。
    - 吞吐量优先的垃圾收集器会倾向于接受`单次耗时较长`的停顿，`累计停顿耗时短`的GC策略。
- `内存占用(Footprint)`：

> 以上三者不可兼得，通常兼顾两者舍弃一方。

## 线程
> [jstack.review Analyze java thread dumps](https://jstack.review)

## 内存
