---
title: 服务端推送消息
date: 2020-12-15 14:15:47
tags: 
categories: 
---

**目录 start**

1. [Server push](#server-push)
    1. [企业平台](#企业平台)
        1. [GoEasy](#goeasy)
    1. [轮询](#轮询)
    1. [长连接](#长连接)
        1. [SSE](#sse)
        1. [Comet](#comet)
        1. [Websocket](#websocket)
    1. [DWR](#dwr)
    1. [HTTP2协议](#http2协议)

**目录 end**|_2020-12-15 14:16_|
****************************************
# Server push

## 企业平台

### GoEasy
- [官网](http://goeasy.io/cn/started) 免费12个月，后续要收费，这个的使用示例比较简单。

************************

## 轮询
- 前端使用 ajax 通过定时器的方式 的发起请求（最简单也是最容易耗尽服务器资源）

## 长连接

### SSE
> 本质是使用HTTP流式长连接(和下载文件类似)

- [Server-Sent Events（服务器推送） 教程](https://blog.p2hp.com/archives/7660)
- [sse demo](https://github.com/jokerwangJL/ssedemo)

- 优点
- 缺点

### Comet
- [github: comet4j 项目](https://github.com/jwangkun/comet4j) 可以直接下载配置jar到tomcat下使用
- [参考博客：comet4j java服务端推送消息到web页面实例](http://blog.csdn.net/shadowsick/article/details/9014139)

- 优点
- 缺点

### Websocket
- [使用Websocket进行消息推送](Skills/Network/Network.md#websocket)
- [代码片段：Springboot使用Websocket进行消息推送](https://gitee.com/kcp1104/codes/14ipgcbjyenxqu6tf9d0543)

- 优点
- 缺点

## DWR
> [官网](http://directwebremoting.org/dwr/index.html)

- 使用xmpp协议的一种技术，能够做到js中调用服务器的Java方法
	-  [参考博客：Spring整合DWR comet 实现无刷新 多人聊天室](http://www.cnblogs.com/hoojo/archive/2011/06/08/2075201.html#top)

- 优点
- 缺点

## HTTP2协议
> 刚开始提出 Server Push 特性的时候很多看好，但是现在HTTP3趋势下 该特性又沉寂了
