---
title: SpringAi
date: 2026-02-26 14:45:09
tags: 
categories: 
---

💠

- 1. [Spring Ai](#spring-ai)
    - 1.1. [Tips](#tips)
    - 1.2. [Spring Ai Alibaba](#spring-ai-alibaba)
        - 1.2.1. [Structured Output](#structured-output)
        - 1.2.2. [Workflow](#workflow)

💠 2026-06-07 23:26:55
****************************************
# Spring Ai

> [Introduction :: Spring AI Reference](https://docs.spring.io/spring-ai/reference/index.html)  


## Tips
- 提示词模板渲染上，SpringAi提供了 PromptTemplate 按 {var} 格式很容易遇到JSON结构而报错，简单平替是 MustachePromptTemplate 使用{{var}}来渲染降低错误概率。
    - 进阶使用 后端模板引擎  Thymeleaf / Freemarker， 或者Jinja2 打通Java和Python。 
        - 例如 医疗问诊工作流的分支极多（多轮、单轮、重症、轻症、科室路由）。强逻辑模板引擎可以在数据库中写出具备“微型编程能力”的超级提示词，将提示词的组装放在提示词自身，能更灵活。
    - 但是！ 当你需要用Ai模型来自动优化提示词时，强大的模板引擎会大大提高对 优化提示词的模型的基准能力： 元认知，代码理解能力，因为模型一旦改错格式渲染就出问题了
    - 所以 Mustache 反而是最适合工程上自动优化的模板。简单直接

## Spring Ai Alibaba
> [Spring AI Alibaba](https://java2ai.com/)  

Spring AI 是一个底层的“连接器”，而 Spring AI Alibaba 是一个高层的“操作系统”。 生命周期的Hook Interceptor，MCP，多Agent。

### Structured Output

> [Structured Output Converter :: Spring AI Reference](https://docs.spring.io/spring-ai/reference/api/structured-output-converter.html)  
> [Structured Output 结构化输出 | Spring AI Alibaba](https://java2ai.com/docs/frameworks/agent-framework/tutorials/structured-output#%E9%87%8D%E8%AF%95%E6%A8%A1%E5%BC%8F)  

- 模型 API 级别的参数（如 OpenAI 的 response_format 或 DashScope/Qwen 的 json_object）。模型在采样（Sampling）解码阶段，就被强制限制只能吐出符合 JSON Schema 的 Token，成功率接近 100%。
- 提示词兜底， 如果模型不支持原生接口，框架会自动退回（Fallback）到最原始的方案：将 BeanOutputConverter 动态生成的 Schema 文本通过字符串拼接塞进你的 Prompt 里，然后靠模型自身的“理解力”去硬碰

但是不同的模型有不同的表现，最好是通过 自动化基准探测 来辅助替换模型的决策

### Workflow
框架里的StateGraph与SpringAi原生的Graph类似但不是一个设计和实现，增加了监控和限流等功能。


