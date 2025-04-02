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

💠 2025-04-02 20:18:21
****************************************
# Nacos
> [Nacos](https://nacos.io/en-us/)

## Design

spring.cloud.config.override-none 默认false 开启后本地配置覆盖远程配置

# Tips
> 集群模式出现节点数据不一致的情况
- 检查日志看是否网络中断或超时导致
- 重启集群

> Nacos 客户端 SocketTimeOut 异常
- 检查网络问题
- 检查应用端GC问题
