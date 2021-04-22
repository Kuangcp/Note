# MySQL innodb锁设计细节
> [InnoDB Locking and Transaction Model](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking-transaction-model.html)

## 共享/排他锁(Shared and Exclusive Locks)
> 共享锁(S)和排他锁(X)是InnoDB引擎实现的`行级别锁`。 

拿共享锁是为了让当前事务去读某一行数据，排他锁则是为了修改或删除某一行数据。

## 意向锁(Intention Locks)
> 意向锁存在的意义在于，使得行锁和表锁能够共存。 `意向锁是表级别锁`，用来说明事务稍后会对表中的数据行加哪种类型的锁(共享锁或独占锁)。

当一个事务A对表加了意向排他锁(IX)时，另外一个事务在加锁前就会通过该表的意向排他锁知道前面已经有事务在对该表进行独占操作，从而等待。

|   |  X  |   IX  |  S |  IS
|:---|:---|:---|:---|:---|
X 	| ❌ | ❌ | ❌ | ❌
IX 	| ❌ |   | ❌ | 
S 	| ❌ | ❌ |   | 
IS 	| ❌ |   |   | 

## 记录锁(Record Locks)
> `记录锁是索引记录上的锁`

例如：SELECT c1 FROM t WHERE c1 = 10 FOR UPDATE;会阻止其他事务对c1=10的数据行进行插入、更新、删除等操作。

记录锁总是锁定索引记录。如果一个表没有定义索引，那么就会去锁定隐式的“聚集索引”。

## 间隙锁(Gap Locks)
> 间隙锁是一个在索引记录之间的间隙上的锁。

一个间隙可能跨越单个索引值、多个索引值，甚至为空。

对于使用唯一索引 来搜索唯一行的语句，只加记录锁不加间隙锁(这并不包括组合唯一索引）。

## 临键锁(Next-key Locks)
> Next-Key Locks是行锁与间隙锁的组合。

当InnoDB扫描索引记录的时候，会首先对选中的索引记录加上记录锁（Record Lock），然后再对索引记录两边的间隙加上间隙锁（Gap Lock）。

## 插入意向锁(Insert Intention Locks)
> 插入意向锁是在数据行插入之前 设置的间隙锁定类型。

如果多个事务插入到相同的索引间隙中，并且它们不在间隙中的相同位置插入，则无需等待其他事务。  
例如：在4和7的索引间隙之间两个事务分别插入5和6，则两个事务不会发冲突阻塞。 

## 自增锁(Auto-inc Locks)
> 自增锁是事务插入到有自增列的表中而获得的一种特殊的`表级锁`。

如果一个事务正在向表中插入值，那么任何其他事务都必须等待，保证第一个事务插入的行是连续的自增值。

************************
## MVCC机制
> [InnoDB Multi-Versioning](https://dev.mysql.com/doc/refman/8.0/en/innodb-multi-versioning.html)

> [MySQL InnoDB MVCC机制](https://www.jianshu.com/p/d67f0329d3bf)

锁开销较大，因此引入MVCC(快照读)： 读不加锁，读写不冲突。在读多写少的场景下极大的增加了系统的并发性能。`只在RC和RR下生效, 因为读未提交不需要(已经不在意一致性了)，序列化同样不需要(绝对不会出现一致性问题)`

Innodb 内部在每行有隐藏列：
1. DB_TRX_ID    6-byte 事务id，每处理一个事务，值自动加一。
1. DB_ROLL_PTR  7-byte 回滚指针， 指向 undo 记录
1. DB_ROW_ID    6-byte 行id， 2^48，如果没有手动设置主键，rowId溢出时会发生数据覆盖(rowId循环使用)

> 每条记录的头信息（record header）里都有一个bit（deleted_flag）来表示当前记录是否已经被删除

在多个事务并行操作某行数据的情况下，不同事务对该行数据的UPDATE会产生多个版本，数据库通过DB_TRX_ID来标记版本，然后用DB_ROLL_PT回滚指针将这些版本以先后顺序连接成一条 Undo Log 链。

> [innodb-consistent-read](https://dev.mysql.com/doc/refman/8.0/en/innodb-consistent-read.html)
一致性视图的生成 ReadView

在read committed级别下，readview会在事务中的每一个SELECT语句查询发送前生成（也可以在声明事务时显式声明START TRANSACTION WITH CONSISTENT SNAPSHOT），因此每次SELECT都可以获取到当前已提交事务和自己修改的最新版本。而在repeatable read级别下，每个事务只会在第一个SELECT语句查询发送前或显式声明处生成，其他查询操作都会基于这个ReadView，这样就保证了一个事务中的多次查询结果都是相同的，因为他们都是基于同一个ReadView下进行MVCC机制的查询操作。
