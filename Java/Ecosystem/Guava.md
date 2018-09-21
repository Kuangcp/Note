`目录 start`
 
- [Guava](#guava)
    - [基础部分](#基础部分)
        - [EventBus](#eventbus)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Guava
> [Github地址](https://github.com/google/guava)
> [官方手册](https://github.com/google/guava/wiki) | git地址:`https://github.com/google/guava.wiki.git`
> [翻译版](http://ifeve.com/google-guava/)

- Guava工程包含了若干被Google的 Java项目广泛依赖 的核心库，例如：集合 [collections] 、缓存 [caching] 、原生类型支持 [primitives support] 、并发库 [concurrency libraries] 、通用注解 [common annotations] 、字符串处理 [string processing] 、I/O 等等。 所有这些工具每天都在被Google的工程师应用在产品服务中。

_包结构_
```
    com.google.common.annotations
    com.google.common.base
    com.google.common.collect
    com.google.common.io
    com.google.common.net
    com.google.common.primitives
    com.google.common.util.concurrent
```

```
    [Google Guava] 7-原生类型
    [Google Guava] 12-数学运算
    [Google Guava] 排序: Guava强大的”流畅风格比较器”
    [Google Guava] 2.1-不可变集合
    [Google Guava] 10-散列
    [Google Guava] 9-I/O
    [Google Guava] 1.2-前置条件
    [Google Guava] 4-函数式编程
    [Google Guava] 6-字符串处理：分割，连接，填充
    [Google Guava] 1.1-使用和避免null
    [Google Guava] 8-区间
    [Google Guava] 2.4-集合扩展工具类
    [Google Guava] 1.3-常见Object方法    @Bean
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
    google Guava包的ListenableFuture解析
    [Google Guava] 11-事件总线
```

## 基础部分
> Optional的设计和Java8的Optional是差不多的, 只是方法的命名不一样而已


### EventBus
> [官方文档](https://github.com/google/guava/wiki/EventBusExplained) | [Guava学习笔记：EventBus](http://www.cnblogs.com/peida/p/EventBus.html)
> [并发编程网 event bus](http://ifeve.com/google-guava-eventbus/) | [走进Guava](https://www.yeetrack.com/?p=1177)

