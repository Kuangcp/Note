---
title: JVM
date: 2018-11-21 10:56:52
tags: 
    - JVM
categories: 
    - Java
---

**目录 start**
 
1. [JVM](#jvm)
    1. [JMM](#jmm)
        1. [堆和栈](#堆和栈)
            1. [各种变量分配机制](#各种变量分配机制)
1. [JVM不同实现](#jvm不同实现)
    1. [Hotspot JVM](#hotspot-jvm)
    1. [OpenJ9](#openj9)

**目录 end**|_2019-03-11 23:27_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# JVM
> Oracle 默认采用的是 Hotspot JVM

> [Java Language and Virtual Machine Specifications](https://docs.oracle.com/javase/specs/)

## JMM
> [github:jvm学习仓库](https://github.com/xwjie/jvm)
> [个人博客: JVM归类](https://vinoit.me/tags/jvm/)

### 堆和栈
> [参考博客: Java中堆内存和栈内存详解](http://www.cnblogs.com/whgw/archive/2011/09/29/2194997.html)

从堆和栈的功能和作用来通俗的比较,堆主要用来存放对象的，栈主要是用来执行程序的.

1. 在函数中定义的一些基本类型的变量和对象的引用变量都是在函数的栈内存中分配
    - 当在一段代码块中定义一个变量时，java就在栈中为这个变量分配内存空间，当超过变量的作用域后，java会自动释放掉为该变量分配的内存空间，该内存空间可以立刻被另作他用
1. 堆内存用于存放由new创建的对象和数组。在堆中分配的内存，由java虚拟机自动垃圾回收器来管理。
    - 在堆中分配的内存，由java虚拟机自动垃圾回收器来管理。在堆中产生了一个数组或者对象后，还可以在栈中定义一个特殊的变量
    - 这个变量的取值等于数组或者对象在堆内存中的首地址，在栈中的这个特殊的变量就变成了数组或者对象的引用变量

引用变量是普通变量，定义时在栈中分配内存，引用变量在程序运行到作用域外释放。  
而数组＆对象本身在堆中分配，即使程序运行到使用new产生数组和对象的语句所在地代码块之外，数组和对象本身占用的堆内存也不会被释放  
数组和对象在没有引用变量指向它的时候，才变成垃圾，不能再被使用，但是仍然占着内存，在随后的一个不确定的时间被垃圾回收器释放掉。

堆是应用程序在运行的时候请求操作系统分配给自己内存，由于从操作系统管理的内存分配,所以在分配和销毁时都要占用时间，因此用堆的效率非常低.  
但是堆的优点在于,编译器不必知道要从堆里分配多少存储空间，也不必知道存储的数据要在堆里停留多长的时间,因此,用堆保存数据时会得到更大的灵活性

JVM是基于堆栈的虚拟机.JVM为每个新创建的线程都分配一个堆栈.也就是说,对于一个Java程序来说，它的运行就是通过对堆栈的操作来完成的。  
堆栈以帧为单位保存线程的状态。JVM对堆栈只进行两种操作:以帧为单位的压栈和出栈操作。 

#### 各种变量分配机制
1. `类变量`（static修饰的变量）：在程序加载时系统就为它在堆中开辟了内存，堆中的内存地址存放于栈以便于高速访问。  
    - 生命周期: 从应用进程启动一直到进程停止
2. `实例变量`：当你使用java关键字new的时候，系统在堆中开辟并不一定是连续的空间分配给变量（比如说类实例），然后根据零散的堆内存地址，通过哈希算法换算为一长串数字以表征这个变量在堆中的"物理位置"。 
    - 生命周期: 当实例变量的引用丢失后，将被GC（垃圾回收器）列入可回收“名单”中，但并不是马上就释放堆中内存
3. `局部变量`：局部变量，由声明在某方法，或某代码段里（比如for循环），执行到它的时候在栈中开辟内存
    - 生命周期: 当局部变量一但脱离作用域，内存立即释放

********************************

# JVM不同实现
## Hotspot JVM

## OpenJ9
IBM主导开发, 捐赠给Eclipse基金会
> [Officail Site](http://www.eclipse.org/openj9/) | [IBM原文](https://www.ibm.com/support/knowledgecenter/SSYKE2_8.0.0/com.ibm.java.vm.80.doc/docs/j9_intro.html)

- [Github:](https://github.com/eclipse/openj9)

> [参考博客: IBM开源JVM实现OpenJ9，并提交Eclipse基金会托管)](http://www.infoq.com/cn/news/2017/09/IBM-JVM-OpenJ9-Eclipse)
> [参考博客: Eclipse Open J9：Eclipse OMR项目提供的开源JVM](http://www.infoq.com/cn/news/2018/03/OMR-OpenJ9)
