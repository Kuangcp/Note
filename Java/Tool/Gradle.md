`目录 start`
 
- [Gradle](#gradle)
    - [书籍](#书籍)
    - [发行版本列表](#发行版本列表)
    - [安装配置](#安装配置)
        - [SDKMAN方式](#sdkman方式)
        - [Chocolate](#chocolate)
        - [命令行选项](#命令行选项)
        - [守护进程](#守护进程)
        - [Docker安装](#docker安装)
    - [配置镜像源](#配置镜像源)
- [关键配置文件](#关键配置文件)
    - [build.gradle](#buildgradle)
        - [初始化一个新项目](#初始化一个新项目)
        - [dependency](#dependency)
        - [统一依赖管理](#统一依赖管理)
        - [配置Wrapper](#配置wrapper)
        - [插件](#插件)
            - [常用插件](#常用插件)
    - [setting.gradle](#settinggradle)
        - [Gradle多模块的构建](#gradle多模块的构建)
            - [另一种方式](#另一种方式)
- [部署](#部署)
    - [War包](#war包)
    - [Jar包](#jar包)
    - [上传至构建仓库](#上传至构建仓库)
    - [构建Docker镜像](#构建docker镜像)
        - [第二种插件方式](#第二种插件方式)

`目录 end` |_2018-09-09_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Gradle
> [官方 guide](https://gradle.org/guides/?q=JVM) | [其他 tutorial](https://www.tutorialspoint.com/gradle/index.htm)  
> [参考博客: 零散知识点总结(1) - Gradle 使用配置总结](https://www.jianshu.com/p/47cbbb4eab13)

**个人看法**
> [参考: Gradle在大型Java项目上的应用](www.infoq.com/cn/articles/Gradle-application-in-large-Java-projects)

**优缺点**
> [Gradle大吐槽](https://blog.csdn.net/MCL529/article/details/79341706)
> [官方对比Gradle和Maven](https://gradle.org/maven-vs-gradle/)

> 优点  
1. 相对于Maven, 配置文件简洁了很多, 所以才入坑学习使用的
2. 对于一些需要自定义的任务,因为核心为Groovy,所以实现能力高
	- 例如:将一个SpringBoot项目构建成一个镜像,并tag上当前构建的镜像为release,然后删除旧有容器,使用新的镜像启动容器

> 缺点  
1. 内存占用巨大,存在内存泄露问题, 以至于在IDEA上不敢使用自动导入, 不然每动一下build.gradle 就会卡半天, 8G内存都不够用!!
2. 编译速度慢, 如果和Maven进行对比, 编译速度和资源占用确实慢

********************
## 书籍
> [Gradle in Action 中译](http://www.jb51.net/books/527811.html) `如果没有一点Groovy基础, 阅读自定义Task等一些高自定义的地方还是比较困惑`

## 发行版本列表
> [官方网址](http://services.gradle.org/) 有各个版本的下载以及版本发行说明
> [Github地址](https://github.com/gradle/gradle/releases)`查看简洁的 Release Note 更方便`

## 安装配置
> 和maven使用同一个本地库 只要加上 M2_HOME 环境变量即可, 值和 MAVEN_HOME 一样, 并没有用

### SDKMAN方式
- 先安装sdkman
- 使用Bash运行`curl -s "https://get.sdkman.io" | bash`
- `sdk install gradle` 即可安装

### Chocolate
- windows 上安装 chocolate
- PowerShell中运行 `wr https://chocolatey.org/install.ps1 -UseBasicParsing | iex`
- 若操作系统默认禁止执行脚本，执行一次`set-executionpolicy remotesigned`后脚本顺利执行
- Chocolatey在安装包的时候，默认路径是按照系统的默认路径来的，如果想修改安装路径可以这样处理：
1. 执行“开始/运行”命令（或者WIN + R），输入“regedit”，打开注册表。
2. 展开注册表到下面的分支[HKEY＿LOCAL＿MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion]，在右侧窗口中找到名为“ProgramFilesDir”的字符串，双击把数值“C:\Program Files”修改为“D：\ProgramFiles”，确定退出后,即可更改常用软件的安装路径了。

### 命令行选项
- `gradle 构建文件中的task名`： 直接运行task
- `-b，--build-file test.gradle` 指定运行脚本文件
- `--offline` 离线模式
- `-P ,--project-prop`:配置参数 -Pmyprop=value
- `-i,--info` : 打印info级别的输出
- `-s,--stacktrace`: 输出错误栈
- `-q,--quiet`:减少构建出错时打印的错误信息
- `tasks` : 输出所有建立的task
- `properties` : 输出所有可用的配置属性

### 守护进程
- 命令加上 `--daemon`就会开启一个守护进程，只会开启一次，
- 守护进程会在空闲3小时后销毁
- 手动关闭 `gadle --stop `
- 构建时不采用守护进程 `--no--daemon`

### Docker安装
> [Docker 文档](https://docs.docker.com/samples/library/gradle/)

****************************
## 配置镜像源
**阿里云**
> [参考博客: 配置Gradle的镜像为阿里云镜像](https://tvzr.com/change-the-mirror-of-gradle-to-aliyun.html)

_当前项目的build.gradle_
```Groovy
  repositories {
    def aliyun = "http://maven.aliyun.com/nexus/content/groups/public/"
    def abroad = "http://central.maven.org/maven2/"
    maven {
      url = aliyun
      artifactUrls abroad
    }
    // 马云上自己的库
    maven {
      url = "https://gitee.com/gin9/MavenRepos/raw/master"
    }
    mavenCentral()
    jcenter()
  }
```
**全局的配置**
_~/.gradle/init.gradle_
```Groovy
allprojects{
    repositories {
        def ALIYUN_REPOSITORY_URL = 'http://maven.aliyun.com/nexus/content/groups/public'
        def ALIYUN_JCENTER_URL = 'http://maven.aliyun.com/nexus/content/repositories/jcenter'
        all { ArtifactRepository repo ->
            if(repo instanceof MavenArtifactRepository){
                def url = repo.url.toString()
                if (url.startsWith('https://repo1.maven.org/maven2')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_REPOSITORY_URL."
                    remove repo
                }
                if (url.startsWith('https://jcenter.bintray.com/')) {
                    project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_JCENTER_URL."
                    remove repo
                }
            }
        }
        maven {
        	url ALIYUN_REPOSITORY_URL
            url ALIYUN_JCENTER_URL
        }
    }
}
```
************************

# 关键配置文件
## build.gradle
_Hello World_
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
-  运行：`gradle -q helloworld`

### 初始化一个新项目
> [doc:building java application](https://guides.gradle.org/building-java-applications/)

### dependency
- 和Maven用的是同一种方式 groupId artifactId version 
- 使用本地依赖 `compile files('lib/ojdbc-14.jar')` 相对的根目录是src同级目录

[Official doc: dependency management](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_plugin_and_dependency_management)

> 4.10  Deprecated: `compile runtime testCompile testRuntime`

- `compile(Deprecated)`
  - Compile time dependencies. Superseded by implementation.

- `implementation extends compile`
    - Implementation only dependencies.

- `compileOnly`
    - Compile time only dependencies, not used at runtime.

- `compileClasspath extends compile, compileOnly, implementation`
    - Compile classpath, used when compiling source. Used by task compileJava.

- `annotationProcessor`
    - Annotation processors used during compilation.

- `runtime(Deprecated) extends compile`
    - Runtime dependencies. Superseded by runtimeOnly.

- `runtimeOnly`
    - Runtime only dependencies.

- `runtimeClasspath extends runtimeOnly, runtime, implementation`
    - Runtime classpath contains elements of the implementation, as well as runtime only elements.

- `testCompile(Deprecated) extends compile`
    - Additional dependencies for compiling tests. Superseded by testImplementation.

- `testImplementation extends testCompile, implementation`
    - Implementation only dependencies for tests.

- `testCompileOnly`
    - Additional dependencies only for compiling tests, not used at runtime.

- `testCompileClasspath extends testCompile, testCompileOnly, testImplementation`
    - Test compile classpath, used when compiling test sources. Used by task compileTestJava.

- `testRuntime(Deprecated) extends runtime, testCompile`
    - Additional dependencies for running tests only. Used by task test. Superseded by testRuntimeOnly.

- `testRuntimeOnly extends runtimeOnly`
    - Runtime only dependencies for running tests. Used by task test.

- `testRuntimeClasspath extends testRuntimeOnly, testRuntime, testImplementation`
    - Runtime classpath for running tests.

- `archives`
    - Artifacts (e.g. jars) produced by this project. Used by tasks uploadArchives.

- `default extends runtime`
    - The default configuration used by a project dependency on this project. Contains the artifacts - and dependencies required by this project at runtime.




### 统一依赖管理
新建一个文件 _dependency.gradle_
```groovy
    ext {
        ver = [
            junit     : '4.12',
        ]
        libs = [
            "junit"   : "junit:junit:$ver.junit",
        ]
    }
```
- 在 build.gradle 中引入 `apply from: 'dependency.gradle'`
- 使用依赖时 只需 `compile libs['junit']` 即使在子模块中也是如此使用


### 配置Wrapper
> 在使用IDE生成项目的时候，可以选择gradle的执行目录，可以选`gradle wrapper` 也可以选自己下载解压的完整包
> 如果使用的不是这个wrapper，那么别人在下载项目后，运行gradle命令就要先安装gradle，使用wrapper更好
```groovy
   task wrapper(type: Wrapper){
      gradleVersion = '4.8'
      distributionUrl = '限定访问内网的URL'
      distributionPath = '包装器被解压缩放的相对路径'
   }
```
- 运行 gradle wrapper 一次即可开始使用包装器的脚本来构建项目了
- 生成gradle包管理器：`gradle wrapper --gradle-version 2.0`

### 插件
有多种方式:

```groovy
// 1
apply plugin: 'java'
// 2
apply{
    'java'
}
// 3
plugins{
    id 'java'
}
```
#### 常用插件
- lombok
> [使用Lombok的正确方式](https://stackoverflow.com/questions/50519138/annotationprocessor-gradle-4-7-configuration-doesnt-run-lombok) | [gradle lombok plugin](https://projectlombok.org/setup/gradle)

[官方文档](https://docs.gradle.org/4.7-rc-1/userguide/java_plugin.html#sec:java_compile_avoidance)
```groovy
  annotationProcessor 'org.projectlombok:lombok:1.18.2'
  compileOnly 'org.projectlombok:lombok:1.18.2'
  testAnnotationProcessor 'org.projectlombok:lombok:1.18.2'
  testCompileOnly 'org.projectlombok:lombok:1.18.2'
```

***************

- maven 
    - `apply plugin: "maven"` 然后就能执行 install等命令了
    - gradle 4.8 用不了 [需要这种方式](https://blog.csdn.net/mxw2552261/article/details/78640338)

- shadowJar 含依赖的jar进行打包

- docker 提供Docker操作
    - `apply plugin: 'docker'`
    - buildscript dependencies 中添加`classpath('se.transmode.gradle:gradle-docker:1.2')`

****************
## setting.gradle
> 项目的配置信息, 一般存在这个文件的时候, Gradle就会认为当前目录是作为一个完整的根项目的, 并在当前目录添加 .gradle 目录  
> 一般默认内容为 `rootProject.name = ''`

### Gradle多模块的构建
> [官网文档 creating multi project builds ](https://guides.gradle.org/creating-multi-project-builds/)

> 采用一个文件统一管理依赖, 然后各个子项目独立引用 | [完整示例 JavaBase](https://github.com/Kuangcp/JavaBase)`统一配置依赖, 管理多模块` 

_如果要添加一个项目也简单_
1. 直接新建一个目录 test
1. 目录下新建空的文件 build.gradle
1. 在根项目的 setting.gradle 中的include 加入 test (可以和文件夹不同名, build.gradle配置下就行了, 建议同名)
1. gradle build 整个项目, 就完成了
1. 最后就是手动的新建项目结构

**********************************
#### 另一种方式
> [参考博客:重拾后端之Spring Boot（六） -- 热加载、容器和多项目](https://www.jianshu.com/p/ac4c00a63750)
> 直接在build.gradle中配置 

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
    project(':common') {
    }
    project(':api') {
    }
    project(':report') {
    }
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
# 部署
## War包

## Jar包
- Gradle默认是只会打包源码，并不会打包依赖（为了更方便依赖的作用）
    - [shadow插件官网文档](http://imperceptiblethoughts.com/shadow/)
- 添加 `apply plugin: "maven"` 然后就能和mvn install 一样的执行 gradle install 了

## 上传至构建仓库
> 特别注意使用gpg, 如果按这下面的一堆文档跟着做的话你要保证你的gpg小于等于2.0版本, 不然就卡在这里了

> [参考项目 ](https://github.com/haiyangwu/sonatype)
> [参考](https://www.jianshu.com/p/49c926589f41)
> [官方文档](http://central.sonatype.org/pages/gradle.html)
> [参考博客](http://blog.csdn.net/h3243212/article/details/72374363#%E9%81%87%E5%88%B0%E7%9A%84%E9%97%AE%E9%A2%98)
> [最简单的方式就是利用码云等平台创建私服 ](https://blog.csdn.net/kcp606/article/details/79675590)

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

### 第二种插件方式
> [参考  通过Gradle使用Docker部署 Spring Boot项目](https://www.jianshu.com/p/7571fa3b394c)

