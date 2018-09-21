`目录 start`
 
- [Tomcat](#tomcat)
    - [Tips](#tips)
    - [原理](#原理)
    - [配置运行](#配置运行)
        - [配置解压版 Tomcat](#配置解压版-tomcat)
            - [IDE中配置运行](#ide中配置运行)
        - [编码](#编码)
        - [虚拟目录](#虚拟目录)
            - [默认主页](#默认主页)
            - [虚拟主机](#虚拟主机)
            - [配置 GZip压缩](#配置-gzip压缩)
            - [配置IO方式](#配置io方式)
    - [Tomcat Native](#tomcat-native)
    - [Web容器和Web服务器的区别](#web容器和web服务器的区别)
        - [【web容器】](#web容器)
            - [【Web服务器】](#web服务器)
            - [【应用程序服务器（The Application Server）】](#应用程序服务器（the-application-server）)
            - [【serverlet】](#serverlet)
            - [【Tomcat】](#tomcat)
            - [【Tomcat与Web服务器、应用服务器的关系】](#tomcat与web服务器、应用服务器的关系)
    - [一、Tomcat 与应用服务器](#一、tomcat-与应用服务器)
    - [二、Tomcat 与 Web 服务器](#二、tomcat-与-web-服务器)
- [优化](#优化)
    - [Tomcat僵死问题](#tomcat僵死问题)
- [Tomcat和Jetty](#tomcat和jetty)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Tomcat
> [官方网站](http://tomcat.apache.org/)

- 官网上大致有：
    - Tomcat `7 8 8.5 9` 大版本
    - Tomcat Native `优化Tomcat性能，提升速倍`
    - Apache Standard Taglib `JSTL的实现`
    - Tomcat Connectors `用于连接IIS Apache` [官方文档](http://tomcat.apache.org/connectors-doc/index.html)

> [一款功能强大的Tomcat管理监控工具](https://zhuanlan.zhihu.com/p/35557373?group_id=967469270317457408)
> [psi-probe](https://github.com/psi-probe/psi-probe)`Tomcat监控管理工具`

##  Tips
- servletContextLisner 和Spring环境的加载顺序要注意
- [Tomcat启动卡住,因为random](https://www.jianshu.com/p/576d356dc163)
*************
## 原理
> 更多查看 `Tomcat那些事儿` 公众号  
> [Tomcat目录部署与Context描述文件context.xml ](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=2650859355&idx=1&sn=2122baf040ae337dba90201a48b4e11c&chksm=f1329888c645119eec4473e11beaf988c48ce02c52151502086595de59b65dd4bd7cf129530e&scene=21#wechat_redirect)
> | [Tomcat配置文件解析与Digester](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=2650859293&idx=1&sn=3c017b2675bb59fda8ae037b7a1e6cb4&chksm=f13298cec64511d8183a23f1b3110bc6b65e8742c6e76391a51c552d86c0bc81a34fab8d0a60&scene=21#wechat_redirect)  
> | [Servlet到底是单例还是多例你了解吗？](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=401278436&idx=1&sn=7d28750b7cff1f706efb82c7fcaa73c5&scene=21#wechat_redirect)
> | [Tomcat类加载器以及应用间class隔离与共享 ](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=2650859298&idx=1&sn=8856375f2268fc33a6bb3fbc6932eca7&chksm=f13298f1c64511e77ef1d77d28272840ca56f62da6e11928c78827e8ec53f937f812a4b49aa0&scene=21#wechat_redirect)  
> | [啥，Tomcat里竟然还有特权应用? ](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=2650859476&idx=1&sn=8be7a37b59a5d167998f6695a1606d39&chksm=f1329807c6451111d2a1c379221655dc87dd105b067f894bfb202d1f9f283bad310a5cdc2277&scene=21#wechat_redirect)
> | [你了解JMX在Tomcat的应用吗?](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=401135587&idx=1&sn=610950fda2eceb3683a9fe45078f1a83&scene=21#wechat_redirect)

## 配置运行
- 精简版, 适合放在服务器
    - [tomcat-clean-8.5.31](http://cloud.kuangcp.top/tomcat-clean-8.5.31.zip) | [tomcat-clean-9.0.8](http://cloud.kuangcp.top/tomcat-clean-9.0.8.zip)
- 个人配置版,适合个人图形化使用
    - [tomcat-admin-9.0.8](http://cloud.kuangcp.top/tomcat-admin-9.0.8.zip) | [tomcat-admin-8.5.31](http://cloud.kuangcp.top/tomcat-admin-8.5.31.zip)

###  配置解压版 Tomcat
`Windows 平台`
1. 在setclasspath中把前几行关于JAVA_HOME，JRE_HOME的路径改成自己的
2. 系统中添加catalina_home环境变量
3. 运行tomcatw.exe配置里面所有的路径( JDK JRE )
4. 双击tomcat.exe启动Tomcat

`Linux 平台`
- 下载解压，然后 bin 目录下执行 `chmod +x *.sh`

> [参考博客](http://blog.csdn.net/kkgbn/article/details/52071109)

`配置管理账号 tomcat-users.xml`
```xml
    <role rolename="manager"/>　  
    <role rolename="manager-gui"/>　  
    <role rolename="admin"/>　  
    <role rolename="admin-gui"/>　  
    <role rolename="manager-script"/>  
    <user username="tomcat" password="tomcat" roles="admin-gui,admin,manager-gui,manager,manager-script"/>
```
- 其中admin-gui是为了能访问manger的界面，manager-secret是为了可以上传war文件 

`配置本机外可访问管理页面`
-  /conf/Catalina/localhost/下  添加manager.xml 
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
- 方法1：conf/server.xml
    - 当中找到host标签里 添加一行 `<Context path="/hello" docBase="c:/mydsadf"/>`

- 方法2：conf/catalina/localhost/myxml.xml
    - `context放置进来< Context  docBase="c:/mydsadf"/>`
    - `访问方式http://localhsot:8080/myxml/`

#### 默认主页
`web.xml`
```xml
    < welcome-file-list>
    < welcome-file>index.html< /welcome-file>
    < /welcome-file-list>
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
    >

```
- `File f=new File("/information.xml");`这个写法是错的，空指针异常
- `request.getParameter`返回字符串，如果表单里面是空的，就返回长度为零的字符串。

#### 配置 GZip压缩
> [tomcat nginx开启Gzip原博客](http://www.imooc.com/article/15304)

- 修改配置文件：/conf/server.xml
`原文件`
```
    <Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />
```
`修改成`
```xml
    <Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" compression="on" compressionMinSize="2048" noCompressionUserAgents="gozilla,traviata" compressableMimeType="text/html,text/xml,text/javascript,application/x-javascript,application/javascript,text/css,text/plain"/>
```
#### 配置IO方式
> 默认http1.1是nio, 还有aio ajp bio

## Tomcat Native
> [官方文档](http://tomcat.apache.org/native-doc/) | [参考博客: tomcat安装与配置native,apr](https://blog.csdn.net/shangruo/article/details/52776212)


*************************
##	Web容器和Web服务器的区别
### 【web容器】 

`何为容器：`
- 容器是一种服务调用规范框架，J2EE 大量运用了容器和组件技术来构建分层的企业级应用。在 J2EE 规范中，相应的有 WEB Container 和 EJB Container 等。
- WEB 容器给处于其中的应用程序组件（JSP，SERVLET）提供一个环境，使 JSP，SERVLET 直接跟容器中的环境变量交互，不必关注其它系统问题
- （从这个角度来说，web 容器应该属于架构上的概念）。web 容器主要由 WEB 服务器来实现。例如：TOMCAT，WEBLOGIC，WEBSPHERE 等。
- 若容器提供的接口严格遵守 J2EE 规范中的 WEB APPLICATION 标准。我们把该容器叫做 J2EE 中的 WEB 容器。
    - WEB 容器更多的是跟基于 HTTP 的请求打交道。而 EJB 容器不是。它是更多的跟数据库、其它服务打交道。
- 容器的行为是 将其内部的应用程序组件与外界的通信协议交互进行了隔离，从而减轻内部应用程序组件的负担（实现方面的负担？）。
    - 例如：SERVLET 不用关心 HTTP 的细节，而是直接引用环境变量 session、request、response 就行、EJB 不用关心数据库连接速度、各种事务控制，直接由容器来完成。

#### 【Web服务器】
- Web 服务器（Web Server）可以处理 HTTP 协议。当 Web 服务器接收到一个 HTTP 请求，会返回一个 HTTP 响应，例如送回一个 HTML 页面。
    - Web 服务器可以响应针对静态页面或图片的请求， 进行页面跳转（redirect），或者把动态响应（dynamic response）的产生委托（delegate）给一些其它的程序
    - 例如 CGI 脚本，JSP（JavaServer Pages）脚本，servlets，ASP（Active Server Pages）脚本，服务器端 JavaScript，或者一些其它的服务器端技术。
        - Web 服务器仅仅提供一个可以执行服务器端程序和返回(程序所产生的)响应的环境，而不会超出职能范围。
        - Web 服务器主要是处理需要向浏览器发送 HTML 的请求以供浏览。

#### 【应用程序服务器（The Application Server）】
- 根据定义，作为应用程序服务器，要求可以通过各种协议（包括 HTTP 协议）把商业逻辑暴露给（expose）客户端应用程序。
    - 应用程序使用此商业逻辑就像你调用对象的一个方法或过程（语言中的一个函数）一样。

#### 【serverlet】

- Servlet（Server Applet），全称 Java Servlet，未有中文译文。是用 Java 编写的服务器端程序。其主要功能在于交互式地浏览和修改数据，生成动态 Web 内容。
- 狭义的 Servlet 是指 Java 语言实现的一个接口
- 广义的 Servlet 是指任何实现了这个 Servlet 接口的类，一般情况下，人们将 Servlet 理解为后者。
- Servlet 运行于支持 Java 的应用服务器中。从实现上讲，Servlet 可以响应任何类型的请求，但绝大多数情况下 Servlet 只用来扩展基于 HTTP 协议的 Web 服务器。

#### 【Tomcat】

- Tomcat 服务器是一个免费的开放源代码的 Web 应用服务器，属于轻量级应用服务器，在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试 JSP 程序的首选。
- 对于一个初学者来说，可以这样认为，当在一台机器上配置好 Apache 服务器，可利用它响应对 HTML 页面的访问请求。
- 实际上 Tomcat 部分是Apache 服务器的扩展，但它是独立运行的，所以当你运行 tomcat 时，它实际上作为一个与 Apache 独立的进程单独运行的。
- Apache Tomcat is an open source software implementation of the Java Servlet and JavaServer Pages technologies.

#### 【Tomcat与Web服务器、应用服务器的关系】
>Tomcat 服务器是一个免费的开放源代码的 Web 应用服务器。因为 Tomcat 技术先进、性能稳定且免费，所以深受 Java 爱好者的喜爱并得到了部分软件开发商的认可，成为目前比较流行的 Web 应用服务器。

*******************
## 一、Tomcat 与应用服务器

>到目前为止，Tomcat 一直被认为是 Servlet/JSP API 的执行器，也就所谓的 Servlet 容器。然而，Tomcat并不仅仅如此，它还提供了 JNDI 和 JMX API 的实现机制。尽管如此，Tomcat 仍然还不能算是应用服务器，因为它不提供大多数 J2EE API 的支持。

很有意思的是，目前许多的应用服务器通常把 Tomcat 作为它们 Servlet 和 JSP API 的容器。由于 Tomcat允许开发者只需通过加入一行致谢，就可以把 Tomcat 嵌入到它们的应用中。遗憾的是，许多商业应用服务器并没有遵守此规则。

对于开发者来说，如果是为了寻找利用 Servlet、JSP、JNDI 和 JMX 技术来生成 Java Web 应用的话，选择Tomcat 是一个优秀的解决方案；但是为了寻找支持其他的 J2EE API，那么寻找一个应用服务器或者把 Tomcat作为应用服务器的辅助，
将是一个不错的解决方案；第三种方式是找到独立的 J2EE API 实现，然后把它们跟Tomcat 结合起来使用。虽然整合会带来相关的问题，但是这种方式是最为有效的。

## 二、Tomcat 与 Web 服务器

Tomcat 是提供一个支持 Servlet 和 JSP 运行的容器。Servlet 和 JSP 能根据实时需要，产生动态网页内容。而对于 Web 服务器来说， Apache 仅仅支持静态网页，对于支持动态网页就会显得无能为力；Tomcat 则既能为动态网页服务，同时也能为静态网页提供支持。
尽管它没有通常的 Web 服务器快、功能也不如 Web 服务器丰富，但是 Tomcat 逐渐为支持静态内容不断扩充。大多数的 Web 服务器都是用底层语言编写如 C，利用了相应平台的特征，因此用纯 Java 编写的 Tomcat 执行速度不可能与它们相提并论。

一般来说，大的站点都是将 Tomcat 与 Apache 的结合，Apache 负责接受所有来自客户端的 HTTP 请求，然后将 Servlets 和 JSP 的请求转发给 Tomcat 来处理。Tomcat 完成处理后，将响应传回给 Apache，最后 Apache 将响应返回给客户端。

*************************
# 优化

## Tomcat僵死问题
- [ ] 分析各种可能的原因

*************************
# Tomcat和Jetty
> [参考博客: Jetty和Tomcat的选择：按场景而定](http://www.open-open.com/lib/view/open1322622094390.html)

- [Jetty官网](http://www.eclipse.org/jetty/) 

```
    一个简单项目, 就是index.jsp 里面放了个 Hello 字符串
    经过对比 8.5.29 jetty 9.2 
    启动时间 jetty花费时间是Tomcat2倍
    启动后内存 Jetty480M Tomcat300M
    1000并发 20000总量 
    Tomcat涨到 460M 第二次480M  连续5次后上660M了 10次900M 最长时间时而220ms 时而 70ms
    Jetty涨到770M 第二次压测直接上900M了 十次后也是900M 最长响应时间稳定在 220ms
```
