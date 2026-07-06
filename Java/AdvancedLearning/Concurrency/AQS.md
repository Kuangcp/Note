---
title: AQS
date: 2024-11-10 14:31:25
tags: 
categories: 
---

💠

- 1. [概述](#概述)
- 2. [核心设计](#核心设计)
    - 2.1. [核心三要素](#核心三要素)
    - 2.2. [两种同步模式](#两种同步模式)
- 3. [Node 节点](#node-节点)
- 4. [核心方法](#核心方法)
    - 4.1. [独占式](#独占式)
    - 4.2. [共享式](#共享式)
    - 4.3. [获取流程](#获取流程)
    - 4.4. [释放流程](#释放流程)
- 5. [Condition 条件队列](#condition-条件队列)
- 6. [常见实现](#常见实现)

💠 2026-07-06 20:05:27
****************************************
# 概述

AQS（AbstractQueuedSynchronizer）是 JUC 包的核心骨架，提供基于 **FIFO 队列** 的同步器框架。通过模板方法模式，子类只需实现少量同步原语，即可构建各种同步组件。

> [The java.util.concurrent Synchronizer Framework: Doug Lea](https://gee.cs.oswego.edu/dl/papers/aqs.pdf)  
> [中文翻译版](http://ifeve.com/aqs/)  
> [35张图深入理解 AQS](https://www.cnblogs.com/wang-meng/p/12816829.html)

# 核心设计

## 核心三要素

| 要素 | 说明 |
|------|------|
| **state** | volatile int，表示同步状态（锁是否被持有、许可数量等） |
| **CLH 队列** | 变体 CLH 锁队列，双向链表，存放等待线程 |
| **Condition 队列** | 单向链表，用于条件等待/通知 |

```java
private volatile int state;          // 同步状态
private transient volatile Node head; // 队列头（持有锁的线程已出队）
private transient volatile Node tail; // 队列尾
```

## 两种同步模式

- **独占模式（Exclusive）**：同一时刻只有一个线程能获取资源（ReentrantLock）
- **共享模式（Shared）**：多个线程可以同时获取（Semaphore、CountDownLatch）

# Node 节点

CLH 队列中的节点，封装等待线程及其状态。

```java
static final class Node {
    static final Node SHARED = new Node();   // 共享模式标记
    static final Node EXCLUSIVE = null;      // 独占模式标记

    static final int CANCELLED =  1; // 取消
    static final int SIGNAL    = -1; // 后继节点需要唤醒
    static final int CONDITION = -2; // 在条件队列中等待
    static final int PROPAGATE = -3; // 共享模式下传播唤醒

    volatile int waitStatus;
    volatile Node prev;
    volatile Node next;
    volatile Thread thread;
    Node nextWaiter; // 条件队列的下一个节点
}
```

# 核心方法

## 独占式

| 方法 | 说明 |
|------|------|
| `acquire(int)` | 独占获取，忽略中断 |
| `acquireInterruptibly(int)` | 独占获取，响应中断 |
| `release(int)` | 独占释放 |
| `tryAcquire(int)` | **子类实现**的获取尝试 |
| `tryRelease(int)` | **子类实现**的释放尝试 |

## 共享式

| 方法 | 说明 |
|------|------|
| `acquireShared(int)` | 共享获取，忽略中断 |
| `acquireSharedInterruptibly(int)` | 共享获取，响应中断 |
| `releaseShared(int)` | 共享释放 |
| `tryAcquireShared(int)` | **子类实现**的共享获取尝试 |
| `tryReleaseShared(int)` | **子类实现**的共享释放尝试 |

## 获取流程

```
acquire() -> tryAcquire()                     (子类：快速尝试)
  ├── 成功 -> 直接返回
  └── 失败 -> addWaiter() + acquireQueued()   (入队 + 自旋等待)
```

## 释放流程

```
release() -> tryRelease()      (子类：释放资源)
  ├── 成功 -> unparkSuccessor() (唤醒后继节点)
  └── 失败 -> 返回 false
```

# Condition 条件队列

```java
public class ConditionObject implements Condition {
    private transient Node firstWaiter; // 条件队列头
    private transient Node lastWaiter;  // 条件队列尾
}
```

| 方法 | 行为 |
|------|------|
| `await()` | 释放锁，进入条件队列阻塞，直到被 signal |
| `signal()` | 将条件队列头节点移入 CLH 同步队列 |
| `signalAll()` | 将所有条件队列节点移入 CLH 同步队列 |

**注意**：调用 `await/signal` 前必须先持有锁（必须在 lock/unlock 之间使用）。

# 常见实现

| 同步器 | 同步模式 | AQS 实现思路 |
|--------|----------|-------------|
| **ReentrantLock** | 独占 | state=0 未锁定；state>0 锁定，可重入时递增 |
| **Semaphore** | 共享 | state 表示剩余许可数 |
| **CountDownLatch** | 共享 | state 为计数值，减到 0 时释放所有等待线程 |
| **ReentrantReadWriteLock** | 独占+共享 | state 高16位=读锁，低16位=写锁 |
| **CyclicBarrier** | — | 未直接使用 AQS（用 ReentrantLock + Condition） |
| **ThreadPoolExecutor.Worker** | 独占 | 用 AQS 实现工作线程的 runState |