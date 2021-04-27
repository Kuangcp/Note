---
title: Java中的锁
date: 2019-04-22 15:49:53
tags: 
categories: 
    - Java
---

**目录 start**

1. [Lock](#lock)
    1. [队列同步器](#队列同步器)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Lock

```java
    Lock lock = new ReentrantLock();
    // 不能放在 try中, 防止 获取锁失败, 并执行了释放锁
    lock.lock();
    try {

    } finally {
        lock.lock();
    }
```

## 队列同步器

AbstractQueuedSynchronizer 队列同步器, 是构建锁和其他同步组件的基础框架
AQS核心思想是，如果被请求的共享资源空闲，则将当前请求资源的线程设置为有效的工作线程，并且将共享资源设置为锁定状态。如果被请求的共享资源被占用，那么就需要一套线程阻塞等待以及被唤醒时锁分配的机制，这个机制AQS是用CLH队列锁实现的，即将暂时获取不到锁的线程加入到队列中。