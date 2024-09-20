---
title: SQL基础
date: 2018-12-16 17:29:28
tags: 
    - SQL
categories: 
    - 数据库
---

💠

- 1. [SQL](#sql)
    - 1.1. [条件语句](#条件语句)
    - 1.2. [聚合函数](#聚合函数)
    - 1.3. [分析函数](#分析函数)
        - 1.3.1. [窗口函数](#窗口函数)
- 2. [安全](#安全)
- 3. [Tips](#tips)

💠 2024-09-20 11:10:09
****************************************
# SQL
> [Wiki: SQL](https://en.wikipedia.org/wiki/SQL)

> [database language SQL](https://archive.org/details/federalinformati127nati/page/n8/mode/1up)

- SQL语言共分为四大类：
    - 数据查询语言DQL: SELECT
    - 数据操纵语言DML: UPDATE、INSERT、DELETE
    - 数据定义语言DDL: CREATE、ALTER、DROP
    - 数据控制语言DCL: GRANT,DENY,REVOKE

> [sqlglot](https://github.com/tobymao/sqlglot) `Python SQL Parser and Transpiler `

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

## 聚合函数



## 分析函数

### 窗口函数
统计不止发生一次，而是发生多次。统计不止发生在记录集形成后，而是发生在记录集形成的过程中

> [窗口函数](https://blog.csdn.net/huozhicheng/article/details/5843782/)

************************

# 安全
> [SQL Injection Payload List](https://github.com/payloadbox/sql-injection-payload-list)  

************************

# Tips
> [soar](https://github.com/XiaoMi/soar)`SQL Optimizer And Rewriter `