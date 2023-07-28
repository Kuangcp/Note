---
title: Java的集合
date: 2018-11-21 10:56:52
tags: 
    - 数据结构
categories: 
    - Java
---

**目录 start**

1. [JDK中的集合](#jdk中的集合)
    1. [集合继承和实现关系](#集合继承和实现关系)
    1. [Iterator](#iterator)
        1. [规避 ConcurrentModificationException](#规避-concurrentmodificationexception)
    1. [Map](#map)
        1. [HashMap](#hashmap)
        1. [ConcurrentHashMap](#concurrenthashmap)
        1. [TreeMap](#treemap)
    1. [List](#list)
    1. [Set](#set)
1. [第三方开源集合框架](#第三方开源集合框架)
    1. [fastutil](#fastutil)
    1. [Koloboke](#koloboke)
    1. [Trove](#trove)

**目录 end**|_2023-07-28 15:22_|
****************************************
# JDK中的集合

[ Java集合必会14问（精选面试题整理）](https://www.cnblogs.com/wmyskxz/p/9381848.html)

## 集合继承和实现关系

- Collection 接口
    - List 接口  
        - ArrayList
        - LinkedList _也实现了Queue接口_ 双向链表实现
        - Vector
    - Set 接口 _内容不允许重复_
        - SortedSet 接口 _单值排序接口_
            - TreeSet
    - Queue 接口 _队列接口_
        - PiorityQueue

- Map接口
    - HashMap _无序, key不重复_
    - HashTable _无序, key不重复_
    - TreeMap _按key排序, key不重复_
    - IdentityMap _key可重复_
    - WeakHashMap _弱引用Map集合_

## Iterator
> 迭代器

### 规避 ConcurrentModificationException 
1. 使用迭代器进行删除， 或者Java8的removeIf
1. 使用没有这个特性的容器，例如： LinkedBlockingQueue
    1. 关联此特性的容器可以查看 java.util.ConcurrentModificationException 的JavaDoc

************************

## Map
> HashMap 键能为null, HashTable则不可以, 而且HashTable是线程安全的(依靠 synchronized 关键字实现) 

> [参考: Java Map 集合类简介 ](https://www.oracle.com/technetwork/cn/articles/maps1-100947-zhs.html)

### HashMap

### ConcurrentHashMap
> 避免 ConcurrentModificationException 

### TreeMap
> [参考: TreeMap 红黑树算法实现](https://www.ibm.com/developerworks/cn/java/j-lo-tree/index.html)

************************

## List
> interface 

包括的方法有:
![List method](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Java/Collection/List/List.png)

List接口有众多实现, 最常用的 ArrayList LinkedList 

******************************

[stackoverflow: list add then unsupportedoperationexception](https://stackoverflow.com/questions/5755477/java-list-add-unsupportedoperationexception)
> 有时候会使用 Arrays.asList() 或者 Collections.singletonList() 来快速生成 List  
> 但是 这两个生成的实例都是返回 AbstractList 的实现类, 其 add remove 方法是没有实现的, 如果调用了就会抛出异常

```java
    public void add(int index, E element) {
        throw new UnsupportedOperationException();
    }
```
> 这是因为, 这个类设计就是采用的定长数组来实现List, 所以不能对其中元素进行更改 类似的还有 `Collections.emptyXxx()`

******************************************
## Set
- Set是无序的，但是StringRedisTemplate的对象操作返回的set竟然是有序的
    - 因为有一个类是SortSet，顾名思义，所以是有序的，要继续多学习和使用Java原生的集合对象了

> [3分钟搞掂Set集合](https://segmentfault.com/a/1190000014391402?utm_source=channel-hottest)

************************

# 第三方开源集合框架

## fastutil
> [Github](https://github.com/vigna/fastutil)

## Koloboke
> [Github](https://github.com/leventov/Koloboke)

## Trove
> [BitBucket](https://bitbucket.org/trove4j/trove/src/master/)
