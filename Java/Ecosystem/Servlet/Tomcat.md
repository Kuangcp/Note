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
- 2. [Tomcat Native](#tomcat-native)
- 3. [Tips](#tips)

💠 2024-06-12 10:01:44
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


************************

# Tomcat Native
> [官方文档](http://tomcat.apache.org/native-doc/) | [参考: tomcat安装与配置native,apr](https://blog.csdn.net/shangruo/article/details/52776212)


*************************

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

