---
title: Java实例化对象的几种方式
date: 2020-02-02 18:45:47
tags: 
categories: 
---

💠

- 1. [Java 实例化对象的方式](#java-实例化对象的方式)
    - 1.1. [new](#new)
    - 1.2. [反射](#反射)
    - 1.3. [clone](#clone)
    - 1.4. [反序列化](#反序列化)
    - 1.5. [Unsafe](#unsafe)

💠 2024-06-02 17:50:57
****************************************
# Java 实例化对象的方式
> [Github: 实例代码](https://github.com/kuangcp/JavaBase/blob/master/class/src/test/java/com/github/kuangcp/instantiation/InstantiationAndConstructorTest.java)

> [Java创建对象的五种方式](https://juejin.im/post/5d44530a6fb9a06aed7103bd)

## new
TODO

## 反射
1. 获取Class对象
1. 反射获取构造器方法或者调用 newInstance 方法(实际上是调用空构造器方法) 进行实例化

## clone
需要规避深拷贝问题，默认只复制第一层的成员属性


## 反序列化
TODO 

## Unsafe
**sun.misc.Unsafe** 中提供 `allocateInstance` 方法，仅通过Class对象就可以创建此类的实例对象，而且不需要调用其构造函数、初始化代码、JVM安全检查等。  
它抑制修饰符检测，也就是即使构造器是private修饰的也能通过此方法实例化，只需提类对象即可创建相应的对象。  
由于这种特性，allocateInstance在 java.lang.invoke、Objenesis（提供绕过类构造器的对象生成方式）、Gson（反序列化时用到）中都有相应的应用。
