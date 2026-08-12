---
title: LLM
date: 2026-08-13 00:43:50
tags: 
categories: 
---

💠

- 1. [LLM](#llm)
- 2. [一、LLM 原理入门](#一llm-原理入门)
    - 2.1. [核心概念](#核心概念)
- 3. [二、适用场景](#二适用场景)
    - 3.1. [常用范式](#常用范式)
- 4. [三、常见部署 API 对比](#三常见部署-api-对比)
    - 4.1. [关键差异](#关键差异)
    - 4.2. [请求示例对比](#请求示例对比)

💠 2026-08-13 00:58:27
****************************************
# LLM

# 一、LLM 原理入门

LLM（Large Language Model，大语言模型）本质上是一个**预测下一个词**的模型：给定一段文本，模型计算下一个 token（词元）最可能是谁，逐个生成，直到形成完整回复。

## 核心概念

- **Token（词元）**：模型处理文本的最小单位。一个英文单词约 1~2 个 token，一个汉字约 1 个 token。计费和上下文长度都按 token 计算。
- **上下文窗口（Context Window）**：模型一次能"看到"的最大 token 数，决定它能记住多长的对话或文档。
- **训练三阶段**：
  1. **预训练（Pre-training）**：在海量互联网文本上学习"语言规律"，得到一个会接话的基座模型。
  2. **监督微调（SFT）**：用"问题-答案"对训练，让模型学会"对话"和"遵循指令"。
  3. **对齐（RLHF 等）**：用人类偏好反馈调整，让输出更安全、更有帮助。
- **Transformer**：当前主流架构，核心是"注意力机制（Attention）"，让模型能关注到句子中任意位置的关联。

一句话理解

> LLM = 一个在大量文本上学过"语言规律"的巨大神经网络，你给它一段提示词（Prompt），它逐词续写，产出看起来合理的回答。它"懂"的是统计规律，而非真正理解世界。

************************

# 二、适用场景

> 擅长

| 场景 | 说明 |
|------|------|
| 文本生成 | 写作、改写、翻译、总结、邮件、文案 |
| 对话 / 客服 | 聊天机器人、问答助手 |
| 代码生成 | 补全、解释、生成、重构、调试 |
| 信息提取 | 从文档中抽取结构化字段 |
| 分类 / 情感分析 | 对文本打标签 |
| 知识问答（RAG） | 结合检索，回答私有知识库问题 |

> 不擅长 / 需注意

- **精确计算**：算术、统计容易出错，应交给代码/工具。
- **事实准确性**：可能"一本正经地胡说八道"（幻觉），需检索或人工核对。
- **实时信息**：知识截止于训练时间，需联网或 RAG 补充。
- **确定性任务**：同样输入可能得到不同输出，可用 `temperature=0` 降低随机性。
- **长文档**：超出上下文窗口的内容会丢失。

## 常用范式

- **Prompt 工程**：通过提示词引导输出。
- **RAG（检索增强生成）**：先检索相关文档再让模型生成，解决私有知识和幻觉。
- **Function Calling / Tool Use**：让模型调用外部工具（搜索、计算、数据库）。
- **Agent**：模型自主规划、调用工具、多步完成任务。

---

# 三、常见部署 API 对比

市面上主流 LLM API 主要有三类：**OpenAI 系**（含其 Chat Completions 与 Responses 两种接口）、**Anthropic**（Claude）。它们能力相似，但在接口设计、参数和调用方式上存在差异。

> 整体定位

| | OpenAI（Chat Completions） | OpenAI（Responses） | Anthropic（Messages） |
|---|---|---|---|
| 模型 | GPT 系列 | GPT 系列 | Claude 系列 |
| 定位 | 经典对话接口，兼容性最好 | 新一代接口，统一多模态与工具 | 强调长上下文与工具调用 |
| 状态 | 成熟、稳定、生态最广 | 官方推荐的新方向 | 稳定 |

## 关键差异

| 维度 | Chat Completions | Responses | Anthropic |
|------|------------------|-----------|-----------|
| 端点 | `/v1/chat/completions` | `/v1/responses` | `/v1/messages` |
| 角色 | `system` / `user` / `assistant` | 同左，另加 `developer` | `system` / `user` / `assistant` |
| 输入 | `messages` 数组 | `input`（支持字符串、数组） | `messages` 数组 |
| 输出 | `choices[0].message` | `output` 数组（含推理、工具调用等类型） | `content` 数组 |
| 工具调用 | `tools` + `tool_calls` | `tools` + `function_call` | `tools` + `tool_use` |
| 温度参数 | `temperature` | 默认 `temperature=1` | `temperature` |
| 最大输出 | `max_tokens` | `max_output_tokens` | `max_tokens` |
| 思考/推理 | 需特定模型参数 | 内建 `reasoning` 字段 | 内建 `thinking` 块 |
| 流式格式 | SSE `delta` | SSE 事件类型更丰富 | SSE `content_block_delta` |

## 请求示例对比

**Chat Completions**

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "你好"}],
    "max_tokens": 100
  }'
```

**Responses**

```bash
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "input": "你好",
    "max_output_tokens": 100
  }'
```

**Anthropic**

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 100,
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

> 选型建议

- **追求生态兼容 / 已有大量基于 Chat Completions 的代码**：用 Chat Completions。
- **新项目、需要统一多模态 + 工具 + 推理**：优先考虑 Responses（OpenAI 官方新方向）。
- **超长文档、复杂工具调用、代码任务**：Anthropic（Claude）。
- **想平滑切换多家**：用统一封装（如 OpenAI SDK 兼容层、LiteLLM），将三家差异屏蔽在底层。
