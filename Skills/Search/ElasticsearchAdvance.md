---
title: ElasticsearchAdvance
date: 2024-05-03 12:21:37
tags: 
categories: 
---

💠

- 1. [Elasticsearch](#elasticsearch)
    - 1.1. [设计](#设计)
    - 1.2. [异常处理](#异常处理)
- 2. [最佳实践](#最佳实践)
    - 2.1. [优化写入](#优化写入)
    - 2.2. [查询](#查询)

💠 2025-11-19 01:01:49
****************************************
# Elasticsearch
[Elasticsearch Best Practice Architecture](https://www.elastic.co/cn/pdf/architecture-best-practices.pdf)

> [Elasticsearch cluster load balancing best practices](https://stackoverflow.com/questions/66098115/elasticsearch-cluster-load-balancing-best-practices)  

## 设计


[Circuit breaker settings](https://www.elastic.co/docs/reference/elasticsearch/configuration-reference/circuit-breaker-settings)


## 异常处理

> [Elasticsearch Service 集群熔断问题如何解决](https://cloud.tencent.com/document/product/845/56272) 
> [记录在使用ES的过程中Data too large的实战排错处理方式ESJVM使用率高，ES fielddata lim - 掘金](https://juejin.cn/post/7092633680706813959)  

************************

# 最佳实践

> [滴滴基于 ElasticSearch 的一站式搜索中台实践](https://www.infoq.cn/article/ug*cbrk9303MiNZPrSEO)  

## 优化写入
> [提升 Elasticsearch 写入速度的案例分享](https://www.infoq.cn/article/t7b52mbzxqkwrrdpVqD2)  

- 大批量写入前设置副本为0写入后再调整副本避免资源竞争，设置刷盘周期时间更大（更高吞吐量，但是也更大的内存压力）
- 增量新增和更新时： 按实际业务

## 查询
1. 在数据无变动的情况下 同一个DSL执行结果可能不一致，分布式查询机制导致
    - DSL中设置的timeout是单纯请求超时控制，设置了5S则意味着时间内查到多少算多少

提升性能：考虑增大副本数量，考虑降低分片数
查询时指定分片
开启查询缓存
监控和调整
预热数据

