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

💠 2024-04-07 13:37:31
****************************************
# Nacos
> [Nacos](https://nacos.io/en-us/)

## Design

# Tips
> 集群模式出现节点数据不一致的情况
- 检查日志看是否网络中断或超时导致
- 重启集群

> Nacos 客户端 SocketTimeOut 异常
- 检查网络问题
- 检查应用端GC问题
