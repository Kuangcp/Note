---
title: PostgreSQL进阶
date: 2018-12-16 17:28:33
tags: 
    - PostgreSQL
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
- 3. [索引](#索引)
- 4. [事务](#事务)
- 5. [Explain](#explain)

💠 2024-09-27 11:12:37
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
                    where conrelid = a.attrelid and conkey[1] = attnum and contype = 'u') > 0 then 'Y'
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
    where attstattarget = -1 and c.relname = 'table_test'
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
TODO 大表和小表 join顺序是否和MySQL一样有要求

************************

# 索引
> [Official Doc](https://www.postgresql.org/docs/11/indexes.html)

# 事务
MVCC WAL 

************************

# Explain 
[Official Doc](https://www.postgresql.org/docs/current/sql-explain.html)

TODO 理解
