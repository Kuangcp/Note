---
title: Spring AOP
date: 2018-12-21 10:49:23
tags: 
    - AOP
    - Spring
categories: 
    - Java
---

**目录 start**

1. [AOP](#aop)
    1. [动态代理](#动态代理)
    1. [基本概念](#基本概念)
    1. [基本配置](#基本配置)
    1. [注意](#注意)
        1. [1 Spring AOP还是完全用AspectJ？](#1-spring-aop还是完全用aspectj)
        1. [2 Spring AOP中使用@AspectJ还是XML？](#2-spring-aop中使用@aspectj还是xml)
        1. [3 混合切面类型](#3-混合切面类型)

**目录 end**|_2020-08-26 18:31_|
****************************************
# AOP
> Aspect Oriented Programming  面向切面编程

## 动态代理
> 这是AOP的起源, 最初是JDK的动态Proxy -> cglib/asm 

> [笔记: Java中的代理](/Java/AdvancedLearning/JavaProxy.md)

## 基本概念
| 英文 | 解释 |
|:----|:----|
|`JoinPoint`|切入面、连接点、切入点（所有方法） |
|`PointCut` |切点（特殊的连接点，需要增强的连接点）|
|`Advice`|增强（切入点的逻辑，待添加的功能）|
|`Aspect`|切面（切点和增强的合集）|
|`Target`|目标对象（被增强的实例）|
|`Weave`|织入（增强切点的过程）|
|`Proxy`|代理（增强后的类，一般是使用了代理类） 装饰器模式|
|`Introduction`|引介（为类添加属性和方法） 用的较少因为破坏了OOP思想|


1. 多个 AOP 时，切面可实现 Ordered 接口 自定义 AOP 顺序

*********************
##  基本配置
`XML文件头`
```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xmlns:aop="http://www.springframework.org/schema/aop"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context-3.0.xsd
        http://www.springframework.org/schema/aop
        http://www.springframework.org/schema/aop/spring-aop-3.0.xsd">
        </beans>
```
- 方法级别的添加代理，Servlet中的过滤器也类似（但是那个是类级别的）

```xml
<!-- 基本类 提供切点 -->
<bean id="student" class="cn.spring.aop.Student"></bean>
<!-- 增强部分 -->
<bean id="adder" class="cn.spring.aop.NewDeal"></bean>
<!-- 使用aop的自动提示也要配置上面的头文件声明 -->
<aop:config>
    <!--aspect表示切面 ref 标明增强方法的类来源 -->
    <aop:aspect id="myAop" ref="adder">
        <!-- execution 是表达式（正则一样的功能）匹配的是具体的切点 -->
        <aop:pointcut expression="execution(* cn.spring.aop.Student.run(..))" id="needAdd"/>
        <!-- 织入 的过程 将增强和切入点结合 -->
        <aop:before method="add" pointcut-ref="needAdd"/>
        <aop:after method="af" pointcut-ref="needAdd"/>
        <aop:around method="around" pointcut-ref="needAdd"/>
    </aop:aspect>
</aop:config>
```

## 注意
- 要注意环绕的写法 `public void around(ProceedingJoinPoint m)throws Throwable{`  
    - [Spring AOP中的around](https://www.oschina.net/code/snippet_246557_9205)  

- 然后在test类中直接getBean（基类）但是实际上是获取到的是装饰好的代理对象  
    - [Spring AOP配置(转)](http://blog.csdn.net/yuqinying112/article/details/7335416)  
    - [aop:config详解](http://www.cnblogs.com/yangy608/archive/2010/11/14/1876833.html)  

- 善用debug 调试看是否获取到的是代理对象 $proxy

-  在Spring的配置文件中，所有的切面和通知器都必须定义在` <aop:config>` 元素内部。 一个`application context`可以包含多个 `<aop:config>`。 一个` <aop:config>` 可以包含 `pointcut`， `advisor` 和 `aspect` 元素（注意它们必须按照这样的顺序进行声明）。 

### 1 Spring AOP还是完全用AspectJ？
做能起作用的最简单的事。Spring AOP比完全使用AspectJ更加简单，因为它不需要引入AspectJ的编译器／织入器到你开发和构建过程中。 
如果你仅仅需要在Spring bean上通知执行操作，那么Spring AOP是合适的选择。如果你需要通知domain对象或其它没有在Spring容器中 
管理的任意对象，那么你需要使用AspectJ。如果你想通知除了简单的方法执行之外的连接点（如：调用连接点、字段get或set的连接点等等）， 
也需要使用AspectJ。
当使用AspectJ时，你可以选择使用AspectJ语言（也称为“代码风格”）或@AspectJ注解风格。 
如果切面在你的设计中扮演一个很大的角色，并且你能在Eclipse中使用AspectJ Development Tools (AJDT)， 那么首选AspectJ语言 :- 
因为该语言专门被设计用来编写切面，所以会更清晰、更简单。如果你没有使用 
Eclipse，或者在你的应用中只有很少的切面并没有作为一个主要的角色，你或许应该考虑使用@AspectJ风格 
并在你的IDE中附加一个普通的Java编辑器，并且在你的构建脚本中增加切面织入（链接）的段落。

### 2 Spring AOP中使用@AspectJ还是XML？

如果你选择使用Spring AOP，那么你可以选择@AspectJ或者XML风格。总的来说，如果你使用Java 5， 我们建议使用@AspectJ风格。
显然如果你不是运行在Java 5上，XML风格是最佳选择。XML和@AspectJ 之间权衡的细节将在下面进行讨论。
XML风格对现有的Spring用户来说更加习惯。它可以使用在任何Java级别中（参考连接点表达式内部的命名连接点，虽然它也需要Java 5）
并且通过纯粹的POJO来支持。当使用AOP作为工具来配置企业服务时（一个好的例子是当你认为连接点表达式是你的配置中的一部分时， 
你可能想单独更改它）XML会是一个很好的选择。对于XML风格，从你的配置中可以清晰的表明在系统中存在那些切面。
XML风格有两个缺点。第一是它不能完全将需求实现的地方封装到一个位置。DRY原则中说系统中的每一项知识都必须具有单一、无歧义、权威的表示。 
当使用XML风格时，如何实现一个需求的知识被分割到支撑类的声明中以及XML配置文件中。当使用@AspectJ风格时就只有一个单独的模块 -切面- 
信息被封装了起来。 第二是XML风格同@AspectJ风格所能表达的内容相比有更多的限制：仅仅支持"singleton"切面实例模型，并且不能在XML中组合命名连接点的声
明。 例如，在@AspectJ风格中我们可以编写如下的内容：

```java
   @Pointcut(execution(* get*())) 
   public void propertyAccess() {} 
   @Pointcut(execution(org.xyz.Account+ *(..)) 
   public void operationReturningAnAccount() {} 
   @Pointcut(propertyAccess() && operationReturningAnAccount()) 
   public void accountPropertyAccess() {}
```
在XML风格中能声明开头的两个连接点：

```xml
  <aop:pointcut id="propertyAccess" expression="execution(* get*())"/> 
  <aop:pointcut id="operationReturningAnAccount"  expression="execution(org.xyz.Account+ *(..))"/>
```
但是不能通过组合这些来定义accountPropertyAccess连接点
- @AspectJ风格支持其它的实例模型以及更丰富的连接点组合。它具有将将切面保持为一个模块单元的优点。 还有一个优点就是@AspectJ切面能被Spring AOP和AspectJ两者都理解 
- 所以如果稍后你认为你需要AspectJ 的能力去实现附加的需求，那么你非常容易转移到基于AspectJ的途径。总而言之，我们更喜欢@AspectJ风格只要你有切面 去做超出简单的“配置”企业服务之外的事情。

### 3 混合切面类型
我们完全可以混合使用以下几种风格的切面定义：使用自动代理的@AspectJ 风格的切面，`schema-defined <aop:aspect>` 的切面，
和用 `<aop:advisor>` 声明的advisor，甚至是使用Spring 1.2风格的代理和拦截器。
由于以上几种风格的切面定义的都使用了相同的底层机制，因此可以很好的共存。
