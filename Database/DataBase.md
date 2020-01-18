---
title: 数据库基础
date: 2018-12-16 17:25:06
tags: 
    - 数据库
    - 工具使用经验
categories: 
    - 数据库
---

**目录 start**
 
1. [数据库](#数据库)
    1. [事务](#事务)
        1. [事务的并发问题](#事务的并发问题)
    1. [数据库并发控制](#数据库并发控制)
1. [关系型数据库](#关系型数据库)
    1. [SQLite](#sqlite)
    1. [SQL Server](#sql-server)
    1. [Mysql](#mysql)
    1. [Oracle](#oracle)
    1. [PostgreSQL](#postgresql)
1. [非关系型数据库](#非关系型数据库)
    1. [Redis](#redis)
    1. [LevelDB](#leveldb)
    1. [MangoDB](#mangodb)
    1. [GemFire](#gemfire)
1. [两者的对比](#两者的对比)
1. [关系型数据库设计](#关系型数据库设计)
    1. [基本表的设计](#基本表的设计)
        1. [关于主键的设计](#关于主键的设计)
    1. [视图的设计](#视图的设计)
1. [非关系型数据库设计](#非关系型数据库设计)
1. [数据库中间件](#数据库中间件)

**目录 end**|_2020-01-19 00:19_|
****************************************
# 数据库
> [码农翻身:爱炫耀的数据库老头儿](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665514001&idx=1&sn=17b72c3e69db6c4277e3045c699b7b6b&chksm=80d67c52b7a1f5446020826841869221873f4578524181384592839d19c4810dc68807117e13&scene=21#wechat_redirect) `事务,undo日志`

> [DB-Engines Ranking](https://db-engines.com/en/ranking) `数据库评分排行`

## 事务 

1. `原子性（Atomicity）`
    - 事务开始后所有操作，要么全部做完，要么全部不做，不可能停滞在中间环节。
    - 事务执行过程中出错，会回滚到事务开始前的状态，所有的操作就像没有发生一样。也就是说事务是一个不可分割的整体，就像化学中学过的原子，是物质构成的基本单位。
1. `一致性（Consistency）`
    - 事务开始前和结束后，数据库的完整性约束没有被破坏 。比如A向B转账，不可能A扣了钱，B却没收到。
1. `隔离性（Isolation）`
    - 同一时间，只允许一个事务请求同一数据，不同的事务之间彼此没有任何干扰。比如A正在从一张银行卡中取钱，在A取钱的过程结束前，B不能向这张卡转账。
1. `持久性（Durability）`
    - 事务完成后，事务对数据库的所有更新将被保存到数据库，不能回滚。

### 事务的并发问题
1. `脏读`
    - 事务A读取了事务B更新的数据，然后B回滚操作，那么A读取到的数据是脏数据
1. `不可重复读`
    - 事务 A 多次读取同一数据，事务 B 在事务A多次读取的过程中，对数据作了更新并提交，导致事务A多次读取同一数据时，结果 不一致。
1. `幻读`
    - 系统管理员A将数据库中所有学生的成绩从具体分数值改为ABCDE等级，但是系统管理员B就在这个时候插入了一条具体分数的记录
    - 当系统管理员A改结束后发现还有一条记录没有改过来，就好像发生了幻觉一样，这就叫幻读。

> 小结：不可重复读的和幻读很容易混淆，不可重复读侧重于`修改`，幻读侧重于`新增或删除`。解决不可重复读的问题只需`锁住满足条件的行`，解决幻读需要`锁表`

## 数据库并发控制

MVCC

************************

# 关系型数据库
> 代表性: Oracle MySQL PostgreSQL SQL Server

> [List of Relational Database Management Systems (RDBMSs)](https://database.guide/list-of-relational-database-management-systems-rdbms/)  

## SQLite
> [Official Site](https://sqlite.org/index.html)  

## SQL Server

## Mysql
> 结合docker配置很快，就是默认编码是latin 每次要改成 utf8mb4

## Oracle
> [Official Site](https://www.oracle.com/database/)  

> 十分的庞大, 学习了他理念的设计, 感受良多

## PostgreSQL
> [Official Site](https://www.postgresql.org/)  

************************

# 非关系型数据库
> key-value 数据库: redis memcached   
> 文档数据库: MongoDB  
> 图数据库: Neo4j  
> 时序数据库: InfluxDB TSDB  

## Redis
> 数据类型丰富,处理非关系型并且结构化的数据十分方便, 结合Python使用就行云流水一般了

## LevelDB
> [Github](https://github.com/google/leveldb)  

## MangoDB
> 文档性数据库, 混合类型: 关系型非关系型

## GemFire
> 分布式内存数据库 12306 采用的解决方案

# 两者的对比
> [为什么说SQL正在击败NoSQL，这对数据的未来意味着什么？](http://www.infoq.com/cn/news/2017/10/SQL-NoSQL-mean-what?utm_source=news_about_rdbms&utm_medium=link&utm_campaign=rdbms)

***********************

# 关系型数据库设计
## 基本表的设计
### 关于主键的设计
> 我哥提出, 基本表中连主键的约束都不要了, 全部由后台的代码进行约束处理

- 如果使用的需要高并发，数据库经常迁移，拆分，分布式，使用UUID,GUID最佳
- 如果是小型项目，使用整型自增即可，排序方便节约内存

## 视图的设计

************************

# 非关系型数据库设计

************************

# 数据库中间件
> [MyCat：开源分布式数据库中间件](https://www.csdn.net/article/2015-07-16/2825228)

