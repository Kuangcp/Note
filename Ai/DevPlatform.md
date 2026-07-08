---
title: DevPlatform
date: 2025-01-10 16:30:07
tags: 
categories: 
---

💠

- 1. [开发平台](#开发平台)
- 2. [RAG](#rag)
    - 2.1. [QAnything](#qanything)
- 3. [综合平台](#综合平台)
    - 3.1. [FastGPT](#fastgpt)
    - 3.2. [Dify](#dify)
    - 3.3. [RagFlow](#ragflow)
        - 3.3.1. [Tips](#tips)

💠 2026-07-08 16:02:50
****************************************
# 开发平台

# RAG

## QAnything
> [netease-youdao/QAnything: Question and Answer based on Anything.](https://github.com/netease-youdao/QAnything)  
> [来自工业界的 RAG 服务，有道 QAnything 源码全流程深度解析 - 知乎](https://zhuanlan.zhihu.com/p/697031773)  

> [为RAG而生-BCE embedding技术报告 - 知乎](https://zhuanlan.zhihu.com/p/681370855)  

更新频率低,已废弃，可作为学习参考

************************

# 综合平台
## FastGPT
> [labring/FastGPT](https://github.com/labring/FastGPT)  

知识库平台

> [一款纯 js 实现的大模型应用服务 FastGPT 解读 - 易迟的博客 | Bryan Blog](https://hustyichi.github.io/2024/07/04/fastgpt/)  
> [FastGPT解密 - cumber的专栏 - 掘金](https://juejin.cn/column/7350107540326236169)  

> [FastGPT Rag模块](/Ai/Rag.md#fastgpt)  

## Dify
> [Dify | Dify](https://docs.dify.ai/zh-hans)  


> Api方式调用 实质是一个HTTP SSE请求，在response中推事件给客户端

通常是 node_started text_chunk node_finished workflow_finished。 流式回复通过text_chunk实现，但是目前存在bug在复杂的if流程中 chunk可能会被合并输出，达不到流效果。

> [Dify Rag模块](/Ai/Rag.md#dify)  
## RagFlow
> [infiniflow/ragflow: RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding.](https://github.com/infiniflow/ragflow?tab=readme-ov-file)  

### Tips
> [IF ELSE can cause the Stream output of LLM nodes to fail](https://github.com/langgenius/dify/issues/12068) if else连接的流式LLM输出变非流了  


