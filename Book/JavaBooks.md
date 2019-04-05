---
title: JavaBooks.md
date: 2018-11-21 10:56:52
tags: 
categories: 
---

**目录 start**
 
1. [Java书籍](#java书籍)
    1. [书单](#书单)
    1. [视频](#视频)
1. [未读](#未读)
1. [已读](#已读)
    1. [《Effective Java》](#effective-java)
    1. [《Java编程思想》](#java编程思想)
    1. [《深入理解Java虚拟机》](#深入理解java虚拟机)
    1. [《Java程序员修炼之道》](#java程序员修炼之道)
    1. [《Java8实战》](#java8实战)
    1. [《Netty权威指南》](#netty权威指南)

**目录 end**|_2019-04-06 00:10_| [Gitee](https://gitee.com/gin9/Memo) | [Github](https://github.com/Kuangcp/Memo)
****************************************

# Java书籍

- [从 Java 代码到 Java 堆](https://www.ibm.com/developerworks/cn/java/j-codetoheap/) `理解和优化您的应用程序的内存使用`

## 书单
> [程序员必读书单](http://www.cnblogs.com/figure9/p/developer-reading-list.html)
> [参考博客: 一个合格的程序员应该读过哪些书(偏java)](https://www.jb51.net/article/35440.htm)
> [参考博客: 2018 年 Java 程序员必读的十本书](http://blog.jobbole.com/113955/)
> [参考博客: 程序员必读的六本书](https://droidyue.com/blog/2015/07/04/six-books-every-programer-must-read/)
> [参考博客: Java自学书籍Top 10](https://www.jb51.net/article/93337.htm)

## 视频
- [用Java学编程  讲师：翁恺](http://study.163.com/course/introduction.htm?courseId=533006#/courseDetail?tab=1)

# 未读 
- Java 8函数式编程 
- Java测试驱动开发 
- head first Java
- head first 设计模式
- 设计模式 可复用面向对象软件的基础 `四人帮`
- Java核心技术 卷1 基础知识 卷2 高级特性
- 实战java高并发程序设计
- Java Performance: The Definitive Guide: Getting the Most Out of Your Code
大教堂和集市
> [参考博客: 《大教堂和集市》笔记](http://www.ruanyifeng.com/blog/2008/02/notes_on_the_cathedral_and_the_bazaar.html)

- Mybatis 从入门到精通
- 深入实践SpringBoot
- 深入浅出 Mybatis 技术原理与实战
- SpringCloud 与 Docker 微服务架构与实战

深入Java虚拟机(原书第2版) 译者: 曹晓钢 / 蒋靖

《Netty in Action 中译》
> [如何评价《Netty实战》这本书？](https://www.zhihu.com/question/58838575)

# 已读
## 《Effective Java》

## 《Java编程思想》

## 《深入理解Java虚拟机》
> 周志明 第二版

`2019-04-05 22:52:51`
- 确实是一本必读的书, 对JVM大致有了一个整体认知, 但是里面也有错误和过时的地方, 需要在网上搜索和自己实践验证下 
- 因为主要是JDK6 和 7 的内容

- 先阅读了 2 3 4 5 学习了JVM内存管理机制 , 在IDE上实践了JVM参数调优(内存和GC相关)
- 阅读 7 9 了解 类加载
- 接下来需要阅读 10 11 了解编译和运行时一些黑魔法...
- 后期需要阅读 6 8 详细了解字节码, 以及字节码执行逻辑
- 12 13 是并发模块

## 《Java程序员修炼之道》
> Benjamin J.Evans | Martijn Verburg

`2017-08-15 21:14:02`
- 这本书在理论上的讲解的确是挺扎实的，但是案例代码不敢恭维，本来Java就不是脚本语言，多个类的协作很常见，里面的demo都是不事先说明这里的案例
- 引用的这些类源码是什么，干什么的，虽然是很简单的类，基本可以猜出来，那么既然如此，为什么不使用更为简单的，就单个类来讲解这个知识点
- 而且代码又不规范，甚至出现了 l 1 要我去区分，这个是看的书里面第一次看到这样的源码，应试考试题目都没有这样的。。。
`2017-08-27 10:49:46`
- 基本整理完了一遍，有些暂时没有用到的先不去学习，总的来说书挺好，对思想的理解有好处，代码就自己想一个更好，书上源码来自一个项目，不简单明了

## 《Java8实战》
`2018-03-11 14:25:10`
- 开始正式的看这本书, 虽然图书馆有这本书, 也稍微看了下目录, 但是一直没有精读, 看前面的一部分就能看出这是一本不错的书, 讲述了Java8的特性, 以及带来的效率的巨大提升
- 通过学习 Stream 和 Lambda 能够大大提升编码效率

## 《Netty权威指南》
`2018-04-03 09:34:32`
- 版本1和2都有大致的看, 学习到了数据交换协议, 以及Netty的简单使用,
- NIO AIO的学习和使用, Netty封装后, 开发简洁了很多, 使用原生的写法要复杂很多
- 并发的再一次学习和理解, 但还是没有开始动手实践
- Netty自己定义协议栈 还没有学习, 感觉挺有难度
