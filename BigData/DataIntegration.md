---
title: DataIntegration
date: 2024-04-10 14:17:16
tags: 
categories: 
---

💠

- 1. [Data Integration](#data-integration)
- 2. [Datax](#datax)
    - 2.1. [设计](#设计)
    - 2.2. [组件](#组件)
        - 2.2.1. [Reader](#reader)
        - 2.2.2. [Writer](#writer)
- 3. [SeaTunnel](#seatunnel)
- 4. [FlinkX ChunJun](#flinkx-chunjun)
- 5. [Flink CDC](#flink-cdc)

💠 2024-06-06 16:55:18
****************************************
# Data Integration
数据集成

# Datax
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

## 设计
> [DataX 3.0 源码解析一](https://www.cnblogs.com/yaozhenfa/p/13840134.html)  

- Job 负责管理 JobContainer
- Task 执行读写 TaskGroupContainer.TaskExecutor 

## 组件
### Reader

通过splitPk和并发 拆分上游数据 并行同步逻辑
- com.alibaba.datax.plugin.rdbms.reader.util.SingleTableSplitUtil#genPKSql
- com.alibaba.datax.plugin.rdbms.reader.util.SingleTableSplitUtil#splitSingleTable  注意设置的splitPK字段的值最好是 数字字母常见的打印字符
	- 参数 expectSliceNumber 的来源于Datax.json的直接指定和 限速channel，限速速率等取较小值。
	- 由于拆分是按ascii实现（先将字符串按ascii转为超大整数BigInteger，做完分段拆分后将若干段的边界值转回ascii），于是拆分的分段字符就会有乱码，导致拆分分段有交叉导致同步的数据量大于上游数据总量
		```java
		List<String> result = RdbmsRangeSplitWrap.splitAndWrap("202301", "202412", 4, "period", "'", DataBaseType.PostgreSQL);
		// 结果： [ ('202301' <= period AND period < '2023PR') ,  ('2023PR' <= period AND period < '2023pr') ,  ('2023pr' <= period AND period < '2024') ,  ('2024' <= period AND period <= '202412') ]

		List<String> result = RdbmsRangeSplitWrap.splitAndWrap("2016-02-06", "2024-05-06", 4, "period", "'", DataBaseType.PostgreSQL);
		// 结果的数组中有元素的字面值包含了控制字符 \r. 将生成的SQL去查数据库没有问题，拆分的四段只有13段能查出数据 24段数据为空
		// 应该是概率性出现问题，因为这个字符转int的做法导致了字符的边界互相影响了，范围SQL产生了交集
		```

### Writer

com.alibaba.datax.plugin.rdbms.writer.CommonRdbmsWriter.Task#startWriteWithConnection **模板类** 消费Reader的数据 批量写入目标库

两个参数，任一条件满足就执行一次insert
- batchSize 默认2048
- batchByteSize 默认32mib 
	- 该参数值需要谨慎设置，此大小是每个Task都需要的缓存区大小，如果设置过大，会发生OOM
	- 例如设置堆内存1G 5并发 该值200Mib时，刚开始同步就会触发OOM，因为堆内存不够，没有留空间给datax自身


************************

# SeaTunnel
> [Github](https://github.com/apache/seatunnel)  

> [首个国人主导的开源数据集成工具：揭秘 Apache 顶级项目 SeaTunnel 背后的故事](https://36kr.com/p/2311155472330244)

使用 Spark、Flink 作为底层数据同步引擎使其具备分布式执行能力，开放并完善的插件体系和API集成

# FlinkX ChunJun
> [Github](https://github.com/DTStack/chunjun)  

# Flink CDC
> [Github](https://github.com/apache/flink-cdc)  

