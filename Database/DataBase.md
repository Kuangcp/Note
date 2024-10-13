---
title: 数据库基础
date: 2018-12-16 17:25:06
tags: 
    - 数据库
    - 工具使用经验
categories: 
    - 数据库
---

💠

- 1. [数据库](#数据库)
    - 1.1. [事务](#事务)
        - 1.1.1. [事务的并发问题](#事务的并发问题)
    - 1.2. [数据库并发控制](#数据库并发控制)
    - 1.3. [SQL 解析&审计](#sql-解析&审计)
        - 1.3.1. [Slow SQL](#slow-sql)
- 2. [关系型和非关系型](#关系型和非关系型)
- 3. [关系型数据库](#关系型数据库)
    - 3.1. [Mysql](#mysql)
    - 3.2. [PolorDB](#polordb)
    - 3.3. [Oracle](#oracle)
    - 3.4. [PostgreSQL](#postgresql)
- 4. [非关系型数据库](#非关系型数据库)
    - 4.1. [Redis](#redis)
    - 4.2. [RocksDB](#rocksdb)
    - 4.3. [LevelDB](#leveldb)
    - 4.4. [MangoDB](#mangodb)
    - 4.5. [GemFire](#gemfire)
- 5. [内置型数据库](#内置型数据库)
    - 5.1. [SQLite](#sqlite)
    - 5.2. [duckdb](#duckdb)
- 6. [关系型数据库设计](#关系型数据库设计)
    - 6.1. [范式](#范式)
        - 6.1.1. [1NF](#1nf)
        - 6.1.2. [2NF](#2nf)
        - 6.1.3. [3NF](#3nf)
        - 6.1.4. [BCNF](#bcnf)
        - 6.1.5. [4NF](#4nf)
    - 6.2. [基本表的设计](#基本表的设计)
        - 6.2.1. [关于主键的设计](#关于主键的设计)
    - 6.3. [视图的设计](#视图的设计)
- 7. [大数据](#大数据)
    - 7.1. [Greenplum](#greenplum)
    - 7.2. [Clickhouse](#clickhouse)
    - 7.3. [TiDB](#tidb)
    - 7.4. [Ignite](#ignite)
- 8. [向量数据库](#向量数据库)
- 9. [图数据库](#图数据库)
- 10. [数据库中间件](#数据库中间件)
- 11. [图形化工具](#图形化工具)

💠 2024-10-13 18:30:08
****************************************
# 数据库
> [码农翻身:爱炫耀的数据库老头儿](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665514001&idx=1&sn=17b72c3e69db6c4277e3045c699b7b6b&chksm=80d67c52b7a1f5446020826841869221873f4578524181384592839d19c4810dc68807117e13&scene=21#wechat_redirect) `事务,undo日志`

> [DB-Engines Ranking](https://db-engines.com/en/ranking) `数据库评分排行`  
> [墨天轮](https://www.modb.pro/)`数据库社区`  

## 事务

> ACID 
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

> [Algorithm for Recovery and Isolation Exploiting Semantics (ARIES)](https://www.geeksforgeeks.org/algorithm-for-recovery-and-isolation-exploiting-semantics-aries/) `事务隔离和恢复算法`

************************

## 数据库并发控制

MySQL: MVCC

## SQL 解析&审计
- [SQL解析在美团的应用](https://tech.meituan.com/2018/05/20/sql-parser-used-in-mtdp.html)
- [美团点评SQL优化工具SQLAdvisor](https://github.com/Meituan-Dianping/SQLAdvisor)
    - [Docker 版本](https://github.com/maxiaolin3366/SQLAdvisor-web)
    - [Blog](https://tech.meituan.com/2017/03/09/sqladvisor-pr.html)
- [see](https://github.com/myide/see) `基于开源组件（Inception & SQLAdvisor & SOAR）的SQL审核&SQL优化的Web平台`

### Slow SQL
> [Getting Help With A Slow Query](https://www.brentozar.com/archive/2009/03/getting-help-with-a-slow-query/)

> [基于代价的慢查询优化建议](https://tech.meituan.com/2022/04/21/slow-query-optimized-advice-driven-by-cost-model.html)

************************

# 关系型和非关系型
> [为什么说SQL正在击败NoSQL，这对数据的未来意味着什么？](http://www.infoq.com/cn/news/2017/10/SQL-NoSQL-mean-what?utm_source=news_about_rdbms&utm_medium=link&utm_campaign=rdbms)

************************

# 关系型数据库
> 代表性: Oracle, MySQL, PostgreSQL, SQL Server

> [List of Relational Database Management Systems (RDBMSs)](https://database.guide/list-of-relational-database-management-systems-rdbms/)  

> [learndb-py](https://github.com/spandanb/learndb-py)

## Mysql
> [MySQL](/Database/MySQL.md)  

## PolorDB
> [Doc](https://help.aliyun.com/product/58609.html)

## Oracle
> [Official Site](https://www.oracle.com/database/)  

## PostgreSQL
> [Official Site](https://www.postgresql.org/)  

************************

# 非关系型数据库
> key-value 数据库: redis memcached   
> 文档数据库: MongoDB  
> 图数据库: Neo4j tugraph-db JanusGraph PG扩展  
> 时序数据库: InfluxDB TSDB  

- [sssdb](https://github.com/ideawu/ssdb) `键值对数据库`

## Redis
> [Redis](/Database/Redis.md)数据类型丰富，单线程纯内存高性能， 且久经考验很稳定

- [Github Tendis](https://github.com/Tencent/Tendis)`兼容Redis访问协议，腾讯开源的存储版，已不维护，商业还有缓存版和混合版`
    - [ Redis vs Tendis：冷热混合存储版架构揭秘 ](https://mp.weixin.qq.com/s/MeYkfOIdnU6LYlsGb24KjQ)  
- [Dragonfly](https://github.com/dragonflydb/dragonfly) 兼容Redis和Memcached的 API,高吞吐量
    - 无共享式架构和VLL的选择，不使用互斥锁或自旋锁的情况下组合原子的多键操作
    - docker run --network=host --ulimit memlock=-1 docker.dragonflydb.io/dragonflydb/dragonfly
    - 虽然宣称更高吞吐量，但是拿[实际应用场景](https://github.com/Kuangcp/GoBase/tree/master/toolbox/countzh)做测试对比发现Redis比Dragonfly消耗资源少且更快
        - 场景为统计字符频率，只高频执行 ZIncrBy 命令（累计执行了337849次，Redis7.0.5 稳定耗时13s 单核30%  Dragonfly 6.2.11稳定耗时19s 等效于单核60%CPU）
- [KeyDB](https://github.com/Snapchat/KeyDB) Redis 的一个高性能分支，专注于多线程、内存效率和高吞吐量


## RocksDB
> [RocksDB](https://github.com/facebook/rocksdb)`FaceBook开源`

## LevelDB
> [Github](https://github.com/google/leveldb)  

> [LedisDB](https://github.com/ledisdb/ledisdb) 基于LevelDB构建Redis协议的数据库实例

## MangoDB
> [MongoDB](/Database/MongoDB.md) 文档性数据库, 混合类型: 关系型非关系型

## GemFire
> 分布式内存数据库 12306 采用的解决方案

************************
# 内置型数据库
> [Github: embedded-database](https://github.com/topics/embedded-database)

## SQLite
> [Official Site](https://sqlite.org/index.html)  

1. 客户端 sqlitebrowser 

常见后缀 
- .db 数据文件 
- .db-wal 是写时日志[WAL](https://www.sqlite.org/wal.html)
- .db-shm 共享内存文件，只包含临时数据。

## duckdb
> [duckdb](https://duckdb.org/)  in-process SQL OLAP Database Management System

可基于CSV，JSON直接建表做数据分析 [CSV Import](https://duckdb.org/docs/data/csv/overview)

************************

# 关系型数据库设计
## 范式
> 范式越高意味着数据冗余更低，表的划分更细，但是在查询数据时需要做大量表连接操作，会严重降低性能

1. 《数据库系统概论》

### 1NF
> 确保每列原子性

数据库表中的所有字段值都是不可分解的原子值

### 2NF
> 在1NF基础上，确保表中的每列都和主键相关，即在一个表中的字段都是仅构成一个实体，不可以把别的实体的字段放进来，会导致插入 删除 修改都很复杂

> 若 R∈1NF 且每一个非主属性完全函数依赖于任何一个候选码 则 R∈2NF

所谓完全依赖是指不能存在仅依赖主关键字一部分的属性，如果存在，那么这个属性和主关键字的这一部分应该分离出来形成一个新的实体，新实体与原实体之间是一对多的关系。为实现区分通常需要为表加上一个列，以存储各个实例的唯一标识。

### 3NF
> 在2NF基础上，任何非主属性不依赖于其它非主属性（在2NF基础上消除传递依赖）, 即引入`外键`

1. 例如 学生成绩表 应该只存学号 课程id 成绩，不应存放学生信息，课程信息，能大大减少数据的冗余
    - 但是实际上为了系统的性能会做部分数据的冗余，例如改动较少的性别姓名等

### BCNF
Boyce-Codd Normal Form（巴斯-科德范式）

> 在3NF基础上，任何非主属性不能对主键子集依赖（在3NF基础上消除对主码子集的依赖）

### 4NF

## 基本表的设计
1. 应尽量避免 字段默认值和业务值发生重叠, 便于后期排查问题，减少一个值的含义
1. 字段应尽量紧凑，达到业务要求的最小设计，利于索引和IO

### 关于主键的设计
> 为了不让数据库成为瓶颈，基本表中连主键的约束都不要了, 全部由后台的代码进行约束处理

- 如果使用的需要高并发，数据库经常迁移，拆分，分布式，使用UUID,GUID，雪花算法等。
- 如果是小型项目，使用整型自增即可，排序方便节约内存

## 视图的设计


************************

# 大数据
## Greenplum
> [Official Site](https://cn.greenplum.org)  

## Clickhouse
> [Clickhouse](/Database/OLAP/Clickhouse.md)

## TiDB
> [Official Doc](https://docs.pingcap.com/zh/)  

## Ignite
> [Github](https://github.com/apache/ignite)

************************
# 向量数据库
- PostgreSQL： 支持向量插件
- [milvus](https://milvus.io/)
- [chroma](https://github.com/chroma-core/chroma)

> [向量数据库｜一文全面了解向量数据库的基本概念、原理、算法、选型](https://cloud.tencent.com/developer/article/2312534)

# 图数据库
> [Note: 图数据库](/Database/Graph.md)  

***********************

# 数据库中间件
> [MyCat：开源分布式数据库中间件](https://www.csdn.net/article/2015-07-16/2825228)

# 图形化工具

- [Mysql-Font](https://github.com/NilsHoyer/MySQL-Front) `连接Mysql的客户端`
- [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL)
- [sqlectron](https://github.com/sqlectron/sqlectron-gui) `简单直观的数据库图形化软件`
- [dbeaver](https://github.com/dbeaver/dbeaver)
    - 配置文件 `/usr/share/dbeaver/dbeaver.ini`
- [dbgate](https://github.com/dbgate/dbgate)
