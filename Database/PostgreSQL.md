---
title: PostgreSQL
date: 2018-12-16 17:27:21
tags: 
    - PostgreSQL
categories: 
    - 数据库
---

💠

- 1. [Postgresql](#postgresql)
- 2. [安装](#安装)
    - 2.1. [Docker方式](#docker方式)
- 3. [管理](#管理)
    - 3.1. [终端命令行使用](#终端命令行使用)
    - 3.2. [用户和角色权限](#用户和角色权限)
        - 3.2.1. [创建用户](#创建用户)
        - 3.2.2. [修改权限](#修改权限)
- 4. [基础数据类型](#基础数据类型)
    - 4.1. [字符串](#字符串)
    - 4.2. [自动增长](#自动增长)
- 5. [DDL](#ddl)
- 6. [DML](#dml)
- 7. [图数据库](#图数据库)
    - 7.1. [AgensGraph](#agensgraph)
- 8. [应用](#应用)
    - 8.1. [Java使用](#java使用)
    - 8.2. [导入导出](#导入导出)

💠 2025-04-18 09:37:55
****************************************
# Postgresql

> [PostgreSQL](http://www.cnblogs.com/fcode/articles/PostgreSQL.html) | [wiki](https://wiki.postgresql.org/wiki/Main_Page)

- 严格实现SQL标准
- Schemas 和表，用户的关系：
    - Schemas相当于是一个数据库进行分类的文件夹

`PostgreSQL和MySQL对比`
> [PostgreSQL 与 MySQL 相比，优势何在？](https://www.zhihu.com/question/20010554)
> [Converting MySQL to PostgreSQL](https://en.wikibooks.org/wiki/Converting_MySQL_to_PostgreSQL)

# 安装
安装客户端 `sudo apt install postgresql-client`  
安装服务端 `sudo apt install postgresql`  

## Docker方式
> [Dockerhub 官方镜像](https://hub.docker.com/_/postgres/)

- `docker pull postgres`
    - 运行容器 `docker run --name mypostgre -i -t -p 5432:5432 postgres`
    - 客户端连接 `psql -h localhost -p 5432 -U postgres`

************************************
# 管理
> [PostgreSQL 9.6.0 手册](http://postgres.cn/docs/9.6/index.html)

## 终端命令行使用
> [PostgreSQL新手入门](http://www.ruanyifeng.com/blog/2013/12/getting_started_with_postgresql.html)
`用熟悉的MySQL命令来解释`
- `\l` show databases
- `\c dbname [user]` 切换数据库
- `\dt` show tables
- `\d tablename` desc tablename
- `\di` 查看索引
- `\du` 查看所有用户
- `\dn` 查看模式列表
- `\copyright` 显示版权信息
- `\encoding` 显示编码信息
- `\h` SQL命令语法上的说明，用*显示全部命令 
- `\prompt [文本]名称` 提示用户设定内部变数
- `\password [username]` 改密码
- `\q` exit

## 用户和角色权限

### 创建用户
- `createuser -P -D -R -e playboy`  //创建一个用户,-P要设置密码，-R,不参创建其他用户，-D不能创建数据库
- `create user myth` 不带login属性
- `create role myth` 具有login属性
- `psql -U playboy -d playboy` 登录用户，一般默认是有用户同名数据库才能登录

- [修改默认登录不需要密码的配置](http://www.linuxidc.com/Linux/2013-04/83564p2.htm)

```sql
    -- 创建用户 创建库 授权
    CREATE USER u_xxx WITH PASSWORD 'xxxxxxx';
    CREATE DATABASE test OWNER u_xxx;
    GRANT ALL PRIVILEGES ON DATABASE test TO u_xxx;
```

### 修改权限
> [参考博客](http://blog.csdn.net/beiigang/article/details/8604578)
> [参考博客_角色](http://www.cnblogs.com/stephen-liu74/archive/2012/05/18/2302639.html)
> [配置](http://www.linuxidc.com/Linux/2013-04/83564p2.htm)

- `ALTER ROLE rolename LOGIN;`  设置登录权限
- `ALTER ROLE david WITH PASSWORD 'ufo456';` 设置密码登录权限
    - 但是，默认是不需要密码 查看pg_hba.conf 文件，发现local 的METHOD 为trust，所以不需要输入密码
    - 将local 的METHOD 更改为password，然后保存重启postgresql。
    - [博客](http://www.linuxidc.com/Linux/2014-02/96886.htm)
- ` ALTER ROLE sandy VALID UNTIL '2014-04-24';` 设置角色有效期
- `SELECT * from pg_roles ;` 查看所有角色

- `CREATE ROLE father login nosuperuser nocreatedb nocreaterole noinherit encrypted password 'abc123';` 
    - 在PostgreSQL中，首先需要创建一个代表组的角色，之后再将该角色的membership 权限赋给独立的角色即可。
- `GRANT CONNECT ON DATABASE test to father;` 角色赋予数据库test 连接权限和相关表的查询权限。

> 注意：如果一个库授权给了用户A，库里面新建了表C 需要再次单独授权给用户A 否则A没有C表的权限

# 基础数据类型
> [Chapter 8. Data Types](https://www.postgresql.org/docs/current/datatype.html)  
> [PostgreSQL 数据类型](https://www.runoob.com/postgresql/postgresql-data-type.html)  


************************

- 日期类型转bigint `select   to_char(period,'yyyymmdd')::bigint  as period_int` 

************************

## 字符串
text varchar 最大1Gb

## 自动增长 
- 相比于MySQL的 AUTO_INCREMENT 关键字标记， pg将该特性设计为数据类型SERIAL， 但是在使用上没有MySQL方便
- SMALLSERIAL 2字节  SERIAL	4字节 	BIGSERIAL 8字节 
    - 注意这个自增序列值实际上是在系统表维护的 `SELECT nextval(pg_get_serial_sequence('the_table', 'the_primary_key'));` 

- 在insert时，如果手动指定了id的值，那这个序列值不会跟着更新，下一次不带id去insert的时候就会冲突报错。
```sql
    create table t_user(id BIGSERIAL primary key , name varchar(31), email varchar(64), deprecated boolean );
    INSERT INTO t_user (id, name, email, deprecated) VALUES (22, 'test6', null, false);
    -- 如果当前序列值为21 这个insert会报错，id重复
    INSERT INTO t_user (name, email, deprecated) VALUES ('test5', null, false);
```
- `id int8 GENERATED ALWAYS AS IDENTITY primary key` 这种字段就无法通过insert values指定id的值，会直接报错。
- `id int8 GENERATED BY DEFAULT AS IDENTITY primary key` 等价于 BIGSERIAL primary key

因此最好的方式是insert完，手动通过setval更新序列值到当前表的最大值。 [PostgreSQL更新所有表序列值到当前表中最大值](https://hhao.wang/archives/545)

```sql
    SELECT nextval(pg_get_serial_sequence('t_user', 'id')); -- 自增
    SELECT currval(pg_get_serial_sequence('t_phone', 'id')); -- get 
    SELECT setval(pg_get_serial_sequence('t_phone', 'id'), 1000); -- set 
```

# DDL
> 注意PG的查看表，函数，视图的定义(DCL)时很复杂，没有直观的语句类似`show create table`可以用，通常使用工具来查看表定义和函数定义视图定义等等。

- 元数据存储： PostgreSQL将数据库对象（表、列、索引等）的元数据存储在系统目录（如pg_catalog）中。
- 数据类型： PostgreSQL支持多种数据类型、约束、继承等特性，这些复杂性使得直接生成一个简单的CREATE TABLE语句变得困难。
    - 为了准确地反映表的定义，需要考虑各种情况，比如默认值、约束、继承关系等。
- 性能： 对于大型数据库生成 show create table 很耗费性能。

```sql
-- 简单查询出列
SELECT attname AS column_name, format_type(atttypid, atttypmod) AS data_type, attnotnull AS is_nullable
FROM pg_attribute  WHERE attrelid = (SELECT oid FROM pg_class WHERE relname = 'table_name') AND attnum > 0;
```

# DML
注意PG的DML语句是支持事务的，也有MVCC机制

> [修改表](http://www.postgres.cn/docs/9.4/ddl-alter.html)   

```sql
ALTER TABLE products ADD COLUMN description text;
ALTER TABLE products DROP COLUMN description;
ALTER TABLE products ALTER COLUMN price TYPE numeric(10,2);
ALTER TABLE products RENAME COLUMN product_no TO product_number;
ALTER TABLE products RENAME TO items;
```

修改一个列的时候需要关注列的 约束（主键，外键，唯一，非空，自定义）和索引，需要同步修改或删除。

************************

# 图数据库
[PostgreSQL 图式搜索(graph search)实践 ](https://developer.aliyun.com/article/328141)`自定义函数和特定SQL模拟图有关的查询算法`  

> 图数据库插件

- [edgedb](https://github.com/edgedb/edgedb)  
- [apache/age](https://github.com/apache/age) 基于AgensGraph衍生（PG插件） [apache/age-viewer](https://github.com/apache/age-viewer)  
    - [Java JDBC驱动](https://github.com/apache/age/tree/master/drivers/jdbc)`也就是使用了PG驱动再附加定义了相应的数据类（节点，边）`  

## AgensGraph
[bitnine-oss/agensgraph](https://github.com/bitnine-oss/agensgraph)  
[AgensGraph - PostgreSQL wiki](https://wiki.postgresql.org/wiki/AgensGraph)  

从架构图上来看，比插件形式绑定更深，属于衍生数据库，因此可以复用PG的特性，例如分布式能力。

启动服务 本质是pg进程 `docker run --name agensgraph -p 5654:5432 -e POSTGRES_PASSWORD=agensgraph -d bitnine/agensgraph:v2.13.0-debian`
- 默认用户名和pg镜像的默认值一样是 postgres

```sql
-- 创建数据库
create graph test_g1;
-- 切换图数据库
SET graph_path = test_g1;
-- 设置用户默认使用的图数据库
ALTER USER postgres SET graph_path = 'test_g1';

-- 查询
match(n) return n;
```

图形客户端: bitnine/agviewer 操作习惯基本和Neo4j自带的网页客户端一致，但是稳定性可用性差很多
- `docker run -d --publish=5655:3001 --name=agviewer bitnine/agviewer:latest` 注意该客户端支持Age和Agensgraph

************************
# 应用

## Java使用
> [Postgresql JDBC Driver](https://github.com/pgjdbc/pgjdbc)

- [官方：springboot使用](https://springframework.guru/configuring-spring-boot-for-postgresql/)
    - [参考博客](https://www.netkiller.cn/java/spring/boot/postgresql.html)

## 导入导出
> 导出

copy 方式，单连接复制出查询语句的结果

- 可以使用pg_dump和pg_dumpall来完成。比如备份sales数据库： 
    - pg_dump drupal > /opt/Postgresql/backup/1.bak 


[JDBC： 长连接流式导出数据](/Java/AdvancedLearning/JDBC.md#长连接流式导出数据)
