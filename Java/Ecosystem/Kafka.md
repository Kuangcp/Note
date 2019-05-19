---
title: Kafaka.md
date: 2018-11-21 10:56:52
tags: 
categories: 
---

**目录 start**
 
1. [Kafaka](#kafaka)
    1. [安装](#安装)
        1. [Docker](#docker)

**目录 end**|_2019-05-19 23:30_|
****************************************
# Kafaka
> Apache顶级项目

> [参考博客: 初探Kafka Streams](http://ifeve.com/%e5%88%9d%e6%8e%a2kafka-streams/)

- [ksql](https://github.com/confluentinc/ksql)
> [参考博客: Kafka Topic Architecture](http://cloudurable.com/blog/kafka-architecture-topics/index.html)  


## 安装

### Docker
> [参考博客: docker部署kafka](https://blog.csdn.net/luanpeng825485697/article/details/81562755#commentBox)  

```sh
    # 启动 Zookeeper
    docker run -d --name kafka-zookeeper -p 2181:2181 --volume /etc/localtime:/etc/localtime wurstmeister/zookeeper

    # 启动 Kafka
    docker run -d --name kafka -p 9092:9092 --link kafka-zookeeper --env KAFKA_ZOOKEEPER_CONNECT=kafka-zookeeper:2181 --env KAFKA_ADVERTISED_HOST_NAME=localhost --env KAFKA_ADVERTISED_PORT=9092 --volume /etc/localtime:/etc/localtime wurstmeister/kafka
```

> 简单使用
1. 创建一个 topic  `bin/kafka-topics.sh --create --zookeeper kafka-zookeeper:2181 --replication-factor 1 --partitions 1 --topic mykafka`
1. 运行一个消息生产者并指定topic `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic mykafka`
    - 此时会提供一个输入命令行, 就能输入数据
1. 查看所有的topic列表 `bin/kafka-topics.sh --list --zookeeper kafka-zookeeper:2181`
1. 运行一个消费者并指定topic `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mykafka --from-beginning`
    - 会收到消息生产者输入的数据

