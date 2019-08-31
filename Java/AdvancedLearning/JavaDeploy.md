---
title: Java应用的部署
date: 2018-11-21 10:56:52
tags: 
    - 部署
categories: 
    - Java
---

**目录 start**
 
1. [部署运行](#部署运行)
    1. [打包可执行jar](#打包可执行jar)
        1. [用命令手动打包](#用命令手动打包)
    1. [打包war](#打包war)
    1. [Docker镜像](#docker镜像)
        1. [手动](#手动)
1. [配置文件](#配置文件)
1. [Tips](#tips)
    1. [Java在Linux上的时区问题](#java在linux上的时区问题)

**目录 end**|_2019-08-31 23:52_|
****************************************
# 部署运行
> 传统的可执行jar, war 以及Docker镜像

> [参考博客: JAR 文件揭密](https://www.ibm.com/developerworks/cn/java/j-jar/index.html)
> [参考博客: maven-assembly-plugin 入门指南](https://www.jianshu.com/p/14bcb17b99e0)

> [Maven 打包部署](/Java/Tool/Maven.md#打包部署)  |  [Gradle 打包部署](/Java/Tool/Gradle.md#打包部署)  

## 打包可执行jar
> [关于MANIFEST.MF文件](https://blog.csdn.net/baileyfu/article/details/1808023)`这个文件很重要, 如果自己手动配置就需要编写该文件`
_MANIFEST.MF示例_
```yml
    Manifest-Version: 1.0
    Archiver-Version: Plexus Archiver
    Built-By: kcp
    Created-By: Apache Maven 3.5.3
    Build-Jdk: 1.8.0_152
    Main-Class: com.youaishujuhui.minigame.Main
```
- 编译文件       `javac -d *.java `
- 打包字节码成jar `jar -cvf hello.jar com/test/*.*` 
- 打包成可执行jar `jar -cvfm hello.jar mainfest *.*` 
    - 其中 `mainfest` 文本文件： `Main-Class: com.test.Main` 
    - 冒号后一定要有空格，文件最后一行一定留空行

*************************

## 打包war
> 最终将生成的war 放到 tomcat 的 webapps 目录下或者 Jetty的 webapps 目录下

## Docker镜像
> 以一个基础镜像,然后将war放进去构建成一个镜像, 然后推送到服务器上构建容器进行运行

1. 简要概括: from jdk基础镜像, 将jar 复制进去, 设置好 CMD

> [jib](https://github.com/GoogleContainerTools/jib)
> - 结合 Maven Gradle 能更方便的构建 Docker镜像

************************

# 配置文件
> 多目标应用环境的发布, 可以使用Maven 多 Profile; Spring 的多profiles; 环境变量; ...

**********************

> 在环境中存储配置

- 通常，应用的 配置 在不同 部署 (预发布、生产环境、开发环境等等)间会有很大差异。这其中包括：
    - 数据库，Memcached，以及其他 后端服务 的配置
    - 第三方服务的证书，如 Amazon S3、Twitter 等
    - 每份部署特有的配置，如域名等

有些应用在代码中使用常量保存配置，这与 12-Factor 所要求的代码和配置严格分离显然大相径庭。配置文件在各部署间存在大幅差异，代码却完全一致。

判断一个应用是否正确地将配置排除在代码之外，一个简单的方法是看该应用的基准代码是否可以立刻开源，而不用担心会暴露任何敏感的信息。

需要指出的是，这里定义的“配置”并不包括应用的内部配置，比如 Rails 的 config/routes.rb，或是使用 Spring 时 代码模块间的依赖注入关系 。这类配置在不同部署间不存在差异，所以应该写入代码。

另外一个解决方法是使用配置文件，但不把它们纳入版本控制系统，就像 Rails 的 config/database.yml 。这相对于在代码中使用常量已经是长足进步，但仍然有缺点：总是会不小心将配置文件签入了代码库；配置文件的可能会分散在不同的目录，并有着不同的格式，这让找出一个地方来统一管理所有配置变的不太现实。更糟的是，这些格式通常是语言或框架特定的。

12-Factor推荐将应用的配置存储于 环境变量 中（ env vars, env ）。环境变量可以非常方便地在不同的部署间做修改，却不动一行代码；与配置文件不同，不小心把它们签入代码库的概率微乎其微；与一些传统的解决配置问题的机制（比如 Java 的属性配置文件）相比，环境变量与语言和系统无关。

配置管理的另一个方面是分组。有时应用会将配置按照特定部署进行分组（或叫做“环境”），例如Rails中的 development,test, 和 production 环境。这种方法无法轻易扩展：更多部署意味着更多新的环境，例如 staging 或 qa 。 随着项目的不断深入，开发人员可能还会添加他们自己的环境，比如 joes-staging ，这将导致各种配置组合的激增，从而给管理部署增加了很多不确定因素。

12-Factor 应用中，环境变量的粒度要足够小，且相对独立。它们永远也不会组合成一个所谓的“环境”，而是独立存在于每个部署之中。当应用程序不断扩展，需要更多种类的部署时，这种配置管理方式能够做到平滑过渡。 

> [参考博客: 在环境中存储配置](https://12factor.net/zh_cn/config)

# Tips

## Java在Linux上的时区问题
- 表象
    - Docker容器中运行的Linux上时区是正确的, 但是Java应用的时区不对
- 原因 
    - JVM获取时区配置的顺序
    1. 查看 环境变量 TZ 
        - `export TZ=Asia/Shanghai`
    1. /etc/sysconfig/clock 中查找 ZONE 的值
        ```conf
        ZONE="Asia/Shanghai"
        UTC=false
        ARC=false
        ```
    1. /etc/localtime 或者 /usr/share/zoneinfo 
        - `ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`
    - 也可以加JVM参数 `-Duser.timezone=GMT+8`
    - 或者硬编码设置时区

> 快速测试Java获取到的时区
```java
    import java.util.Date;
    import java.time.ZoneOffset;

    public class TimeTest {
        public static void main(String[] args){
            System.out.println(new Date());
            System.out.println(ZoneOffset.systemDefault());
        }
    }
```
