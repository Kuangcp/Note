---
title: Mybatis
date: 2018-11-21 10:56:52
tags: 
    - ORM
categories: 
    - Java
---

**目录 start**

1. [Mybatis](#mybatis)
    1. [流程控制](#流程控制)
        1. [foreach 循环语句](#foreach-循环语句)
            1. [collection](#collection)
        1. [if 判断语句](#if-判断语句)
        1. [choose 相当于switch语句](#choose-相当于switch语句)
    1. [延迟加载](#延迟加载)
    1. [缓存](#缓存)
        1. [分布式缓存](#分布式缓存)
    1. [Spring整合](#spring整合)
1. [Tips](#tips)

**目录 end**|_2020-05-17 16:13_|
****************************************
# Mybatis
> [Official](https://mybatis.org/mybatis-3/)  

> 一个灵活的数据库中间件框架
> [参考: 如何在MyBatis中优雅的使用枚举](https://segmentfault.com/a/1190000010755321)

> [mybatis系统学习](https://github.com/brianway/springmvc-mybatis-learning)

> $ 和 # 的区别 =-]
- `${}` 会有SQL注入的漏洞，`#{}`则没有
    - 使用 $ 是SQL进行String直接进行拼接，使用#是preparstatement的预处理然后注入
- 都遵循 [OGNL](https://www.ibm.com/developerworks/cn/opensource/os-cn-ognl/) 语法

## 流程控制

### foreach 循环语句
```xml
    <foreach collection="param_list 自定义的话就是Map中的key，或者使用 @Param("")来指定 " item="params" index="currentIndex 当前索引"  separator="循环分隔符" open="在循环前加上字符" close="循环结束后加上字符">
        ${params}
    </foreach>
```
#### collection

有 arry list map 几种 还有item是必写，其他的是可选的

### if 判断语句
- `<if test=""></if>`

- update 判空 set `<set><if test="col!=null">col=#{col},</if></set>`
    - mybatis会自动去除多余的逗号

### choose 相当于switch语句
- `<choose><when test=""></when></choose>`

************************

## 延迟加载
- [ ] 

************************

## 缓存
- 一级缓存
    - 一级缓存是SqlSession级别的缓存。在操作数据库时需要构造sqlSession对象，在对象中有一个数据结构（HashMap）用于存储缓存数据。不同的sqlSession之间的缓存数据区域（HashMap）是互相不影响的。
- 二级缓存
    - 二级缓存是mapper级别的缓存，多个SqlSession去操作同一个Mapper的sql语句，多个SqlSession可以共用二级缓存，二级缓存是跨SqlSession的。

### 分布式缓存
mybatis提供了一个cache接口，可用于实现自己的缓存逻辑  

> [整合ehcache](https://github.com/brianway/springmvc-mybatis-learning/blob/master/mybatis/mybatis%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0(16)-mybatis%E6%95%B4%E5%90%88ehcache.md)`其中使用ehcache是本地单机模式的，实际上ehcache是支持分布式的`

## Spring整合
> [spring和mybatis整合](https://github.com/brianway/springmvc-mybatis-learning/blob/master/mybatis/mybatis%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0(17)-spring%E5%92%8Cmybatis%E6%95%B4%E5%90%88.md)


************************
# Tips
1. 展示执行SQL `logging.level.mapperAbsolutePackagePath=DEBUG` [Logging](https://mybatis.org/mybatis-3/logging.html)
