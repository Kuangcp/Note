---
title: JavaOOM
date: 2024-03-06 14:09:01
tags: 
categories: 
---

💠

- 1. [OOM](#oom)
    - 1.1. [简单案例](#简单案例)
    - 1.2. [Heap space OOM](#heap-space-oom)
    - 1.3. [Metaspace OOM](#metaspace-oom)
    - 1.4. [Compressed Class Space OOM](#compressed-class-space-oom)
    - 1.5. [Direct Memory OOM](#direct-memory-oom)
    - 1.6. [GC overhead limit exceeded](#gc-overhead-limit-exceeded)
- 2. [分析](#分析)

💠 2024-08-22 11:15:26
****************************************
# OOM 
> 注意OOM并不代表Java进程一定会退出，如果导致OOM的地方能被catch，且泄漏点能随着这次任务的终止而可回收的话，JVM将继续正常运行。  
> [Why JVM can recovery from OOM Java heap space by itself](https://stackoverflow.com/questions/72865015/why-jvm-can-recovery-from-oom-java-heap-space-by-itself)

## 简单案例

例如 
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
************************

## Heap space OOM
异常信息：

java.lang.OutOfMemoryError: Java heap space
java.lang.OutOfMemoryError: Requested array size exceeds VM limit

[Error java.lang.OutOfMemoryError: GC overhead limit exceeded](https://stackoverflow.com/questions/1393486/error-java-lang-outofmemoryerror-gc-overhead-limit-exceeded)`常见于内存缓慢泄漏，GC成本越来越高时`

## Metaspace OOM
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


## Compressed Class Space OOM

## Direct Memory OOM 

[Netty堆外内存泄露排查盛宴](https://tech.meituan.com/2018/10/18/netty-direct-memory-screening.html)


## GC overhead limit exceeded
> [Error java.lang.OutOfMemoryError: GC overhead limit exceeded](https://stackoverflow.com/questions/1393486/error-java-lang-outofmemoryerror-gc-overhead-limit-exceeded)


# 分析
重点是保存现场，获取到问题时间内多维度的信息辅助快速定位，首要是 dump文件 其次是 jstack历史 gc日志 应用日志 监控系统上问题时间段的指标变化情况 等等。

> [由JDK bug引发的线上OOM](http://ifeve.com/%e7%94%b1jdk-bug%e5%bc%95%e5%8f%91%e7%9a%84%e7%ba%bf%e4%b8%8aoom/)
> [Speeding up Java heap dumps with GNU Debugger](https://medium.com/platform-engineer/speeding-up-java-heap-dumps-with-gnu-debugger-c01562e2b8f0)`但是实测更慢，可能和环境有关吧 maybe`

- [jmap](/Java/AdvancedLearning/JvmTool.md#jmap)
- jcmd 1 GC.heap_dump /tmp/docker.hprof

通常使用 jmap或jcmd dump到文件，但是如果JVM已经发生OOM且进程占用CPU很高的情况下jmap会很慢甚至失败（例如attach失败）。
此时可以使用gdb先dump下core，再转为hprof文件。

- ulimit -c unlimited
- gcore pid `core文件可能会很大，800M堆dump出了7G的文件`
- jmap -dump:format=b,file=heap.hprof /path/to/java core.${pid} `该过程是单线程的，会很慢`
