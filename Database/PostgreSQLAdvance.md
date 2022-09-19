---
title: PostgreSQL进阶
date: 2018-12-16 17:28:33
tags: 
    - PostgreSQL
categories: 
    - 数据库
---

**目录 start**

1. [PostgreSQL Advance](#postgresql-advance)
1. [索引](#索引)

**目录 end**|_2022-09-14 13:34_|
****************************************
# PostgreSQL Advance

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
where attstattarget = -1
  and c.relname = 'table_test'
```

# 索引
> [Official Doc](https://www.postgresql.org/docs/11/indexes.html)

# Explain 
[Official Doc](https://www.postgresql.org/docs/current/sql-explain.html)

