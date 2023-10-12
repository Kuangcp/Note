---
title: Kafka
date: 2018-11-21 10:56:52
tags: 
categories: 
---

💠

- 1. [Kafka](#kafka)
    - 1.1. [安装](#安装)
        - 1.1.1. [Docker](#docker)

💠 2023-10-12 11:48
****************************************
# Kafka
> [Official Doc](https://kafka.apache.org/21/documentation.html)  

> [参考: 初探Kafka Streams](http://ifeve.com/%e5%88%9d%e6%8e%a2kafka-streams/)  
- [ksql](https://github.com/confluentinc/ksql)  
> [参考: Kafka Topic Architecture](http://cloudurable.com/blog/kafka-architecture-topics/index.html)  

> [参考: Apche Kafka 的生与死 – failover 机制详解](https://www.cnblogs.com/fxjwind/p/4972244.html) `解释 I wrote this conflicted ephemeral node`  

## 安装

### Docker
> [参考: docker部署kafka](https://blog.csdn.net/luanpeng825485697/article/details/81562755#commentBox)  

> Kafka 容器的创建强制性依赖 Zookeeper, 但是在使用中可以直接使用Kafka
```sh
    # 启动 Zookeeper
    docker run -d --name kafka-zookeeper -p 2181:2181 --volume /etc/localtime:/etc/localtime wurstmeister/zookeeper

    # 启动 Kafka
    docker run -d --name kafka -p 9092:9092 --link kafka-zookeeper --env KAFKA_ZOOKEEPER_CONNECT=kafka-zookeeper:2181 --env KAFKA_ADVERTISED_HOST_NAME=localhost --env KAFKA_ADVERTISED_PORT=9092 --volume /etc/localtime:/etc/localtime wurstmeister/kafka
```

> Hello World

/opt/kafka_xxx 目录下

1. 创建一个 topic  `bin/kafka-topics.sh --create --zookeeper kafka-zookeeper:2181 --replication-factor 1 --partitions 1 --topic mykafka`
1. 运行一个消息生产者并指定topic `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic mykafka`
    - 此时会提供一个输入命令行, 就能输入发送的消息内容
1. 查看所有的topic列表 `bin/kafka-topics.sh --list --zookeeper kafka-zookeeper:2181`
    - 或者 `bin/kafka-topics.sh --list --bootstrap-server 127.0.0.1:9092`
1. 运行一个消费者并指定topic `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mykafka --from-beginning`
    - 会收到消息生产者输入的内容

************************
> [参考: 深度解读：Kafka 放弃 ZooKeeper，消息系统兴起二次革命](https://www.infoq.cn/article/phf3gfjutdhwmctg6kxe)  

> 自2.8.0开始 Kafka移除了Zookeeper依赖 可单独启动 [Docker: bitnami/kafka](https://hub.docker.com/r/bitnami/kafka)  


