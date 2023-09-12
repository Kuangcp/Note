---
title: Java排查手册
date: 2023-08-25 15:51:12
tags: 
categories: 
---

**目录 start**

1. [Troubleshoot](#troubleshoot)
    1. [Memory](#memory)
        1. [GC](#gc)
        1. [Metaspace OOM](#metaspace-oom)
        1. [Compressed Class Space OOM](#compressed-class-space-oom)
    1. [CPU](#cpu)

**目录 end**|_2023-08-28 23:31_|
****************************************
# Troubleshoot

> [troubleshoot memory leak](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/memleaks.html)

## Memory

### GC
> [Java中9种常见的CMS GC问题分析与解决](https://tech.meituan.com/2020/11/12/java-9-cms-gc.html)

> [大量类加载器创建导致诡异FullGC](https://heapdump.cn/article/1924890)


### Metaspace OOM
[一次Metaspace OutOfMemoryError问题排查记录](https://juejin.cn/post/7114516283290288158)`很多GeneratedMethodAccessor类`

原理理解比较复杂，但定位和解决问题会比较简单，经常会出问题的几个点有 Orika 的 classMap、JSON 的 ASMSerializer、Groovy 动态加载类等，基本都集中在反射、Javasisit 字节码增强、CGLIB 动态代理、OSGi 自定义类加载器等的技术点上


https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/memleaks.html


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


## CPU

