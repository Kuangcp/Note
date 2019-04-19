---
title: JavaRedis.md
date: 2018-11-21 10:56:52
tags: 
categories: 
---

**目录 start**
 
1. [Java使用redis](#java使用redis)
    1. [Jedis](#jedis)
        1. [jedis遇到的异常](#jedis遇到的异常)
    1. [Redisson](#redisson)
    1. [Lettuce](#lettuce)
    1. [vertx-redis-client](#vertx-redis-client)

**目录 end**|_2019-04-19 13:04_| [Kuangcp](https://github.com/Kuangcp/Note) | [yi-yun](https://github.com/yi-yun/Memo)
****************************************
# Java使用redis
> [Official List](https://redis.io/clients#java)

## Jedis
> [Github: Jedis](https://github.com/xetorthio/jedis) 简单直接 

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

## Redisson
> [Github: Redisson](https://github.com/redisson/redisson)

*********************
## Lettuce
> [Official](https://lettuce.io/) | [Github:](https://github.com/lettuce-io/lettuce-core)

和 Spring Netty 结合紧密， 适合 Spring 系， 没有Jedis简洁

## vertx-redis-client
> [Github: vertx-redis-client](https://github.com/vert-x3/vertx-redis-client)

