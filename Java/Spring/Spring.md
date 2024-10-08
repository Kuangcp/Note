---
title: Spring
date: 2018-12-21 10:46:01
tags: 
    - Spring
categories: 
    - Java
---

💠

- 1. [Spring](#spring)
    - 1.1. [配置使用](#配置使用)
        - 1.1.1. [通过构建工具](#通过构建工具)
        - 1.1.2. [注解方式](#注解方式)
            - 1.1.2.1. [xml文件配置](#xml文件配置)
            - 1.1.2.2. [常用的注解](#常用的注解)
        - 1.1.3. [xml方式](#xml方式)
            - 1.1.3.1. [xml方式和注解方式的比较](#xml方式和注解方式的比较)
    - 1.2. [Spring技巧](#spring技巧)
        - 1.2.1. [获取Context上下文环境](#获取context上下文环境)
            - 1.2.1.1. [在JSP或Servlet中获取](#在jsp或servlet中获取)
        - 1.2.2. [Spring 和 ServletContextList](#spring-和-servletcontextlist)
- 2. [基础](#基础)
    - 2.1. [Bean概述](#bean概述)
        - 2.1.1. [Bean生命周期](#bean生命周期)
        - 2.1.2. [Bean的作用域](#bean的作用域)
    - 2.2. [容器的扩展点](#容器的扩展点)
        - 2.2.1. [Aware](#aware)
        - 2.2.2. [BeanPostProcessor](#beanpostprocessor)
        - 2.2.3. [BeanFactoryPostProcessor](#beanfactorypostprocessor)
    - 2.3. [IOC/DI 控制反转](#iocdi-控制反转)
        - 2.3.1. [循环依赖](#循环依赖)
    - 2.4. [Application Context](#application-context)
    - 2.5. [Scheduling](#scheduling)
    - 2.6. [Events](#events)
    - 2.7. [异步](#异步)
    - 2.8. [RestTemplate](#resttemplate)
    - 2.9. [Utils](#utils)
        - 2.9.1. [ReflectionUtils](#reflectionutils)
    - 2.10. [SpEL](#spel)
- 3. [Web开发的最佳实践](#web开发的最佳实践)
    - 3.1. [优雅部署](#优雅部署)
- 4. [Tips](#tips)

💠 2024-10-08 16:06:24
****************************************
# Spring
> [Spring官网](https://spring.io/) | [spring4all社区](http://www.spring4all.com/)

> [Spring For All 社区 ->  Spring 官方教程翻译](http://www.spring4all.com/article/558)

> [Spring Tutorial](https://www.tutorialspoint.com/spring/index.htm)

## 配置使用
> **通过原始的复制jar方式 :** 官网下载对应的jar, 添加到ide中
### 通过构建工具
Maven 中 pom.xml 中, Gradle是 build.gradle 添加以下等依赖:

_核心依赖_
1. spring-core
1. spring-beans
1. spring-context

_其他,可选_
1. spring-aop
1. spring-websocket
1. spring-jdbc 
1. spring-tx 
1. spring-web
1. spring-webmvc
1. spring-test

### 注解方式
> 需要在配置文件 xml配置文件 中配置包扫描 才能生效

#### xml文件配置
```xml
    <!-- 头部分要添加Context -->
    <?xml version="1.0" encoding="UTF-8"?>
    <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:context="http://www.springframework.org/schema/context"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
             http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
             http://www.springframework.org/schema/context
             http://www.springframework.org/schema/context/spring-context-3.0.xsd">
        <!-- 对使用了注解的包进行扫描 -->
        <context:component-scan base-package="com.github.kuangcp"></context:component-scan>
    </beans>
```
> **注意** 只需要这个配置文件就可以使用注解来使用Spring框架

#### 常用的注解
- 标注为bean
    - `@Component([value=]"id") `不写则默认是当前类名
    - @Entity
    - @Service
    - @Repository
    - @Controller 和 @RestController

- 自动注入
    - `@Resource([value=]"id")` 按名字注入
    - `@Autowried` 根据类型自动注入（只对单例起作用）和 `Resource(类名首字母小写)` 等价
        - 通过阅读源码还可以知道 可以将符合条件的Bean注入到 List 和 Map 中去, 甚至 Optional
    - `@Qualifier("id") `自动注入后的进一步精确（多个Bean的情况）
        - 如果同类型的Bean有明显的主次关系（或者说缺省值），可以在Bean的声明时加上 `@Primary` 注解，那就可以省去`Qualifier`的使用

- **注意 :** 关于自动注入, 在属性上打 @Autowried 注解是不建议的, 作者建议采用构造器方式:  [Why field injection is evil](http://olivergierke.de/2013/11/why-field-injection-is-evil/)
    - 如果使用了 lombok 那么可以在类上使用 
        - `@RequiredArgsConstructor(onConstructor = @__(@Autowired))`
        - 然后注入的属性打上 `@NonNull` 注解
        - 本质上是帮你自动生成了一个将所有 `@NonNull` 注解属性作为参数的构造器

- AOP
    - @Aspect 注明是切面类
    - @Before("execution(public void com.wjt276.dao.impl.UserDaoImpl.save(com.wjt276.model.User))") 和xml方式的before对应

- bean扫描
    - ComponentScan 扫描指定包下Spring注解的类

> [参考: Why field injection is evil](http://olivergierke.de/2013/11/why-field-injection-is-evil/)
***********************
###  xml方式
- 只用到bean的头，主要配置内容：`<bean><property></property></bean>`

```xml
    <!-- 对使用了注解的包进行扫描 -->
	<context:component-scan base-package="cn.spring.aop"></context:component-scan>
       <!-- 一般而言，bean都是单实例的 -->
    <bean id="person" class="cn.spring.entity.Person"> 
        <property name="name" value="myth"/>
        <property name="addr" value="vol"/>
    </bean>
    <bean id="construct" class="cn.spring.entity.ConstructorEntity">
    <!-- 如果是不同的类型的参数 顺序可以随意，但是数据类型一样的话就要严格按顺序了-->
    <constructor-arg type="java.lang.String" value="String_1"></constructor-arg>
        <!-- 注意引用类型是要写全路径，基本数据类型是可以直接写小写 -->
    <constructor-arg type="int" value="2"></constructor-arg>
        <!-- <constructor-arg type="java.lang.String" value="String_2"></constructor-arg> -->
    </bean>
    <bean id="TestConstruct" class="cn.spring.entity.TestConstruct">
        <property name="entity" ref="construct"></property>
    </bean>
    <!-- 加载属性文件 -->
    <bean id="property_config" class="org.springframework.beans.factory.config.PreferencesPlaceholderConfigurer">
        <property name="locations">
            <list>
                <value>cn/spring/entity/db.properties</value>
            </list>
        </property>
    </bean>
    <!-- 测试获取属性文件 -->
    <bean id="show_db" class="cn.spring.entity.TestProperties">
        <!-- 特别注意大小写问题 -->
        <property name="driver" value="${driver}"/>
        <property name="username" value="${username}"/>
        <property name="password" value="${password}"/>
        <property name="url" value="${url}"/>
    </bean>
```

#### xml方式和注解方式的比较

- 当你确定切面是实现一个给定需求的最佳方法时，你如何选择是使用Spring AOP还是AspectJ，以及选择 Aspect语言（代码）风格、@AspectJ声明风格或XML风格？
- 这个决定会受到多个因素的影响，包括应用的需求、 开发工具和小组对AOP的精通程度。
- **个人理解**：使用bean的时候使用注解，AOP使用xml方式，更直观

**************

##  Spring技巧
### 获取Context上下文环境
#### 在JSP或Servlet中获取
```java
    ApplicationContext context = WebApplicationContextUtils.getWebApplicationContext(config.getServletContext());
```
### Spring 和 ServletContextList
- 想要启动Tomcat之后，初始化运行一些方法，把数据从数据库拿出放入redis中，然后使用了ServletContextListener
    - 然后还是按照往常一样的使用Spring自动注入的便利，来使用service层获取数据，但是忽略了启动顺序
    - **context-param -> listener -> filter -> servlet**
    - 所以在启动这个初始化方法的时候，其实Spring的环境是还没有加载的，所以没有扫描，也就没有了自动注入，也就有了空指针异常
    - 所以要使用如下方法得到Spring的Context（上下文），获取bean，再操作
  
```java
    public void contextInitialized(ServletContextEvent event) { 
        ApplicationContext context = WebApplicationContextUtils.getWebApplicationContext(event.getServletContext());
        //....
    }
``` 

****************

# 基础

## Bean概述

在容器内bean的定义包含以下信息:

-   `包限定的类名`：通常定义ben的实现类
-   `bean的行为元素`:包含bean的范围、生命周期等
-   `依赖项`：该bean所引用的依赖项
-   `设置其他属性配置`：如配置连接池bean中使用的连接数等

### Bean生命周期
-   初始化(当一个bean配置和了多个生命周期时，执行顺序如下顺序)
    -   在方法上使用`@PostConstruct`注解(推荐使用，同xml中的`init-method`属性一致)
    -   实现接口`InitializingBean`，在方法`afterPropertiesSet()`中可进行bean的初始化操作(在容器设置完bean的必须属性后执行，不建议使用接口，推荐使用注解或xml配置)
    -   在bean的xml配置中在`<beans>`标签上使用类似于属性`default-init-method="init"`的配置后,在beans下配置的bean会在初始化时调用bean中定义的方法名为`init`的方法
    -   实现接口`BeanPostProcessor`中的`postProcessBeforeInitialization`及`postProcessAfterInitialization`方法。该接口会处理他可以找到的所有回调接口    

-   销毁(当一个bean配置和了多个生命周期时，执行顺序如下顺序)
    -   在方法上使用`@PreDestroy`注解(同上，及与xml配置中的`destroy-method`属性一致)
    -   实现接口`DisposableBean`,在方法`destroy()`中，可进行bean的销毁时的操作
    -   在bean的xml配置中在`<beans>`标签上使用类似于属性`default-destroy-method="destroy"`的配置后,在beans下配置的bean会在销毁时调用bean中定义的方法名为`destroy`的方法
    
-   关闭与启动
    -   实现接口`Lifecycle`
    
-   在非Web应用中关闭spring IOC容器
    -   调用`ConfigurableApplicationContext`中的`registerShutdownHook()`方法，这样便就能调用销毁的回调函数
    
-   为Bean提供`ApplicationContext`实例
    -   实现`ApplicationContextAware`,则就可以为该bean实例获取`ApplicationContext`
    
-   让Bean获取自身在BeanFactory中的名称(id或name)
    -   实现`BeanNameAware`接口中,则咎可以获取名称(该方法在初始化之前)

### Bean的作用域

在Spring2.0之前spring中bean的作用域只有`singleton（单例）`及`prototype（原型）`两种。
在Spring2.0后便又增加了`request`、`session`及`application`三种作用域，且这三种作用域都只用于基于web的Spring ApplicationContext。
直到现在，Spring又增加了作用与`webSocket`的作用域，该作用域与2.0之后增加的三种作用域一样都只作用与基于web的Spring ApplicationContext。

- `singleton`: 该作用域是Spring bean默认的作用域；使用该作用域时，在Spring IOC容器中只会存在一个共享的bean实例。所有的对该bean的请求（如通过注入或getBean方法获取实例）都只会获取同一个实例。针对于该作用域，Spring容器可进行比较全面的生命周期的管理
- `prototype`: 使用该作用域时，所有对于该bean的请求都会返回一个新的实例，即每次请求，都会创建一个新的实例
- `request`: 该作用域将bean的作用范围限定在单个HTTP请求中，即每次HTTP请求都会创建一个新的bean实例，是的每次HTTP请求都有一个自己的实例。该作用域只用于基于web的Spring ApplicationContext。
- `session`: 该作用域将bean的作用范围限定在HTTP请求中的Session的生命周期内。即bean的生命周期与Session一致，当Session存活时，该bean的实例也存活，但当Session销毁时，该Session内的bean实例也将被销毁。适合于基于web的Spring ApplicationContext
- `application`: 使用该作用域时，在整个web程序中，只会存在一个该bean的实例。如果只存在一个web应用，则该bean的作用域与`singleton`类似。适合于基于web的Spring ApplicationContext。
- `websocket`： 该作用域是Spring新增的作用域，该作用域将该bean实例作用范围限定在一个生命周期的WebSocket中。适合于基于web的Spring ApplicationContext。


## 容器的扩展点

### Aware
在Spring容器中，提供了许多Aware接口，使用这些接口可以更好的对bean进行扩展，获取许多与容器相关的组件；今天，我们大概来看看Spring中提供的一些Aware接口：  
`BeanNameAware`: 该接口只有一个`setBeanName`方法，如果Spring容器检测到bean实现了该接口，则会将该bean实例的beanName属性注入到该实例中。  
- `ApplicationContextAware`: 该接口只有个`setApplicationContext`方法；如果Spring容器检测到bean实现了该接口，则会将Spring的ApplicationContext注入到bean实例中。  
    - 但一般不建议通过实现该接口获取容器ApplicationContext，因为通过实现接口的方式会增加代码的耦合度，如果希望获取ApplicationContext实例，可以使用一般的注入方式，如使用注解`@Autowired`,这样便就可以获取ApplicationContext，如：  
    ```java
        @Autowired
        private ApplicationContext applicationContext;
    ```
- `BeanClassLoaderAware`: 该接口有个`setBeanClassLoader`方法，与前两个接口类似，实现了该接口后，可以向bean中注入加载该bean的ClassLoader
- `BeanFactoryAware`: 该接口有个`setBeanFactory`方法，用来将当前的beanFactory注入到该bean实例中
- `ApplicationEventPublisherAware`: ApplicationContext事件机制是观察者设计模式的实现，通过ApplicationEvent类和ApplicationListener接口，可以实现ApplicationContext的事件处理。
    - 其中`ApplicationEvent`为容器事件。实现接口`ApplicationEventPublisherAware`的bean可获取`ApplicationEventPublisher`实例(因为ApplicationContext已实现接口`ApplicationEventPublisher`接口，所以其实此处默认还是注入了`ApplicationContext`实例)，用于发布事件
-  `MessageSourceAware`: 实现该接口可，可获取`MessageSource`实例，该实例用于解析消息的策略接口,支持该类消息的参数化与国际化(因为ApplicationContext已实现接口`MessageSource`接口，所以其实此处默认还是注入了`ApplicationContext`实例)
-   `NotificationPublisherAware`: 实现该接口的bean，可获取JMX通知发布者
-   `ResourceLoaderAware`: 可获取Spring中配置的加载程序(ResourceLoader)，用于对资源进行访问；可用于访问类l类路径或文件资源
-   `ServletConfigAware`: 该接口仅在wen应用中有效，用于获取ServletConfig
-   `ServletContextAware`: 该接口仅在wen应用中有效，用于获取ServletContext
-   `LoadTimeWeaverAware`: 可获取`LoadTimeWeaver`实例，用于在加载时处理类定义

### BeanPostProcessor

在Spring中。我们可以定义bean的初始化方法，从而完成某些初始化动作。

可查看源码中对该接口 BeanPostProcessor 的注释定义

> 工厂钩子，允许自定义修改新的bean实例，例如 检查标记接口或用代理包装它们。  
> ApplicationContexts可以在其bean定义中自动检测 BeanPostProcessor bean，并将它们应用于随后创建的任何bean。bean factories允许对后处理器进行编程注册，适用于通过该工厂创建的所有bean。

简单来说，就是我们可以在Spring创建bean实例后，bean初始化之前和初始化之后完成一些自定义的操作。

顾名思义，这两个方法，一个是在bean初始化之前执行，一个是在bean初始化之后执行。 
-   `postProcessBeforeInitialization`
-   `postProcessAfterInitialization`

假如有个定义好的Student，现在希望在不改变原有代码的情况下将它的address字段赋上某个值。

Student
```java
    @Component
    @Data
    public class Student {
        private int id;
        private String name;
        private String address;
    }
```

扩展
```java
    @Component
    public class StudentExpansion implements BeanPostProcessor {
        @Override
        public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
            return bean;
        }
        @Override
        public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
            if (bean instanceof Student) {
                Student student = (Student) bean;
                student.setAddress("中国");
            }
            return bean;
        }
    }
```

### BeanFactoryPostProcessor
和 BeanPostProcessor 类似，都是Spring用于初始化Bean的扩展点，但是 `BeanFactoryPostProcessor`的执行时间是在Spring容器对bean进行实例化之前，而`BeanPostProcessor`则是在Spring容器对bean进行实例化之后的初始化环节。   

`BeanFactoryPostProcessor`允许对bean的定义(配置的元数据)进行修改。例如我们常见的下列配置：

```xml
    <!--加载配置文件-->
    <context:property-placeholder        location="classpath:jdbc.properties"/>

    <!--配置c3p0连接池-->
    <bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
        <property name="driverClass" value="${jdbc.driver}"/>
        <property name="jdbcUrl" value="${jdbc.url}"/>
        <property name="user" value="${jdbc.user}"/>
        <property name="password" value="${jdbc.password}"/>
    </bean>
```

在以上对于数据库的配置中，我们引用了配置文件`jdbc.properties`中的值
```ini
    jdbc.driver = com.mysql.jdbc.Driver
    jdbc.url = jdbc:mysql:///BookManager
    jdbc.user = root
    jdbc.password =123
```

那么问题来了，在Spring将bean实例化时是如何将配置元数据中的`${jdbc.driver}`替换成真实的`com.mysql.jdbc.Driver`的呢？
- 这便就是`BeanFactoryPostProcessor`在Spring容器中的最典型的使用场景之一。
- 该处理的实现类为`PropertyPlaceholderConfigurer`，它实现了接口`BeanFactoryPostProcessor`中的`postProcessBeanFactory`方法， 
- 负责在bean实例化之前将配置元数据中的如同`${jdbc.driver}`的配置替换为它真实的值，然后Spring便就可以正常的实例化了。  

-   在`PropertyPlaceholderConfigurer`中`postProcessBeanFactory`方法的实现如下：

```java
    /**
    * {@linkplain #mergeProperties Merge}, {@linkplain #convertProperties convert} and
    * {@linkplain #processProperties process} properties against the given bean factory.
    * @throws BeanInitializationException if any properties cannot be loaded
    */
    @Override
    public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
        try {
            // 读取配置中配置的properties文件
            Properties mergedProps = mergeProperties();

            // Convert the merged properties, if necessary.
            convertProperties(mergedProps);

            // Let the subclass process the properties.
            processProperties(beanFactory, mergedProps);
        }
        catch (IOException ex) {
            throw new BeanInitializationException("Could not load properties", ex);
        }
    }
```

-   其中`processProperties`方法在`PropertyPlaceholderConfigurer`中的实现为

```java
    /**
    * Visit each bean definition in the given bean factory and attempt to replace ${...} property
    * placeholders with values from the given properties.
    */
    @Override
    protected void processProperties(ConfigurableListableBeanFactory beanFactoryToProcess, Properties props)
            throws BeansException {

        StringValueResolver valueResolver = new PlaceholderResolvingStringValueResolver(props);
        doProcessProperties(beanFactoryToProcess, valueResolver);
    }
```

************************

##  IOC/DI 控制反转
- DI 译为依赖注入 所有的bean都在IOC容器中（单例的）多例的不在该容器中进行管理
- 通过注入 可以注入基本属性 对象属性，集合属性，构造器，properties等
- 不采用Spring的IOC容器使用Java基础来实现：
   - **静态代理** 
       - 针对每个具体类分别编写代理类
       - 针对一个接口编写一个代理类
   - **动态代理**
       - 针对一个方面编写一个InvocationHandler，然后借用JDK反射包中的Proxy类为各种接口动态生成相应的代理类 

属性上 @Autowired 即可, 但是现在不建议直接在属性上使用注解, 而是建议用在构造器上, 这是为了避免NPE: 当使用new实例化时, 里面本该注入的属性会为null

`使用Lombok简化该方式`
```java
    @Component
    @RequiredArgsConstructor(onConstructor = @__(@Autowired))
    public class A{
        @NonNull
        private B b;
    }
```

### 循环依赖
- [Spring循环依赖](https://cloud.tencent.com/developer/article/1769948) 

************************

## Application Context 
> [Spring Application Context Events](https://www.baeldung.com/spring-context-events) `通过监听Context的事件感知Spring上下文的启动和关闭`

*****************
## Scheduling
> [Official Doc](https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/integration.html#scheduling)

> [参考: The @Scheduled Annotation in Spring](https://www.baeldung.com/spring-scheduled-tasks)  
> [参考: Spring Scheduler的使用与坑](http://qinghua.github.io/spring-scheduler/)
> [参考: [Spring]支持注解的Spring调度器](https://www.cnblogs.com/jingmoxukong/p/5825806.html#%E5%AE%8C%E6%95%B4%E8%8C%83%E4%BE%8B)
> [参考: spring scheduled的动态线程池调度和任务进度的监控](https://blog.csdn.net/yyx1025988443/article/details/78698046)

其主体是 TaskExecutor 和 TaskScheduler 组成的, 也就是调度和执行

- [cron maker](http://www.cronmaker.com/)

************************

## Events
> [Spring Events](https://www.baeldung.com/spring-events)

> [Synchronous and Asynchronous Spring Events in One Application](https://www.keyup.eu/en/blog/101-synchronous-and-asynchronous-spring-events-in-one-application)  
> [@EventListener with @Async in Spring](https://stackoverflow.com/questions/37179426/eventlistener-with-async-in-spring)

> [参考: spring线程池(同步、异步）](http://www.cnblogs.com/duanxz/p/9435343.html)

## 异步
> 需要启动类或配置类上标注 @EnableAsync

应用层面在方法上加上@Async就可以快速将普通方法转为异步方法。

但是便利就表示处理是通用的，实际业务场景多变的情况下就容易出问题了。
- 线程池问题： 默认使用Spring声明的
- 任务通信问题： 

************************

## RestTemplate
> [大文件OOM问题](https://github.com/spring-projects/spring-framework/issues/12564) 发送文件时将文件的字节全部读取到内存中再发送，文件大且多时容易OOM

## Utils
### ReflectionUtils


## SpEL
> [Spring5.5 SpEL](https://docs.spring.io/spring-integration/docs/5.5.11/reference/html/spel.html)  

****************

# Web开发的最佳实践

- 使用AOP来简化开发MVC的代码
- 繁杂的代码如何简化

## 优雅部署
> 如何在用户影响最小的情况下，实现服务的升级部署

> [Spring环境中正确关闭线程池的姿势](https://blog.csdn.net/qq271859852/article/details/107442161)

需要解决的问题：
- A 后端服务不可用，需要等新进程启动完后才能恢复服务
- B 用户有感知到请求失败或无响应，请求超时，但是等几个请求后又会恢复正常
- C 业务线程池里执行中的线程被中断，业务在任意的环节上中断，数据不一致
- D 可能导致流量倾斜导致其他节点负载飙升，甚至引起雪崩效应（节点一个接一个down掉）
- E 用户请求分发到未启动完全或未初始化业务逻辑的节点上

> 简单实现
1. 宿主机部署，Nginx 代理到 多个Java进程，手动逐个进程 kill和启动
2. 解决的问题： A 

> 初步方案
1. 采用K8S部署，svc下分发到多个pod，pod配置存活和就绪探针，滚动升级（启动新的就绪容器后才销毁已有旧容器）
2. 解决的问题： A D E 

> 优化方案
1. 除了K8S配置外，应用本身增加 shutdownHook 线程对资源进行回收和限制
2. 或者使用Spring的生命周期管理，监听 ContextClosedEvent 事件，对线程池，缓存等等，业务系统上需要等待执行或者销毁的数据。
3. 解决的问题： A C D E

> 网关
1. 基于以上配置外， 引入 [Gateway](/Skills/Ecology/Gateway.md#功能) 
    - 进入销毁周期的服务器会从网关的反向代理列表中移除，新请求不会进入该服务器
1. 解决的问题： ABCDE

************************

# Tips
- 不要对有 @Configuration 注解的配置类进行 Field 级的依赖注入 否则容易引发循环依赖 [Spring循环依赖问题分析](https://blog.mythsman.com/post/5d838c7c2db8a452e9b7082c/)

如果有两个maven模块， A依赖B 假如 A和B中有相同 package 的同名类 a b，此时A模块是main入口模块，配置了对应package注解扫描
- [ ] 此时会是a还是b，将注册到IOC容器内
