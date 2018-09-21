`目录 start`
 
- [Hibernate](#hibernate)
    - [Hibernate基础配置](#hibernate基础配置)
        - [JDBC和Hibernate比较](#jdbc和hibernate比较)
            - [配置流程](#配置流程)
        - [Hibernate必需JAR](#hibernate必需jar)
        - [编写数据库表对应框架持久层的对象](#编写数据库表对应框架持久层的对象)
        - [hibernate.cfg.xml文件](#hibernatecfgxml文件)
        - [日志文件的配置](#日志文件的配置)
        - [SessionFactory和Session比较](#sessionfactory和session比较)
        - [OID的作用：](#oid的作用)
        - [id生成策略](#id生成策略)
        - [非普通类型](#非普通类型)
    - [Hibernate实体关联配置](#hibernate实体关联配置)
        - [一对多的配置](#一对多的配置)
            - [**注意 ：**](#注意-)
        - [多对多的配置](#多对多的配置)
            - [学生方配置](#学生方配置)
            - [课程方配置](#课程方配置)
        - [一对一的配置](#一对一的配置)
        - [使用多对一的技巧](#使用多对一的技巧)
            - [添加记录](#添加记录)
            - [删除记录](#删除记录)
        - [继承关系的配置](#继承关系的配置)
        - [Hibernate异常](#hibernate异常)
            - [could not find a getter for](#could-not-find-a-getter-for)
            - [个人总结](#个人总结)
        - [Hibernate对象的状态](#hibernate对象的状态)
            - [Session的方法](#session的方法)
            - [特别注意](#特别注意)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Hibernate
## Hibernate基础配置
### JDBC和Hibernate比较
* JDBC
    *   使用其简洁精悍，最快，但是使用时接收数据以及多方面的比较麻烦
* Hibernate
    *   单表操作是很便捷的，但是涉及到多表复杂操作时比较麻烦

#### 配置流程
> 如果后续需要添加表的话，就这个顺序
- **1 :**  先有数据库和表，建立cfg.xml文件配置好数据库的基本参数
- **2 :**  使用工具建立POJO持久类
- **3 :**  导入Hibernate所必需JAR包，最好使用Myeclipse的配置，自己导包总有一堆错误
- **4 :**  使用MyEclipse自动创建hbm.xml文件，还有各种文件。配置好hbm文件里关于表间关系的映射，或者在Myeclipse配置时手动选择
- **5 :**  配置好DAO类中事务开启和关闭，以及各种所必需的配置，若表没有设立主键，那么POJO类需要继承自动生成的抽象类（含有主键）
- **6 :**  调用DAO或者自己的Utils类，通过Hibernate来操作数据库

### Hibernate必需JAR
> Hibernate 3.6
- required目录下所有JAR都要导入
- jpa的JAR包（做注解用）
- 日志包：
    - slf4j-api-* .jar  该包是一个日志接口，需要一个JAR包的实现：
    - slf4j-log4j12.jar 该包是转换的JAR包
    - log4j-1.2.11.jar  实现的JAR包
- 数据库驱动包  mysql-connector-java-5.1.7-bin.jar
- 在src同级目录下新建一个lib目录，把JAR包复制进去，然后右击将jar文件  Add to build path 加入到类搜索路径里

###  编写数据库表对应框架持久层的对象
- 使用自己的工具类创建到对应的包下，或者用相关工具生成，类型要自己多加注意

### hibernate.cfg.xml文件
> 作为默认的主配置文件
- 数据库连接属性 驱动，url，用户名，密码
- 数据库方言 
- 辅助配置
- POJO类配置文件的映射
- etc/hibernate.properties里可以看到更多配置，数据库连接池，SQL优化等
- 在：project/core/src/main/resources/org/hibernate/下有各种dtd文件，
    - 可以为eclipse的xml配置自动提示功能

### 日志文件的配置
> 默认是Log4j, 
在etc下复制log4j.properties到src下，就可以了，本人ssh下复制log4j.xml就可以了

### SessionFactory和Session比较
* 【SessionFactory】 
>   重量级容器：消耗大量资源，不能有太多实例,二级缓存
通常将该工厂类是单例模式，一个工厂类实例表示一个数据库
所以Hibernate一般是不能跨数据库来做事务操作。但是EJB和JPA可以实现
>> 这个配置选项：
hibernate.hbm2ddl.auto create-drop 在一个数据库中创建，然后使用完关闭实例时就删除所有建立的表
hibernate.hbm2ddl.auto create 清除数据库的表及数据，重新创建表
hibernate.hbm2ddl.auto update 更改配置文件，能够在数据库进行操作（更新，建立）
hibernate.hbm2ddl.auto validate

* 【session】
>   轻量级的容器，一级缓存
是非线程安全的对象

### OID的作用：
> 在Hibernate中唯一标识对象的属性，每个实体都是必须要有OID的

### id生成策略
* assigned：要求用户去手动指定对象的OID；该对象ID的类型可以是任意的
* identity：MySQL的自动生成
* native：数据类型是数值型，id的生成策略为数据库底层自增长（数据库自己去决定使用哪种方式，MySQL用identity，Oracle用序列等）
* sequence：Oracle数据库推荐，数值型（Long）
* seqhilo oracle :推荐使用的策略，使用序列来搭配高低机制
* uuid.hex :32位字符
* uuid:
* hilo：类型为数值型（long） [实际开发中推荐使用]

> id = hi+lo (高位和低位进行组合)
sessionFactory实例化，高位就会加一，生成算法是：hi*(max lo +1)+lo;
    
```xml
    <generator class="hilo" >
    <param name="table">stu_hilo</param>
    <!-- 放高值的表名 最好是一个对象对应于一个高低值的表避免了并发-->
    <param name="cloumn">next_hi</param>
    <!-- 高的值放在表的哪个字段 -->
    <param name="max_lo">100</ param>
    <!-- 每个轮回值的上限是多少 虚拟机启动频繁就设小一些，避免编码的浪费-->
    </generator>
```

### 非普通类型
* Set集合：

```xml
    <set name="Nos" table="表">
        <key column="外码"></key><!-- 外码 是必须的 -->
        <element column="号码" type="string"/>
    </set>
```
* List集合:

```xml
    <list>
        <key></key>
        <index></index>
        <element></element>
    </list>
```
* 查询列 属性：
`<property name="" formula="(select sum() from 选修表 as u where u.id=id)"></property>`

## Hibernate实体关联配置
### 一对多的配置
* 注意：一定要两个都有oid的情况才能配置一对多的映射,不能是依赖于另一个主键类
* 一方：

```xml
    <set name="" [cascade=""]> 
        <key column="这是外键"></key>
        <one-to-many class="多方的类"></one-to-many>
    </set>
```
* 多方：
`<many-to-one name="" class="一方的类" column="外键，key要一致" />`
* 双向的关联，会有update的SQL语句的执行来维护关系，影响效率
* 多方维护：一方中set标签加inverse="true"一方就不会维护，代码一定要多方执行set**(*)
* 一方维护：一方代码一定要执行**.add*()

####  **注意 ：**
- 1.在一的一方，修改xml文件，添加一个set 属性，表示 多方 的一个集合
```xml
    <set name="类中属性名（集合）" inverse="true">
        <key>< column name="数据库列名"/></key>
        <one-to-many class="多方类路径"/>
    </set>
```
- 2.在一的一方，修改POJO持久类文件，添加一个hashset，用来存储多方，添加setget方法，名字就是配置文件里添加的那个名字 注意修改构造器

- 3.在多的一方，修改xml文件，置换掉那个外键，换成many-to-one标签，里面写上外键的列
`<many-to-one name="类中属性名（对象）" class="一方的类路径" column="数据库中列名"></many-to-one>`

- 4.在多的一方，修改POJO持久类文件，添加一个一方的对象添加setget方法，名字就是配置文件里添加的那个名字  注意修改构造器
    * 一方的set集合中有inverse属性，多方是没有的，Hibernate中inverse是和外键对应的，一方配置了inverse是false，一方就不会维护关系（外键），一般是给多方维护，因为效率高
    * cascade是对象和对象之间的操作，和外键没有关系
    * 处于持久化状态的对象在Session中，客户端不需要做Session的save/update 操作，Hibernate会自动的去检查处于持久化的对象的状态的属性是否发生改变，改变了就发送update语句。
        * 如果该对象是一方，在一的一方映射文件中有cascade=all时，Hibernate内部还会检查该持久化对象关联的集合，对此集合进行update操作，但是该操作和外键没有关系，只有当通过多方建立关系后，才能使外键有值。

### 多对多的配置

* 关系在第三方表中，和两张表本身没有关系
* 多对多维护关系，谁都能维护关系（效率是一样的）维护一般是在页面上进行的
* table 是多对多的中间表（存放了一个关系）
* key中的column一般是填当前配置文件中的id
* 多对多的配置是需要两个外键的
* 如果使用了反转并使用了级联，就只会保存实体，但是关系是没有维护的（就是不会插入到第三方表），和一对多一样的（一对多是外键列没有值）。
* ！！如果双方都级联了，必须要有一方inverse，不然会有重复维护的错误发生

#### 学生方配置
```xml
    <set name="students" table="student_course">
        <key column="cid"></key>
        <many-to-many class="Student" column="stu_id"></many-to-many>
    </set>
```
#### 课程方配置

```xml
    <set name="courses" table="student_course">
        <key column="stu_id"></key>
        <many-to-many class="Course" column="cid"></many-to-many>
    </set>
```

***********************************

### 一对一的配置
* 单向
    只要配置单向的配置文件添加：
    `<many-to-one name=""class="映射的类" column="数据库字段" unique="true"></many-to-one>`
* 双向
    * 一方 甲：
    `<many-to-one name="" class="乙方类"column="数据库字段" unique="true"></many-to-one>`
    * 一方 乙：
    `<one-to-one name="" class="甲方类" property-ref="甲方配置的标签的name"></one-to-one>`

********************
### 使用多对一的技巧
#### 添加记录
1. 当需要添加一个多方时，一看成课程，多看成成绩。当然的首先得有相关课程，再添加成绩记录。
2. 那就先实例化一个课程对象，配置好信息
3. 实例化多个成绩实例，再 课程对象.get**Set().add(成绩对象); 将成绩对象添加到集合中，
4. session.save(课程对象)；
> 注意：既然实现了这样的操作，那就说明了在实例化成绩的时候，不需要指定课程的值，那就需要添加一个构造器
#### 删除记录
1. 如果删除一方，那就会将一删除，如果没有配置级联，就会将多方的外键置空，不会删除多方表
2. 如何通过一方修改多方的一条, 把一方的set中的要修改的一条，（查找之前需要对象 = session.load(对象.class,主键名)将多方的数据加载进来）
    - 注意多方不能有空列必须指定一个默认值（是和构造器有关么？）
    - 再查找出来，修改再update，新增也是如此增加多的一方的时候，就是在一方的set中新增一条记录，多方的操作都体现在了一方那里

*****************************************
### 继承关系的配置
> 两种方式，一般采用前者
```xml
    <!-- 将子类插入到父类的配置文件 需要使用key来关联的-->
        <joined-subclass name="cn.hibernate.extend.Student" table="extend_student">
            <key column="id"></key>
            <property name="sru_id" type="long"></property>
        </joined-subclass>
    <!--
        union是相当于将父类的所有属性复制到子类里，是共享父类的OID，
        所以父类的OID是不能和子类的OID重复的
        不然 查询的时候就会报错,
        所以就需要改父类的主键生成策略是高低值（或者是手动set），可以手动配置高低值的表的生成
    -->
        <union-subclass name="cn.hibernate.extend.Student" table="union_student">
            <property name="sru_id" type="long"></property>
        </union-subclass>
```
*******************************************************
### Hibernate异常
#### could not find a getter for
原因：1 可能真的没写get方法，或者get方法不合规范 setget方法中不允许两个连续大写字母
        2 *.hmb.xml文件中的属性名和pojo持久类中属性名不一致（一定不能在表名中添加下划线）
        3 方法名写错（基本不可能，都是自动生成的）
        
#### 个人总结
当使用了没有 主键的表，使用Myeclipse自动创建配置文件，使用自己的Table2Class来生成POJO持久类，
就要继承对应的自动创建的抽象类，因为没有主键的表默认是将所有列看成一个主键，并且还会有添加一个id属性，
这样也说明还有一点就是，这种表的字段不能有叫做id的列

是不是可以不用手动去使用那个类，好像这里自动生成的一切都有，

自动生成会生成：
    对应POJO的抽象类，hbm配置文件，以及默认的几个类，HibernateSessionFactory，IBaseHibernateDao，
    对应的Dao（添加的时候默认是没有使用事务，所以需要手动修改）,添加，删除，都是依据主键的，
    至少要初始化主键，当然还得满足数据库的要求

### Hibernate对象的状态
> 主要是对象内存和Session中的状态区别，而不是Session和数据库

-  `临时态`：刚实例化对象。对象在数据库中不存在，Session中也不存在
-  `游离态`：刚实例化的对象，但是该对象手动指定了OID并且OID在数据库中已经存在，并且是没有绑定Session的（特殊的临时态）
    * 保存两个有关联关系的对象，update时，如果配置文件中配置了级联，就会一起保存，一般建议在一方级联
-  `持久态`：该对象在数据库中存在，该对象绑定在Session（一级缓存）中
-  `删除态`：session.delete(对象)，删除后对象从数据库和Session中都移除了，但是OID还在内存中。
    * 游离态delete后就成了删除态
    * 持久态delete后就成了删除态

#### Session的方法
- save
- update
- delete 
- saveOrUpdate 由入参的OID来自动选择是要save还是update
- merge 形参：临时态的对象。形参和Session没有任何关系，返回对象Object2（持久化对象），所以在Session关闭的时候Object2的更改会同步到数据库中
- get 将数据库中指定对象获取为持久态，查不到就是返回null
- load 懒加载。使用代理对象，延迟加载。用到了别的属性就去查数据库。查不到就抛异常
- flush 刷新Session
- evict 定点清除 将指定的对象从Session中移除，变成游离态
- clear 全部清除 
- close

#### 特别注意
* 一个对象（内存）不能存在于多个Session中，一个存，一个改的情况是会错误的
* 但是数据库中同一条记录可以实例化为多个对象（内存），那么这些对象（内存）放在不同的Session中是可以的

* get：
    * 只延迟加载有外键关联的那部分属性，没有使用就不会查询，只有用到了才会查询
    * 多方：立即加载就要在配置文件中将对应的属性中添加 fetch="join"
    * 一方：配置文件中set标签 加上lazy="false"（两条SQL），再添加 fetch="join"后就只有一条SQL语句，但是这个一方是不能做分页查询的
* load：
    * 在你确定OID是一定有的时候使用load提高效率，但是实际开发过程中用的少，因为实际上没有这么确定。

* 懒加载如果Session关闭了或者是对象游离态。就会有懒加载初始化的异常
