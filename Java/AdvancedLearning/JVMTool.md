---
title: JVM 监控&诊断工具
date: 2018-11-21 10:56:52
tags: 
    - JVM
categories: 
    - Java
---

💠

- 1. [JVM 监控&诊断](#jvm-监控&诊断)
    - 1.1. [JVM参数](#jvm参数)
    - 1.2. [JVM内存参数](#jvm内存参数)
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
    - 2.9. [jhsdb](#jhsdb)
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

💠 2024-03-04 19:04:38
****************************************

# JVM 监控&诊断
命令行终端
- 标准终端类：jps、jinfo、jstat、jstack、jmap
- 功能整合类：jcmd、vjtools、arthas、greys

可视化界面
- 简易：JConsole、JVisualvm、HA、GCHisto、GCViewer
- 进阶：MAT、JProfiler

命令行推荐 arthas ，可视化界面推荐 JProfiler  
此外还有一些在线的平台 [gceasy](https://gceasy.io/)、heaphero、fastthread 。

## JVM参数
> [JDK8 Java 参数概览](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/java.html)  
> [Java HotSpot VM Options](https://www.oracle.com/java/technologies/javase/vmoptions-jsp.html)

- [远程调试](/Java/AdvancedLearning/JavaDebug.md#远程调试)
- `-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9999 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false`
    - 开启无需认证 非SSL的JMX端口: 9999

- `-XX:+TraceClassUnloading -XX:+TraceClassLoading` 打印类装载
- `-Xloggc:/home/logs/gc.log`
- `-XX:+HeapDumpOnOutOfMemoryError` 注意路径的文件名不能重复

> 编译类参数
- CICompilerCount是JIT进行热点编译的线程数，和并发标记线程数一样，热点编译也是CPU密集型任务，默认值为2。
在CICompilerCountPerCPU开启的时候（JDK7默认关闭，JDK8默认开启），手动指定CICompilerCount是不会生效的，JVM会使用系统CPU核数进行计算。
所以当使用JRE8并且版本小于1.8.0_131，采用默认参数时，CICompilerCount会在20左右，对业务性能影响较大，特别是启动阶段。建议升级Java版本，特殊情况要使用老版本Java 8，请加上`-XX:CICompilerCount=[n]`, 同时不能指定-XX:+CICompilerCountPerCPU ，下表给出了生产环境下常见规格的推荐值。

| CPU核数 | 1 | 2 | 4 | 8 | 16 |
|:---|:---|:---|:---|:---|:---|
| 推荐值 | 2 | 2 | 3 | 3 | 8 | 

## JVM内存参数
> 堆(老年代 年轻代)，堆外，元空间，栈

- `-XX:CompressedClassSpaceSize=500m` 压缩类元空间大小 默认是1g
- `-XX:SurvivorRatio` 配置 Edgen 和 单个Survivor 的比例, 如果配置为2 则是 2:1:1

- `-XX:+PrintFlagsInitial` 输出初始默认值

> java -XX:+PrintFlagsFinal -version
- `输出JVM最终属性值` -XX:+PrintFlagsFinal 
    - MaxHeapSize 最大堆内存
    - MaxRAMFraction 默认最大内存占物理机内存的比例 JDK6，7，8 都是4 即1/4
    - `-Xmn` MaxNewSize 默认值是Xmx的1/3 即最大堆内存 MaxHeapSize 的1/3
    - NUMA 机制
    - `java -XX:+PrintFlagsFinal -version | grep "Use.*GC"` 查看默认GC实现

- [初始和最大堆内存设置为一样的好处](https://gceasy.ycrash.cn/gc-recommendations/benefits-of-setting-initial-and-maximum-memory-size.jsp)

> 快速确认进程内存配置  OpenJDK： ` `  OracleJDK ： `jmap -heap pid`

> [参考: JVM实用参数（一）JVM类型以及编译器模式](http://ifeve.com/useful-jvm-flags-part-1-jvm-types-and-compiler-modes-2/)  
> [xxfox](http://xxfox.perfma.com/)`Jvm参数辅助工具`  
> [参考: JVM动态反优化](https://blog.mythsman.com/post/5d2c12cc67f841464434a3ec/)   

************************

# JDK自带工具
> 都是jdk的bin目录下的工具

## java
> 使用方式：
- 执行类： `java [-options] class [args...]`
- 执行包： `java [-options] -jar jarfile [args...]` 或 `java -jar [-options] jarfile [args...]`

> 这些Java options都不会生效。
`java -jar jarfile [-options] [args...]`  
`java -jar jarfile [args...] [-options]`  

### 环境变量的使用
> [What is the java -D command-line option good for? ](https://coderanch.com/t/178539/certification/java-command-line-option-good)
- 传入 `java -Dkey=true -jar xxx.jar`
    - *-D 参数* 要前于 -jar
- 获取 `System.getProperty("key", "defaultvalue");`

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

> [How to Analyze Java Thread Dumps](https://www.baeldung.com/java-analyze-thread-dumps)`分析工具和思路`
> [OpenJDK11 jstack output explanation](https://stackoverflow.com/questions/76476637/openjdk11-jstack-output-explanation)

### 实现原理
- [Jstack 源码分析](https://zhuanlan.zhihu.com/p/36224094)

[jmap -F and jstack -F](https://stackoverflow.com/questions/26140182/running-jmap-getting-unable-to-open-socket-file)`jmap和jstack 默认及加-F选项背后实现机制及优缺点`
- [Dynamic Attach Mechanism](http://openjdk.java.net/groups/hotspot/docs/Serviceability.html#battach)
- [HotSpot Serviceability Agent](http://openjdk.java.net/groups/hotspot/docs/Serviceability.html#bsa)

## jcmd


## jhsdb
> [自JDK9发布](https://dzone.com/articles/jhsdb-a-new-tool-for-jdk-9) | [Oracle jhsdb](https://docs.oracle.com/javase/9/tools/jhsdb.htm)

jstack jmap jinfo jsnap 等命令功能的迁移和加强

> 例如
- `jmap -heap pid` => `jhsdb jmap --heap --pid pid`

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

> 提高效率的使用场景
1. 可以使用 Profiler 下的JDBC，操作业务流程，获取所有执行的SQL，用来做索引优化，或排查问题
    - **注意可能不准确**，需要对监控到的SQL有质疑的想法 
        - 真实案例： 监控到对MySQL执行的某条SQL为 `xxx in ('NULL', 2, 4)`. 应用写法不规范未过滤集合中的null值就拼接进了条件
        - 实际上MySQL驱动执行的SQL是 `xxx in (NULL, 2, 4)` 这会导致此子句永远是false，详见 [MySQL 条件操作符](/Database/MySQLAdvance.md#条件操作符)
        - Clone Visualvm的代码后 通过GUI找功能实现，发现可疑方法 org.graalvm.visualvm.lib.jfluid.results.jdbc.SQLStatement#getFullSql
        - 通过arthas watch该方法的返回后，确认是这个方法的问题，
        - 结论为：基于 PreparedStatement 得到执行SQL的实现方式和MySQL驱动的不一样。

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
