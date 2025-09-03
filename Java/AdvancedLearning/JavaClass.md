---
title: Java的字节码
date: 2018-11-21 10:56:52
tags: 
    - 字节码
categories: 
    - Java
---

💠

- 1. [字节码以及类加载](#字节码以及类加载)
- 2. [编译优化](#编译优化)
    - 2.1. [JIT 即时编译](#jit-即时编译)
- 3. [字节码](#字节码)
    - 3.1. [字节码相关框架](#字节码相关框架)
    - 3.2. [常量池](#常量池)
- 4. [类加载机制](#类加载机制)
    - 4.1. [类加载器](#类加载器)
        - 4.1.1. [特殊场景](#特殊场景)
            - 4.1.1.1. [JDBC](#jdbc)
            - 4.1.1.2. [Tomcat](#tomcat)
        - 4.1.2. [JDK9 jigsaw](#jdk9-jigsaw)
    - 4.2. [加载和连接](#加载和连接)
    - 4.3. [方法句柄](#方法句柄)
- 5. [Agent](#agent)
- 6. [反编译](#反编译)
- 7. [热部署](#热部署)

💠 2025-09-03 11:19:19
****************************************
# 字节码以及类加载
> [相关示例代码](https://github.com/Kuangcp/JavaBase/tree/master/class) 

************************
> 书籍
- 深入理解Java虚拟机 周志明
- Java 虚拟机字节码 从入门到实战 吴就业

# 编译优化
> 由源文件 *.java 编译成 *.class 文件这个过程中做的调优

类中定义的常量 如果是字面值, 其他引用这个常量的地方编译后会被替换成字面值, 该常量属性的 get 方法也是直接返回字面值  
字面值就是无需运算的值, 而不是表达式 例如 `final int num = 2;` 反例 `final int num = 3>2?1:2;`

## JIT 即时编译
目前有三种：C1 C2 Graal

| 类型 | JVM参数 | 特点 |
|:---|:---|:---|
| C1 | -client | 编译耗时短 |
| C2 | -server | 编译耗时长执行效率好`需要收集运行期profile信息来辅助编译也就是PGO` |
| Graal |  |  |

> 注意 自JDK8起默认开启分层编译`C1 C2混用` -client -server参数**无效**

> [Graal Compiler](https://www.graalvm.org/latest/reference-manual/java/compiler/)  
> [Deep Dive Into the New Java JIT Compiler – Graal](https://www.baeldung.com/graal-java-jit-compiler)

************************

# 字节码
> [参考: 学会阅读Java字节码](https://www.cnblogs.com/beautiful-code/p/6425376.html)
> [参考: 字节码增强技术探索](https://tech.meituan.com/2019/09/05/java-bytecode-enhancement.html)  


字节码是程序的中间表达形式，源码和机器码之间的产物 字节码是由源文件执行javac产生的

某些高级语言特性（语法糖）在字节码中会进行简化，例如循环结构，会转换成为分支指令

- 每个操作都由一个字节表示，因此叫做字节码
- 字节码是一种抽象表示方法 字节码进一步编译得到机器码

- `javap -c -p class文件` 反编译字节码文件，-p 能看到私有属性
    - 输出所有的属性以及类的定义信息
    - 静态块
    - 构造方法
    - 方法信息
    - 静态属性信息
    - 静态方法信息

## 字节码相关框架
> [Apache bcel](http://commons.apache.org/proper/commons-bcel/index.html)  

asm  
javassist

> [raphw/byte-buddy: Runtime code generation for the Java virtual machine.](https://github.com/raphw/byte-buddy)  
******************

## 常量池
> 常量池是为类文件中的其他常量元素提供快捷访问方式的区域。对于JVM来说常量池相当于符号表
> [参考博客](http://www.cnblogs.com/LeonNew/p/5314731.html)  

- `javap -v class文件` 输出很多额外信息，# 开头的就是常量池信息
![图](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Java7Developer/p120.jpg)

- [ ] 理解常量池 以及使用场景

************************

# 类加载机制
- 类的生命周期 
    - `加载 Loading` -> `验证 Verification` -> `准备 Preparation` -> `解析 Resolution` -> `初始化 Initialization` -> `使用 Using`  -> `卸载 Unloading`
    - 验证、 准备、 解析，统称为 链接 Linking

## 类加载器
> [参考:  一文带你深扒ClassLoader内核，揭开它的神秘面纱！ ](https://www.cnblogs.com/wmyskxz/p/13575224.html#_label4)`深入源码，举例清晰`  

> [深入分析Java类加载器原理本文分析了双亲委派模型的实现原理，并通过代码示例说明了什么时候需要实现自己的类加载器以及如何 - 掘金](https://juejin.cn/post/6844903794627608589)  

> 双亲委派模型(`parents delegation model`） 实现代码：`java.lang.ClassLoader#loadClass(java.lang.String, boolean)`
> 其工作原理是，如果一个类加载器收到了类加载请求(只讨论首次加载，已经加载过的会走缓存), 它并不会自己先去加载，而是委托给父类的加载器去执行  
> 如果父类加载器还存在其父类加载器，则进一步向上委托，依次递归，请求最终将到达顶层的启动类加载器  
> 如果父类加载器可以完成类加载任务，就成功返回，倘若父类加载器无法完成此加载任务，子加载器才会尝试自己去加载

- Java平台经典类加载器层级：
    1. `BootStrap ClassLoader`  根（引导）加载器：通常在VM启动后不久就实例化，最顶层的加载类，主要加载 核心类库 并且不做验证工作 
        - 加载目录 `%JRE_HOME%\lib` 下的rt.jar、resources.jar、charsets.jar 和 class 文件
    2. `Extendsion ClassLoader` 扩展类加载器：加载安装时自带的标准扩展，一般包括安全性扩展
        - 加载目录 `%JRE_HOME%\lib\ext` 下的 jar 包和 class 文件。
    3. `Application ClassLoader`  应用或系统类加载器：应用最广泛的类加载器，负责加载应用类(当前应用的 classpath 的所有类)
    4. `自定义ClassLoader` 自定义类载器

> 注意：  
>1. 例如在读取类路径下文件时，可以通过 `classA.getClassLoader().getResourceAsStream("app.properties")` 但是如果类classA对象是由 BootStrap 类加载器加载的， getClassLoader() 将返回 null  
>1. 当出现jar包多版本时，先加载了其中一个版本就不会加载另一个版本，而这个加载顺序往往是由操作系统的文件排序决定的 [相关案例](/Java/Blog/Java-ClassLoad-Confuse.md) 

### 特殊场景
JDBC,JNBI,Tomcat 等

#### JDBC

例如 DriverManager.getConnection(); 创建JDBC连接， java.sql.DriverManager#loadInitialDrivers 静态代码块中实现了驱动类的加载，同时 DriverManager位于 rt.jar， 会被BootStrap 加载，但是驱动实现类通常在外部目录，第三方的类不能被根加载器加载。

JDBC中通过引入ThreadContextClassLoader（线程上下文加载器，默认情况下是AppClassLoader）的方式破坏了双亲委派原则

```java
    public static <S> ServiceLoader<S> load(Class<S> service) {
        ClassLoader cl = Thread.currentThread().getContextClassLoader();
        return ServiceLoader.load(service, cl);
    }
```

#### Tomcat
> [参考: 图解Tomcat类加载机制](https://www.cnblogs.com/aspirant/p/8991830.html)  

- *CommonClassLoader* Tomcat最基本的类加载器，加载路径`/common/*`中的class可以被Tomcat容器本身以及各个Webapp访问；
- *CatalinaClassLoader* Tomcat容器私有的类加载器，加载路径`/server/*`中的class对于Webapp不可见；
- *SharedClassLoader* 各个Webapp共享的类加载器，加载路径`/shared/*`中的class对于所有Webapp可见，但是对于Tomcat容器不可见；
- *WebappClassLoader* 各个Webapp私有的类加载器，加载路径`/WebApp/WEB-INF/*`中的class只对当前Webapp可见；

为了实现不同Tomcat容器间的隔离， WebApp类加载器和Jsp类加载器通常会存在多个实例，每一个Web应用对应一个WebApp类加载器`WebAppClassLoader`，每一个JSP文件对应一个Jsp类加载器。

WebApp类加载器就为了类隔离而违背了双亲委派模型，仅自身负责加载类，不向上传递

### JDK9 jigsaw

> [模块化（jboss modules、osgi、jigsaw）](https://hollischuang.github.io/toBeTopJavaer/#/basement/jvm/moduler)  

在JDK9中，整个JDK都基于模块化进行构建，以前的rt.jar, tool.jar被拆分成数十个模块，编译的时候只编译实际用到的模块，同时各个类加载器各司其职，只加载自己负责的模块。

```java
    Class<?> c = findLoadedClass(cn);
    if (c == null) {
        // 找到当前类属于哪个模块
        LoadedModule loadedModule = findLoadedModule(cn);
        if (loadedModule != null) {
            //获取当前模块的类加载器
            BuiltinClassLoader loader = loadedModule.loader();
            //进行类加载
            c = findClassInModuleOrNull(loadedModule, cn);
        } else {
            // 找不到模块信息才会进行双亲委派
                if (parent != null) {
                c = parent.loadClassOrNull(cn);
                }
        }
    }
```

************************

## 加载和连接
> [参考: 第七章.虚拟机类加载机制](http://ifeve.com/%e7%ac%ac%e4%b8%83%e7%ab%a0-%e8%99%9a%e6%8b%9f%e6%9c%ba%e7%b1%bb%e5%8a%a0%e8%bd%bd%e6%9c%ba%e5%88%b6/)

`加载`
- 这个过程就是读取字节码文件，创建一个字节数组装在这些内容，加载结束后这个对象还不能直接调用 

`连接`
- 加载完成后，类必须连接起来，分为三步：验证，准备，解析。
    - 验证：
        - 验证文件的合理性，完整性检查，检查常量池，方法的字节码检查。主要的：
        - 是否所有方法都遵守访问控制关键字的限定
        - 方法调用的参数个数和静态类型是否正确
        - 确保字节码不会试图滥用堆栈
        - 确保变量使用之前被正确初始化了
        - 检查变量是否仅被赋予恰当类型的值
    - 准备：
        - 分配内存，准备初始化类中的静态变量，但不会现在就初始化，也不会执行任何VM字节码
    - 解析：
        - 促使VM检查类文件中所引用的类型是不是都是已知的类型。如果有运行时有未知的类型，那又要引发一次类加载过程
        - 当需要加载的类全部加载解析完毕后，VM就可以初始化最初那个加载的类了。
        - 这时所有的静态变量都可以进行初始化，所有静态代码块都会运行，这一步完成后，类就能使用了

## 方法句柄
> 主要用于反射 用到再学

![图](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Java7Developer/p118.jpg)

************************
# Agent
> [JDK: Interface Instrumentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.instrument/java/lang/instrument/Instrumentation.html)

> [Guide to Java Instrumentation](https://www.baeldung.com/java-instrumentation)  
> [ Java Agent 探针技术](https://juejin.cn/post/7086026013498408973)  

Java Agent 主要有以下功能
- Java Agent 在加载 Java 字节码之前拦截并对字节码进行修改;
- Java Agent 在 Jvm 运行期间修改已经加载的字节码;

Java Agent 的应用场景

| 能力 | 案例 |
|:----|:----|
| IDE的调试功能     |  Eclipse、IntelliJ IDEA ；
| 热部署功能        |  JRebel、XRebel、spring-loaded；
| 各种线上诊断工具   |  Btrace、Greys， Arthas；
| 各种性能分析工具   |  Visual VM、JConsole 等；
| 全链路性能检测工具  |  Skywalking、Pinpoint等；


> [agent](https://github.com/yxkong/agent)`线程池监控`  

************************

# 反编译
> [JD](http://java-decompiler.github.io/)  
> [https://varaneckas.com/jad/](https://varaneckas.com/jad/)  
> [Java-Class-Viewer](https://www.codeproject.com/Articles/35915/Java-Class-Viewer)  
> [classpy](https://github.com/zxh0/classpy)  

************************

# 热部署
> 通过替换 class 实现不停机热更新

> [Spring hot swapping](https://docs.spring.io/spring-boot/docs/current/reference/html/howto-hotswapping.html)

1. Instrumentation
1. 自定义类加载器
1. OSGI 热插拔接口

[Instrumentation 新功能](https://www.ibm.com/developerworks/cn/java/j-lo-jse61/index.html)
[基于Java Instrument的Agent实现](https://www.jianshu.com/p/b72f66da679f)
[Java 5 特性 Instrumentation 实践](https://www.ibm.com/developerworks/cn/java/j-lo-instrumentation/)
[java组件中的热插拔（osgi)](https://blog.csdn.net/javierhui111/article/details/3830833)
[agentmain 方式 ](https://www.cnblogs.com/cm4j/p/hot_deploy.html)

> [Java 类的热替换 —— 概念、设计与实现 - 时空穿越者 - 博客园](https://www.cnblogs.com/studyLog-share/p/4720603.html)  

相关项目: 

[game-hot-update](https://github.com/youxijishu/game-hot-update) | [游戏服务器之Java热更新](https://www.cnblogs.com/wgslucky/p/9127681.html)
[groovy hotswap demo](https://github.com/chaopeng/groovy-hotswap-demo)

> [Java系列 | 远程热部署在美团的落地实践](https://tech.meituan.com/2022/03/17/java-hotswap-sonic.html)`未开源`

************************

