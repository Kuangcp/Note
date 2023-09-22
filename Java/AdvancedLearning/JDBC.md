---
title: JDBC
date: 2018-12-16 17:28:17
tags: 
categories: 
    - Java
---

**目录 start**

1. [JDBC](#jdbc)
    1. [长连接流式导出数据](#长连接流式导出数据)
    1. [MySQL](#mysql)
    1. [Java内置数据库Derby](#java内置数据库derby)
1. [Tips](#tips)

**目录 end**|_2023-09-22 18:34_|
****************************************
# JDBC
> [码农翻身:JDBC的诞生](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513438&idx=1&sn=2967d595bb7d4ffdd2dacd3ab7501bbd&chksm=80d6799db7a1f08b27dc97650434fb2fc0e2570628945db99d9300a99e52828fd05c42fdb441&scene=21#wechat_redirect)

- 基础的批量操作SQL ` pstmt.executeBatch(); //批量执行`

- 注册 driver
- 创建 connection
- 创建 statement
- 执行获取 Resultset
- 处理返回结果 resultst

Statement 和 PrepareStatement 的区别， 掌握PrepareStatement的主要用法(推荐使用)

## 长连接流式导出数据
```java
private void fetchBatchWithDataResource(DataSource ds, String sql, String where, int fetchSize, Consumer<List<LinkedHashMap<String, Object>>> handle) {
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
        boolean handled = false;
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
                data = new ArrayList<>();
                handled = true;
            } else {
                handled = false;
            }
        }
        if (!handled) {
            handle.accept(data);
            counter++;
        }

        log.info("stream export: size={} count={}", data.size(), counter);
    } catch (Exception e) {
        log.error("", e);
    } finally {
        close(connection, stmt, rs);
    }
}
```
- Statement 设置了 fetchSize 或者 TYPE_FORWARD_ONLY 模式后，都会采用游标的方式获取全部的数据
- handle 则是 CSV Excel 的消费处理逻辑

************************

## MySQL
> 与MySQL的互操作

- [Java数据类型和MySQL数据类型对应](https://dev.mysql.com/doc/connector-j/5.1/en/connector-j-reference-type-conversions.html)`简单来说就是基本数据类型加上String是有对应的MySQL基本数据类型`

## Java内置数据库Derby
> 在Java11中被移除了
> [Derby](http://db.apache.org/derby/derby_comm.html)

TODO 数据库连接池 设计 ThreadLocal

************************

# Tips
> [mysql-connector-java 插入 utf8mb4 字符失败问题处理分析](https://blog.arstercz.com/mysql-connector-java-%e6%8f%92%e5%85%a5-utf8mb4-%e5%ad%97%e7%ac%a6%e5%a4%b1%e8%b4%a5%e9%97%ae%e9%a2%98%e5%a4%84%e7%90%86%e5%88%86%e6%9e%90/)
