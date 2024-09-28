---
title: 消息队列
date: 2018-11-21 10:56:52
tags: 
    - MQ
categories: 
---

💠

- 1. [MQ](#mq)
    - 1.1. [为何需要使用](#为何需要使用)
    - 1.2. [风险分析](#风险分析)
    - 1.3. [JMS](#jms)
- 2. [MQ中间件](#mq中间件)
    - 2.1. [RocketMQ](#rocketmq)
    - 2.2. [ActiveMQ](#activemq)
    - 2.3. [Kafka](#kafka)
    - 2.4. [RabbitMQ](#rabbitmq)
    - 2.5. [Pulsar](#pulsar)
    - 2.6. [nsq](#nsq)

💠 2024-09-28 11:21:46
****************************************
# MQ

> [参考: MQ消息中间件](https://blog.csdn.net/qq_29676623/article/details/85108070)

## 为何需要使用
解耦、异步、削峰

## 风险分析
- 引入新系统, 增加了故障的风险

## JMS
> Java Message Service 规范而已,和JDBC一样, 具体实现由厂商来实现

[码农翻身:Java帝国之JMS的诞生](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513515&idx=1&sn=380bb1cb56d4151fd3acc5aa86f1da9a&chksm=80d67a68b7a1f37e3d98fe4495eab4db097eedd695c99fbd8704cc0464595842c4da598b99e3&scene=21#wechat_redirect)

************************

# MQ中间件
> [Kafka vs. Pulsar vs. RabbitMQ](https://www.confluent.io/kafka-vs-pulsar/)

## RocketMQ
> [有关demo](https://github.com/lirenzuo/rocketmq-rocketmq-all-4.1.0-incubating)

4.3 开始支持[事务消息](https://rocketmq.apache.org/zh/docs/featureBehavior/04transactionmessage/)
- [RocketMQ是如何实现事务消息的](https://github.com/Cicizz/binary/blob/master/RocketMQ/RocketMQ%E4%BA%8B%E5%8A%A1%E6%B6%88%E6%81%AF/RocketMQ%E6%98%AF%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E4%BA%8B%E5%8A%A1%E6%B6%88%E6%81%AF%E7%9A%84.md)

## ActiveMQ
> [Official Site](http://activemq.apache.org/)

## Kafka
[Kafka](./Kafka.md)  
[Redpanda](https://github.com/redpanda-data/redpanda)  

## RabbitMQ
采用 Erlang 开发

> [参考: 我为什么要选择RabbitMQ ](https://www.sojson.com/blog/48.html)

## Pulsar

## nsq
