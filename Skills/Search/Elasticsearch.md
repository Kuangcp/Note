---
title: Elasticsearch
date: 2019-05-10 18:10:21
tags: 
categories: 
    - ELK
---

**目录 start**

1. [Elasticsearch](#elasticsearch)
    1. [Install](#install)
    1. [Java](#java)

**目录 end**|_2020-06-24 02:06_|
****************************************
# Elasticsearch
> [Official Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html)  
> [参考: Elasticsearch 快速开始](https://www.cnblogs.com/cjsblog/p/9439331.html)  

## Install
> [install](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) | [Docker](https://hub.docker.com/_/elasticsearch/)  
> [Guide to Elasticsearch in Java](https://www.baeldung.com/elasticsearch-java)  

`docker run -d --name es7 --net es-network -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms2560m -Xmx2560m"   elasticsearch:7.14.2`

### GUI
浏览器插件： Elasticvue


## Index 
