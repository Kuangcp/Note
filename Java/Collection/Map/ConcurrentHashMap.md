---
title: ConcurrentHashMap
date: 2025-01-07 09:56:23
tags: 
categories: 
---

💠

- 1. [ConcurrentHashMap](#concurrenthashmap)
    - 1.1. [结构](#结构)
    - 1.2. [构造函数](#构造函数)
    - 1.3. [put](#put)
    - 1.4. [get](#get)
    - 1.5. [remove](#remove)
    - 1.6. [Tips](#tips)
    - 1.7. [ConcurrentHashMap 与 HashMap](#concurrenthashmap-与-hashmap)
        - 1.7.1. [线程安全性](#线程安全性)
        - 1.7.2. [实现机制](#实现机制)
        - 1.7.3. [性能对比](#性能对比)
        - 1.7.4. [其他区别](#其他区别)
    - 1.8. [线程安全机制（JDK 1.8）](#线程安全机制jdk-18)
        - 1.8.1. [CAS操作](#cas操作)
        - 1.8.2. [synchronized锁](#synchronized锁)
        - 1.8.3. [volatile关键字](#volatile关键字)
        - 1.8.4. [扩容机制](#扩容机制)
    - 1.9. [总结](#总结)

💠 2025-12-16 20:28:35
****************************************
# ConcurrentHashMap
> [API: ConcurrentHashMap](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html)


> [参考: ConcurrentHashMap源码分析（JDK8）](https://www.cnblogs.com/zerotomax/p/8687425.html)  
> [参考: Java并发编程：ConcurrentHashMap](https://www.cnblogs.com/dolphin0520/p/3932905.html)

> 注意: JDK1.8 之前使用分段锁（Segment），JDK1.8 之后使用 CAS + synchronized 实现线程安全

## 结构
ConcurrentHashMap的数据结构与HashMap类似，都是数组 + 链表 + 红黑树的结构，但实现了线程安全。

- 修改HashMap，并不需要将整个结构都锁住，只要锁住即将修改的桶（就是单个元素）
    - 好的HashMap 实现，在读取时不需要锁，写入时只要锁住要修改的单个桶 Java能达到这个标准，但是需要程序员去操作底层的细节才能实现
- `ConcurrentHashMap`类 还实现了ConcurrentMap接口，有些提供了还提供了原子操作的新方法
    - `putIfAbsent()` 如果还没有对应键，就把键/值添加进去
    - `remove()` 如果键存在而且值与当前状态相等，则用原子方式移除键值对
    - `replace()` API 为HashMap中原子替换的操作方法提供了两种不同的形式
- key value 均不允许为null

> 1.7 到 1.8 改动
- JDK 1.7: 采用分段锁（Segment）机制，将数据分成多个段，每个段独立加锁
    - JDK 1.8: 采用 CAS + synchronized 机制，锁的粒度更细，只锁住数组中的单个桶（Node）
    - 数据结构：取消了 Segment 分段锁的数据结构，取而代之的是数组+链表+红黑树的结构。
- 保证线程安全机制：JDK1.7 采用Segment 的分段锁机制实现线程安全，其中 Segment 继承自 ReentrantLock 。JDK1.8采用CAS+synchronized保证线程安全。
- 锁的粒度：JDK1.7 是对需要进行数据操作的 Segment 加锁，JDK1.8调整为对每个数组元素加锁（Node）。
- 链表转化为红黑树：定位节点的 hash 算法简化会带来弊端，hash冲突加剧，因此在链表节点数量大于 8（且数据总量大于等于 64）时，会将链表转化为红黑树进行存储。
- 查询时间复杂度：从JDK1.7的遍历链表O(n)， JDK1.8 变成遍历红黑树O(logN)。


![](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Java/Collection/Map/ConcurrentHashMap.png)

************************

ConcurrentHashMap的迭代器是弱一致性(weakly-consistent)的，和 ConcurrentSkipListMap 一样，它不会抛出ConcurrentModificationException异常，但是无法保证迭代器遍历的元素是一个完整的快照。因此，在迭代器遍历时，可能会遗漏或重复遍历某些元素。

> 源码层面怎么做到的
不复制整个数组（不像 CopyOnWrite）；  
不维护 modCount（所以检测不到并发修改）；  
分段推进（Java 8+ 是数组+链表/树，迭代器按 slot 顺序读）；  
遇到被并发搬走的桶 → 直接跳过或读到新值，不会重试。 

## 构造函数
默认初始容量 16 和 默认负载因子 0.75，与HashMap相同。

- 如果手动指定了初始容量，会根据 `tableSizeFor` 方法计算得到一个大于初始容量的最小的2的指数值
- 支持并发级别（concurrencyLevel）参数（JDK 1.7），JDK 1.8 中该参数仅用于兼容性，实际不再使用

## put
> 线程安全的put操作实现

1. 计算key的hash值（与HashMap相同：`(h = key.hashCode()) ^ (h >>> 16)`）；
2. `if` 桶（数组）大小为0，则初始化桶（使用CAS保证线程安全）；
3. `if` 桶中key的下标上没有节点对象，则使用CAS直接插入；
4. `else if` 该位置正在扩容（hash值为MOVED），则帮助扩容；
5. `else` 如果有节点对象
   1. `synchronized` 锁住该桶的头节点；
   2. `if` key的下标上有节点对象且key相同，则替换旧值；
   3. `else if` 有节点对象且为树节点，则调用树节点的putTreeVal()插入key对应的节点对象；
   4. `else` 则遍历桶对应的链表查找key是否存在于链表中；
      1. `if` 找到了对应key的节点，则替换旧值；
      2. `if` 没找到对应key的节点，则尾插法插入节点并判断是否需要树化；
6. 每当插入新节点，则使用CAS更新size并判断是否需要扩容；

**关键点：**
- 使用CAS进行无锁操作（初始化、插入空桶）
- 使用synchronized锁住单个桶，而不是整个Map
- 支持多线程协助扩容（helpTransfer）

## get
> 线程安全的get操作实现

1. 计算key的hash值；
2. 定位到对应的桶；
3. `if` 桶的头节点就是要找的key，直接返回value；
4. `else if` 头节点的hash值小于0（表示正在扩容或为树节点），调用对应的find方法查找；
5. `else` 遍历链表查找对应的key；

**关键点：**
- get操作是无锁的，通过volatile保证可见性
- 支持在扩容过程中进行查找（ForwardingNode）

## remove
> 线程安全的remove操作实现

1. 计算key的hash值；
2. 定位到对应的桶；
3. `synchronized` 锁住该桶的头节点；
4. 查找对应的节点并删除；
5. 如果删除后链表长度小于6，进行反树化；

## Tips
- size/isEmpty 等是弱一致，不能保证瞬时精确


## ConcurrentHashMap 与 HashMap

### 线程安全性
- **HashMap**: 线程不安全，多线程环境下可能出现数据丢失、死循环等问题
- **ConcurrentHashMap**: 线程安全，支持高并发读写操作

### 实现机制
- **HashMap**: 无锁，性能高但不安全
- **ConcurrentHashMap (JDK 1.7)**: 分段锁（Segment），锁粒度较粗
- **ConcurrentHashMap (JDK 1.8)**: CAS + synchronized，锁粒度更细，性能更好

### 性能对比
- **单线程**: HashMap性能略优于ConcurrentHashMap
- **多线程**: ConcurrentHashMap性能远优于HashMap + synchronized

### 其他区别
- ConcurrentHashMap的key和value都不能为null（HashMap允许null）
- ConcurrentHashMap的size()方法返回的是近似值（多线程环境下）
- ConcurrentHashMap支持弱一致性迭代器

## 线程安全机制（JDK 1.8）

### CAS操作
- 用于无锁的初始化、插入空桶等操作
- 使用 `sun.misc.Unsafe` 类提供的CAS方法

### synchronized锁
- 只锁住单个桶（Node），而不是整个Map
- 锁的粒度更细，减少锁竞争

### volatile关键字
- Node的val和next字段使用volatile修饰，保证可见性
- 数组table使用volatile修饰，保证扩容时的可见性

### 扩容机制
- 支持多线程协助扩容（helpTransfer）
- 使用ForwardingNode标记正在扩容的桶
- 扩容时不影响读操作

