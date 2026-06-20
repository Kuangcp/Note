---
title: SpringAi
date: 2026-02-26 14:45:09
tags: 
categories: 
---

💠

- 1. [Spring Ai](#spring-ai)
    - 1.1. [Tips](#tips)
    - 1.2. [网络](#网络)
- 2. [Spring Ai Alibaba](#spring-ai-alibaba)
    - 2.1. [Structured Output](#structured-output)
    - 2.2. [Workflow](#workflow)
        - 2.2.1. [CheckPoint](#checkpoint)

💠 2026-06-17 19:58:18
****************************************
# Spring Ai

> [Introduction :: Spring AI Reference](https://docs.spring.io/spring-ai/reference/index.html)  


## Tips
- 提示词模板渲染上，SpringAi提供了 PromptTemplate 按 {var} 格式很容易遇到JSON结构而报错，简单平替是 MustachePromptTemplate 使用{{var}}来渲染降低错误概率。
    - 进阶使用 后端模板引擎  Thymeleaf / Freemarker， 或者Jinja2 打通Java和Python。 
        - 例如 医疗问诊工作流的分支极多（多轮、单轮、重症、轻症、科室路由）。强逻辑模板引擎可以在数据库中写出具备“微型编程能力”的超级提示词，将提示词的组装放在提示词自身，能更灵活。
    - 但是！ 当你需要用Ai模型来自动优化提示词时，强大的模板引擎会大大提高对 优化提示词的模型的基准能力： 元认知，代码理解能力，因为模型一旦改错格式渲染就出问题了
    - 所以 Mustache 反而是最适合工程上自动优化的模板。简单直接

## 网络
常见的Agent提供的接口是SSE协议，但是 HTTP/2 Streamable 是 SSE 底层传输协议的“终极增强版”。

好处是兼容性好，但是缺点是 HTTP1.1 的时候浏览器会有默认6TCP连接的限制，一个用户如果开 6 个大模型对话标签页，浏览器就报错或者无响应。
HTTP2 Streamable 能实现TCP连接的多路复用， 支持头部压缩 HPACK， TCP双向全双工（可以做客户端的主动触发）


> 开启 HTTP/2 Streamable

```yaml
server:
  port: 8080
  http2:
    enabled: true # 👈 核心：一键开启 HTTP/2 支持
```

- Spring AI 已经对底层流式协议做了完美封装，你只需要正常返回 Flux，并指定媒体类型为 TEXT_EVENT_STREAM_VALUE（即 SSE）
    - 注：此时只要客户端使用 HTTPS 或支持 HTTP/2 的协议请求该接口，Spring Boot 就会自动将其降维升级为 HTTP/2 Streamable 模式运行。

```java
    @GetMapping(value = "/api/agent/chat", produces = MediaType.TEXT_EVENT_STREAM_VALUE) // 👈 声明为 SSE 流
    public Flux<String> streamChat(@RequestParam String prompt) {
        return this.chatClient.prompt()
                .user(prompt)
                .stream() // 👈 开启 Spring AI 流式调用
                .map(chatResponse -> chatResponse.getResult().getOutput().getContent()); 
                // 过滤出文本 token 实时吐给前端
    }
```

与之对应的就是前端也需要做适配

- 必须全量普及 HTTPS： 所有的主流浏览器（Chrome、Edge、Safari）都遵循一个死规定：只支持基于 TLS（HTTPS）的 HTTP/2。
- 传统 EventSource API 的替换： 浏览器的原生 new EventSource() API 是不支持自定义 Header（如 Authorization: Bearer token）的。适配代价：为了在安全鉴权下使用 HTTP/2 流，前端需要抛弃 EventSource，改用微软开源的 @microsoft/fetch-event-source 库，或者直接使用现代的 fetch 结合 ReadableStream 接收数据。

并且前端到后端的所有中间链路都需要适配： Nginx 应用网关 等。

# Spring Ai Alibaba
> [Spring AI Alibaba](https://java2ai.com/)  

Spring AI 是一个底层的“连接器”，而 Spring AI Alibaba 是一个高层的“操作系统”。 生命周期的Hook Interceptor，MCP，多Agent。


## Structured Output

> [Structured Output Converter :: Spring AI Reference](https://docs.spring.io/spring-ai/reference/api/structured-output-converter.html)  
> [Structured Output 结构化输出 | Spring AI Alibaba](https://java2ai.com/docs/frameworks/agent-framework/tutorials/structured-output#%E9%87%8D%E8%AF%95%E6%A8%A1%E5%BC%8F)  

- 模型 API 级别的参数（如 OpenAI 的 response_format 或 DashScope/Qwen 的 json_object）。模型在采样（Sampling）解码阶段，就被强制限制只能吐出符合 JSON Schema 的 Token，成功率接近 100%。
- 提示词兜底， 如果模型不支持原生接口，框架会自动退回（Fallback）到最原始的方案：将 BeanOutputConverter 动态生成的 Schema 文本通过字符串拼接塞进你的 Prompt 里，然后靠模型自身的“理解力”去硬碰

但是不同的模型有不同的表现，最好是通过 自动化基准探测 来辅助替换模型的决策

## Workflow
框架里的StateGraph与SpringAi原生的Graph类似但不是一个设计和实现，增加了监控和限流等功能。

### CheckPoint
在启动StateGraph时，传入的 RunnableConfig里的 threadId， 对应 com.alibaba.cloud.ai.graph.checkpoint.savers.MemorySaver#_checkpointsByThread的key。
在业务意义上 threadId就是 sessionId，用于SpringAiAlibaba管理实现多轮问答的记忆实现。


