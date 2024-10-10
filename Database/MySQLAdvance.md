---
title: MySQL进阶
date: 2018-12-16 17:26:16
tags: 
    - MySQL
categories: 
    - 数据库
---

💠

- 1. [MySQL进阶](#mysql进阶)
    - 1.1. [查询](#查询)
        - 1.1.1. [SQL执行顺序](#sql执行顺序)
        - 1.1.2. [性能优化场景](#性能优化场景)
        - 1.1.3. [条件操作符](#条件操作符)
    - 1.2. [事务](#事务)
        - 1.2.1. [幻读](#幻读)
        - 1.2.2. [事务隔离级别](#事务隔离级别)
        - 1.2.3. [事务死锁](#事务死锁)
        - 1.2.4. [隐含事务](#隐含事务)
    - 1.3. [性能调优](#性能调优)
        - 1.3.1. [Join](#join)
        - 1.3.2. [查看状态变量](#查看状态变量)
    - 1.4. [存储引擎](#存储引擎)
        - 1.4.1. [InnoDB](#innodb)
        - 1.4.2. [MyIsAM](#myisam)
- 2. [Tips](#tips)
    - 2.1. [SQL 片段](#sql-片段)

💠 2024-10-10 10:41:00
****************************************
# MySQL进阶
> [Github: MySQL Sever](https://github.com/mysql/mysql-server)  

> [Mysql 5.7.35 源码解释](https://github.com/shockerli/mysql-annotated-5.7.35)  
> [参考: shell 下执行mysql 命令](http://www.cnblogs.com/wangkangluo1/archive/2012/04/27/2472898.html)  

> [JavaGuide: mysql](https://github.com/Snailclimb/JavaGuide/tree/main/docs/database/mysql)  
> [图解MySQL介绍](https://xiaolincoding.com/mysql/)  

## 查询
> [SQL通用优化方案(where优化、索引优化、分页优化、事务优化、临时表优化)](https://www.cnblogs.com/sochishun/p/7003513.html)  
> [MySQL 索引](/Database/MySQLIndex.md)  

### SQL执行顺序
> [SQL执行顺序（以MySQL为准）](https://segmentfault.com/a/1190000024577490)  

FROM， ON， JOIN，WHERE，GROUP BY，SUM，COUNT，HAVING，SELECT，DISTINCT，ORDER BY，LIMIT  

1. FROM：先去获取from里面的表，拿到对应的数据，生成虚拟表1。
1. ON：对虚拟表1应用ON筛选，符合条件的数据生成虚拟表2。
1. JOIN：根据JOIN的类型去执行相对应的操作，获取对应的数据，生成虚拟表3。
1. WHERE：对虚拟表3的数据进行条件过滤，符合记录的数据生成虚拟表4。
1. GROUP BY：根据group by中的列，对虚拟表4进行数据分组操作，生成虚拟表5。
1. CUBE|ROLLUP（聚合函数使用）：主要是使用相关的聚合函数，生成虚拟表6。
1. HAVING：对虚拟表6的数据过滤，生成虚拟表7，这个过滤是在where中无法完成的，同时count（expr）返回不为NULL的行数，而count（1）和count（*）是会返回包括NULL在内的行数。
1. SELECT：选择指定的列，生成虚拟表8。
1. DISTINCT：数据去重，生成虚拟表9。
1. ORDER BY：对虚拟表9中的数据进行指定列的排序，生成虚拟表10。
1. LIMIT：取出指定行的记录，生成虚拟表11，返回给查询用户。

### 性能优化场景 
> 多字段模糊查询
1. `select * from target where concat(ifnull(host, ''), ifnull(username, '')) like '%localhost%' > 0 limit 0,1;`
    - 将多个字段(空的替换为空串)拼接成一个字符 或 提前拼接为一个新字段， 再模糊查询
2. `select * from target where host like '%localhost%' or username like '%localhost%' limit 0,1;`
    - 这种查询虽然也能实现, 但是性能差一些

> 分页查询性能优化 [MySQL分页查询的性能优化](https://www.cnblogs.com/scotth/p/7995856.html)
- 使用索引降低扫描总行数
- 子查询法
- 只查询索引内字段

1. 尽量少用 select *, 按需查询字段降低IO成本
1. 尽量少用 or，同时尽量用 union all 代替 union

### 条件操作符
> [操作符](https://dev.mysql.com/doc/refman/8.0/en/non-typed-operators.html)

> Tips 
- [in](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_in)
    - in的元素个数太多导致SQL长度超出  max_allowed_packet 参数值的问题
    - 类型强转
    - in 左侧表达式为null 或 右侧集合表达式为null时 该部分运算结果为null
        - `AND id NOT IN (null)` 等价于 `AND id IN (null)` 等价于 `AND NULL` 

************************

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

InnoDB 默认隔离级别为 可重复读

| 事务隔离级别 | 脏读 | 不可重复读 | 幻读 |
|:---|:---:|:---:|:---:|
| 读未提交（read-uncommitted）    | 会 | 会 | 会 |
| 提交读（read-committed）        |   | 会 | 会 |
| 可重复读（repeatable-read）     |   |    | 会 |
| 串行化（serializable） 	      |   |    |   |

需要结合InnoDB引擎具体的锁分析以上隔离级别产生和解决问题的方式

- `脏读` 同一事务内 读取到了其他未提交事务修改后的数据
- `不可重复读` 同一事务内 前后多次读取，数据内容不一致
- `幻读` 同一事务内 前后多次读取，数据总量不一致

************************
InnoDB通过加间隙锁来防止幻读

> 可重复读 问题
1. 当 事务T1, 对事务T2已提交数据A进行了修改，此时数据A 的 trx_id隐藏列就变成了T1事务id 此时 事务 T1 就能查出此条数据

### 事务死锁

> [deadlock](https://stackoverflow.com/questions/2332768/how-to-avoid-mysql-deadlock-found-when-trying-to-get-lock-try-restarting-trans)

一个事务里 lock A lock B 另一个事务里 lock B lock A , 这时候两个事务都做了第一步， 然后做第二步会发生死锁

- 在业务层面上比较容易出现的场景 例如
    - 一个事务方法内更新两个用户的数据，一个线程先后更新 A B， 另一个线程 先后更新 B A, 
        - 此时如果能对 A B 做排序按相同的顺序做更新操作即可避免死锁
    - 一个事务方法更新A表 另一个事务方法 更新B表 A B 两个表有外键关联 然后两个方法更新的又恰好是关联的数据，因为 innodb引擎，更新A表也会锁住B表 从而导致死锁

### 隐含事务
> 以下语句执行时会创建独立事务

- DDL语句，ALTER DATABASE、ALTER EVENT、ALTER PROCEDURE、ALTER TABLE、ALTER VIEW、CREATE TABLE、DROP TABLE、RENAME TABLE、TRUNCATE TABLE等；
- 修改MYSQL架构的语句，CREATE USER、DROP USER、GRANT、RENAME USER、REVOKE、SET PASSWORD；
- 管理语句，ANALYZE TABLE、CACHE INDEX、CHECK TABLE、LOAD INDEX INTO CACHE、OPTIMIZE TABLE、REPAIR TABLE等

需要注意业务逻辑事务中不能包含这些语句，否则无法保证数据一致性，比如在线编辑表单的功能。 但是PG可以实现在同一事务内。

************************

## 性能调优
> [Doc: Optimizing Queries with EXPLAIN](https://dev.mysql.com/doc/refman/5.7/en/using-explain.html)`依据 explain 输出结果调优`

> [MySQL下INNODB引擎的SELECT COUNT(*)性能优化及思考](http://www.piaoyi.org/database/MySQL-INNODB-SELECT-COUNT.html)

> `set max_execution_time=3000;`MySQL服务器设置SQL执行最大时间 (5.7.8 新增), 如果SQL执行超时则报错, 单位 ms

1. 字段在满足业务需求前提下越小越好
1. 使用 JOIN 代替子查询
1. 使用 UNION 代替手动创建临时表
1. 5.6及以上版本，存储`时间类型`时的效率： int > datetime > timestamp
1. limit 做分页时 记录上次分页最后一条记录的id使用上where进行过滤 提高性能, 前提id是int自增的
1. 批量更新 `rewriteBatchedStatements`

> 业务代码层面 `容易被忽视`
1. 减少不必要的SQL交互，例如 多次重复查询
1. 精简SQL大小，避免操作无需操作的字段，例如更新仅更新一个字段，但是SQL写了更新所有字段
1. for循环执行SQL

### Join

> JOIN 的SQL写法
1. LEFT JOIN 左连接,左边为驱动表,右边为被驱动表.
1. RIGHT JOIN 右连接,右边为驱动表,左边为被驱动表.
1. INNER JOIN 内连接, mysql会选择数据量比较小的表作为驱动表，大表作为被驱动表.

可通过EXPLANIN查看SQL语句的执行计划,EXPLANIN分析的第一行的表即是驱动表.

> 尽量**小表驱动大表** 如果反过来则需要连接20w次 `for(20万){    for(20条){}    }`

> [MySQL Explain](/Database/MySQLIndex.md#explain) 中 Extra字段中会提到 MySQL内部使用到的Join类型
- Using join buffer (Block Nested Loop)
- Using join buffer (Batched Key Access)
- Using join buffer (hash join)

[Nested Join Optimization](https://dev.mysql.com/doc/refman/8.0/en/nested-join-optimization.html)

> Join or
- `select apply a left join user b on a.name = b.name or a.addr = b.addr`
    - 改写为 `select apply a left join user b on a.name = b.name left join user c on a.addr = c.addr`
    - 使用到user表字段的地方需要改写判断 b 和 c。

************************

> [我们公司不让开发使用 join 包括 left join,不让用子查询，合理吗？](https://www.v2ex.com/t/678312)
> [业务多表 join，单条 SQL 梭哈一把好还是多次查询在代码整合好](https://www.v2ex.com/t/557498)

************************

### 查看状态变量
> [ SHOW VARIABLES](https://dev.mysql.com/doc/refman/5.7/en/show-variables.html)  

- 查看所有连接 `show processlist;`
- 查看最大连接数 `show variables like "max_conn%";`
    - 设置最大连接数 `set global max_connections=5000;`

************************

## 存储引擎
> [Alternative Storage Engines](https://dev.mysql.com/doc/refman/8.0/en/storage-engines.html)  

### InnoDB
[InnoDB](/Database/MySQLInnodb.md)

### MyIsAM

*****************************

# Tips
- 将需要执行的SQL写入文件 并将结果输出到文件 `mysql -u root -h 192.168.10.201 -p123 < query.sql  > result.log`

- [参考: 自增主键不连续的几种情况](https://cloud.tencent.com/developer/article/1634218)  
    - 事务回滚，插入语句报错，MySQL自增锁优化

- [Percona Doc](https://www.percona.com/) | [DockerHub](https://hub.docker.com/_/percona)

## SQL 片段

1. 删除库下所有表 `select concat('drop table ',table_name,';') from information_schema.TABLES where table_schema='DATABASE_NAME';`

> 统计表和索引的存储占用
```sql
    select table_schema                         as 'DB',
        table_name                              as 'TABLE',
        table_rows                              as 'TOTAL',
        truncate(data_length / 1024 / 1024, 2)  as 'Data MiB',
        truncate(index_length / 1024 / 1024, 2) as 'Index MiB'
    from information_schema.tables
    where table_schema = 'test-db'
    order by data_length desc, index_length desc;
```
注意：table_rows是预估值，和实际值相差40%-50%，实际值需要看count(*), analyze table table_name 可提高近似率，但仍偏差较大
