---
title: JavaWeb
date: 2018-12-20 10:30:43
tags: 
    - Web
categories: 
    - Java
---

**目录 start**
 
1. [Java Web](#java-web)
    1. [JSP/Servlet](#jspservlet)
        1. [Servlet](#servlet)
        1. [JSP](#jsp)
            1. [九大内置对象](#九大内置对象)
            1. [四个作用域](#四个作用域)
        1. [框架](#框架)
        1. [缓存](#缓存)
    1. [Tips](#tips)

**目录 end**|_2019-04-19 15:38_|
****************************************
# Java Web
## JSP/Servlet

### Servlet
### JSP
> [参考博客: JSP面试题及答案](http://www.cnblogs.com/iOS-mt/p/5717631.html)

#### 九大内置对象

| 对象 | 说明 | 类型 | 作用域 |
|:----|:----|:----|:----|
| request     |       请求对象　   |             类型 javax.servlet.ServletRequest    |    作用域 Request
| response    |      响应对象     |              类型 javax.servlet.SrvletResponse   |    作用域  Page
| pageContext |   页面上下文对象     |  类型 javax.servlet.jsp.PageContext |     作用域    Page
| session     |       会话对象    |               类型 javax.servlet.http.HttpSession|       作用域    Session
| application |      应用程序对象   |       类型 javax.servlet.ServletContext          |作用域    Application
| out         |          输出对象 |                  类型 javax.servlet.jsp.JspWriter|             作用域    Page
| config      |        配置对象   |               类型 javax.servlet.ServletConfig   |         作用域    Page
| page        |       页面对象    |              类型 javax.lang.Object              |              作用域    Page
| exception   |     例外对象      |           类型 javax.lang.Throwable              |       作用域    page  

#### 四个作用域
> [参考博客: JSP的四大作用域](http://www.cnblogs.com/featherfly/p/3513656.html)

| 域 | 说明 |
|:----|:----|
| application | 在所有应用程序中有效
| session | 在当前会话中有效
| request | 在当前请求中有效
| page | 在当前页面有效

***********************

### 框架

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

**************************
### 缓存 

_如何做Etag缓存_
1. 自定义了EtagCache注解
2. 通过拦截器判断带EtagCache注解的Controller
3. 通过Spring Data Jpa自带的乐观锁 version, 针对每个资源就可以做到EtagCache
4. 将其值放在http的header中
5. 还有另一种做法就是 自己针对内容进行hash code编码

**************************** 

## Tips
- 1、JSP页面上的SQL标签以及EL标签是优先于文件头的那些JavaServlet语句运行的，所以要保证非法进入页面时重定向的问题
- 2、如果想要获取异常来据此返回参数到页面弹窗提示，那么就要对一层层的方法调用，进行查找，所有的try catch 块 都要检查
    - 因为一般我的习惯就是把异常当场就处理了，而要实现这个要求就必须将异常层层上抛！！！！
* 3、中文乱码问题：
    - **接收**
        - 使用get方法，需要转换成gbk :`newString(s.getBytes("ISO-88511-1","gbk");`
        - post方法需要转换成UTF-8
    - **回应** 均使用UTF-8

*  4、查询数据： 使用set集合，查询对象是否存在，使用contians
*  5、Servlet 是单例多线程的
*  6、**eclipse中将java项目转成web项目**
    *  经常在eclipse中导入web项目时，出现转不了项目类型的问题，导入后就是一个java项目，有过很多次经历，今天也有同事遇到类似问题，就把这个解决方法记下来吧，免得以后再到处去搜索。 
    **解决步骤**： 
  
-  1、进入项目目录，可看到.project文件，打开。 
-  2、找到`<natures>...</natures>`代码段。 
-  3、在第2步的代码段中加入如下标签内容并保存： 
 
``` xml
    <nature>org.eclipse.wst.common.project.facet.core.nature</nature>
    <nature>org.eclipse.wst.common.modulecore.ModuleCoreNature</nature> 
    <nature>org.eclipse.jem.workbench.JavaEMFNature</nature> 

``` 
- 4、在eclipse的项目上点右键，刷新项目。 
- 5、在项目上点右键，进入属性（properties） 
- 6、在左侧列表项目中点击选择“Project Facets”，在右侧选择“Dynamic Web Module”和"Java"，点击OK保存即可。


1. RPC RMI
    - RPC Remote Process Calls 
    - RMI Remote Method Invocation 
