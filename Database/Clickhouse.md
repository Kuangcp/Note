---
title: Clickhouse
date: 2023-03-31 09:58:36
tags: 
categories: 
---

**目录 start**

1. [Clickhouse](#clickhouse)
    1. [设计](#设计)
    1. [Tips](#tips)
        1. [分布式表业务使用实践](#分布式表业务使用实践)

**目录 end**|_2023-09-22 09:52_|
****************************************
# Clickhouse 
> [Official Site](https://clickhouse.com)  

## 设计

## Tips
### 分布式表业务使用实践
- 合理使用排序键让数据均匀分布
- 数据大量查询导入导出时
    - [ClickHouse SQL基本语法和导入导出实战](https://cloud.tencent.com/developer/article/1979184)
    - 导出时需要注意传统的 limit offset 会导致结果集 重复和丢失，需要追加 order by 子句

