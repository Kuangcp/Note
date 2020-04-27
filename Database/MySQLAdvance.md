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
    1. [事务](#事务)
        1. [事务隔离级别](#事务隔离级别)
        1. [事务死锁](#事务死锁)
    1. [性能调优](#性能调优)
        1. [查看状态变量](#查看状态变量)
    1. [存储引擎](#存储引擎)
        1. [InnoDB](#innodb)
1. [Tips](#tips)
    1. [SQL 片段](#sql-片段)

**目录 end**|_2020-04-27 23:42_|
****************************************
# MySQL进阶

- [Mysql Redis UDF 复制](http://www.cnblogs.com/zhxilin/archive/2016/09/30/5923671.html)

> [参考: shell 下执行mysql 命令](http://www.cnblogs.com/wangkangluo1/archive/2012/04/27/2472898.html)

> [参考: 轻松理解MYSQL MVCC 实现机制](https://blog.csdn.net/whoamiyang/article/details/51901888#commentBox)  

## 事务
### 事务隔离级别
> [参考: MySQL的四种事务隔离级别](https://www.cnblogs.com/huanongying/p/7021555.html)  

| 事务隔离级别 | 脏读 | 不可重复读 | 幻读
|:---|:---:|:---:|:---:|
| 读未提交（read-uncommitted） | 会 | 会 | 会
| 提交读（read-committed） | \ | 会 | 会
| 可重复读（repeatable-read）  | \ | \ | 会
| 串行化（serializable） 	   | \ | \ | \ 

### 事务死锁

> [deadlock](https://stackoverflow.com/questions/2332768/how-to-avoid-mysql-deadlock-found-when-trying-to-get-lock-try-restarting-trans)

一个事务里 lock A lock B 另一个事务里 lock B lock A , 这时候两个事务都做了第一步， 然后做第二步会发生死锁

- 在业务层面上比较容易出现的场景 例如
    - 一个事务方法内更新两个用户的数据，一个线程先后更新 A B， 另一个线程 先后更新 B A, 
        - 此时如果能对 A B 做排序按相同的顺序做更新操作即可避免死锁
    - 一个事务方法更新A表 另一个事务方法 更新B表 A B 两个表有外键关联 然后两个方法更新的又恰好是关联的数据，因为 innodb引擎，更新A表也会锁住B表 从而导致死锁

************************

## 性能调优
> [Doc: Optimizing Queries with EXPLAIN](https://dev.mysql.com/doc/refman/5.7/en/using-explain.html)

> [MySQL下INNODB引擎的SELECT COUNT(*)性能优化及思考](http://www.piaoyi.org/database/MySQL-INNODB-SELECT-COUNT.html)

> `set max_execution_time=3000;` (5.7.8 新增) 设置SQL执行最大时间, 超时报错, 单位 ms

> 5.6及以上版本时间类型效率 int > datetime > timestamp

> limit 做分页时 记录上次分页最后一条记录的id使用上where进行过滤 提高性能, 前提id是int自增的

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
