---
title: MySQL进阶
date: 2018-12-16 17:26:16
tags: 
    - MySQL
categories: 
    - 数据库
---

**目录 start**
 
1. [MySQL进阶](#mysql进阶)
    1. [事务隔离级别](#事务隔离级别)
    1. [性能调优](#性能调优)
        1. [查看状态变量](#查看状态变量)
    1. [存储引擎](#存储引擎)
        1. [InnoDB](#innodb)
1. [Tips](#tips)
    1. [SQL 片段](#sql-片段)

**目录 end**|_2019-04-29 00:24_|
****************************************
# MySQL进阶

- [Mysql Redis UDF 复制](http://www.cnblogs.com/zhxilin/archive/2016/09/30/5923671.html)

> [参考博客: shell 下执行mysql 命令](http://www.cnblogs.com/wangkangluo1/archive/2012/04/27/2472898.html)

> [参考博客: 轻松理解MYSQL MVCC 实现机制](https://blog.csdn.net/whoamiyang/article/details/51901888#commentBox)  

## 事务隔离级别
> [参考博客: MySQL的四种事务隔离级别](https://www.cnblogs.com/huanongying/p/7021555.html)  

| 事务隔离级别 | 脏读 | 不可重复读 | 幻读
|:---|:---:|:---:|:---:|
| 读未提交（read-uncommitted） | 会 | 会 | 会
| 不可重复读（read-committed） | \ | 会 | 会
| 可重复读（repeatable-read）  | \ | \ | 会
| 串行化（serializable） 	   | \ | \ | \ 


## 性能调优
> [Doc: Optimizing Queries with EXPLAIN](https://dev.mysql.com/doc/refman/5.7/en/using-explain.html)

> [MySQL下INNODB引擎的SELECT COUNT(*)性能优化及思考](http://www.piaoyi.org/database/MySQL-INNODB-SELECT-COUNT.html)

> `set max_execution_time=3000;` (5.7.8 新增) 设置SQL执行最大时间, 超时报错, 单位 ms

> 5.6及以上版本时间类型效率 int > datetime > timestamp

### 查看状态变量
> [ SHOW VARIABLES](https://dev.mysql.com/doc/refman/5.7/en/show-variables.html)  

- 查看所有连接 `show processlist;`
- 查看最大连接数 `show variables like "max_conn%";`
    - 设置最大连接数 `set global max_connections=5000;`

## 存储引擎
### InnoDB
行溢出

*****************************

# Tips
- 将需要执行的SQL写入文件 并将结果输出到文件 `mysql -u root -h 192.168.10.201 -p123 < query.sql  > result.log`

## SQL 片段

1. 删除库下所有表 `select concat('drop table ',table_name,';') from information_schema.TABLES where table_schema='DATABASE_NAME';`
