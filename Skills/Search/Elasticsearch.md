---
title: Elasticsearch
date: 2019-05-10 18:10:21
tags: 
categories: 
    - ELK
---

💠

- 1. [Elasticsearch](#elasticsearch)
- 2. [Install](#install)
    - 2.1. [单节点](#单节点)
    - 2.2. [集群](#集群)
    - 2.3. [客户端](#客户端)
        - 2.3.1. [Java](#java)
- 3. [Index](#index)
- 4. [Mapping](#mapping)
- 5. [DSL](#dsl)
- 6. [分词器](#分词器)
- 7. [向量搜索](#向量搜索)

💠 2025-10-21 21:22:16
****************************************
# Elasticsearch
> [Official Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html)  
> [参考: Elasticsearch 快速开始](https://www.cnblogs.com/cjsblog/p/9439331.html)  

使用场景：

> [七个生产案例告诉你BATJ为何选择ElasticSearch！应用场景和优势！](https://segmentfault.com/a/1190000022799288)  
> [Elasticsearch技术方案选型的10个注意点](https://time.geekbang.org/column/article/108196)  
> [liuhuanyong/MusicLyricChatbot](https://github.com/liuhuanyong/MusicLyricChatbot)  

中文教程：

> [一起学Elasticsearch系列](https://github.com/BookaiCode/JavaRecord?tab=readme-ov-file#lock-elasticsearch)  
> [ElasticSearch知识体系详解](https://pdai.tech/md/db/nosql-es/elasticsearch.html)

************************

# Install
> [Installing Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)  
> [Command line tools](https://www.elastic.co/guide/en/elasticsearch/reference/current/commands.html)  

************************
## 单节点
> [Run Elasticsearch locally](https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html)

```sh
    # es8
    docker network create elastic
    # 可追加内存设置 -e ES_JAVA_OPTS="-Xms2560m -Xmx2560m" 避免启动占用大量内存 32G内存占用了17G 用visualvm查看实际内存占用才700M
    docker run --name es8 --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t docker.elastic.co/elasticsearch/elasticsearch:8.13.2
    # kibana
    docker run --name kibana --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.13.2

    # ES启动完成后会有如下输出 elastic的初始密码以及Kibana的TokenElas
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                            
    ✅ Elasticsearch security features have been automatically configured!                                                                                                                                               
    ✅ Authentication is enabled and cluster connections are encrypted.    

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
- 重新生成token bin/elasticsearch-create-enrollment-token --scope kibana
- 重置初始用户的密码 bin/elasticsearch-reset-password -u elastic

> [参考: 用容器快速上手Elasticsearch](http://qinghua.github.io/elastic-search/)

## 集群
> [docker compose install cluster](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose-file)

## 客户端
- Kibana 官方支持
- Elasticvue 浏览器插件

### Java
> [Guide to Elasticsearch in Java](https://www.baeldung.com/elasticsearch-java)`使用elasticsearch包访问ES`  
> [Spring Boot整合Elasticsearch](https://github.com/cloudgyb/es-spring-boot)`使用 SpringData`  


# Index 
- `PUT /{indexName}?pretty` 创建索引
- `DELETE /{indexName}?pretty` 删除索引 `异步,不可撤销,不可逆`

- `GET /{indexName}/_search` 搜索
- `GET /{indexName}/_doc/doc_id` 查询指定文档id
- `GET /{indexName}/_doc/doc_id` 新增或覆盖文档
- `POST /{indexName}/_update/doc_id` 新增或更新文档

- `GET _cat/indices?v` 获取所有索引信息

************************

# Mapping
> [Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)

************************

# DSL
> [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

> [EQL](https://www.elastic.co/guide/en/elasticsearch/reference/current/eql.html)`Event Query Language`  

************************

# 分词器

> [infinilabs/analysis-ik](https://github.com/infinilabs/analysis-ik)  

> [goto456/stopwords: 中文常用停用词表（哈工大停用词表、百度停用词表等）](https://github.com/goto456/stopwords)  
> [Elasticsearch：如何在 Elasticsearch 中正确使用同义词功能 - 搜索客，搜索人自己的社区](https://elasticsearch.cn/article/14808)  
> [借助同义词让 Elasticsearch 更加强大 | Elastic Blog](https://www.elastic.co/cn/blog/boosting-the-power-of-elasticsearch-with-synonyms)  


> [CLUEbenchmark/SimCLUE: 3000000+语义理解与匹配数据集。可用于无监督对比学习、半监督学习等构建中文领域效果最好的预训练模型](https://github.com/CLUEbenchmark/SimCLUE)  
************************

# 向量搜索
版本 8.5+



