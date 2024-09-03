---
title: DataOrchestration
date: 2024-04-17 15:18:45
tags: 
categories: 
---

💠

- 1. [数据协作](#数据协作)
    - 1.1. [DolphinScheduler](#dolphinscheduler)
    - 1.2. [Argo](#argo)
    - 1.3. [Airflow](#airflow)
- 2. [其他](#其他)
    - 2.1. [Azkaban](#azkaban)
    - 2.2. [nifi](#nifi)

💠 2024-09-03 14:05:18
****************************************
# 数据协作
> [What is Data Orchestration & Why It’s Essential for Analysis](https://segment.com/resources/data-strategy/what-is-data-orchestration/)

## DolphinScheduler
> [Github](https://github.com/apache/dolphinscheduler)  
> [Youtube](https://www.youtube.com/@apachedolphinscheduler)  

DolphinScheduler 是国内易观数据公司在2018年开源，2019年进入Apache项目的分布式调度工具,

思考：Job实例的执行交由K8S，避免Worker出现资源瓶颈，甚至去掉Worker只保留master，实例执行全部用K8S

## Argo
> [Github](https://github.com/argoproj/argo-workflows)

云原生工作流引擎

## Airflow
> [Github](https://github.com/apache/airflow)  

强代码实现的工作流引擎

************************

# 其他
## Azkaban
> [Github](https://github.com/azkaban/azkaban)  

主要用于管理Hadoop工作流程

## nifi
> [Github](https://github.com/apache/nifi)  

处理和分发数据, 组件也只针对数据处理，功能比较单一
