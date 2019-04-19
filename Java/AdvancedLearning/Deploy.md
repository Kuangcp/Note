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
        1. [Maven](#maven)
        1. [Gradle](#gradle)
    1. [打包war](#打包war)
    1. [Docker镜像](#docker镜像)
        1. [手动](#手动)
        1. [Maven](#maven)
        1. [Gradle](#gradle)
1. [配置文件](#配置文件)

**目录 end**|_2019-04-19 13:04_| [Kuangcp](https://github.com/Kuangcp/Note) | [yi-yun](https://github.com/yi-yun/Memo)
****************************************
# 部署运行
> 传统的可执行jar, war 以及Docker镜像

> [参考博客: JAR 文件揭密](https://www.ibm.com/developerworks/cn/java/j-jar/index.html)
> [参考博客: maven-assembly-plugin 入门指南](https://www.jianshu.com/p/14bcb17b99e0)

## 打包可执行jar
### 用命令手动打包
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
- 编译文件        `javac -d *.java `
- 打包字节码成jar `jar -cvf hello.jar com/test/*.*` 
- 打包成可执行jar `jar -cvfm hello.jar mainfest *.*` 
    - 其中：`mainfest` 文本文件： `Main-Class: com.test.Main` 冒号后一定要有空格，文件最后一行一定留空行

- 运行jar包中指定的类`java -cp clojure.jar clojure.main`
    - 多个jar运行 `java -cp jline-0.9.94.jar;clojure.jar jline.ConsoleRunner clojure.main`
    - [参考博客: 用java –jar 命令运行Jar包](https://blog.csdn.net/paullinjie/article/details/53188943)

### Maven

**不依赖Jar的项目**
> [Demo项目](https://gitee.com/gin9/codes/ri4x8cut3awgh0e271lfb54) | [详情](/Java/Tool/Maven.md#31打包成可执行jar)

**依赖Jar的项目**
- [ ] 完善 Maven 含 Jar 打包可执行jar

> [Maven实战（九）——打包的技巧](http://www.infoq.com/cn/news/2011/06/xxb-maven-9-package)
> [Maven打包成可执行jar](https://blog.csdn.net/u013177446/article/details/53944424)
> [参考博客: 使用MAVEN打包可执行的jar包](https://www.jianshu.com/p/afb79650b606)

1. [Demo项目的完整代码片段](https://gitee.com/gin9/codes/ri4x8cut3awgh0e271lfb54)
    - 多个main的情况下运行指定的main 
        - `java -cp example03-1.0-SNAPSHOT.jar cn.zhouyafeng.itchat4j.main.TulingRobot`

> war和jar一样使用
- Springboot项目能够做到, 其实就是Main方法, 然后配置了一个Servlet的加载类就可以当war用了
    - [通过Maven构建打包Spring boot，并将config配置文件提取到jar文件外](http://lib.csdn.net/article/java/65574)

> [一个项目生成若干不同内容的Jar](https://stackoverflow.com/questions/2424015/maven-best-practice-for-generating-multiple-jars-with-different-filtered-classes)

### Gradle
> [参考博客: Building Java Applications](https://guides.gradle.org/building-java-applications/)

**不依赖Jar的项目**
1. 依据模板新建项目 `gradle init --type java-application` 
    ```groovy
        // 主要是如下配置
        plugins {
            // Apply the java plugin to add support for Java
            id 'java'
            // Apply the application plugin to add support for building an application
            id 'application'
        }
        // Define the main class for the application
        mainClassName = 'App'
    ```
1. add this config to build.gradle
    ```groovy
        jar {
            manifest {
                attributes 'Main-Class': 'base.Main'
            }
        }
    ```
1. run : `gradle clean jar && java -jar file`   

**依赖Jar的项目**
> 有好几种插件可以实现 1.[shadow插件官网文档](http://imperceptiblethoughts.com/shadow/) 

- [ ] 完善 Gradle 含 Jar 打包可执行jar

*************************

## 打包war
> 供 Servlet 容器直接运行

> 最终将生成的war 放到 tomcat 的 webapps 目录下或者Jetty的 webapps 目录下

********************

## Docker镜像
> 以一个基础镜像,然后将war放进去构建成一个镜像, 然后推送到服务器上构建容器进行运行

> [jib](https://github.com/GoogleContainerTools/jib)
> - 结合 Maven Gradle 方便的构建 Docker镜像

### 手动

### Maven

### Gradle

**********************************

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
