---
title: ClickhouseAdvance
date: 2024-04-26 01:17:19
tags: 
    - Clickhouse
    - OLAP
    - Advanced
categories: 
    - 数据库
---

💠

- 1. [Clickhouse](#clickhouse)
    - 1.1. [设计](#设计)
    - 1.2. [事务](#事务)
    - 1.3. [存算分离](#存算分离)
- 2. [使用实践](#使用实践)
    - 2.1. [写入](#写入)
        - 2.1.1. [同步写入](#同步写入)
    - 2.2. [查询](#查询)
    - 2.3. [监控](#监控)

💠 2026-07-08 16:02:50
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
    - 因此官方在自建一个 `clickhouse-keeper` 替换ZK, 自 21.12 (2021年底) 起已生产就绪

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


## 存算分离

> [ClickHouse 存算分离架构探索 - JuiceFS 博客](https://juicefs.com/zh-cn/blog/solutions/clickhouse-disaggregated-storage-and-compute-practice)  

************************

# 使用实践

> [Getting started with ClickHouse? Here are 13 "Deadly Sins" and how to avoid them](https://clickhouse.com/blog/common-getting-started-issues-with-clickhouse)  

## 写入
> [Bulk Inserts](https://clickhouse.com/docs/en/optimize/bulk-inserts)

- CK应尽量避免高并发小数据量写入, 应用层不好调整的话，可以前置一层Buffer引擎, 将小数据量合并后再写.
    - [ClickHouse连接ZK频繁超时处理案例](https://www.modb.pro/db/159455)`数据小批次频繁写入导致part过多，大幅影响zk的性能`  
- 在使用Datax等同步工具做数据写入时，需要注意写入批次参数`batchSize` 设置10w-100w更好，避免CK做大量小文件的合并从而触发报错 `too many parts`
- 数据同步时，直接往分布式表写是简单的做法
    - 进一步优化是直接写local，手动按分片键拆分上游数据，往不同节点的local写，需要保证数据均衡和完整 
    - 例如整数字段按节点数取余，如果不能达到均匀的分布，可以组合业务字段hash后转整型再按节点数取余
- 数据同步写入分区表时，尽量在写入前做好手动分区,**避免单次数据插入到多个分区**，手动规避数据分布式分发带来的效率开销
    - 因此在一些并发同步的场景下，需要考虑每个数据任务是否使用分片键做的拆分，如果分片键无法保证数据的均匀分布而采用其他字段做拆分分片时
        - 注意CK端容易有写入报错，因为此时每个任务都会涉及到多个分区，zk ck 负载都会高
        - Can't get data for node /clickhouse/table/02/tgysg/xxx/blocks/xxxx: node doesn't exist (No node). (KEEPER_EXCEPTION)
        - ZooKeeper session has been expired.. (NO_ZOOKEEPER) 
- Datax 数据同步写入复制表，ZK负载过大引发报错
    - 类似小数据量写入的做法 在写入复制表前，先从上游写入到CK的非复制表中去，然后再通过CK内部的insert select。实测效率提升100%，原因目前推断为CK内部insert有做优化
-  数据文件方式同步 [百亿级数据同步，如何基于 SeaTunnel 的 ClickHouse 实现？](https://seatunnel.apache.org/zh-CN/blog/2022/05/10/ClickHouse/)`在上游数据端就生成ck的数据文件，然后传输文件，ck服务端attach挂载该文件`  

Spark 解析HDFS数据生成CK file（单个分区做一个gz压缩包，解压入库）完成写入Clickhouse

参考： 

> [Clickhouse写入问题汇总](https://www.cnblogs.com/yisany/p/14275785.html)  

> [How to configure ClickHouse for INSERT performance? ](https://dev.to/shiviyer/how-to-configure-clickhouse-for-insert-performance-4cof)`大批量写入，异步写入，按需取消写入约束，表引擎调优，压缩算法替换，结合监控数据寻找出最合适业务数据的一套配置`  
> [Essential Monitoring Queries - part 1 - INSERT Queries](https://clickhouse.com/blog/monitoring-troubleshooting-insert-queries-clickhouse)  

### 同步写入
注意CK是最终一致性，所以修改不具备事务性，但是在特定业务场景如果需要依赖数据的有限一致性，可以通过设置一些参数值来靠拢

执行的insert SQL后追加 SETTINGS async_insert = 0;
用户级设置 SETTINGS insert_quorum=2;
会话设置：
SET async_insert = 0;  -- 关闭异步写入
SET wait_for_async_insert = 1;  -- 等待写入完成
SET wait_for_insert_timeout = 10;  -- 设置等待超时时间（秒）

缺点：
写入延迟增加，因为需要等待数据落盘
写入吞吐量下降，特别是在高并发场景
可能影响查询性能，因为写入操作会占用更多系统资源

更高的 CPU 使用率
更多的内存占用
更频繁的磁盘 I/O 操作

## 查询
不适合查单行的点查询, 最小查询数据量是索引粒度(index_granularity)的行数, 即使查询一条数据，CK也会按索引粒度加载整块数据进缓存


## 监控
> [查询日志 system.query_log](https://clickhouse.com/docs/zh/operations/system-tables/query_log)  

```sql
-- 查询SQL执行记录
select hostname() hostname
      ,type
      ,query_kind
      ,event_time
      ,databases
      ,user
      ,address 
      ,query_duration_ms
      ,query
      ,exception_code
      ,exception
from clusterAllReplicas('default_cluster', system.query_log) 
where event_date = toDate(now()) and event_time > (now() - toIntervalMinute(300))
    --and query_duration_ms > 40000
    --and user not in('default','industrial_cloud')
    --and has(databases,'linkedsee_new')
      and query like '%user_info_local%'
      and query_kind not in('Select')
order by event_date ,event_time desc
limit 1009
```
