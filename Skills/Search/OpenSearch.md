---
title: OpenSearch
date: 2026-02-12 17:56:32
tags: 
categories: 
---


💠

- 1. [OpenSearch](#opensearch)
    - 1.1. [RAG选型](#rag选型)

💠 2026-02-12 17:56:32
****************************************
# OpenSearch

> [opensearch-project/OpenSearch: 🔎 Open source distributed and RESTful search engine.](https://github.com/opensearch-project/OpenSearch)  


> [Docker - OpenSearch Documentation](https://docs.opensearch.org/latest/install-and-configure/install-dashboards/docker/)`单实例快速启动`  


## RAG选型

| 维度               | **OpenSearch**                   | **Milvus**       | **ES 8.x**          |
| ---------------- | -------------------------------- | ---------------- | ------------------- |
| **RRF 算法**       | ✅ **原生支持** `hybrid_search` + RRF | ❌ 需自研或外挂         | ⚠️ 8.8+ 支持，但功能弱于 OS |
| **分块（Chunking）** | ✅ **Ingest Pipeline 自动分块**       | ❌ 需外部处理          | ✅ Ingest Pipeline   |
| **向量检索**         | ✅ **k-NN + 磁盘索引（HNSW）**          | ✅ 核心能力（HNSW/IVF） | ✅ k-NN              |
| **文本检索（BM25）**   | ✅ **原生 Lucene**                  | ❌ 无，需外挂          | ✅ 原生                |
| **混合检索（向量+文本）**  | ✅ **一条查询搞定**                     | ⚠️ 需多路召回后融合      | ✅ 但 RRF 弱于 OS       |
| **重排（Rerank）**   | ✅ **LTR + 外部模型**                 | ⚠️ 需自研           | ✅ LTR               |
| **存储成本（200GB）**  | ✅ **磁盘索引，成本低**                   | ⚠️ 内存优先，成本高      | ✅ 磁盘索引              |
| **运维复杂度**        | ✅ **一套系统**                       | ❌ **向量+文本两套系统**  | ✅ 一套系统              |

