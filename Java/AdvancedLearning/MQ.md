---
title: MQ
date: 2018-11-21 10:56:52
tags: 
    - MQ
categories: 
    - Java
---

**目录 start**
 
1. [MQ](#mq)
    1. [为何需要使用](#为何需要使用)
    1. [风险分析](#风险分析)
    1. [JMS](#jms)
1. [MQ中间件](#mq中间件)
    1. [RocketMQ](#rocketmq)
    1. [ActiveMQ](#activemq)
    1. [Kafka](#kafka)
    1. [RabbitMQ](#rabbitmq)

**目录 end**|_2019-04-19 13:04_| [Kuangcp](https://github.com/Kuangcp/Note) | [yi-yun](https://github.com/yi-yun/Memo)
****************************************
# MQ

> [参考博客: MQ消息中间件](https://blog.csdn.net/qq_29676623/article/details/85108070)

## 为何需要使用
解耦、异步、削峰

## 风险分析
- 引入新系统, 增加了故障的风险

## JMS
> Java Message Service 规范而已,和JDBC一样, 具体实现由厂商来实现

[码农翻身:Java帝国之JMS的诞生](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513515&idx=1&sn=380bb1cb56d4151fd3acc5aa86f1da9a&chksm=80d67a68b7a1f37e3d98fe4495eab4db097eedd695c99fbd8704cc0464595842c4da598b99e3&scene=21#wechat_redirect)

# MQ中间件
## RocketMQ
> [有关demo](https://github.com/lirenzuo/rocketmq-rocketmq-all-4.1.0-incubating)

4.3 开始支持分布式事务

## ActiveMQ
> [Official Site](http://activemq.apache.org/)

## Kafka
> [Official Site](http://kafka.apache.org/)

## RabbitMQ
采用 Erlang 开发

> [参考博客: 我为什么要选择RabbitMQ ](https://www.sojson.com/blog/48.html)
