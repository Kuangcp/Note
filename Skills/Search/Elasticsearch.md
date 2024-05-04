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
        - 1.1.1. [单节点](#单节点)
        - 1.1.2. [集群](#集群)
        - 1.1.3. [客户端](#客户端)
    - 1.2. [Index](#index)
    - 1.3. [Mapping](#mapping)
    - 1.4. [DSL](#dsl)
    - 1.5. [分词器](#分词器)
    - 1.6. [向量搜索](#向量搜索)

💠 2024-05-04 18:13:33
****************************************
# Elasticsearch
> [Official Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html)  
> [参考: Elasticsearch 快速开始](https://www.cnblogs.com/cjsblog/p/9439331.html)  


> [Elasticsearch技术方案选型的10个注意点](https://time.geekbang.org/column/article/108196?utm_campaign=geektime_search&utm_content=geektime_search&utm_medium=geektime_search&utm_source=geektime_search&utm_term=geektime_search)

> [一起学Elasticsearch系列](https://github.com/BookaiCode/JavaRecord?tab=readme-ov-file#lock-elasticsearch)
> [Guide to Elasticsearch in Java](https://www.baeldung.com/elasticsearch-java)`使用elasticsearch包访问ES`  
> [Spring Boot整合Elasticsearch](https://github.com/cloudgyb/es-spring-boot)`使用 SpringData`  

## Install
> [Installing Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)  
> [Command line tools](https://www.elastic.co/guide/en/elasticsearch/reference/current/commands.html)  

************************
### 单节点
> [Run Elasticsearch locally](https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html)

```sh
    # es8
    docker network create elastic
    # 可追加内存设置 -e ES_JAVA_OPTS="-Xms2560m -Xmx2560m" 避免启动占用大量内存 32G内存占用了17G 用visualvm查看实际内存占用才700M
    docker run --name es8 --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t docker.elastic.co/elasticsearch/elasticsearch:8.13.2
    # kibana
    docker run --name kibana --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.13.2

    # ES启动完成后会有如下输出 elastic的初始密码以及Kibana的Token
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                            
    ✅ Elasticsearch security features have been automatically configured!                                                                                                                                               
    ✅ Authentication is enabled and cluster connections are encrypted.    

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
- 重新生成token bin/elasticsearch-create-enrollment-token --scope kibana
- 重置初始用户的密码 bin/elasticsearch-reset-password -u elastic

> [参考: 用容器快速上手Elasticsearch](http://qinghua.github.io/elastic-search/)

### 集群
> [docker compose install cluster](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose-file)

### 客户端
- Kibana 官方支持
- Elasticvue 浏览器插件

## Index 
- `PUT /{indexName}?pretty` 创建索引
- `DELETE /{indexName}?pretty` 删除索引 `异步不可撤销`

- `GET /{indexName}/_search` 搜索
- `GET /{indexName}/_doc/doc_id` 查询指定文档id
- `GET /{indexName}/_doc/doc_id` 新增或覆盖文档
- `POST /{indexName}/_update/doc_id` 新增或更新文档

- `GET _cat/indices?v` 获取所有索引信息

## Mapping
> [Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)

## DSL
> [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)


## 分词器

************************

## 向量搜索
版本 8.5+



