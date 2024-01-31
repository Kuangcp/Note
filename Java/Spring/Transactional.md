---
title: Spring 事务
date: 2018-12-21 10:54:05
tags: 
    - Spring
categories: 
    - Java
---

💠

- 1. [Spring 事务](#spring-事务)
    - 1.1. [propagation](#propagation)
    - 1.2. [isolation](#isolation)
    - 1.3. [失效场景](#失效场景)
    - 1.4. [异常场景](#异常场景)
    - 1.5. [可编程事务管理](#可编程事务管理)

💠 2024-01-31 11:40:19
****************************************
# Spring 事务
> [Doc: Transaction Management](https://docs.spring.io/spring-framework/docs/5.2.x/spring-framework-reference/data-access.html#spring-data-tier)

## propagation

## isolation

************************

> 事务 和 AOP 同时使用 顺序问题

[Afterreturning 和 Transactional](https://stackoverflow.com/questions/39406242/afterreturning-aspect-executes-in-same-transaction-of-pointcut-method#)

## 失效场景
> [一口气说出 6种，@Transactional注解的失效场景 ](https://juejin.cn/post/6844904096747503629)

1. 数据库引擎不支持事务，例如 MyISAM
1. 注解所在类没有进入IOC容器
1. 注解所在方法没有public修饰， 从反射和代理技术角度是可以实现非public代理，只是在规范上要求public修饰
1. 该方法在当前类被调用，AOP没有生效
1. 数据源没有加载事务管理器
1. propagation 设置不正确: PROPAGATION_SUPPORTS PROPAGATION_NOT_SUPPORTED PROPAGATION_NEVER
1. 异常被catch或者 rollbackFor 指定的类型不匹配（非自身且非子类）且该异常非RuntimeException和Error 子类
    - org.springframework.transaction.interceptor.RuleBasedTransactionAttribute#rollbackOn
    - org.springframework.transaction.interceptor.DefaultTransactionAttribute#rollbackOn

## 异常场景
> 事务内语句 部分未回滚 部分失败

1. 使用 MySQL DML 和 DDL 混合使用 。`PG 支持DDL事务手动管理 MySQL的DDL会使用隐含事务不提供手动管理`

## 可编程事务管理

- TransactionTemplate
- TransactionOperator
- TransactionManager
- ReactiveTransactionManager
