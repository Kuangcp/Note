---
title: Redis进阶
date: 2018-12-16 17:29:06
tags: 
    - Redis
categories: 
    - 数据库
---

**目录 start**
 
1. [Redis底层数据结构](#redis底层数据结构)
    1. [简单动态字符串](#简单动态字符串)
    1. [链表](#链表)
    1. [字典](#字典)
    1. [跳表](#跳表)
    1. [整数集合](#整数集合)
    1. [压缩列表](#压缩列表)
    1. [对象](#对象)
1. [Redis常用命令](#redis常用命令)
    1. [Run Configuration](#run-configuration)
    1. [过期策略](#过期策略)
    1. [事务](#事务)
    1. [服务器](#服务器)
    1. [实现原理](#实现原理)
        1. [scan](#scan)
1. [数据安全和性能](#数据安全和性能)
    1. [持久化策略](#持久化策略)
    1. [复制](#复制)
    1. [数据迁移](#数据迁移)
    1. [错误分析](#错误分析)
1. [主从](#主从)
1. [哨兵](#哨兵)
1. [cluster集群](#cluster集群)

**目录 end**|_2020-03-24 17:22_|
****************************************
# Redis底层数据结构
## 简单动态字符串
## 链表
## 字典

## 跳表
> [跳表基础](/Skills/CS/DS/LinearList.md)

> [Redis设计与实现: 跳跃表的实现](http://redisbook.com/preview/skiplist/datastruct.html)

Redis 的跳跃表由 redis.h/zskiplistNode 和 redis.h/zskiplist 两个结构定义， 其中 zskiplistNode 结构用于表示跳跃表节点  
而 zskiplist 结构则用于保存跳跃表节点的相关信息， 比如节点的数量， 以及指向表头节点和表尾节点的指针 等等。

```C
    typedef struct zskiplistNode {
        // 后退指针
        struct zskiplistNode *backward;

        // 分值
        double score;

        // 成员对象
        robj *obj;

        // 层
        struct zskiplistLevel {

            // 前进指针
            struct zskiplistNode *forward;

            // 跨度
            unsigned int span;

        } level[];

    } zskiplistNode;
```
## 整数集合

## 压缩列表

## 对象

************************

# Redis常用命令

- 关闭数据库 `shutdown` 该命令会在关闭数据库前保存数据
- 保存内存中数据到文件 `save`
- 认证 `auth 口令` 
- 测试联通性 `ping` 连接成功会返回pong

- 模糊删除 
    - 删除 6666端口 的 2数据库中`detail-2018-07-0*`模式的数据: `./redis-cli -p 6666 -n 2 keys "detail-2018-07-0*" | xargs  ./redis-cli -p 6666 -n 2 del`

- 查看所有连接 client list 

> [redis-stat](https://github.com/junegunn/redis-stat)

## Run Configuration	
- *slaveof*
    - `redis-server --port 9999 --slaveof 127.0.0.1 6379` 启动一个9999端口作为6379的从服务器进行同步
    - 或者服务启动后执行 `slaveof host port`（如果已经是从服务器，就丢去旧服务器的数据集，转而对新的主服务器进行同步）
    - 从服务变成主服务 `slaveof no one` (同步的数据集不会丢失，迅速替换主服务器)

- *loglevel*
    - `./redis-server /etc/redis/6379.conf --loglevel debug	`

## 过期策略
- `expire key seconds` 设置键的过期时间
- `PTTL/TTL key ` 查看键剩余过期时间（生存时间） ms/s
    -  -1 表示永久 -2 表示没有该key

## 事务

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

## 服务器

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
    - [参考: redis info 命令查看redis使用情况](https://blog.csdn.net/kexiaoling/article/details/51810919)
    - info stats 中 total_commands_processed 是实际请求, 还是说redis自己执行的命令 TODO 
- LASTSAVE
- MONITOR
- PSYNC
- SAVE
- SHUTDOWN
- SLAVEOF
- SLOWLOG
- SYNC
- TIME

## 实现原理
### scan
TODO 

************************

# 数据安全和性能
## 持久化策略
## 复制

## 数据迁移
- 使用主从复制来进行数据, 或者自己写Py脚本?


## 错误分析

1. `JedisConnectionException:  Could not get a resource from the pool` cause by `java.util.NoSuchElementException: Unable to validate object`
    - 多种原因, 由于设置了 testOnBorrow 为 true, 那么在每次获取数据时, 就会先测试性的获取一个数据, 然后校验能否正常拿到该数据 如果拿不到就抛出这个异常, 原因可能有:
        1. 根本没有连接上Redis, 配置有问题 端口 bind 什么的
        1. Redis 存放数据的 rdb 文件所在目录 没有存储空间了
        1. 没有内存空间了, 由于执行save操作时, 会进行fork子进程 然后进行持久化 TODO 验证

************************
> [参考博客: redis哨兵、集群](https://blog.csdn.net/u012129558/article/details/77146287)  

https://www.jianshu.com/p/42ee966f96e5
https://www.jianshu.com/p/06ab9daf921d
https://www.cnblogs.com/demingblog/p/10295236.html

# 主从

# 哨兵

# cluster集群
