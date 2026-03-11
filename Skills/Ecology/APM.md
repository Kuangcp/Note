---
title: APM
date: 2024-03-23 17:52:21
tags: 
categories: 
---

💠

- 1. [可观测性基础概念](#可观测性基础概念)
- 2. [核心支柱](#核心支柱)
    - 2.1. [链路追踪 (Tracing)](#链路追踪-tracing)
    - 2.2. [指标监控 (Metrics)](#指标监控-metrics)
    - 2.3. [日志管理 (Logging)](#日志管理-logging)
- 3. [技术标准与协议](#技术标准与协议)
    - 3.1. [OpenTelemetry](#opentelemetry)
    - 3.2. [OpenMetrics](#openmetrics)
- 4. [全栈 APM 平台](#全栈-apm-平台)
    - 4.1. [SkyWalking](#skywalking)
    - 4.2. [Sentry](#sentry)
    - 4.3. [CAT](#cat)
- 5. [专用追踪系统 Tracing](#专用追踪系统-tracing)
- 6. [时序数据库与监控 Metrics](#时序数据库与监控-metrics)
    - 6.1. [Prometheus](#prometheus)
- 7. [采集与埋点](#采集与埋点)
    - 7.1. [Java Agent 探针（无侵入采集）](#java-agent-探针无侵入采集)
    - 7.2. [Micrometer 指标门面](#micrometer-指标门面)
    - 7.3. [Prometheus Exporter](#prometheus-exporter)
    - 7.4. [OpenTelemetry Collector](#opentelemetry-collector)

💠 2026-03-11 14:17:09
****************************************

# 可观测性基础概念

> Observability = 可观测性 ≠ 监控 (Monitoring)

| 维度 | 监控 (Monitoring) | 可观测性 (Observability) |
|------|------------------|-------------------------|
| 目标 | 已知问题的检测 | 未知问题的探索 |
| 数据 | 预定义指标 | 多源信号（链路/指标/日志） |
| 方式 | 被动告警 | 主动分析 |
| 问题 | "系统是否健康？" | "为什么系统不健康？" |

三大支柱：Tracing（链路）+ Metrics（指标）+ Logging（日志）

# 核心支柱

## 链路追踪 (Tracing)
分布式系统的请求路径追踪，解决跨服务调用问题

- **代表产品**：Jaeger, Zipkin, SkyWalking, Tempo
- **核心概念**：Trace → Span → Tag/Event

## 指标监控 (Metrics)
可聚合的数值型数据，用于趋势分析和告警

- **代表产品**：Prometheus, VictoriaMetrics, InfluxDB
- **核心概念**：Counter, Gauge, Histogram, Summary

## 日志管理 (Logging)
离散的事件记录，用于详细排查

- **代表产品**：ELK, Loki, Fluentd
- **核心概念**：结构化日志、日志聚合、日志追踪关联

# 技术标准与协议

## OpenTelemetry
> [Github: OpenTelemetry](https://github.com/open-telemetry)

**定位**：CNCF 毕业项目，可观测性的"标准接口"

**核心价值**：
- 统一采集标准（替代 OpenTracing + OpenCensus）
- 脱离语言和架构，提供一致的埋点 API
- 支持自动 instrumentation 和手动埋点

**架构组件**：
- **API/SDK**：应用埋点库
- **Collector**：采集网关（接收/处理/导出）
- **Protocol**：OTLP 传输协议（gRPC/HTTP）

## OpenMetrics
Prometheus 指标格式的开放标准，云原生监控的事实标准


# 全栈 APM 平台
> Application performance Management `分布式链路追踪，技术或业务指标监控告警`

Tracing + Metrics + Logging  一站式解决方案，适合快速搭建

> [Github: APM](https://github.com/topics/apm)

- [Glowroot](https://github.com/glowroot/glowroot)`技术指标 Web SQL JVM JMX监控，agent方式` 默认H2数据库，可支持Mongo，ES，Kafka等  
- [pinpoint-apm/pinpoint](https://github.com/pinpoint-apm/pinpoint)  
- [JavaMelody](https://github.com/javamelody/javamelody)
- [Scouter](https://github.com/scouter-project/scouter)
- [Stagemonitor](https://github.com/stagemonitor/stagemonitor)
- [MoSKito](https://github.com/anotheria/moskito)


| 产品 | 特点 | 存储后端 | 适用场景 |
|------|------|---------|---------|
| **SkyWalking** | 国产 Apache 项目，Java 生态友好 | ES/H2/MySQL/TiDB | 中大型微服务 |
| **Pinpoint** | 韩国开源，代码级追踪，侵入性强 | HBase | 深度排查 |
| **CAT** | 美团开源，实时性高，国内大厂用得多 | MySQL/ES | 高并发电商 |
| **Sentry** | 专注异常追踪，前端友好 | PostgreSQL | 错误监控为主 |

## SkyWalking
> [Official Site](http://skywalking.apache.org/)  | [Downloads](https://skywalking.apache.org/downloads/)]

[server](https://hub.docker.com/r/apache/skywalking-oap-server) | [ui](https://hub.docker.com/r/apache/skywalking-ui)

```sh
docker run --name oap -p 12340:1234 -p 11800:11800 -p 12800:12800  -d apache/skywalking-oap-server:8.3.0-es6
docker run --name oap-ui -p 8080:8080 -d -e SW_OAP_ADDRESS=http://192.168.7.54:12800 apache/skywalking-ui
```

应用启动 java -javaagent:/opt/apache-skywalking-apm-bin/agent/skywalking-agent.jar -Dskywalking.agent.service_name=xxxtest -Dskywalking.collector.backend_service=127.0.0.1:11800 -jar application.jar

## Sentry 
[Github](https://github.com/getsentry/sentry)

[Docker compose 部署](https://github.com/getsentry/self-hosted)

感知应用异常:

[UncaughtExceptionHandlerIntegration](https://github.com/getsentry/sentry-java/blob/main/sentry/src/main/java/io/sentry/UncaughtExceptionHandlerIntegration.java) + LogAppender

## CAT
> [陆金所 CAT 优化实践](https://www.infoq.cn/article/XvGZcW312MdatCKFMR8b)

> [Github: cat-docker](https://github.com/lghuntfor/cat-docker)  
> [深度剖析开源分布式监控CAT](https://tech.meituan.com/2018/11/01/cat-in-depth-java-application-monitoring.html)

感知应用异常： 

1. 实现日志框架的Appender基类，捕获Error到 `Cat.logError`，并手动声明该Appender到配置文件中
2. 手动设置**静态**的默认全局异常处理`Thread.setDefaultUncaughtExceptionHandler`，防止异常漏捕获。
    - SpringBoot项目里发生机率较小,因为基本都有Controller层的全局异常处理，且大部分请和逻辑从web端进入。
    - 只有自定义线程池,Scheduler线程池,Junit等地方，未捕获运行时异常，才会走默认逻辑异常栈被输出到标准错误 System.err 中。

# 专用追踪系统 Tracing
- **Jaeger**：Uber 开源，云原生设计，Kubernetes 友好
- **Tempo**：Grafana 生态，轻量级，与 Loki/Prometheus 集成好
- **Zipkin**：Twitter 开源，历史悠久，社区成熟

# 时序数据库与监控 Metrics
- **Prometheus**：云原生指标监控标准，Pull 模式
- **VictoriaMetrics**：高性能 Prometheus 兼容存储
- **InfluxDB**：时序数据库，Push 模式
- **Grafana**：可视化平台，非采集系统但通常配套使用

## Prometheus
[Github: Prometheus](https://github.com/prometheus/prometheus)

通常和 Grafana 结合使用

> [Prometheus+Grafana监控SpringBoot项目JVM信息](https://developer.aliyun.com/article/890169) `JMX Exporter`
> [JVM 接入 Prometheus](https://cloud.tencent.com/document/product/1416/56032)`手动声明HTTP`

> [Prometheus running on Kubernetes ](https://github.com/prometheus-operator/kube-prometheus)

默认是拉模式，如果想通过推模式采集应用端信息需要借助 PushGateway 组件


# 采集与埋点
- [Prometheus: JMX Exporter](https://github.com/prometheus/jmx_exporter)
- [micrometer](https://github.com/micrometer-metrics/micrometer)`门面框架类似于SLF4J 支持多种采集`
    - [Quick Guide to Micrometer](https://www.baeldung.com/micrometer)

- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)
- LoongCollector （原阿里云 Logtail 开源版）

## Java Agent 探针（无侵入采集）
- **SkyWalking Java Agent**：字节码增强，自动埋点
- **Pinpoint Agent**：更重的探针，详细调用链
- **Glowroot**：轻量级，Web 界面，H2/Mongo/ES 存储
- **JavaMelody**：传统监控，JVM/HTTP/SQL 监控

## Micrometer 指标门面
> [Github: micrometer](https://github.com/micrometer-metrics/micrometer)

技术指标监控告警，离业务指标比较远，例如 主机，数据库，容器，网络

**定位**：指标界的 SLF4J，统一抽象层

**适配后端**：Prometheus, Datadog, CloudWatch, InfluxDB 等

## Prometheus Exporter
- **JMX Exporter**：暴露 JVM 指标到 Prometheus
- **自定义 Exporter**：业务指标暴露（HTTP /metrics 端点）

## OpenTelemetry Collector
**定位**：采集网关，统一接收 OTLP，转发到多个后端

**部署模式**：
- Agent 模式（Sidecar，与应用同节点）
- Gateway 模式（集群级汇聚）


