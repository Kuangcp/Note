---
title: MySQL
date: 2018-12-16 17:24:50
tags: 
    - MySQL
    - 基础
categories: 
    - 数据库
---

💠

- 1. [Mysql](#mysql)
    - 1.1. [规约](#规约)
- 2. [安装](#安装)
    - 2.1. [Ubuntu安装配置MySQL](#ubuntu安装配置mysql)
    - 2.2. [Docker安装](#docker安装)
    - 2.3. [图形化客户端](#图形化客户端)
    - 2.4. [命令行辅助工具](#命令行辅助工具)
- 3. [基本数据类型](#基本数据类型)
    - 3.1. [数值类型](#数值类型)
        - 3.1.1. [short](#short)
        - 3.1.2. [int](#int)
        - 3.1.3. [decimal](#decimal)
    - 3.2. [时间类型](#时间类型)
    - 3.3. [字符类型](#字符类型)
        - 3.3.1. [varchar](#varchar)
        - 3.3.2. [text](#text)
        - 3.3.3. [JSON](#json)
    - 3.4. [LongBlob](#longblob)
- 4. [数据库](#数据库)
    - 4.1. [创建](#创建)
    - 4.2. [修改](#修改)
    - 4.3. [导出和导入](#导出和导入)
- 5. [表](#表)
    - 5.1. [创建](#创建)
    - 5.2. [ALTER](#alter)
        - 5.2.1. [增删字段](#增删字段)
    - 5.3. [索引](#索引)
    - 5.4. [临时表](#临时表)
- 6. [视图](#视图)
- 7. [触发器](#触发器)
    - 7.1. [创建单语句的触发器](#创建单语句的触发器)
    - 7.2. [创建多语句的触发器](#创建多语句的触发器)
    - 7.3. [NEW 和 OLD关键字](#new-和-old关键字)
- 8. [存储过程](#存储过程)
    - 8.1. [基本结构示例](#基本结构示例)
- 9. [函数](#函数)
    - 9.1. [简单示例](#简单示例)
- 10. [常用命令集合](#常用命令集合)
    - 10.1. [查看数据库参数](#查看数据库参数)
        - 10.1.1. [查看连接状况](#查看连接状况)
    - 10.2. [自增长](#自增长)
    - 10.3. [主键约束的修改](#主键约束的修改)
    - 10.4. [修改表名](#修改表名)
    - 10.5. [定界符](#定界符)
    - 10.6. [关于时间](#关于时间)
        - 10.6.1. [常用函数](#常用函数)
        - 10.6.2. [获取当前时间与n个月之间的天数](#获取当前时间与n个月之间的天数)
        - 10.6.3. [datetime和timestamp区别](#datetime和timestamp区别)
    - 10.7. [插入外码](#插入外码)
- 11. [变量](#变量)
- 12. [基本流程语法](#基本流程语法)
- 13. [异常](#异常)
- 14. [用户管理](#用户管理)
    - 14.1. [查看](#查看)
    - 14.2. [创建](#创建)
    - 14.3. [修改](#修改)
        - 14.3.1. [授权](#授权)

💠 2024-10-09 16:33:39
****************************************
# Mysql
> [Official Download](https://dev.mysql.com/downloads/mysql/) | [Official Doc](https://dev.mysql.com/doc/)

> [key words](https://dev.mysql.com/doc/mysqld-version-reference/en/keywords-5-7.html)

> 注意: utf8 最大字节为3, 非标准意义上的 utf8 实现, utf8mb4 才是真正意义上的 utf8 `5.5.3才开始支持` utf8 一般情况不会出问题, 除非有 emoji 等等

> 书籍
- MySQL技术内幕： InnoDB存储引擎
- 高性能MySQL
- [MySQL 是怎样运行的：从根儿上理解 MySQL](https://juejin.cn/book/6844733769996304392)

## 规约
- 优先选择utf8字符集，需要存储emoji字符的，则选择utf8mb4字符集。不要单独定义字符集、校验集、存储引擎、行格式。
    - CREATE TABLE ... ENGINE = INNODB DEFAULT CHARSET = utf8 ROW_FORMAT = COMPACT，尽量不要单独指定这些选项。不同的字符集/校验集关联查询会导致索引失效，5.6、5.7默认的ROW_FORMAT不同，最好让其自行匹配当前版本。
- 小数类型为 decimal，禁止使用 float 和 double。
- varchar 是可变长字符串，不预先分配存储空间，长度不要超过 5000，如果存储长度大于此值，定义字段类型为 text，独立出来一张表，用主键来对应，避免影响其它字段索引效率
- 字段允许适当冗余，以提高查询性能，但必须考虑数据一致。冗余字段应遵循:
    - 不是频繁修改的字段。
    - 不是 varchar 超长字段，更不能是 text 字段。

# 安装
## Ubuntu安装配置MySQL
- 更新列表` sudo apt-get update `
- 安装MySQL `sudo apt-get install mysql-server mysql-client`
- 检查服务是否已经开启 ： `sudo netstat -tap | grep mysql `
  - （启动显示cp 0 0 localhost.localdomain:mysql *:* LISTEN - ）
- 启动服务 ： `sudo /etc/init.d/mysql restart `
- 查看编码 ： `status` 或者 `show variables like 'character_set_%`

_配置_
- 打开配置文件： `sudo gedit /etc/mysql/mysql.conf.d/mysqld.cnf`
    - 如果要允许远程访问，就注释掉 `bind-address`
    - 如果是服务器要配置远程访问 就 bind-address=服务器IP
    - 确保skip-networking被删除或者屏蔽，否则不支持TCP/IP 访问

```ini
[mysqld]
character-set-server=utf8
[client]
default-character-set = utf8
```

_重启_
- 重启MySQL ：`sudo systemctl restart mysql`

- 命令行连接
> mysql -h host -P port -u username  -p'password' database

## Docker安装
> [Docker安装MySQL](/Linux/Container/DockerSoft.md#MySQL) | [博客：Mysql有没有必要Docker化](http://www.infoq.com/cn/articles/can-mysql-run-in-docker)

## 图形化客户端
> Windows平台上 MySQL-Font HeidiSQL | [10个Mysql图形客户端](http://www.linuxidc.com/Linux/2015-01/111421.htm)

## 命令行辅助工具
> [mycli](https://github.com/dbcli/mycli) `自动补全功能`

********************************
# 基本数据类型
> [MySQL 数据类型](http://www.cnblogs.com/bukudekong/archive/2011/06/27/2091590.html)

## 数值类型
### short

### int

### decimal 
-  The declaration syntax for a DECIMAL column is DECIMAL(M,D). The ranges of values for the arguments are as follows:
   - M is the maximum number of digits (the precision). It has a range of 1 to 65.
   - D is the number of digits to the right of the decimal point (the scale). It has a range of 0 to 30 and must be no larger than M. 
- 在MySQL 3.23 及以后的版本中，DECIMAL(M, D) 的取值范围等于早期版本中的DECIMAL(M + 2, D) 的取值范围。
1. 当插入的整数部分的值超过了其表示范围后就直接忽略了小数部分的值，并以最大值填充。 
2. 当整数部分合法，小数部分多余的位数，直接截断。

## 时间类型
- bigint 存入时间戳
- date
- time
- datetime 
- timestamp

> 注意 只有 timestamp 是含时区信息的，因为客户端写入值时取会话时区转换为UTC值（例如 1997-07-16T19:20+08:00 ），查询时MySQL会从UTC转为客户端会话的时区。
> datetime类型更像是存储了格式化的字符串。

> [MySQL日期类型选择建议](https://javaguide.cn/database/mysql/some-thoughts-on-database-storage-time.html)
- 空间效率timestamp更好，但是最大值到2038年，bigint可读性差但是兼容性好时区处理留给了应用层。


> 报错： Zero date value prohibited
- MySQL数据库在面对0000-00-00 00:00:00日期的处理时，如果没有设置对应的对策，就会产生异常
    - 可以配置处理 策略 exception 异常（默认值）， round 近似值， convertToNull(转为null)
    - 例如 JDBC URL添加参数 zeroDateTimeBehavior=convertToNull

************************

## 字符类型
### varchar
### text

### JSON
> [The JSON Data Type](https://dev.mysql.com/doc/refman/8.4/en/json.html)  


## LongBlob
- 这种数据类型可以直接把图像文件存到数据库中！
创建UTF8编码数据库 `CREATE DATABASE `test2` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci`

*****************************
# 数据库

## 创建
> create database name;

## 修改
- 转换表所有字段编码 `alter table a convert to character set utf8mb4;`
- 修改单个字段编码 `alter table a modify name  varchar(100) character set utf8mb4;`

## 导出和导入
> 以下的 -p -h 参数依数据库的配置情况而定

1. 只导出数据库的结构 `mysqldump -uroot -pmysql -d dbname > /data/backup/sql/dbname.sql`  
    - 导出具体的表就在 数据库名 后加上 表名
    - 导出结构和数据 去掉-d参数
1. 导入
    - 执行SQL文件 `source /path/to/dbname.sql` 特别注意文件的路径问题， 是以MySQL客户端运行时的路径为根路径的
    - 或者 `mysql -uusername -ppassword database < /path/sqlfile.sql;`

> [数据库迁移 Java工具的实现](https://blog.csdn.net/EASYgoing00/article/details/72885280)  主要的思路是Java调用系统命令行执行命令后得到导出文件， 然后读取导出的文件 进一步操作

大数据量表的导出： 常规使用分页分批加载到Excel中，改进版则使用长连接，流查询方式加载数据

************************

# 表
## 创建
- `create table name (field int, field varchar(32)....);`
- 查看表的创建语句 `show create table name;`

## ALTER
> [Official Doc](https://dev.mysql.com/doc/refman/5.7/en/alter-table.html)

_重命名表格_ `RENAME TABLE old TO new `

### 增删字段
- 增加字段 `alter table name add field1 int, field2 varchar(20);`
- 删除字段 `alter table name drop column field1, drop column field2;`
- 重命名字段 `alter table name change old_name new_name bigint;`

************************
## 索引
> [MySQL Index](/Database/MySQLIndex.md)

## 临时表
> [CREATE TEMPORARY TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-temporary-table.html)  

场景： 依据计算需要，从原始表过滤聚合后的数据放入临时表，不同的交互流程后，将临时表删除。是否可在Session级别无感实现。
方案： 

************************

# 视图
> 保障数据安全性，提高查询效率

> [参考: ](http://www.jb51.net/article/36363.htm)
```sql
    CREATE [ALGORITHM]={UNDEFINED|MERGE|TEMPTABLE}]
        VIEW 视图名 [(属性清单)]
        AS SELECT 语句
        [WITH [CASCADED|LOCAL] CHECK OPTION];
```
- ALGORITHM表示视图选择的算法（可选参数）
    - UNDEFINED：MySQL将自动选择所要使用的算法
    - MERGE：将视图的语句与视图定义合并起来，使得视图定义的某一部分取代语句的对应部分
    - TEMPTABLE：将视图的结果存入临时表，然后使用临时表执行语句
- 视图名表示要创建的视图的名称
- 属性清单表示视图中的列名，默认与SELECT查询结果中的列名相同（可选参数）
- WITH CHECK OPTION表示更新视图时要保证在该试图的权限范围之内（可选参数）
    - CASCADED：更新视图时要满足所有相关视图和表的条件
    - LOCAL：更新视图时，要满足该视图本身定义的条件即可
> tips：创建试图时最好加上WITH CASCADED CHECK OPTION参数，这种方式比较严格,可以保证数据的安全性

# 触发器
## 创建单语句的触发器
- `CREATE TRIGGER ins_sum BEFORE INSERT ON account FOR EACH ROW SET @sum = @sum + NEW.amount;`
- `CREATE TRIGGER trigger_name trigger_time trigger_event ON tbl_name FOR EACH ROW trigger_stmt`

## 创建多语句的触发器
```sql
      CREATE TRIGGER trigger_name trigger_time trigger_event
          ON tbl_name FOR EACH ROW
      BEGIN
          .......
      END
```
## NEW 和 OLD关键字
- 使用OLD和NEW关键字，能够访问受触发程序影响的行中的列（OLD和NEW不区分大小写）。在INSERT触发程序中，仅能使用NEW.col_name，没有旧行。
- 在DELETE触发程序中，仅能使用OLD.col_name，没有新行。在UPDATE触发程序中，可以使用OLD.col_name来引用更新前的某一行的列，也能使用NEW.col_name来引用更新后的行中的列。
- 用OLD命名的列是只读的。你可以引用它，但不能更改它。对于用NEW命名的列，如果具有SELECT权限，可引用它。
- 在BEFORE触发程序中，如果你具有UPDATE权限，可使用“SET NEW.col_name = value”更改它的值。这意味着，
- 你可以使用触发程序来更改将要插入到新行中的值，或用于更新行的值。
- 在BEFORE触发程序中，AUTO_INCREMENT列的NEW值为0，不是实际插入新记录时将自动生成的序列号。

************************

# 存储过程
## 基本结构示例
```sql
       -- loop 要有iterate 和leave才是完整的
    CREATE PROCEDURE doiterate(p1 INT)
      BEGIN
        label1: LOOP
          SET p1 = p1 + 1;
          IF p1 < 10 THEN ITERATE label1; END IF;
          LEAVE label1;
        END LOOP label1;
        SET @x = p1;
      END
      call doiterate(7);
      select @x;
```

************************

#  函数
## 简单示例

```sql
    ---函数部分,修改定界符 
    delimiter //
    CREATE FUNCTION hello (s CHAR(20)) RETURNS CHAR(50)
    RETURN CONCAT('Hello, ',s,'!');
    //
    --将定界符改回来，是第二句SQL语句
    delimiter ;
    select hello('Myth ');
    drop function hello;
    -- 函数
    create function fun_test(var1 int,var2 varchar(16)) returns int
    begin 
        declare temp int;
        select count(*) into temp from test;
        return temp;
    end;
    select fun_test(8,'d');
```

************************

# 常用命令集合
## 查看数据库参数
### 查看连接状况
> [查看mysql数据库连接数、并发数相关信息。](https://blog.csdn.net/caodongfang126/article/details/52764213)`show status like 'Threads%';`

- 查看连接 show processlist  如果是普通用户，只能查看自己当前的连接状态
- 查看表的状态 show table status like 'assitant' 可以看到当前自动增长的id当前值 

## 自增长
- 创建表时设置自增长，并设置起始值
    - create table cc( id int auto_increment,name varchar(20),primary key(id) ) auto_increment=1000;
- 设置已有字段自增长 
    - alter table test MODIFY id INT UNSIGNED AUTO_INCREMENT;
- 自增长的修改 
    - alter table test auto_increment=10； 注意只能改的比当前的值大，不可以改的比当前小
- 自增长字段溢出
    - 设置自动增长的列，只能是int类型（包含了各种int），当出现了溢出就可以改成bigint 但是如果有外键约束，可能就会更改失败，还不如删库重建，实在太大了就删约束再建约束

## 主键约束的修改
alter table 表名  add constraint (PK_表名) primary key (j,k,l); 关于一些约束条件constraint好像没有起到作用比如 check

## 修改表名
rename table table1 to table2; 	切记不可随便修改表名，改了就要修改相应的 外键，触发器，函数，存储过程！！！

## 定界符
delimiter 任意字符除了转义字符：\

************************

## 关于时间 
### 常用函数
- **NOW()**函数以 'YYYY-MM-DD HH:MM:SS' 返回当前的日期时间，可以直接存到**DATETIME**字段中。
- **CURDATE()**以’YYYY-MM-DD’的格式返回今天的日期，可以直接存到**DATE**字段中。
- **CURTIME()**以’HH:MM:SS’的格式返回当前的时间，可以直接存到**TIME**字段中。
   - 例：insert into tablename (fieldname) values (now())
   - insert into data values ('Myth','4','2016-03-10',curtime());//年月日，时间
   - select datediff(curdate(), date_sub(curdate(), interval i month)); 
- 一般函数是不能作为 default默认值的，使用只能在插入修改数据时使用

### 获取当前时间与n个月之间的天数
- 问题：假设当前是5月19 且（提前月份）n=1 就是计算从4月19到今天的天数
    ```sql
        -- 时间格式的简单操作：
        select DATE_FORMAT(produceDate, '%Y') as yeahr from historybarcodesort
            where DATE_FORMAT(produceDate, '%Y')='2013'
        select date_format('1997-10-04 22:23:00','%y %M %b %D %W %a %Y-%m-%d %H:%i:%s %r %T');
            显示结果：97 October Oct 4th Saturday Sat 1997-10-04 22:23:00 10:23:00 PM 22:23:00
        -- 查询指定时间：
        get_date = "2006-12-07"
        SELECT count(*) FROM t_get_video_temp Where DATE_FORMAT(get_date, '%Y-%d')='2006-07';
        SELECT count(*) FROM t_get_video_temp Where get_date like '2006%-07%';
    ```

### datetime和timestamp区别
```sql
    -- 问题：为什么 5.5的环境下运行两句命令得到不同的结果（5.6不会报错）
    creata table test1(one_time timestamp not null default current_timestamp,two_time timestamp);
    -- 报错：Incorrect table definition; there can be only one TIMESTAMP column with CURRENT_TIMESTAMP in DEFAULT or ON UPDATE clause
    create table test2(one_time timestamp,two_time timestamp not null default current_timestamp);
    或者 将timestamp 改成datetime 也不会有错，那么问题来了 区别是什么？
    -- 上面报错原因不明，大意是只能有一个timestamp的列有默认值
```

**DATETIME、DATE 和 TIMESTAMP 区别：**
- **DATETIME** 类型可用于需要同时包含日期和时间信息的值。MySQL以'YYYY-MM-DD HH:MM:SS' 格式检索与显示DATETIME类型。
    - 支持的范围是 '1000-01-01 00:00:00' 到 '9999-12-31 23:59:59'。
    - (“支持”的含义是，尽管更早的值可能工作，但不能保证他们均可以。)
- **DATE** 类型可用于需要一个日期值而不需要时间部分时。MySQL 以 'YYYY-MM-DD' 格式检索与显示 DATE 值。
    - 支持的范围是 '1000-01-01' 到 '9999-12-31'。
- **TIMESTAMP** 列类型提供了一种类型，通过它你可以以当前操作的日期和时间自动地标记 Insert 或Update 操作。
    - 如果一张表中有多个 TIMESTAMP 列，只有第一个被自动更新。

> “完整”TIMESTAMP格式是14位，但TIMESTAMP列也可以用更短的显示尺寸创造
最常见的显示尺寸是6、8、12、和14。
你可以在创建表时指定一个任意的显示尺寸，但是定义列长为0或比14大均会被强制定义为列长14
列长在从1～13范围的奇数值尺寸均被强制为下一个更大的偶数。

> 例如：
定义字段长度 强制字段长度
```
TIMESTAMP(0) -> TIMESTAMP(14)
TIMESTAMP(15)-> TIMESTAMP(14)
TIMESTAMP(1) -> TIMESTAMP(2)
TIMESTAMP(5) -> TIMESTAMP(6)
```
> 所有的TIMESTAMP列都有同样的存储大小，
使用被指定的时期时间值的完整精度（14位）存储合法的值不考虑显示尺寸。
不合法的日期，将会被强制为0存储

 **自动更新第一个 TIMESTAMP 列在下列任何条件下发生：**
- 列值没有明确地在一个 Insert 或 LOAD DATA INFILE 语句中被指定。
- 列值没有明确地在一个 Update 语句中被指定，并且其它的一些列值已发生改变。(注意，当一个 Update 设置一个列值为它原有值时，这将不会引起 TIMESTAMP 列的更新，因为，如果你设置一个列值为它当前值时，MySQL 为了效率为忽略更新。)
- 明确地以 NULL 设置 TIMESTAMP 列。
- 第一个列以外其它 TIMESTAMP 列，可以设置到当前的日期和时间，只要将该列赋值 NULL 或 NOW()。
- 任何 TIMESTAMP 列均可以被设置一个不同于当前操作日期与时间的值，这通过为该列明确指定一个你所期望的值来实现。这也适用于第一个 TIMESTAMP 列。这个选择性是很有用的，举例来说，当你希望 TIMESTAMP 列保存该记录行被新添加时的当前的日期和时间，但该值不再发生改变，无论以后是否对该记录行进行过更新：
- 当该记录行被建立时，让 MySQL 设置该列值。这将初始化该列为当前日期和时间。
- 以后当你对该记录行的其它列执行更新时，为 TIMESTAMP 列值明确地指定为它原来的值。
- 另一方面，你可能发现更容易的方法，使用 DATETIME 列，当新建记录行时以 NOW() 初始化该列，以后在对该记录行进行更新时不再处理它。

## 插入外码
```sql
alter table `Bookinfo` add constraint `F_N` foreign key `F_N`(`classno`) references `Bookclass`(`classno`) on delete cascade on update cascade;
```

************************

# 变量
- 加了@ 的是用户变量， 限定当前用户，当前客户端， 在declare中声明的参数可以不加 @，那就是是局部变量
- 例如：declare a int ;  也可以直接就用不用声明，作为临时变量 例如这两种写法：
   - set @name =   expr;
	- select @name:= expr;
- 注意：MySQL中只有基本数据类型，没有Oracle中那个绑定类型：表类型或行类型，所以处理起来有点。。不如Oracle方便，不管是触发器还是存储过程
- set @a= select * from User；执行这句话就会报出 operand should contain 1 column(s)错误，就是说多值赋值的错误

# 基本流程语法
```sql
	if ... then 
	elseif ... then (注意elseif中间没有空格)
	end if;
```

************************

# 异常

************************

# 用户管理
> [参考博客](http://www.cnblogs.com/fslnet/p/3143344.html)

## 查看
- 查询用户信息 `select host,user,password from user ;`
- 查看权限 `show grants for zx_root;`

## 创建
> 创建本地超级用户： CREATE USER 'myth'@'localhost' IDENTIFIED BY 'ad';   
> 授予所有权限 GRANT all privileges  ON *.* TO 'myth'@'localhost';   
> 创建远程访问指定数据库用户 ： CREATE USER 'myth'@'%' IDENTIFIED BY 'ad';   
> 授予数据库db的所有权限 GRANT all privileges  ON db.* TO 'myth'@'%';

- 创建用户 `CREATE USER 'username'@'host' IDENTIFIED BY 'password';`
- 设置密码 `SET PASSWORD FOR 'username'@'%' = PASSWORD("123456");`
    - 修改密码也是这个语句注意的是要  `flush privileges;`
- 删除用户 `drop user 'username'@'host'`
    - 如果服务器需要远程访问 修改配置文件`/etc/mysql/mysql.conf.d/mysqld.cnf`，注释掉 bind_address 一行
```
    %            匹配所有主机
    localhost    localhost不会被解析成IP地址，直接通过UNIXsocket连接
    127.0.0.1    会通过TCP/IP协议连接，并且只能在本机访问；
    ::1          ::1就是兼容支持ipv6的，表示同ipv4的127.0.0.1
```
## 修改
- 修改名字：`rename user feng to newuser；`

### 授权
1. grant all privileges  ON databasename.tablename TO 'username'@'host' 
    - all privileges 所有权限
    - alter | alter routine
    - create | create routine | create temporary table | create user | create view
    - delete | drop
    - execute | file
    - index | insert
    - lock table | process | reload
    - replication | client | replication slave
    - select | show databases | show view
    - shutdown | super
    - update | usage
2. 回收权限 revoke, 用法和 grant 一样

- 刷新权限缓存 `flush privileges;`
