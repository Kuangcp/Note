---
title: JVM 监控&诊断
date: 2018-11-21 10:56:52
tags: 
    - JVM
categories: 
    - Java
    - Troubleshoot
---

💠

- 1. [JVM 监控&诊断](#jvm-监控&诊断)
- 2. [JVMTI](#jvmti)
- 3. [JDK自带工具](#jdk自带工具)
    - 3.1. [java](#java)
        - 3.1.1. [环境变量的使用](#环境变量的使用)
    - 3.2. [jar](#jar)
    - 3.3. [jps](#jps)
    - 3.4. [jstat](#jstat)
    - 3.5. [jinfo](#jinfo)
    - 3.6. [jmap](#jmap)
    - 3.7. [jhat](#jhat)
        - 3.7.1. [OQL](#oql)
        - 3.7.2. [HPROF](#hprof)
    - 3.8. [jstack](#jstack)
        - 3.8.1. [实现原理](#实现原理)
    - 3.9. [jcmd](#jcmd)
    - 3.10. [jhsdb](#jhsdb)
- 4. [集成库](#集成库)
    - 4.1. [jvm-sandbox](#jvm-sandbox)
- 5. [终端类工具](#终端类工具)
    - 5.1. [Arthas](#arthas)
    - 5.2. [async-profiler](#async-profiler)
- 6. [图形化工具](#图形化工具)
    - 6.1. [JProfiler](#jprofiler)
    - 6.2. [YourKit](#yourkit)
    - 6.3. [Visualvm](#visualvm)
    - 6.4. [MAT](#mat)
    - 6.5. [JMC](#jmc)
        - 6.5.1. [JFR](#jfr)
    - 6.6. [IBM Heap Analyzer](#ibm-heap-analyzer)
    - 6.7. [IntelliJ IDEA](#intellij-idea)

💠 2026-01-27 19:13:38
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

> [jvm-tools](https://github.com/aragozin/jvm-tools)

# JVMTI
`JVM Tool Interface`

# JDK自带工具
> 都是jdk的bin目录下的工具，注意使用时要和目标JVM同一个JDK版本，以及同一个用户，衍生的工具如Arthas等等同理。

## java
> 使用方式：
- 执行类： `java [-options] class [args...]`
- 执行包： `java [-options] -jar jarfile [args...]` 或 `java -jar [-options] jarfile [args...]`

> **注意** 这些Java options都*不会*生效。
`java -jar jarfile [-options] [args...]`  
`java -jar jarfile [args...] [-options]`  

### 环境变量的使用
> [What is the java -D command-line option good for? ](https://coderanch.com/t/178539/certification/java-command-line-option-good)
- 传入 `java -Dkey=true -jar xxx.jar`
    - -D 参数 要在 -jar **之前**
- 获取 `System.getProperty("key", "defaultvalue");`

## jar
- `jar -tf xxx.jar | grep Driver` 查找jar包是否有对应的类

## jps
> 主要用来输出JVM中运行的进程状态信息
- option:
    - -q 忽略输出的类名、Jar名以及传递给main方法的参数，只输出pid。
    - -m 输出传递给main方法的参数，如果是内嵌的JVM则输出为null。
    - -l 输出应用程序主类的完整包名，或者是应用程序JAR文件的完整路径。
    - -v 输出传给JVM的参数。
    - -V 输出通过标记的文件传递给JVM的参数（.hotspotrc文件，或者是通过参数-XX:Flags=指定的文件）

## jstat
> [Oracle Doc： jstat](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstat.html)

- option:
    - -class 类加载情况
    - -compiler 编译统计
    - -printcompilation JVM编译方法统计
    - 查看内存相关指标
        - `-gcutil` 总gc统计情况
        - `-gc` gc统计情况
        - `-gccapacity` 堆内存空间
        - `-gcnew` 和 `-gcnewcapacity` 新生代gc和内存统计
        - `-gcold` 和 `-gcoldcapacity` 老年代gc和内存统计
        - `-gcpermcapacity` JDK7 永久代 
        - `-gcmetacapacity` JDK8 元空间
    - -t 在第一列输出时间戳`(s)`。该时间戳从jvm启动后开始计时
    - -h3 每隔N行输出一次列表头
    - $PID 进程号
    - interval 输出间隔时间，单位毫秒
    - count 输出次数

> [CSDN: jstat](https://blog.csdn.net/achuo/article/details/107793361)

> Demo:
- `jstat -gcutil -t -h5 7919 1000 50` 


| 列名       | 含义（百分比，除次数/时间外）|
| -------- | -------------------------- |
| **S0**   | Survivor-0 区使用率            |
| **S1**   | Survivor-1 区使用率            |
| **E**    | Eden 区使用率                  |
| **O**    | Old 区使用率                   |
| **M**    | Metaspace 使用率              |
| **CCS**  | Compressed Class Space 使用率 |
| **YGC**  | Young GC 次数                | 
| **YGCT** | Young GC 累计耗时             |
| **FGC**  | Full GC 次数                 | 
| **FGCT** | Full GC 累计耗时               |
| **CGC**  | Concurrent GC 次数（G1/Z 垃圾回收器等）  |
| **CGCT** | Concurrent GC 累计耗时         |
| **GCT**  | 所有 GC 总耗时                 |

## jinfo 
> 观察运行中的 java 进程的运行环境参数：参数包括 Java System 属性和 JVM 命令行参数

> Demo:
- jinfo 14352
- jinfo -sysprops 14352
- 查看JVM参数 `jinfo -flags 14352`
    - jinfo -flag MaxPermSize 14352

## jmap 
> 用来查看堆内存使用状况

> Demo:
- `jmap -histo $PID` 展示实例和占用内存情况
    - `jmap -histo:live $PID` 展示存活实例情况 **注意会触发FullGC**
- `jmap -heap $PID` 展示Java堆的各内存区域大小及占用情况
- `jmap -dump:live,format=b,file=heapLive.hprof $PID` dump下存活对象  **注意会触发FullGC**
    - `jmap -dump:format=b,file=heapLive.hprof $PID` dump所有对象
    - 失败时 可以尝试 -F 参数，强制dump，但此时的dump文件不一定是完整可打开的。
    - 提示attach失败时 可修改 `echo 0 > /proc/sys/kernel/yama/ptrace_scope`  jmap依赖ptrace实现，此选项放开ptrace仅支持父进程执行的限制

注意 centos7.9里，如果当前用户在没有权限的目录下执行dump命令 **低级失误**
- 将默认创建在 /tmp/hsperfdata_username/ 目录下，由于tmp的清理特性，随时会丢失。

************************

## jhat
>  Java Head Analyse Tool [Oracle: jhat](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/tooldescr012.html)

用于分析 jmap 转储出来的堆文件, 分析完后启动一个WebServer， 浏览器打开 127.0.0.1:7000 查看

> 参数
- -J-mx2g 设置最大内存2g
- -J-d64 64位模式
- -port 端口

> 使用
- 网页
    - 首页 所有类，点击可查看类的实例列表
    - 底部 Other Queries 包含： histo，OQL查询，类实例 查看功能
- 比较多个dump `jhat -baseline snapshot_1.hprof snapshot_2.hprof` 1，2文件是先后dump产生的
    - 在底部的类实例`Show instance counts` 中能看到多了一列 例如 `instances (111060 new) of class`
- [OQL查询](http://localhost:7000/oql/) 
    - [OQL使用手册](http://localhost:7000/oqlhelp/)

### OQL
```sql
 select <JavaScript expression to select>
         [ from [instanceof] <class name> <identifier>
         [ where <JavaScript boolean expression to filter> ] ]
```

### HPROF
> [HPROF: A Heap/CPU Profiling Tool](https://docs.oracle.com/javase/8/docs/technotes/samples/hprof.html)  
> [heapdumpstamp](https://github.com/bostrt/heapdumpstamp)`获取hprof创建时间戳`  

************************

## jstack 
> jstack [option] pid  主要用来查看某个Java进程内的线程堆栈信息
- Option:
    - -F: 强制产生一个线程dump 
        - `注意`此方式得到的dump**缺失很多信息**， 只有线程栈和操作系统线程id，没有线程名，线程cid，锁等信息
        - 而且相对于没有-F的方式，实现原理完全不一样，见下文链接
    - -m: 打印java和native frames
    - -l: 打印关于锁的附加信息
    - -J-d64: 64位模式

> 找出占用CPU最高的线程: [封装的Shell active_cpu_thread](https://github.com/Kuangcp/Script/blob/master/shell/assistant/java-tool.sh)
1. `jps 或者 ps aux | grep xxx` 得到对应Java进程id
1. `top -Hp 进程id` 查看 time 占用最长 或者 CPU占用最高 的线程id
1. `printf %x 线程id` 得到 16进制线程id
1. `jstack 进程id | grep -A 20 16进制线程id` 查看该线程的栈,进而分析到代码

> [How to Analyze Java Thread Dumps](https://www.baeldung.com/java-analyze-thread-dumps)`分析工具和思路`  
> [OpenJDK11 jstack output explanation](https://stackoverflow.com/questions/76476637/openjdk11-jstack-output-explanation)  
> [How to Analyze Java Thread Dumps](https://dzone.com/articles/how-analyze-java-thread-dumps)  

扩展：通过在短时间内多次获取stack分析出 活锁，死循环，死锁等问题点，但是通常这类问题只能通过修复代码并重启解决，无法热修复

快速分析

> [jstack.review - Java Thread Dump Analyzer](https://jstack.review)`支持多份jstack对比`  
> [threaddump-analyzer](https://github.com/spotify/threaddump-analyzer)

### 实现原理
- [Jstack 源码分析](https://zhuanlan.zhihu.com/p/36224094)

通常来说 jstack pid 报错无法attach时，意味着是高负载情况了，可以加-F参数尝试  
[jmap -F and jstack -F](https://stackoverflow.com/questions/26140182/running-jmap-getting-unable-to-open-socket-file)`jmap和jstack 默认及加-F选项背后实现机制及优缺点`
- [Dynamic Attach Mechanism](http://openjdk.java.net/groups/hotspot/docs/Serviceability.html#battach)
- [HotSpot Serviceability Agent](http://openjdk.java.net/groups/hotspot/docs/Serviceability.html#bsa)

************************

## jcmd
> jcmd [pid | main-class] command... | PerfCounter.print | -f filename  [Oracle jcmd doc](https://docs.oracle.com/en/java/javase/17/docs/specs/man/jcmd.html)

- jcmd 列出所有可操作的JVM进程
- -f filename 执行文件内的命令

_command_

- Compiler
    - Compiler.codecache
    - Compiler.queue
- GC GC信息，触发GC，堆信息
    | 命令 | 说明 |
    |:----|:----|
    | GC.run                      | 触发一次Full GC
    | GC.heap_info                | 查看堆使用统计
    | GC.class_histogram -all     | 类实例统计 
    | GC.heap_dump -all filename  | 创建所有对象的dump
    | GC.finalizer_info           | finalization 队列信息
    - 参数 `-all` 全部对象，如果去除该参数，将**触发Full GC**来找到所有存活对象

- JFR 
    - JFR.start 会输出提示信息
    - JFR.configure
    - JFR.stop name=1 filename=now.jfr （`name`参数从start执行后的提示信息中获取）
    - JFR.dump
- JVMTI
- ManagementAgent
- System
- Thread
- VM 
    - VM.command_line
    - VM.version
    - VM.uptime [-date]
    - VM.system_properties
- Memory
    - VM.native_memory

## jhsdb
> [jdk9 jhsdb](https://dzone.com/articles/jhsdb-a-new-tool-for-jdk-9) | [Oracle jhsdb](https://docs.oracle.com/javase/9/tools/jhsdb.htm)

JDK9之前通过是Jar方式启动 HSDB CLHSDB。部分功能有被jmap等命令封装 例如 `jmap -heap`
- `java -cp .:sa-jdi.jar sun.jvm.hotspot.CLHSDB` HSDB需要和目标JVM同一个版本
    - help 查看帮助
    - jseval 执行javascript
    - attach：连接到目标进程戒core
    - universe：查看Java heap的情况
    - inspect：查看某个地址对应的数据结构的内容
    - scanoops：扫描某个地址段的Java对象

jstack jmap jinfo jsnap 等命令功能的迁移和加强

> 例如
- `jmap -heap pid` => `jhsdb jmap --heap --pid pid`

********************

# 集成库
> [aragozin/heaplib: JVM Heap dump processing utility](https://github.com/aragozin/heaplib/tree/master)  

## jvm-sandbox
> [jvm-sandbox](https://github.com/alibaba/jvm-sandbox)

> [JVM SandBox 的技术原理与应用分析](https://www.infoq.cn/article/TSY4lGjvSfwEuXEBW*Gp)

# 终端类工具
> [vjtools](https://github.com/vipshop/vjtools)`唯品会`  
> [github.com/dingjs/javaagent](https://github.com/dingjs/javaagent)  

## Arthas
> [Github: Arthas](https://github.com/alibaba/arthas)`阿里巴巴`

> [Arthas Tunnel | arthas](https://arthas.aliyun.com/doc/tunnel.html)  

## async-profiler
> [async-profiler](https://github.com/jvm-profiling-tools/async-profiler)`CPU和内存采样 渲染火焰图`

************************

# 图形化工具

> [Heap Dump Analysers](http://www.fasterj.com/tools/heapdumpanalysers.shtml)  
> [Java Monitoring Tools](https://sematext.com/guides/java-monitoring/)`Profile APM log 等多个解决思路`  

## JProfiler
> [Official Site](https://www.ej-technologies.com/products/jprofiler/overview.html)`收费`  

[OOM 踩坑日记](https://huminxi.netlify.app/2022/06/24/oom%20%E8%B8%A9%E5%9D%91%E6%97%A5%E8%AE%B0/#more)

```
// v13
S-NEO_PENG#890808-g4tibemn0jen#37bb9

// v14
S-J14-NEO_PENG#890808-1jqjtz91lywcp9#23624
```

## YourKit
[YourKit Java Profiler](https://www.yourkit.com/java/profiler)`收费`

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
    - **注意可能不准确**，需要对监控到的SQL辩证对待 
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

> [Analyzing Threads](https://help.eclipse.org/latest/index.jsp?topic=%2Forg.eclipse.mat.ui.help%2Ftasks%2Fanalyzingthreads.html)

注意: 有这样的一种场景, 从数据库获取大量的数据创建为对象, 导致瞬间的OOM 这时候即使使用 jmap 去 dump 了快照, 也看不到占用大量内存的对象, 因为MAT默认展示的是GC可达对象，需要在菜单选择看不可达对象

分析思路：
- 对象: histogram, Top ,
- 线程: 
- 类加载器： histogram -> basic -> merge classloader
- 不可达对象：

************************

> [mat用小内存解析超大堆快照的可行方法](https://baofeidyz.com/feasible-method-for-mat-to-analyze-super-large-heap-snapshots-with-small-memory)

利用安装目录下的 ParseHeapDump.sh 命令行解析 dump的 hprof文件 
全部解析： ParseHeapDump.sh ~/Downloads/java_pidxxx.hprof org.eclipse.mat.api:suspects org.eclipse.mat.api:overview org.eclipse.mat.api:top_components

- ParseHeapDump.sh ~/Downloads/java_pidxxx.hprof org.eclipse.mat.api:suspects
- ParseHeapDump.sh ~/Downloads/java_pidxxx.hprof org.eclipse.mat.api:overview
- ParseHeapDump.sh ~/Downloads/java_pidxxx.hprof org.eclipse.mat.api:top_components

并且可以发现结果文件为html，可以挂载到nginx等web服务器共享结果

************************
> 比较多个dump文件

[MAT比较多个heap dump文件](https://blog.csdn.net/zhuxingchong/article/details/110449138)

************************

## JMC
> [Java Mission Control](https://docs.oracle.com/en/java/java-components/jdk-mission-control/)

1. 通过JMX连接目标JVM 实时监控应用指标
1. 通过对运行中的JVM进行飞行记录`Flight Recorder`, 分析指定时间内代码的可优化点，指标值变化情况

指标值包括：JVM的 内存，CPU，GC，线程，类加载，网络和文件IO； 宿主机的CPU、内存等指标，联合做参考

> [目标JVM开启远程访问JMX](/Java/AdvancedLearning/JMX.md#JVM参数配置) `注意JDK6后就默认开启了进程访问JMX`  
> [JMC 9](https://www.oracle.com/java/technologies/javase/jmc9-release-notes.html)`自身需要JDK17以上运行，可以监控JDK 7u40及往后的版本`  
> [thegreystone/jmc-tutorial: A hands-on-lab/tutorial for learning JDK Mission Control 7+.](https://github.com/thegreystone/jmc-tutorial)  
### JFR
> [JEP 328: Flight Recorder](https://openjdk.org/jeps/328)  
> [Monitoring Java Applications with Flight Recorder | Baeldung](https://www.baeldung.com/java-flight-recorder-monitoring)  

JFR 0.9 版本对应 JDK7 和 JDK8 （均为商用版本）， JFR 1.0 版本对应 JDK 9 和 JDK 10， JFR 2.0 版本对应 JDK11

对于一个JVM进程开启JFR时，实际上是开启了一个线程收集信息，开始这个线程的时候默认内存为250Mib，满了后会循环使用 溢出的部分丢弃或者写入配置的文件路径上。
默认采集全部支持的事件，可以按需过滤出关心的事件，降低性能影响。  
dump指令是将内存的数据dump到磁盘，线程继续在收集 stop 则是停止该收集线程  

开启JFR方式
- JMC: 启动应用，启动JMC，JMC连接到业务JVM后，开启一段时间的JFR，然后直接操作业务逻辑，JFR结束后可以直接进行分析
- jcmd: 使用 [jcmd](#jcmd) 对已经运行中的应用开启 JFR 

> [troubleshoot之:使用JFR解决内存泄露 - flydean - 博客园](https://www.cnblogs.com/flydean/p/jvm-diagnostic-memory-leak.html)  
> [深度探索JFR - JFR详细介绍与生产问题定位落地 - 1. JFR说明与启动配置-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1811738)  

************************

## IBM Heap Analyzer
> [Official Site](https://www.ibm.com/developerworks/community/alphaworks/tech/heapanalyzer)

************************

## IntelliJ IDEA
[Analyze the memory snapshot](https://www.jetbrains.com/help/idea/read-the-memory-snapshot.html)
