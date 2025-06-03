---
title: Rag
date: 2025-04-30 11:30:51
tags: 
categories: 
---

💠

- 1. [RAG](#rag)
    - 1.1. [Rag 评测](#rag-评测)
    - 1.2. [实践](#实践)

💠 2025-06-03 11:29:27
****************************************
# RAG
> [[Large Language Models with Semantic Search] - 引言與關鍵字搜尋Keyword/lexical Search - HackMD](https://hackmd.io/@YungHuiHsu/rku-vjhZT)  

> [RAG预处理增强：让Fastgpt/Dify召回更多东西 - 53AI-AI知识库|大模型知识库|大模型训练|智能体开发](https://www.53ai.com/news/RAG/2024091558913.html)  
> [FlagOpen/FlagEmbedding: Retrieval and Retrieval-augmented LLMs](https://github.com/FlagOpen/FlagEmbedding)  
> [来自工业界的开源知识库 RAG 项目最全细节对比_开源rag知识库-CSDN博客](https://blog.csdn.net/hustyichi/article/details/140293940)  
> [大模型主流应用RAG的介绍——从架构到技术细节 | 我的学习笔记 | 土猛的员外](https://luxiangdong.com/2023/09/25/ragone/)  

> [如何在不微调的情况下提高 RAG 的准确性？ - 知乎](https://www.zhihu.com/question/638730143)  

> [基于大语言模型知识问答应用落地实践 – 知识库构建（上） | 亚马逊AWS官方博客](https://aws.amazon.com/cn/blogs/china/practice-of-knowledge-question-answering-application-based-on-llm-knowledge-base-construction-part-1/)  


> [InternLM/HuixiangDou: HuixiangDou: Overcoming Group Chat Scenarios with LLM-based Technical Assistance](https://github.com/InternLM/HuixiangDou?tab=readme-ov-file)  


> [基于大语言模型知识问答应用落地实践 – 知识库构建（上） | 亚马逊AWS官方博客](https://aws.amazon.com/cn/blogs/china/practice-of-knowledge-question-answering-application-based-on-llm-knowledge-base-construction-part-1/)  


## Rag 评测
> [RAG 评测调研：框架、指标和方法 | EvalScope](https://evalscope.readthedocs.io/zh-cn/latest/blog/RAG/RAG_Evaluation.html)  

指标：召回率

## 实践

> [如何提升RAG知识库文档的召回准确率？ - 53AI-AI知识库|大模型知识库|大模型训练|智能体开发](https://www.53ai.com/news/RAG/2025031330416.html)  

1. 自然语言 -> embedding 入库
2. 召回内容 -> 拆解，拓展，语义补全 -> 搜索 -> rerank

![alt text](./img/002-rag-map.png)

- RAG之前先做query分类
- chunking方法很重要
- 选择支持混合检索的向量数据库(语义检索+关键词检索)
- 用文档检索文档能提升召回效果
- 文档重排效果显著
- 如果召回量很大，记得先摘要再生成
- 微调时混合相关和无关文档可以提升生成效果

> [RAG最佳实践 - 知乎](https://zhuanlan.zhihu.com/p/5834624096)  
> [Searching for Best Practices in Retrieval-Augmented Generation](https://arxiv.org/pdf/2407.01219)  

[RAG 全流程](https://waytoagi.feishu.cn/wiki/QBssw7z4oiGS40kDlltcjozBnxc)