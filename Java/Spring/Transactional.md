---
title: Spring 事务
date: 2018-12-21 10:54:05
tags: 
    - Spring
categories: 
    - Java
---

**目录 start**

1. [Spring 事务](#spring-事务)
    1. [失效场景](#失效场景)
    1. [可编程事务管理](#可编程事务管理)

**目录 end**|_2021-04-22 21:33_|
****************************************
# Spring 事务
> [Doc: Transaction Management](https://docs.spring.io/spring-framework/docs/5.2.x/spring-framework-reference/data-access.html#spring-data-tier)

************************

> 事务 和 AOP 同时使用 顺序问题

[Afterreturning 和 Transactional](https://stackoverflow.com/questions/39406242/afterreturning-aspect-executes-in-same-transaction-of-pointcut-method#)

## 失效场景

1. 引擎不支持事务，例如 MyISAM
1. 注解所在类没有进入IOC容器
1. 注解所在方法没有public修饰， 从反射和代理角度是可以实现的，只是规范上应该要public
1. 该方法在当前类被调用，AOP没有生效
1. 数据源没有加载事务管理器
1. propagation 设置不正确
1. 异常被catch或者rollback指定的类型不对应

## 可编程事务管理

- TransactionTemplate
- TransactionOperator
- TransactionManager
- ReactiveTransactionManager
