---
title: MySQL进阶
date: 2018-12-16 17:26:16
tags: 
    - MySQL
categories: 
    - 数据库
---

**目录 start**
 
1. [MySQL Advanced](#mysql-advanced)
    1. [部署](#部署)
    1. [性能调优](#性能调优)
    1. [SQL 片段](#sql-片段)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# MySQL Advanced

- [Mysql Redis UDF 复制](http://www.cnblogs.com/zhxilin/archive/2016/09/30/5923671.html)

> [参考博客: shell 下执行mysql 命令](http://www.cnblogs.com/wangkangluo1/archive/2012/04/27/2472898.html)
- 将需要执行的SQL写入文件 并将结果输出到文件 `mysql -u root -h 192.168.10.201 -p123 < query.sql  > result.log`

## 部署
> 第一次看到MySQL内存上3G, 资源占用这么大, 还导致了内存不够, 直接MySQL自己退出了

## 性能调优
- 分析SQL运行效率: `explain` + SQL

> [MySQL下INNODB引擎的SELECT COUNT(*)性能优化及思考](http://www.piaoyi.org/database/MySQL-INNODB-SELECT-COUNT.html)

### 查看状态变量
> [ SHOW VARIABLES](https://dev.mysql.com/doc/refman/5.7/en/show-variables.html)  

- 查看所有连接 `show processlist;`
- 查看最大连接数 `show variables like "max_conn%";`
    - 设置最大连接数 `set global max_connections=5000;`

*****************************
## SQL 片段

1. 拼接删除库下所有表的SQL `select concat('drop table ',table_name,';') from information_schema.TABLES where table_schema='DATABASE_NAME';`

