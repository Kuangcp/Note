---
title: HashMap
date: 2019-04-16 15:35:58
tags: 
categories: 
    - Java
---

**目录 start**
 
1. [HashMap](#hashmap)
    1. [结构](#结构)
    1. [构造函数](#构造函数)
    1. [put()](#put)
    1. [resize()](#resize)
    1. [get()](#get)
    1. [HashMap 与 HashTable](#hashmap-与-hashtable)
    1. [总结](#总结)
1. [Tips](#tips)

**目录 end**|_2019-04-16 15:36_| [Gitee](https://gitee.com/gin9/Memo) | [Github](https://github.com/Kuangcp/Memo)
****************************************
# HashMap 
> [API: HashMap](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html)

> [参考博客: 死磕 java集合之HashMap源码分析](https://juejin.im/post/5cb163bee51d456e46603dfe#heading-17)  
> [HashMap 实现原理](http://www.importnew.com/27043.html)  
> [HashMap 怎么 hash？又如何 map？](https://my.oschina.net/editorial-story/blog/2396106)  

## 结构 
HashMap的数据结构是 数组(称为bucket)加单链表 (数组是只放一个Node对象, 单链表是为了放通过hash计算得到的index一致的元素包装成的Node对象)

![](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Java/Collection/Map/HashMap.png)

## 构造函数
- 空构造函数: 采用默认初始容量 16 和 默认负载因子 0.75
- 初始容量参数: 采用传入的初始容量, 默认负载因子
- 初始容量, 负载因子参数: 采用传入的两个参数

其中初始容量会根据 tableSizeFor 方法计算得到 大于初始容量的最小的2的指数值 3->4 4->8 ...

## put() 
> 得到 key 的数组下标 `(n - 1) & key 的 hash 值` n 为数组大小

1. 计算key的hash值(先计算hashCode 然后进行 高低位做异或运算 (高16和低16做异或) `(h = key.hashCode()) ^ (h >>> 16)`)；
1. `if` 桶（数组）大小为0，则初始化桶；
1. `if` 桶中key的下标上没有节点对象，则直接插入；
1. `else` 如果有节点对象
    1. `if` key的下标上有节点对象 转 `#` 流程；
    1. `else if` 有节点对象且为树节点，则调用树节点的putTreeVal()插入key对应的节点对象；
    1. `else` 则遍历桶对应的链表查找key是否存在于链表中；
        1. `if` 找到了对应key的节点，则转 `#` 流程；
        1. `if` 没找到对应key的节点，则在链表最后插入一个新节点并判断是否需要树化；
1. 如果插入了新节点，则数量加1并判断是否需要扩容；

- `#` 如果找到了对应key的元素，则判断是否需要替换旧值，并直接返回旧值；

## resize()
1. 如果旧容量大于0，则新容量等于旧容量的2倍，但不超过最大容量2的30次方，新扩容阈值为旧扩容阈值的2倍；
1. 创建一个新容量的桶；
1. 移动元素
    1. `if` 该下标只有一个节点, 就rehash下直接放过去 `newTab[e.hash & (newCap - 1)] = e;`
    1. `if` 该下标上是一个树节点 则打散成两棵树 `((TreeNode<K, V>) e).split(this, newTab, j, oldCap);`
    1. `else` 也就是说这是一个长链表 原链表分化成两个链表，低位链表存储在原来桶的位置，高位链表搬移到原来桶的位置加旧容量的位置；
        - 例如桶的原大小4 , 节点的hash 3、7、11、15 `index = ((4-1) & hash)`
        - 扩容一次 3和11保持不变(因为`hash&oldCap == 0`)， 而 7和15要搬移到`(4-1) & hash + oldCap`中去 

## get()

## HashMap 与 HashTable

- HashMap 是线程不安全的，HashTable 线程安全，因为它在 get、put 方法上加了 synchronized 关键字。
- HashMap 和 HashTable 的 hash 值是不一样的，所在的桶的计算方式也不一样。HashMap 的桶是通过 & 运算符来实现 (tab.length - 1) & hash，
    - 而 HashTable 是通过取余计算，速度更慢（hash & 0x7FFFFFFF) % tab.length （当 tab.length = 2^n 时，因为 HashMap 的数组长度正好都是 2^n，所以两者是等价的）
- HashTable 的 synchronized 是方法级别的，也就是它是在 put() 方法上加的，这也就是说任何一个 put 操作都会使用同一个锁，而实际上不同索引上的元素之间彼此操作不会受到影响；
    - ConcurrentHashMap 相当于是 HashTable 的升级，它也是线程安全的，而且只有在同一个桶上加锁，也就是说只有在多个线程操作同一个数组索引的时候才加锁，极大提高了效率。

## 总结
1. HashMap是一种散列表，采用（数组 + 链表 + 红黑树）的存储结构；
1. HashMap的默认初始容量为16（1<<4），默认装载因子为0.75f，容量总是2的n次方；
1. HashMap扩容时每次容量变为原来的两倍；
1. 当桶的数量小于64时不会进行树化，只会扩容；
1. 当桶的数量大于64且单个桶中元素的数量大于8时，进行树化；
1. 当单个桶中元素数量小于6时，进行反树化；
1. HashMap是非线程安全的容器；
1. HashMap查找添加元素的时间复杂度都为O(1)；

# Tips
> 发生 ConcurrentModificationException 时:
1. 使用 ConcurrentHashMap 替换掉HashMap (推荐)
1. 使用 synchronized 限制迭代或修改方法 

hashmap的实现原理，从负载因子，冲突处理，equals，hashcode一口气讲下来，中间没卡壳儿的。虽然这不是什么太高深的东西，但还是可以感觉得到理论基础特别扎实。好多工作五六年的人解释不清楚equals和hashcode这两个函数在hashmap中干嘛用的。回答模式一般都是先从理论，原理层面把这个问题讲清楚，然后再从最佳实践方面讲一下不同的应用场景会涉及哪些问题，最后是他做过的项目怎么用的。

1.8 解决了扩容死循环的问题 怎么解决的, 线程安全么, 为什么不安全, 除了没有实现锁
