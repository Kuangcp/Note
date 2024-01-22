---
title: 机器学习-工程平台
date: 2024-01-20 22:56:10
tags: 
categories: 
---

💠

- 1. [平台](#平台)
    - 1.1. [H2O](#h2o)

💠 2024-01-22 10:38:30
****************************************
# 平台
> 将机器学习工程化组织的平台

## H2O
- [H2O Wave](https://h2o.ai/platform/ai-cloud/make/h2o-wave/) `开源` 基于动态数据实时渲染仪表板WEBAPI服务 Python实现
- [H2O Driverless AI](https://h2o.ai/platform/ai-cloud/make/h2o-driverless-ai/) `商业化` 将ML工程简化，在交互上构建清晰的工作流程

- [H2O-3](https://h2o.ai/platform/ai-cloud/make/h2o/)`开源` 类似于 Jupyter Notebook 的数据开发平台

历史还有H2O-2版本， 14年开始做起 [两个项目Star History 对比](https://star-history.com/#h2oai/h2o-3&h2oai/h2o-2&Date)

> [Github](https://github.com/h2oai/h2o-3) | [Youtube H2Oai](https://www.youtube.com/@H2Oai)

![](./img/h2o-structure.excalidraw.svg)

建模支持的算法
```
    Aggregator
    ANOVA for Generalized Linear Model
    Cox Proportional Hazards
    Deep Learning
    Distributed Random Forest
    Extended Isolation Forest
    Gradient Boosting Machine
    Import MOJO Model
    Generalized Linear Modeling
    Generalized Low Rank Modeling
    Information Diagram
    Isolation Forest
    K-means
    Model Selection
    Naive Bayes
    Principal Components Analysis
    RuleFit
    Stacked Ensemble
    TargetEncoder
    Uplift Distributed Random Forest
    Word2Vec
    XGBoost
```

- 下载压缩包解压运行jar之后，可打开一个默认无认证体系的 [H2O Flow](http://h2o-release.s3.amazonaws.com/h2o/rel-3.44.0/3/docs-website/h2o-docs/flow.html)
- [MOJO](https://docs.h2o.ai/h2o/latest-stable/h2o-docs/mojo-quickstart.html)`模型的抽象表示` 导出为GenModel即jar包可部署到应用中。


- [GLM Tutorial](https://github.com/h2oai/h2o-3/blob/master/h2o-docs/src/product/tutorials/glm/glm.md)
![](./img/h2o-glm.excalidraw.svg)
