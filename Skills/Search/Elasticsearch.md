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

💠 2023-10-12 11:48
****************************************
# Elasticsearch
> [Official Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html)  
> [参考: Elasticsearch 快速开始](https://www.cnblogs.com/cjsblog/p/9439331.html)  

## Install
> [install](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) | [Docker](https://hub.docker.com/_/elasticsearch/)  
> [Guide to Elasticsearch in Java](https://www.baeldung.com/elasticsearch-java)  

1. `docker network create es-network`
1. `docker run -d --name es7 --net es-network -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms2560m -Xmx2560m"   elasticsearch:7.14.2`

> [参考: 用容器快速上手Elasticsearch](http://qinghua.github.io/elastic-search/)

入门：构建出 RestHighLevelClient  使用 bulk search 接口 

### GUI
浏览器插件： Elasticvue


## Index 
