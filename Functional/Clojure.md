---
title: Clojure
date: 2018-11-21 10:56:52
tags: 
    - 基础
    - 函数式编程
categories: 
    - Clojure
---

**目录 start**

1. [Clojure](#clojure)
    1. [安装](#安装)
    1. [基础](#基础)

**目录 end**|_2020-12-18 15:50_|
****************************************
# Clojure
> Lisp的方言 [参考博客 Clojure 学习笔记 :0 零基础教程](https://www.jianshu.com/p/32b7ef3659db)

## 安装
- [Clojure官网下载地址](https://clojure.org/community/downloads)
    - 解压后运行jar包进入REPL `java -cp clojure-1.8.0.jar clojure.main`
- Linux 下推荐 [leiningen](https://leiningen.org/)
    - Arch `yay -S leiningen`

## 基础

Clojure的设计原则可以概括成5个词汇：简单、专注、实用、一致和清晰。这不是我概括的，而是《The joy of clojure》概括的。
（1）简单： 鼓励纯函数，极简的语法（少数special form），个人也认为clojure不能算是多范式的语言（有部分OO特性），为了支持多范式引入的复杂度，我们在C++和Scala身上都看到了。
（2）专注：前缀运算符不需要去考虑优先级，也没有什么菱形继承的问题，动态类型系统（有利有弊），REPL提供的探索式编程方法（告别修改/编译/运行的死循环，所见即所得）。
（3）实用：前面提到，构建在JVM之上，跟Java语言的互操作非常容易。直接调用Java方法，不去发明一套新的调用语法，努力规避Java语言中繁琐的地方(doto,箭头宏等等）。
（4）清晰：纯函数（前面提到），immutable var，immutable数据结构，STM避免锁问题。不可变减少了心智的负担，降低了多线程编程的难度，纯函数也更利于测试和调试。
（5）一致：语法的一致性：例如doseq和for宏类似，都支持destructring,支持相同的guard语句（when,while）。数据结构的一致性：sequence抽象之上的各种高阶函数。

- 命令式语言 Java Groovy Scala都是用一个内存和状态模型，把变量映射到一个内存位置
    - Clojure是将值作为重点，Clojure的值一旦创建就不能修改。变量和值建立映射关系，如果再次赋值，不是修改变量，而是映射到新的值上
    - (def <名称> <值>)

************************

> Hello World

`java -cp clojure-1.8.0.jar clojure.main`进入REPL终端
```clojure
    user => (def hello(fn [] "hello"))
    user => (hello)
```

