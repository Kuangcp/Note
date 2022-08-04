---
title: MQ理论基础
date: 2022-08-03 10:03:18
tags: 
categories: 
---

**目录 start**

1. [MQ理论](#mq理论)
1. [问题和方案](#问题和方案)
    1. [消息丢失](#消息丢失)
        1. [生产端](#生产端)
        1. [MQ自身](#mq自身)
        1. [消费端](#消费端)
    1. [消息重复](#消息重复)
    1. [消费顺序](#消费顺序)

**目录 end**|_2022-08-03 10:03_|
****************************************
# MQ设计理论

# 问题和方案
## 消息丢失
### 生产端
原因：异步发送 mq在生产端的client和MQ通信出现故障， 或者 上线时生产端未执行完就被重启了

发送消息的ack机制，规避掉MQ中的异步发送机制，生产端发送消息时，同步等待MQ确认收到消息后才返回

### MQ自身

### 消费端

原因： 自动确认消息机制，消费到消息就通知MQ消费完成，实际上消费者可能消费到消息正准备处理业务，节点突然down了。  
调整为消息消费完成才提交确认。消息的消费实现幂等利于重试

## 消息重复
原因： MQ未收到消费端的消费确认消息，消费端宕机等

消费端实现幂等。
- 构造业务id利用持久层（Redis MySQL等）来判断是否重复

## 消费顺序
扩展高可用性和顺序消费是一个取舍的问题

每个MQ的特性会不一样，实现思路大体相似，让MQ的消息控制于一个物理队列或者逻辑队列中，并将消费端限制为一个。
消费端改为多个就需要应用层自身实现消息的消费是并行，但是提交是有序的。

## 消息积压
原因：生产端TPS异常升高、消费端TPS下降或故障

