---
title: Nacos
date: 2024-01-11 23:00:53
tags: 
categories: 
---

💠

- 1. [Nacos](#nacos)
    - 1.1. [Design](#design)
- 2. [Tips](#tips)

💠 2025-05-06 11:19:53
****************************************
# Nacos
> [Nacos](https://nacos.io/en-us/)

## Design

> 配置加载

spring.cloud.config.override-none 默认false 设置true后,会优先使用本地配置（本地环境变量，本地properties文件等）覆盖远程配置（此配置需要配置在远程Nacos上）
- org.springframework.cloud.bootstrap.config.PropertySourceBootstrapConfiguration#insertPropertySources 处理逻辑

org.springframework.util.PropertyPlaceholderHelper#parseStringValue  
org.springframework.core.env.PropertySourcesPropertyResolver#logKeyFound 按顺序从 source 列表加载到第一个配置值就return  
- logging.level.org.springframework.core.env=DEBUG 开启日志查看加载情况


# Tips
> 集群模式出现节点数据不一致的情况
- 检查日志看是否网络中断或超时导致
- 重启集群

> Nacos 客户端 SocketTimeOut 异常
- 检查网络问题
- 检查应用端GC问题
