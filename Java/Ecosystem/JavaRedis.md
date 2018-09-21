`目录 start`
 
- [Java使用redis](#java使用redis)
    - [Jedis](#jedis)
        - [jedis遇到的异常](#jedis遇到的异常)
        - [SpringBoot使用Redis](#springboot使用redis)
    - [Lettuce](#lettuce)

`目录 end` |_2018-08-20_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Java使用redis
## Jedis
> [Github:](https://github.com/xetorthio/jedis)简单直接, 但是项目很久没有更新了

- maven依赖(Spring 4.1.7)：
```xml
    <dependency>
        <groupId>org.springframework.data</groupId>
        <artifactId>spring-data-redis</artifactId>
        <version>1.6.0.RELEASE</version>
    </dependency>
    <dependency>
        <groupId>redis.clients</groupId>
        <artifactId>jedis</artifactId>
        <version>2.9.0</version>
        <type>jar</type>
    <scope>compile</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-lang3</artifactId>
        <version>3.3.2</version>
    </dependency>
```
`Spring配置文件`
```xml
    <!--
        加载redis配置文件 
        如果已经加载了一个文件，那么第一个就要写这个配置项，
        <property name="ignoreUnresolvablePlaceholders" value="true"/>
        第二个要加 后面的配置 
        不然就只会加载前面那个文件
    -->
    <context:property-placeholder location="classpath:redis.properties" ignore-unresolvable="true"/>
    <!-- redis连接池的配置 -->
    <bean id="jedisPoolConfig" class="redis.clients.jedis.JedisPoolConfig">
        <property name="maxActive" value="${redis.pool.maxActive}"/>
        <property name="maxIdle" value="${redis.pool.maxIdle}"/>
        <property name="minIdle" value="${redis.pool.minIdle}"/>
        <property name="maxWait" value="${redis.pool.maxWait}"/>
        <property name="testOnBorrow" value="${redis.pool.testOnBorrow}"/>
        <property name="testOnReturn" value="${redis.pool.testOnReturn}"/>
    </bean>
    <!-- redis的连接池pool，不是必选项：timeout/password  -->
    <bean id = "jedisPool" class="redis.clients.jedis.JedisPool">
        <constructor-arg index="0" ref="jedisPoolConfig"/>
        <constructor-arg index="1" value="${redis.host}"/>
        <constructor-arg index="2" value="${redis.port}" type="int"/>
        <constructor-arg index="3" value="${redis.timeout}" type="int"/>
        <constructor-arg index="4" value="${redis.password}"/>
    </bean>
```

- java实际测试类[JedisUtilsTest.java](https://github.com/Kuangcp/Maven_SSM/blob/master/src/test/java/redis/JedisUtilTest.java)

- jedis 使用后要disconnect释放连接,最新版本close就不用了，使用连接池就不用
- jedis 的事务 使用exec释放事务

### jedis遇到的异常
- Invocation of init method failed; nested exception is java.lang.NoSuchMethodError: org.springframework.core.serializer.support.DeserializingConverter
- 版本对不上，要Spring和Spring-data-redis 和 redis和commons-lang3对应
- 目前是4.1.7 + 1.6.0 + 2.9.0 + 3.3.2 编译通过了	

### SpringBoot使用Redis
> [SpringBoot配置Redis](/Java/Spring/SpringBootDatabase.md)	

*********************
## Lettuce
> [Official](https://lettuce.io/) | [Github:](https://github.com/lettuce-io/lettuce-core)
