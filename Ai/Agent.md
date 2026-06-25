---
title: Agent
date: 2026-06-07 23:26:55
tags: 
categories: 
---

💠

- 1. [Agent](#agent)
    - 1.1. [工程实践](#工程实践)
    - 1.2. [落地框架](#落地框架)
- 2. [方法论](#方法论)
    - 2.1. [Prompt Engineering](#prompt-engineering)
    - 2.2. [Harness Engineering](#harness-engineering)
    - 2.3. [Loop Engineering](#loop-engineering)
- 3. [通信](#通信)
    - 3.1. [MCP](#mcp)
    - 3.2. [A2A](#a2a)
    - 3.3. [ACP](#acp)
- 4. [渲染](#渲染)

💠 2026-06-25 16:47:42
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


## 落地框架
- LangChain 最主流，也有对应语言的移植版本 LangChain4j，
- [SpringAi](/Ai/SpringAi.md)
- AgentScope Java和Python版本
- ADK
- Eino
- [Koog](https://docs.koog.ai/)  

> 落地平台

- Dify
- Coze
- n8n

# 方法论

## Prompt Engineering


## Harness Engineering
> 代表应用： OpenClaw 和 Hermes Agent 


## Loop Engineering


************************


# 通信
应用层：Agent 框架 (如 LangChain / AutoGen) —— 构建智能体大脑和逻辑
      ↓
通信层：A2A / ACP —— 负责 Agent 之间的协作（A2A管跨云，ACP管本地）
      ↓
工具层：MCP —— 负责 Agent 对下调用具体工具、读取文件和上下文
      ↓
模型层：LLM (如 Claude / GPT) —— 提供核心的推理与理解能力

## MCP
> [Introduction - Model Context Protocol](https://modelcontextprotocol.io/introduction)
> [modelcontextprotocol/servers: Model Context Protocol Servers](https://github.com/modelcontextprotocol/servers)  
> [supercorp-ai/supergateway: Run MCP stdio servers over SSE and SSE over stdio. AI gateway.](https://github.com/supercorp-ai/supergateway)  

MCP (Model Context Protocol) —— “Agent ↔ 工具与数据”, 由 Anthropic 提出的通用上下文获取协议

为什么要提出MCP呢, Function Call 不够用吗?
- Function Call 确实能覆盖很多场景，但 MCP 把能力拆成 Tools、Resources、Prompts 三个正交概念，是为了让 AI 和外部系统的协作边界更清晰、更安全、更可维护。
    - Resources 是 AI 的"眼睛"（只读感知），Prompts 是 AI 的"嘴型"（表达范式），Tools 是 AI 的"手"（改变世界）。


> Tools


> Resources 

- 引入了URI 标识 + 订阅/缓存机制，AI 可以只读一次，后续引用 URI 即可。
- 只读承诺：服务器声明"我不会变"，客户端/AI 可以安全缓存
- 订阅机制：资源变化时服务器主动推送，AI 不需要轮询
- URI 即身份：同样的 URI 在不同会话中指向同一逻辑实体

例如

```
URI 方案：
  file:///project/src/main.java     ← 本地文件
  user://profile/preferences          ← 用户配置
  db://postgres/customers/123       ← 数据库记录（只读视图）
  git://repo/HEAD:README.md         ← Git 对象
```

> Prompts

可复用的领域指令模板

- 没有 Prompts 概念时，系统提示词（system prompt）只能通过：客户端硬编码, 或某个 get_prompt_template 的 Tool
- 这导致可复用的领域指令无法被服务端声明和版本化管理。MCP 的 Prompts 让服务器实现例如说："我提供了一套标准的代码审查模板，客户端可以直接用"。

> 三者协作的完整流程

用户：帮我审查这个 PR
AI：

    发现服务器声明了 Prompt: "code_review" → 决定使用
    发现需要参数 {{diff}} → 检查 Resources
    读取 Resource: git://repo/pulls/42.diff
    填充 Prompt 模板，生成完整请求
    审查过程中发现代码调用了外部 API
    读取 Resource: api://service/v1/openapi.json 了解接口规范
    最终建议：这里有个 SQL 注入风险
    用户说：发邮件给作者
    AI 调用 Tool: send_email（触发用户确认）

> 开源工具
- [googleapis/genai-toolbox: MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox)`MCP工具箱操作各种数据库`  

## A2A
ACP (Agent Communication Protocol) —— “Agent ↔ Agent（本地/边缘）”, 由 IBM (BeeAI) 等大厂提出的智能体通信协议

它是局域网内 Agent 通信协议

## ACP
A2A (Agent-to-Agent) —— “Agent ↔ Agent（跨平台/云端）”,  由谷歌等公司推动的跨平台智能体外交协议


# 渲染
> [ag-ui-protocol/ag-ui: AG-UI](https://github.com/ag-ui-protocol/ag-ui)  

智能体和前端渲染之间的协议
