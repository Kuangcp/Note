`目录 start`
 
- [数据库模块](#数据库模块)
    - [Relational Database](#relational-database)
        - [多数据源配置](#多数据源配置)
        - [连接池](#连接池)
            - [c3p0](#c3p0)
            - [druid](#druid)
            - [HikariPool](#hikaripool)
        - [JPA](#jpa)
        - [Mybatis](#mybatis)
            - [自定义查询](#自定义查询)
                - [HQL](#hql)
                - [原生SQL](#原生sql)
            - [Mysql](#mysql)
            - [映射关系](#映射关系)
                - [一对一](#一对一)
                - [一对多](#一对多)
                - [多对多](#多对多)
        - [Restful设计](#restful设计)
            - [【特别注意】](#特别注意)
        - [Jpa数据分页](#jpa数据分页)
        - [数据库上的事务支持](#数据库上的事务支持)
    - [Non Relational database](#non-relational-database)
        - [JPA](#jpa)
            - [Redis的简单使用](#redis的简单使用)
            - [关于StringRedisTemplate的方法使用](#关于stringredistemplate的方法使用)
            - [消息订阅和发布](#消息订阅和发布)

`目录 end` |_2018-09-05_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 数据库模块
> 主要是采用的JPA，极大的缩减了代码量，但是要注意不要过度依赖框架，丧失了基本的能力

## Relational Database
### 多数据源配置
> 为什么要有多数据源? 思考

> [Spring Boot多数据源配置与使用](https://www.jianshu.com/p/34730e595a8c)

### 连接池
#### c3p0
- [参考博客](http://www.cnblogs.com/520playboy/p/7526252.html)

#### druid
- [druid连接池的配置](http://makaidong.com/L_Sail/1/40930_11573921.html)

#### HikariPool
> 性能最好的数据库连接池

- [ ] 听说代码很精简, 阅读源码学习
*******************
### JPA
> 连接池:1.x 默认是tomcat-jdbc连接池 2.x 是 HikariPool

- [Blog: 原生SQL的写法](http://blog.csdn.net/Amy_Queen/article/details/72454099)

- [ ] 怎么映射视图到实体上?

### Mybatis

> [IDEA下创建Springboot，thymeleaf，Mybatis，Postgresql，Gradle项目](https://blog.csdn.net/juewang_love/article/details/53769906)
#### 自定义查询
##### HQL
- 使用Hibernate语法模式,将对象和数据库的表看成一个实体,方便书写SQL,但是在Controller层和Service层
    - 进行写代码的时候,参数的传递全是实体对象,要不停的new,这样真的没问题么(当有各种复杂的关联关系的时候,单个对象的CURD基本没有什么问题)
    - `TODO` 所以还不如直接写原生SQL! 那么JPA就真的没有使用的必要性了,直接用Mybatis结合插件生成自动的CRUD的代码,这样更为轻量
    - 待后续使用后再回来填坑

##### 原生SQL

- 涉及到数据的修改,就要加上前两个前缀,查询就直接写Query注解即可
```java
    @Modifying
    @Transactional
    @Query(value = "update a set b=?1", nativeQuery = true)
```

*************************
#### Mysql
- 1.引入依赖
```groovy
	compile('org.springframework.boot:spring-boot-starter-data-jpa')
	compile('org.springframework.boot:spring-boot-starter-jdbc')
	runtime('mysql:mysql-connector-java')
```
- 2.继承接口，打好实体类的注解 @Entity 

- 3.*切记 属性名不能使用下划线（数据库风格）不然写声明方法就会报错，jpa只是看下划线前半部分，会说找不到属性*
    - jpa在创建表时会把驼峰命名改成数据库风格的形式

- 4.jpa是声明特定方法的接口，让jpa来实现并自动注入，如果是没有的方法，就可以使用@Query注解
    - 默认使用的是HQL（HQL是基于类的所以使用的是类的名字不是表的名字），可以设置下使用原生SQL

#### 映射关系
##### 一对一
> 据说这是性能最好的方式, 但是有一点让人不舒服, A的id是名存实亡的, 数据库都没有这个字段, 实际上就是B的id, 但是对象又一定要保留这个id, 不然约束通不过  
> 也就是说, 创建的时候要设置A的id的值, 但是后面却用不到这个值

```java
@Entity
@Data
public class A {
  @Id
  private String id;
  private String name;
  @OneToOne(fetch = FetchType.LAZY)
  @MapsId
  private B b;
}

@Data
@Entity
public class B implements Serializable {
  @Id
  private String id;
  private String name;
}
```
##### 一对多
- 一方的配置是当前类的id，多方则按基本ER的规则来，注解中配置的是外键的名字, 所以当前类中的属性,外键名是不能重复的
```java
    // 一方
public class TestOne{
    @Id
    private String testOneId;
    @OneToMany
    @JoinColumn(name = "testOneId")//这个名字可以重复，最终会有一个随机码生成
    private Set<TestMany> testManySet;
}
    // 多方
public class TestMany {    
    @Id
    private String testManyId;
    @ManyToOne
    @JoinColumn(name = "testOneId")
    private TestOne testOneId;
}
```
- [ ] 问题: 当两个表互相引用了, 需要修改表结构 ,怎么删除重建两张表结构, 简单的命令会陷入死锁

*************

##### 多对多

*************
### Restful设计
- 1.添加依赖

```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-rest</artifactId>
    </dependency>
```
- 2.引入自动配置类

```java
    @Configuration
    public class RestConfiguration extends RepositoryRestMvcConfiguration {
        @Override
        public RepositoryRestConfiguration config() {
            return super.config();
        }
        @Override
        public ProfileResourceProcessor profileResourceProcessor(RepositoryRestConfiguration config) {
            // 设置rest根目录是应用路径下的路径 : localhost:8080/rest
            config.setBasePath("/rest");
            // 允许输出id
            config.exposeIdsFor(Goods.class);
            return super.profileResourceProcessor(config);
        }
    }
```
- 3.配置repository的名字例如：（只要配置repository就能用REST了）

```java
    @RepositoryRestResource(path = "book")
    public interface BookDao extends JpaRepository<Book,Long>{}
```

- 4.启动应用，控制台有如下输出
![输出](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Java/Spring/output.png)

- 所有路径的使用方法：
    - `GET` 查询单个 `/repo/id` 成功：200 失败404
    - `GET` 查询所有 `/repo` 成功200 失败404
    - `POST` 新增 `/repo` json数据发送 成功 201 失败404
    - `DELETE` 删除 `/repo/id` json数据 成功204 失败404
    - `PUT` 更新 `/repo/id` json 更新成功200 没有该id就插入201 失败404（使用主键自动增长就不会遇到404）

#### 【特别注意】
- rest得到的数据没有id
    - 添加配置 `config.exposeIdsFor(Goods.class);` 即可查看到id [参考博客](http://tommyziegler.com/how-to-expose-the-resourceid-with-spring-data-rest/)

### Jpa数据分页
> [参考博客](https://www.tianmaying.com/tutorial/spring-jpa-page-sort)

- 分页 page 从0开始 size是个数 sort可以不需要（如果本来就是id排序就没必要了） 
    - 原理就是 预编译SQL然后查询总数，然后再执行 必须有两条SQL执行
- 查询的结果不包含实体的id属性

### 数据库上的事务支持
- JPA对所有默认方法都开启了事务支持，查询类事务默认启用readOnly=true

****************
## Non Relational database
### JPA
#### Redis的简单使用
_配置连接信息_
```conf
    # REDIS (RedisProperties)
    # Redis数据库索引（默认为0）
    spring.redis.database=0
    # Redis服务器地址
    spring.redis.host=127.0.0.1
    # Redis服务器连接端口
    spring.redis.port=6379
    # Redis服务器连接密码（默认为空）
    spring.redis.password=
    # 连接池最大连接数（使用负值表示没有限制）
    spring.redis.pool.max-active=8
    # 连接池最大阻塞等待时间（使用负值表示没有限制）
    spring.redis.pool.max-wait=-1
    # 连接池中的最大空闲连接
    spring.redis.pool.max-idle=8
    # 连接池中的最小空闲连接
    spring.redis.pool.min-idle=0
    # 连接超时时间（毫秒）0不超时
    spring.redis.timeout=0
```

`在一个配置类中复制如下代码即可使用 StringRedisTemplate RedisTemplate 的实例`
```java
    @Bean
    public RedisTemplate<Object,Object> redisTemplate(RedisConnectionFactory factory) {
        RedisTemplate<Object,Object> template = new RedisTemplate<>();
        Jackson2JsonRedisSerializer jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer<>(Object.class);
        template.setConnectionFactory(factory);
        ObjectMapper om = new ObjectMapper();
        om.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
        om.enableDefaultTyping(ObjectMapper.DefaultTyping.NON_FINAL);
        jackson2JsonRedisSerializer.setObjectMapper(om);
        // 值序列化采用 jackson2JsonRedisSerializer
        template.setValueSerializer(jackson2JsonRedisSerializer);
        // 键序列化采用 StringRedisSerializer
        template.setKeySerializer(new StringRedisSerializer());
        template.afterPropertiesSet();
        return template;
    }
    @Bean
    StringRedisTemplate template(RedisConnectionFactory connectionFactory) {
        return new StringRedisTemplate(connectionFactory);
    }
``` 
`两个对象的简单使用`
```java
    stringRedisTemplate.opsForValue().set("aaa", "hello");
    String result = stringRedisTemplate.opsForValue().get("aaa");
    //获取所有
    Set<String> keysList =  stringRedisTemplate.keys("*");
    for(String temp :keysList){
        log.info(temp);
    }
```
- 以上配置的template都是只是建立在最简单的键值对上，String-String，所以对象使用的是json来存储
- 但是使用的时候如同使用MySQL一样，是ORM框架自动处理数据的转换


#### 关于StringRedisTemplate的方法使用
- 常见数据类型的中间对象
    - opsForValue() 操作简单键值对数据
        - hasKey()
    - opsForHash() 操作含有hash的数据
    - opsForList() 操作含有list的数据
    - opsForZSet() 操作含有zset（有序）的数据
        - range()方法返回指定范围的数据 Java中Set类型的（诡异的是顺序保持了一致）
    - opsForSet() 操作含有set的数据

- 设置超时时间
    - `redisTemplate.expire("max",tempTime,TimeUnit.SECONDS);`

#### 消息订阅和发布
[参考博客: Spring Boot使用Redis进行消息的发布订阅](https://www.tianmaying.com/tutorial/springboot-redis-message)


