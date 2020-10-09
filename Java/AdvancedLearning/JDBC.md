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
1. [Tips](#tips)

**目录 end**|_2020-10-09 17:22_|
****************************************
# JDBC
> [码农翻身:JDBC的诞生](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513438&idx=1&sn=2967d595bb7d4ffdd2dacd3ab7501bbd&chksm=80d6799db7a1f08b27dc97650434fb2fc0e2570628945db99d9300a99e52828fd05c42fdb441&scene=21#wechat_redirect)

- 基础的批量操作SQL ` pstmt.executeBatch(); //批量执行`

- 注册 driver
- 创建 connection
- 创建 statement
- 执行获取 Resultset
- 处理返回结果 resultst

Statement 和 PrepareStatement 的区别， 掌握PrepareStatement的主要用法(推荐使用)

## MySQL
> 与MySQL的互操作

- [Java数据类型和MySQL数据类型对应](https://dev.mysql.com/doc/connector-j/5.1/en/connector-j-reference-type-conversions.html)`简单来说就是基本数据类型加上String是有对应的MySQL基本数据类型`

## Java内置数据库Derby
> 在Java11中被移除了
> [Derby](http://db.apache.org/derby/derby_comm.html)


************************

# Tips
> [mysql-connector-java 插入 utf8mb4 字符失败问题处理分析](https://blog.arstercz.com/mysql-connector-java-%e6%8f%92%e5%85%a5-utf8mb4-%e5%ad%97%e7%ac%a6%e5%a4%b1%e8%b4%a5%e9%97%ae%e9%a2%98%e5%a4%84%e7%90%86%e5%88%86%e6%9e%90/)
