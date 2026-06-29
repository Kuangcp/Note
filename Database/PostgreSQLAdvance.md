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
        - 2.4.2. [JOIN 类型和策略](#join-类型和策略)
        - 2.4.3. [JOIN 最佳实践](#join-最佳实践)
- 3. [索引](#索引)
- 4. [事务](#事务)
    - 4.1. [MVCC (Multi-Version Concurrency Control)](#mvcc-multi-version-concurrency-control)
        - 4.1.1. [核心数据结构](#核心数据结构)
        - 4.1.2. [实现原理](#实现原理)
        - 4.1.3. [可见性判断规则](#可见性判断规则)
        - 4.1.4. [事务隔离级别](#事务隔离级别)
        - 4.1.5. [优缺点](#优缺点)
        - 4.1.6. [关键配置](#关键配置)
    - 4.2. [WAL (Write-Ahead Logging)](#wal-write-ahead-logging)
        - 4.2.1. [核心原则](#核心原则)
        - 4.2.2. [写入流程](#写入流程)
        - 4.2.3. [WAL 记录结构](#wal-记录结构)
        - 4.2.4. [LSN 与数据页的关系](#lsn-与数据页的关系)
        - 4.2.5. [Checkpoint](#checkpoint)
        - 4.2.6. [崩溃恢复流程](#崩溃恢复流程)
        - 4.2.7. [WAL 的额外用途](#wal-的额外用途)
        - 4.2.8. [关键配置](#关键配置)
        - 4.2.9. [WAL Segment 文件](#wal-segment-文件)
- 5. [集群](#集群)
- 6. [Explain](#explain)
    - 6.1. [基本语法](#基本语法)
    - 6.2. [关键信息](#关键信息)
        - 6.2.1. [1. 成本估算（Cost）](#1-成本估算cost)
        - 6.2.2. [2. 实际执行时间（ANALYZE）](#2-实际执行时间analyze)
        - 6.2.3. [3. 缓冲区使用（BUFFERS）](#3-缓冲区使用buffers)
        - 6.2.4. [4. 扫描类型（Scan Type）](#4-扫描类型scan-type)
            - 6.2.4.1. [Seq Scan（顺序扫描）](#seq-scan顺序扫描)
            - 6.2.4.2. [Index Scan（索引扫描）](#index-scan索引扫描)
            - 6.2.4.3. [Index Only Scan（仅索引扫描）](#index-only-scan仅索引扫描)
            - 6.2.4.4. [Bitmap Index Scan + Bitmap Heap Scan](#bitmap-index-scan--bitmap-heap-scan)
        - 6.2.5. [5. JOIN类型](#5-join类型)
            - 6.2.5.1. [Nested Loop（嵌套循环）](#nested-loop嵌套循环)
            - 6.2.5.2. [Hash Join（哈希连接）](#hash-join哈希连接)
            - 6.2.5.3. [Merge Join（归并连接）](#merge-join归并连接)
        - 6.2.6. [6. 排序和聚合](#6-排序和聚合)
            - 6.2.6.1. [Sort（排序）](#sort排序)
            - 6.2.6.2. [HashAggregate（哈希聚合）](#hashaggregate哈希聚合)
            - 6.2.6.3. [GroupAggregate（分组聚合）](#groupaggregate分组聚合)
        - 6.2.7. [7. 过滤条件（Filter）](#7-过滤条件filter)
        - 6.2.8. [8. 并行执行（Parallel）](#8-并行执行parallel)
    - 6.3. [版本差异和新特性](#版本差异和新特性)
        - 6.3.1. [PostgreSQL 9.6+](#postgresql-96)
        - 6.3.2. [PostgreSQL 10+](#postgresql-10)
        - 6.3.3. [PostgreSQL 12+](#postgresql-12)
        - 6.3.4. [PostgreSQL 13+](#postgresql-13)
        - 6.3.5. [PostgreSQL 14+](#postgresql-14)
        - 6.3.6. [PostgreSQL 15+](#postgresql-15)
    - 6.4. [优化实践](#优化实践)
        - 6.4.1. [1. 识别慢查询](#1-识别慢查询)
        - 6.4.2. [2. 索引优化](#2-索引优化)
        - 6.4.3. [3. 统计信息更新](#3-统计信息更新)
        - 6.4.4. [4. 配置参数调优](#4-配置参数调优)
        - 6.4.5. [5. 查询重写](#5-查询重写)
    - 6.5. [常见问题和解决方案](#常见问题和解决方案)
        - 6.5.1. [1. 成本估算不准确](#1-成本估算不准确)
        - 6.5.2. [2. 顺序扫描大表](#2-顺序扫描大表)
        - 6.5.3. [3. 排序使用磁盘](#3-排序使用磁盘)
        - 6.5.4. [4. 并行查询未启用](#4-并行查询未启用)
    - 6.6. [最佳实践](#最佳实践)
- 7. [Tips](#tips)

💠 2026-06-29 17:42:10
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


### JOIN 最佳实践

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

> 优化建议

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

## MVCC (Multi-Version Concurrency Control)

PostgreSQL 通过 **MVCC** 实现事务隔离，核心机制是**每行数据保留多个版本**，读写互不阻塞。

### 核心数据结构

每一行（tuple）有两个隐藏字段：
- `xmin`：创建该行版本的事务 ID
- `xmax`：删除/锁定该行版本的事务 ID

### 实现原理

| 操作 | 行为 |
|------|------|
| **INSERT** | 新行的 `xmin` = 当前事务 ID，`xmax` = 0（无效） |
| **DELETE** | 逻辑删除：将当前行的 `xmax` 设为当前事务 ID（标记为已删除），后续 `VACUUM` 会清理 |
| **UPDATE** | 等效于 DELETE + INSERT：将旧行的 `xmax` = 当前事务 ID，同时插入新行（`xmin` = 当前事务 ID） |

### 可见性判断规则

事务在读取行时，根据 `xmin` / `xmax` 和当前快照判断是否可见：

```
当前事务快照包含：所有已提交事务的列表 + 正在运行的事务列表
```

- **行可见**条件：`xmin` 已提交且未过期，且 `xmax` 无效或为当前事务
- **行不可见**条件：`xmin` 未提交，或 `xmax` 为已提交的其他事务

### 事务隔离级别

| 隔离级别 | 实现方式 |
|----------|----------|
| **Read Committed**（默认） | 每个 SQL 语句获取一次快照 |
| **Repeatable Read** | 整个事务使用同一快照（第一次查询时） |
| **Serializable** | 基于 SSI（Serializable Snapshot Isolation），检测序列化冲突 |

### 优缺点

- 优点：读从不阻塞写，写从不阻塞读
- 缺点：需要 `VACUUM` 清理过期版本（死元组），可能导致表膨胀

### 关键配置

```sql
-- 调整 VACUUM 触发阈值
autovacuum_vacuum_scale_factor = 0.01   -- 触发比例（默认 0.2）
autovacuum_vacuum_threshold = 50        -- 触发最小行数
autovacuum_naptime = 1min               -- 调度间隔
```

---

## WAL (Write-Ahead Logging)

WAL 是 PostgreSQL 保证**事务持久性（Durability）**和**崩溃安全（Crash Safety）**的核心机制。

### 核心原则

> **日志先行**：在数据页写入磁盘之前，必须先确保对应的日志已安全落盘。

### 写入流程

```
事务提交 → WAL 缓冲区 → WAL 文件（磁盘） → 返回 commit 成功 → 数据页（延迟写入）
```

1. 事务修改数据页时，先将变更记录写入 **WAL 缓冲区**
2. 事务 `COMMIT` 时，WAL 缓冲区内容 **强制刷入 WAL 文件**（`fsync`）
3. 确认 WAL 落盘后，返回客户端提交成功
4. 数据页的写入由 **checkpoint 进程** 或 **脏页刷出** 在后台异步完成

### WAL 记录结构

每条 WAL 记录包含：

| 字段 | 说明 |
|------|------|
| **LSN** (Log Sequence Number) | WAL 中位置，单调递增，数据页上会记录 `pd_lsn`（该页最后一次修改的 LSN） |
| **Prev** | 上一条记录的 LSN，形成链 |
| **XID** | 产生该记录的事务 ID |
| **Resource Manager** | 资源管理器类型（Heap、Btree、Transaction 等） |
| **Payload** | 具体变更数据（增量变更或全页镜像） |

### LSN 与数据页的关系

```
数据页的 pd_lsn >= WAL 记录的 LSN  → 该页已应用此变更（无需恢复）
数据页的 pd_lsn < WAL 记录的 LSN   → 该页尚未应用（需要 REDO）
```

### Checkpoint

Checkpoint 是 WAL 和持久化之间的关键同步点：

1. 将所有脏页刷入磁盘
2. 保证 `redo` 起点前的 WAL 不再需要
3. 更新控制文件中的 checkpoint 位置

```sql
-- 手动触发 checkpoint
CHECKPOINT;

-- 调整 checkpoint 间隔
checkpoint_timeout = 5min             -- 最大间隔（默认 5min）
max_wal_size = 1GB                     -- WAL 最大大小（默认 1GB）
min_wal_size = 80MB                    -- WAL 最小大小
```

### 崩溃恢复流程

```
数据库启动 → 读取控制文件找到最后一个 checkpoint
          → REDO 阶段：从 checkpoint LSN 开始重放 WAL
          → 恢复到一致状态 → 数据库可用
```

### WAL 的额外用途

| 用途 | 说明 |
|------|------|
| **PITR (Point-In-Time Recovery)** | 基础备份 + 连续 WAL 归档，可恢复到任意时间点 |
| **Streaming Replication** | Standby 节点持续接收并重放主节点的 WAL |
| **归档日志** | `archive_command` 将 WAL 段归档到远程存储 |

### 关键配置

```sql
wal_level = replica                   -- WAL 记录级别（minimal / replica / logical）
fsync = on                            -- 确保 WAL 写入的持久性
synchronous_commit = on               -- 等待 WAL 落盘后才返回 commit 成功
wal_buffers = 16MB                    -- WAL 缓冲区大小
wal_sync_method = fdatasync           -- WAL 同步方法（fdatasync / fsync / open_sync）
archive_mode = on                     -- 启用归档
archive_command = 'cp %p /archive/%f' -- 归档命令
```

### WAL Segment 文件

- 默认大小 **16MB**（可通过 `--wal-segsize` 在编译时指定）
- 命名格式：`000000010000000000000001`（timeline + LSN）
- 循环使用：已归档或已 checkpoint 的 WAL 段可被回收复用

---

************************

# 集群
> [创建数据库集群](http://www.postgres.cn/docs/9.3/creating-cluster.html)  

> [PostgreSQL—集群方案 – Enmalvi](http://www.enmalvi.com/2022/10/28/postgresql-patroni/#shu_ju_ku_ji_qun_fang_an)  

************************

# Explain 
[Official Doc](https://www.postgresql.org/docs/current/sql-explain.html)

EXPLAIN 用于显示PostgreSQL查询优化器生成的执行计划，是性能分析和优化的核心工具。

## 基本语法

```sql
EXPLAIN [ ( option [, ...] ) ] statement
EXPLAIN [ ANALYZE ] [ VERBOSE ] statement
```

> 常用选项

- **ANALYZE**：实际执行查询并显示实际运行时间（默认不执行）
- **VERBOSE**：显示详细的计划信息
- **BUFFERS**：显示缓冲区使用情况（需要ANALYZE）
- **COSTS**：显示成本估算（默认开启）
- **TIMING**：显示实际时间（需要ANALYZE，默认开启）
- **SUMMARY**：显示总时间和总行数（默认开启）
- **FORMAT**：输出格式（TEXT/XML/JSON/YAML）

> 常用组合

```sql
-- 基础：查看执行计划（不执行）
EXPLAIN SELECT * FROM table_name WHERE id = 1;

-- 标准：执行并显示详细信息
EXPLAIN (ANALYZE, BUFFERS, VERBOSE) 
SELECT * FROM table_name WHERE id = 1;

-- JSON格式：便于程序解析
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT * FROM table_name WHERE id = 1;
```

## 关键信息

### 1. 成本估算（Cost）

```
Cost=0.00..25.00 rows=1000 width=36
```

- **启动成本（0.00）**：返回第一行前的成本
- **总成本（25.00）**：返回所有行的总成本
- **rows**：估算的行数
- **width**：平均行宽度（字节）

**关注点：**
- 成本单位是**相对值**，不是实际时间
- 对比不同计划的成本值
- 如果`rows`估算偏差大，需要更新统计信息（ANALYZE）

### 2. 实际执行时间（ANALYZE）

```
Execution Time: 0.123 ms
```

- **Planning Time**：计划时间
- **Execution Time**：实际执行时间

**关注点：**
- 实际时间比成本估算更准确
- 注意Planning Time是否过长（可能统计信息过期）

### 3. 缓冲区使用（BUFFERS）

```
Buffers: shared hit=4 read=1
```

- **shared hit**：从共享缓冲区读取的页数（缓存命中）
- **shared read**：从磁盘读取的页数（缓存未命中）
- **shared written**：写入磁盘的页数
- **temp read/written**：临时文件读写

**关注点：**
- `shared hit`比例高表示缓存效果好
- `shared read`多表示可能需要增加`shared_buffers`或优化查询

### 4. 扫描类型（Scan Type）

#### Seq Scan（顺序扫描）
```
Seq Scan on table_name
```
- **全表扫描**，适用于小表或大部分数据需要读取
- **优化**：添加索引或使用WHERE条件过滤

#### Index Scan（索引扫描）
```
Index Scan using idx_name on table_name
```
- **使用索引查找**，适用于等值查询
- **优化**：确保索引存在且选择性高

#### Index Only Scan（仅索引扫描）
```
Index Only Scan using idx_name on table_name
```
- **只扫描索引**，不需要访问表数据（PostgreSQL 9.2+）
- **最优**：如果所有需要的列都在索引中

#### Bitmap Index Scan + Bitmap Heap Scan
```
Bitmap Index Scan on idx_name
Bitmap Heap Scan on table_name
```
- **位图索引扫描**，适用于多条件查询
- **过程**：先扫描索引建立位图，再访问表

### 5. JOIN类型

#### Nested Loop（嵌套循环）
```
Nested Loop
  -> Seq Scan on small_table
  -> Index Scan on large_table
```
- **适用**：小表驱动大表，内表有索引
- **成本**：O(外表行数 × 内表查找成本)

#### Hash Join（哈希连接）
```
Hash Join
  Hash Cond: (a.id = b.id)
  -> Seq Scan on table_a
  -> Hash
      -> Seq Scan on table_b
```
- **适用**：没有索引或索引不适用
- **过程**：对小表建立哈希表，扫描大表匹配

#### Merge Join（归并连接）
```
Merge Join
  Merge Cond: (a.id = b.id)
  -> Index Scan using idx_a on table_a
  -> Index Scan using idx_b on table_b
```
- **适用**：两个表都已排序（有索引）
- **成本**：O(n+m)

### 6. 排序和聚合

#### Sort（排序）
```
Sort
  Sort Key: column_name
  Sort Method: quicksort  Memory: 1024kB
```
- **关注**：`Sort Method`
  - `quicksort`：内存排序
  - `external merge`：外部排序（需要临时文件）
- **优化**：如果经常排序，考虑添加索引

#### HashAggregate（哈希聚合）
```
HashAggregate
  Group Key: column_name
```
- **适用**：GROUP BY操作
- **优化**：确保有足够的`work_mem`

#### GroupAggregate（分组聚合）
```
GroupAggregate
  Group Key: column_name
```
- **适用**：已排序的数据进行聚合
- **需要**：数据已按GROUP BY列排序

### 7. 过滤条件（Filter）

```
Filter: (id > 100 AND status = 'active')
Rows Removed by Filter: 9500
```

**关注点：**
- `Rows Removed by Filter`：被过滤掉的行数
- 如果过滤率高，考虑添加索引

### 8. 并行执行（Parallel）

```
Parallel Seq Scan on table_name
  Workers Planned: 4
  Workers Launched: 4
```

**关注点：**
- `Workers Planned`：计划的并行worker数
- `Workers Launched`：实际启动的worker数
- 需要`max_parallel_workers_per_gather > 0`（PostgreSQL 9.6+）

## 版本差异和新特性

### PostgreSQL 9.6+

**并行查询**
```sql
-- 启用并行查询
SET max_parallel_workers_per_gather = 4;
EXPLAIN ANALYZE SELECT * FROM large_table;
```

**关注点：**
- 并行扫描适用于大表
- 需要足够的CPU核心和内存

### PostgreSQL 10+

**JIT编译**（Just-In-Time Compilation）
```sql
SET jit = on;
EXPLAIN ANALYZE SELECT SUM(amount) FROM orders GROUP BY customer_id;
```

**关注点：**
- JIT可以加速复杂查询（PostgreSQL 11+默认开启）
- 适用于大量数据处理

### PostgreSQL 12+

**增量排序**（Incremental Sort）
```
Incremental Sort
  Sort Key: a, b
  Presorted Key: a
```

**优势：**
- 如果数据已按部分键排序，可以增量排序
- 减少排序成本

### PostgreSQL 13+

**并行索引扫描**
```
Parallel Index Scan using idx_name
  Workers Planned: 2
```

**优势：**
- 大索引可以并行扫描
- 提高索引扫描性能

### PostgreSQL 14+

**增强的EXPLAIN输出**
- 更详细的并行执行信息
- 更好的JIT统计信息

### PostgreSQL 15+

**MERGE命令的执行计划**
- 支持MERGE语句的EXPLAIN分析

## 优化实践

### 1. 识别慢查询

```sql
-- 查找执行时间长的操作
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT * FROM orders WHERE customer_id = 123;

-- 关注：
-- - Execution Time > 100ms
-- - Seq Scan on large tables
-- - Rows Removed by Filter 很高
-- - External Sort（磁盘排序）
```

### 2. 索引优化

```sql
-- 如果看到 Seq Scan，检查是否需要索引
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';

-- 如果看到 Index Scan but rows很高，检查索引选择性
-- 如果看到 Bitmap Heap Scan，考虑复合索引
```

### 3. 统计信息更新

```sql
-- 如果rows估算偏差大，更新统计信息
ANALYZE table_name;

-- 或者增加统计信息采样
ALTER TABLE table_name ALTER COLUMN column_name SET STATISTICS 1000;
ANALYZE table_name;
```

### 4. 配置参数调优

```sql
-- 增加工作内存（用于排序、哈希等）
SET work_mem = '256MB';

-- 启用并行查询
SET max_parallel_workers_per_gather = 4;
SET max_parallel_workers = 8;

-- 启用JIT（PostgreSQL 11+）
SET jit = on;
SET jit_above_cost = 100000;
```

### 5. 查询重写

```sql
-- 避免全表扫描
-- 不好：
SELECT * FROM orders WHERE EXTRACT(YEAR FROM created_at) = 2023;

-- 好：
SELECT * FROM orders WHERE created_at >= '2023-01-01' AND created_at < '2024-01-01';

-- 使用覆盖索引（Index Only Scan）
CREATE INDEX idx_covering ON orders (customer_id, status, amount);
-- 查询只需要这些列时可以使用Index Only Scan
```

## 常见问题和解决方案

### 1. 成本估算不准确

**问题**：rows估算偏差大

**解决**：
```sql
-- 更新统计信息
ANALYZE table_name;

-- 增加统计信息采样
ALTER TABLE table_name SET (autovacuum_analyze_scale_factor = 0.02);
```

### 2. 顺序扫描大表

**问题**：Seq Scan on large table

**解决**：
- 添加索引
- 优化WHERE条件
- 使用分区表（PostgreSQL 10+）

### 3. 排序使用磁盘

**问题**：Sort Method: external merge Disk

**解决**：
```sql
-- 增加work_mem
SET work_mem = '256MB';

-- 或添加索引避免排序
CREATE INDEX idx_sort ON table_name (sort_column);
```

### 4. 并行查询未启用

**问题**：没有并行执行

**解决**：
```sql
-- 检查配置
SHOW max_parallel_workers_per_gather;
SHOW max_parallel_workers;

-- 启用并行
SET max_parallel_workers_per_gather = 4;
```

## 最佳实践

1. **定期使用EXPLAIN ANALYZE**：了解查询实际性能
2. **关注BUFFERS**：识别缓存命中率问题
3. **对比不同计划**：尝试不同的查询写法
4. **保持统计信息最新**：定期ANALYZE
5. **使用索引**：但避免过度索引
6. **监控执行时间**：设置慢查询日志

> 参考：
> - [PostgreSQL EXPLAIN文档](https://www.postgresql.org/docs/current/sql-explain.html)
> - [使用EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
> - [查询性能](https://www.postgresql.org/docs/current/performance-tips.html)

# Tips

```sql
-- 查询所有表（包括索引、TOAST）的总大小，按大小降序
SELECT
    schemaname AS schema,
    relname AS table_name,
    pg_size_pretty(pg_total_relation_size(relid)) AS total_size,
    pg_size_pretty(pg_relation_size(relid)) AS table_size,
    pg_size_pretty(pg_indexes_size(relid)) AS index_size,
    pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) AS external_size
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```