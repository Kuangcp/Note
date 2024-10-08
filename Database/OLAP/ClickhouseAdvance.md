---
title: ClickhouseAdvance
date: 2024-04-26 01:17:19
tags: 
categories: 
---

💠

- 1. [Clickhouse](#clickhouse)
    - 1.1. [设计](#设计)
    - 1.2. [事务](#事务)
- 2. [使用实践](#使用实践)
    - 2.1. [写入](#写入)
    - 2.2. [查询](#查询)
    - 2.3. [监控](#监控)

💠 2024-10-08 11:39:18
****************************************
# Clickhouse

## 设计
官网的介绍为面向OLAP的高性能列式数据库。

> 多主架构
- Ck中数据节点是平等的，没有master/slave之分， 相较于Greenplum等特定主备架构具有更高的可用性
    - 操作请求（查询和DDL）会由客户端决定负载均衡选择一个节点发送指令，选中的这个节点会成为临时的业务协调节点，负责管理指令在集群内的执行
    - 正是多主特性，部署的主节点数等于1时就是单节点模式，同样可以高性能提供查询服务，只是不具备高可用
- **重依赖Zookeeper**，所有节点数据一致性和分布式表，复制表数据的一致性，分片的游标都需要依赖zookeeper管理
    - 当一个集群内创建了大量的分布式表，复制表时（目前使用中发现到了4000+时），如果有高频率的建表/删表DDL，分布式表的数据写入等操作会容易超时，此时的瓶颈是因为ZK的OP/S下降了。
    - 因此官方在计划自建一个 `clickhouse-keeper` 替换ZK

> 列式存储
- OLAP业务具有的一个特性是基于多维度指标的大宽表数据，聚合计算出某些维度指标的结果，如果是行存储，io成本会高于列存储（按需加载列文件）
- 具有更高的压缩率，同列的数据类型是一致的，可以做更有效率的压缩，压缩比率高了以后，就可以cache更多的数据在内存中
    - [Compression in ClickHouse](https://altinity.com/blog/2017-11-21-compression-in-clickhouse)`支持LZ4（快大） Zstd（慢小）`
    - 如果IO是瓶颈（IOPS不够高） Zstd更合适
    - 如果压缩解压逻辑时CPU是瓶颈 LZ4 更合适
    - 如果不差钱 IO和CPU都很强，不压缩最合适


> 索引
- 一级索引: 排序键 主键  物理存储, 用索引粒度 index_granularrity 跳表一样去连接多个块
- 二级索引: 强依赖一级 命中一级情况下才能优化使用到二级. 不像MySQL可以单独命中二级回一级再回表查
    - minmax 表达式按块记录表达式的min max值, 用于加速扫描表达式
    - set 数据去重后存储到索引数据块（有容量限制）

注意：MergeTree 主键索引 允许重复数据

## 事务
> [Transactional (ACID) support](https://clickhouse.com/docs/en/guides/developer/transactional)  

************************

# 使用实践

> [Getting started with ClickHouse? Here are 13 "Deadly Sins" and how to avoid them](https://clickhouse.com/blog/common-getting-started-issues-with-clickhouse)  

## 写入
> [Bulk Inserts](https://clickhouse.com/docs/en/optimize/bulk-inserts)

- CK应尽量避免高并发小数据量写入, 应用层不好调整的话，可以前置一层Buffer引擎, 将小数据量合并后再写.
- 在使用Datax类同步工具做数据写入时，需要注意写入批次参数`batchSize` 设置10w-100w更好，避免CK做大量小文件的合并从而触发报错 `too many parts`
- 数据同步时，直接往分布式表写是简单的做法
    - 进一步优化是直接写local，手动按分片键拆分上游数据，往不同节点的local写，需要保证数据均衡和完整 
    - 例如整数字段按节点数取余，如果不能达到均匀的分布，可以组合业务字段hash后转整型再按节点数取余
- 数据同步写入分区表时，尽量在写入前做好手动分区,避免单次数据插入到多个分区，手动规避数据分布式分发带来的效率开销
    - 因此在一些并发同步的场景下，需要考虑每个数据任务是否使用分片键做的拆分，如果分片键无法保证数据的均匀分布而采用其他字段做拆分分片时
        - 注意CK端容易有写入报错，因为此时每个任务都会涉及到多个分区，zk ck 负载都会高
        - Can't get data for node /clickhouse/table/02/tgysg/xxx/blocks/xxxx: node doesn't exist (No node). (KEEPER_EXCEPTION)
        - ZooKeeper session has been expired.. (NO_ZOOKEEPER) 


> 数据文件方式同步 [百亿级数据同步，如何基于 SeaTunnel 的 ClickHouse 实现？](https://seatunnel.apache.org/zh-CN/blog/2022/05/10/ClickHouse/)`在上游数据端就生成ck的数据文件，然后传输文件，ck服务端attach挂载该文件`  
> [Clickhouse写入问题汇总](https://www.cnblogs.com/yisany/p/14275785.html)  

[ClickHouse连接ZK频繁超时处理案例](https://www.modb.pro/db/159455)`数据小批次频繁写入导致part过多，大幅影响zk的性能`  
> [How to configure ClickHouse for INSERT performance? ](https://dev.to/shiviyer/how-to-configure-clickhouse-for-insert-performance-4cof)`大批量写入，异步写入，按需取消写入约束，表引擎调优，压缩算法替换，结合监控数据寻找出最合适业务数据的一套配置`  
> [Essential Monitoring Queries - part 1 - INSERT Queries](https://clickhouse.com/blog/monitoring-troubleshooting-insert-queries-clickhouse)  

## 查询
不适合查单行的点查询, 最小查询数据量是索引粒度(index_granularity)的行数, 即使查询一条数据，CK也会按索引粒度加载整块数据进缓存


## 监控
> [查询日志 system.query_log](https://clickhouse.com/docs/zh/operations/system-tables/query_log)  

