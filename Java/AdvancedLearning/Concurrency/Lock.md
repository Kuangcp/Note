---
title: Java中的锁
date: 2019-04-22 15:49:53
tags: 
categories: 
    - Java
---

💠

- 1. [Lock](#lock)
- 2. [Lock 接口与 synchronized 对比](#lock-接口与-synchronized-对比)
- 3. [正确使用姿势](#正确使用姿势)
- 4. [ReentrantLock 可重入锁](#reentrantlock-可重入锁)
- 5. [ReentrantReadWriteLock 读写锁](#reentrantreadwritelock-读写锁)
- 6. [StampedLock](#stampedlock)
- 7. [Condition 条件队列](#condition-条件队列)
- 8. [实践要点与坑](#实践要点与坑)

💠 2026-09-16 21:12:57
****************************************
# Lock

> 锁的通用概念（悲观锁/乐观锁、自旋锁、锁升级、死锁四条件、CAS/ABA、分段锁等）见 [并发核心概念与理论](/Skills/Councurrency/Concurrency.md)。  
> 本文聚焦 Java JUC 中 `Lock` 的实践用法；底层队列同步器原理见 [AQS](/Java/AdvancedLearning/Concurrency/AQS.md)。

# Lock 接口与 synchronized 对比

`java.util.concurrent.locks.Lock` 是 JUC 提供的显式锁接口，`synchronized` 是 JVM 内置的隐式锁。

| 能力 | `synchronized` | `Lock` |
|:---|:---|:---|
| 可中断获取 | ❌ 阻塞时无法中断 | ✅ `lockInterruptibly()` |
| 超时获取 | ❌ | ✅ `tryLock(time, unit)` |
| 非阻塞尝试 | ❌ | ✅ `tryLock()` 立即返回 |
| 公平锁 | ❌ 非公平 | ✅ `new ReentrantLock(true)` |
| 多条件队列 | ❌ 只能 `wait/notify` 一个 | ✅ `newCondition()` 多个 |
| 读写分离 | ❌ | ✅ `ReentrantReadWriteLock` / `StampedLock` |
| 自动释放 | ✅ 代码块结束自动释放 | ❌ 必须手动 `unlock()` |

**实践选型原则：**
- 简单互斥、代码块短、不需要超时/中断 → 直接用 `synchronized`（JDK 6+ 有锁升级优化，性能足够）
- 需要 `tryLock` 超时、可中断、公平锁、多个条件变量、读写分离 → 用 `Lock`
- 大量读 + 少量写 → `ReentrantReadWriteLock` 或 `StampedLock`

# 正确使用姿势

```java
Lock lock = new ReentrantLock();
// lock() 不能放在 try 里：如果获取锁失败，进入 catch/finally 会执行错误逻辑
lock.lock();
try {
    // 临界区
} finally {
    lock.unlock();   // 保证释放；之前示例误写成 lock.lock() 会导致锁无法释放
}
```

`unlock()` 必须放在 `finally` 里，否则临界区抛异常会导致锁永远不释放。

# ReentrantLock 可重入锁

- 默认**非公平锁**（吞吐量优先），`new ReentrantLock(true)` 创建**公平锁**（FIFO，避免饥饿但吞吐下降）
- 可重入：同一线程可多次 `lock()`，需对应次数的 `unlock()`

```java
ReentrantLock lock = new ReentrantLock();

public void outer() {
    lock.lock();
    try {
        inner();   // 同一线程重入，不会死锁
    } finally {
        lock.unlock();
    }
}

public void inner() {
    lock.lock();
    try {
        // ...
    } finally {
        lock.unlock();
    }
}
```

> `synchronized` 也是可重入的；可重入锁用 `state` 计数实现（见 AQS）。

# ReentrantReadWriteLock 读写锁

读读共享、读写互斥、写写互斥；读多写少场景提升并发度。

```java
ReentrantReadWriteLock rw = new ReentrantReadWriteLock();
Lock read = rw.readLock();
Lock write = rw.writeLock();

public String get(String key) {
    read.lock();
    try {
        return cache.get(key);
    } finally {
        read.unlock();
    }
}

public void put(String key, String value) {
    write.lock();
    try {
        cache.put(key, value);
    } finally {
        write.unlock();
    }
}
```

**锁降级**（写锁 → 读锁，保证数据一致性后再释放写锁）：

```java
write.lock();
try {
    cache.put(key, value);
    read.lock();      // 先获取读锁
} finally {
    write.unlock();   // 再释放写锁，降级为读锁
}
try {
    return cache.get(key);
} finally {
    read.unlock();
}
```

> 注意：`ReentrantReadWriteLock` 不支持锁升级（持有读锁再拿写锁会死锁）。  
> 写多读少时读锁可能被写线程饿死，可用下面的 `StampedLock` 缓解。

# StampedLock

`StampedLock` 是 JDK 8 引入的读写锁增强版，支持**乐观读**（读时不加锁，读完校验），避免读锁阻塞写锁。

```java
StampedLock sl = new StampedLock();

public double distanceFromOrigin() {
    long stamp = sl.tryOptimisticRead();   // 乐观读，拿 stamp 不加锁
    double x = this.x, y = this.y;
    if (!sl.validate(stamp)) {             // 校验期间是否有写操作
        stamp = sl.readLock();             // 有写，升级为悲观读锁
        try {
            x = this.x;
            y = this.y;
        } finally {
            sl.unlockRead(stamp);
        }
    }
    return Math.sqrt(x * x + y * y);
}

public void move(double dx, double dy) {
    long stamp = sl.writeLock();
    try {
        x += dx;
        y += dy;
    } finally {
        sl.unlockWrite(stamp);
    }
}
```

**坑：**
- `StampedLock` **不可重入**，同一线程重复加锁会死锁
- 不是 `ReentrantReadWriteLock` 的直接替代，写多场景可减少写饥饿
- `validate` 失败后需重新以悲观读锁读取，不能直接用旧值

# Condition 条件队列

`Lock` 的 `newCondition()` 返回 `Condition`，提供类似 `wait/notify` 的等待/唤醒，且一把锁可以有多个条件队列。

```java
Lock lock = new ReentrantLock();
Condition notEmpty = lock.newCondition();
Condition notFull = lock.newCondition();

public void produce(Object item) throws InterruptedException {
    lock.lock();
    try {
        while (queue.size() == MAX) {
            notFull.await();       // 队列满则等待，释放锁
        }
        queue.add(item);
        notEmpty.signal();         // 唤醒一个消费者
    } finally {
        lock.unlock();
    }
}

public Object consume() throws InterruptedException {
    lock.lock();
    try {
        while (queue.isEmpty()) {
            notEmpty.await();
        }
        Object item = queue.remove();
        notFull.signal();
        return item;
    } finally {
        lock.unlock();
    }
}
```

**与 `wait/notify` 对比：**
- `await()` 必须在持有锁时调用，调用后**释放锁**，被唤醒后需**重新获取锁**才返回
- `signal()` 唤醒单个等待线程，`signalAll()` 唤醒全部
- 判断条件必须用 `while` 而不是 `if`（防止虚假唤醒）
- 一把 `ReentrantLock` 可创建多个 `Condition`，比 `synchronized` 单监视器更精细

# 实践要点与坑

1. **`unlock()` 放 `finally`**，`lock()` 放 `try` 外。
2. **`tryLock` 超时防止死锁**：多把锁时用 `tryLock(time)` 获取失败就释放已持有的锁，破坏死锁的「持有并等待」条件（概念见 [并发核心概念与理论](/Skills/Councurrency/Concurrency.md#死锁的四个必要条件与检测预防)）。
3. **公平锁性能差**：非公平锁允许「插队」减少上下文切换；公平锁严格 FIFO，吞吐通常更低，无特殊需求别开。
4. **读写锁不升级**：`ReentrantReadWriteLock` 持读锁再拿写锁会死锁；`StampedLock` 不可重入。
5. **虚拟线程场景**：JDK 24 之前虚拟线程在 `synchronized` 内阻塞会 Pinning（钉死载体线程），建议用 `ReentrantLock` 替代（见 [Java21 虚拟线程](/Java/AdvancedLearning/Release/Java21.md#pinning)）；JDK 24+ 已通过 JEP 491 修复。
6. **优先 `synchronized`**：绝大多数互斥场景 `synchronized` 简洁且足够快，只有明确需要超时/中断/公平/多条件/读写分离时才引入 `Lock`。
7. **实现关系**：`ReentrantLock`、`ReentrantReadWriteLock`、`Semaphore`、`CountDownLatch` 等底层都基于 AQS，理解原理看 [AQS](/Java/AdvancedLearning/Concurrency/AQS.md)。
