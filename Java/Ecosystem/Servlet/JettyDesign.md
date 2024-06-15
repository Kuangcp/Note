---
title: JettyDesign
date: 2024-06-15 11:01:15
tags: 
categories: 
---

💠

- 1. [Jetty Design](#jetty-design)
    - 1.1. [宏观架构](#宏观架构)
    - 1.2. [线程模型](#线程模型)

💠 2024-06-15 11:05:37
****************************************
# Jetty Design
> [Github: Jetty](https://github.com/jetty/jetty.project)

## 宏观架构

## 线程模型

从抽象来看三者关系如下

![](/Java/Ecosystem/Servlet/img/001-jetty-selector.drawio.svg)

但是由 ExecutionStrategy接口的实现来提供三者在运行时的多种组合方式 [strategy源码](https://github.com/jetty/jetty.project/tree/jetty-12.0.x/jetty-core/jetty-util/src/main/java/org/eclipse/jetty/util/thread/strategy)

> ProduceConsume

一个线程顺序读请求和执行业务，即所有IO数据处理Connector和Handler 用的是一个线程（线程池里只有一个线程），实际上缺点很明显吞吐量不高

> ProduceExecuteConsume

一个线程顺序读，线程池执行业务，类似于单Reactor多线程模型。

> ExecuteProduceConsume

相较于传统的[NIO Reactor](/Skills/CS/IO.md#Reactor)多Reactor多线程模型，主要的区别是 Connector和Handler在一个事件触发后是在同一个线程执行。  
好处是IO接收的数据无需传递和线程上下文切换，充分利用CPU缓存，弊端是如果业务逻辑Handler阻塞或CPU计算消耗很长时间就会快速耗尽线程池线程，然后导致Connetcor没有线程资源执行，从而引发请求积压和拒绝。

************************

Jetty实际运行时采用的是 EatWhatYouKill 策略， 线程池线程充足时采用ExecuteProduceConsume和低线程资源时采用ProduceExecuteConsume，为了避免低线程资源情况时的请求拒绝问题，将请求积压起来等线程池平稳的消费执行完。


