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

**目录 end**|_2020-04-27 23:42_|
****************************************
# SQL
> 基础SQL语言的学习使用

> [soar](https://github.com/XiaoMi/soar)`SQL Optimizer And Rewriter `


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