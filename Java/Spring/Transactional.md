---
title: Spring的事务
date: 2018-12-21 10:54:05
tags: 
    - Spring
categories: 
    - Java
---

**目录 start**

1. [Spring 事务](#spring-事务)
    1. [可编程事务管理](#可编程事务管理)

**目录 end**|_2020-08-25 16:11_|
****************************************
# Spring 事务
> [Doc: Transaction Management](https://docs.spring.io/spring-framework/docs/5.2.x/spring-framework-reference/data-access.html#spring-data-tier)

************************

> 事务 和 AOP 同时使用 顺序问题

[Afterreturning 和 Transactional](https://stackoverflow.com/questions/39406242/afterreturning-aspect-executes-in-same-transaction-of-pointcut-method#)

## 可编程事务管理

- TransactionTemplate
- TransactionOperator
- TransactionManager
- ReactiveTransactionManager
