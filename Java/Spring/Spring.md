`目录 start`
 
1. [Spring](#spring)
    1. [配置使用](#配置使用)
        1. [通过构建工具](#通过构建工具)
        1. [注解方式](#注解方式)
            1. [xml文件配置](#xml文件配置)
            1. [常用的注解](#常用的注解)
        1. [xml方式](#xml方式)
            1. [xml方式和注解方式的比较](#xml方式和注解方式的比较)
    1. [Spring技巧](#spring技巧)
        1. [获取Context上下文环境](#获取context上下文环境)
            1. [在JSP或Servlet中获取](#在jsp或servlet中获取)
        1. [Spring 和 ServletContextList](#spring-和-servletcontextlist)
1. [基础](#基础)
    1. [生命周期](#生命周期)
    1. [IOC/DI 控制反转](#iocdi-控制反转)
    1. [Scheduling](#scheduling)
    1. [Websocket](#websocket)
        1. [maven配置](#maven配置)
    1. [Web开发上的一些优秀的习惯](#web开发上的一些优秀的习惯)

`目录 end` |_2018-11-25_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
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

> [参考博客: Why field injection is evil](http://olivergierke.de/2013/11/why-field-injection-is-evil/)
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

- [ ] look up 方法注入

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
