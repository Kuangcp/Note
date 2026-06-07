---
title: AgentObservability
date: 2026-06-08 00:25:30
tags: 
categories: 
---


💠

- 1. [Agent 观测](#agent-观测)
    - 1.1. [Langsmith](#langsmith)
    - 1.2. [Langfuse](#langfuse)
    - 1.3. [Opik](#opik)
    - 1.4. [Phoenix](#phoenix)
    - 1.5. [Laminar](#laminar)
    - 1.6. [Helicone](#helicone)

💠 2026-06-08 00:25:30
****************************************
# Agent 观测

开源选择： Langfuse，Opik， Phoenix

如果想要完善的更高的数据量的分析系统，采用Langfuse，如果早期阶段，使用 Phoenix 会更简单。  
但是，即使都是基于OTel协议接入，但是为了适配对应的监控系统的UI数据展示，都会需要一些特定的tag适配（点名Langfuse），所以都是有对接成本的，并不是无缝切换观测系统

## Langsmith
> [LangSmith: AI Agent & LLM Observability and Evals Platform](https://www.langchain.com/langsmith-platform)  

LangChain 生态最佳搭配， 但是只有商业版本

## Langfuse
> [langfuse/langfuse](https://github.com/langfuse/langfuse)  

- 功能： 提示词管理，监控，评估评测，Playground
- 架构： TypeScript Next.js， ZK+CK，MinIO，PG，Redis, Langfuse Worker和Web

支撑每天数百万级 Trace 的高并发场景

## Opik
> [Quickstart | Opik Documentation | Opik Documentation](https://www.comet.com/docs/opik/quickstart/?from=llm&utm_source=opik&utm_medium=github&utm_content=quickstart_link&utm_campaign=opik)  
> [comet-ml/opik](https://github.com/comet-ml/opik)  

- 功能： 监控，自动化大模型评测 适合CI/CD
- 架构： 相较于Langfuse 采用 Java，ZK+CK，MinIO，Redis，MySQL，Jaeger。


## Phoenix
> [Phoenix - Arize AI](https://arize.com/phoenix/)  

- 功能： 
- 架构： Python， Pg

## Laminar 
> [Laminar - Open-source observability for AI agents](https://laminar.sh/)  

只支持 TypeScript Python 生态

## Helicone
> [Helicone / AI Gateway & LLM Observability](https://www.helicone.ai/)  

