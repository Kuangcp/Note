---
title: Clickhouse
date: 2023-03-31 09:58:36
tags: 
categories: 
---

💠

- 1. [Clickhouse](#clickhouse)
    - 1.1. [设计](#设计)
    - 1.2. [使用](#使用)
        - 1.2.1. [Explain](#explain)
    - 1.3. [Tips](#tips)
        - 1.3.1. [分布式表业务使用实践](#分布式表业务使用实践)

💠 2024-02-22 14:38:36
****************************************
# Clickhouse 
> [Official Site](https://clickhouse.com)  

> [What is ClickHouse? ](https://medium.com/doublecloud-insights/what-is-clickhouse-a-comprehensive-guide-for-getting-started-5aae9afd38b0)

## 设计


************************

## 使用

### Explain 
> [Clickhouse: Explain](https://clickhouse.com/docs/en/sql-reference/statements/explain)  
> [Using Explain to analyze and improve Clickhouse queries performance](https://medium.com/datadenys/using-explain-to-analyze-and-improve-clickhouse-queries-performance-23dbcdf55a97)  

相比于MySQL的Explain，CK设计Explain能查看更多维度的指标

JSON格式查看 `EXPLAIN json = 1, indexes = 1 SQL`
- 关注最内层的Indexes结构里的 **Initial Parts** 全部块 **Selected Parts** 读取的块 **Initial Granules** 全部粒度 **Selected Granules** 读取的粒度。 读取的指标越小越好，因此表要基于使用情况设计好分区利于查询效率

************************

## Tips
### 分布式表业务使用实践
- 合理使用排序键让数据均匀分布
- 数据大量查询导入导出时
    - [ClickHouse SQL基本语法和导入导出实战](https://cloud.tencent.com/developer/article/1979184)
    - 导出时需要注意传统的 limit offset 会导致结果集 重复和丢失，需要追加 order by 子句

