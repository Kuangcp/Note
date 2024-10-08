---
title: JDBC
date: 2018-12-16 17:28:17
tags: 
categories: 
    - Java
---

💠

- 1. [JDBC](#jdbc)
    - 1.1. [Statement](#statement)
        - 1.1.1. [PrepareStatement](#preparestatement)
    - 1.2. [ResultSet](#resultset)
        - 1.2.1. [长连接流式导出数据](#长连接流式导出数据)
    - 1.3. [SQLException](#sqlexception)
- 2. [厂商驱动](#厂商驱动)
    - 2.1. [MySQL](#mysql)
    - 2.2. [Clickhouse](#clickhouse)
- 3. [Tips](#tips)

💠 2024-10-08 11:23:38
****************************************
# JDBC
Java DataBase Connectivity

核心思想是定义一套接口规范，让各个数据库厂商实现这套接口，从而让应用方调用数据库的能力时可以不关心底层数据库
- 设计是美好的，但是现实是丑陋的，或者说无法对多类型的数据库做完全的抽象一致，基础功能确实能一致化，其他功能还是要特殊化处理
    - 举例： 获取某个表的元信息`表引擎，表索引，字段名，字段类型` MySQL和PostgreSQL实现完全不一致，pg实现成本很大，有些功能无法实现

> [码农翻身:JDBC的诞生](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513438&idx=1&sn=2967d595bb7d4ffdd2dacd3ab7501bbd&chksm=80d6799db7a1f08b27dc97650434fb2fc0e2570628945db99d9300a99e52828fd05c42fdb441&scene=21#wechat_redirect)

> 基础流程
- 注册 driver
- 建立 connection
- 创建 statement
- 执行获取 ResultSet
- 解析返回的 ResultSet


> Tips
- 基础的批量操作SQL ` pstmt.executeBatch(); //批量执行`
- [在Java11中被移除了的 Derby](http://db.apache.org/derby/derby_comm.html)

## Statement
主要分为 Statement 和 PrepareStatement, 在使用层面主要的区别为前者直接执行原始SQL,存在SQL注入风险, 后者是编译模板。

### PrepareStatement
> [Oracle: Using Prepared Statements](https://docs.oracle.com/javase/tutorial/jdbc/basics/prepared.html)

依赖于具体数据库，常见的 [MySQL](https://dev.mysql.com/doc/refman/8.3/en/sql-prepared-statements.html) [PostgreSQL](https://jdbc.postgresql.org/documentation/server-prepare/)都有SQL编译功能

> 权衡
- [PrepareStatement的功与过](https://www.cnblogs.com/wangzhen3798/p/12206811.html)`最多的问题是 因为SQL只编译解析一次，执行计划的重用导致会忽略实际传入的参数对执行计划的影响`
- [MyBatis select query slow](https://groups.google.com/g/mybatis-user/c/Wubq26QCWYo?pli=1)`应该是一样的问题编译SQL在不同执行时，执行计划变更导致的慢`
    - [Query is slow with JDBC parameters, fast with concatenated SQL](https://dba.stackexchange.com/questions/231109/query-is-slow-with-jdbc-parameters-fast-with-concatenated-sql) `MSSQL`


> 客户端参数调整
- [Druid](https://github.com/alibaba/druid/blob/master/druid-spring-boot-starter/README_EN.md)`pool-prepared-statements` 连接池层面的缓存

************************

## ResultSet
> 仅为JDBC接口，具体行为细节来自实际数据库厂商提供的驱动

### 长连接流式导出数据
常见的分页导出的缺点有 分页越来越慢和不稳定排序导致页之间数据重复或丢失，用长连接流方式可以规避

```java
    // 阻塞模式 查数据和业务逻辑交替执行
    private void fetchBatchWithDataResource(DataSource ds, String sql, String where, int fetchSize,
                                            Consumer<List<LinkedHashMap<String, Object>>> handle) {
        Connection connection = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            connection = ds.getConnection();
            String query;
            if (StringUtils.isNotBlank(where)) {
                query = sql + " WHERE " + where;
            } else {
                query = sql;
            }

            log.info("stream export: query={}", query);

            stmt = connection.createStatement(ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY);
            stmt.setQueryTimeout(3600);
            stmt.setFetchSize(fetchSize);

            rs = stmt.executeQuery(query);
            int counter = 0;

            List<LinkedHashMap<String, Object>> data = new ArrayList<>();
            while (rs.next()) {
                ResultSetMetaData meta = rs.getMetaData();
                int columnCount = meta.getColumnCount();
                LinkedHashMap<String, Object> row = new LinkedHashMap<>();
                for (int i = 1; i <= columnCount; i++) {
                    row.put(meta.getColumnName(i), rs.getObject(i));
                }
                data.add(row);

                if (data.size() > fetchSize) {
                    handle.accept(data);
                    counter++;
                    data.clear();
                }
            }
            if (!data.isEmpty()) {
                handle.accept(data);
                counter++;
            }

            log.info("stream export: count={} dataSize={} ", counter, (counter - 1) * fetchSize + data.size());
        } catch (Exception e) {
            log.error("", e);
            throw new RuntimeException(e);
        } finally {
            close(connection, stmt, rs);
        }
    }
```
- Statement 设置了 fetchSize 或者 TYPE_FORWARD_ONLY 模式后，都会采用游标的方式获取全部的数据
- 参数 handle 是解析ResultSet 去生成 CSV Excel 等业务逻辑方法引用
- 优化版本 生产者-消费者模式，降低阻塞时间，从而降低大量任务的整体耗时，但是CPU毛刺会增多且明显
    - 生产者：查询，消费者：业务逻辑，队列：QueueChannel 
    - [样例代码](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/test/java/com/github/kuangcp/queue/use/blocking/ReaderWriterTest.java)

- Clickhouse可以直接使用, 不需要额外的配置
- PostgreSQL 调整：
    - executeQuery前 **关闭 autoCommit**，finally 开启，才会fetch指定的数据量,否则会拉取全部的数据到JVM。[pg jdbc doc](https://jdbc.postgresql.org/documentation/head/connect.html#connection-parameters)
- MySQL 调整：
    - url配置需要添加 useCursorFetch=true 或者 关闭 autoCommit 

## SQLException
大部分数据库厂商都会由此派生出自定义的异常，CK除外，因此支持JDBC通用数据库的平台需要做特殊处理。

************************
# 厂商驱动
## MySQL

- [Java数据类型和MySQL数据类型对应](https://dev.mysql.com/doc/connector-j/5.1/en/connector-j-reference-type-conversions.html)`简单来说就是基本数据类型加上String是有对应的MySQL基本数据类型`

## Clickhouse
> [clickhouse-java](/Database/OLAP/Clickhouse.md#java)  

************************

# Tips
> [mysql-connector-java 插入 utf8mb4 字符失败问题处理分析](https://blog.arstercz.com/mysql-connector-java-%e6%8f%92%e5%85%a5-utf8mb4-%e5%ad%97%e7%ac%a6%e5%a4%b1%e8%b4%a5%e9%97%ae%e9%a2%98%e5%a4%84%e7%90%86%e5%88%86%e6%9e%90/)

> 批量插入性能优化
- 关闭事务，或者手动管理事务 循环插入前开启，插入完一批再提交
- 多条 `insert values()` 改为一条 `insert values (),()`