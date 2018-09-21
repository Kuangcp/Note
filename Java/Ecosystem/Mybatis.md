`目录 start`
 
- [Mybatis](#mybatis)
    - [Mybatis](#mybatis)
        - [xml文件配置：](#xml文件配置)
            - [主配置文件：](#主配置文件)
                - [操作配置文件：](#操作配置文件)
        - [导入JAR包：](#导入jar包)
        - [创建SqlSessionFactory类 内容：](#创建sqlsessionfactory类-内容)
            - [maven Spring-mybaits 配置](#maven-spring-mybaits-配置)
                - [**SessionFactory类，使用Spring注入一个工厂类，然后使用本地线程组，节省Session开销**](#sessionfactory类使用spring注入一个工厂类然后使用本地线程组节省session开销)
        - [流程控制](#流程控制)
            - [foreach 循环语句](#foreach-循环语句)
                - [collection 有 arry list map 几种 还有item是必写，其他的是可选的](#collection-有-arry-list-map-几种-还有item是必写其他的是可选的)
            - [if 判断语句:](#if-判断语句)
            - [set 方便书写update语句](#set-方便书写update语句)
            - [choose 相当于switch语句](#choose-相当于switch语句)
                - [$和的区别：](#$和的区别)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Mybatis
> 一个灵活的数据库中间件框架


## Mybatis
### xml文件配置：
- 创建mybatis-config.xml文件
    - 该文件是主配置文件，配置了sessionFactory
- 创建generatorConfig.xml文件
    - 是各种操作的配置，一个操作对应一个SQL的配置

#### 主配置文件：
```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
    "http://mybatis.org/dtd/mybatis-3-config.dtd">
    <configuration>
    <!-- 配置别名 为了方便配置操作文件--> 
    <typeAliases> 
        <typeAlias type="cn.mybatis.test.Human" alias="Human" />  
    </typeAliases> 
    <!-- 配置环境变量 --> 
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/test?characterEncoding=UTF-8"/>
                <property name="username" value="root"/>
                <property name="password" value="123456"/>
            </dataSource>
        </environment>
    </environments>
    <!-- 配置mappers --> 
    <mappers> 
        <mapper resource="cn/mybatis/test/HumanDao.xml" />  
    </mappers> 
    </configuration>
```
##### 操作配置文件：
```xml
    <?xml version="1.0" encoding="UTF-8" ?> 
    <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd"> 
    <mapper namespace="cn.mybatis.test"> 
        <!-- 按id查询 -->
        <select id="queryUsersById" parameterType="Human" resultType="Human">  
            <!-- useCache="false" -->
            <![CDATA[ 
          select * from inserts t where t.id=#{id}
          ]]>  
        </select>  
        <!-- 查询全部 -->
        <select id="queryUsers" resultType="Human">
            select * from inserts
        </select>
        <!-- 插入记录 -->    
        <insert id="insertUser" parameterType="Human" >
        <!-- 该字段是必须要在数据库中自增长的
            可能会有并发问题
            useGeneratedKeys="true" keyProperty="id"
            所以用查询方式好点， 写语句就不要考虑主键了
         -->
            <selectKey resultType="int" keyProperty="id">
                select LAST_INSERT_ID()
            </selectKey>
            insert into inserts (name) values(#{name})
        </insert>
        <!-- 删除记录 -->
        <delete id="deleteUser" parameterType="String">
            delete from inserts where id=#{id}
        </delete>
        <!-- 更新记录 -->
        <update id="updateUserById" parameterType="Human">
            update inserts set name=#{name} where id=#{id}
        </update>
    </mapper> 
```
### 导入JAR包：
- **核心包**
- mybatis-3.4.1.jar 主包
- dom4j-1.6.1.jar 日志记录
- log4j-1.2.15.jar
- slf4j-api-1.5.8.jar
- slf4j-log4j12.jar

###  创建SqlSessionFactory类 内容：
```java
    private static SqlSessionFactory sessionFactory;
    static{
        try{
            String resource = "cn/mybatis/test/mybatis-config.xml";
            InputStream inputStream = Resources.getResourceAsStream(resource);
            sessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
        }catch (Exception e) {
            System.out.println("获取Session失败");
        }
    }
    /**
     * 获取Session
     */
    public static SqlSession getSession(){
        SqlSession session = null;
        session = sessionFactory.openSession();
        return session;
    }
```

#### maven Spring-mybaits 配置
- 使用Spring自动注入对象,方便别名和SessionFactory的管理
- pom引入必须的JAR包就可以了

```xml
      <!--基本属性-->
      <bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
           <property name="driverClass" value="${driver}"/>
           <property name="jdbcUrl" value="${url}"/>
           <property name="user" value="${username}"/>
           <property name="password" value="${password}"/>
           <property name="initialPoolSize" value="${initialSize}"/>
           <property name="maxPoolSize" value="${maxSize}"/>
       </bean>
       <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
           <property name="dataSource" ref="dataSource"/>
           <!--操作配置文件的路径-->
           <property name="mapperLocations" value="classpath:bean/*.xml"/>
           <!--bean的路径，进行别名的自动扫描-->
           <property name="typeAliasesPackage" value="com.book.bean"/>
       </bean>
       <bean id="mybatisSessionFactory" class="com.book.dao.MybatisSessionFactory">
           <property name="sessionFactory" ref="sqlSessionFactory"/>
       </bean>
       <!--定义数据源-->
       <tx:annotation-driven transaction-manager="transactionManager" />
       <bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
           <property name="dataSource" ref="dataSource"/>
       </bean>
```

#####  **SessionFactory类，使用Spring注入一个工厂类，然后使用本地线程组，节省Session开销**

```java

    @Component
    public class MybatisSessionFactory {
       @Autowired
       private  SqlSessionFactory sessionFactory;
       // 日志
       private static org.slf4j.Logger Log = LoggerFactory.getLogger(MybatisSessionFactory.class);
       //使用本地线程组能避免不必要的Session开支，加强性能
       private static final ThreadLocal<SqlSession> THREAD_LOCAL = new ThreadLocal<SqlSession>();
       /**
        * 获取Session
        * @return
        */
       public  SqlSession getSession(){
           SqlSession session = (SqlSession)THREAD_LOCAL.get();
           if(session==null ){
               session = this.sessionFactory.openSession();
               THREAD_LOCAL.set(session);
           }
           Log.info("__获取了一个Session__"+session);
           return session;
       }
       /*
           关闭连接
        */
       public void closeSession(){
           SqlSession session = (SqlSession)THREAD_LOCAL.get();
           THREAD_LOCAL.set(null);
           if(session!=null){
               session.close();
           }
       }
       public  SqlSessionFactory getSessionFactory() {
           return sessionFactory;
       }
       public  void setSessionFactory(SqlSessionFactory sessionFactory) {
           this.sessionFactory = sessionFactory;
       }
    }
```

### 流程控制

#### foreach 循环语句
```xml
    <foreach collection="param_list 自定义的话就是Map中的key，或者使用 @Param("")来指定 " item="params" index="currentIndex 当前索引"  separator="循环分隔符" open="在循环前加上字符" close="循环结束后加上字符">
        ${params}
    </foreach>
```
##### collection 有 arry list map 几种 还有item是必写，其他的是可选的
#### if 判断语句:
- `<if test=""></if>`

#### set 方便书写update语句
- `<set><if test="col!=null">col=#{col},</if></set>`

> mybatis会自动去除多余的逗号，但是每一行书写要写逗号

#### choose 相当于switch语句
- `<choose><when test=""></when></choose>`

#### $和#的区别：
- \$ 会有SQL注入的漏洞，#则没有
- 使用$ 是SQL进行String的拼接，使用#是preparstatement的预处理然后注入
- 使用#的时候出现这个问题
2017-01-22 11:16:11.046 [main] DEBUG myth.book.getAll_Param_BookType - ==>  Preparing: select * from book_type where ? and ? and 1=1; 
2017-01-22 11:16:11.136 [main] DEBUG myth.book.getAll_Param_BookType - ==> Parameters:  book_type<10 (String),  'father_type='2 (String)
- 条件不能使用数值，
    条件是单独使用时也是String但是是有效的
