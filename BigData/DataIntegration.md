---
title: DataIntegration
date: 2024-04-10 14:17:16
tags: 
categories: 
---

💠

- 1. [Data Integration](#data-integration)
    - 1.1. [Datax](#datax)
    - 1.2. [SeaTunnel](#seatunnel)
    - 1.3. [FlinkX ChunJun](#flinkx-chunjun)
    - 1.4. [Flink CDC](#flink-cdc)

💠 2024-05-27 22:18:00
****************************************
# Data Integration
数据集成

## Datax
> [Github](https://github.com/alibaba/DataX)  阿里云DataWorks的开源版

> **注意** 这是一次性的开源项目，bug基本需要自己处理，从代码行数提交情况和issue，PR的活跃情况可以看出
- [Clickhouse reader writer](https://github.com/alibaba/DataX/pull/264)
- [Kafka writer](https://github.com/alibaba/DataX/pull/1856)

离线数据同步框架， 扩展读/写 Plugin 以支持多种数据源。  
核心框架负责处理流控，缓存，并发，自定义的[数据转换Transformer](https://github.com/alibaba/DataX/blob/master/transformer/doc/transformer.md)等。

- 特性
    - 轻量： 一份JSON配置启动一个Java进程
    - 支持线程级并发同步，按指定分批字段拆分数据 **限制分批字段整型或字符串**
    - 运行时定期展示流量，行数等进度信息
    - 支持脏数据探测，failfast
    - 支持流控策略配置 字节数，行数
- 限制
    - 不支持实时增量，离线增量需要手动调整JSON配置实现
    - 单进程模式，无法集群式同步，资源利用不够高(单任务在做好读端和写端的优化话是可以打满网卡的)

> [DataX 3.0 源码解析一](https://www.cnblogs.com/yaozhenfa/p/13840134.html)  

************************

## SeaTunnel
> [Github](https://github.com/apache/seatunnel)  

> [首个国人主导的开源数据集成工具：揭秘 Apache 顶级项目 SeaTunnel 背后的故事](https://36kr.com/p/2311155472330244)

使用 Spark、Flink 作为底层数据同步引擎使其具备分布式执行能力，开放并完善的插件体系和API集成

## FlinkX ChunJun
> [Github](https://github.com/DTStack/chunjun)  

## Flink CDC
> [Github](https://github.com/apache/flink-cdc)  

