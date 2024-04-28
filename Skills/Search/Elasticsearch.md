---
title: Elasticsearch
date: 2019-05-10 18:10:21
tags: 
categories: 
    - ELK
---

💠

- 1. [Elasticsearch](#elasticsearch)
    - 1.1. [Install](#install)
        - 1.1.1. [GUI](#gui)
    - 1.2. [Index](#index)
- 2. [最佳实践](#最佳实践)
    - 2.1. [优化写入](#优化写入)

💠 2024-04-26 01:17:07
****************************************
# Elasticsearch
> [Official Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html)  
> [参考: Elasticsearch 快速开始](https://www.cnblogs.com/cjsblog/p/9439331.html)  


> [Elasticsearch技术方案选型的10个注意点](https://time.geekbang.org/column/article/108196?utm_campaign=geektime_search&utm_content=geektime_search&utm_medium=geektime_search&utm_source=geektime_search&utm_term=geektime_search)

> [一起学Elasticsearch系列](https://github.com/BookaiCode/JavaRecord?tab=readme-ov-file#lock-elasticsearch)

## Install
> [install](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) | [Docker](https://hub.docker.com/_/elasticsearch/)  
> [Guide to Elasticsearch in Java](https://www.baeldung.com/elasticsearch-java)  

> 部署单节点
1. `docker network create es-network`
1. `docker run -d --name es7 --net es-network -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms2560m -Xmx2560m"   elasticsearch:7.14.2`

> [docker compose install cluster](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose-file)

> [参考: 用容器快速上手Elasticsearch](http://qinghua.github.io/elastic-search/)

### GUI
浏览器插件： Elasticvue


## Index 


************************

# 最佳实践

> [滴滴基于 ElasticSearch 的一站式搜索中台实践](https://www.infoq.cn/article/ug*cbrk9303MiNZPrSEO)  

## 优化写入
> [提升 Elasticsearch 写入速度的案例分享](https://www.infoq.cn/article/t7b52mbzxqkwrrdpVqD2)  



