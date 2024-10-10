---
title: Python Concurrency
date: 2018-12-13 16:00:40
tags: 
    - Concurrency
categories: 
    - Python
---

💠

- 1. [Concurrency](#concurrency)
    - 1.1. [GIL](#gil)
    - 1.2. [协程 asyncio](#协程-asyncio)
    - 1.3. [多线程 threading](#多线程-threading)
    - 1.4. [多进程 multiprocessing](#多进程-multiprocessing)
- 2. [实践](#实践)
    - 2.1. [Ray](#ray)

💠 2024-10-10 10:41:00
****************************************
# Concurrency

Python中的并发编程可大致分为： 协程，多线程，多进程

协程Coroutine(asyncio)
- 优点： 任务单元和内核线程数是多对多关系，任务调度是用户态级别，线程切换开销小
- 缺点： 相比于同步式需要换成异步的写法，现有的库支持不完善
- 适用场景： 海量IO密集型任务

多线程Thread(threading)
- 优点： 任务单元和实际内核线程绑定，同步代码换成多线程实现时调整小，无须依赖的库做调整`只能说相对小，比如多线程里日志问题`
- 缺点： 相比协程有更大的线程切换开销，相比进程更轻量，GIL的存在导致只能实现并发而不是并行
- 适用场景： 大量IO密集型任务

多进程Process(multiprocessing)
- 优点：多核并行计算，同步代码换成多进程时调整中等，无须依赖库调整，但需要全局考虑存在进程内数据共享的场景不支持
- 缺点：资源占用重，应用数据共享时需要使用到进程间通信
- 适用场景： CPU密集型任务

通常来说
- IO绑定的场景适用 协程和多线程（存在GIL），例如用户输入，数据库，文件，网络；
- CPU绑定的场景适用多进程，例如 矩阵乘法，搜索，加解密，正则匹配，图像处理

## GIL 
> [What Is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)  
> [Python的GIL是什么鬼，多线程性能究竟如何](http://cenalulu.github.io/python/gil-in-python/)`讲解了GIL以及使用其他并发库`  
> [Celery](https://docs.celeryq.dev/en/stable/)  

简单来说，GIL在早期将C的库集成入Python时，GIL的存在使得应用开发无须考虑并发安全问题，也就无须考虑锁的开销，单线程的性能也很高。
而且Python有多种解释器实现，只有CPython中有GIL

## 协程 asyncio


## 多线程 threading
创建并绑定操作系统的内核线程，但是无法像Java，Go那样并行执行，每个线程在执行前都需要获取GIL锁，即至多只有一个线程能使用CPU计算。


思考： 如何实现像Java一样完备的状态管理和异常管理。 如何实现线程池，如何实现生产者消费者队列加多线程。

## 多进程 multiprocessing

************************

# 实践
## Ray
分布式多进程框架
