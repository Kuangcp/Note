---
title: Voice
date: 2025-03-29 12:06:38
tags: 
categories: 
---


💠

- 1. [语音大模型](#语音大模型)

💠 2025-03-29 12:06:38
****************************************
# 语音大模型
> [语音大模型概述（持续更新中2025.03） - 知乎](https://zhuanlan.zhihu.com/p/14831605089)  

1. 级联方案 (Cascade) — 目前最成熟

- ASR → LLM → TTS 三段式，如 GPT-4o Voice Mode、Gemini Live
- 优点：每段独立优化，效果好且可控
- 缺点：延迟高，丢失副语言信息（语调、情感、停顿）

2. 语音离散化 + LLM — 主流探索方向

- 用 audio tokenizer（如 EnCodec、SpeechTokenizer、HuBERT）将语音压成离散 token
- 然后像文本 token 一样塞进 LLM 做 next token prediction
- 代表：Moshi (Kyutai)、GLM-4-Voice、Llama-Omni
- 优点：复用 LLM 架构和训练基础设施
- 缺点：离散化有信息损失，音质受限

3. 全连续表示 (Continuous) — 前沿

- 不经过离散化，直接在连续空间建模，如 GPT-4o Advanced Voice（用 diffusion/flow matching 生成音频）、Seed-TTS (
ByteDance)
- 优点：音质最高，表达力最强
- 缺点：训练和推理成本极高

4. Streaming / 实时方案

- 关键是 输入流式编码 + 输出流式合成，支持打断 (barge-in)
- 核心技术：streaming audio encoder、chunked decoding、early exit

## 数字人
