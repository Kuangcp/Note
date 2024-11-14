---
title: LinkedHashMap
date: 2022-08-09 15:30:22
tags: 
categories: 
    - Java
---

**目录 start**

1. [LinkedHashMap](#linkedhashmap)

**目录 end**|_2022-08-09 15:46_|
****************************************
# LinkedHashMap
> 关键点在于 java.util.LinkedHashMap.Entry

大部分逻辑完全 继承于HashMap， 在Node上引入了两个引用，将key维护为一个双向链表，保证了遍历时key的有序性

> [参考: Java集合之LinkedHashMap](https://www.cnblogs.com/xiaoxi/p/6170590.html)  

利用 LinkedHashMap 实现LRU时可以让自己代码更简化，在访问key时只需要将key remove和put一次就好了，这样迭代map时靠前的元素都是可以被淘汰的。

