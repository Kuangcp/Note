---
title: DataIntegration
date: 2024-04-10 14:17:16
tags: 
categories: 
---

💠

- 1. [Data Integration](#data-integration)
- 2. [Datax](#datax)
    - 2.1. [使用](#使用)
        - 2.1.1. [Tips](#tips)
    - 2.2. [设计](#设计)
    - 2.3. [组件](#组件)
        - 2.3.1. [Reader](#reader)
        - 2.3.2. [Writer](#writer)
- 3. [SeaTunnel](#seatunnel)
- 4. [FlinkX ChunJun](#flinkx-chunjun)
- 5. [Flink CDC](#flink-cdc)
- 6. [Kettle](#kettle)

💠 2024-08-29 15:44:41
****************************************
# Data Integration
数据集成

# Datax
> [Github](https://github.com/alibaba/DataX)  阿里云DataWorks的开源版 | [HashData](https://github.com/HashDataInc/DataX/) 增加了插件支持

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

## 使用
> [使用手册](https://github.com/alibaba/DataX/blob/master/userGuid.md)


### Tips
- 配置的json文件要`严格按照案例JSON来配置`，因为他不是按对象解析是按无结构json来顺序解析的，踩过一个坑就是writer在reader上面，然后驱动加载出问题了，查看对应源码和jvm的加载类发现是有的，很隐蔽的报错，完全想不到是json配置顺序问题。

> [为什么不建议使用DataX读写GreenPlum](https://www.modb.pro/db/52542) 不建议用 postgresqlwriter,可以用 [HashData DataX](https://github.com/HashDataInc/DataX) 的 gpdbwriter 插件替代  
> 打包指定模块 mvn clean package -DskipTests assembly:assembly -pl plugin-rdbms-util -am

************************

## 设计
> [DataX 3.0 源码解析一](https://www.cnblogs.com/yaozhenfa/p/13840134.html)  | [DataX核心源码流程](https://blog.csdn.net/ooeeerrtt/article/details/123779721)

![](./img/datax-main-process.png)

- Job 负责管理 JobContainer
- Task 执行读写 TaskGroupContainer.TaskExecutor 
    - readerThread writerThread 实现多线程的生产者消费者模型 通过 com.alibaba.datax.core.statistics.communication.Communication 通信

## 组件
### Reader
- table模式： 只配置源表的 column，不灵活（需要源表对目标表字段名和类型一致）但支持并发。
- querySQL模式：配置源表查询SQL，可以join，别名，函数计算。更灵活但是**不支持并发**，同步性能差

> 并行同步： 通过splitPk:拆分字段`只支持整数，字符串` 和 speed.channel: 并发数 去拆分上游数据
- com.alibaba.datax.plugin.rdbms.reader.util.SingleTableSplitUtil#genPKSql
- com.alibaba.datax.plugin.rdbms.reader.util.SingleTableSplitUtil#splitSingleTable 注意设置的splitPK字段的值最好是 数字字母常见的打印字符
	- 参数 expectSliceNumber 的来源于Datax.json的直接指定和 限速channel，限速速率等取较小值。
	- 由于拆分是按ascii实现（先将字符串按ascii转为超大整数BigInteger，做完分段拆分后将若干段的边界值转回ascii）
		```java
		List<String> result = RdbmsRangeSplitWrap.splitAndWrap("202301", "202412", 4, "period", "'", DataBaseType.PostgreSQL);
		// 结果： [ ('202301' <= period AND period < '2023PR') ,  ('2023PR' <= period AND period < '2023pr') ,  ('2023pr' <= period AND period < '2024') ,  ('2024' <= period AND period <= '202412') ]

		List<String> result = RdbmsRangeSplitWrap.splitAndWrap("2016-02-06", "2024-05-06", 4, "period", "'", DataBaseType.PostgreSQL);
		// 结果的数组中有元素的字面值包含了控制字符 \r. 将生成的SQL去查数据库没有问题，拆分的四段只有13段能查出数据 24段数据为空
		```
    - TODO 但是出现过分段后数据范围有交叉导致同步的数据量大于上游数据总量， 可能是概率性出现问题，因为这个字符转int的做法导致了字符的边界互相影响了，范围SQL产生了交集？
    - 特定优化思路：将拆分列查出全部去重值后构造出分批in的SQL。 优点：将以该列的数据分布情况并发同步，贴合数据的业务特点。缺点：如果该列的去重值非常多，SQL会超长。
- 拆分后同样是游标查询 com.alibaba.datax.plugin.rdbms.reader.CommonRdbmsReader.Task#startRead
    - `ResultSet query(Connection conn, String sql, int fetchSize)`

### Writer

com.alibaba.datax.plugin.rdbms.writer.CommonRdbmsWriter.Task#startWriteWithConnection **模板类** 消费Reader的数据 批量写入目标库

> 两个参数，任一条件满足就执行一次insert
- batchSize 默认2048
- batchByteSize 默认32mib 
	- 该参数值需要谨慎设置，此大小是每个Task都需要的缓存区大小，如果设置过大，会发生OOM
	- 例如设置堆内存1G 5并发 该值200Mib时，刚开始同步就会触发OOM，因为堆内存不够，没有留空间给datax自身

************************

# SeaTunnel
> [Github](https://github.com/apache/seatunnel) | [关于 SeaTunnel](https://seatunnel.apache.org/zh-CN/docs/about)  

> [首个国人主导的开源数据集成工具：揭秘 Apache 顶级项目 SeaTunnel 背后的故事](https://36kr.com/p/2311155472330244)

使用 Spark、Flink 作为底层数据同步引擎使其具备分布式执行能力，开放并完善的插件体系和API集成。  
核心流程为 Source -> Transform -> Sink 。 Source 和 Sink 统称为Connector 负责读写数据库， Transform负责数据转换：别名映射，函数处理过滤。  

这个架构设计将读和转换分离了，就没有Datax的两个模式所面临的问题，既支持读数据时做别名，也支持并发。

************************

> [并行读取](https://seatunnel.apache.org/zh-CN/docs/connector-v2/source/Jdbc#parallel-reader) 支持 数值，字符串，日期 类型字段
- 生成拆分列逻辑  ChunkSplitter#generateSplits 字符串类型字段采用的是hash后取模方式 ` JdbcDialect#hashModForField` pg,oracle,mssql。
- 执行数据拆分 FixedChunkSplitter#createSplitStatement

************************

# FlinkX ChunJun
> [Github](https://github.com/DTStack/chunjun)  

# Flink CDC
> [Github](https://github.com/apache/flink-cdc)  


************************

# Kettle
> [Github](https://github.com/pentaho/pentaho-kettle)  
> [web kettle](https://github.com/JoeyBling/webkettle)  

[kettle java源码 kettle源码分析](https://blog.51cto.com/u_16213668/8667940)

************************

> [Kettle大量数据快速导出的解决方案](https://www.cnblogs.com/47Gamer/p/13993373.html)`奇怪的是SpringBoot项目同样Fetch方式加流式Excel导出，整体导出效率低很多`
- 关联源码在 org.pentaho.di.trans.steps 下的 tableinput 和 excelwriter 包
