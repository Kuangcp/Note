---
title: Java之GC
date: 2021-05-14 20:36:48
tags: 
categories: 
---

**目录 start**

1. [GC](#gc)
    1. [GC类型](#gc类型)
    1. [GC术语](#gc术语)
    1. [内存分代](#内存分代)
    1. [判断存活算法](#判断存活算法)
        1. [引用计数算法](#引用计数算法)
        1. [可达性分析算法](#可达性分析算法)
    1. [GC算法](#gc算法)
        1. [标记清除算法](#标记清除算法)
        1. [复制算法](#复制算法)
        1. [标记整理算法](#标记整理算法)
1. [垃圾收集器](#垃圾收集器)
    1. [Serial](#serial)
    1. [ParNew](#parnew)
    1. [Parallel Scavenge](#parallel-scavenge)
    1. [Serial Old](#serial-old)
    1. [Parallel Old](#parallel-old)
    1. [CMS](#cms)
    1. [G1](#g1)
    1. [ZGC](#zgc)
    1. [ShenandoahGC](#shenandoahgc)
1. [Tuning](#tuning)
    1. [Tool](#tool)

**目录 end**|_2021-05-14 20:41_|
****************************************
# GC
> Garbage Collection

GC 的目的是识别出不再使用的内存，并将其变为可用的。现代垃圾收集器通常分几个阶段以及根据不同的分代使用不同的垃圾收集器来完成回收过程

> 要点： 什么时候, 对什么东西, 做了什么

cms(JDK14中被移除)，epsilon，g1，parallel，serial，shenandoah，zgc

- [Oracle JDK8 GC调优指南](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/toc.html)
- [Oracle JDK11 GC调优指南](https://docs.oracle.com/en/java/javase/11/gctuning/introduction-garbage-collection-tuning.html)

> [Github: OpenJDK 12 GC 算法源码](https://github.com/openjdk/jdk/tree/jdk-12+33/src/hotspot/share/gc)  
> [《沙盘模拟系列》JVM如何调优](https://my.oschina.net/u/4030990/blog/3149182)  
> [参考: CMS Deprecated. Next Steps?](https://dzone.com/articles/cms-deprecated-next-steps)  

************************

## GC类型

> [RednaxelaFX](https://www.zhihu.com/question/41922036/answer/93079526)
- `Partial GC`：并不收集整个GC堆的模式
    - `Young GC`：只收集young gen的GC
    - `Old GC`：只收集old gen的GC。只有CMS的concurrent collection是这个模式
    - `Mixed GC`：收集整个young gen以及部分old gen的GC。只有G1有这个模式
- `Full GC`：收集整个堆，包括young gen、old gen、perm gen（如果存在的话）等所有部分的模式。
    - gc日志中有明确的 [Full GC ]

`新生代GC Minor GC`  
发生在新生代的垃圾收集动作, 因为大多数对象都是存活时间很短, 所以 Minor GC 非常频繁, 一般回收速度也比较快.   
扫描过后将 Eden 和 现在使用的 Survivor 两个区中的存活对象 全搬去空闲的 Survivor.   
如果 存活的对象内存大小大于 Survivor 区大小, 则需要`分配担保机制`提前将对象转移到老年代中

`老年代GC Major GC`  
发生在老年代的GC, 出现了 Major GC, 往往会伴随至少一次 Minor GC. Major GC 的速度一般会比 Minor GC 慢10倍以上.

> [What causes a Full GC to run?](https://stackoverflow.com/questions/42226785/what-causes-a-full-gc-to-run)

> [参考: Major GC和Full GC的区别是什么？](https://www.zhihu.com/question/41922036)
- HotSpot上的一次 Full GC: 针对 新生代 老生代 元空间 的全局范围的GC, 将会 STW(Stop The World)

> https://www.zhihu.com/question/41922036/answer/93079526

- 最简单的分代式GC策略，按HotSpot VM的serial GC的实现来看，触发条件是：
    - young GC：当young gen 中的 eden gen 分配满的时候触发。注意young GC中有部分存活对象会晋升到old gen，所以young GC后old gen的占用量通常会有所升高。
    - full GC：当准备要触发一次young GC时，如果发现统计数据说之前young GC的平均晋升大小比目前old gen剩余的空间大，则不会触发young GC而是转为触发full GC
    - （因为HotSpot VM的GC里，除了CMS的concurrent collection之外，其它能收集old gen的GC都会同时收集整个GC堆，包括young gen，所以不需要事先触发一次单独的young GC）；
    - 或者，如果有perm gen的话，要在perm gen分配空间但已经没有足够空间时，也要触发一次full GC；或者System.gc()、heap dump带GC，默认也是触发full GC。

************************

## GC术语

- `并行（Parallel）` 运行中的 JVM 包含应用程序线程和 GC 线程。在并行阶段，会运行多个 GC 线程，也就是说任务被拆分给它们去完成。至于 GC 线程是否可以与正在运行的应用程序线程重叠，这个在规范中并没有特别说明。
- `串行（Serial）` 只有单个 GC 线程在运行。与上面的并行阶段一样，规范中也没有说明 GC 线程是否可以与当前运行的应用程序线程重叠。
- `并发（Concurrent）` GC 线程和应用程序线程并发执行。
- `Stop The World（STW）` 应用程序线程被暂停，让 GC 线程执行它们的任务。当你遇到 GC 停顿时，说明虚拟机进入了 STW 阶段。
- `增量（Incremental）` 在增量阶段，它可以运行一段时间，并基于某些条件提前终止，例如时间预算或执行更高优先级的 GC 阶段。

## 内存分代

> [Oracle Java8 Doc: Generation](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/generations.html#sthref16)

![](img/003-jvm-generation-design.drawio.svg)

> [参考: JVM中新生代为什么要有两个Survivor（form,to）？](https://www.zhihu.com/question/44929481)  
> [参考: 为什么新生代内存需要有两个Survivor区](https://blog.csdn.net/antony9118/article/details/51425581)  

> [聊聊JVM的年轻代](http://ifeve.com/jvm-yong-generation/)  
> 我是一个普通的java对象，我出生在Eden区，在Eden区我还看到和我长的很像的小兄弟，我们在Eden区中玩了挺长时间。  
有一天Eden区中的人实在是太多了，我就被迫去了Survivor区的“From”区，自从去了Survivor区，我就开始漂了，  
有时候在Survivor的“From”区，有时候在Survivor的“To”区，居无定所。  
直到我18岁的时候，爸爸说我成人了，该去社会上闯闯了。于是我就去了年老代那边，年老代里，人很多，并且年龄都挺大的，我在这里也认识了很多人。  
在年老代里，我生活了20年(每次GC加一岁)，然后被回收。  

## 判断存活算法
### 引用计数算法
> 给对象添加一个引用计数器, 每当有一个地方引用该对象就加一, 引用失效就减一; 计数器值为零的对象就是不可能被使用的对象

但是该算法无法解决 对象间循环引用的问题, 例如 A 引用 B, B 引用 A, 但是这两个对象都是没有被别的对象引用，此时遍历对象才能解决。

### 可达性分析算法
当一个对象到 GC Roots 对象没有任何引用链相连时(或者说从 GC Roots 到该对象的路径不可达), 则证明该对象是可回收的

GC Roots 对象包含:
- 虚拟机栈(栈帧中的本地变量表)中引用的对象
- 方法区中类静态属性引用的对象
- 方法去中常量引用的对象
- 本地方法栈中 JNI (Native 方法) 引用的对象
- 线程对象

************************

## GC算法
### 标记清除算法
> 首先标记出所有需要回收的对象, 在标记完成后统一回收

`缺点`
1. 效率问题: 标记和清除两个过程的效率不高
1. 空间问题: 容易引起内存碎片化问题, 碎片太多可能导致后期需要分配较大对象时找不到足够大的连续内存
    - 并因此触发一次垃圾收集动作

### 复制算法
> 将内存按容量划分为等大的两块, 每次只使用其中的一块, 当这块的内存用到需要回收了, 就将需要存活的对象复制到另一块上去, 将该块全部清理掉  
> 转而只使用另一个块 这样就不会有内存碎片化问题, 但是可使用的内存只有原来的一半

适用于新生代

### 标记整理算法
> 标记过程和标记清除算法是一致的, 但是后续是让存活的对象往一端移动, 清理掉端边界以外的内存.

适用于老年代

************************

# 垃圾收集器
> JVM垃圾收集器发展历程 

- 第一阶段，Serial（串行）收集器
    - 在jdk1.3.1之前，java虚拟机仅仅能使用Serial收集器。 Serial收集器是一个单线程的收集器，但它的“单线程”的意义并不仅仅是说明它只会使用一个CPU或一条收集线程去完成垃圾收集工作，更重要的是在它进行垃圾收集时，必须暂停其他所有的工作线程，直到它收集结束。
- 第二阶段，Parallel（并行）收集器
    - Parallel收集器也称吞吐量收集器，相比Serial收集器，Parallel最主要的优势在于使用多线程去完成垃圾清理工作，这样可以充分利用多核的特性，大幅降低gc时间。
- 第三阶段，CMS（并发）收集器
    - CMS收集器在Minor GC时会暂停所有的应用线程，并以多线程的方式进行垃圾回收。在Full GC时不再暂停应用线程，而是使用若干个后台线程定期的对老年代空间进行扫描，及时回收其中不再使用的对象。
- 第四阶段，G1（并发）收集器
    - G1收集器（或者垃圾优先收集器）的设计初衷是为了尽量缩短处理超大堆（大于4GB）时产生的停顿。相对于CMS的优势而言是内存碎片的产生率大大降低。

> `java -XX:+PrintCommandLineFlags -version` 可以通过该命令快速知道当前版本JDK默认垃圾收集器

*******************

> JVM垃圾收集器种类

根据设计, 往往是新生代和老年代使用不同的垃圾收集器并组合使用, 因为各分代之间特性不同  
1. 新生代
    - Serial (第一代)
    - PraNew (第二代)
    - Parallel Scavenge (第三代)
    - G1收集器(第四代)
2. 老年代
    - Serial Old (第一代)
    - Parallel Old (第二代)
    - CMS (第三代)
    - G1收集器 (第四代)

- 收集器搭配时的限制条件: 
    - CMS不能和 Parallel Scavenge 一起用
    - Parallel Old 只能和 Parallel Scavenge 一起用
    - G1 只能单独使用(独自处理新生代和老年代)

************************

- `吞吐量 = 运行用户代码时间 / (用户代码时间 + 垃圾收集时间)`
- 并行和并发
    - 并行：充分利用多核CPU来缩短STW的时间, 并发：部分其他收集器需要停顿的逻辑也和用户进程并发执行

************************

> 查看当前使用的垃圾收集器 
- `-XX:+PrintCommandLineFlags` 或者查看GC日志中代的名称 `-XX:+PrintGCDetails`
- JDK1.7 1.8 默认垃圾收集器Parallel Scavenge（新生代）+Parallel Old（老年代）
- JDK1.9 以上 默认垃圾收集器G1

************************

## Serial
> 单线程垃圾收集器 JDK1.3.1之前唯一选择, 仅用于新生代

单线程的收集器, 采用复制算法, client模式下默认收集器, 因为client的内存一般不会很大, 单线程反而效率更高, STW的时间也不会很长

************************

## ParNew
> Serial 收集器的多线程版本, 仅用于新生代

仅有该收集器和Serial收集器能和CMS收集器一起使用, 当使用CMS的时候默认是ParNew

> 注: 单核服务器时, 该收集器性能必然比Serial差, 因为线程调度开销

************************

## Parallel Scavenge
> 并行多线程收集器, 同样使用标记复制算法 着重点是可控制的吞吐量, 可以高效率利用CPU时间, 仅用于新生代

`-XX:-UseParallelGC`

- 控制最大垃圾收集停顿时间 `-XX:MaxGCPauseMillis` (大于0的整数 millis)
    - 该值并不是越小越好, GC停顿时间缩短是牺牲吞吐量和新生代空间来换取的 
    - 新生代空间越小则垃圾收集器回收时间则更短, 但是也更频繁, 停顿时间降下来了,但是吞吐量就下降了
- 直接设置吞吐量大小 `-XX:GCTimeRatio` (0,100)
    - 收集器将尽可能保证内存回收的时间不超过设置值, 值为垃圾收集时间占总时间的比率, 相当于吞吐量的倒数
    - 如果设置为 49 则允许的最大GC时间占总时间的 1/(1+49)
- GC自适应策略 `-XX:+UseAdaptiveSizePolicy`
    - 该参数启用后, 就无需手动设置新生代的大小(-Xmn)和Eden和Survivor的比例(-XX:SurvivorRatio) 晋升老年代对象大小(-XX:PretenureSizeThreshold) 等细节参数了
    - 虚拟机将动态调整这些参数

************************

## Serial Old
> Serial收集器的老年代版本, 单线程收集器 

主要用于client模式下  
server模式下: 1.5之前的版本与Parallel Scavenge搭配使用, 或者作为CMS的备选方案

************************

## Parallel Old
> 是Parallel Scavenge 收集器的老年代版本

`-XX:+UseParallelOldGC`

************************

## CMS
> Concurrent Mark Sweep 着重点是尽可能缩短垃圾收集时用户线程的停顿时间 [Oracle Doc](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/cms.html)

`-XX:+UseConcMarkSweepGC`

工作流程, 依次执行
1. 初始标记 CMS initial mark
1. 并发标记 CMS concurrent mark
1. 最终标记 CMS final remark
1. 并发清除 CMS concurrent sweep

> 例如：
```log
4936.782: [GC (CMS Initial Mark) [1 CMS-initial-mark: 747140K(1494272K)] 752384K(1800960K), 0.0043788 secs] [Times: user=0.01 sys=0.00, real=0.00 secs] 
4936.787: [CMS-concurrent-mark-start]
4936.942: [CMS-concurrent-mark: 0.156/0.156 secs] [Times: user=0.23 sys=0.01, real=0.16 secs] 
4936.942: [CMS-concurrent-preclean-start]
4936.948: [CMS-concurrent-preclean: 0.005/0.005 secs] [Times: user=0.01 sys=0.00, real=0.00 secs] 
4936.948: [CMS-concurrent-abortable-preclean-start]
4938.832: [GC (Allocation Failure) 2020-11-23T17:06:01.905+0800: 4938.832: [ParNew: 277821K->4257K(306688K), 0.0088608 secs] 1024961K->751463K(1800960K), 0.0089994 secs] [Times: user=
4939.249: [CMS-concurrent-abortable-preclean: 0.774/2.301 secs] [Times: user=1.32 sys=0.09, real=2.31 secs] 
4939.250: [GC (CMS Final Remark) [YG occupancy: 142153 K (306688 K)]2020-11-23T17:06:02.323+0800: 4939.250: [Rescan (parallel) , 0.0225236 secs]2020-11-23T17:06:02.346+0800: 4939.273:
4939.382: [CMS-concurrent-sweep-start]
4939.627: [CMS-concurrent-sweep: 0.235/0.245 secs] [Times: user=0.43 sys=0.03, real=0.24 secs] 
4939.627: [CMS-concurrent-reset-start]
4939.631: [CMS-concurrent-reset: 0.004/0.004 secs] [Times: user=0.00 sys=0.00, real=0.01 secs]
```

- 优点: 并发低停顿  
- 缺点: 
    1. 因为会和用户进程抢占CPU资源, 会导致应用程序变慢, 造成总吞吐量的下降. 默认启动的线程数为 (CPU数量+3)/4
    1. 无法处理浮动垃圾, 可能出现 Concurrent Mode Failure 从而引起新一次FullGC
        - 并发清理阶段用户线程还在运行，这段时间就可能产生新的垃圾，新的垃圾在此次GC无法清除，只能等到下次清理
    1. 由于使用的是标记清除算法, 容易导致大量空间碎片, 这样的后果是分配大内存对象会很麻烦, 往往出现老年代总空间还有大量剩余, 但是没有足够大的连续空间
        - 为了解决该问题, 提供了参数 `-XX:+UseCMSCompactAtFullCollection` 默认开启, 用于在FullGC时进行内存碎片的合并, 该过程无法并发还是要 STW
        - 还有一个参数 `-XX:CMSFullGCsBeforeCompaction` 默认为0, 设置多少次不压缩的FullGC后进行一次压缩的FullGC(内存合并的FullGC)

其中 初始标记 和 重新标记 仍然需要 STW, 两个并发的过程是和用户线程并发执行的对吞吐量有一定影响  
且由于是并发执行的, 那么并发的两个阶段用户进程是需要执行的, 就需要给这些线程预留足够的内存空间, 默认触发GC的阈值是 老年代使用了68%后(1.5) 1.6是92%  
可通过 `-XXCMSInitiatingOccupancyFraction` 进行设置. 如果CMS执行期间发现剩余内存不足以让程序正常运行, 就会临时启用 Serial Old  
所以该参数不可设置过高, 否则容易导致频繁采用单线程版的垃圾回收器, 大大延长 STW 时间

> [参考: JVM 源码解读之 CMS GC 触发条件 ](https://mp.weixin.qq.com/s?__biz=MzUyMDE1ODQ3NQ==&mid=2247483851&idx=1&sn=8cb444039449848531b7ca72c396e07e&chksm=f9efedafce9864b9dbb645863d7d3c8b34e83888d07e175dd9c931576db2ecc0aa90835fcf50&scene=21#wechat_redirect)  

CMS自己会进入full GC的情况就是它的并发收集模式跟不上应用分配内存的速度了，或者是碎片化开始变严重了。  
主要体现是GC日志里可以看到concurrent mode failure字样，然后就开始可以看到 [Full GC ... ] 的日志了  
这样就带来一个问题，如果CMS并发GC发生了，此时是无法利用 `-XX:+HeapDumpBeforeFullGC` 参数保留现场，因为不是发生 FullGC  

## G1
> Garbage First 面向服务端应用的垃圾收集器, JDK7发布, JDK9作为默认GC [Oracle Doc](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/g1_gc.html#garbage_first_garbage_collection)

`-XX:+UseG1GC`

- 分代收集
    - 虽然G1可以独立管理整个堆, 但同样具有分代的概念
- 空间整合
    - 从整体上看是基于标记整理算法, 局部(两个Region之间)上基于标记复制算法, 相比于CMS不容易产生内存碎片
- 可预测的停顿
    - G1除了追求低停顿, 还能建立可预测的停顿时间模型, 能让使用者明确指定在一个长度为M毫秒的时间片段内, 消耗在垃圾收集上的时间不得超过N毫秒
    - 几乎是RTSJ的特征

> [参考: JVM系列篇：深入剖析G1收集器](https://my.oschina.net/u/3959491/blog/3029276)

- 字符串常量池去重 特性 `-XX:+UseStringDeduplication -XX:+PrintStringDeduplicationStatistics`

************************

## ZGC
> JDK11引入 JDK15正式使用 [wiki: ZGC](https://wiki.openjdk.java.net/display/zgc/Main) | [ZGC Release note](https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html#JDK-8197831)

`-XX:+UnlockExperimentalVMOptions -XX:+UseZGC`

> [参考: Oracle 即将发布的全新 Java 垃圾收集器 ZGC](https://www.infoq.cn/article/oracle-release-java-gc-zgc)

************************

## ShenandoahGC
> JDK12  [wiki: ShenandoahGC](https://wiki.openjdk.java.net/display/shenandoah/Main)

> [参考: JDK12 ShenandoahGC小试牛刀](https://juejin.im/post/5c934a5d5188252dad05d82a)  

************************
# Tuning
## Tool
- [GCViewer](https://github.com/chewiebug/GCViewer)  
