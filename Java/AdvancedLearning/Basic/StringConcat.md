---
title: StringConcat
date: 2019-04-19 13:04:48
tags: 
categories: 
---

**目录 start**

1. [字符串拼接](#字符串拼接)
    1. [StringBuffer 和 StringBuilder](#stringbuffer-和-stringbuilder)

**目录 end**|_2020-11-25 20:35_|
****************************************
# 字符串拼接

1. 当有少量连接操作时，直接使用 `+` 。
    - 因为如果都是字面量，编译器会直接连接，如果包含变量，编译器会自动替换为 StringBuilder append 方式
1. 当`单线程`下有大量连接操作时，使用 StringBuilder
1. 当`多线程`下有大量连接操作时，使用 StringBuffer

## StringBuffer 和 StringBuilder
> [参考博客](https://blog.csdn.net/rmn190/article/details/1492013)

StringBuffer 是线程安全的, StringBuilder 不是

- 为何在拼接时, StringBuider 会比直接使用String更好(在循环体中)   
    - 因为用 String 会产生大量常量, StringBuilder StringBuffer 都是使用的字符数组来存储内容, 追加仅仅是扩容字符数组(实现在抽象类 AbstractStringBuilder 中)  
    - StringBuilder StringBuffer 都是继承于它, Buffer 和 Builder 区别仅仅是 append 方法上加了 synchronized 关键字

