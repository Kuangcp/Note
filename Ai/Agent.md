---
title: Agent
date: 2026-06-07 23:26:55
tags: 
categories: 
---


💠

- 1. [Agent](#agent)
    - 1.1. [工程实践](#工程实践)

💠 2026-06-07 23:26:55
****************************************

# Agent

- 一种分法：Workflow 对比 reAct ，控制权的转移，适用不同场景， 例如 dify对比openclaw。

> [FoundationAgents/MetaGPT: 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming](https://github.com/FoundationAgents/MetaGPT)  


## 工程实践

从“手工、野生、跑通就好”走向“系统性、行业级、工程可控”，核心要解决的是 “确定性、稳定性、扩展性、评测性” 这四大硬伤。

> 一、 架构与设计模式（如何让行为更可控）

* 状态机与图结构（State & Graph）：
* 理解图驱动（Graph-based）的核心逻辑。
   * 深度掌握 LangGraph 或 Spring AI Alibaba 中的 Multi-Agent 状态转移设计。
   * 学习条件路由（Conditional Router）、自循环（Looping）的终止条件判定（防止死循环）。
* 认知模式演进（Cognitive Patterns）：
* 超越简单的 ReAct 模式。
   * 系统学习 Plan-and-Solve（先规划后执行）、Self-Refine / Self-Correction（自我反思与纠错机制）、RAG-Fusion + Agent。
* 多智能体协同模式（Multi-Agent Collaboration）：
* Orchestrator-Workers（中心编排模式）： 适用于复杂分流任务。
   * Choreography / Sequential（流式协同）： 智能体接力赛。
   * Debate / Multi-agent Discussion（辩论模式）： 提高复杂决策的准确率。

> 二、 核心组件与高级技术（如何让边界更清晰）

* 工具与技能管理（Tool & Skill Management）：
* 动态技能注入： 深入研究 [Anthropic 提出的 Skill 标准](https://www.cnblogs.com/imust2008/p/19489542) 及 [Spring AI Alibaba SkillRegistry](https://www.cnblogs.com/jucunqi/p/19812940) 的“渐进式披露”（先注入元数据，按需加载完整的 SKILL.md）。
   * MCP 协议（Model Context Protocol）： 掌握 Anthropic 开放的 MCP 协议，实现标准化的工具/上下文接入。
* 高级上下文与记忆管理（Memory Architecture）：
* 短期记忆： 基于 Window/Token 裁剪的 Buffer Memory。
   * 长期记忆： 实体提取（Entity Extraction）、基于向量数据库的用户画像与事实记忆（User Profile & Facts Base）持久化。
   * 语义压缩： 通过 LLM 自动背景总结（Summarizer），降低长期对话的 Token 成本。
* 工程化 Prompt 资产管理：
* Prompt 的版本控制与热更新。
   * Prompt 与代码逻辑的解耦（Jinja2/Mustache 模板化管理）。

> 三、 生产级工程化落地（如何像传统软件一样稳健）

* 人机协同与安全红线（Human-in-the-Loop）：
* 高危工具调用（如：扣款、删库、发送外部邮件）的人工审批机制（Interrupt & Resume）。
   * 状态回滚（Time-Travel）：支持人工介入后修正历史状态并重新运行。
* 高并发与性能优化（Performance & Scaling）：
* Streaming（流式响应）： 如何在复杂的 Multi-Agent/Workflow 图结构中，平滑地将中间节点及最终节点的 Token 流式透传给前端。
   * 异步队列处理： 长耗时 Agent 任务的线程池隔离、消息队列（Kafka/RocketMQ）削峰。
* 安全与防御（LLM Security）：
* 防 Prompt 注入（Prompt Injection Mitigation）。
   * 敏感词过滤（Guardrails）与输出合规性校验。

> 四、 监控、评测与数据驱动（如何衡量好坏并持续迭代）

* 深度可观测性（Observability - 进阶 Langfuse）：
* Tracing 深度治理： 精确定义 Span、Generation、Event，计算每个节点的精确 Cost（Token 消耗）和 Latency（延迟）。
   * Session 追踪： 将多轮对话与底层复杂图调用的 Tracing 链条完美打通。
* Agent 评测体系（Evaluation）：
* LLM-as-a-Judge： 利用更高级的模型（如 GPT-4o / Qwen-Max）对 Agent 的中间输出、工具选择、最终回答进行自动化打分。
   * 基准测试（RAGas / G-Eval）： 针对特定业务场景搭建黄金数据集（Golden Dataset），每次代码或 Prompt 变更后进行回归测试。
* 数据闭环（Data Flywheel）：
* 收集 Langfuse 中用户踩踩（Thumbs Down）或人工修正的 Bad Case。
   * 将 Bad Case 转化为 RAG 知识、微调（Fine-tuning）数据集或 Few-Shot 示例，形成反哺闭环。



