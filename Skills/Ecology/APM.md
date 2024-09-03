---
title: APM
date: 2024-03-23 17:52:21
tags: 
categories: 
---

💠

- 1. [APM](#apm)
    - 1.1. [OpenTelemetry](#opentelemetry)
    - 1.2. [SkyWalking](#skywalking)
    - 1.3. [Sentry](#sentry)
    - 1.4. [CAT](#cat)
- 2. [采集客户端](#采集客户端)
- 3. [Monitoring](#monitoring)
    - 3.1. [Prometheus](#prometheus)

💠 2024-09-03 21:27:16
****************************************
# APM
> Application performance Management `分布式链路追踪，技术或业务指标监控告警`

核心为 可观测性(Observability) 监测(Monitoring)

> [Github: APM](https://github.com/topics/apm)

[Glowroot](https://github.com/glowroot/glowroot)`技术指标 Web SQL JVM JMX监控，agent方式支持单机和集群（存储使用cassandra）`  

Pinpoint
[JavaMelody](https://github.com/javamelody/javamelody)
[Scouter](https://github.com/scouter-project/scouter)
[Stagemonitor](https://github.com/stagemonitor/stagemonitor)
[MoSKito](https://github.com/anotheria/moskito)

## OpenTelemetry 
[Github: OpenTelemetry](https://github.com/open-telemetry)

CNCF组织的项目，脱离语言和技术架构，更有发展前景的可观测性项目。

## SkyWalking
> [Official Site](http://skywalking.apache.org/)  | [Downloads](https://skywalking.apache.org/downloads/)]

[server](https://hub.docker.com/r/apache/skywalking-oap-server) | [ui](https://hub.docker.com/r/apache/skywalking-ui)

```sh
docker run --name oap -p 12340:1234 -p 11800:11800 -p 12800:12800  -d apache/skywalking-oap-server:8.3.0-es6
docker run --name oap-ui -p 8080:8080 -d -e SW_OAP_ADDRESS=http://192.168.7.54:12800 apache/skywalking-ui
```

应用启动 java -javaagent:/opt/apache-skywalking-apm-bin/agent/skywalking-agent.jar -Dskywalking.agent.service_name=xxxtest -Dskywalking.collector.backend_service=127.0.0.1:11800 -jar application.jar

************************

## Sentry 
[Github](https://github.com/getsentry/sentry)

[Docker compose 部署](https://github.com/getsentry/self-hosted)

感知应用异常:

[UncaughtExceptionHandlerIntegration](https://github.com/getsentry/sentry-java/blob/main/sentry/src/main/java/io/sentry/UncaughtExceptionHandlerIntegration.java) + LogAppender

************************

## CAT
> [陆金所 CAT 优化实践](https://www.infoq.cn/article/XvGZcW312MdatCKFMR8b)

> [Github: cat-docker](https://github.com/lghuntfor/cat-docker)  
> [深度剖析开源分布式监控CAT](https://tech.meituan.com/2018/11/01/cat-in-depth-java-application-monitoring.html)

感知应用异常： 

1. 实现日志框架的Appender基类，捕获Error到 `Cat.logError`，并手动声明该Appender到配置文件中
2. 手动设置**静态**的默认全局异常处理`Thread.setDefaultUncaughtExceptionHandler`，防止异常漏捕获。
    - SpringBoot项目里发生机率较小,因为基本都有Controller层的全局异常处理，且大部分请和逻辑从web端进入。
    - 只有自定义线程池,Scheduler线程池,Junit等地方，未捕获运行时异常，才会走默认逻辑异常栈被输出到标准错误 System.err 中。

************************
# 采集客户端
- [Prometheus: JMX Exporter](https://github.com/prometheus/jmx_exporter)
- [micrometer](https://github.com/micrometer-metrics/micrometer)`门面框架类似于SLF4J 支持多种采集`
    - [Quick Guide to Micrometer](https://www.baeldung.com/micrometer)

- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)

************************

# Monitoring
技术指标监控告警，离业务指标比较远，例如 主机，数据库，容器，网络

## Prometheus
[Github: Prometheus](https://github.com/prometheus/prometheus)

通常和 Grafana 结合使用

> [Prometheus+Grafana监控SpringBoot项目JVM信息](https://developer.aliyun.com/article/890169) `JMX Exporter`
> [JVM 接入 Prometheus](https://cloud.tencent.com/document/product/1416/56032)`手动声明HTTP`

> [Prometheus running on Kubernetes ](https://github.com/prometheus-operator/kube-prometheus)

