---
title: 使用maven新建Java Web3.0项目
date: 2019-02-12 16:28:54
tags: 
categories: 
---

**目录 start**
 
1. [使用maven新建Web3.0项目](#使用maven新建web30项目)
    1. [添加web容器](#添加web容器)
        1. [Jetty](#jetty)
        1. [Tomcat](#tomcat)
    1. [加入Servlet的API包](#加入servlet的api包)

**目录 end**|_2019-02-12 16:36_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 使用maven新建Web3.0项目
> [网络maven仓库](http://mvnrepository.com/)

- 新建maven 选择webapp 然后输入三要素
- 但是因为模板默认的是web2.3，所以要手动修改成3.0
- 1. pom文件中添加插件 编译部分
```xml
    <plugin>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.0</version>
        <configuration>
            <source>1.8</source>
            <target>1.8</target>
        </configuration>
    </plugin>
```
- 2.navigator目录模式下 修改相关文件，把2.3改成3.0
- 3.eclipse中右击改动Facets 然后maven-update一下就可以了

## 添加web容器
### Jetty
- http://mvnrepository.com/ 里找到想要的版本，加入即可
特别注意 NIO的原因，静态文件在服务器启动的时候不能更改，需要找到maven仓库下的org/eclipse/jettyjetty-webapp/ 
下的jar包中的default配置文件，把useFileBuffer标签的 true 改成false

```xml
<plugin>
    <groupId>org.mortbay.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <version>8.1.16.v20140903</version>
    <executions>
        <execution>
            <!-- 在打包成功后使用jetty:run来运行 -->
            <phase>package</phase>
            <goals>
                <goal>run</goal>
            </goals>
        </execution>
    </executions>
    <configuration>
        <stopKey>stop</stopKey>
        <stopPort>9999</stopPort>
        <scanIntervalSeconds>1</scanIntervalSeconds>
        <contextXml>${project.basedir}/src/main/resources/jetty-context.xml</contextXml>
        <webApp>
        <!--这里配置主机后的目录，现在表示根目录，最好加上项目名例如： /Project -->
            <contextPath>/</contextPath>
        </webApp>
        <connectors>
            <connector implementation="org.eclipse.jetty.server.nio.SelectChannelConnector">
                <port>80</port>
                <maxIdleTime>60000</maxIdleTime>
            </connector>
        </connectors>
    </configuration>
</plugin>
```
- 部署成功后，使用jetty:run 即可运行起服务器

### Tomcat
- 去Tomcat官网 找到maven plugins进入找到想要的版本即可

```xml
<plugin>
    <groupId>org.apache.tomcat.maven</groupId>
    <artifactId>tomcat6-maven-plugin</artifactId>
    <version>2.2</version>
    <executions>
        <execution>
            <!-- 在打包成功后使用tomcat6:deploy来运行 -->
            <phase>package</phase>
            <goals>
                <goal>run</goal>
            </goals>
        </execution>
    </executions>
    <configuration>
        <!-- 注意此处的url -->
        <url>http://localhost:8080/manager/text</url>
        <server>tomcat6</server> <!-- 此处的名字必须和setting.xml中配置的ID一致 -->
        <path>/mavenProject</path> <!-- 此处的名字是项目发布的工程名 -->
    </configuration>
</plugin>
```
- 部署完成后 tomcat7:deploy 运行服务器

## 加入Servlet的API包
```xml
    <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <version>3.0.1</version>
        <scope>provided</scope>
	</dependency>
```
