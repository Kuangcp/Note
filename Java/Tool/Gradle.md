---
title: Gradle
date: 2018-12-12 21:29:59
tags: 
    - Gradle
categories: 
    - Java
---

💠

- 1. [Gradle](#gradle)
    - 1.1. [书籍](#书籍)
    - 1.2. [发行版本列表](#发行版本列表)
- 2. [安装](#安装)
    - 2.1. [Chocolate](#chocolate)
    - 2.2. [解压配置](#解压配置)
    - 2.3. [Wrapper](#wrapper)
    - 2.4. [CUI使用](#cui使用)
        - 2.4.1. [命令行选项](#命令行选项)
        - 2.4.2. [动作](#动作)
            - 2.4.2.1. [build](#build)
            - 2.4.2.2. [test](#test)
        - 2.4.3. [守护进程](#守护进程)
- 3. [配置](#配置)
    - 3.1. [全局配置文件](#全局配置文件)
    - 3.2. [build.gradle](#buildgradle)
        - 3.2.1. [SourceSet](#sourceset)
        - 3.2.2. [依赖管理](#依赖管理)
            - 3.2.2.1. [依赖排除以及指定依赖版本](#依赖排除以及指定依赖版本)
            - 3.2.2.2. [统一管理依赖](#统一管理依赖)
        - 3.2.3. [配置镜像源](#配置镜像源)
        - 3.2.4. [插件](#插件)
            - 3.2.4.1. [Lombok](#lombok)
            - 3.2.4.2. [Maven Publish](#maven-publish)
            - 3.2.4.3. [shadowJar](#shadowjar)
            - 3.2.4.4. [docker](#docker)
            - 3.2.4.5. [protobuf-gradle-plugin](#protobuf-gradle-plugin)
    - 3.3. [setting.gradle](#settinggradle)
- 4. [Gradle多模块的构建](#gradle多模块的构建)
    - 4.1. [另一种多模块的构建方式](#另一种多模块的构建方式)
- 5. [使用](#使用)
    - 5.1. [安装到本地仓库](#安装到本地仓库)
    - 5.2. [上传至构件仓库](#上传至构件仓库)
- 6. [打包部署](#打包部署)
    - 6.1. [构建Docker镜像](#构建docker镜像)
        - 6.1.1. [插件方式构建Docker镜像](#插件方式构建docker镜像)

💠 2024-05-02 00:46:30
****************************************

# Gradle
> [Official Guide](https://gradle.org/guides/?q=JVM) | [tutorials](https://www.tutorialspoint.com/gradle/index.htm)  

> [参考: 零散知识点总结(1) - Gradle 使用配置总结](https://www.jianshu.com/p/47cbbb4eab13)

> [Github: Gradle samples](https://github.com/gradle/gradle/tree/master/subprojects/docs/src/samples)
******************************
个人决定弃用Gradle

**优缺点**
> [Gradle大吐槽](https://blog.csdn.net/MCL529/article/details/79341706)
> [官方对比Gradle和Maven](https://gradle.org/maven-vs-gradle/)

> 优点  
1. 相较Maven,Gradle配置文件更简洁，灵活度高（groovy语言实现各种自定义操作：多目标构建，多端发布）
1. 知名项目在使用，阅读调试源码需要使用到，例如：Srping全家桶、Andriod等等
1. 支持编程式任务，相较于Maven的XML配置文件，Gradle的配置文件为Groovy或Kotlin脚本，更灵活 功能强大。
    - 常见的 多目标构建，多端发布 等等
	- 例如自定义的本地ci流程: 将SpringBoot项目打包构建Docker镜像,并打上 release且带上git commitId 的 tag, 然后删除应用旧有运行时容器,使用新的镜像启动新的容器

> 缺点  
1. 内存和CPU等资源占用大于Maven，虽然新出的mvnd资源占用更大 emm。
1. 引用依赖时对Maven兼容，发布依赖不支持，`需要第三方插件`。？？？
1. Gradle本身设计使用的API和规范一直在变，有些改动不考虑兼容性，`不稳定`。
    - 当你想要捡起一个多年前的项目编译运行时发现要看文档，调整一堆才能正常用，当然，不更新Gradle就没问题 但是每年一个大版本，强迫症不适应
1. 多项目管理没有Maven方便，多项目结构或依赖发生变更需要更复杂更慢的流程才能刷新重新加载完成。
1. Gradle 缺省使用wrapper，并且Gradle发布非常频繁，容易导致本地一堆gradle版本占用磁盘，加载新项目还需要等待下载不同的gradle版本
    - 虽然可以通过手动快速取消IDEA自动下载，手动指定Gradle版本来避免，但是过程就很恶心。
1. IDEA对Gradle的支持远没有Maven好（例如依赖跳转，依赖冲突，依赖树等功能 Gradle全没有），一方面也是Gradle变更太快，设计太灵活导致的
    - 报错信息全靠Google，没法直接定位，如果使用Maven的话报错基本发生在代码中，而不是构建工具本身，`时间不是可以这么浪费的`。

> [参考: Gradle在大型Java项目上的应用](www.infoq.com/cn/articles/Gradle-application-in-large-Java-projects)  
> [我讨厌 Gradle！！！](https://gist.github.com/CrazyBoyFeng/936680de7dd0a7cdd5558c7ba6e8fe84)  
> [唉，来吐槽一下 gradle](https://www.v2ex.com/t/735701)  

********************
## 书籍
> [Gradle in Action 中译](http://www.jb51.net/books/527811.html) `如果没有一点Groovy基础, 阅读自定义Task等一些高自定义的地方还是比较困惑`

## 发行版本列表
> [Github地址](https://github.com/gradle/gradle/releases)`查看简洁的 Release Note 更方便`

# 安装
> 注意 Gradle 会默认使用Maven的本地库, 但是是复制过来使用而不是共用   
> 会将 `~/.m2/repository` 复制到 `~/.gradle/caches/modules-2/files-2.1/`, 目录结构也发生改变  
- [Gradle 使用Maven的本地仓库](https://blog.csdn.net/kcp606/article/details/81636426)

> 或者 SDKMAN安装 `sdk install gradle`

## Chocolate
- windows 上安装 chocolate
- PowerShell中运行 `wr https://chocolatey.org/install.ps1 -UseBasicParsing | iex`
- 若操作系统默认禁止执行脚本，执行一次`set-executionpolicy remotesigned`后脚本顺利执行
- Chocolatey在安装包的时候，默认路径是按照系统的默认路径来的，如果想修改安装路径可以这样处理：
1. 执行“开始/运行”命令（或者WIN + R），输入“regedit”，打开注册表。
2. 展开注册表到下面的分支[HKEY＿LOCAL＿MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion]，在右侧窗口中找到名为“ProgramFilesDir”的字符串，双击把数值“C:\Program Files”修改为“D：\ProgramFiles”，确定退出后,即可更改常用软件的安装路径了。

## 解压配置
> [官方下载网址](http://services.gradle.org/) 有各个版本的下载以及版本发行说明

- [腾讯云镜像](https://mirrors.cloud.tencent.com/gradle/)

1. 解压到任意目录, 并将 bin 目录加入 环境变量即可

## Wrapper
> [The Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html)

类似于 Maven 的 mvnw 脚本 在使用IDE生成项目的时候，可以选择gradle的执行目录，可以选`gradle wrapper` 也可以选自己下载解压的完整包  
如果使用的不是这个wrapper，那么别人在下载项目后，运行gradle命令就要先安装gradle，使用wrapper更好  

```groovy
   task wrapper(type: Wrapper){
      gradleVersion = '4.8'
      distributionUrl = '限定访问内网的URL'
      distributionPath = '包装器被解压缩放的相对路径'
   }
```
- 运行 gradle wrapper 一次即可开始使用包装器的脚本来构建项目了
- 生成gradle包管理器：`gradle wrapper --gradle-version 2.0`
- 下载的多版本gradle `~/.gradle/wrapper/dists`
************************

## CUI使用
### 命令行选项
- `tasks` : 输出所有建立的task
- `properties` : 输出所有可用的配置属性
- 执行 task `gradle taskName`
- 交互式新建项目 `gradle init`

- `-b，--build-file test.gradle` 指定运行脚本文件
- `--offline` 离线模式
- `-P ,--project-prop`:配置参数 -Pmyprop=value
- `-i,--info` : 打印info级别的输出
- `-s,--stacktrace`: 输出错误栈
- `-q,--quiet`:减少构建出错时打印的错误信息

### 动作
#### build

#### test 

- gradle test -Dtest.single=YourTestClass
- gradle test --tests org.somewhere.MyTestClass
- gradle test --tests org.somewhere.MyTestClass.my_test_case

### 守护进程

- 命令加上 `--daemon`就会开启一个守护进程，只会开启一次
- 守护进程会在空闲3小时后销毁
- 手动关闭 `gadle --stop `
- 构建时不采用守护进程 `--no--daemon`

************************

# 配置
## 全局配置文件

> 配置镜像源

_~/.gradle/init.gradle_
```groovy
allprojects{
    repositories {
        def ALIYUN_REPOSITORY_URL = 'https://maven.aliyun.com/repository/public'
        def ALIYUN_JCENTER_URL = 'https://maven.aliyun.com/repository/public'
        def ALIYUN_GOOGLE_URL = 'https://maven.aliyun.com/repository/google'
        def ALIYUN_GRADLE_PLUGIN_URL = 'https://maven.aliyun.com/repository/gradle-plugin'
        all { ArtifactRepository repo ->
            if(repo instanceof MavenArtifactRepository){
                def url = repo.url.toString()
                if (url.startsWith('https://repo1.maven.org/maven2/')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_REPOSITORY_URL."
                    remove repo
                }
                if (url.startsWith('https://jcenter.bintray.com/')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_JCENTER_URL."
                    remove repo
                }
                if (url.startsWith('https://dl.google.com/dl/android/maven2/')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_GOOGLE_URL."
                    remove repo
                }
                if (url.startsWith('https://plugins.gradle.org/m2/')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_GRADLE_PLUGIN_URL."
                    remove repo
                }
            }
        }
        maven { url ALIYUN_REPOSITORY_URL }
        maven { url ALIYUN_JCENTER_URL }
        maven { url ALIYUN_GOOGLE_URL }
        maven { url ALIYUN_GRADLE_PLUGIN_URL }
    }
}
```

## build.gradle
> _Hello World_
```groovy
   task helloworld{
      doLast {
         printf 'Hello World!'
      }
   }
   // 或者是 使用 << 代表doLast：
   task helloworld<<{
      println 'Hello world!'
   }
```
运行：`gradle -q helloworld`

**************************
> 初始化新项目  [Doc:building java application](https://guides.gradle.org/building-java-applications/) 或者直接使用 gradle init 交互式新建一个项目

********************************

### SourceSet
> [SourceSet](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.SourceSet.html)

```groovy
    sourceSets{
        main{
            proto{
                srcDir 'proto/proto'
            }
            java{
                srcDir 'out/build/generated/main'
            }
        }
    }
```
***************

### 依赖管理
和Maven用的是同一种方式: groupId artifactId version 

> 注意: Java项目中 compile 在 Gradle 已弃用, 取而代之的是新增的多种定义方式 implementation api 等等  
> 明确了各种定义方式在项目中依赖的范围, 看起来更完美, 但是复杂度大大提高了

所以依据个人使用爱好, 简单易用就 compile testCompile 到底, 强迫症就 好好看官方文档 所有定义方式过一遍....

在定义项目时
- 可以直接使用简单原始的 [Java plugin](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_plugin_and_dependency_management)

- 也可以根据使用场景的不同使用不同的方案 [Building Java & JVM projects](https://docs.gradle.org/5.2/userguide/building_java_projects.html)
    1. `Java libraries` 适用于: Java 库. 
    1. `Java applications` 适用于: 可执行jar
    1. `Java web applications` 适用于: Java Web项目, 打包成 war
    1. `Java EE applications` 适用于: Java EE, 打包成 ear
    1. `Java Platforms` 适用于: Java套件, 本身不包含任何代码, 只是一组依赖的聚合

***************
> Java

`implementation`  
Gradle 中取代 compile 的方式, 使用范围比 compile 略小, 比如
- B 项目中定义依赖: implementation A
- C 项目中定义依赖: implementation B

此时 C 项目不能在代码中使用 A 中的类, 因为在 C 项目中 A 是声明为 runtime的, 也就是只在运行时会用到  
如果 B 使用的 compile, 那么 C 就能直接访问 A 中的类, 但是这是官方不推荐的

******************

> Java Libraries  

`新增了 api 等定义方式`  [Java Library plugin](https://docs.gradle.org/current/userguide/java_library_plugin.html#sec:java_library_configurations_graph)

`api`
使用这种方式就可以更好的实现上文的需求, B 项目会被引用, 那么他就应该是一个库, 所以要考虑到 B 依赖的项目 是否也会被引用
- B 项目中定义依赖: api A 

C 项目就能使用 A 中的类了

***************

> Java applications

就是 Java 上加上了 MainClass 的配置, 使得打包的jar包可执行

************************

> 其他依赖方式: 

1. 使用本地jar依赖 `implementation files('lib/ojdbc-14.jar')`  lib 与 src 为同级目录  
1. 项目间依赖 `implementation project(':projectName')`
1. 本地目录依赖
    ```groovy
    repositories {
        flatDir {
            dirs 'libs'
        }
    }
    ```

*********************

#### 依赖排除以及指定依赖版本

1. 在 configuration 中排除 
```groovy
    configurations {
        compile.exclude module: 'commons'
        all*.exclude group: 'org.gradle.test.excludes', module: 'reports'
    }
```
1. 在具体的某个dependency中排除
```groovy
    dependencies{
        // 依赖排除
        compile(''){
            exclude group: '' // 按group排除
            exclude module: '' // 按 artifact 排除
            exclude grop: '', module: '' // 按 group artifact 排除
        }
        // 全局依赖排除
        all*.exclude group:'org.unwanted', module: 'iAmBuggy'

        // 禁用依赖传递
        compile('com.zhyea:ar4j:1.0') {
            transitive = false
        }
        
        configurations.all {
            transitive = false
        }

        // 强制使用指定版本的依赖
        compile('com.zhyea:ar4j:1.0') {
            force = true
        }
        // 始终使用最新的依赖,  若 1.+ 则是 1.xx版本的最新版
        compile 'com.zhyea:ar4j:+'
        
        configurations.all {
            resolutionStrategy {
                force 'org.hamcrest:hamcrest-core:1.3'
            }
        }
    }
```
******************

#### 统一管理依赖
> [完整示例 JavaBase](https://github.com/Kuangcp/JavaBase)

1. 新建一个文件 _dependency.gradle_
    ```groovy
        rootProject.ext {
            ver = [
                junit     : '4.12',
            ]
            libs = [
                "junit"   : "junit:junit:$rootProject.ver.junit",
            ]
        }
    ```
1. 在 build.gradle 中引入 `apply from: 'dependency.gradle'`
1. 使用依赖时 只需 `implementation rootProject.libs['junit']` 即使在子模块中也是如此使用

###  配置镜像源
**阿里云**
> [参考: 配置Gradle的镜像为阿里云镜像](https://tvzr.com/change-the-mirror-of-gradle-to-aliyun.html)

> **当前项目的build.gradle**
```Groovy
  repositories {
    mavenLocal()
    def aliyun = "http://maven.aliyun.com/nexus/content/groups/public/"
    def abroad = "http://central.maven.org/maven2/"
    maven {
      url = aliyun
      artifactUrls abroad
    }
    // 码云上自己的仓库
    maven {
      url = "https://gitee.com/gin9/MavenRepos/raw/master"
    }
    mavenCentral()
    jcenter()
  }
```

### 插件
> 引入一个插件有多种方式

```groovy
    // 1
    apply plugin: 'java'
    // 2
    apply{
        'java'
    }
    // 3 Gradle5 推荐
    plugins{
        id 'java'
    }
```

#### Lombok
> [详细](/Java/Tool/Lombok.md)

#### Maven Publish
- [Maven Publish Plugin](https://docs.gradle.org/current/userguide/publishing_maven.html)

#### shadowJar 
> 打包为 fat jar 也就是包含所有依赖jar的jar包

#### docker
> 提供Docker 的 API
1. 引入 `apply plugin: 'docker'`
    - buildscript dependencies 中添加`classpath('se.transmode.gradle:gradle-docker:1.2')`

#### protobuf-gradle-plugin
> [Github: protobuf-gradle-plugin](https://github.com/google/protobuf-gradle-plugin)

## setting.gradle
> 项目的配置信息, 一般存在这个文件的时候, Gradle就会认为当前目录是作为一个完整的根项目的, 并在当前目录添加 .gradle 目录  

- 必须: `rootProject.name = '项目名'`
- 配置子项目 `include('A','B')`

***************

# Gradle多模块的构建
> [Official Doc: creating multi project builds ](https://guides.gradle.org/creating-multi-project-builds/)

> 手动增加一个子项目
1. mkdir test
1. gradle init 然后删除自动创建的 setting.gradle 
1. setting.gradle 中的include 加入 test(项目名不是目录名)

**********************************

## 另一种多模块的构建方式
> [参考博客:重拾后端之Spring Boot（六） -- 热加载、容器和多项目](https://www.jianshu.com/p/ac4c00a63750)  
> 全部在父项目`build.gradle`中配置 

```groovy
    // 一个典型的根项目的构建文件结构
    buildscript {
        //  构建脚本段落可以配置整个项目需要的插件，构建过程中的依赖以及依赖类库的版本号等
    }
    allprojects {
        //  在这个段落中你可以声明对于所有项目（含根项目）都适用的配置，比如依赖性的仓储等
    }
    subprojects {
        //  * 在这个段落中你可以声明适用于各子项目的配置（不包括根项目哦）
        version = "0.0.1"
    }
    //  * 对于子项目的特殊配置
    project(':common') {}
    project(':api') {}
    project(':report') {}
```

```groovy
    project(':common') {
        dependencies {
            compile("org.springframework.boot:spring-boot-starter-data-rest")
            compile("org.springframework.boot:spring-boot-starter-data-mongodb")
            compile("org.projectlombok:lombok:${lombokVersion}")
        }
    }

    project(':api') {
        dependencies {
            compile project(':common')
            compile("org.springframework.boot:spring-boot-devtools")
        }
    }

    project(':report') {
        dependencies {
            compile project(':common')
            compile("org.springframework.boot:spring-boot-devtools")
            compile files(["lib/simsun.jar"])
            compile("org.springframework.boot:spring-boot-starter-web")
        }
    }
```

- [有关多模块的构建详情参考这里](https://github.com/Kuangcp/GradleIntegrationMultipleModules)
- [参考更为规范的多项目构建](https://github.com/someok/gradle-multi-project-example)

******************************************************
# 使用
## 安装到本地仓库
> 含源码 类似Maven的 install 或 deploy [The Maven Publish Plugin](https://docs.gradle.org/current/userguide/publishing_maven.html)

```groovy
    apply plugin: "maven-publish"

    // publish with source code
    task sourceJar(type: Jar) {
        from sourceSets.main.allJava
    }
    publishing {
        publications {
            mavenJava(MavenPublication) {
                from components.java
                artifact sourceJar {
                    classifier "sources"
                }
            }
        }
    }
```

> `gradle publishToMavenLocal`

## 上传至构件仓库
> [Official Doc](https://docs.gradle.org/current/userguide/publishing_overview.html)

> 特别注意使用gpg, 如果按这下面的一堆文档跟着做的话你要保证你的gpg小于等于2.0版本, 不然就卡在这里了

> [参考项目 ](https://github.com/haiyangwu/sonatype)
> [参考](https://www.jianshu.com/p/49c926589f41)
> [官方文档](http://central.sonatype.org/pages/gradle.html)
> [参考博客](http://blog.csdn.net/h3243212/article/details/72374363#%E9%81%87%E5%88%B0%E7%9A%84%E9%97%AE%E9%A2%98)
> [最简单的方式就是利用码云等平台创建私服 ](https://blog.csdn.net/kcp606/article/details/79675590)

************************

# 打包部署
> [参考: Building Java Applications](https://guides.gradle.org/building-java-applications/)

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
- Gradle默认是只会打包源码，并不会打包依赖

> 原生方式打包含依赖的Jar,并设置mainClass
```groovy
    task uberJar(type: Jar) {
        archiveClassifier = 'all-dependency'

        from sourceSets.main.output

        dependsOn configurations.runtimeClasspath
        from {
            configurations.runtimeClasspath.findAll { it.name.endsWith('jar') }.collect { zipTree(it) }
        }

        manifest {
            attributes 'Main-Class': 'com.xxx.Main'
        }
    }
```

> 通过插件
- [shadow插件官网文档](http://imperceptiblethoughts.com/shadow/)

## 构建Docker镜像
> [用 Docker、Gradle 来构建、运行、发布一个 Spring Boot 应用](http://www.importnew.com/24671.html)

_build.gradle_
```groovy
    apply plugin: 'docker'
    buildscript {
        ext {
            springBootVersion = '2.0.1.RELEASE'
        }
        repositories {
            mavenCentral()
        }
        dependencies {
            classpath("org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}")
            classpath('se.transmode.gradle:gradle-docker:1.2')
        }
    }
    task buildDocker(type: Docker, dependsOn: build) {
        //设置自动上传的话，命名就不能乱取了，仓库名/镜像名：tag
    //    push = true
        test.enabled=false
        applicationName = jar.baseName
        dockerfile = file('src/main/docker/Dockerfile')
        doFirst {
            copy {
                from war
                into stageDir
            }
        }
    }
```

_Dockerfile_
```dockerfile
    FROM frolvlad/alpine-oraclejdk8:slim
    VOLUME /tmp
    # 配置通配符是为了不受版本影响
    ADD weixin*.war app.war
    # ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.war"]
    ENTRYPOINT ["java","-jar","/app.war"]
```
- `gradle buildDocker` 即可构建镜像
- 运行 `docker run --name web --link postgre:db -p 5678:8889 -it 镜像` 注意其中要关联PostgreSQL的容器

### 插件方式构建Docker镜像
> [参考  通过Gradle使用Docker部署 Spring Boot项目](https://www.jianshu.com/p/7571fa3b394c)

