---
title: PostgreSQL进阶
date: 2018-12-16 17:28:33
tags: 
    - PostgreSQL
    - Advanced
categories: 
    - 数据库
---

💠

- 1. [PostgreSQL Advance](#postgresql-advance)
- 2. [Query](#query)
    - 2.1. [元数据](#元数据)
    - 2.2. [硬解析和软解析](#硬解析和软解析)
    - 2.3. [PREPARE](#prepare)
    - 2.4. [JOIN](#join)
        - 2.4.1. [JOIN 顺序优化](#join-顺序优化)
        - 2.4.2. [最佳实践](#最佳实践)
        - 2.4.3. [JOIN 类型和策略](#join-类型和策略)
        - 2.4.4. [优化建议](#优化建议)
- 3. [索引](#索引)
- 4. [事务](#事务)
- 5. [集群](#集群)
- 6. [Explain](#explain)

💠 2026-01-13 19:30:54
****************************************
# PostgreSQL Advance

> [Blog: 励志成为postgresql大神](https://www.modb.pro/u/430972)

************************

# Query
## 元数据
```sql
    -- 查询表元数据（唯一性，必填，字段类型）
select a.attname                             as fieldName,
       d.typname                             as type,
       (case
            when atttypmod - 4 > 0 then atttypmod - 4
            else 0
           end)                                 length,

       (case
            when (select count(*)
                  from pg_constraint
                  where conrelid = a.attrelid
                    and conkey[1] = attnum
                    and contype = 'u') > 0 then 'Y'
            else 'N'
           end)                              as un,
       (case
            when a.attnotnull = true then 'Y'
            else 'N'
           end)                              as nullable,
       col_description(a.attrelid, a.attnum) as comment
from pg_attribute a
         left join pg_class c on a.attrelid = c.oid
         left join pg_type d on a.atttypid = d.oid
where attstattarget = -1
  and c.relname = 'table_test'
```

## 硬解析和软解析

## PREPARE
> [PostgreSQL Prepare](https://jdbc.postgresql.org/documentation/server-prepare/)

************************

> 执行计划问题
- [关于PostgreSQL的绑定变量窥视的问题详解](http://www.pgsql.tech/article_103_10000095)
    - PG11及以下的版本 会话参数 prepareThreshold 默认为5 12可以设置plan_cache_mode参数
- [PostgreSQL 硬解析和通用执行计划](https://www.modb.pro/db/48162) `在 Oracle中被称为绑定变量窥视。但 PostgreSQL中并没有这样的定义，更严格地说，PostgreSQL叫custom执行计划和通用执行计划`
- [What are the bennefits of prepareThreshold = 5 in pgjdbc](https://stackoverflow.com/questions/56261410/what-are-the-bennefits-of-preparethreshold-5-in-pgjdbc)

************************

## JOIN

### JOIN 顺序优化

**PostgreSQL vs MySQL 在 JOIN 顺序上的差异：**

1. **PostgreSQL（基于成本的优化器 CBO）**
   - PostgreSQL 使用**基于成本的查询优化器**，会自动分析所有可能的 JOIN 顺序
   - 优化器会考虑：
     - 表的大小（行数、页数）
     - 索引可用性
     - 统计信息（ANALYZE 收集的）
     - 选择性（selectivity）
     - 连接条件的选择性
   - **通常不需要手动调整 JOIN 顺序**，优化器会自动选择最优方案
   - 优化器会尝试多种 JOIN 策略：
     - Nested Loop Join（嵌套循环）
     - Hash Join（哈希连接）
     - Merge Join（归并连接）

2. **MySQL（传统优化器）**
   - MySQL 5.7 及之前版本的优化器相对较弱
   - 通常建议**小表在前，大表在后**（LEFT JOIN 时）
   - MySQL 8.0+ 引入了更好的优化器，但仍可能受 JOIN 顺序影响

### 最佳实践

```sql
-- PostgreSQL 通常不需要关心顺序，优化器会自动优化
SELECT * FROM large_table l
JOIN small_table s ON l.id = s.id;

-- 但如果优化器选择不当，可以通过子查询或 CTE 引导
WITH filtered_large AS (
    SELECT * FROM large_table WHERE condition
)
SELECT * FROM filtered_large l
JOIN small_table s ON l.id = s.id;
```

### JOIN 类型和策略

1. **Nested Loop Join**
   - 适用于：小表驱动大表，有索引支持
   - 成本：O(n*m)，但实际受索引影响

2. **Hash Join**
   - 适用于：没有索引或索引不适用时
   - 过程：先对小表建立哈希表，再扫描大表
   - PostgreSQL 会自动选择较小的表作为哈希表

3. **Merge Join**
   - 适用于：两个表都已排序（有索引或 ORDER BY）
   - 成本：O(n+m)

### 优化建议

1. **确保统计信息最新**
   ```sql
   ANALYZE table_name;  -- 更新统计信息
   ```

2. **检查执行计划**
   ```sql
   EXPLAIN (ANALYZE, BUFFERS) 
   SELECT * FROM large_table l
   JOIN small_table s ON l.id = s.id;
   ```

3. **索引优化**
   - 确保 JOIN 条件列有索引
   - 复合索引可能更有效

4. **配置参数调整**（如需要）
   ```sql
   -- 调整 JOIN 成本估算
   SET join_collapse_limit = 1;  -- 限制优化器重排 JOIN
   SET from_collapse_limit = 1;   -- 限制 FROM 子句重排
   ```

**PostgreSQL 与 MySQL 不同，通常不需要手动调整 JOIN 顺序。**

- PostgreSQL 的优化器会自动选择最优的 JOIN 顺序和策略
- 优化器会考虑表大小、索引、统计信息等因素
- 只有在优化器选择不当的情况下，才需要手动干预（通过子查询、CTE 或配置参数）
- 关键是保持统计信息最新（定期 ANALYZE）和适当的索引

> 参考：
> - [PostgreSQL Query Planning](https://www.postgresql.org/docs/current/planner-optimizer.html)
> - [PostgreSQL Join Strategies](https://www.postgresql.org/docs/current/planner-optimizer.html#planner-join-search)

************************

# 索引
> [Official Doc](https://www.postgresql.org/docs/11/indexes.html)

CREATE INDEX test1_id_index ON test1 (id);

# 事务
MVCC WAL 

************************

# 集群
> [创建数据库集群](http://www.postgres.cn/docs/9.3/creating-cluster.html)  

> [PostgreSQL—集群方案 – Enmalvi](http://www.enmalvi.com/2022/10/28/postgresql-patroni/#shu_ju_ku_ji_qun_fang_an)  

************************

# Explain 
[Official Doc](https://www.postgresql.org/docs/current/sql-explain.html)

TODO 理解
