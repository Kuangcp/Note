---
title: JDBC
date: 2018-12-16 17:28:17
tags: 
categories: 
    - Java
---

**目录 start**
 
1. [JDBC](#jdbc)
    1. [MySQL](#mysql)
    1. [Java内置数据库Derby](#java内置数据库derby)

**目录 end**|_2019-10-19 17:04_|
****************************************
# JDBC
> [码农翻身:JDBC的诞生](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513438&idx=1&sn=2967d595bb7d4ffdd2dacd3ab7501bbd&chksm=80d6799db7a1f08b27dc97650434fb2fc0e2570628945db99d9300a99e52828fd05c42fdb441&scene=21#wechat_redirect)

- 基础的批量操作SQL ` pstmt.executeBatch(); //批量执行`

注册driver
创建 connection
创建 statement
执行获取 Resultset
处理返回结果 resultst

Statement 和 PrepareStatement 的区别， 掌握PrepareStatement的主要用法(推荐使用)

## MySQL
> 与MySQL的互操作

- [Java数据类型和MySQL数据类型对应](https://dev.mysql.com/doc/connector-j/5.1/en/connector-j-reference-type-conversions.html)`简单来说就是基本数据类型加上String是有对应的MySQL基本数据类型`

## Java内置数据库Derby
> 在Java11中被移除了
> [Derby](http://db.apache.org/derby/derby_comm.html)
