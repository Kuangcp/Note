---
title: AgentApp
date: 2026-06-14 01:06:31
tags: 
categories: 
---


💠

- 1. [Agent 应用实践](#agent-应用实践)
    - 1.1. [通信协议](#通信协议)

💠 2026-06-14 01:06:31
****************************************
# Agent 应用实践

## 通信协议
为了实现用户在弱网环境仍能流畅接收Agent的输出，通常需要实现：断线重连，Token序列的断点续传，TPOT的辅助优化 等功能

1. 激进直接上HTTP3 QUIC，就可以实现TCP的漂移了
1. 加一层WebSocket

目前我们的做法是Ws [netty-ws-starter](https://gitee.com/gin9/netty-ws-starter)  

用户通过WS连接上服务，然后WS层Handler发起请求到服务端的Agent应用，然后将响应的Token再放入Redis 队列  
Handler处理重连，心跳保持，断点续传，甚至TPOT的优化（因为现在有些模型不是传统的一个sse事件输出一个Token了，可能是攒批一样的把多个token作为一个SSE事件响应出来，如果按大模型的响应流速来做真实渲染的话，就会感觉的一卡一卡的，所以还可以在这一层把一个sse事件套一层分词或者简单的字符串长度拆分后再入Redis队列，这样不需要多个客户端平台来处理渲染的优化）



