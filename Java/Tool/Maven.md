`目录 start`
 
- [Maven](#maven)
    - [1.安装](#1安装)
        - [1.1.Maven常用命令](#11maven常用命令)
            - [从jar安装到本地库](#从jar安装到本地库)
        - [1.2.settings.xml配置](#12settingsxml配置)
            - [配置镜像源](#配置镜像源)
                - [阿里云](#阿里云)
            - [配置本地仓库](#配置本地仓库)
    - [2.maven配置](#2maven配置)
        - [2.1.eclipse中配置](#21eclipse中配置)
        - [2.2.配置插件](#22配置插件)
        - [2.3.POM配置文件详解](#23pom配置文件详解)
        - [2.4.配置代码编译版本](#24配置代码编译版本)
    - [3.构建](#3构建)
        - [3.1.使用maven构建多模块的项目](#31使用maven构建多模块的项目)
        - [3.2.Maven多配置环境](#32maven多配置环境)
        - [3.3.部署](#33部署)
    - [4.maven的依赖](#4maven的依赖)
        - [4.1 依赖的范围](#41-依赖的范围)
            - [依赖的传递](#依赖的传递)
        - [4.2.处理项目间依赖方法](#42处理项目间依赖方法)
        - [4.3.依赖冲突](#43依赖冲突)
            - [排除依赖](#排除依赖)
        - [4.4.继承](#44继承)
    - [5.使用maven新建Web3.0项目](#5使用maven新建web30项目)
        - [5.1.添加web容器](#51添加web容器)
            - [5.1.2.Jetty](#512jetty)
            - [5.1.3.Tomcat](#513tomcat)
        - [5.2.加入Servlet的API包](#52加入servlet的api包)
    - [6.常用插件](#6常用插件)
        - [6.1.lombok](#61lombok)
        - [6.2 protobuf](#62-protobuf)
    - [7.构建工具对比](#7构建工具对比)
        - [7.1.Maven和Ant的区别一](#71maven和ant的区别一)
        - [7.2.Maven的优势](#72maven的优势)
    - [8.发布构件](#8发布构件)
    - [9.配置私服](#9配置私服)
        - [nexus](#nexus)
        - [码云](#码云)
            - [创建仓库](#创建仓库)
            - [引用仓库中的构件](#引用仓库中的构件)
                - [Gradle](#gradle)
                - [Maven](#maven)

`目录 end` |_2018-08-14_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Maven
> [官网](https://maven.apache.org/) | [官网手册](https://maven.apache.org/guides/) | [http://takari.io/ 在线练习网](http://takari.io/)
> [关于Maven的完整博客](http://tengj.top/2018/01/01/maven/)

## 1.安装
* 下载zip包解压，将bin目录配置至PATH（最好是配置MAVEN_HOME然后引用）

### 1.1.Maven常用命令
> mvn [插件]:[目标] [参数]
> mvn [阶段]

* mvn archetype:generate ：创建 Maven 项目
    * -DgroupId=组织名/公司网址的反写+项目名
    * -DartifactId=项目名-模块名
    * -Dversion=版本号
    * -Dpackage=代码所在的包

- `compile` ：编译源代码
- `test-compile` ：编译测试代码
- `test` ： 运行应用程序中的单元测试
- `site` ： 生成项目相关信息的网站
- `clean` ：清除目标目录中的生成结果
- `package` ： 依据项目生成 jar 文件
- `install` ：在本地 Repository 中安装 jar
- `deploy`：将jar包发布到远程仓库
- 使用id为ChatServer的Profile `-PChatServer` 

- 跳过测试
    - `-Dmaven.test.skip=true` 不执行测试用例，也不编译测试用例类。
    - `-DskipTests=true` 不执行测试用例，但编译测试用例类生成相应的class文件至target/test-classes下
    - `-Dmaven.javadoc.skip=true` 跳过文档生成

_配置文件中配置_
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <skip>true</skip>
    </configuration>
</plugin>
```
#### 从jar安装到本地库
```
mvn install:install-file 
    -Dfile=D:\mvn\spring-context-support-3.1.0.RELEASE.jar \
    -DgroupId=org.springframework  \
    -DartifactId=spring-context-support \
    -Dversion=3.1.0.RELEASE \
    -Dpackaging=jar
```
*****
### 1.2.settings.xml配置
> 要特别注意 `settings.xml` 后者覆盖前者 加载顺序是: 
>> `maven目录/conf/setting.xml`  
>> `用户目录下/.m2/setting.xml` 

#### 配置镜像源
> 在 用户目录下 .m2/setttings.xml 中 找到 mirrors 标签 进行添加`mirror节点`即可

##### 阿里云

```xml
<mirror> 
    <id>alimaven</id> 
    <name>aliyun maven</name> 
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url> 
    <mirrorOf>central</mirrorOf> 
</mirror> 
```
#### 配置本地仓库
`localRepository节点`
*****************
## 2.maven配置
### 2.1.eclipse中配置
> 高版本自带maven，需要注意的是eclipse的JRE运行环境目录要选择jdk下的JRE目录

### 2.2.配置插件
> [插件地址](http://maven.apache.org/plugins/index.html)

### 2.3.POM配置文件详解
> [版本说明](http://www.blogjava.net/RomulusW/archive/2008/05/04/197985.html)

```xml
      <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
     <modelVersion>4.0.0</modelVersion>
     <groupId>反写的公司域名+项目名</groupId>
     <artifactId>项目名+模块名</artifactId>
     <!--
         第一个 0 是大版本号
         第二个 0 是分支版本号
         第三个 0 是小版本号
         snapshot 快照
         alpha 内部测试
         beta 公测
         RC 发行候选版本
         Release/GA 正式发布
     -->
     <version>0.0.1-SNAPSHOT</version>
     <!--jar war zip pom-->
     <packaging>jar</packaging>
     <!--项目描述名-->
     <name>test</name>
     <!--项目地址-->
     <url>http://maven.apache.org</url>
     <!--项目描述-->
     <description></description>
     <developers></developers>
     <licenses></licenses>
     <orgnazation></orgnazation>

    <!-- 配置属性 -->
    <properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <!-- 统一定义版本 -->
        <springframework.version>1.5.6</springframework.version>
	</properties>
     <!--依赖-->
     <dependencies>
       <dependency>
         <groupId>junit</groupId>
         <artifactId>junit</artifactId>
         <version>3.8.1</version>
         <!--
            test 表明这个构件只在test目录下可以被引用
            compile 默认的
            provided 只在编译中引用
            runtime 编译和运行都有效
         -->
         <scope>test</scope>
         <!--设置依赖是否可选，默认是false-->
         <optional></optional>
         <!--排除依赖传递列表-->
         <exclusions></exclusions>
       </dependency>
     </dependencies>
     <dependencyManagement>
     </dependencyManagement>
     <build>
      <plugins>
         <!-- 构件三要素 -->
      </plugins>
     </build>
     <!--继承-->
     <parent></parent>
     <modules>
         <module></module>
     </modules>
```

### 2.4.配置代码编译版本
```xml
<build>
    <plugins>
        <plugin>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.1</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

## 3.构建
### 3.1.使用maven构建多模块的项目
`.gitignore文件`
```
    .idea/
    *.iml
    target/
    *.log 
```
`父项目pom文件`
``` xml
    <groupId>com.github.kuangcp</groupId>
    <artifactId>Modules</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>repository</module>
        <module>service</module>
        <module>website</module>
    </modules>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <java.version>1.8</java.version>
    </properties>
```
`子项目pom文件`
```xml
    <artifactId>website</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>
    <parent>
        <groupId>com.github.kuangcp</groupId>
        <artifactId>Modules</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
```
### 3.2.Maven多配置环境
> [Maven 如何为不同的环境打包](https://www.zybuluo.com/haokuixi/note/25985) `开发、测试和产品环境`

- [ ] 子项目编译打包各自独立，怎么整合成一个

### 3.3.部署
> [Java项目部署方式整理](/Java/AdvancedLearning/Deploy.md)

******************
## 4.maven的依赖
### 4.1 依赖的范围
> 依赖范围就是用来控制依赖和三种classpath(编译classpath，测试classpath、运行classpath)的关系

- `compile`:编译依赖范围。如果没有指定，就会默认使用该依赖范围。使用此依赖范围的Maven依赖，对于编译、测试、运行三种classpath都有效。
    - 典型的例子是spring-core,在编译、测试和运行的时候都需要使用该依赖。
- `test`: 测试依赖范围。使用次依赖范围的Maven依赖，只对于测试classpath有效
    - 在编译主代码或者运行项目的使用时将无法使用此依赖。典型的例子是Jnuit,它只有在编译测试代码及运行测试的时候才需要。
- `provided`:已提供依赖范围。使用此依赖范围的Maven依赖，对于编译和测试classpath有效，但在运行时候无效。
    - 典型的例子是servlet-api,编译和测试项目的时候需要该依赖，但在运行项目的时候，由于容器以及提供，就不需要Maven重复地引入一遍。
- `runtime`:运行时依赖范围。使用此依赖范围的Maven依赖，对于测试和运行classpath有效，但在编译主代码时无效。
    - 典型的例子是JDBC驱动实现，项目主代码的编译只需要JDK提供的JDBC接口，只有在执行测试或者运行项目的时候才需要实现上述接口的具体JDBC驱动。

| 依赖范围 Scope | 对于编译classpath | 对于测试classpath | 对于运行classpath | Demo | 
|:----:|:----:|:----:|:----:|:----:|
| compile | Y | Y | Y | spring-boot-starter-web |
| test |  | Y |  | Junit |
| provided | Y | Y |  | servlet-api |
| runtime |  | Y | Y | JDBC的实现Jar |
| system | Y | Y |  | Maven仓库之外的类库文件 |

#### 依赖的传递
- 比如一个account-email项目为例
    - account-email有一个compile范围的spring-code依赖，
    - spring-core有一个compile范围的commons-logging依赖，
- 那么commons-logging就会成为account-email的compile的范围依赖，commons-logging是account-email的一个传递性依赖

### 4.2.处理项目间依赖方法
```
项目A依赖B
A项目 pom.xml中配置依赖 （构件三要素）
B项目 先clean package
      然后build 的 install
A 项目 compile
```

### 4.3.依赖冲突
- 依赖路径短优先
   - 1 A->B->C->X(jar文件)
   - 2 A->C->X(jar文件)
   - 会选择 2 中的X的jar版本
- 先声明的优先

#### 排除依赖
`对应的<dependency>标签中添加`
```xml
<exclusions>
    <exclusion>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-logging</artifactId>
    </exclusion>
</exclusions>
```

### 4.4.继承
> 新建一个项目作为父项目  
> 然后在需要引用父项目的子项目pom文件中, 加上parent 标签里面写上 父项目的三要素

*************************
## 5.使用maven新建Web3.0项目
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

### 5.1.添加web容器
#### 5.1.2.Jetty
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

#### 5.1.3.Tomcat
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

### 5.2.加入Servlet的API包
```xml
    <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <version>3.0.1</version>
        <scope>provided</scope>
	</dependency>
```

## 6.常用插件
### 6.1.lombok
> 极大的简化了bean的代码量

```xml
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <version>1.16.10</version>
        <scope>provided</scope>
    </dependency>
```

### 6.2 protobuf
> [maven 插件 ](https://www.xolstice.org/protobuf-maven-plugin/) `本质还是要使用系统安装的protoc, 然后插件实现了自动编译文件`

****************************

## 7.构建工具对比
> [码农翻身:小李的Build之路(上)](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513207&idx=1&sn=cbfad70e656fc50c4fff18678a282b95&scene=21#wechat_redirect) | [码农翻身:小李的Build之路(下)](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513212&idx=1&sn=280647b0c6cd265f85590f64d3216bee&scene=21#wechat_redirect) `这个小故事讲述了ant到maven的演化`

### 7.1.Maven和Ant的区别一

1. ant脚本是可以直接运行在maven中的。maven和ant最大的差别就是在于maven的编译以及所有的脚本都有一个基础，就是POM（project object model）。这个模型定义了项目的方方面面，然后各式各样的脚本在这个模型上工作，而ant完全是自己定义，显然maven更胜一筹。

2. maven对所依赖的包有明确的定义，如使用那个包，版本是多少，一目了然。而ant则通常是简单的inclde 所有的jar。导致的最终结果就是，你根本无法确定JBoss中的lib下的common－logging 是哪个版本的，唯一的方法就是打开 META－INF 目录下MANIFEST.MF。

3. maven是基于中央仓库的编译，即把编译所需要的资源放在一个中央仓库里，如jar，tld，pom，等。当编译的时候，maven会自动在仓库中找到相应的包，如果本地仓库没有，则从设定好的远程仓库中下载到本地。这一切都是自动的，而ant需要自己定义了。这个好处导致的结果就是，用maven编译的项目在发布的时候只需要发布源码，小得很，而反之，ant的发布则要把所有的包一起发布，显然maven又胜了一筹。

4. maven有大量的重用脚本可以利用，如生成网站，生成javadoc，sourcecode reference，等。而ant都需要自己去写。

5. maven目前不足的地方就是没有象ant那样成熟的GUI界面，不过mavengui正在努力中。目前使用maven最好的方法还是命令行，又快又方便

### 7.2.Maven的优势

- 协同开发的基本规范，为大家提供方便的协作的模式，能增加代码的复用，提高生产率。
- 提供方便，规范化的打包方法，是公司完成自动构建系统的核心部分，能帮助提高敏捷开发的效率(敏捷开发提倡尽早集成)。
- 减少冗余，减少出错的可能。
- 中心资源库管理，能减低源码库的大小，中心资源库可以统一定期备份。
- 目录结构规范，让开发者从一个maven项目过度到另一maven项目很容易。
- 大量的开源项目使用了maven。

********************
## 8.发布构件到公共仓库
- [ ] Jforg mvnrepository 

> [将项目发布到 maven 中央仓库踩过的坑](http://blog.csdn.net/h3243212/article/details/72374363)

> [发布Maven构件到中央仓库](https://www.xncoding.com/2018/01/27/tool/maven-central.html)

*********************
## 9.配置私服
> 不用去跑审核流程, 私有, 快速, 便捷
### nexus
> 需要运行软件, 一般公司内部局域网使用, 如果自己有服务器也能开放给公众使用 [参考博客: maven私服搭建及gradle上传](https://www.jianshu.com/p/b1fe26d5b8c8)

### 码云
> 利用公开仓库来搭建私服 | [参考博客:  使用git仓库搭建maven私服 ](https://my.oschina.net/polly/blog/1649362)
#### 创建仓库
> 当然了在各个托管平台都可以的, 只不过码云是国内的, 毕竟要快 github gitlab bitbucket 就....

1. 创建好一个空的公开仓库
2. 使用统一的groupId, 这样就会放到默认目录 `~/.m2/repository/` 下 只要在groupId对应的目录下 git init
3. 只需在项目中执行install, 然后在此目录进行提交即可

#### 引用仓库中的构件
##### Gradle
build.gradle 中添加
```groovy
repositories {
    maven{
        url "https://gitee.com/你的用户名/创建的仓库/raw/master"
    }
}
```
##### Maven
pom.xml中添加
```xml
<repositories>
  <repository>
    <id>mvnrepo</id>
    <name>mvn repository</name>
    <url>https://gitee.com/用户名/仓库/raw/master</url>
  </repository>
</repositories>
```
