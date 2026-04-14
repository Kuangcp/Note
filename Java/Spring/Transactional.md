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

💠 2026-01-16 16:14:52
****************************************
# Spring 事务
> [Doc: Transaction Management](https://docs.spring.io/spring-framework/docs/5.2.x/spring-framework-reference/data-access.html#spring-data-tier)

## propagation

**事务传播行为**：定义方法在已有事务中的行为

| 传播行为 | 说明 | 使用场景 |
|---------|------|---------|
| **REQUIRED**（默认） | 如果存在事务则加入，否则创建新事务 | 最常用，适合大多数场景 |
| **REQUIRES_NEW** | 总是创建新事务，挂起当前事务 | 需要独立事务，不受外层影响 |
| **SUPPORTS** | 如果存在事务则加入，否则非事务执行 | 可选事务，不影响调用方 |
| **NOT_SUPPORTED** | 非事务执行，挂起当前事务 | 不需要事务的方法 |
| **MANDATORY** | 必须在事务中，否则抛异常 | 强制要求事务 |
| **NEVER** | 必须在非事务中，否则抛异常 | 禁止事务 |
| **NESTED** | 嵌套事务，外层回滚会影响内层 | 需要保存点的嵌套场景 |

**示例：**
```java
@Transactional(propagation = Propagation.REQUIRED)  // 默认
public void methodA() {
    methodB();  // 加入A的事务
}

@Transactional(propagation = Propagation.REQUIRES_NEW)
public void methodB() {
    // 创建新事务，A的事务被挂起
    // B提交后，A继续执行
}
```

## isolation

**事务隔离级别**：控制事务间的数据可见性

| 隔离级别 | 脏读 | 不可重复读 | 幻读 | 说明 |
|---------|:---:|:--------:|:---:|------|
| **READ_UNCOMMITTED** | ✅ | ✅ | ✅ | 最低级别，性能最好但数据不安全 |
| **READ_COMMITTED**（Oracle默认） | ❌ | ✅ | ✅ | 避免脏读，但可能出现不可重复读 |
| **REPEATABLE_READ**（MySQL默认） | ❌ | ❌ | ✅ | 避免脏读和不可重复读 |
| **SERIALIZABLE** | ❌ | ❌ | ❌ | 最高级别，完全隔离但性能最差 |

**示例：**
```java
@Transactional(isolation = Isolation.READ_COMMITTED)
public void updateUser() {
    // 只能读取已提交的数据
}

@Transactional(isolation = Isolation.REPEATABLE_READ)
public void queryUser() {
    // 同一事务内多次读取结果一致
}
```

**注意：**
- Spring的隔离级别是对数据库隔离级别的抽象
- 实际隔离级别取决于数据库支持（MySQL InnoDB支持所有级别）
- 隔离级别越高，性能开销越大

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

1. 一个事务内 DML 和 DDL 混合使用，  MySQL5.6以下 和 PG8.0以下
    - MySQL： 5.6 以后 InnoDB支持
    - Pg： 8.0 之后（引入保存点、MVCC 成熟）

## 可编程事务管理

- TransactionTemplate
- TransactionOperator
- TransactionManager
- ReactiveTransactionManager
