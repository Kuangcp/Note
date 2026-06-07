---
title: Prompt
date: 2025-04-30 11:30:51
tags: 
categories: 
---

💠

- 1. [Prompt](#prompt)
    - 1.1. [最佳实践-原则](#最佳实践-原则)
    - 1.2. [自动优化](#自动优化)

💠 2026-06-08 00:25:30
****************************************
# Prompt

> [Text generation and prompting - OpenAI API](https://platform.openai.com/docs/guides/text?api-mode=responses)  
> [[GenAI][RAG] Prompt Engineering for Multimodal Model - HackMD](https://hackmd.io/@YungHuiHsu/rJzaU3LSC)  


在工程学中，Prompt 已经不再是“写小作文”，而是被视为一种“弱类型、概率性的底层代码”。编写它需要遵循类似于软件工程的严谨设计模式。

总结几个典型信号，如果你中招了，说明自动化优化必须提上日程：

输出不一致：改了一个字，模型反应像换了脑子；
调试耗时：找一个问题 Prompt，排查几个小时甚至几天；
上线节奏慢：每次调试都得打全套回归，版本频繁卡在 Prompt 上；
幻觉问题反复出现：哪怕数据完美，还是输出离谱。

这些现象都是系统性问题，不靠“勤奋”能解决，只能靠工程手段破局。


[Promptfoo](https://promptfoo.org.cn/)`提示词的安全和评估平台`  


## 最佳实践-原则
> 架构设计规则：单一职责与解耦

* 规则：一个 Prompt 节点只做一件事（如：只做分类、只做参数提取、或只做风格润色）。
* 反例：在同一个 Prompt 里让模型“先判断用户意图，如果意图是 A 就提取订单号，如果意图是 B 就拒绝，并且最后输出要用 JSON”。这种“全能 Prompt”极易在修复 A 规则时导致 B 规则失效。
* 正例：拆分成两个 Workflow 节点。节点 1 纯做意图分类（Router），节点 2 纯做数据提取（Extractor）。

但是这里有一个trade off， 如果节点拆的很细，多个模型环节的串行执行会导致用户的 TTFT 延长。


> 上下文隔离原则 (Context Separation)

* 规则：严格区分 “指令（Instructions）”、“业务上下文/知识（Context）” 和 “用户输入（Input Data）”。
* 工程手段：使用明确的 XML 标签（如 <instruction>、<context>、<user_input>）进行包裹。大模型对 XML 标签的结构感知力远强于 Markdown 或纯文本，这能有效防止用户输入污染（Prompt Injection）导致工作流崩溃。

> 负向约束的“熔断机制” (Negative Constraints & Safety Rails)

* 规则：大模型“擅长做加法，不擅长做减法”。当你要求“不要做什么”时，必须同时给出“如果不做，应该返回什么特定的兜底信号”。
* 反例：如果找不到订单，不要瞎编。（模型仍可能幻觉）
* 正例：如果从文本中无法提取到完整的 12 位订单号，必须立刻中断并仅输出：{"error": "ORDER_NOT_FOUND"}。绝对允许输出任何其他解释性文本。


> Few-Shot 样本的“正态分布”原则 (Balanced Few-Shot)

* 规则：当你通过 Few-Shot（少样本）来修复 Bad Case 时，正例和负例的比例要平衡（最好 1:1 或 2:1）。
* 打地鼠根源：你修复了 A case，往 Prompt 里塞了一个 A 的正确示例，模型就会产生“过拟合（Overfitting）”，导致接下来的判断都疯狂往 A 的特征上靠，从而引发了 B case 报错。
* 工程解法：引入一个 A 的正例，就要同时引入一个类似特征的负例。

> 结构化输出协议 (Structured Output Protocol)

* 规则：生产环境的 Workflow 节点间传递，一律强制要求返回 JSON/YAML，并配合 JSON Schema。
* 工程手段：
* 在 Prompt 尾部声明：Output absolute valid JSON matching the schema below.。
   * 利用大模型厂商提供的原生功能（如 Open AI 的 Structured Outputs，或 Qwen 的 Function Calling/JSON Mode），从底层阻断“模型话痨（输出多余的‘好的，这是为您生成的 JSON...’）”导致的解析异常。


> 基于语义版本号的 Prompt 资产管理 (Prompt Versioning)

* 规则：Prompt 必须像 Maven 依赖或 Git 代码一样拥有独立的语义版本号（Semantic Versioning, 如 v1.1.0）。
* 规范：
* 补丁号 (v1.0.1)：微调了某个形容词或加了一个 Few-Shot，不改变输出结构。
   * 次版本号 (v1.1.0)：增加了一个新的判断维度，输出的 JSON 字段变多了。
   * 主版本号 (v2.0.0)：底座模型更换（如从 Qwen-Plus 换到 Qwen-Max），Prompt 重构。


> 黄金测试集的一票否决制 (Regression Testing)

* 规则：任何针对 Prompt 的修改，在未通过回归测试集（Regression Dataset）前，研发可见，生产不可见。
* 工程指标：每次为了修 Bad Case 改动 Prompt 后，必须自动化跑一遍测试集。设定硬性指标：当前 Bad Case 解决率 = 100%，历史 Golden Case 跌落率（Regression Rate）= 0%。只要历史 Case 挂了一个，这次修改直接作废。



```markdown
    # Role
    你是一个专职于后端错误日志分类与根因分析（RCA）的 AIOps 专家机器人。

    # Task
    分析用户输入的后端错误日志，将其归类并给出置信度。

    # Categories
    - DB_ERROR: 数据库连接失败、SQL语法错误、连接池耗尽、锁超时等。
    - NETWORK_ERROR: 网络超时、连接被拒、DNS解析失败、第三方API不可达（注：原NETWORK_TIMEOUT扩大为此项）。
    - AUTH_FAIL: 密码错误、Token过期、签名验证失败、权限不足。
    - CODE_EXCEPTION: 空指针、类型转换错误、业务逻辑异常、内存溢出（新增：减少UNKNOWN的概率）。
    - UNKNOWN: 无法识别、日志信息不足或属于其他未定义类型。

    # Rules
    1. 只能从 [DB_ERROR, NETWORK_ERROR, AUTH_FAIL, CODE_EXCEPTION, UNKNOWN] 中选择一个类别。
    2. 根因交叉原则：如果日志同时包含数据库和网络错误，且网络错误是由数据库连接引起的（如 DB Connection Refused），以底层数据库错误（DB_ERROR）为准。
    3. 严格限制：输出必须是合法、完整的标准 JSON 字符串，严禁包含任何 Markdown 标记（如 ```json）、换行符或解释性文字。

    # Output Format
    {
    "category": "string",
    "reason": "string (用简短、客观的一句话说明判断依据)",
    "confidence": "float (0.00-1.00，保留两位小数)"
    }

    # Examples
    Input: Connection refused to mysql://localhost:3306
    Output: {"category": "DB_ERROR", "reason": "Failed to connect to MySQL database instance.", "confidence": 0.98}

    Input: Connection refused to https://stripe.com
    Output: {"category": "NETWORK_ERROR", "reason": "External API endpoint is unreachable.", "confidence": 0.95}

    Input: java.lang.NullPointerException at com.user.Service.getUser(Service.java:45)
    Output: {"category": "CODE_EXCEPTION", "reason": "Null pointer exception detected in application code.", "confidence": 1.00}
```

## 自动优化
自动提示词工程优化 Automatic Prompt Engineering

> [MetaGPT/examples/spo at main · FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT/tree/main/examples/spo)  

> [如何让 AI 来自己优化提示词 - mdnice 墨滴](https://mdnice.com/writing/e68752daa49a48b7ac9e388a49d9b8bf)  
> [Self-Supervised Prompt Optimization](https://arxiv.org/pdf/2502.06855)  

大致流程是： 建立黄金测试集，结合生产监控的低分数据 自动化评测，模型自动优化 前后版本评估对比，选择最终提示词版本

１.种子输入：仅需提供初始提示词和少量测试问题（无需标注答案）。
２.优化阶段：AI根据当前最优提示生成改进版
３.测试阶段：用新旧提示分别生成两版输出
４.评估阶段：AI自动比较两版输出，选出更优结果对应的提示
５.优选保留：获胜的提示成为下一轮优化的基准
６.循环迭代：达到预设迭代次数或性能稳定时停止


