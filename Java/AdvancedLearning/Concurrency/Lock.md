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
