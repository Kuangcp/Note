`目录 start`
 
- [Redis](#redis)
    - [Book](#book)
    - [【windows上的基本配置】](#windows上的基本配置)
    - [Linux下的使用](#linux下的使用)
        - [docker安装redis](#docker安装redis)
        - [命令安装](#命令安装)
        - [解压即用](#解压即用)
    - [redis配置文件](#redis配置文件)
    - [Redis命令行常规使用](#redis命令行常规使用)
        - [过期策略](#过期策略)
        - [数据类型](#数据类型)
            - [字符串 String](#字符串-string)
            - [列表 list](#列表-list)
            - [集合 set](#集合-set)
            - [有序集合 zset](#有序集合-zset)
            - [散列 hash](#散列-hash)
            - [HyperLogLog](#hyperloglog)
            - [GEO【地理位置】](#geo地理位置)
        - [Pub/Sub发布订阅](#pubsub发布订阅)
        - [事务](#事务)
        - [服务器](#服务器)
        - [Run Configuration](#run-configuration)
    - [数据安全和性能](#数据安全和性能)
        - [持久化策略](#持久化策略)
        - [复制](#复制)
        - [数据迁移](#数据迁移)
    - [【Redis的使用】](#redis的使用)
        - [作为日志记录](#作为日志记录)
        - [作为网站统计数据](#作为网站统计数据)
        - [存储配置信息](#存储配置信息)
        - [自动补全](#自动补全)
        - [构建锁](#构建锁)
        - [任务队列](#任务队列)
    - [编程语言的使用](#编程语言的使用)
        - [Java 使用](#java-使用)
        - [Python使用](#python使用)
        - [webdis](#webdis)

`目录 end` |_2018-08-26_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Redis
> [Redis官网](https://redis.io/) | [Redis中文社区](http://www.redis.cn/) | [Redis教程](http://www.runoob.com/redis/redis-tutorial.html) 

- [Redis中文文档](http://redisdoc.com/index.html)

## Book 
> [Redis设计与实现 第二版](http://www.shouce.ren/api/view/a/13483)

## 【windows上的基本配置】
- 注册为服务
	- `redis-server --service-install redis.windows.conf --loglevel verbose`
- 使用cmder
	- cmd 中运行 `E:/redis/redis-server.exe E:/redis/redis.windows.conf`
- 配置密码
	- `requirepass redis1104`
	- 客户端登录 `auth redis1104`

## Linux下的使用
### docker安装redis
> [docker-install-redis](/Linux/Container/DockerSoft.md#redis)

### 命令安装
> 这样不太好做多个redis, 个人不喜欢这种方式

- 安装 `apt install redis`
- 开启数据库服务 `redis-server`
- 打开客户端 `redis-cli`

### 解压即用
> [下载我打包好的(仅适用于Linux平台)](https://github.com/Kuangcp/Configs/tree/master/Database/redis)  
> [4.0.2](http://cloud.kuangcp.top/redis-4.0.2.zip) | [3.2.8](http://cloud.kuangcp.top/redis-3.2.8.zip)  

`个人配置步骤:`
- 官网下载源码，执行`make`进行编译，编译完成后，复制src目录中的`redis-cli redis-server`就可以用了，redis-benchmark可选，测性能
    - 再复制下面的简化配置文件，或者使用源码中根目录下的配置文件自己配置下
    - [简化配置文件](https://raw.githubusercontent.com/Kuangcp/Configs/master/Database/redis/simple_redis.conf)
- 再创建以下两个脚本就可以便捷的使用redis了
`server_redis.sh`
```sh
    basepath=$(cd `dirname $0`; pwd)
    echo $basepath
    $basepath/redis-server $basepath/redis.conf>redis.log &
```
`client_redis.sh`
```sh
    basepath=$(cd `dirname $0`; pwd)
    $basepath/redis-cli -p 6379
```

****************************
## redis配置文件
- [配置文件讲解](https://github.com/Kuangcp/Configs/blob/master/Database/redis/explain_redis.conf) | [原始配置文件](https://github.com/Kuangcp/Configs/blob/master/Database/redis/redis.conf)
- `使用ing`[简化配置文件](https://github.com/Kuangcp/Configs/blob/master/Database/redis/simple_redis.conf) 

********
## Redis命令行常规使用

- 关闭数据库 `shutdown` 他会在关闭前保存数据
- 保存内存中数据 `save`
- 认证 `auth` 口令
- 测试联通性 `ping` 连接成功会返回pong
- 模糊删除 
    - 删除 6666端口 的 2数据库中`detail-2018-07-0*`模式的数据: `./redis-cli -p 6666 -n 2 keys "detail-2018-07-0*" | xargs  ./redis-cli -p 6666 -n 2 del`

### 过期策略
- `expire key seconds` 设置键的过期时间
- `PTTL/TTL key ` 查看键剩余过期时间（生存时间） ms/s
    -  -1表示永久 -2表示没有该key

### 数据类型
> [中文文档](http://redisdoc.com/index.html)

#### 字符串 String
> 字符串就是字节组成的序列 可以放字节串，整数，浮点数

- `set key newval nx `存在则set失败
- `set key newval xx `不存在则set失败
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
	- `set key val ex secondes` set时设置超时时间
- `persist key` 去除超时时间
- `ttl key` 查看剩余存活时间 -1表示永久 -2表示没有该key

#### 列表 list
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

#### 集合 set
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

#### 有序集合 zset
> 元素是键值对，键是member成员，值是score分值必须是浮点数

- _zadd_ 将一个给定分值的成员添加到有序集合里
- ZCARD
- ZCOUNT
- _zincrby_ 自增

- _zrange_ 根据元素在有序集合中的位置，从有序集合中从小到大获取多个元素
    - `zrange name 0 -1 withscores` 获取所有并获取分值
    - `zrange name 0 3 withscores`  获取分数最少的4个键值对
- _zrevrange_ 相反的, 从大到小

- _zrangebyscore_ 获取有序集合在给定范围中的所有元素
    - `zrangebyscore name 0 200 withscores`
- ZRANK
- ZREM
- ZREMRANGEBYRANK
- ZREMRANGEBYSCORE
- ZREVRANGEBYSCORE
- ZREVRANK
- ZSCORE
- ZUNIONSTORE
- `zinterstore` 进行集合之间的并集（可以看作关系型数据库的多表连接）
- ZSCAN
- ZRANGEBYLEX
- ZLEXCOUNT
- ZREMRANGEBYLEX

#### 散列 hash
> (类似Map 嵌套，一个内置的微型redis)

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

#### HyperLogLog
- PFADD
- PFCOUNT
- PFMERGE

#### GEO【地理位置】
- GEOADD
- GEOPOS
- GEODIST
- GEORADIUS
- GEORADIUSBYMEMBER
- GEOHASH

***************
### Pub/Sub发布订阅

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

**************
### 事务

- `DISCARD` 取消事务，放弃执行事务块内的所有命令。
- `EXEC`
    - 执行所有事务块内的命令。假如某个(或某些) key 正处于 WATCH 命令的监视之下，且事务块中有和这个(或这些) key 相关的命令，
    - 那么 EXEC 命令只在这个(或这些) key 没有被其他命令所改动的情况下执行并生效，否则该事务被打断(abort)。
- `MULTI` 标记一个事务块的开始。事务块内的多条命令会按照先后顺序被放进一个队列当中，最后由 EXEC 命令原子性(atomic)地执行。
- `UNWATCH` 
    - 取消 WATCH 命令对所有 key 的监视。如果在执行 WATCH 命令之后， EXEC 命令或 DISCARD 命令先被执行了的话，那么就不需要再执行 UNWATCH 了。
    - 因为 EXEC 命令会执行事务，因此 WATCH 命令的效果已经产生了；而 DISCARD 命令在取消事务的同时也会取消所有对 key 的监视，因此这两个命令执行之后，就没有必要执行 UNWATCH 了。
- `WATCH key [key ...]`
    - 监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。

*************
### 服务器

- BGREWRITEAOF
- BGSAVE
- CLIENT GETNAME
- CLIENT KILL
- CLIENT LIST
- CLIENT SETNAME
- CONFIG GET
- CONFIG RESETSTAT
- CONFIG REWRITE
- CONFIG SET
- DBSIZE
- DEBUG OBJECT
- DEBUG SEGFAULT
- FLUSHALL
- FLUSHDB
- INFO
- LASTSAVE
- MONITOR
- PSYNC
- SAVE
- SHUTDOWN
- SLAVEOF
- SLOWLOG
- SYNC
- TIME
*****************************
	
### Run Configuration	
- *slaveof*
    - `redis-server --port 9999 --slaveof 127.0.0.1 6379` 启动一个9999端口作为6379的从服务器进行同步
    - 或者服务启动后执行 `slaveof host port`（如果已经是从服务器，就丢去旧服务器的数据集，转而对新的主服务器进行同步）
    - 从服务变成主服务 `slaveof no one` (同步的数据集不会丢失，迅速替换主服务器)
- *loglevel*
    - `./redis-server /etc/redis/6379.conf --loglevel debug	`

***********
## 数据安全和性能
### 持久化策略
### 复制

### 数据迁移
- 使用主从复制来进行数据, 或者自己写Py脚本?

*******
## 【Redis的使用】
### 作为日志记录
### 作为网站统计数据
### 存储配置信息
### 自动补全
- 搜索建议

### 构建锁

### 任务队列
- 发送邮件

## 编程语言的使用
***************************
### Java 使用
*******************
### Python使用
> pip install redis 该模块和redis命令的用法几乎一模一样, 上手很快
- [redis文档](https://pypi.python.org/pypi/redis/) `python操作redis的库的文档`

### webdis
> 将redis变为一个简单的web接口  

> [官网](http://webd.is/) | [Github地址](https://github.com/nicolasff/webdis)

