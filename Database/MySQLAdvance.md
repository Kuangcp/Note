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
    1. [查询](#查询)
    1. [锁](#锁)
        1. [Innodb](#innodb)
    1. [事务](#事务)
        1. [幻读](#幻读)
        1. [事务隔离级别](#事务隔离级别)
        1. [事务死锁](#事务死锁)
    1. [性能调优](#性能调优)
        1. [查看状态变量](#查看状态变量)
    1. [存储引擎](#存储引擎)
        1. [InnoDB](#innodb)
1. [Tips](#tips)
    1. [SQL 片段](#sql-片段)

**目录 end**|_2020-11-18 00:14_|
****************************************
# MySQL进阶

- [Mysql Redis UDF 复制](http://www.cnblogs.com/zhxilin/archive/2016/09/30/5923671.html)

> [参考: shell 下执行mysql 命令](http://www.cnblogs.com/wangkangluo1/archive/2012/04/27/2472898.html)

> [参考: 轻松理解MYSQL MVCC 实现机制](https://blog.csdn.net/whoamiyang/article/details/51901888#commentBox)  

## 查询
_全字段模糊查询_
1. `select * from target where concat(ifnull(host, ''), ifnull(username, '')) like '%localhost%' > 0 limit 0,1;`
    - 将全字段(空的替换为空串)连接成一个字符再模糊查询, 
2. `select * from target where host like '%localhost%' or username like '%localhost%' limit 0,1;`
    - 这种查询虽然也能实现, 但是性能差一些

- 分页查询性能优化 [MySQL分页查询的性能优化](https://www.cnblogs.com/scotth/p/7995856.html)
    - 尽量使用索引优化扫描行数
    - 子查询法
    - 只读索引方法

## 锁
### Innodb
> [InnoDB Locking](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking.html)

## 事务
- 当前会话隔离级别
    - 查看 select @@tx_isolation;
    - 设置 SET TRANSACTION ISOLATION LEVEL repeatable read;
- 当前系统隔离级别
    - 查看 select @@global.tx_isolation;
    - 设置 set global transaction isolation level repeatable read;

[Doc 隔离级别](https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-isolation-levels.html)

### 幻读
> [Phantom Rows](https://dev.mysql.com/doc/refman/8.0/en/innodb-next-key-locking.html)

### 事务隔离级别
> [参考: MySQL的四种事务隔离级别](https://www.cnblogs.com/huanongying/p/7021555.html)  

| 事务隔离级别 | 脏读 | 不可重复读 | 幻读
|:---|:---:|:---:|:---:|
| 读未提交（read-uncommitted）    | 会 | 会 | 会
| 提交读（read-committed）        |   | 会 | 会
| 可重复读（repeatable-read）     |   |    | 会
| 串行化（serializable） 	      |   |    | 

************************

- InnoDB 默认隔离级别为 可重复读

- InnoDB和Falcon存储引擎通过多版本并发控制(MVCC，Multiversion Concurrency Control)机制(快照读) **部分解决了 可重复读级别的 幻读问题**
    - 但是某种特殊场景下，幻读还是存在: 
    1. 当 事务T1, 对事务T2已提交数据A进行了修改，此时数据A 的 trx_id隐藏列就变成了T1事务id
        - 此时 事务 T1 就能查出此条数据
    1. 事务T1 准备提交id为10的一条数据，但是发现报错，因为别的事务已经提交了这条数据

### 事务死锁

> [deadlock](https://stackoverflow.com/questions/2332768/how-to-avoid-mysql-deadlock-found-when-trying-to-get-lock-try-restarting-trans)

一个事务里 lock A lock B 另一个事务里 lock B lock A , 这时候两个事务都做了第一步， 然后做第二步会发生死锁

- 在业务层面上比较容易出现的场景 例如
    - 一个事务方法内更新两个用户的数据，一个线程先后更新 A B， 另一个线程 先后更新 B A, 
        - 此时如果能对 A B 做排序按相同的顺序做更新操作即可避免死锁
    - 一个事务方法更新A表 另一个事务方法 更新B表 A B 两个表有外键关联 然后两个方法更新的又恰好是关联的数据，因为 innodb引擎，更新A表也会锁住B表 从而导致死锁

************************

## 性能调优
> [Doc: Optimizing Queries with EXPLAIN](https://dev.mysql.com/doc/refman/5.7/en/using-explain.html)`依据 explain 调优`

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

- [参考: 自增主键不连续的几种情况](https://cloud.tencent.com/developer/article/1634218)  
    - 事务回滚，插入语句报错，MySQL自增锁优化

## SQL 片段

1. 删除库下所有表 `select concat('drop table ',table_name,';') from information_schema.TABLES where table_schema='DATABASE_NAME';`
