---
title: StringConcat.md
date: 2019-04-19 13:04:48
tags: 
categories: 
---

**目录 start**
 
1. [字符串拼接](#字符串拼接)
    1. [StringBuffer和StringBuilder](#stringbuffer和stringbuilder)

**目录 end**|_2019-10-19 17:04_|
****************************************
# 字符串拼接

## StringBuffer和StringBuilder
> [参考博客](https://blog.csdn.net/rmn190/article/details/1492013)

StringBuffer 是 线程安全的, StringBuilder 不是

- 为何在拼接时, StringBuider 会比直接使用String更好(在循环体中)   
    - 因为用 String 会产生大量常量, StringBuilder StringBuffer 都是使用的字符数组来存储内容, 追加仅仅是扩容字符数组(实现在抽象类 AbstractStringBuilder 中)  
    - StringBuilder StringBuffer 都是继承于它, Buffer 和 Builder 区别仅仅是 append 方法上加了 synchronized 关键字

