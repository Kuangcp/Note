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
- 5. [Tips](#tips)

💠 2026-08-13 01:13:35
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

- **Transformer**：当前主流架构，核心是"注意力机制（Attention）"。
    - **Attention 的本质**：把每个 token 映射成三组向量——**Query（查询）**、**Key（键）**、**Value（值）**。生成某个位置的输出时，用它的 Query 与所有位置的 Key 算相似度（点积 → softmax）得到注意力权重，再对所有 Value 加权求和。一句话：**决定"当下这一步，该重点看上下文里哪些位置"**。
    - **为什么重要**：RNN 等旧结构靠顺序传递，信息在长距离上会衰减；Attention 让任意两个位置直接建立联系、且可并行计算，是模型能"记住"长上下文、捕捉语义关联的基础。
    - **多头注意力（Multi-Head）**：同时用多组 QKV，让不同"头"分别关注不同侧面（一个头盯"发烧"、一个头盯"多久"），最后拼接起来。
    - **复制/归纳头（Induction / Copy Head）——重复提问的根源**：训练中模型会自发学会一些"复制型"注意力头。
        - 当上下文里刚出现一段高相关文本（比如医生刚问"请问发烧多少度、发烧多久了"），下一步生成时注意力会强烈集中到这段文本上，直接原样复述。
        - 因为在"接一个医生追问"这个任务里，那句刚问过的话恰好是最高概率的续写——既在主题上吻合、又是逐字复制，是一条低熵（高置信）的捷径。

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

---

# Tips

> 一些实用又有趣的小技巧与冷知识。

- **随机数指纹**：让模型反复输出一个 1~10000 的随机数，采样几百次画分布，会发现不同模型偏好各异——有的偏爱整百、有的回避极值、有的分布更均匀。这个"粗糙的分布指纹"甚至能用来大致判断一个匿名模型是哪家训出来的。
- **先让它"想"再答**：在指令里加"一步一步思考、先给理由再下结论"，能显著提升数学/推理题的准确率（CoT 的简化版）。代价是多消耗 token，且现在不少模型已默认开启思考，需要时再显式关闭。
- **要求纯 JSON**：需要结构化结果时，加一句"只输出 JSON，不要任何解释、不要代码块"，下游解析会省心很多。
- **few-shot 比长指令更稳**：给 2~3 个"输入 → 输出"示例，往往比写一大段规则文字更能压住模型行为，尤其对格式类任务。
- **自我校验**：追问"再检查一遍你的回答，有没有错误？"，能抓到一部分低级错误和幻觉（但别全信，它有时也会嘴硬）。
- **`temperature=0` 也不绝对确定**：同 prompt 仍可能因服务端实现、浮点差异产生微小波动，别把 0 当成完全可复现。
- **警惕 prompt 注入**：用户输入里可能夹带"忽略之前的指令"，永远别把用户内容当系统指令执行；医疗、客服等场景要显式隔离并做过滤。
- **让模型先复述任务**：复杂指令先让模型"先复述一遍你的理解再执行"，能显著降低漏条件、会错意的概率。
- **"不知道就说不知道"**：加这句话能压住一部分幻觉，但治标不治本，事实性问题仍要靠 RAG/检索兜底。
- **换模型先测 tokenizer**：不同模型的 tokenizer 不同，同一段中文的 token 数可能差很多，直接影响成本与上下文占用，迁移前先拿真实语料测一遍。
