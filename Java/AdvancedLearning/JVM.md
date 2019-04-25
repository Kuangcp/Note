---
title: JVM
date: 2019-04-02 10:56:52
tags: 
    - JVM
categories: 
    - Java
---

**目录 start**
 
1. [JVM](#jvm)
    1. [运行时数据区](#运行时数据区)
        1. [程序计数器](#程序计数器)
        1. [Java虚拟机栈](#java虚拟机栈)
        1. [本地方法栈](#本地方法栈)
        1. [Java堆](#java堆)
            1. [堆内存分配策略](#堆内存分配策略)
        1. [方法区](#方法区)
            1. [运行时常量池](#运行时常量池)
        1. [直接内存](#直接内存)
    1. [元空间](#元空间)
    1. [参数配置](#参数配置)
1. [GC](#gc)
    1. [GC 术语](#gc-术语)
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
1. [JVM不同实现](#jvm不同实现)
    1. [Hotspot JVM](#hotspot-jvm)
    1. [OpenJ9](#openj9)

**目录 end**|_2019-04-25 14:45_|
****************************************
# JVM
> Oracle 默认采用的是 Hotspot JVM

> [Java Language and Virtual Machine Specifications](https://docs.oracle.com/javase/specs/)

> [Github:jvm学习仓库](https://github.com/xwjie/jvm)
> [个人博客: JVM归类](https://vinoit.me/tags/jvm/)
 
`书籍`
- 《深入理解 Java 虚拟机》(周志明 第二版) 大部分内容来源于此, 但是部分内容是依据Java8有所改动

## 运行时数据区
![](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Java/Jvm/MemoryArea.png)

线程私有的内存区域: 程序计数器 本地方法栈 虚拟机栈. 生命周期与线程保持一致

### 程序计数器
可以看作是当前线程所执行的字节码的行号指示器, 这个内存区域是唯一一个在JVM规范中没有规定任何 OutOfMemoryError 的区域

### Java虚拟机栈
> HotSpot 中不区分Java虚拟机栈和本地方法栈, 虽然 -Xoss 存在(设置本地方法栈大小)但是是无效的, 只能通过 -Xss 设置

虚拟机栈描述的是Java方法执行的内存模型: 每个方法在执行的同时, 都会创建一个栈帧(Stack Frame) 用于存储局部变量表, 操作数栈, 动态链接, 方法出口等信息  
每个方法调用到执行完成的过程, 就对应着一个栈帧在虚拟机栈中入栈到出栈的过程

- 局部变量表
    - 存放了编译期可知的各种 基本数据类型, 对象引用, returnAddress 类型
        - 对象引用: reference 类型, 不等同于对象本身, 可能是一个指向对象地址的引用指针, 可能是一个代表对象的句柄, (可能是其他与此对象相关的位置?)
        - returnAddress: 指向了一条字节码指令的地址
    - 只有 long double 类型 会占用 2 个局部变量空间, 其他类型都只占用 1 个, 局部变量表所需的内存空间在编译后就已经确定下来, 运行期是不会变的

- Java虚拟机规范中对该内存区域定义了两种异常状况
    - 如果线程请求的栈深度大于虚拟机所允许的最大深度, 将抛出 StackOverFlowError 
    - 如果虚拟机在扩展栈时, 无法申请到足够的内存, 则抛出 OutOfMemoryError 异常

### 本地方法栈
Native Method Stack, 与虚拟机栈所发挥的作用是相似的, 只不过虚拟机栈是为虚拟机执行Java方法服务, 本地方法栈是为了虚拟机使用 Native 方法服务

### Java堆
> Java虚拟机规范中的描述是 所有对象实例以及数组都是在堆上分配, 但是由于 JIT编译器 逃逸分析 栈上分配, 标量替换等技术, 就变得没那么绝对了

堆分为 新生代(包含: Eden, Survivor from, Survivor to) 老年代   
从堆和栈的功能和作用来通俗的比较,堆主要用来存放对象的，栈主要是用来执行程序的.  
JVM是基于堆栈的虚拟机.JVM为每个新创建的线程都分配一个堆栈.也就是说,对于一个Java程序来说，它的运行就是通过对堆栈的操作来完成的。  
堆栈以栈帧为单位保存线程的状态。JVM对堆栈只进行两种操作:以帧为单位的压栈和出栈操作。 

> [参考博客: Java中堆内存和栈内存详解](http://www.cnblogs.com/whgw/archive/2011/09/29/2194997.html)

#### 堆内存分配策略
- 对象的内存分配, 粗略讲就是在堆上分配(但也可能经过JIT编译后被拆散成标量类型并间接地栈上分配)   
- 对象主要分配在Eden; 如果启动了本地线程分配缓冲, 则优先在TLAB上分配; 也有直接分配在老年代的 (长字符串以及数组)

1. `类变量`（static修饰的变量） 在程序加载时系统就为它在堆中开辟了内存，堆中的内存地址存放于栈以便于高速访问。  
    - 生命周期: 从应用进程启动一直到进程停止
2. `实例变量` 当你使用java关键字new的时候，系统在堆中开辟并不一定是连续的空间分配给变量（比如说类实例），然后根据零散的堆内存地址，通过哈希算法换算为一长串数字以表征这个变量在堆中的"物理位置"。 
    - 生命周期: 当实例变量的引用丢失后，将被GC（垃圾回收器）列入可回收“名单”中，但并不是马上就释放堆中内存
3. `局部变量` 局部变量，由声明在某方法，或某代码段里（比如for循环），执行到它的时候在栈中开辟内存
    - 生命周期: 当局部变量一但脱离作用域，内存立即释放

************************    

- 如果对象在 Eden 出生, 并经过一次 MinorGC后存活, 并能被 Survivor 容纳, 将被移入 Survivor 且年龄为1.
    - 对象在 Survivor 每经过一次 MinorGC 年龄加1, 当达到 MaxTenuringThreshold(默认15) 就会移入老年代
- 如果 Survivor 空间中相同年龄所有对象大小的总和大于 Survivor 空间的一半, 年龄大于等于该年龄的对象都将进入老年代, 无需等到设置的 MaxTenuringThreshold

> 堆内存配置: 新生代一般设置为整个堆空间的1/3到1/4左右最合适。  
新生代内存不能过大也不能过小, 过大则老年代内存过小, 导致频繁 FullGC  
过小则导致对象全在老年代分配,新生代上无法分配(Allocation Failure) 也将导致频繁 Full GC 

### 方法区
方法区存在于永久代 Perm Gen, 对应于Java8中的MetaSpace

用于存放 Class 相关信息, 常量, 静态变量, 访问修饰符, 字段描述, 方法描述, JIT编译器编译后的代码等数据   
在 HotSpot 虚拟机上, 方法区也看做是 永久代 Permanent Gen, 两者关系是: 方法区是Java虚拟机规范, 永久代是方法区在Hotspot上的实现  
从Java8开始, 永久代已经被 MetaSpace(操作的直接内存) 取代   

JDK7中符号表被移动到 Native Heap中，字符串常量池和类引用被移动到 Java Heap中。

#### 运行时常量池
运行时常量池是方法区的一部分, 用于存放编译期生成的各种字面量和符号引用,这部分内容将在类加载后进入方法区的运行时常量池存放.

### 直接内存
直接内存并不是虚拟机运行时数据区的一部分, 也不是Java虚拟机规范中定义的内存区域. 但是这部分内存也被频繁地使用, 而且也可能导致 OutOfMemoryError 

NIO 会经常使用, 提高性能

## 元空间
> Java8 引入, 取代了以往的 Perm Gen

- 充分利用了Java语言规范：类及相关的元数据的生命周期与类加载器的一致。
- 每个类加载器都有它的内存区域-元空间
- 只进行线性分配
- 不会单独回收某个类（除了重定义类 RedefineClasses 或类加载失败）
- 没有GC扫描或压缩
- 元空间里的对象不会被转移
- 如果GC发现某个类加载器不再存活，会对整个元空间进行集体回收

## 参数配置
`-XX:SurvivorRatio` 配置 Edgen 和 单个Survivor 的比例, 如果配置为2 则是 2:1:1

**********************

# GC
> Garbage Collection

GC 的目的是识别出不再使用的内存，并将其变为可用的。现代垃圾收集器通常分几个阶段以及根据不同的分代使用不同的垃圾收集器来完成回收过程

> 什么时候, 对什么东西, 做了什么


`新生代GC Minor GC`  
发生在新生代的垃圾收集动作, 因为大多数对象都是存活时间很短, 所以 Minor GC 非常频繁, 一般回收速度也比较快.   
扫描过后将 Eden 和 现在使用的 Survivor 两个区中的存活对象 全搬去空闲的 Survivor.   
如果 存活的对象内存大小大于 Survivor 区大小, 则需要`分配担保机制`提前将对象转移到老年代中

`老年代GC Major GC`  
发生在老年代的GC, 出现了 Major GC, 往往会伴随至少一次 Minor GC. Major GC 的速度一般会比 Minor GC 慢10倍以上.

> [What causes a full GC to run?](https://stackoverflow.com/questions/42226785/what-causes-a-full-gc-to-run)
*************
> [Generation](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/generations.html#sthref16)

![Generation](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Java/Jvm/Generation.png)

> [参考博客: JVM中新生代为什么要有两个Survivor（form,to）？](https://www.zhihu.com/question/44929481)  
> [参考博客: 为什么新生代内存需要有两个Survivor区](https://blog.csdn.net/antony9118/article/details/51425581)  

> [聊聊JVM的年轻代](http://ifeve.com/jvm-yong-generation/)  
> 我是一个普通的java对象，我出生在Eden区，在Eden区我还看到和我长的很像的小兄弟，我们在Eden区中玩了挺长时间。  
有一天Eden区中的人实在是太多了，我就被迫去了Survivor区的“From”区，自从去了Survivor区，我就开始漂了，  
有时候在Survivor的“From”区，有时候在Survivor的“To”区，居无定所。  
直到我18岁的时候，爸爸说我成人了，该去社会上闯闯了。于是我就去了年老代那边，年老代里，人很多，并且年龄都挺大的，我在这里也认识了很多人。  
在年老代里，我生活了20年(每次GC加一岁)，然后被回收。  

## GC 术语

- `并行（Parallel）` 运行中的 JVM 包含应用程序线程和 GC 线程。在并行阶段，会运行多个 GC 线程，也就是说任务被拆分给它们去完成。至于 GC 线程是否可以与正在运行的应用程序线程重叠，这个在规范中并没有特别说明。
- `串行（Serial）` 只有单个 GC 线程在运行。与上面的并行阶段一样，规范中也没有说明 GC 线程是否可以与当前运行的应用程序线程重叠。
- `并发（Concurrent）` GC 线程和应用程序线程并发执行。
- `Stop The World（STW）` 应用程序线程被暂停，让 GC 线程执行它们的任务。当你遇到 GC 停顿时，说明虚拟机进入了 STW 阶段。
- `增量（Incremental）` 在增量阶段，它可以运行一段时间，并基于某些条件提前终止，例如时间预算或执行更高优先级的 GC 阶段。

## 判断存活算法
### 引用计数算法
> 给对象添加一个引用计数器, 每当有一个地方引用该对象就加一, 引用失效就减一; 计数器值为零的对象就是不可能被使用的对象

但是该算法无法解决 对象间循环引用的问题, 例如 A 引用 B, B 引用 A, 但是这两个对象都是没有被别的对象引用

- [ ] 如何解决循环引用问题?

### 可达性分析算法
当一个对象到 GC Roots 对象没有任何引用链相连时(或者说从 GC Roots 到该对象不可达), 则证明该对象是不可用的

GC Roots 对象包含:
- 虚拟机栈(栈帧中的本地变量表)中引用的对象
- 方法区中类静态属性引用的对象
- 方法去中常量引用的对象
- 本地方法栈中 JNI (Native 方法) 引用的对象

************************

## GC算法
> [参考博客: Major GC和Full GC的区别是什么？](https://www.zhihu.com/question/41922036)

*****

- [ ] HotSpot 上 一次 Full GC: 针对 新生代 老生代 元空间 的全局范围的GC, 将会 STW(Stop The World)

> https://www.zhihu.com/question/41922036/answer/93079526

- 最简单的分代式GC策略，按HotSpot VM的serial GC的实现来看，触发条件是：
    - young GC：当young gen 中的 eden gen 分配满的时候触发。注意young GC中有部分存活对象会晋升到old gen，所以young GC后old gen的占用量通常会有所升高。
    - full GC：当准备要触发一次young GC时，如果发现统计数据说之前young GC的平均晋升大小比目前old gen剩余的空间大，则不会触发young GC而是转为触发full GC
    - （因为HotSpot VM的GC里，除了CMS的concurrent collection之外，其它能收集old gen的GC都会同时收集整个GC堆，包括young gen，所以不需要事先触发一次单独的young GC）；
    - 或者，如果有perm gen的话，要在perm gen分配空间但已经没有足够空间时，也要触发一次full GC；或者System.gc()、heap dump带GC，默认也是触发full GC。

### 标记清除算法
> 首先标记出所有需要回收的对象, 在标记完成后统一回收

`缺点`
1. 效率问题: 标记和清除两个过程的效率不高
1. 空间问题: 容易引起内存碎片化问题, 碎片太多可能导致后期需要分配较大对象时找不到足够大的连续内存
    - 并因此触发一次垃圾收集动作

### 复制算法
> 将内存按容量划分为等大的两块, 每次只使用其中的一块, 当这块的内存用到需要回收了, 就将需要存活的对象复制到另一块上去, 将该块全部清理掉  
> 转而只使用另一个块 这样就不会有内存碎片化问题, 但是可使用的内存缩减为原来的一半了

适用于新生代

### 标记整理算法
> 标记过程和标记清除算法是一致的, 但是后续是让存活的对象往一端移动, 清理掉端边界以外的内存.

适用于老年代

************************

## 垃圾收集器
> JVM垃圾收集器发展历程

- 第一阶段，Serial（串行）收集器
    - 在jdk1.3.1之前，java虚拟机仅仅能使用Serial收集器。 Serial收集器是一个单线程的收集器，但它的“单线程”的意义并不仅仅是说明它只会使用一个CPU或一条收集线程去完成垃圾收集工作，更重要的是在它进行垃圾收集时，必须暂停其他所有的工作线程，直到它收集结束。
- 第二阶段，Parallel（并行）收集器
    - Parallel收集器也称吞吐量收集器，相比Serial收集器，Parallel最主要的优势在于使用多线程去完成垃圾清理工作，这样可以充分利用多核的特性，大幅降低gc时间。
- 第三阶段，CMS（并发）收集器
    - CMS收集器在Minor GC时会暂停所有的应用线程，并以多线程的方式进行垃圾回收。在Full GC时不再暂停应用线程，而是使用若干个后台线程定期的对老年代空间进行扫描，及时回收其中不再使用的对象。
- 第四阶段，G1（并发）收集器
    - G1收集器（或者垃圾优先收集器）的设计初衷是为了尽量缩短处理超大堆（大于4GB）时产生的停顿。相对于CMS的优势而言是内存碎片的产生率大大降低。

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
> 查看当前使用的垃圾收集器 
- `-XX:+PrintCommandLineFlags` 或者查看GC日志中代的名称 `-XX:+PrintGCDetails`
- JDK1.7 1.8 默认垃圾收集器Parallel Scavenge（新生代）+Parallel Old（老年代）
- JDK1.9 默认垃圾收集器G1

***************

### Serial
> 单线程垃圾收集器 JDK1.3.1之前唯一选择, 仅用于新生代

单线程的收集器, 采用复制算法, client模式下默认收集器, 因为client的内存一般不会很大, 单线程反而效率更高, STW的时间也不会很长

### ParNew
> Serial 收集器的多线程版本, 仅用于新生代

仅有该收集器和Serial收集器能和CMS收集器一起使用, 当使用CMS的时候默认是ParNew

> 注: 单核服务器时, 该收集器性能必然比Serial差, 因为线程调度开销

### Parallel Scavenge
> 并行多线程收集器, 同样使用标记复制算法 着重点是可控制的吞吐量, 可以高效率利用CPU时间, 仅用于新生代

吞吐量 = 运行用户代码时间 / (用户代码时间 + 垃圾收集时间)

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

### Serial Old
> Serial收集器的老年代版本, 单线程收集器 

主要用于client模式下  
server模式下: 1.5之前的版本与Parallel Scavenge搭配使用, 或者作为CMS的备选方案

### Parallel Old
> 是Parallel Scavenge 收集器的老年代版本

### CMS
> Concurrent Mark Sweep 着重点是尽可能缩短垃圾收集时用户线程的停顿时间

工作流程, 依次执行
1. 初始标记 CMS initial mark
1. 并发标记 CMS concurrent mark
1. 重新标记 CMS remark
1. 并发清除 CMS concurrent sweep

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

### G1
> Garbage First 面向服务端应用的垃圾收集器, JDK7发布, JDK9作为默认GC

- 并行和并发
    - 充分利用多核CPU来缩短STW的时间, 部分其他收集器需要停顿的逻辑也和用户进程并发执行
- 分代收集
    - 虽然G1可以独立管理整个堆, 同样具有分代的概念
- 空间整合
    - 从整体上看是基于标记整理算法, 局部(两个Region之间)上基于标记复制算法, 相比于CMS不容易产生内存碎片
- 可预测的停顿
    - G1除了追求低停顿, 还能建立可预测的停顿时间模型, 能让使用者明确指定在一个长度为M毫秒的时间片段内, 消耗在垃圾收集上的时间不得超过N毫秒
    - 几乎是RTSJ的特征

> [参考博客: JVM系列篇：深入剖析G1收集器](https://my.oschina.net/u/3959491/blog/3029276)

### ZGC
> JDK11 

> [参考博客: Oracle 即将发布的全新 Java 垃圾收集器 ZGC](https://www.infoq.cn/article/oracle-release-java-gc-zgc)

********************************

# JVM不同实现
## Hotspot JVM
原先 SUN 公司开发, 现为 Oracle JDK 中默认JVM

## OpenJ9
IBM主导开发, 捐赠给Eclipse基金会

> [Officail Site](http://www.eclipse.org/openj9/) | [IBM原文](https://www.ibm.com/support/knowledgecenter/SSYKE2_8.0.0/com.ibm.java.vm.80.doc/docs/j9_intro.html)

- [Github:](https://github.com/eclipse/openj9)

> [参考博客: IBM开源JVM实现OpenJ9，并提交Eclipse基金会托管)](http://www.infoq.com/cn/news/2017/09/IBM-JVM-OpenJ9-Eclipse)
> [参考博客: Eclipse Open J9：Eclipse OMR项目提供的开源JVM](http://www.infoq.com/cn/news/2018/03/OMR-OpenJ9)
