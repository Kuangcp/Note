`目录 start`
 
- [JVM上的多语言使用](#jvm上的多语言使用)
    - [语言生态学](#语言生态学)
        - [重新实现的语言和原生语言](#重新实现的语言和原生语言)
    - [JVM上的多语言编程](#jvm上的多语言编程)
        - [Groovy](#groovy)
        - [Scala](#scala)
        - [Clojure](#clojure)
        - [为什么非要用Java语言](#为什么非要用java语言)
        - [JVM对备选语言的支持](#jvm对备选语言的支持)
        - [编译器小说](#编译器小说)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# JVM上的多语言使用
> 先把Java熟练先, 

    喜欢Ruby => 用Groovy
    喜欢LISP，喜欢STM功能 => 用Clojure
    喜欢C++ => 用Kotlin

## 语言生态学
- 大致讨论 解释型和编译型， 动态和静态， 命令式和函数式
- Java是运行时编译，静态类型的命令式语言。强调安全性，代码清晰，性能，并表现出一定程度的繁琐和死板（例如部署）

`解释型和编译型`
- 在80 90 年代，边界较为清晰，类C语言是编译型，Perl和Python是解释型。但Java是两者都有
- 基于JVM来划分的边界是：该语言是否将源码编译为类文件并且执行，不产生类文件的语言会由解释器逐行执行。有些语言既有编译器又有解释器，有些是既有解释器又有产生字节码的即时编译器JIT

`动态和静态类型`
- 动态类型语言，变量在不同的时间可能会有不同的类型 动态类型语言是跟踪变量的值的类型信息，静态类型语言是跟踪变量的类型信息
- 静态类型适合做编译型语言

`命令式和函数式`
- Java是典型的命令式语言，命令式语言把程序的运行状态建模为可修改的数据，用一系列的指令来改变状态。因此在命令式语言中，程序状态是核心概念
- 命令式语言主要分为两类，一种是面向过程语言，一种是面向对象语言
    - 面向过程：Basic Fortran 这种语言将代码和数据完全分离开，有简单的代码操作数据范式
    - 面向对象：数据和代码（方法形式）封装在对象中，面向对象语言中或多或少会存在元数据（比如：类信息）引入的额外结构
- 函数式语言他把计算本身当成最重要的概念。函数式语言和过程式语言一样对值进行操作，但他不会修改输入，而是像数学函数一样返回新值
    - 函数被看成是一个小处理机，输入值并输出值，他们没有自己的状态，并且将他们和任何外部状态绑定在一起也没有意义
- `Groovy带一点函数式风格，Scala对FP的利用更为充分，Clojure是纯粹的函数式语言，没有丁点儿面向对象特性`

### 重新实现的语言和原生语言
> 一般来说，以JVM为目标的语言较重新实现的语言能将自己的类型系统和JVM的类型系统结合的更紧密

- 重新实现已有语言的JVM语言：
    - JRuby：Ruby是一个动态类型的面向对象语言，有些函数式特性，在JVM上基本算解释型的
    - Jython：动态的面向对象语言。运行方式是先生成Python字节码再转化成JVM字节码。这使得他能以看起来像是Python的典型解释型模式下运行
    - Rhino：他在JVM上提供了一个JavaScript实现，既支持编译模式，也支持解释模式

## JVM上的多语言编程
- 非Java技术的作用可以分为三个层次 特定领域层，动态层，稳定层，多语言编程金字塔：
![p178金字塔](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Java7Developer/p178.jpg)

- 静态类型语言更倾向于稳定层的任务，能力不是那么强，通用性较低的技术在金字塔的顶部更好用

> [Java 、Groovy、 Scala 的未来会怎样？](https://www.zhihu.com/question/21740715)
> [Java & Groovy & Scala & Kotlin - 16.方法，Lambda 与闭包](https://www.jianshu.com/p/3d01a98da9f9)


Scala有两个流派：FP和Better Java。FP派喜欢scalaz，喜欢shapeless，喜欢type level programming。这一派特点是程序高度抽象但可读性奇差。
适合PL研究者验证概念，适合业余项目自嗨，也适合学习PL概念。不适合多人协作的工程项目。Better Java派以前之所以存在，单纯是因为Java语法设计太烂，烂到无法忍受。
而JVM上当时也没有其它更好的选择。
那些告诉你“写了n年Java以后，我切换到Scala，现在每天都活在幸福中”的人，基本都是这一派。但Scala as a better Java的工程性也不好，因为特性太多太复杂，除非有高手带队，否则很难只用到它“better java”的那个子集。
解决一个问题的同时，往往引入更多的问题。所以会有Java8发布以后Linkedin所有新项目全部回归Java这种事情。Groovy是动态语言，工程性比Scala还差。
但是因为有Gradle这种被广泛采用的项目，所以会存活下去。但是请记住爱因斯坦曾经说过：“任何超过两百行的新项目，都不应该采用动态语言开发，无论是Ruby，Python，Perl，Groovy还是Clojure”。
哦，对了，也不要用Clojure。因为它是动态语言，而且是Lisp系的动态语言。“Lisp系”意味着，读书的时候可以靠它开眼界。毕业工作以后，对于这一类语言，能躲多远就躲多远。
刚刚发布的Kotlin看上去靠谱。它不讲究FP有多纯，目标就一个：“a better java”。Kotlin在“到底引入多少FP特性”上面做得恰到好处。 
看到Kotlin，我马上就想起了这个演讲：“Please stop polluting our imperative languages with pure concepts”。
Kotlin有以下好处：
1. 强大的IDE。而且是JetBrains第一方支持，不是3年更新一次的第三方插件；
2. 库多生态强。Kotlin的设计者非常重视和Java的互操作，所以Kotlin号称可以无缝衔接所有Java库。
3. 宇宙第一运行时：JVM。
4. Android上不能用Java8的新语法，Kotlin恰逢其时的出现，抓了一波完美的timing。如果Kotlin依靠Android开发爆发，那服务器端，大数据界，也会收益，最后多面开花，势不可挡。
但是Kotlin刚出来，到底有没有它自称的那么好用还待观察。另外，Kotlin社区现在集中力量攻坚Android，在服务器和大数据方向没什么靠谱项目。所以还是得用Java8。
总之，“魔镜啊魔镜，谁是JVM上最好的语言”之最后决战，将是Java10 vs Kotlin（Java9在语法特性上已经输了）。而在这场最终决战之前，C#已经靠着CoreCLR统一世界了。

最后送上人生经验两则：  
1.
```
    match comment with
    | "X怎么不能Y？人家Z就是这样做的。" ->  reply "卡马克能用haskell移植Wolf 3D，你能？"
    | _ -> reply "Thank you"
```
2.
```
    match location with
    | Office -> use whatever your boss chose
    | Home   -> use F#
```
### Groovy
> James Strachan 于2003年发明，可以看作动态层语言，擅长DSL构建

### Scala
> Martin Odersky 于2003年意外产生，一门支持函数式编程的面向对象语言  
> 有一个非常好的ScalaTest测试框架，比Junit更简洁，

### Clojure
> Rich Hickey设计的属于Lisp家族的语言，动态类型的函数式语言，编译型语言但是通常以源码发布

### 为什么非要用Java语言
- Java 作为一种通用，静态类型的编译型语言，实现稳定层方便，但是放到金字塔上层就成为负担
    - 编译耗时
    - 静态类型不够灵活，重构时间长
    - 部署麻烦
    - 语法不适合生产DSL（领域专用语言 domain specific language）

![p180 分类](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Java7Developer/p180.jpg)

****************

### JVM对备选语言的支持
- 一种语言要在JVM上运行的两种方式：
    - 一个产生类文件的编译器
    - 一个用JVM字节码实现的解释器
![p183.jpg](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Java7Developer/p183.jpg)
- 有一种评估语言运行时环境复杂度的简单方法，看运行实现中Jar的大小，Clojure相对较轻量，JRuby就显得重

**************************

### 编译器小说
> 语言的某些特性是由编程环境和高层语言合成的，在底层JVM中不存在，这种特性就称为编译器小说

- Java中的编译器小说还包括检查型异常和内部类（通常内部类都会转换成带有特殊合成访问方法的顶层类），如果jar -cvf看jar包，能看到很多含`$`的类，这些就是被取出转换成`常规类`的内部类
`备选语言的编译器小说`
![p184.jpg](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Java7Developer/p184.jpg)
- 函数一等值：
    - 这个就是说可以将函数当成其他普通值一样操作，Java只能把类当做最小的代码和功能单元。解决这种差异的方法是，因为对象只是把数据和操作数据的方法绑定在一起，只要有一个没有状态只有一个方法的对象。
    - 这似乎就是Java8的lambda表达式的存在条件，单方法的实现用操作符 `->`
- 多继承：
    - 在Java和JVM中无法实现多继承，只能使用接口，但是接口又没有任何具体的方法
    - 在Scala中特性机制 trait 允许将方法的实现混合到类中，所以提供了不同的继承视图，这种行为必须由Scala编译器和运行时合成，在VM层面不提供这种特性
  

