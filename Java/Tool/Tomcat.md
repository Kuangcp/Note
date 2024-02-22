---
title: Tomcat
date: 2018-12-20 10:26:32
tags: 
    - Tomcat
categories: 
    - Java
---

💠

- 1. [Tomcat](#tomcat)
    - 1.1. [目录结构](#目录结构)
    - 1.2. [配置运行](#配置运行)
        - 1.2.1. [配置解压方式的Tomcat](#配置解压方式的tomcat)
            - 1.2.1.1. [IDE中配置运行](#ide中配置运行)
        - 1.2.2. [编码](#编码)
        - 1.2.3. [虚拟目录](#虚拟目录)
            - 1.2.3.1. [默认主页](#默认主页)
            - 1.2.3.2. [虚拟主机](#虚拟主机)
            - 1.2.3.3. [配置 GZip压缩](#配置-gzip压缩)
            - 1.2.3.4. [配置IO方式](#配置io方式)
    - 1.3. [Tomcat Native](#tomcat-native)
    - 1.4. [Web容器和Web服务器的区别](#web容器和web服务器的区别)
        - 1.4.1. [Web容器](#web容器)
        - 1.4.2. [Web服务器](#web服务器)
            - 1.4.2.1. [Servlet](#servlet)
- 2. [同类项目](#同类项目)
    - 2.1. [Jetty](#jetty)
        - 2.1.1. [配置](#配置)
    - 2.2. [Undertow](#undertow)
- 3. [Tips](#tips)

💠 2024-02-22 18:18:03
****************************************
# Tomcat
> [官方网站](http://tomcat.apache.org/)

- 官网上大致有：
    - Tomcat `7 8 8.5 9` 大版本
    - Tomcat Native `优化Tomcat性能，提升数倍`
    - Apache Standard Taglib `JSTL的实现`
    - Tomcat Connectors `用于连接IIS Apache` [官方文档](http://tomcat.apache.org/connectors-doc/index.html)

> [一款功能强大的Tomcat管理监控工具](https://zhuanlan.zhihu.com/p/35557373?group_id=967469270317457408)  
> [psi-probe](https://github.com/psi-probe/psi-probe)`Tomcat监控管理工具`

************************

## 目录结构
```
├── bin 二进制文件, Shell脚本 
├── conf 配置
├── lib jar包
├── logs 日志
├── temp 缓存
├── webapps 应用, war发布的目录
└── work 
```

查看Tomcat版本 `sh bin/version.sh`

## 配置运行
> 个人配置好的

- 精简版, 适合放在服务器 [tomcat-clean-8.5.31](http://cloud.kuangcp.top/tomcat-clean-8.5.31.zip) | [tomcat-clean-9.0.8](http://cloud.kuangcp.top/tomcat-clean-9.0.8.zip)
- 个人配置版,适合个人使用 [tomcat-admin-9.0.8](http://cloud.kuangcp.top/tomcat-admin-9.0.8.zip) | [tomcat-admin-8.5.31](http://cloud.kuangcp.top/tomcat-admin-8.5.31.zip)

###  配置解压方式的Tomcat
`Windows 平台`
1. 在setclasspath中把前几行关于JAVA_HOME，JRE_HOME的路径改成自己的
2. 系统中添加catalina_home环境变量
3. 运行tomcatw.exe配置里面所有的路径( JDK JRE )
4. 双击tomcat.exe启动Tomcat

`Linux 平台`
- 下载解压，然后 bin 目录下执行 `chmod +x *.sh`

************************

> 配置管理账户

`配置管理账号 tomcat-users.xml 中的 tomcat-users 节点`

```xml
    <role rolename="manager"/>　  
    <role rolename="manager-gui"/>　  
    <role rolename="admin"/>　  
    <role rolename="admin-gui"/>　  
    <role rolename="manager-script"/>  
    <user username="tomcat" password="tomcat" roles="admin-gui,admin,manager-gui,manager,manager-script"/>
```
- 其中admin-gui是为了能访问manger的界面，manager-secret是为了可以上传war文件 

************************

`配置本机外可访问管理页面`  

/conf/Catalina/localhost/ 下添加 manager.xml 文件
```xml
    <Context privileged="true" antiResourceLocking="false"   
         docBase="${catalina.home}/webapps/manager">  
             <Valve className="org.apache.catalina.valves.RemoteAddrValve" allow="^.*$" />  
    </Context> 
```

#### IDE中配置运行
> [你一定不知道IDE里的Tomcat是怎么工作的！ ](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=401107149&idx=1&sn=908bd8ba76b38417570056795626c163&scene=21#wechat_redirect)

- 虽然IDE也是引用到解压的Tomcat路径, 但是只是使用了可执行文件, 配置文件和一系列中间文件都是和原Tomcat隔离的, 这样也保证了原Tomcat能单独运行不受影响

### 编码
- 编辑conf/下的server.xml，配置Connector项 `URIEncoding="UTF-8"`
- 浏览器表单utf-8     xml utf-8  乱码 服务器   浏览器  乱码  使用response.setContentType("text/html; charset=utf-8");。
- 无效方法response.setChaoactorEncoding; xml文件里面有乱码，saxreader会生成document错误。
- 浏览器表单get方式：需要重新编码获得字符串    浏览器表单post方式 request.setCharactorEncoding(utf-8);
- 自己建立的工程里面的web.xml继承了conf/web.xml.只需要重写自己的web.xml相关的配置的参数就可以覆盖其功能

### 虚拟目录
`指定webapp目录外的可访问的文件`
1. 方法1：conf/server.xml
    - 当中找到host标签里 添加一行 `<Context path="/hello" docBase="c:/mydsadf"/>`

1. 方法2：conf/catalina/localhost/myxml.xml
    - context中添加 `<Context  docBase="c:/mydsadf"/>`
    - 访问方式 `http://localhsot:8080/myxml/`

#### 默认主页
`web.xml`
```xml
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
    </welcome-file-list>
```

#### 虚拟主机
`server.xml`
```xml
    <host name="www.baidu.com" appBase="c:/webA" 
    unpackWARs="true" autoDeploy="true">
    <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
                prefix="localhost_access_log." suffix=".txt"
                pattern="%h %l %u %t &quot;%r&quot; %s %b" />
    < Context path="/" docBase="d:/webA" />
```

- `File f=new File("/information.xml");`这个写法是错的，空指针异常
- `request.getParameter`返回字符串，如果表单里面是空的，就返回长度为零的字符串。

#### 配置 GZip压缩
> [tomcat nginx开启Gzip原博客](http://www.imooc.com/article/15304)

- 修改配置文件：/conf/server.xml
`原文件`
```xml
    <Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />
```
`修改成`
```xml
    <Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" compression="on" compressionMinSize="2048" noCompressionUserAgents="gozilla,traviata" compressableMimeType="text/html,text/xml,text/javascript,application/x-javascript,application/javascript,text/css,text/plain"/>
```
#### 配置IO方式
> 默认http1.1是nio, 还有aio ajp bio

## Tomcat Native
> [官方文档](http://tomcat.apache.org/native-doc/) | [参考: tomcat安装与配置native,apr](https://blog.csdn.net/shangruo/article/details/52776212)


*************************
## Web容器和Web服务器的区别
### Web容器

`何为容器：`  
容器是一种服务调用规范框架，J2EE 大量运用了容器和组件技术来构建分层的企业级应用。在 J2EE 规范中，相应的有 WEB Container 和 EJB Container 等。

- WEB 容器给处于其中的应用程序组件（JSP，SERVLET）提供一个环境，使 JSP，SERVLET 直接跟容器中的环境变量交互，不必关注其它系统问题
- （从这个角度来说，web 容器应该属于架构上的概念）。web 容器主要由 WEB 服务器来实现。例如：TOMCAT，WEBLOGIC，WEBSPHERE 等。
- 若容器提供的接口严格遵守 J2EE 规范中的 WEB APPLICATION 标准。我们把该容器叫做 J2EE 中的 WEB 容器。
    - WEB 容器更多的是跟基于 HTTP 的请求打交道。而 EJB 容器不是。它是更多的跟数据库、其它服务打交道。
- 容器的行为是 将其内部的应用程序组件与外界的通信协议交互进行了隔离，从而减轻内部应用程序组件的负担（实现方面的负担？）。
    - 例如：SERVLET 不用关心 HTTP 的细节，而是直接引用环境变量 session、request、response 就行、EJB 不用关心数据库连接速度、各种事务控制，直接由容器来完成。

### Web服务器
- Web 服务器（Web Server）可以处理 HTTP 协议。当 Web 服务器接收到一个 HTTP 请求，会返回一个 HTTP 响应，例如送回一个 HTML 页面。
- Web 服务器可以响应针对静态页面或图片的请求， 进行页面跳转（redirect），或者把动态响应（dynamic response）的产生委托（delegate）给一些其它的程序
    - 例如 CGI 脚本，JSP（JavaServer Pages）脚本，servlets，ASP（Active Server Pages）脚本，服务器端 JavaScript，或者一些其它的服务器端技术。
    - Web 服务器仅仅提供一个可以执行服务器端程序和返回(程序所产生的)响应的环境，而不会超出职能范围。
    - Web 服务器主要是处理需要向浏览器发送 HTML 的请求以供浏览。

#### Servlet 

- Servlet（Server Applet），全称 Java Servlet，未有中文译文。是用 Java 编写的服务器端程序。其主要功能在于交互式地浏览和修改数据，生成动态 Web 内容。
- 狭义的 Servlet 是指 Java 语言实现的一个接口
- 广义的 Servlet 是指任何实现了这个 Servlet 接口的类，一般情况下，人们将 Servlet 理解为后者。
- Servlet 运行于支持 Java 的应用服务器中。从实现上讲，Servlet 可以响应任何类型的请求，但绝大多数情况下 Servlet 只用来扩展基于 HTTP 协议的 Web 服务器。

*************************
# 同类项目
## Jetty
- [Jetty官网](http://www.eclipse.org/jetty/) 

[参考: Jetty使用教程（一）——开始使用Jetty ](http://www.cnblogs.com/yiwangzhibujian/p/5832597.html)

### 配置
_自身log配置_
> [相关](http://zetcode.com/java/jetty/logging/)
_resources/jetty-logging.properties_ 内容如下开启DEBUG
```conf
    org.eclipse.jetty.util.log.class=org.eclipse.jetty.util.log.StrErrLog
    org.eclipse.jetty.LEVEL=DEBUG
    jetty.logs=logs
```

> [参考: Jetty和Tomcat的选择：按场景而定](http://www.open-open.com/lib/view/open1322622094390.html)

```
    一个简单项目, 就是index.jsp 里面放了个 Hello 字符串
    经过对比 8.5.29 jetty 9.2 
    启动时间 jetty花费时间是Tomcat2倍
    启动后内存 Jetty480M Tomcat300M
    1000并发 20000总量 
    Tomcat涨到 460M 第二次480M  连续5次后上660M了 10次900M 最长时间时而220ms 时而 70ms
    Jetty涨到770M 第二次压测直接上900M了 十次后也是900M 最长响应时间稳定在 220ms
```

## Undertow
> [Official Site](http://undertow.io/)  

************************

#  Tips
- servletContextLisner 和Spring环境的加载顺序要注意
- [Tomcat启动卡住,因为random](https://www.jianshu.com/p/576d356dc163)

************************
> [Tomcat 启动报错SEVERE: Unable to process Jar entry](https://www.jqhtml.com/43116.html)

- 表现
    - 启动Tomcat 大量的 Unable to process Jar entry
    - 最后 Tomcat OOM
- 排查过程
    - 首先判断为Maven缓存导致的问题, 下载下来的jar是有问题的, 但是通过比较 md5 发现文件是一致的
    - 然后搜索相关信息, javassist jar包依赖冲突, 也不是
- 技术原因分析
    - 在这次遇到的问题是 spring-boot-autoconfigure 2.0.1.RELEASE 依赖不能和 Tomcat 7.0.55 兼容, 导致了 Unable to process Jar entry EOFException 报错
    - 但是这个报错不影响应用 深层次原因是 这个 autoconfigure 会尝试将项目所有依赖都加载扫描一次
    - 如果物理机或者容器内存不够, 就会直接down掉, 但是! 内存够的话 就不影响后续的启动, 除非应用确实需要使用SpringBoot框架的 2.0.1 版本
- 人为原因
    - 没有做好依赖管理, 导致了 SpringBoot 被错误的引入

