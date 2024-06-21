---
title: MySQL索引
date: 2021-05-27 21:36:58
tags: 
categories: 
---

💠

- 1. [索引](#索引)
    - 1.1. [Explain](#explain)
    - 1.2. [为何选择 B+ 树结构](#为何选择-b+-树结构)
    - 1.3. [基本DDL](#基本ddl)
- 2. [索引的类型](#索引的类型)
    - 2.1. [普通索引](#普通索引)
    - 2.2. [唯一索引](#唯一索引)
    - 2.3. [主键索引](#主键索引)
    - 2.4. [主键索引/聚集索引](#主键索引聚集索引)
    - 2.5. [辅助索引/非聚集索引](#辅助索引非聚集索引)
    - 2.6. [Hash 索引](#hash-索引)
        - 2.6.1. [AHI 自适应哈希索引](#ahi-自适应哈希索引)
    - 2.7. [全文索引](#全文索引)
- 3. [需要使用索引的场景](#需要使用索引的场景)
    - 3.1. [索引优化](#索引优化)
        - 3.1.1. [统计报表](#统计报表)
- 4. [SQL查询未命中索引的场景](#sql查询未命中索引的场景)

💠 2024-06-21 10:47:46
****************************************

# 索引
> [Official Doc](https://dev.mysql.com/doc/refman/5.7/en/optimization-indexes.html)  

索引是采用特定的数据结构设计(B+Tree 或者 Hash), 为了对若干列进行快速访问  

> 优点
1. 加快查询速度
1. 如果使用唯一索引，保证数据库表中每条数据的唯一性；
1. 加快表与表之间的连接操作
1. 使用排序和分组检索数据时，可以显著的加快排序和分组的时间

> 缺点
1. 需要额外占用存储空间，如果索引建立太多可能会导致索引空间大于数据空间反而降低性能
1. 当对被索引的数据进行DML(增删改), 需要重建索引, 有一定性能影响
1. 如果是MySQL5.7及以下版本，在大表上建索引会阻塞很长时间。

> 注意: [Avoiding Full Table Scans](https://dev.mysql.com/doc/refman/5.7/en/table-scan-avoidance.html)

- 业务上具有唯一特性的字段，即使是多个字段的组合，也必须建成唯一索引
- 对长度大于50的 varchar 字段建立索引时，按需求恰当的使用前缀索引，或使用其他方法(例如增加int类型列col_crc32，然后对col_crc32建立索引)
- 合理创建联合索引(避免冗余)，区分度最高的在`最左边`，单个索引的字段数`不超过5个`
- 单张表的索引数量控制在5个以内，若单张表多个字段在查询需求上都要单独用到索引，需要经过DBA评估。查询性能问题无法解决的，应从产品设计，数据建模，技术架构上进行重构

## Explain
> [Explain](https://dev.mysql.com/doc/refman/8.0/en/using-explain.html)

- 使用 explain 判断SQL语句是否合理使用索引
    1. id：数字越大越先执行，一样大则从上往下执行，如果为NULL则表示是结果集，不需要用来查询。
    2. select_type：
    
    |  |  |
    |:----|:----|
    |simple            | 不需要union的操作或者是不包含子查询的简单select语句。|
    |primary           | 需要union操作或者含有子查询的select语句。|
    |union             | 连接两个select查询，第一个查询是dervied派生表，第二个及后面的表select_type都是union。|
    |dependent union   | 与union一样，出现在union 或union all语句中，但是这个查询要受到外部查询的影响。|
    |union result      | 包含union的结果集。|
    |subquery          | 除了from字句中包含的子查询外，其他地方出现的子查询都可能是subquery。|
    |dependent subquery| 与dependent union类似，表示这个subquery的查询要受到外部表查询的影响。|
    |derived           | from字句中出现的子查询，也叫做派生表，其他数据库中可能叫做内联视图或嵌套select。|

    3. table: 表名，如果是用了别名，则显示别名
    4. type 从上至下，好到差：除了all之外，其他的type都可以使用到索引，除了index_merge之外，其他的type只可以用到一个索引。

    |  |  |
    |:----|:----|
    |  |  |
    |system          | 表中只有一行数据或者是空表。|
    |const           | 使用唯一索引或者主键，返回记录一定是1行记录的等值where条件时，通常type是const。|
    |eq_ref          | 出现在要连接过个表的查询计划中，驱动表只返回一行数据，且这行数据是第二个表的主键或者唯一索引，且必须为not null，唯一索引和主键是多列时，只有所有的列都用作比较时才会出现eq_ref。|
    |ref             | 不像eq_ref那样要求连接顺序，也没有主键和唯一索引的要求，只要使用相等条件检索时就可能出现，常见与辅助索引的等值查找。|
    |fulltext        |  全文索引检索，要注意，全文索引的优先级很高，若全文索引和普通索引同时存在时，mysql不管代价，优先选择使用全文索引。|
    |ref_or_null     |  与ref方法类似，只是增加了null值的比较。实际用的不多。|
    |unique_subquery |  用于where中的in形式子查询，子查询返回不重复值唯一值。|
    |index_subquery  | 用于in形式子查询使用到了辅助索引或者in常数列表，子查询可能返回重复值，可以使用索引将子查询去重。|
    |range           |  索引范围扫描，常见于使用>,<,is null,between ,in ,like等运算符的查询中。|
    |index_merge     |  表示查询使用了两个以上的索引，最后取交集或者并集，常见and ，or的条件使用了不同的索引。|
    |index           |  索引全表扫描，把索引从头到尾扫一遍，常见于使用索引列就可以处理不需要读取数据文件的查询、可以使用索引排序或者分组的查询。|
    |all             |  这个就是全表扫描数据文件，然后再在server层进行过滤返回符合要求的记录。|

    5. possible_keys： 查询可能使用到的索引。
    6. key： 查询真正使用到的索引。
    7. key_len： 用于处理查询的索引长度。
    8. ref： 常数等值查询显示const，连接查询则显示表的关联字段。
    9. rows： 执行计划中估算的扫描行数，不是精确值。
    10. filtered： 表示存储引擎返回的数据在server层过滤后，剩下多少满足查询的记录数量的比例。
    11. extra： 该字段信息较多，这里就不一一叙述了。

- 在实际的使用过程中, 需要重点去关注type、key、key_len、rows、extra这几个参数， type要努力优化到**range级别**，all要尽量少的出现，在查询的过程中要尽量使用索引
- 在extra里面出现 Using filesort, Using temporary 是不太好的，要去优化提高性能。

- 通常情况下一个SQL语句只能在表上命中一个索引，但还有 索引合并 的情况 [参考: MySQL索引合并的使用与原理](https://blog.csdn.net/gentlezuo/article/details/107677543)  
    - intersect， union， sort-union

> 注意Explain返回的是可能的查询器和优化器的执行策略。  
> `explain analyze` 会将SQL真正执行并记录被拆分后的SQL执行环节的大致耗时

## 为何选择 B+ 树结构
> [参考:【原创】为什么Mongodb索引用B树，而Mysql用B+树?](https://www.cnblogs.com/rjzheng/p/12316685.html)  `MongoDB PostgreSQL 都是使用B-Tree`  
> [从 MongoDB 及 Mysql 谈B/B+树](https://blog.csdn.net/wwh578867817/article/details/50493940)  
> [分布式数据库千亿级超大表性能优化实践](http://www.itpub.net/2020/02/28/5356/)  

- 相较于平衡二叉树：节点的多叉导致数据节点发生变化时，调整成本更低，IO次数也更低
- MySQL Innodb 设计索引块是固定大小，中间节点上存放数据就会导致能用来存放指针数据的空间变小，也就意味着引用的子节点更少，树的高度更高（增加了IO次数），极端情况下退化为线性表。
- 叶子节点用双向链表连接，方便范围查询，索引排序
    - InnoDB B+树索引的每一层节点间，都通过前后指针组成双向链表相互连接
- 联合索引原理：依据字段顺序 例如 (a,b,c)，会先依据a有序，然后b有序，最后c有序的方式来组织B+树，据此才有`最左原则`的限制
    - 如果中间某列没有值或使用like会导致后面的列不走索引

> 特点：
- 叶子节点：
    - 如果是聚簇索引，则保存的是实际数据节点
    - 如果是非聚簇索引，保存的是主键id，需要走主键索引取数据

> [InnoDB索引同层非叶子节点间，也是双向链表吗？](https://juejin.cn/post/7259411780375085114) 数据结构层面展示MySQL的B+树实现

## 基本DDL
1. **创建**
    - ALTER 方式
        - 普通索引 `ALTER table ADD INDEX index_name(column1, column2);`
        - 唯一索引 ADD UNIQUE
        - 主键索引 ADD PRIMARY KEY
    - CREATE 方式
        - 普通方式 `CREATE INDEX index_name ON table_name (column_list)`
        - 唯一索引 `CREATE UNIQUE INDEX index_name ON table_name(column_list)`
1. **删除**
    - `DROP INDEX index_name ON talbe_name`
    - `ALTER TABLE table_name DROP INDEX index_name`
    - `ALTER TABLE table_name DROP PRIMARY KEY`      

1. **查看** 
    - `show index from tableName`
    - [Official Doc](https://dev.mysql.com/doc/refman/5.7/en/show-index.html)`详解命令的输出内容`

1. **强制使用索引**
    - `select * from test force index(idx_name) where id = 1;`

************************

# 索引的类型
- 按「数据结构」分类：B+tree索引、Hash索引、Full-text索引。
- 按「物理存储」分类：聚簇索引（主键索引）、二级索引（辅助索引）。
- 按「字段特性」分类：主键索引、唯一索引、普通索引、前缀索引。
- 按「字段个数」分类：单列索引、联合索引。

> 覆盖索引
- 覆盖索引（covering index，或称索引覆盖），即`仅从辅助索引中就可以得到查询的信息`，而不需要查询聚集索引甚至回表。

> 联合索引
- 两个或更多个列上的索引被称作联合索引，联合索引又叫复合索引

## 普通索引
是最基本的索引，只在单列上建立索引，无特殊限制

## 唯一索引
与前面的普通索引类似，不同的就是：索引列的值必须唯一，但允许有空值。如果是组合索引，则列值的组合必须唯一

## 主键索引
是一种特殊的唯一索引，一个表只能有一个主键，不允许有空值。
- 当创建表时没有显示定义主键时： 
    1. 首先判断表中是否有非空的整形唯一索引,如果有,则该列为主键(这时候可以使用 select _rowid from table 查询到主键列).
    2. 如果没有符合条件的则会自动创建一个6字节的主键(该主键是查不到的).

## 主键索引/聚集索引
聚集索引(Clustered Index)

聚集索引：指该索引决定了表中数据行**物理存储**排序方式的索引，因此`一个表只能有一个聚集索引`

而聚集索引（clustered index）就是按照每张表的主键构造一棵B+树，同时叶子节点中存放的即为`整张表的行记录数据`，也将聚集索引的叶子节点称为数据页。  
聚集索引的这个特性决定了索引组织表中数据也是索引的一部分。同B+树数据结构一样，每个数据页都通过一个双向链表来进行链接。

聚簇索引中的叶子节点记录了主键值、事务 id、用于事务和 MVCC 的回滚指针以及所有的剩余列。

## 辅助索引/非聚集索引
辅助索引（Secondary Index，也称非聚集索引）

叶子节点并不包含行记录的全部数据，只包含索引列 和 主键值（回查主键索引），辅助索引的存在并不影响数据聚集索引及数据存储，因此每张表上可以有多个辅助索引。  

当通过辅助索引来寻找数据时，InnoDB存储引擎会遍历辅助索引并通过叶节点级别的指针获得指向主键索引的`主键值`，然后再通过`主键索引`来找到一个完整的行记录，而 MyISAM 没有这个特性。
```sql
-- MySQL 5.7 
create table report_user_date(id bigint primary key auto_increment, user_id bigint,
 name varchar(32), avatar varchar(32), phone varchar(16), a_c int , b_c int, d_c int , e_c int, crea datetime);

alter table report_user_date add index idx_user(user_id,crea);

-- 如果只查询索引字段（user_id 或 crea），还能利用上联合索引，即使查询条件没有最左列
-- innodb 引擎时，由上述特性 查id 也能使用上联合索引，myisam 就不能了
explain select id  from report_user_date where crea < '2021-12-26';

-- 如果查询非索引字段，就用不上联合索引了; 字段越多，查询越慢
select name  from report_user_date where crea < '2021-12-26';
```

非聚集索引的使用场合为 查询所获数据量较少时 或者 某字段中的数据的唯一性比较高时， 非聚集索引必须是稠密索引`SQL查询的字段大部分有建索引`

************************

## Hash 索引
对于Innodb而言不支持完整的hash索引，只有AHI。MEMORY/HEAP/NDB 才支持

语法： `alter table xx add index idx_a(uid) using hash`

> 适用场景
1. 等值查询，索引列数据分散

> 限制和缺点
1. 哈希索引只保存哈希码和指针，而不存储字段值，所以不能使用索引中的值来规避回表问题
1. 哈希索引数据并不是按照索引值顺序存储的，所以无法用于排序和范围查询
1. 哈希索引不支持 部分索引值 查找，因为哈希索引始终是使用`索引列的全部内容`来计算哈希码。
1. HASH冲突（链地址法）会对整体维护加大负担（查询，新增，删除）。

> 优化
1. 假如查询字段A较长，可用新列B存储字段A的hash值，再基于B列建立Hash索引，优化索引存储大小

### AHI 自适应哈希索引
> [Adaptive Hash Index](https://dev.mysql.com/doc/refman/8.0/en/innodb-adaptive-hash.html)

- 自适应哈希索引 默认开启 `show variables like "innodb_adaptive_hash_index";` 
- 查看引擎状况，能看到hash索引使用情况 `show engine innodb  status;`

存储引擎会自动对个索引页上的查询进行监控，如果能够通过使用自适应哈希索引来提高查询效率，其便会自动创建自适应哈希索引，不需要开发人员或运维人员进行任何设置操作。
自适应哈希索引是`对innodb的缓冲池的B+树页进行创建，不是对整张表创建`，因此适用于热点数据，如果查询是离散平均的还是建议直接建Hash索引，不适用AHI。

## 全文索引

************************

# 需要使用索引的场景
1. 经常出现在 where 条件中的字段需添加索引。
2. join 关联，被驱动表需要对关联字段添加索引。
3. order by ，group by ，distinct的字段需要添加在索引的后面。

> 创建索引时避免有如下误解：
1. 宁滥勿缺。认为一个查询就需要建一个索引。
1. 宁缺勿滥。认为索引会消耗空间、严重拖慢更新和新增速度。
1. 抵制唯一索引。认为业务的唯一性一律需要在应用层通过“先查后插”方式解决。

## 索引优化
### 统计报表
> 如果使用MySQL存储 一定数据量的统计报表数据，使用 MyISAM 有更多优势, 没有事务，行锁等开销

```sql
    CREATE TABLE `report_user_date` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `user_id` bigint(20) DEFAULT NULL,
    `name` varchar(32) DEFAULT NULL,
    `avatar` varchar(32) DEFAULT NULL,
    `phone` varchar(16) DEFAULT NULL,
    `a_c` int(11) DEFAULT NULL,
    `b_c` int(11) DEFAULT NULL,
    `d_c` int(11) DEFAULT NULL,
    `e_c` int(11) DEFAULT NULL,
    `crea` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `idx_user` (`user_id`,`crea`)
    )
```

1. 构造测试数据
```go
    // 生成随机数据
    insertOne := "insert into report_user_date( user_id, name, avatar, phone, a_c, b_c, d_c, e_c,crea) value (?,?,?,?,?,?,?,?,?);"
	stmt, _ := db.Prepare(insertOne)
	now := time.Now()
	for i := 0; i < 100000; i++ {
		stmt.Exec(i%2000, fmt.Sprint(i), fmt.Sprint(i), fmt.Sprint(i), i, i+1, i+2, i+3, now.Add(time.Second*time.Duration(i)))
	}
    // 多次复制自身数据 扩大数据量 
    // insert into report_user_date( user_id, name, avatar, phone, a_c, b_c, d_c, e_c,crea) select user_id, name, avatar, phone, a_c, b_c, d_c, e_c,crea from report_user_date;
```
2. 对比查询效率
```sql
-- MySQL 5.7 340w数据

select user_id, count(a_c )  from report_user_date where user_id between 100 and 700  group by user_id ;
-- innodb 2700ms
-- myisam 900ms

select user_id, count(distinct a_c ),count(distinct b_c ) from report_user_date where user_id between 100 and 700 and crea < '2021-12-26 18:00:00' group by user_id ;
-- innodb 2700ms
-- myisam 1100ms

select user_id from report_user_date where crea < '2021-12-26';
-- 如果只查询索引字段，还能利用上联合索引，即使查询条件没有最左列字段， 如果查询非索引字段，就用不上联合索引了，字段越多，查询越慢
-- 如果查询的是id 主键字段：innodb 会使用上索引，myisam 就不能了
```

************************

# SQL查询未命中索引的场景

> 全局
- 如果MySQL分析器估计使用全表扫描要比使用索引快,则不使用索引(例如 全部记录数量少于10 等等)
- 通过索引扫描的记录数超过20%-30%，可能会变成全表扫描。`和查询条件无关`
    - 例如 使用 <> 或！= , is null 或 is not null [不影响使用索引](https://dev.mysql.com/doc/refman/5.5/en/is-null-optimization.html)，通常是因为扫描行数过多
- 注意: 索引列上存在 null 值, 索引仍能使用, 包括 is null 和 is not null, 但是 Null值可能会相比于默认值占用更多存储空间
- 使用了索引字段做条件过滤，但是使用了非索引字段来做Order by

> 联合索引
- 第一个索引列使用范围查询 >，in，bewteen 等等，导致后续字段无法走索引
- 最左前缀原则，查询条件不是最左索引列

> 单字段条件查询时
- 使用 or `但是如果所有的or条件都必须是独立索引，会使用索引`
    - 优化方向： 使用in代替or
- 模糊查询 条件列`最左`是通配符`%`
- 查询条件数据类型不匹配, 例如 `where name = 1`, 会导致索引失效，并且查询结果可能正常，可能非预期
    1. `where int_col='123'` 不会发生 **类型隐式转换**，可使用索引
    1. `where int_col='abc'` 'abc'被隐式转换为0，可使用索引
    1. `where char_col=123` 发生类型隐式转换，不会使用索引

> 其他
- HEAP表使用HASH索引时，使用范围检索或者ORDER BY
- 多表关联时，排序字段不属于驱动表，无法利用索引完成排序
- 两个独立索引，其中一个用于检索，一个用于排序(只能用到一个)
- JOIN查询时，关联列`数据类型/以及字符集/检验集`不一致也会导致索引不可用
- 对索引列进行运算（加减乘除等）
