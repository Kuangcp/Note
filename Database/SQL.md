---
title: SQL基础
date: 2018-12-16 17:29:28
tags: 
    - SQL
categories: 
    - 数据库
---

**目录 start**

1. [SQL](#sql)
    1. [条件语句](#条件语句)

**目录 end**|_2021-05-27 21:59_|
****************************************
# SQL
> [soar](https://github.com/XiaoMi/soar)`SQL Optimizer And Rewriter `

- SQL语言共分为四大类：
    - 数据查询语言DQL: SELECT
    - 数据操纵语言DML: UPDATE、INSERT、DELETE
    - 数据定义语言DDL: CREATE、ALTER、DROP
    - 数据控制语言DCL: GRANT,DENY,REVOKE

## 条件语句
`case when then else end `
```sql
update table_test set mark = 
    case
        when id = 2 then '2'
        when id = 5 then '5' 
        else ''
    end
where id in (2,5);
```