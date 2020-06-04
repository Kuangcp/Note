---
title: Gradle进阶
date: 2018-12-11 21:29:29
tags: 
    - Gradle
    - Advanced
categories: 
    - Java
---

**目录 start**

1. [Gradle进阶知识](#gradle进阶知识)
    1. [Gradle 使用和配置](#gradle-使用和配置)
        1. [主配置目录](#主配置目录)
    1. [Gradle 构建块](#gradle-构建块)
    1. [task](#task)
        1. [task的依赖关系](#task的依赖关系)
        1. [终结器 task](#终结器-task)
        1. [Groovy的POGO类管理配置文件上的版本号](#groovy的pogo类管理配置文件上的版本号)
        1. [task 的inputs 和 outputs](#task-的inputs-和-outputs)
        1. [编写和使用自定义task](#编写和使用自定义task)
            1. [声明task规则](#声明task规则)
    1. [增量式构建特性](#增量式构建特性)
1. [测试模块](#测试模块)
    1. [单元测试](#单元测试)
        1. [使用JUnit](#使用junit)
        1. [使用其他框架 TestNG Spock](#使用其他框架-testng-spock)
    1. [配置测试执行](#配置测试执行)
1. [多语言编程](#多语言编程)
    1. [处理javascript](#处理javascript)
        1. [压缩javascript](#压缩javascript)
        1. [Java 和 Groovy的联合编译](#java-和-groovy的联合编译)
        1. [Java 和 Scala](#java-和-scala)
    1. [Jenkin 使用](#jenkin-使用)
        1. [下载安装和配置](#下载安装和配置)
1. [发布自己的构件](#发布自己的构件)

**目录 end**|_2020-06-04 19:41_|
****************************************
# Gradle进阶知识
> [gradle api ](https://docs.gradle.org/4.9/dsl/org.gradle.api.Project.html) `所有{}结构 以及配置`

> [davenkin的学习仓库](https://github.com/davenkin/gradle-learning)
> [个人学习Gradle的记录仓库](https://github.com/Kuangcp/LearnGradle)

## Gradle 使用和配置
### 主配置目录
> ~/.gradle

```
├── caches
│   ├── 4.8
│   ├── 4.9
│   ├── jars-3
│   ├── modules-2
│   │   ├── files-2.1 依赖的Jar 缓存目录
│   │   ├── metadata-2.58
│   │   └── modules-2.lock
│   └── transforms-1
├── daemon
│   ├── 4.8
│   └── 4.9
├── native
│   ├── 25
│   └── jansi
├── notifications
│   ├── 4.8
│   └── 4.9
└── workers
```
> ~/.gradle/caches/modules-2/files-2.1 等价于Maven的 ~/.m2/repository 目录  
> 不得不说, 这个目录很丑, 字母加字符短杠..强迫症很难受

- 那么问题来了, 以前一直以为是和Maven共用一个仓库
    - 他和Maven本地仓库没有半毛钱关系, 他只是去复制了一下而已! [详情](https://blog.csdn.net/kcp606/article/details/81636426)

## Gradle 构建块
- 三个基本块 project task property， 使用DDD（领域驱动设计）
- 一个真实的项目包含多个project 而 Project又包含多个task ，task之间通过依赖来确保执行顺序
- build.gradle 和 pom.xml 作用是一致的，但是gradle可以使用一份源码 构建出多种想要的目标程序

## task
- [doc:task](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html)

### task的依赖关系
```groovy
   version = '0.1-SNAPSHOT'
   task first {
   	println 'First Run !'
   }
   task second {
   	println 'Second Run !'
   }
   task printVersion (dependsOn:[second,first]){
   	doLast {
   		println "Version : $version"
   		logger.quiet "Version : $version"
   	}
   }
   task third <<{
	println 'Third Run!'
   }
   third.dependsOn('printVersion')
```

- 如果把second的定义放在First前面，就会先运行second
- 这个例子就说明了，被依赖方的运行，不是按照声明的顺序，而是定义的顺序
    - （因为依赖是只要被依赖方执行即可，和顺序关系不是很大）
- 还可以使用SLF4J的logger实现
    - 日志级别 DEBUG,ERROR,INFO,TRACE,WARN ,还有QUIET...
- 如果 是 `gradle -b tasksL.gradle -q third` 就会运行所有的task，因为这是最后一层依赖
    - 如果 是`gradle -b tasksL.gradle -q printVersion` 就会只运行 printVersion 如果整个文件有编译错误也是不运行的

### 终结器 task
```Groovy
   task f<<{println 'first'}
   task s<<{println 'second'}
   f.finalizedBy s
   //当运行 gradle f 就会自动触发 s
   //如果gradle s 就和f没有任何关系了
```
***************************

### Groovy的POGO类管理配置文件上的版本号
- [taskL.gradle](https://github.com/Kuangcp/LearnGradle/blob/master/demo/tasksL.gradle)
-  gradle -b tasksL.gradle -q printVersion
-  虽然只是 运行了这个task 但是读取文件的task也被自动调用了
-  因为Gradle的构建生命周期阶段如下: 初始化、配置和执行 读取文件就属于配置阶段
	- **注意** : 项目的每一次构建都会运行属于配置阶段的代码，即使你只是运行了 gradle tasks


### task 的inputs 和 outputs
- 流程 : inputs -> |task| -> outputs
- gradle通过比较两个task的inputs和outputs来决定task是否最新
    - 如果inputs和outputs没有改变 就不会执行该task
    - 输入和输出可以是，一个文件，多个文件，一个目录，一个property属性
- [示例代码:turnVersion.gradle](https://github.com/Kuangcp/LearnGradle/blob/master/demo/turnVersion.gradle)
    - makeRealeseVersion : 将一个项目的版本切换为发布版本 
    - IOReleaseVersion : 通过inputs/outputs来添加增量式构建支持 
        - 发现并不能得到书上的预期效果，书上是说改动了properties文件才会让这个task运行，没有改就会说 up-to-date
        - 但是实际得到的是，改动了properties或者是构建文件都会引起task运行，两者都不改动就不会运行task，而且不会有输出提示up-to-date，要自己手动logger

***************

### 编写和使用自定义task
- 自定义task包含两个组件：
    - 自定义的task类，封装了逻辑行为，也被称为任务类型
    - 真实的task 提供了用于配置行为的task类所暴露的属性值

- 这个task就是做到了改配置文件，确保是RELEASE版本
```Groovy
//先要实例化version属性对象的存在
   version = new ProjectVersion(0,1,true)
   //继承DefaultTask类型的自定义task类
   class ReleaseVersionTask extends DefaultTask{
    @Input Boolean release
    @OutputFile File destFile
    ReleaseVersionTask(){
        group = 'versioning'
        description = 'Make Project a release version'

    }
    //task的行为逻辑
    @TaskAction
    void start (){
        project.version.release = true;
        ant.propertyfile(file:destFile){
            entry(key:'release',type:'string',operation:'=',value:'true')
        }
        println "$project.version"
    }
}
//version的POGO类
class ProjectVersion{
    Integer major
	Integer minor
    Boolean release
    ProjectVersion (Integer major ,Integer minor){
		this.major = major
		this.minor = minor
	}
    ProjectVersion (Integer major ,Integer minor,Boolean release){
		this(major,minor)
		this.release = release
	}
    @Override
    String toString(){
        "$major.$minor${release?'-RELEASE':'-SNAPSHOT'}"
    }
}
//真实的task，用来操作自定义类暴露的几个属性
//使用命令来运行，本质是运行真实的task但是行为逻辑在自定义类中编写
//gradle -b UserDefineTask.gradle -q makeReleaseVersion
//如果要改动一些数据可以直接更改暴露的task而不用去改自定义的task类
task makeReleaseVersion(type:ReleaseVersionTask){
    release = 'true'
    destFile = file('version.properties')
}
```

#### 声明task规则
```groovy
   //All used property must define and initial first
   version = new ProjectVersion(0,1,true)
   ext.versionFile = file('version.properties')
   class ProjectVersion{
       Integer major
   	Integer minor
       Boolean release
       ProjectVersion (Integer major ,Integer minor){
   		this.major = major
   		this.minor = minor
   	}
       ProjectVersion (Integer major ,Integer minor,Boolean release){
   		this(major,minor)
   		this.release = release
   	}
       @Override
       String toString(){
           "$major.$minor${release?'-RELEASE':'-SNAPSHOT'}"
       }
   }
   // task规则的定义
   tasks.addRule("Pattern: increment<Classifier>Version - Increment the project version classifier." ){
   //根据预定义模式来检查task的名称
    String taskName -> if(taskName.startsWith('increment') && taskName.endsWith('Version')){
        //根据符合命名模式的task动态添加一个doLast的方法
        task(taskName)<<{
         //从完整的task名称中提取类型字符串，
         //字面意思是将字符串中increment和Version两个串去除掉然后转小写再赋值
            String classifier = (taskName - 'increment' - 'Version').toLowerCase()
            String currentVersion = version.toString()
            switch (classifier){
                case 'major':++version.major
                    break
                case 'minor':++version.minor
                    break
                default : throw new GradleException("Invalid version type '$classifier' . Allow types :['Major','Minor']")
            }
            String newVersion = version.toString()
            logger.info "Increment $classifier project version: $currentVersion -> $newVersion"
            ant.propertyfile(file:versionFile){
                entry(key:classifier,type:'int',operation:'+',value:1)
            }
        }
    }
}
```
- 运行 `gradle -b RulesTask.gradle -q incrementMinorVersion`就可以增加版本号了，就是一个动态的执行命令的机制
    - 使用 incrementMajorVersion就可以增加主版本号
- 如果运行 `gradle -b RulesTask.gradle -q tasks` 就会得到一个具体的tasks的组Rules


## 增量式构建特性
- 如果Java源文件与最后一次运行的构建不同的话，运行 `compileJava task` 将充分提高构建的性能

*****************************

# 测试模块
> 凡是依赖于本地环境的测试，使用完就注释Test注解，还有那些会CRUD，影响到数据的测试方法也是
> 以防以后线上测试通不过 打包失败, 

- 跳过测试 `gradle build -x test` 或者是 `--exclude-task test` 参数 

## 单元测试
### 使用JUnit
> [使用Junit4](/MyBlog/how-to-use-junit.md)

### 使用其他框架 TestNG Spock

*************

## 配置测试执行

**************************************

# 多语言编程
## 处理javascript
### 压缩javascript
- 调用Google Closure Compiler 的task 来压缩javascript文件 将所有的javascript压缩成一个javascript文件
- 执行该task  gradle :web :taskname
- 执行之后就能得到一个优化的js文件，现在就要在页面中修改原来的js引用

### Java 和 Groovy的联合编译
- src 下 main 下 java 和groovy 的一个目录结构，直接编译就会发生Java无法依赖groovy的类
- 错误：需要配置 ` sourceSets.main.java.srcDirs=[]` ` sourceSets.main.groovy.srcDirs=['src/main/java','src/main/groovy']`
    - 正确： `sourceSets.main.java.srcDirs=['src/main/java','src/main/groovy']` 上面的会报错
- 配置好后就能把groovy当普通Java类直接使用了

************

### Java 和 Scala
-  联合双向编译 Java和scala
- ` sourceSets.main.scala.srcDirs` ` sourceSets.main.groovy.srcDirs=['src/main/java','src/main/scala']`
- 那么问题来了，如果是有了java groovy scala 呢怎么配置编译，直接就加上就好了嘛？


## Jenkin 使用
### 下载安装和配置
- 官网下载war包后，直接使用Java命令运行 或者放在web容器中运行
- 配置下载插件（位置在C盘用户目录下， 其实第一次运行后也是会解压在.jenkin 目录下 插件就在plugin目录下）
- 

# 发布自己的构件 

[如何发布Jar包到Maven Central Repository ](https://lambeta.com/2017/09/15/release-jar-to-maven-central-repository/)

