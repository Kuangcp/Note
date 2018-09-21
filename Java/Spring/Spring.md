`目录 start`
 
- [Spring](#spring)
    - [配置使用](#配置使用)
        - [通过构建工具](#通过构建工具)
        - [注解方式](#注解方式)
            - [xml文件配置](#xml文件配置)
            - [常用的注解](#常用的注解)
        - [xml方式](#xml方式)
            - [xml方式和注解方式的比较](#xml方式和注解方式的比较)
    - [Spring技巧](#spring技巧)
        - [获取Context上下文环境](#获取context上下文环境)
            - [在JSP或Servlet中获取](#在jsp或servlet中获取)
        - [Spring 和 ServletContextList](#spring-和-servletcontextlist)
- [基础](#基础)
    - [生命周期](#生命周期)
    - [IOC/DI 控制反转](#iocdi-控制反转)
    - [AOP](#aop)
        - [基本概念](#基本概念)
        - [基本配置](#基本配置)
        - [注意](#注意)
            - [1 Spring AOP还是完全用AspectJ？](#1-spring-aop还是完全用aspectj)
            - [2 Spring AOP中使用@AspectJ还是XML？](#2-spring-aop中使用@aspectj还是xml)
            - [3 混合切面类型](#3-混合切面类型)
    - [Scheduling](#scheduling)
    - [Websocket](#websocket)
        - [maven配置](#maven配置)
    - [Web开发上的一些优秀的习惯](#web开发上的一些优秀的习惯)

`目录 end` |_2018-09-10_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
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
    - `@Qualifier("id") `自动注入后的进一步精确（多个的情况：）
- **注意 :** 关于自动注入, 在属性上打 @Autowried 注解是不建议的, 作者建议采用构造器方式:  [Why field injection is evil](http://olivergierke.de/2013/11/why-field-injection-is-evil/)

- AOP
    - @Aspect 注明是切面类
    - @Before("execution(public void com.wjt276.dao.impl.UserDaoImpl.save(com.wjt276.model.User))") 和xml方式的before对应

- bean扫描
    - ComponentScan 扫描指定包下Spring注解的类

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

# 基础
## 生命周期
@PreDestroy
@PostConstruct

- [ ] 完善

##  IOC/DI 控制反转
- DI 译为依赖注入 所有的bean都在IOC容器中（单例的）多例的不在该容器中进行管理
- 通过注入 可以注入基本属性 对象属性，集合属性，构造器，properties等
- 不采用Spring的IOC容器使用Java基础来实现：
   - **静态代理** 
       - 针对每个具体类分别编写代理类
       - 针对一个接口编写一个代理类
   - **动态代理**
       - 针对一个方面编写一个InvocationHandler，然后借用JDK反射包中的Proxy类为各种接口动态生成相应的代理类 

属性上 @Autowired 即可, 但是现在不建议直接在属性上使用注解, 而是建议在构造器上, 为了避免 手动使用new 实例化Bean, 然后里面本该注入的属性全部为null
可以用lombok来协助
```java
@Component
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
public class A{
  @NonNull
  private B b;
  }
```
**********************
## AOP
> Aspect Oriented Programming  面向切面编程

### 基本概念
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

*********************
###  基本配置
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
### 注意
- 要注意环绕的写法 `public void around(ProceedingJoinPoint m)throws Throwable{`  
    - [Spring AOP中的around](https://www.oschina.net/code/snippet_246557_9205)  

- 然后在test类中直接getBean（基类）但是实际上是获取到的是装饰好的代理对象  
    - [Spring AOP配置(转)](http://blog.csdn.net/yuqinying112/article/details/7335416)  
    - [aop:config详解](http://www.cnblogs.com/yangy608/archive/2010/11/14/1876833.html)  

- 善用debug 调试看是否获取到的是代理对象 $proxy

-  在Spring的配置文件中，所有的切面和通知器都必须定义在` <aop:config>` 元素内部。 一个`application context`可以包含多个 `<aop:config>`。 一个` <aop:config>` 可以包含 `pointcut`， `advisor` 和 `aspect` 元素（注意它们必须按照这样的顺序进行声明）。 

#### 1 Spring AOP还是完全用AspectJ？
做能起作用的最简单的事。Spring AOP比完全使用AspectJ更加简单，因为它不需要引入AspectJ的编译器／织入器到你开发和构建过程中。 
如果你仅仅需要在Spring bean上通知执行操作，那么Spring AOP是合适的选择。如果你需要通知domain对象或其它没有在Spring容器中 
管理的任意对象，那么你需要使用AspectJ。如果你想通知除了简单的方法执行之外的连接点（如：调用连接点、字段get或set的连接点等等）， 
也需要使用AspectJ。
当使用AspectJ时，你可以选择使用AspectJ语言（也称为“代码风格”）或@AspectJ注解风格。 
如果切面在你的设计中扮演一个很大的角色，并且你能在Eclipse中使用AspectJ Development Tools (AJDT)， 那么首选AspectJ语言 :- 
因为该语言专门被设计用来编写切面，所以会更清晰、更简单。如果你没有使用 
Eclipse，或者在你的应用中只有很少的切面并没有作为一个主要的角色，你或许应该考虑使用@AspectJ风格 
并在你的IDE中附加一个普通的Java编辑器，并且在你的构建脚本中增加切面织入（链接）的段落。

#### 2 Spring AOP中使用@AspectJ还是XML？

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

#### 3 混合切面类型
我们完全可以混合使用以下几种风格的切面定义：使用自动代理的@AspectJ 风格的切面，`schema-defined <aop:aspect>` 的切面，
和用 `<aop:advisor>` 声明的advisor，甚至是使用Spring 1.2风格的代理和拦截器。
由于以上几种风格的切面定义的都使用了相同的底层机制，因此可以很好的共存。

*****************
## Scheduling
> [Official Doc](https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/integration.html#scheduling)

> [参考博客: The @Scheduled Annotation in Spring](https://www.baeldung.com/spring-scheduled-tasks)  
> [参考博客: Spring Scheduler的使用与坑](http://qinghua.github.io/spring-scheduler/)
> [参考博客: [Spring]支持注解的Spring调度器](https://www.cnblogs.com/jingmoxukong/p/5825806.html#%E5%AE%8C%E6%95%B4%E8%8C%83%E4%BE%8B)
> [参考博客: spring scheduled的动态线程池调度和任务进度的监控](https://blog.csdn.net/yyx1025988443/article/details/78698046)

其主体是 TaskExecutor 和 TaskScheduler 组成的, 也就是调度和执行

- [cron maker](http://www.cronmaker.com/)
- []()
*******************
## Websocket
### maven配置

```xml
  <dependency>
     <groupId>org.springframework</groupId>
     <artifactId>spring-websocket</artifactId>
     <version>${spring.version}</version>
   </dependency>
   <dependency>
     <groupId>org.springframework</groupId>
     <artifactId>spring-messaging</artifactId>
     <version>${spring.version}</version>
   </dependency>
```
- [ ] Spring方式, 现在用boot用多了, 都忘了怎么配置Spring了

****************
## Web开发上的一些优秀的习惯
- 使用AOP来简化开发MVC的代码
- 繁杂的代码如何简化
