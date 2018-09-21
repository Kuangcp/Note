`目录 start`
 
- [JavaEE](#javaee)
    - [2.【几大框架简述】](#2几大框架简述)
    - [9 【SpringMVC】](#9-springmvc)
        - [9.1 必要JAR包：](#91-必要jar包)
        - [9.2 实现逻辑](#92-实现逻辑)
        - [9.3 controller的配置](#93-controller的配置)
            - [9.3.1类型转换（也可以使用Hibernate的convert）](#931类型转换（也可以使用hibernate的convert）)
                - [SpringMVC的内置代理](#springmvc的内置代理)
                - [Hibernate的covert包](#hibernate的covert包)
            - [Controller层的异常处理（一般处理自定义异常）](#controller层的异常处理（一般处理自定义异常）)
            - [拦截器机制](#拦截器机制)
            - [视图解析](#视图解析)
            - [上传下载](#上传下载)
            - [JSON的解析](#json的解析)
    - [10.【SSH框架的整合】](#10ssh框架的整合)
    - [11.【SSM框架的整合】](#11ssm框架的整合)
    - [12.【Redis的使用】](#12redis的使用)
        - [12.1 【Java 使用 redis 配置】](#121-java-使用-redis-配置)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# JavaEE

*******************
## 2.【几大框架简述】
* MVC设计模式：
    * M
        * hibernarte （相应操作的SQL语句由Hibernate框架生成）
        * mybatis（SQL用户根据需要去写的）
        * JPA 和Hibernate是相同的内核，由Hibernate派生而来
    * C
        * struts1.x
        * struts2.x
        * springmvc  
        * spring  模块的整合
    * V:
        视图层
- **再度理解** Dao service模式的概念
    * dao : 基础单笔业务的功能模块
    * service : 将单个的dao组合一起，得到复杂的业务逻辑
    * 如果要实现AOP或者规范化，dao和service分别要有接口的存在（为了多态，代理，严谨）

## 9 【SpringMVC】
- 一般使用注解方式更方便书写
### 9.1 必要JAR包：
- Spring的核心JAR包
- spring-web-3.2.6.RELEASE.jar
- spring-webmvc-3.2.6.RELEASE.jar
- spring-webmvc-portlet-3.2.6.RELEASE.jar

### 9.2 实现逻辑

- 核心类是DispatchServlet 由它来接收各种请求
- 发出request请求，到controller解析器，得到Model和view等的名字
- 发送到controller执行，返回view名字
- 发送到视图解析器
- 执行视图返回到dispatchServlet

### 9.3 controller的配置
- 类：
   - @Controller
   - @RequestMapping("/WebApplicationRootURL")
- 方法
    - @RequestMapping("/ActionURL")
        - @RequestMapping("/action/{id}") 方法要使用(@PathVariable("id") String id)
    - @ResponseBody 返回对象，自动解析成JSON

#### 9.3.1类型转换（也可以使用Hibernate的convert）

```xml
    <mvc:annotation-driven conversion-service="conversionService" />
    <!--配置ConversionService -->
    <bean id="conversionService"
        class="org.springframework.context.support.ConversionServiceFactoryBean">
        <property name="converters">
            <set>
                <ref bean="DateConverter" />
            </set>
        </property>
    </bean>
```


##### SpringMVC的内置代理

##### Hibernate的covert包

#### Controller层的异常处理（一般处理自定义异常）

```java
    处理所有接收到的的异常
    @ControllerAdvice
    public class ExceptionHandle{
    @EXceptionHandler({Exception.class})
    public ModelAndView dealException(Exception e){
        ModelAndView view = new ModelAndView("exception";
        Exception e = new Exception("错误信息");
        view.addObject("",e.getMessage());
        return view;
    }
    
```

#### 拦截器机制

```xml
    implements HandleInterceptor 有三个方法
    
    preHandle 返回true就继续往后，false就被拦截
    PostHandle 在渲染视图之前，
    afterCompletion 渲染视图之后调用，释放资源
    
    
    配置文件，需要配置：
    ？如果这个路径大于springmvc拦截的路径？
      <mvc:interceptors>
       <mvc:interceptor>
           <bean class=""></bean>
           <mvc:mapping path="/**"/>
       </mvc:interceptor>
```
#### 视图解析
```java
    ModelAndView view = ModelAndView("index"); 
    使用这种写法是进入配置好的视图解析器，进行路径的拼接然后转发
    ModelAndView("redirect:/l/login.jsp");
    就是使用重定向方式，注意路径要写全，因为不会拼接
 ```
 
 
#### 上传下载
jar包：
- common-upload
- common-io

---
配置文件

---

#### JSON的解析
- 第三方的JSON工具包：
    - jsonlib
    - jackson ： 三个包 annotion core databind
    - gson

- 发送JSON
    - 只要有返回值，方法前加上这个注解就会自动返回JSON格式的数据而不是对象
    - @responseBody
    - @ReqeustMapping("")
- 接收JSON 
    - 参数前 也加上@equestBody 就可以把JSON数据转成对象

********************

## 10.【SSH框架的整合】


## 11.【SSM框架的整合】


## 12.【Redis的使用】

### 12.1 【Java 使用 redis 配置】
> [Java使用Redis](/Database/Redis.md#Java使用Redis)