---
title: Clickhouse
date: 2023-03-31 09:58:36
tags: 
categories: 
---

💠

- 1. [Clickhouse](#clickhouse)
    - 1.1. [数据类型](#数据类型)
        - 1.1.1. [bitmap](#bitmap)
    - 1.2. [数据库引擎](#数据库引擎)
- 2. [使用](#使用)
    - 2.1. [Java JDBC](#java-jdbc)
- 3. [Explain](#explain)
- 4. [Tips](#tips)
    - 4.1. [分布式表业务使用实践](#分布式表业务使用实践)

💠 2024-04-11 15:54:40
****************************************
# Clickhouse 
> [Official Site](https://clickhouse.com)  

> [What is ClickHouse? ](https://medium.com/doublecloud-insights/what-is-clickhouse-a-comprehensive-guide-for-getting-started-5aae9afd38b0)

************************

## 数据类型
> [ClickHouse Data Types](https://clickhouse.com/docs/en/sql-reference/data-types)

### bitmap
> 并没有这个类型定义，只是在使用过程中有。

位图对象有两种构造方法。一个是由聚合函数groupBitmapState构造的，另一个是由Array Object构造的。同时还可以将位图对象转化为数组对象`bitmapToArray()`。

[Roaring bitmaps](https://github.com/RoaringBitmap/CRoaring)  
[BitMap及其在ClickHouse中的应用](https://zhuanlan.zhihu.com/p/480345952)`CK针对数据的分布情况做了一些优化`  

## 数据库引擎
- Atomic
- MySQL 关联远程库表
- MaterializedMySQL 原生实现MySQL引擎 支持从MySQL全量及增量实时同步
- Lazy
- PostgreSQL
- MaterializedPostgreSQL
- Replicated
- SQLite

************************

# 使用
> [snuba](https://github.com/getsentry/snuba)`Sentry开发， CK的一个查询层`

## Java JDBC
> 实际上是对Http客户端的封装
```java
        Properties properties = new Properties();
        properties.setProperty("socket_keepalive", "true"); //socket_timeout时间由系统设置
        properties.setProperty("auto_discovery", "true"); // 节点自动发现
        properties.setProperty("load_balancing_policy", "roundRobin"); // 负载均衡
        properties.setProperty("health_check_interval", "1000"); // 健康检查间隔(以毫秒为单位)
        properties.setProperty("health_check_query", "select 1"); // 健康检查语句
        properties.setProperty("node_check_interval", "1000"); // 节点检查间隔(以毫秒为单位)
        properties.setProperty("failover", "2"); // 发生故障转移最大次数
        properties.setProperty("retry", "2"); // 故障重试最大次数

        // 客户端负载均衡的方式
        String url = "jdbc:clickhouse://h1:p1,h2:p2,h3:p3,h4:p4/default?socket_timeout=6000000";
        ClickHouseDataSource dataSource = new ClickHouseDataSource(url, properties)
```

# Explain 
> [Clickhouse: Explain](https://clickhouse.com/docs/en/sql-reference/statements/explain)  
> [Using Explain to analyze and improve Clickhouse queries performance](https://medium.com/datadenys/using-explain-to-analyze-and-improve-clickhouse-queries-performance-23dbcdf55a97)  

相比于MySQL的Explain，CK设计Explain能查看更多维度的指标

JSON格式查看 `EXPLAIN json = 1, indexes = 1 SQL`
- 关注最内层的Indexes结构里的 **Initial Parts** 全部块 **Selected Parts** 读取的块 **Initial Granules** 全部粒度 **Selected Granules** 读取的粒度。 读取的指标越小越好，因此表要基于使用情况设计好分区利于查询效率

************************

# Tips
## 分布式表业务使用实践
- 合理使用排序键让数据均匀分布
- 数据大量查询导入导出时
    - [ClickHouse SQL基本语法和导入导出实战](https://cloud.tencent.com/developer/article/1979184)
    - 导出时需要注意传统的 limit offset 会导致结果集 重复和丢失，需要追加 order by 子句

