---
title: 远程调用
date: 2018-11-21 10:56:52
tags: 
    - RPC
categories: 
    - 分布式
---

💠

- 1. [RPC](#rpc)
    - 1.1. [架构设计](#架构设计)
    - 1.2. [HTTP](#http)
    - 1.3. [RPC vs MQ](#rpc-vs-mq)
- 2. [实践](#实践)

💠 2024-05-06 19:59:21
****************************************
# RPC
> Remote Procedure Calls 

- 进程间通信（IPC）是在多任务操作系统或联网的计算机之间运行的程序和进程所用的通信技术。分为两种
    - 本地过程调用LPC,用在多任务操作系统中，使得同时运行的任务能互相会话。这些任务共享内存空间使任务同步和互相发送信息。
    - 远程过程调用RPC,类似于LPC，只是调用方和被调用方中间隔了网络这一层

- 通常使用 IDL(Interface Definition) 建立接口定义, 达成约束, 一般指一种开发方式和规范, 具体的实现可以多样

> [Github rpc-framework ](https://github.com/topics/rpc-framework?l=java)

## 架构设计
> [如何手撸一个较为完整的RPC框架 ](https://juejin.cn/post/6992867064952127524)  

RPC 框架一般有这些组件：服务治理(注册发现)、负载均衡、容错、序列化/反序列化、编解码、网络传输、线程池、动态代理等，当然有的RPC框架还会有连接池、日志、安全等。

> [序列化](/Skills/Serialization/Serialization.md)

## HTTP
可以将常见的http的web请求，看作是前端调用服务端的方，服务端之间自然也是可以用HTTP实现RPC

针对RPC优化：长连接，HTTP2二进制协议

## RPC vs MQ

************************

# 实践

> [参考: 良好的RPC接口设计，需要注意这些方面](https://www.jianshu.com/p/dca5b00e72e4)