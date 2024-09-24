---
title: Java中的原子类
date: 2019-06-04 19:44:41
tags: 
categories: 
---

💠

- 1. [UnSafe](#unsafe)
- 2. [CAS](#cas)
- 3. [原子类](#原子类)

💠 2024-09-24 16:47:51
****************************************

> [CAS, Unsafe和原子类详解](https://pdai.tech/md/java/thread/java-thread-x-juc-AtomicInteger.html)

# UnSafe 

Unsafe类使Java语言拥有了类似C语言指针一样操作内存空间的能力, 也随之带来了指针相关问题的风险。

************************

# CAS
CAS的全称为Compare-And-Swap，直译就是对比后交换，是一条CPU的原子指令。  
其作用是让CPU先进行比较两个值是否相等，然后原子地更新某个位置的值，其实现方式是基于硬件平台的汇编指令，JVM只是封装了汇编调用，这便是原子类的核心基础。  
CAS方式为乐观锁，synchronized 为悲观锁。  


> ABA问题
如果一个值原来是A，变成了B，又变成了A，那么使用CAS操作时会直接执行Swap。

解决思路： 
1. 可以加版本号， 1A->2B->3A
1. Java 1.5开始，JDK的Atomic包里提供了一个类 `AtomicStampedReference` 来解决ABA问题, compare值时并比较对象内存引用

> 竞争高时CPU高负载
当并发激烈时 compare操作 大部分情况会失败，无休止的循环将导致CPU使用率飙升。类似的，Disruptor队列核心使用CAS，也有这个问题  

如果JVM能支持处理器提供的pause指令，那么效率会有一定的提升，但是目前JVM无法避免该问题。pause指令有两个作用：  
第一，它可以延迟流水线执行命令(de-pipeline)，使CPU不会消耗过多的执行资源，延迟的时间取决于具体实现的版本，在一些处理器上延迟时间是零；  
第二，它可以避免在退出循环的时候因内存顺序冲突(Memory Order Violation)而引起CPU流水线被清空(CPU Pipeline Flush)，从而提高CPU的执行效率。  

> 只能保证一个共享变量的原子操作

解决思路：从Java 1.5开始，JDK提供了AtomicReference类来保证引用对象之间的原子性，就可以把多个变量打包为一个对象 来进行CAS操作。

************************

# 原子类

> `java.util.concurrent.atomic` 提供适当的原子方法 避免在共享数据上出现竞争危害的方法  
> 使用Java自带的原子类, 可以避免同步锁带来的并发访问性能降低的问题, 减少犯错的机会. 对于 int, long, boolean 等成员变量大量使用原子类
>> 但是使用者必须通过类似 compareAndSet或者set或者与这些操作等价的`原子操作`来保证更新的原子性.

- 常见的操作系统的支持， 他们是非阻塞的（无需线程锁）， 常见的方法是实现序列号机制（和数据库里的序列号机制类似），在`AtomicInteger`或`AtomicLong`上用原子
    - 操作`getAndIncrement()`方法， 并且提供了nextId 方法得到唯一的完全增长的数值
- 注意： 原子类不是相似的类继承而来，所以 AtomicBoolean不能当Boolean用
