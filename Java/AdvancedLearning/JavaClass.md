---
title: Java的字节码
date: 2018-11-21 10:56:52
tags: 
    - 字节码
categories: 
    - Java
---

**目录 start**

1. [字节码以及类加载](#字节码以及类加载)
1. [编译优化](#编译优化)
1. [字节码](#字节码)
    1. [常量池](#常量池)
1. [类加载机制](#类加载机制)
    1. [类加载器](#类加载器)
        1. [特殊场景](#特殊场景)
            1. [Tomcat](#tomcat)
    1. [加载和连接](#加载和连接)
    1. [方法句柄](#方法句柄)
1. [反编译](#反编译)
    1. [JD](#jd)
    1. [Jad](#jad)
1. [字节码相关框架](#字节码相关框架)
1. [热更新](#热更新)
1. [分析工具](#分析工具)

**目录 end**|_2020-09-12 20:13_|
****************************************
# 字节码以及类加载
> [个人相关代码](https://github.com/Kuangcp/JavaBase/tree/master/class) 

# 编译优化
> 由源文件 *.java 编译成 *.class 文件这个过程中做的调优

类中定义的常量 如果是字面值, 其他引用这个常量的地方编译后会被替换成字面值, 该常量属性的 get 方法也是直接返回字面值  
字面值就是无需运算的值, 而不是表达式 例如 `final int num = 2;` 反例 `final int num = 3>2?1:2;`

************************

# 字节码
> [参考: 学会阅读Java字节码](https://www.cnblogs.com/beautiful-code/p/6425376.html)

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

> 双亲委派模型(`java.lang.ClassLoader#loadClass(java.lang.String, boolean)`) 其工作原理的是，如果一个类加载器收到了类加载请求(只讨论首次加载，已经加载过的会走缓存提前返回)  
> 它并不会自己先去加载，而是委托给父类的加载器去执行，如果父类加载器还存在其父类加载器，则进一步向上委托，依次递归，请求最终将到达顶层的启动类加载器  
> 如果父类加载器可以完成类加载任务，就成功返回，倘若父类加载器无法完成此加载任务，子加载器才会尝试自己去加载，这就是双亲委派模式

- Java平台经典类加载器：
    - `BootStrap ClassLoader`  根（引导）加载器：通常在VM启动后不久就实例化，最顶层的加载类，主要加载 核心类库 并且不做验证工作 
        - 加载目录 `%JRE_HOME%\lib` 下的rt.jar、resources.jar、charsets.jar 和 class 文件
    - `Extendsion ClassLoader` 扩展类加载器：加载安装时自带的标准扩展，一般包括安全性扩展
        - 加载目录 `%JRE_HOME%\lib\ext` 下的 jar 包和 class 文件。
    - `Application ClassLoader`  应用或系统类加载器：应用最广泛的类加载器，负责加载应用类(当前应用的 classpath 的所有类)
    - `自定义ClassLoader` 自定义类载器

> 注意：  
>1. 例如在读取类路径下文件时，可以通过 `classA.getClassLoader().getResourceAsStream("app.properties")` 但是如果类classA对象是由 BootStrap 类加载器加载的， getClassLoader() 将返回 null  
>1. 当出现jar包多版本时，先加载了其中一个版本就不会加载另一个版本，而这个加载顺序往往是由操作系统的文件排序决定的 [相关案例](/Java/Blog/Java-ClassLoad-Confuse.md) 

### 特殊场景
#### Tomcat
> [参考: 图解Tomcat类加载机制](https://www.cnblogs.com/aspirant/p/8991830.html)  

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

****************

# 反编译
## JD
> [JD](http://java-decompiler.github.io/)

## Jad
> [https://varaneckas.com/jad/](https://varaneckas.com/jad/)


**************************************

# 热更新
> 通过替换 class 实现不停机热更新, 但是还有有局限性, 类结构, 方法签名不能有改变

> [Spring hot swapping](https://docs.spring.io/spring-boot/docs/current/reference/html/howto-hotswapping.html)

1. Instrumentation
1. 自定义类加载器
1. OSGI 热插拔接口

[Instrumentation 新功能](https://www.ibm.com/developerworks/cn/java/j-lo-jse61/index.html)
[基于Java Instrument的Agent实现](https://www.jianshu.com/p/b72f66da679f)
[Java 5 特性 Instrumentation 实践](https://www.ibm.com/developerworks/cn/java/j-lo-instrumentation/)
[java组件中的热插拔（osgi)](https://blog.csdn.net/javierhui111/article/details/3830833)
[agentmain 方式 ](https://www.cnblogs.com/cm4j/p/hot_deploy.html)

相关项目: 

[game-hot-update](https://github.com/youxijishu/game-hot-update) https://www.cnblogs.com/wgslucky/p/9127681.html
[groovy hotswap demo](https://github.com/chaopeng/groovy-hotswap-demo)

************************

# 分析工具
> [github.com/dingjs/javaagent](https://github.com/dingjs/javaagent)  
