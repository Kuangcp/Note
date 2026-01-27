---
title: ElasticsearchAdvance
date: 2024-05-03 12:21:37
tags: 
categories: 
---

💠

- 1. [Elasticsearch](#elasticsearch)
    - 1.1. [设计](#设计)
        - 1.1.1. [更新 update](#更新-update)
    - 1.2. [异常处理](#异常处理)
        - 1.2.1. [写入延迟](#写入延迟)
- 2. [最佳实践](#最佳实践)
    - 2.1. [优化写入](#优化写入)
    - 2.2. [查询](#查询)

💠 2026-01-28 00:01:03
****************************************
# Elasticsearch
[Elasticsearch Best Practice Architecture](https://www.elastic.co/cn/pdf/architecture-best-practices.pdf)

> [Elasticsearch cluster load balancing best practices](https://stackoverflow.com/questions/66098115/elasticsearch-cluster-load-balancing-best-practices)  

## 设计


[Circuit breaker settings](https://www.elastic.co/docs/reference/elasticsearch/configuration-reference/circuit-breaker-settings)


### 更新 update

ES 的 update 在底层就是 “先标记旧文档为已删除，再写入新文档”

在 bulk 里做的是 update，相当于对同一条 doc 重新索引一次；ES 会：
   把旧版本文档的 _id 标记为 逻辑删除（在 .del 文件里打标）
   立即写入一条 新版本文档（_version + 1）
   因此 doc.deleted 计数会增加，但 文档总数（total.docs.count）不会下降，因为你只是“换了一条新记录”，并没有真正减少数据

## 异常处理

> [Elasticsearch Service 集群熔断问题如何解决](https://cloud.tencent.com/document/product/845/56272) 
> [记录在使用ES的过程中Data too large的实战排错处理方式ESJVM使用率高，ES fielddata lim - 掘金](https://juejin.cn/post/7092633680706813959)  

### 写入延迟

延迟型 bulk（bulk 请求 RT 飙高、队列积压但 CPU 并不爆满）90% 都是“**磁盘 I/O 被写放大**”导致的，剩下 10% 是“**过多小段 segment 合并**”或“**热点 shard 分布不均**”。

---

1. 最大元凶：磁盘写放大（Write Amplification）  
   - **大字段 + 高频更新** → 一条 5 KB 文档实际产生 32 KB（16 KB×2）溢出页 + 16 KB translog → 磁盘写带宽被吃满，iowait 飙高；  
   - **机械盘 or 云盘 IOPS 上限低** → util% 未到 100%，但 **iowait > 30 ms** 就能把 bulk RT 从 50 ms 拉到 1 s+；  
   - **验证**：`iostat -x 1` 看 `await`/`svctm`，若 `await > svctm × 3` 即为 I/O 排队 。

2. 第二元凶：segment 合并风暴  
   - `refresh_interval` 过短（1s）+ 小 bulk（<5 MB）→ 每秒产生大量 5-10 MB segment；  
   - 后台 **max_merge_count** 默认 3，合并速度跟不上生成速度 → 合并线程 CPU 占满，bulk 被 throttle（限流）。  
   - **观测**：`/_cat/thread_pool/force_merge?v` 出现 `active=3 queue>0`，同时 `indexing.throttle_time_in_millis` 突增 。

3. 第三元凶：热点 shard / 超大 shard  
   - 单个 shard > 50 GB 且 **routing=`_id`** → 所有 bulk 都落到同一节点，该节点磁盘队列先满 → 集群整体 bulk latency 被“最慢节点”拖高；  
   - **观测**：`/_cat/shards` 看同一 node 上该索引 shard 体积，若比其他节点大 5× 以上即为热点 。

4. 网络/小包拆包（云环境常见）  
   - bulk 请求 < 1 MB、但 qps 极高 → 16 KB 小包拆片 + TCP 头开销 → 网卡小包率 50k pps+，**网卡中断 CPU 占满**；  
   - **观测**：`sar -n DEV 1` 看 `rxpck/s` 与 `%soft`，若软中断 > 30% 即网络瓶颈 。

---

一句话速查表  
| 现象 | 优先敲的命令 | 红灯阈值 | 文献 |
|---|---|---|---|
| 磁盘写放大 | `iostat -x 1` | await > 30 ms 且 util% < 80% |  |
| 合并风暴 | `_cat/thread_pool/force_merge` | queue > 0 且 throttle_time 突增 |  |
| 热点 shard | `_cat/shards` | 单 shard > 50 GB 或同一 node 2× 体积 |  |
| 小包风暴 | `sar -n DEV 1` | rxpck/s > 50k 且 %soft > 30% |  |

************************

# 最佳实践

> [滴滴基于 ElasticSearch 的一站式搜索中台实践](https://www.infoq.cn/article/ug*cbrk9303MiNZPrSEO)  

## 优化写入
> [提升 Elasticsearch 写入速度的案例分享](https://www.infoq.cn/article/t7b52mbzxqkwrrdpVqD2)  

- 大批量写入前设置副本为0写入后再调整副本避免资源竞争，设置刷盘周期时间更大（更高吞吐量，但是也更大的内存压力）
- 增量新增和更新时： 按实际业务


写入的bulk如果出现了高时延的情况，还可能拖慢查询的性能，因为写入线程池满了后会占用查询的线程（ES 8 默认 node.processors 共享），就可能导致查询请求排队从而导致 写入和查询 都出现高时延


## 查询
1. 在数据无变动的情况下 同一个DSL执行结果可能不一致，分布式查询机制导致
    - DSL中设置的timeout是单纯请求超时控制，设置了5S则意味着时间内查到多少算多少

提升性能：考虑增大副本数量，考虑降低分片数
查询时指定分片
开启查询缓存
监控和调整
预热数据

