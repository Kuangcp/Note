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
    - 6.1. [词库](#词库)
- 7. [向量搜索](#向量搜索)

💠 2026-01-28 00:01:03
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
- 重置初始用户的密码 bin/elasticsearcElash-reset-password -u elastic

> [参考: 用容器快速上手Elasticsearch](http://qinghua.github.io/elastic-search/)

## 集群
> [docker compose install cluster](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose-file)

## 客户端
- Kibana 官方支持Ela
- Elasticvue 浏览器插件

### Java
> [Guide to Elasticsearch in Java](https://www.baeldung.com/elasticsearch-java)`使用elasticsearch包访问ES`  
> [Spring Boot整合Elasticsearch](https://github.com/cloudgyb/es-spring-boot)`使用 SpringData`  


# Index 
- `PUT /{indexName}?pretty` 创建索引
- `DELETE /{indexName}?pretty` 删除索引 `异步,不可撤销,不可逆`
- 注意重命名操作对于ES是成本较大的操作，可以通过设置别名来适配业务，其次资源占用依次是： Clone，Snapshot/Restore，Reindex。

- `GET /{indexName}/_search` 搜索
- `GET /{indexName}/_doc/doc_id` 查询指定文档id
- `GET /{indexName}/_doc/doc_id` 新增或覆盖文档
- `POST /{indexName}/_update/doc_id` 新增或更新文档
- `POST /{indexName}/_bulk` 批量新增或更新

- `GET _cat/indices?v` 获取所有索引信息

************************

# Mapping
> [Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)

新增字段映射

```json
PUT /user_idx/_mapping
{
  "properties": {
    "age": {
      "type": "integer"
    }
  }
}
```
************************

# DSL
> [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

> [EQL](https://www.elastic.co/guide/en/elasticsearch/reference/current/eql.html)`Event Query Language`  

************************

# 分词器
目前中文领域常用的是ik和jieba

> [infinilabs/analysis-ik](https://github.com/infinilabs/analysis-ik)  

> [goto456/stopwords: 中文常用停用词表（哈工大停用词表、百度停用词表等）](https://github.com/goto456/stopwords)  
> [Elasticsearch：如何在 Elasticsearch 中正确使用同义词功能 - 搜索客，搜索人自己的社区](https://elasticsearch.cn/article/14808)  
> [借助同义词让 Elasticsearch 更加强大 | Elastic Blog](https://www.elastic.co/cn/blog/boosting-the-power-of-elasticsearch-with-synonyms)  


> [CLUEbenchmark/SimCLUE: 3000000+语义理解与匹配数据集。可用于无监督对比学习、半监督学习等构建中文领域效果最好的预训练模型](https://github.com/CLUEbenchmark/SimCLUE)  

## 词库
需要放在ES服务指定目录下，重启ES集群，所有节点都要加载词库文件：主节点，数据节点，协调节点。 词库是应用在数据节点的，主节点加载是为了分析分词器配置有效性，确保词库文件格式和路径正确（为啥不在放入的时候校验）。

当词库文件很大时，会导致节点启动时间变长
热更新问题：词库更改时需要重启所有节点，或者使用远程词库（http方式）

> 实践
- 核心词库：高频词汇，本地加载
- 扩展词库：低频词汇，远程加载或按需加载

************************
# 向量搜索
> [Vector search](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html)

版本 8.5+ 开始支持向量搜索

- 支持 kNN 搜索
- 支持 dense_vector 字段类型
- 支持 cosine similarity, dot_product, l2_norm 等相似度计算方式
- 支持 HNSW 算法加速搜索
- 支持与其他查询组合使用

主要应用场景:
- 图像相似度搜索
- 语义文本搜索
- 推荐系统
- 异常检测

示例:

1. 创建索引并配置向量字段:

```json
PUT /image_search
{
  "mappings": {
    "properties": {
      "image_id": {
        "type": "keyword"
      },
      "image_vector": {
        "type": "dense_vector",
        "dims": 512,
        "index": true,
        "similarity": "cosine"
      },
      "image_url": {
        "type": "keyword"
      },
      "tags": {
        "type": "keyword"
      }
    }
  }
}
```

2. 插入向量数据:

```json
POST /image_search/_doc
{
  "image_id": "img_001",
  "image_vector": [0.1, 0.2, 0.3, ...],
  "image_url": "https://example.com/img1.jpg",
  "tags": ["cat", "pet"]
}

POST /image_search/_doc
{
  "image_id": "img_002", 
  "image_vector": [0.2, 0.3, 0.4, ...],
  "image_url": "https://example.com/img2.jpg",
  "tags": ["dog", "pet"]
}
```

3. 执行向量搜索:

```json
GET /image_search/_search
{
  "query": {
    "knn": {
      "field": "image_vector",
      "query_vector": [0.15, 0.25, 0.35, ...],
      "k": 10,
      "num_candidates": 100
    }
  }
}
```

4. 向量搜索与其他查询组合:

```json
GET /image_search/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "knn": {
            "field": "image_vector",
            "query_vector": [0.15, 0.25, 0.35, ...],
            "k": 10,
            "num_candidates": 100
          }
        }
      ],
      "filter": [
        {
          "term": {
            "tags": "pet"
          }
        }
      ]
    }
  }
}
```

5. 混合搜索 (向量 + 文本):

```json
GET /image_search/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "knn": {
            "field": "image_vector",
            "query_vector": [0.15, 0.25, 0.35, ...],
            "k": 10,
            "num_candidates": 100
          }
        },
        {
          "match": {
            "tags": "cat"
          }
        }
      ]
    }
  }
}
```

6. 语义文本搜索示例:

```json
PUT /semantic_search
{
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "standard"
      },
      "content_vector": {
        "type": "dense_vector",
        "dims": 768,
        "index": true,
        "similarity": "cosine"
      }
    }
  }
}

POST /semantic_search/_doc
{
  "content": "人工智能技术正在快速发展",
  "content_vector": [0.1, 0.2, 0.3, ...]
}

GET /semantic_search/_search
{
  "query": {
    "knn": {
      "field": "content_vector",
      "query_vector": [0.12, 0.22, 0.32, ...],
      "k": 5
    }
  }
}
```

重要参数说明:

- `dims`: 向量维度，必须与插入的向量维度一致
- `index`: 是否建立索引，true 启用 HNSW 算法加速
- `similarity`: 相似度计算方式
  - `cosine`: 余弦相似度
  - `dot_product`: 点积相似度  
  - `l2_norm`: L2 范数距离
- `k`: 返回最相似的 k 个结果
- `num_candidates`: 候选数量，影响搜索精度和性能

性能优化建议:

1. 合理设置 `num_candidates` 参数
2. 使用 `filter` 减少搜索空间
3. 选择合适的相似度计算方式
4. 定期重建索引优化向量分布

> [参考: Elasticsearch 向量搜索最佳实践](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html#knn-search-best-practices)



