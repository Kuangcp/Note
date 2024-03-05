---
title: Java问题排查手册
date: 2023-08-25 15:51:12
tags: 
categories: 
---

💠

- 1. [Troubleshoot](#troubleshoot)
    - 1.1. [GC](#gc)
        - 1.1.1. [主要关注指标](#主要关注指标)
    - 1.2. [Memory](#memory)
    - 1.3. [OOM](#oom)
        - 1.3.1. [Heap space OOM](#heap-space-oom)
        - 1.3.2. [Metaspace OOM](#metaspace-oom)
        - 1.3.3. [Compressed Class Space OOM](#compressed-class-space-oom)
        - 1.3.4. [Direct Memory OOM](#direct-memory-oom)
    - 1.4. [CPU](#cpu)
        - 1.4.1. [线程](#线程)
- 2. [常见问题](#常见问题)
    - 2.1. [IDEA调优](#idea调优)
    - 2.2. [FD泄漏： Unable to Open Socket File](#fd泄漏-unable-to-open-socket-file)

💠 2024-03-05 19:05:16
****************************************
# Troubleshoot

> [Oracle: Troubleshoot memory leak](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/memleaks.html)
> [Oracle: General Java Troubleshooting ](https://docs.oracle.com/en/java/javase/11/troubleshoot/general-java-troubleshooting.html)  

> [目前最全的Java服务问题排查套路](https://juejin.cn/post/6844903816379236360)  

排查思路：

- `Delta` 正式环境可复现问题，测试或灰度无法出现，且不能轻易重启正式环境，通过对生产的JVM做各类指标的记录，对比某个业务操作前后或故障前后的指标差异分析出问题的触发点
    - 限制：不能做太影响性能的指标记录和分析
- `Debug` 在测试或灰度环境上可复现问题，可直接Debug接入调试代码，或本地采用高耗能的方式debug分析`抓包，strace，CPU火焰图，等方式`
    - 限制：**可复现**，通常能有这个条件已经能直接通过debug代码就能解决问题了

## GC
> [Java GC](/Java/AdvancedLearning/JvmGC.md)

> [Java中9种常见的CMS GC问题分析与解决](https://tech.meituan.com/2020/11/12/java-9-cms-gc.html)

> [大量类加载器创建导致诡异FullGC](https://heapdump.cn/article/1924890)
> [参考: 译：谁是 JDK8 中最快的 GC](https://club.perfma.com/article/233480)  
> [《沙盘模拟系列》JVM如何调优](https://my.oschina.net/u/4030990/blog/3149182)  
> [深入浅出GC问题排查](https://blog.ysboke.cn/archives/242.html)
> [参考: CMS Deprecated. Next Steps?](https://dzone.com/articles/cms-deprecated-next-steps)  

- [Oracle JDK8 GC调优指南](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/toc.html)
- [Oracle JDK11 GC调优指南](https://docs.oracle.com/en/java/javase/11/gctuning/introduction-garbage-collection-tuning.html)

`工具`
> [gceasy.io](https://gceasy.io)  
> [GCViewer](https://github.com/chewiebug/GCViewer)  

`实践`
> [从实际案例聊聊Java应用的GC优化](https://tech.meituan.com/2017/12/29/jvm-optimize.html)`观察监控指标调整JVM参数： 年轻代 晋升阈值等`


### 主要关注指标
> [garbage-collection-kpi](https://blog.gceasy.io/2016/10/01/garbage-collection-kpi/)`其中FootPrint定义应有误，JVM应指代内存占用而不是CPU资源`

- `延迟（Latency）`： 也可以理解为最大停顿时间，即垃圾收集过程中单次 STW 的最长时间，越短越好，一定程度上可以接受频次的增多，是 GC 技术的主要发展方向。
- `吞吐量（Throughput）`： 应用系统的生命周期内，由于 GC 线程会占用 Mutator 当前可用的 CPU 时钟周期，吞吐量即为 Mutator 有效花费的时间占系统总运行时间的百分比
    - 例如应用系统运行了 100 min，GC 累计耗时 1 min，则系统吞吐量为 99%。
    - 吞吐量优先的垃圾收集器会倾向于接受`单次耗时较长`的停顿，`累计停顿耗时短`的GC策略。
- `内存占用(Footprint)`：

> 以上三者不可兼得，通常兼顾两者舍弃一方。

## Memory 
- [Blog:java优化占用内存的方法(一)](http://blog.csdn.net/zheng0518/article/details/48182437)

- [GC 性能优化 专栏](https://blog.csdn.net/column/details/14851.html)
- [Java调优经验谈](http://www.importnew.com/22336.html)

- [Memory Footprint of A Java Process](https://zhuanlan.zhihu.com/p/158712025)

## OOM 
> 注意OOM并不代表Java进程一定会退出，如果导致OOM的地方能被catch，且泄漏点能随着这次任务的终止而可回收的话，JVM将继续正常运行。  
> [Why JVM can recovery from OOM Java heap space by itself](https://stackoverflow.com/questions/72865015/why-jvm-can-recovery-from-oom-java-heap-space-by-itself)

例如最简单的案例
```java
    public static void main(String[] args) {
        try {
            List<byte[]> data = new ArrayList<>();
            while (true) {
                try {
                    TimeUnit.MILLISECONDS.sleep(100);
                } catch (InterruptedException e) {
                    log.error("", e);
                }
                log.info("size={}", data.size());
                data.add(new byte[1024 * 1024]);
            }
        } catch (Throwable e) {
            log.error("", e);
        }

        while (true) {
            try {
                TimeUnit.MILLISECONDS.sleep(500);
            } catch (InterruptedException e) {
                log.error("", e);
            }
            log.info("do something");
        }
    }
```

又或者常见的SpringMVC服务
```java
    @GetMapping("/oom")
    public String oom() {
        List<byte[]> data = new ArrayList<>();
        while (true) {
            try {
                TimeUnit.MILLISECONDS.sleep(100);
            } catch (InterruptedException e) {
                log.error("", e);
            }
            log.info("size={}", data.size());
            data.add(new byte[1024 * 1024]);
        }
    }
```

注意 `org.springframework.web.servlet.DispatcherServlet` 中的 `doDispatch` catch了Error也包装成了Exception，方便统一异常处理器。  
这只会导致Tomcat的NIO线程终止了这次请求，局部变量 data 就可以回收掉了，整个服务仍正常进行，只是在快要OOM时高频的GC影响了系统的吞吐量而已。

```java
    catch (Exception ex) {
        dispatchException = ex;
    }
    catch (Throwable err) {
        // As of 4.3, we're processing Errors thrown from handler methods as well,
        // making them available for @ExceptionHandler methods and other scenarios.
        dispatchException = new NestedServletException("Handler dispatch failed", err);
    }
```

### Heap space OOM
异常信息：

java.lang.OutOfMemoryError: Java heap space
java.lang.OutOfMemoryError: Requested array size exceeds VM limit

### Metaspace OOM
[一次Metaspace OutOfMemoryError问题排查记录](https://juejin.cn/post/7114516283290288158)`很多GeneratedMethodAccessor类`

原理理解比较复杂，但定位和解决问题会比较简单，经常会出问题的几个点有 Orika 的 classMap、JSON 的 ASMSerializer、Groovy动态加载类等，基本都集中在 反射、Javasisit字节码增强、CGLIB动态代理、OSGi自定义类加载器等技术点上
> [参考: Metaspace 之一：Metaspace整体介绍](https://www.cnblogs.com/duanxz/p/3520829.html)  


https://heapdump.cn/article/1924890
https://heapdump.cn/article/54786?from=pc
https://heapdump.cn/article/2152817

-XX:+TraceClassLoading -XX:+TraceClassUnloading
-verbose:class

https://developer.aliyun.com/article/780535

https://www.mastertheboss.com/java/solving-java-lang-outofmemoryerror-metaspace-error/#google_vignette

https://javakk.com/805.html
https://www.dongcb.com/818.html

https://juejin.cn/post/7114516283290288158


### Compressed Class Space OOM

### Direct Memory OOM 

[Netty堆外内存泄露排查盛宴](https://tech.meituan.com/2018/10/18/netty-direct-memory-screening.html)

************************

## CPU

### 线程
> [jstack.review Analyze java thread dumps](https://jstack.review)

# 常见问题
## IDEA调优
```conf
    -server
    -Xms1700m  # 最小堆
    -Xmx1700m  # 最大堆 配成一样是为了避免扩容
    -XX:MetaspaceSize=350m # 只是一个阈值, 达到该阈值才进行 GC
    -XX:MaxMetaspaceSize=350m # 最大值

    -Xnoclassgc 
    -Xverify:none # 不进行字节码校验
    -XX:+AggressiveOpts # 激进式优化

    -XX:ReservedCodeCacheSize=320m # 编译时代码缓存 IDEA 警告不能低于240M
```

> [参考: Java’s -XX:+AggressiveOpts: Can it slow you down?](https://www.opsian.com/blog/aggressive-opts/)  
> [参考: JVM参数MetaspaceSize的误解 ](https://mp.weixin.qq.com/s/jqfppqqd98DfAJHZhFbmxA?)

## FD泄漏： Unable to Open Socket File
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

- 处理过的案例： [Apache DolphinScheduler V1.3.6 channel 未关闭导致socket泄漏](https://github.com/apache/dolphinscheduler/blob/d21eb7b1809aa513ced920d5d08575502bde8911/dolphinscheduler-server/src/main/java/org/apache/dolphinscheduler/server/worker/processor/TaskCallbackService.java#L156)
    - 单纯从服务器现场看只能看到worker对master建立了大量socket，而且fd的特殊性无法判断socket真实建立时间
    - 从worker和master的内存Dump入手，查看大量的socket（出问题时已4w+）会和哪些对象数量异常增多有关
    - 排查可能异常的对象（优先看Netty和Socket有关的对象），对比上下文代码（优先关注对象创建和销毁处代码），最终定位到泄漏对象为NettyRemoteChannel，以及上述泄漏点
    - 处理方式： remove前先关闭Channel

