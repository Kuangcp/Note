# Ai
> [liguodongiot/llm-action: 本项目旨在分享大模型相关技术原理以及实战经验（大模型工程化、大模型应用落地）](https://github.com/liguodongiot/llm-action)  

## 工程化演进

1. Prompt Engineering（提示工程）—— 2022-2023
这是最早期的工程化形态，核心是把 AI 当做一个黑盒函数，通过精心设计的输入来影响输出。

    核心关注点：措辞技巧、Few-shot 示例、Chain-of-Thought、角色设定
    局限：高度依赖模型版本，脆弱性强，难以规模化维护
    本质：人与模型的单轮/多轮对话调优

2. Context Engineering（上下文工程）—— 2023-2024
随着长上下文窗口的突破（128K、1M tokens），人们意识到"给模型看什么"比"怎么问"更重要。

    核心关注点：
        RAG（检索增强生成）：从外部知识库动态注入相关上下文
        上下文压缩与筛选：在有限窗口内放入最有价值的信息
        记忆机制：短期对话历史 vs 长期知识库的分离管理
    标志性转变：从"写更好的 prompt"转向"构建更好的上下文管道"
    本质：信息检索与组装系统的工程化

3. Agent Engineering / Harness Engineering（智能体/框架工程）—— 2024-2025
当单轮调用无法满足复杂任务时，AI 工程化进入工作流编排阶段。

    核心关注点：
        工具调用（Tool Use）：让模型能使用外部 API、代码解释器、数据库
        多 Agent 协作：规划者（Planner）→ 执行者（Executor）→ 验证者（Verifier）的分工
        控制流与状态机：循环、条件分支、错误回退、人工介入点
        评估与观测（Evals & Observability）：不是每次都能成功，需要监控和度量
    代表框架：LangChain、LlamaIndex、AutoGen、CrewAI、Dify、Coze 等
    本质：把 AI 当作分布式系统中的智能节点来编排



# Local Ai
> [The 6 Best LLM Tools To Run Models Locally](https://getstream.io/blog/best-local-llm-tools/)  

> [Docs | LocalAI documentation](https://localai.io/docs/)  

## Ollama
> [Ollama](https://ollama.com/)  
> [ollama/ollama](https://github.com/ollama/ollama/tree/main)  

可以像Docker一样一层层自定义模型

# Java生态
LangChain4j 和 Spring AI 
