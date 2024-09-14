---
title: Redis
date: 2018-12-16 17:28:55
tags: 
    - Redis
categories: 
    - 数据库
---

💠

- 1. [Redis](#redis)
    - 1.1. [Book](#book)
- 2. [安装和配置](#安装和配置)
    - 2.1. [Windows](#windows)
    - 2.2. [Linux](#linux)
        - 2.2.1. [Docker 方式](#docker-方式)
        - 2.2.2. [解压即用](#解压即用)
    - 2.3. [Redis配置文件](#redis配置文件)
- 3. [数据类型](#数据类型)
    - 3.1. [String](#string)
        - 3.1.1. [BitMap](#bitmap)
        - 3.1.2. [HyperLogLog](#hyperloglog)
    - 3.2. [List](#list)
    - 3.3. [Set](#set)
    - 3.4. [Zset](#zset)
    - 3.5. [Hash](#hash)
    - 3.6. [Stream](#stream)
    - 3.7. [GEO地理位置](#geo地理位置)
- 4. [Scan](#scan)
- 5. [Pipelining](#pipelining)
- 6. [Pub/Sub发布和订阅](#pubsub发布和订阅)
- 7. [客户端](#客户端)
    - 7.1. [Java](#java)
    - 7.2. [Python](#python)
    - 7.3. [GUI客户端](#gui客户端)
    - 7.4. [Cli](#cli)
- 8. [Project](#project)
    - 8.1. [Codis](#codis)
    - 8.2. [webdis](#webdis)
    - 8.3. [Redis Stack](#redis-stack)
- 9. [Redis的应用场景](#redis的应用场景)
    - 9.1. [分布式锁](#分布式锁)
    - 9.2. [消息队列](#消息队列)
- 10. [Redis 缓存相关问题](#redis-缓存相关问题)
    - 10.1. [缓存雪崩](#缓存雪崩)
    - 10.2. [缓存击穿](#缓存击穿)
    - 10.3. [缓存穿透](#缓存穿透)

💠 2024-09-14 11:51:16
****************************************
# Redis
> [Official Site](https://redis.io/) | [Redis中文社区](http://www.redis.cn/) | [Redis教程](http://www.runoob.com/redis/redis-tutorial.html) 

- [Redis Official doc zh](http://redisdoc.com/index.html)

> [参考: nodejs + redis/mysql 连接池问题](https://www.cnblogs.com/laozhbook/p/nodejs_redis_connection_pool.html)`单线程问题`
> [Redis 命令参考](http://doc.redisfans.com/index.html)`中文版，注意版本时效性` 

## Book 
> [Redis设计与实现 第二版](http://www.shouce.ren/api/view/a/13483)  
> [Redis 设计与实现](http://redisbook.com)`作者自建网站`

***********************

# 安装和配置
## Windows
- 注册为服务
	- `redis-server --service-install redis.windows.conf --loglevel verbose`
- 使用cmder
	- cmd 中运行 `E:/redis/redis-server.exe E:/redis/redis.windows.conf`
- 配置密码
	- `requirepass redis1104`
	- 客户端登录 `auth redis1104`

## Linux
包管理器安装 redis 如 debian系`apt install redis` arch系`pacman -S redis`

### Docker 方式
> [docker-install-redis](/Linux/Container/DockerSoft.md#redis)

### 解压即用
> [下载我打包好的(仅适用于Linux平台)](https://github.com/Kuangcp/Configs/tree/master/Database/redis)  
> [4.0.2](http://cloud.kuangcp.top/redis-4.0.2.zip) | [3.2.8](http://cloud.kuangcp.top/redis-3.2.8.zip)

`个人配置步骤:`
1. 从源码编译: [官网下载源码](https://redis.io/)
    - src下执行`make`进行编译，编译完成后，复制src目录中的`redis-cli redis-server`就可以用了
    - `redis-benchmark` 压测工具
    
1. 配置文件: 再复制下面的简化配置文件，或者使用源码中根目录下的配置文件自己配置下
    - [简化配置文件](https://raw.githubusercontent.com/Kuangcp/Configs/master/Database/redis/simple_redis.conf)
1. 再下载脚本就可以便捷的使用redis了 [shell辅助脚本](https://github.com/Kuangcp/Configs/tree/master/Database/redis/helper)

************************

## Redis配置文件
- [配置文件讲解](https://github.com/Kuangcp/Configs/blob/master/Database/redis/explain_redis.conf) | [原始配置文件](https://github.com/Kuangcp/Configs/blob/master/Database/redis/redis.conf)

- [简化配置文件](https://github.com/Kuangcp/Configs/blob/master/Database/redis/simple_redis.conf) 

**************************

# 数据类型
> [社区: 中文文档](http://redisdoc.com/index.html)

## String
> 字符串就是字节组成的序列 可以放字节串，整数，浮点数

> `SET key value [EX seconds] [PX millisecounds] [NX|XX]`

- EX seconds: 设置键的过期时间为second秒
- PX millisecounds: 设置键的过期时间为millisecounds 毫秒
- NX: 只在键不存在的时候,才对键进行设置操作
- XX: 只在键已经存在的时候,才对键进行设置操作

SET操作成功后,返回的是OK,失败返回NIL

- `incr incrby decr decrby`  只要存入的String能被解析为数值,就能执行这些命令: 递增或者递减
- `incr` 是原子操作即并发的情况下不会有脏读(可用于主键生成策略)
- `getset key val` get旧值并且set新值
- `mset mget `
	- `mset key val key val` 
	- `mget key key key` 返回值组成的数组
- `exists key` 有该值就返回1否则0
- `del key` 返回1被删除，0 key不存在
- `type key` 返回值的类型
- `expire key secondes` 设置或改变超时时间，精度是秒或毫秒
- `persist key` 去除超时时间
- `ttl key` 查看剩余存活时间 -1表示永久 -2表示没有该key

************************

### BitMap
> [参考: redis的bitset实战](https://segmentfault.com/a/1190000016296106)  

基于string, 可以操作每个 bit 的值
- setbit key offset value
    - `set key 上偏移量offset(2^32) 的 值 value(0/1)`
- getbit key offset 
- bitop
    - 主要做bitset的and、or、xor、not操作，结果存在新的bitset中，注意时间复杂度为O(N)
- bitpos
    - 返回指定bitset中在指定起始位置中第一个出现指定值的offset，不传start，end默认估计是0,-1
- bitcount
    - 统计bitset中出现1的个数

可以基于bitmap手动实现BloomFilter，也可以直接使用RedisStack的BloomFilter组件。

### HyperLogLog
> 用于做基数统计的算法

HyperLogLog 的优点是，在输入元素的数量或者体积非常非常大时，计算基数所需的空间总是固定 的、并且是很小的  

- PFADD 添加元素到制定 HyperLogLog 中
- PFCOUNT 返回给定 HyperLogLog 的基数估算值。
- PFMERGE 将多个 HyperLogLog 合并为一个 HyperLogLog 

************************

## List
- llen 
- `rpush key val val val `右/尾添加元素 lpush是左/头，若表不存在就新建
- `rpushx key value` 若表不存在就什么都不做，否则尾插元素
- `rpop key` 从list右/尾端中删除元素返回元素值 没有了就返回null
- `lrange key 0 -1` 取指定长度的list -1表示全部
- `ltrim key 0 2` 截取当前的list
- `lindex key index`   返回偏移量为index的元素(提到偏移量一般都是0开始)
- `linsert key BEFORE|AFTER pivot value`
    - 将值 value 插入到列表 key 当中，位于值 pivot 之前或之后。
    - 当 pivot 不存在于列表 key 时，不执行任何操作。当 key 不存在时， key 被视为空列表，不执行任何操作。
    - 如果 key 不是列表类型，返回一个错误。
- `lrem key count value` 根据参数 count 的值，移除列表中与参数 value 相等的元素。
- 阻塞式的列表弹出命令(block) `队列很有用`
    - `blpop`
    - `brpop`
    - `bpoplpush`
    - `brpoplpush` 阻塞式先右弹再左进

## Set
- `SADD key member [member ...]`
- `SCARD key` 返回集合 key 的基数(集合中元素的数量)。
- `SDIFF key [key ...]`  返回一个集合的全部成员，该集合是所有给定集合之间的差集。不存在的 key 被视为空集。
- `SDIFFSTORE destination key [key ...]`  这个命令的作用和 SDIFF 类似，但它将结果保存到 destination 集合，而不是简单地返回结果集。如果 destination 集合已经存在，则将其覆盖。destination 可以是 key 本身。
- `SINTER key [key ...]` 返回一个集合的全部成员，该集合是所有给定集合的交集。不存在的 key 被视为空集。当给定集合当中有一个空集时，结果也为空集(根据集合运算定律)。
- `SINTERSTORE destination key [key ...]` 与sdiffstore类似
- `SISMEMBER key member` 判断 member 元素是否集合 key 的成员。
- `SMEMBERS key` 获取某Set所有元素
- `SMOVE source destination member` 将 member 元素从 source 集合移动到 destination 集合。 SMOVE 是原子性操作。
- `SPOP key` 移除并返回集合中的一个随机元素
- `SRANDMEMBER key [count]` 如果命令执行时，只提供了 key 参数，那么返回集合中的一个随机元素
- `SREM key member [member ...]` 移除集合 key 中的一个或多个 member 元素，不存在的 member 元素会被忽略。
- `SUNION key [key ...]` 返回一个集合的全部成员，该集合是所有给定集合的并集。
- `SUNIONSTORE destination key [key ...]`
- `SSCAN key cursor [MATCH pattern] [COUNT count]` 参考 SCAN 命令

************************

## Zset
> 元素是键值对，键是member成员，值是score分值必须是浮点数

- ZADD 将一个给定分值的成员添加到有序集合里
- ZCARD 获取有序集合的成员数
- ZCOUNT min max 计算在有序集合中指定区间分数的成员数
- ZINCRBY key increment member 自增

- ZRANGE 根据元素在有序集合中的位置，从有序集合中从小到大获取多个元素
    - `zrange name 0 -1 withscores` 获取所有并获取分值
    - `zrange name 0 3 withscores`  获取分数最少的4个键值对

- ZREVRANGE 相反的, 从大到小

- _zrangebyscore_ 获取有序集合在给定范围中的所有元素
    - `zrangebyscore name 0 200 withscores`
- ZRANK
- ZREM
- ZREMRANGEBYRANK
- ZREMRANGEBYSCORE
- ZREVRANGEBYSCORE
- ZREVRANK
- `ZSCORE key member` 依据指定member获取score
- ZUNIONSTORE
- `zinterstore` 进行集合之间的并集（可以看作关系型数据库的多表连接）
- ZSCAN
- ZRANGEBYLEX
- ZLEXCOUNT
- ZREMRANGEBYLEX

************************

## Hash
> key-value 结构

- HDEL 删除散列中指定的K
- HEXISTS
- HGET
- HGETALL
- HINCRBY
- HINCRBYFLOAT
- HKEYS
- HLEN
- HMGET
- HMSET
- HSET
- HSETNX
- HVALS
- HSCAN
- HSTRLEN

## Stream 

************************

## GEO地理位置
- GEOADD
- GEOPOS
- GEODIST
- GEORADIUS
- GEORADIUSBYMEMBER
- GEOHASH

************************
# Scan 
- **SCAN** 命令用于迭代当前数据库中的数据库键 相较于 keys 降低阻塞进程的概率。
    - cursor 游标 
        - 注意这个游标不是 常见的 fori 循环里的i规律递增，第一次 sscan 会返回 cursor(第一个参数) 需要下一次拿这个 cursor 作为参数继续获取
        - 直到 `返回 0` 表示迭代完成 如果数据发生变化游标也会变化，且 count 是不保证准确数量的
    - count 数量
        - redis 只保证返回的数据数量大于等于 count. **注意count不能小于1 否则报 syntax error**
    - match pattern 匹配key的模式
    - 因为 这种不易理解的迭代方式, Spring 的 RedisTemplate 只提供了 count pattern 参数 cursor 默认为0

- **SSCAN** 命令用于迭代 Set 键中的元素。
- **HSCAN** 命令用于迭代哈希键中的键值对。
- **ZSCAN** 命令用于迭代有序集合中的元素（包括元素成员和元素分值）

> 使用SCAN命令代替原有全查询命令更安全，因为是部分查询不容易像全查询命令那样阻塞Redis进程，因此往往生产环境会禁止全查询命令 keys smembers 等 

> 注意 scan 命令只能顺序依据返回的cursor进行查找，而且由于实现方式，不一定每次查询是有数据的  
> 也就导致了在有大量key的db里面 找到 match pattern 的所有key 靠手工执行scan一次次找是不可能的

************************

# Pipelining
> 一次请求/响应服务器能实现处理新的请求即使旧的请求还未被响应。这样就可以将多个命令发送到服务器，而不用等待回复，最后在一个步骤中读取该答复。

- `(printf "PING\r\nPING\r\nPING\r\n"; sleep 1) | nc localhost 6379`

************************

# Pub/Sub发布和订阅
> 基于 阻塞 list 实现

- `PSUBSCRIBE pattern [pattern ...]`
    - 订阅一个或多个符合给定模式的频道。每个模式以 * 作为匹配符，比如 it* 匹配所有以 it 开头的频道( it.news 、 it.blog 、 it.tweets 等等)，
    -  news.* 匹配所有以 news. 开头的频道( news.it 、 news.global.today 等等)，诸如此类。
- `PUBLISH channel message`
    - 将信息 message 发送到指定的频道 channel 。
- `PUBSUB <subcommand> [argument [argument ...]]`
    - PUBSUB 是一个查看订阅与发布系统状态的内省命令， 它由数个不同格式的子命令组成， 以下将分别对这些子命令进行介绍。
    - `PUBSUB CHANNELS [pattern]` 列出当前的活跃频道。设置pattern参数就会匹配活跃频道，否则是列出所有频道
    - `PUBSUB NUMSUB [channel-1 ... channel-N]` 返回给定频道的订阅者数量， 订阅模式的客户端不计算在内。
    - `PUBSUB NUMPAT` 返回订阅模式的数量。注意， 这个命令返回的不是订阅模式的客户端的数量， 而是客户端订阅的所有模式的数量总和。
- `PUNSUBSCRIBE [pattern [pattern ...]]`
    - 指示客户端退订所有给定模式。如果没有模式被指定，也即是，一个无参数的 PUNSUBSCRIBE 调用被执行，
    - 那么客户端使用 PSUBSCRIBE 命令订阅的所有模式都会被退订。在这种情况下，命令会返回一个信息，告知客户端所有被退订的模式。
- `SUBSCRIBE channel [channel ...]`
    - 订阅给定的一个或多个频道的信息。
- `UNSUBSCRIBE [channel [channel ...]]`
    - 指示客户端退订给定的频道。如果没有频道被指定，也即是，一个无参数的 UNSUBSCRIBE 调用被执行，
    - 那么客户端使用 SUBSCRIBE 命令订阅的所有频道都会被退订。在这种情况下，命令会返回一个信息，告知客户端所有被退订的频道。

************************

# 客户端
> [program language client](http://www.redis.com.cn/clients)

## Java
> [详细](/Java/Ecosystem/JavaRedis.md)

************************

## Python
> pip install redis 该模块和redis命令的用法几乎一模一样, 上手很快
- [redis文档](https://pypi.python.org/pypi/redis/) `python操作redis的库的文档`

## GUI客户端
> [官方收录 客户端](https://redis.io/clients) | [alternativeto 列表](https://alternativeto.net/software/redily/)

> [Redis Desktop Manager](https://github.com/uglide/RedisDesktopManager/)  
> [Another Redis DeskTop Manager](https://gitee.com/qishibo/AnotherRedisDesktopManager)  

> arch 上暂时存在这个问题导致无法使用 Redis Desktop Manager [Github Issues](https://github.com/uglide/RedisDesktopManager/issues/4826)
1. rm -rf ~/.cache/fontconfig
1. rm -rf ~/snap/redis-desktop-manager/common/.cache/fontconfig
1. fc-cache -r

## Cli 
- redis-cli 
- redli 
    - go install github.com/IBM-Cloud/redli@latest

************************

> [FastoRedis](https://fastoredis.com/)  
> [Redis Plus](https://gitee.com/MaxBill/RedisPlus)  
> Redily  
> [Medis](https://github.com/luin/medis)  
> [rdbtools](https://rdbtools.com)  
> p3x-redis-ui  

*********

# Project
> 衍生项目 

## Codis
> [Github: Codis](https://github.com/CodisLabs/codis)
> [Kedis](https://gitee.com/kehaw9818/Kedis)  

## webdis
> 将redis变为一个简单的web接口  

> [官网](http://webd.is/) | [Github地址](https://github.com/nicolasff/webdis)

## Redis Stack
> [Github Redis Stack](https://github.com/redis-stack/redis-stack)

Redis Stack 是一组软件套件，它主要由三部分组成。Redis Stack Server，RedisInsight，Redis Stack 客户端 SDK。 其中 Redis Stack Server 由 Redis，RedisSearch，RedisJSON，RedisGraph，RedisTimeSeries 和 RedisBloom 组成。

可支撑如下业务
- 索引和查询Redis数据，聚合运算，`全文检索`
- 运行高级向量相似性搜索 `(KNN)`
- 有效地存储和操作嵌套的 `JSON 文档`
- 将关系构建和建模为`属性图`
- 存储、查询和聚合`时间序列数据`
- 利用快速、空间和计算高效的`概率数据结构`

************************

# Redis的应用场景
> [Redis的n种妙用，不仅仅是缓存 ](https://mp.weixin.qq.com/s?__biz=MzI3NzE0NjcwMg==&mid=2650123010&idx=2&sn=c17bd9192daa15c00502b7e27acacc61&chksm=f36bb623c41c3f35060bf244eddddc25ea6e2b96900f57299e0d8ffe548a08823b057dee5baf&mpshare=1&scene=1&srcid=0109PazxT49BtR2oCJ6Od32h&pass_ticket=ZX4WKje%2FJzbdB6LEivhrNCtzmljNugDZul02fl5SX4snt5QLMa6Cle9o1I5CumfQ#rd)

> [参考: 为什么我们做分布式使用Redis？](https://my.oschina.net/u/3971241/blog/2221560)`缓存的场景和应对措施`

## 分布式锁
> [Doc: setnx](http://cndoc.github.io/redis-doc-cn/cn/commands/setnx.html)`包含以此命令设计锁的一些缺陷`  
> [redisson](https://github.com/redisson/redisson)  

单机 使用 setnx， redis分布式部署的情况下使用RedLock

> [基于Redis的分布式锁到底安全吗（上）？](https://mp.weixin.qq.com/s/JTsJCDuasgIJ0j95K8Ay8w)  
> [基于Redis的分布式锁到底安全吗（下）？](https://mp.weixin.qq.com/s/4CUe7OpM6y1kQRK8TOC_qQ?)  
> [参考: Redis 分布式锁进化史解读 + 缺陷分析](https://zhuanlan.zhihu.com/p/161078350)  

> [参考: redis分布式锁在MySQL事务代码中使用](https://blog.csdn.net/seapeak007/article/details/99337781)  
> [参考: Lua脚本在redis分布式锁场景的运用](https://www.cnblogs.com/demingblog/p/9542124.html)  

## 消息队列
> List, Pub/Sub, Stream 可实现, 可靠性依次增加，但依然会有消息丢失问题

> [asynq](https://github.com/hibiken/asynq)  

************************

`搜索`
> [RediSearch](https://github.com/RediSearch/RediSearch)

************************

# Redis 缓存相关问题
## 缓存雪崩
同一时间大量缓存失效，请求都打到DB，导致DB负载过大甚至宕机。

与此同时，大量缓存集中失效会让Redis瞬时OPS很高，操作的延迟会突增。

1. 大量 key 使用了相同的过期时间
    - 过期时间加随机值或者特定算法分散过期时间
    - 使用本地缓存(JVM级别)
    - 当请求过多，提供服务降级
1. Redis发生重启(Redis 未做持久化)
    - 启动时预先加载 热点Key

## 缓存击穿
针对缓存中没有但是DB中有的数据请求

1. 当某个Key失效后，瞬间涌入大量的请求同一个Key，这些请求不会命中Redis，都会请求到DB，导致数据库压力过大
    1. 设置热点Key，自动检测热点Key，将热点Key的过期时间加大或者永不过期。
    2. 在更新缓存时加互斥锁。当发现没有命中Redis，去查数据库的时候，在执行更新缓存的操作上加锁，当一个线程访问时，其它线程等待
        - 这个线程访问过后，缓存中的数据会被重建，这样其他线程就可以从缓存中取值。

## 缓存穿透
针对缓存和 DB 都没有的数据 请求

1. 对查询结果为空的情况也进行缓存，这样，再次访问时，缓存层会直接返回空值。缓存时间设置短一点，或者该key对应的数据insert了之后清理缓存。
2. 对一定不存在的key进行过滤。例如： 布隆过滤器