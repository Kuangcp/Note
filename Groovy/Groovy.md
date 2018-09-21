`目录 start`
 
- [Groovy](#groovy)
    - [书籍](#书籍)
    - [语言特性](#语言特性)
    - [安装配置](#安装配置)
        - [在IDEA中](#在idea中)
        - [Maven引入Groovy](#maven引入groovy)
        - [Docker](#docker)
    - [Groovy基础](#groovy基础)
        - [Groovy特性](#groovy特性)
            - [默认导入](#默认导入)
            - [隐式return](#隐式return)
            - [默认生成setter getter](#默认生成setter-getter)
            - [数字处理](#数字处理)
            - [变量，动态和静态类型，作用域](#变量动态和静态类型作用域)
            - [列表和映射语法](#列表和映射语法)
            - [动态调用函数](#动态调用函数)
        - [函数](#函数)
        - [闭包](#闭包)
        - [测试](#测试)
        - [调用系统命令行](#调用系统命令行)
    - [强大的注解](#强大的注解)
    - [与Java的差异](#与java的差异)
        - [Java不具备的Groovy特性](#java不具备的groovy特性)
    - [Groovy和Java的交互](#groovy和java的交互)
        - [Maven中引入Groovy](#maven中引入groovy)
        - [Groovy调用Java](#groovy调用java)
        - [Java调用Groovy](#java调用groovy)
        - [Groovy和Spring](#groovy和spring)
    - [坑](#坑)
        - [默认return](#默认return)
    - [Grails](#grails)

`目录 end` |_2018-09-01_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Groovy
> [Groovy 官网](http://www.groovy-lang.org/) | 

> [实战Groovy系列](https://www.ibm.com/developerworks/cn/java/j-pg/)`有体系的知识`
> [精通Groovy](https://www.ibm.com/developerworks/cn/education/java/j-groovy/j-groovy.html)
> [Groovy：Java 程序员的 DSL](https://www.ibm.com/developerworks/cn/java/j-pg02179.html)
> [w3cschool Groovy教程](https://www.w3cschool.cn/groovy/)
> [并发编程网 Groovy分类文章](http://ifeve.com/category/groovy/)
> [infoQ 上Groovy相关](http://www.infoq.com/cn/groovy)

## 书籍
> [Groovy in Action](http://ishare.iask.sina.com.cn/f/12475871.html) `在线阅读英文原版`

## 语言特性
- Groovy 具有的Java所没有的语言特性 ：
    - 函数字面值（闭包）
    - 对集合的一等支持
    - 对正则表达式的一等支持
    - 对XML处理的一等支持 （一等表示内置，不需要调用类库）
- Groovy处理XML和循环遍历集合的方式要比Java简洁
- Groovy性能：如果你需要注重性能，Groovy不是一个好的选择，Groovy的对象都派生于GroovyObject，Groovy的方法都不是直接调用的而是反射执行的。虽然有invokedynamic关键字进行优化
    - 一些重活还是调用Java类库好些，毕竟是互通互用的，调用groovyserv类库能提高性能

## 安装配置
- [安装sdkman](./Skills/AppManual.md#使用sdkman)
    - 然后 `sdk install groovy`
    - 新建文件 `println "Hello World!"` 然后 `groovy 文件`
        - 或者`groovy -e "println 'Hello World!'"`

### 在IDEA中
> 因为构建工具Gradle中就已经包含了Groovy的库,所以最好就是只配置好一个Gradle, 然后配置Groovy时选择Gradle的目录即可

### Maven引入Groovy
- [参考博客](http://www.cnblogs.com/xiziyin/archive/2010/03/29/1699860.html)

### Docker
> [Docker官方文档](https://docs.docker.com/samples/library/groovy/)

*************************
## Groovy基础
> 作为一个脚本语言，和Python Ruby Smalltalk语法相似

- groovyc groovy 类似于 javac java

### Groovy特性

#### 默认导入
`这一些导入是默认隐含在Groovy代码中`
```groovy
    import groovy.lang.*
    import groovy.util.*
    import java.lang.*
    import java.io.*
    import java.math.BigDecimal
    import java.math.BigInteger
    import java.net.*
    import java.util.*
```
- 添加额外的JAR可以使用`@Grab`注解或者和Java一样加入到ClassPath中去

#### 隐式return
- 如果方法是具有返回值的, Groovy会在`代码块`的行末缺省return null, 
    - 如果末行有一个表达式, 并有返回值, 就会return该值, 略坑

#### 默认生成setter getter
> 类当中的属性, 只要不是使用private修饰, 就能自动生成getter setter, 并且直接`.引用`属性, 相当于调用了对应的get set

#### 数字处理
- Groovy默认浮点数使用BigDecimal，Java中BigDecimal构造器入参是字符串，Groovy是数值，底层转换了一下，看起来更自然
- 因为是脚本语言，可以在控制台直接运行。Groovy对BEDMAS是支持的 （括号，次方，除，乘，加，减）

#### 变量，动态和静态类型，作用域
`变量`
- 如果要让Groovy和Java互操作，Groovy也能使用静态类型 `def static `，因为他简化了类型重载和调度机制
- 注意 普通类状态：在类中不能出现没有类型的变量 至少要有def这个无类型，其他的和Java一致 `def private static name = "90"`

`Groovy里的动态类型和静态类型`
- 如果变量不在定义时声明类型，那么就是一个动态类型，反之则是静态类型，静态类型就和Java的语法是一致的了，类型不可变

`作用域（通常这是指脚本状态时的普通类就是和Java一致）`
- 绑定域：是脚本的全局作用域。就是在脚本顶层没有声明类型的变量
- 本地域：变量的作用域局限于声明他们的代码块。就是在顶层声明了类型或者在代码块里
    - [变量作用域学习代码](https://github.com/kuangcp/JavaBase/blob/master/src/main/groovy/com/learn/base/VariableScope.groovy)

#### 列表和映射语法
- Groovy将列表和映射结构当做语言中的一等类型，列表和映射在底层是`ArrayList` 和 `LinkedHashMap`实现的
    - 列表：`lists = ['2', 2, new Date()]` 其实这个和Python的语法差不多，同样的支持负索引
    - 映射：`maps = [Java:"2", A:2]` 声明Maps
    - [列表和映射的学习代码](https://github.com/kuangcp/JavaBase/blob/master/src/main/groovy/com/learn/base/LearnListAndMap.groovy)

#### 动态调用函数

```groovy
    // 当前类, 可以这么用
    def test(name) {
        return "Hi "+name
    }
    String a = "test"
    print("${a}"("myth"))

```
```java
    class Condition{
        static isLevelMore(int level){
            return level > 30
        }
    }
    class Use {
        static void main(String[]a){
            // 跨类, 需要使用反射
            // 1
            MetaMethod method = Condition.metaClass.getMetaMethod("isLevelMore", 20)
            println method
            println method.invoke(Condition.class, 20)

            // 2
            Method method1 = Condition.class.getMethod("isLevelMore", int.class)
            println method1.invoke(Condition.class, 40)
            
            // 3
            Condition.getDeclaredMethods().toList().toSet().each {if(it.toString().contains("isLevelMore")){
                println it.invoke(Condition.class, 40)
            }}
        }
    }
```

### 函数
> [参考博客: Groovy进阶之函数、闭包和类](https://www.tuicool.com/articles/iEBJnqF)

### 闭包
```groovy
// 简单示例
    def plus = { x, y ->
        println "$x plus $y is ${x + y}"
    }
    plus(2, 3)
```

### 测试
[参考博客: 用 Groovy 更迅速地对 Java 代码进行单元测试](https://www.ibm.com/developerworks/cn/java/j-pg11094/)

*************************
### 调用系统命令行
> [Groovy 执行"cp *"shell 命令 ](http://www.guanggua.com/question/183352-groovy-execute-cp-shell-command.html)

1. 字符串.execute()
2. 字符串数组.execute() 这种更好些，尤其是多个参数的时候
    - 写法和Dockerfile一致 ` ["sh", "-c", "cp src/*.txt dst/"].execute()`

***************************
## 强大的注解
> 和Java不同的是, Groovy提供具有功能性的注解, Java大多是接口规范性注解

@ToString 自动实现toString方法, 但是字符串有点冗余
> [参考博客: Groovy中那些神奇注解之ToString](http://www.cnblogs.com/varlxj/p/5181788.html)

_日志相关_ 只需要引入对应的依赖, 就和lombok一样的使用
```java
    @Log4j
    @Log4j2
    @Slf4j
```
************
## 与Java的差异

- 简化输出语句：`println()` `print()` `printf()`
- Groovy的省略语法:
    - `语句结束处的分号`： 结束的分号是可选的，除非一行多条语句
    - `返回语句 return`： 方法中返回对象可以不使用return，会默认返回最后一个表达式的计算结果
    - `方法参数两边的括号`： 如果方法里的方法调用至少有一个参数，且没有二义性，则可以省略括号 
    - `public访问限定符`： 默认是public修饰符, 只有private public protected
    - 这类设计是为了让源码更为简洁，快速原型设计时体现出优势 

`脚本文件和类文件的差异`
- 一个文件定义了文件同名class 类（默认加上public） 就不能当脚本运行
    - 因为作为一个脚本文件运行的时候，是创建一个与文件同名的类 并且 继承了 `groovy.lang.Script` 将你写的语句封装起来
    - 当你显式的定义了同名类 也会隐性继承于Groovy超类 `groovy.lang.GroovyObject` 类似与Java的Object，就会当一个正常的类文件，不能写脚本了
- 脚本文件中方法不能命名为 run，对于类是没有限制，和Java一样使用

`异常处理`
- Groovy不区分已检查异常和未检查异常。Groovy会忽略方法签名中的所有throws

`Groovy中的相等`
- Groovy把 == 当做equals方法，检查真实对象是否相等需要使用Groovy的内置函数 is。但是仍然可以使用 == 来判断 null
    - 两种方式对于基本类型是一样的， == 用于对象时就是比较内存了，equals是比较值

`内部类`
- Groovy支持内部类，但大多数情况下我们应该使用函数字面值（下面有更为详细的学习）替代它。

> [示例代码](https://github.com/kuangcp/JavaBase/blob/master/src/main/groovy/com/learn/base/DiverseFromJava.groovy)

### Java不具备的Groovy特性
- GroovyBean，更简单的bean
- 用操作符`?.`实现null对象的安全访问
- 猫王操作符(Elvis operator)，更短的if/else结构
- Groovy字符串，更强的字符串抽象
- 函数字面值（闭包），函数当值传递
- 对正则表达式的本地支持
- 更简单的XML处理


`GroovyBean`
- 虽然很像JavaBean但是省略了显式声明的getset方法，提供了自动构造方法（采用映射来作为入参，很方便），允许使用`.`引用私有成员变量。修改默认行为显式重定义即可
- 封装性得以保留，语法更精简, `new Person().name="myth"`，其实就是隐式调用了set方法
```groovy
class Person{
    String name
    int age
}
```

`安全解引用 ?.`
- 如果对象是null，就什么都不做，理解为当做该次调用不存在。
- 函数也是支持这种安全解引用，所以Groovy的默认集合方法，例如max() 能自动处理好null引用

`猫王操作符`
- 可以把带有默认值的 if/else 结构写的极其短小，因为这个符号看起来很像猫王鼎盛时期梳的大背头。用猫王操作符不用检查null，也不用重复变量。

`增强型字符串`
- Groovy有一个GString类，他比String要灵活
- 特别注意，这个GString和String没有任何继承关系，不能将GString作为映射中的键，或者用来比较相等，这些使用的结果都是不可预料的
- 和Python一样的有个 三引号多行字符串

`函数字面值`
- 函数当成一等类型可以赋值等操作，要活用就没这么简单了

`内置集合操作`
- 集合内置函数
    - each : 遍历集合，对其中的每一项应用函数字面值 
    - collect : 收集在集合中每一项应用函数字面值的返回结果 相当于其他语言 map/reduce的map函数
    - inject : 用函数字面值处理集合并构建返回值 相当于其他语言 map/reduce的reduce函数
    - findAll : 找到集合中所有与函数字面值匹配的元素
    - max : 返回集合中的最大值
    - min : 返回集合中的最小值

`对正则表达式的内置支持`
- `~`   创建一个模式 （创建一个编译的Java Pattern）
- `=~`  创建一个匹配器 （创建一个Java Matcher对象）
- `==~` 计算字符串  （相当于在Pattern上调用Java match()方法）

`对XML的处理`
> XML是一个卓越的详细的数据交换语言，这不是一个图灵完备(必须能做条件判断，修改内存数据)的语言，所以只能用来交换数据

- Groovy有构建器的概念，用其原生语法可以处理任何树形结构的数据 HTML XML JSON等
- 解析XML：
    - XMLParser   支持XML文档的GPath表达式 GPath是一种表达式语言
    - XMLSlurper  跟XMLParser类似，但是以懒加载的方式工作
    - DOMCategory 用一些语法支持DOM的底层解析

> [示例代码](https://github.com/kuangcp/JavaBase/blob/master/src/main/groovy/com/learn/base/ModernGroovy.groovy)

***********************
## Groovy和Java的交互
### Maven中引入Groovy
> [参考文档 ](https://groovy.github.io/gmaven/groovy-maven-plugin/execute.html)

- 此方法不能打包, 只是在idea中能成功运行
```xml
<!-- 添加插件-->
<plugin>
    <groupId>org.codehaus.gmaven</groupId>
    <artifactId>groovy-maven-plugin</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy-all</artifactId>
            <version>2.0.6</version>
        </dependency>
    </dependencies>
</plugin>
<!-- 添加Groovy依赖-->
<dependency>
    <groupId>org.codehaus.groovy</groupId>
    <artifactId>groovy-all</artifactId>
    <version>2.4.7</version>
</dependency>
```
*********************************************

> [参考博客 eclipse开发Groovy代码，与java集成，maven打包编译](http://www.cnblogs.com/rightmin/p/4945797.html) | [Groovy file does not compile in Intellij IDEA](https://stackoverflow.com/questions/8310563/groovy-file-does-not-compile-in-intellij-idea)

```xml
    <plugin>
        <!-- 编译插件 -->
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.7.0</version>
        <configuration>
            <target>1.8</target>
            <source>1.8</source>
            <encoding>UTF-8</encoding>
            <compilerId>groovy-eclipse-compiler</compilerId>
            <verbose>true</verbose>
        </configuration>
        <dependencies>
            <dependency>
                <groupId>org.codehaus.groovy</groupId>
                <artifactId>groovy-eclipse-compiler</artifactId>
                <version>2.9.3-01</version>
            </dependency>
            <dependency>
                <groupId>org.codehaus.groovy</groupId>
                <artifactId>groovy-eclipse-batch</artifactId>
                <version>2.5.0-01</version>
            </dependency>
        </dependencies>
    </plugin>
```
> 这样的配置就能 `mvn clean package`

### Groovy调用Java
- 只要将JAR放入classpath中，只要java能调用到，groovy也能调用到，也就是说直接用，无需特别配置
- 也可以使用@Grab注解，来加载JAR

### Java调用Groovy
> [参考博客](http://www.tuicool.com/articles/i6raAv)
> [参考 在 Java 应用程序中加一些 Groovy 进来](https://www.ibm.com/developerworks/cn/java/j-pg05245/)

- 从Java调用Groovy需要将Groovy及其相关的JAR放到这个程序的CLASSPATH下
- Java调用Groovy代码的几种方法
    - 使用Bean Scripting Framework(BSF) 即JSR223
    - 使用GroovyShell
    - 使用GroovyClassLoader
    - 使用GroovyScriptEngine
    - 使用嵌入式的Groovy控制台

> [示例代码](https://github.com/kuangcp/JavaBase/blob/master/src/main/java/com/classfile/JavaUseGroovy.java)

### Groovy和Spring
> [参考博客: Groovy 使 Spring 更出色，第 1 部分](https://www.ibm.com/developerworks/cn/java/j-groovierspring1.html)

**************************************
## 坑
> 因为是动态的, 所以, 当Java或Groovy类更改了一些接口, 属性名, 调用方那里不会报错, 直到运行才报错, 而且 eclipse idea 都不报错, 只是会把错误的属性和调用变成带有下划线的灰色...

### 默认return
> 只要在方法最后一行放入表达式, 就会自动return, 这就导致了Groovy不会对方法进行检查, 逻辑复杂时如果少了一个return, 不会报编译错误, 方法直接返回null.  
> 这个坑, 硬是Debug了近一个小时, debug功力要提升了

***********************
## Grails
- [入门博客](http://www.jianshu.com/p/32c9b45a788f)
> [入门视频](http://www.icoolxue.com/album/show/341)

