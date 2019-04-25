---
title: Java基础语法
date: 2018-11-21 10:56:52
tags: 
    - 基础
    - 语法
categories: 
    - Java
---

**目录 start**
 
1. [基础语法](#基础语法)
    1. [代码风格](#代码风格)
    1. [结构](#结构)
        1. [判断](#判断)
        1. [循环](#循环)
    1. [用户输入输出](#用户输入输出)
1. [数据类型](#数据类型)
    1. [自动拆装箱](#自动拆装箱)
    1. [基础数据类型](#基础数据类型)
        1. [byte](#byte)
        1. [char](#char)
        1. [boolean](#boolean)
        1. [short](#short)
        1. [int](#int)
        1. [long](#long)
        1. [float](#float)
        1. [double](#double)
    1. [封装类型](#封装类型)
        1. [String](#string)
        1. [Float](#float)
        1. [Double](#double)
        1. [Integer](#integer)
        1. [Long](#long)
        1. [Boolean](#boolean)
        1. [Void](#void)
    1. [枚举类型](#枚举类型)
    1. [内部类](#内部类)
    1. [类型强转](#类型强转)
    1. [时间类型](#时间类型)
    1. [非原生类型](#非原生类型)
        1. [元组](#元组)
1. [运算](#运算)
    1. [除法](#除法)
    1. [取余](#取余)
    1. [位运算](#位运算)
1. [类的结构](#类的结构)
    1. [修饰符](#修饰符)
        1. [权限修饰符](#权限修饰符)
        1. [final](#final)
        1. [static](#static)
        1. [abstract](#abstract)
    1. [成员属性](#成员属性)
    1. [方法](#方法)
        1. [方法的传参方式](#方法的传参方式)
        1. [equals](#equals)
        1. [hashcode](#hashcode)
1. [抽象类](#抽象类)
1. [继承和接口](#继承和接口)
1. [Object](#object)
    1. [VO](#vo)
    1. [PO](#po)
    1. [TO](#to)
    1. [BO](#bo)
    1. [POJO](#pojo)
    1. [DAO](#dao)
1. [关键字](#关键字)
    1. [try](#try)

**目录 end**|_2019-04-25 14:45_|
****************************************
# 基础语法

## 代码风格
> [Google Style Guide](https://github.com/google/styleguide) | [阿里巴巴开发手册](/Java/AlibabaJavaStandard.md)

## 结构
### 判断
- if
- switch

### 循环
- while
    - `while(true){}`
    - `do{}while(true);`
- for 循环
    - `for(int a=0; i<10; i++){}`
- for each循环
    - `for(Object item:list){}` 其中list对象如果是通过调用一个对象的方法返回的，那么只会调用一次

## 用户输入输出
- `System.out.println("")` 输出并在末尾追加换行
    - .print() 输出, 行末不换行
    - .printf() 格式化输出, 和C语法类似

***********************
# 数据类型
> [Primitive Data Types](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)

## 自动拆装箱
> 在日常Java开发中, 基本数据类型和包装类型是可以视为等价的(唯一差别就是包装类型能表达null), 就是因为自动拆装箱的存在

| 基本数据类型 | 封装类型 | 默认值 |
|:----|:----|
| byte | Byte |
| char | Character |
| boolean | Boolean |
| short | Short |
| int | Integer |
| long | Long |
| float | Float |
| double | Double |
| void | Void |

> 存在的意义: TODO 

- 存储方式及位置的不同，基本类型是直接存储变量的值保存在堆栈中能高效的存取，封装类型需要通过引用指向实例，具体的实例保存在堆中。
- 初始值的不同，封装类型的初始值为null，基本类型的的初始值视具体的类型而定，比如int类型的初始值为0，boolean类型为false；
- 使用方式的不同, 在泛型时只能使用封装类型, 基本类型无法表达null

> 弊端

性能问题

自动装箱都是通过包装类的valueOf()方法来实现的.自动拆箱都是通过包装类对象的xxxValue()来实现的。

## 基础数据类型
> 八种基本数据类型 byte char boolean short int long float double

> [The Java™ Tutorials: Primitive Data Types](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)  

> [参考博客: Java 有值类型吗？](http://www.yinwang.org/blog-cn/2016/06/08/java-value-type)

确实, 这样来看Java没有值类型才是更统一的, 不过有没有对程序都是一样的, 因为Java没有解引用, 基本数据类型又没有成员, 所以值还是引用, 没差

### byte
> 字节 -128, 127, 表示 8位 一个字节 的值

### char

用 2 个字节来表示 Unicode 值 取值范围: '\u0000' (or 0) , '\uffff' (or 65,535 inclusive).

### boolean
> [参考 你真的知道Java中boolean类型占用多少个字节吗？](https://www.jianshu.com/p/2f663dc820d0)

### short

### int
> 数值范围 -2^31,2^31-1 int占四个字节 32位 一位是符号位   
Java8 以上可以使用无符号的 int, 值范围: 0, 2^32-1

### long
> 数值范围 -2^63 2^63-1 占八个字节 64位 一位是符号位  
Java8 以上可以使用无符号的 long, 值范围: 0, 2^64-1

### float

### double

**************************
## 封装类型
> `wrapper class`基本类型和包装类型不能混为一谈 本质上的 class是不同的, 只不过自动拆装箱才让人感觉没差别

|  |  |
|:----|:----|
| Integer.TYPE | int.class |
| Byte.TYPE    | byte.class |
| Boolean.TYPE | boolean.class |
| Double.TYPE  | double.class |
| Void.TYPE    | void.class |

***************************

> 封装类型的缓存行为 

对于 Integer, 有 IntegerCache 类缓存 [-128, 127] 范围内的值. 可以通过 `-XX:AutoBoxCacheMax` 修改上限值  
且 Byte Short Long Character 都有对应的缓存对象和缓存值范围, 但是只有Integer的缓存范围可变  

Byte, Short, Long有固定范围: [-128, 127]   
对于Character, 范围是 ‘\u0000’ 至 ‘\u007f’ 即 [0,127]  

true 和 false 也是缓存了的

> 可能造成的困惑
```java
    assert Integer.valueOf(1) == Integer.valueOf(1);
    assert Integer.valueOf(128) != Integer.valueOf(128);
```

### String
> 该类是final修饰的, 原因:[知乎问题](https://www.zhihu.com/question/31345592)

字符串对象是不可变的，这意味着一旦创建，它们的值就不能更改。 String类在技术上不是基本数据类型，但考虑到语言给予它的特殊支持，您可能倾向于将其视为基本数据类型。

- 常量池
    - 字符串常量池存在于方法区 
    - [String：字符串常量池](https://segmentfault.com/a/1190000009888357)

- 常见编码转换
    - 一般Windows文件默认编码：`str = new String(str.getBytes("iso8859-1"), "gb2312"); ` 
    - properties文件中获取中文 `str = new String(str.getBytes("utf-8"), "utf-8");`

> [字符串拼接](/Java/AdvancedLearning/Basic/StringConcat.md)

### Float
### Double
### Integer

> [BigInteger](https://docs.oracle.com/javase/8/docs/api/java/math/BigInteger.html)

### Long
> [Unsigned arithmetic in Java](https://www.javamex.com/java_equivalents/unsigned_arithmetic.shtml)  
> [Java equivalent of unsigned long long?](https://stackoverflow.com/questions/508630/java-equivalent-of-unsigned-long-long)

无符号Long:  `Long.parseUnsignedLong();` `Long.toUnsignedString();` 
> [参考博客: Java 中的无符号类型是怎么回事儿？](https://www.cnblogs.com/yuanyq/p/java_unsigned_types.html)

### Boolean

### Void
- void 的包装类型, 常用于反射时对应上 返回值为void的方法(总得有个类型 Void.TYPE) 该类型在 jdk1.1就有了, 1.5出了泛型后, 又多了一个用途(因为泛型不支持原始类型)

> The Void class is an uninstantiable placeholder class to hold a reference to the Class object representing the Java keyword void.

> [参考博客: What is the need of Void class in Java](https://stackoverflow.com/questions/2352447/what-is-the-need-of-void-class-in-java)

> [参考博客: Uses for the Java Void Reference Type?](https://stackoverflow.com/questions/643906/uses-for-the-java-void-reference-type)

1. 在AOP中, 增强根据切点的返回值类型, 做出不同的逻辑, 有可能用到Void
1. Void 强调 the nothing, null 强调 nothing
1. Void 作为方法的返回值时,只能返回 null 

- 案例:  
    - Future<Void>
    - ResponseEntity<Void> 
    - A `Consumer<T>` can be viewed as a `Function<T, Void>`.
    - A `Supplier<T>` can be viewed as a `Function<Void, T>`

> [official api](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html)

> When you use the visitor pattern it can be cleaner to use Void instead of Object when you want to be sure that the return value will be null. Example: 
```java
    public interface LeavesVisitor<OUT>{
    OUT visit(Leaf1 leaf);
    OUT visit(Leaf2 leaf);
    }
```

> When you will implement your visitor you can explicitly set OUT to be Void so that you know your visitor will always return null, instead of using Object

```java
    public class MyVoidVisitor implements LeavesVisitor<Void>{
        Void visit(Leaf1 leaf){
            //...do what you want on your leaf
            return null;
        }
        Void visit(Leaf2 leaf){
            //...do what you want on your leaf
            return null;
        }
    }
```
****************************
## 枚举类型
> [official doc: enum](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html)

枚举类的构造器必须是private 或者 package private (也就是缺省)

> [参考博客: Java 语言中 Enum 类型的使用介绍](https://www.ibm.com/developerworks/cn/java/j-lo-enum/index.html)
从上面的定义形式来看，似乎 Java 中的枚举类型很简单，但实际上 Java 语言规范赋予枚举类型的功能非常的强大，它不仅是简单地将整形数值转换成对象，而是将枚举类型定义转变成一个完整功能的类定义。

- 简单定义
    - `public enum Color {RED, GREEN, GRAY, BLUE, YELLOW, WHITE, PURPLE, BLACK}`

- 简单单例
```java
    public enum Tool{
        INSTANCE(12); 
        private int num; 
        Tool(int num){
            this.num = num;
        }
        public getNum(){
            return num;
        }
    }
    // 使用的时候
    Tool.INSTANCE.getNum();
```

> [参考博客: 关于java枚举类型的疑问 ](https://segmentfault.com/q/1010000000306839)
> [compilation-error-switch-with-enum](https://stackoverflow.com/questions/5551568/compilation-error-switch-with-enum)

***************************
## 内部类
> 就是一种特殊的成员变量, 其特征和成员属性是一致的

- https://www.tutorialspoint.com/java/java_innerclasses.htm
- https://www.geeksforgeeks.org/anonymous-inner-class-java/

**************************
## 类型强转
> 数学运算时,数据类型自动往大数据类型转: int float double

- Double -> int 直接(int)num;

- int/Integer -> Long 不能隐式转, 需要 Long.valueOf()

**********************

## 时间类型

1. 最早常用是 Date 然后 Calendar 然后Java8: Instant LocalDateTime ...

_获取指定时间_ [获取指定时间的时间戳](https://blog.csdn.net/jssongwei/article/details/71403354)

## 非原生类型
### 元组
> Groovy 中实现了一个元组系统 Tuple 

元组在语言层面, 适合应用于组合少量的多元的数据, 在多种语言中元组都是不可变的

优点: 
1. 元组可以同时存储多种类型元素，且元素类型固定，以保证数据安全， 编译器会对赋值参数类型进行检查
1. 元组的元素个数固定，不允许增加、删除，编译器会严格校验赋值参数个数
1. 无需定义key，但是必要时可以为数据命名，方便数据访问
1. 适合同时遍历多元数据

缺点:
1. 不适合存储大量数据，因为元组不支持append、remove等方法
1. 考虑到工程实际情况，后端使用的语言可能不支持元组，需要转换为其他格式

**************

# 运算
## 除法
整数相除会向下取整, 浮点数相除则是正常数学运算

- `3 / 2 => 1`
- `3 / 2.0 => 1.5`

## 取余
> a % b => `a - (a / b) * b`

所以负数的计算不能想当然, 比如 `-64 % -4 => -64`

## 位运算
> [Bitwise and Bit Shift Operators](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op3.html)

******************
# 类的结构
## 修饰符

### 权限修饰符
> [参考博客: java 权限修饰符](https://blog.csdn.net/yan8024/article/details/6426451)

| 权限修饰符 | 范围 | 注释 |
|:----|:----|:----|
| public | 任意范围 |  |
| protected | 子类/同包 | 子类是可以在任意包的 |
| package private | 同包 | 顾名思义就是包级别的private(缺省) |
| private | 当前类 | 当前类级别private, 内部类从属于当前类 |

> 同包是指 `package xxx;` 是一致的; 而 `package a;` 与 `package a.b;` 不是同包  

### final
### static 
### abstract 

***************

## 成员属性
作为Java的bean, 或者大多数情况下, 属性都是私有的, 然后提供setter getter 方法,而且 一般来说, setter和getter方法是不能包含逻辑的, 也就是简单的赋值 取值
乍一看相比于C语言, 似乎这是多此一举, 但是注意面向对象思想, 一个对象对外提供的应该只是行为, 具有较强的语义性, 什么对象执行了什么方法, 而直接引用就可能将对象属性和静态属性混淆

## 方法
方法的签名: 
- [ ] 方法签名的详解

>1. 关于方法上参数使用 final 修饰的作用: 明确该方法内部不能对参数进行修改, 避免bug

### 方法的传参方式
> [Java 有值类型吗？](http://www.yinwang.org/blog-cn/2016/06/08/java-value-type)

`值类型`: 存储在线程栈里的数据类型，如int型, 以及对象的引用变量  
`引用类型` :存储在托管堆里的数据类型，如Date型，或自定义class对象；

- `值传递`: 每次传递变量时，都是对栈里的原始值进行拷贝，如栈地址0001处存放一个整数值4，值传递时，先copy整数值4，将之存放在栈地址0002处的内存空间，再将栈地址0002进行传递；
- `引用传递`: 每次传递变量时，直接传递栈地址，如栈地址0001处存放一个整数值4，引用传递时，直接传递栈地址0001，而不做复制。

> 总结: Java只有值传递
- 值传递  会创建副本(copy) 所以 函数无法改变原始对象
- 引用传递 不创建副本, 所以 函数中可以改变原始对象

### equals
> [Java提高篇——equals()与hashCode()方法详解](http://www.cnblogs.com/Qian123/p/5703507.html)
> [参考博客: equals()和hashCode()区别？](https://www.cnblogs.com/jesonjason/p/5492208.html)

Object中equals是比较内存地址， hashcode是比较散列函数的值， 后者性能更好，但是可能出现哈希碰撞  
equals相等hashcode一定相等，equals不等 hashcode可能一致可能不一致

> 重写equals方法  
> [参考博客: 关于重写entity的equals()和hashCode()方法的必要性](https://blog.csdn.net/hiroyuki/article/details/6247244) 

Double, Integer, Math, String 都是重写了equals方法， 因此比较的都是值不是内存地址

### hashcode

java.lnag.Object中对hashCode的约定：
1. 在一个应用程序执行期间，如果一个对象的equals方法做比较所用到的信息没有被修改的话，则对该对象调用hashCode方法多次，它必须始终如一地返回同一个整数。
2. 如果两个对象根据equals(Object o)方法是相等的，则调用这两个对象中任一对象的hashCode方法必须产生相同的整数结果。
3. 如果两个对象根据equals(Object o)方法是不相等的，则调用这两个对象中任一个对象的hashCode方法，不要求产生不同的整数结果。但如果能不同，则可能提高散列表的性能。

************

# 抽象类
1. Concrete and Abstract Class

******************

# 继承和接口
> [Lesson: Interfaces and Inheritance](https://docs.oracle.com/javase/tutorial/java/IandI/index.html)

**************
# Object 

> [参考博客:  java的(PO,VO,TO,BO,DAO,POJO)解释](http://www.cnblogs.com/yxnchinahlj/archive/2012/02/24/2366110.html) | [VO DAO BO 等缩写的意义](https://zhuanlan.zhihu.com/p/35762537?group_id=969493512006373376)

- [ ] 原因? 场景是 类继承了一个实现了自定义接口的自定义抽象类

Warning:(18, 1) java: Generating equals/hashCode implementation but without a call to superclass, even though this class does not extend java.lang.Object. If this is intentional, add '@EqualsAndHashCode(callSuper=false)' to your type.

## VO
> (value object) 值对象
1. 使用new关键字创建的, 由GC回收的, 
2. VO是值对象, 业务对象, 存活在业务层的, 是业务逻辑使用的
    - 它存在的目的就是为数据提供一个生存的地方
3. VO的属性是根据当前业务的不同而不同的
    - 也就是说，它的每一个属性都一一对应当前业务逻辑所需要的数据的名称。

## PO
> (persistant object) 持久对象
1. PO则是向数据库中添加新数据时创建，删除数据库中数据时削除的。
    - 并且它只能存活在一个数据库连接中，断开连接即被销毁。
2. PO是持久化对象, 是有状态的, 每个属性代表其当前状态, 他是物理数据的对象表示
    - 使用它能够让我们的程序与物理数据解耦，并且可以简化对象数据与物理数据之间的转换。
3. PO的属性是跟数据库表的字段一一对应的。
4. PO对象需要实现序列化接口

> 首先说PO和VO吧，它们的关系应该是相互独立的，一个VO可以只是PO的部分，也可以是多个PO构成，同样也可以等同于一个PO（当然我是指他们的属性）。
正因为这样，PO独立出来，数据持久层也就独立出来了，它不会受到任何业务的干涉。又正因为这样，业务逻辑层也独立开来，它不会受到数据持久层的影响，业务层关心的只是业务逻辑的处理，至于怎么存怎么读交给别人吧！
不过，另外一点，如果我们没有使用数据持久层，或者说没有使用hibernate，那么PO和VO也可以是同一个东西，虽然这并不好。

## TO
> (transfer Object) 数据传输对象
- 在应用程序不同tie(关系)之间传输的对象

## BO
> (business object) 业务对象
- 从业务模型的角度看,见UML元件领域模型中的领域对象。封装业务逻辑的java对象,通过调用DAO方法,结合PO,VO进行业务操作。
- 它装满了业务逻辑的处理，在业务逻辑复杂的应用中有用。

## POJO
> [Wikipedia: POJO](https://en.wikipedia.org/wiki/Plain_old_Java_object) `Plain Old Java Object`

> (plain ordinary java object) 简单无规则java对象
- 纯的传统意义的java对象。就是说在一些Object/Relation Mapping工具中，能够做到维护数据库表记录的persisent object完全是一个符合Java Bean规范的纯Java对象，没有增加别的属性和方法。我的理解就是最基本的Java Bean，只有属性字段及setter和getter方法！

## DAO
> (data access object) 数据访问对象
- 通常和PO结合使用，DAO中包含了各种数据库的操作方法

*************************
# 关键字
>  Java关键字和保留字

|||||||||
|:----|:----|:----|:----|:----|:----|:----|:----|
| abstract | class    | extends | implements | null      | strictfp     | true
| assert   | const    | false   | import     | package   | super        | try
| boolean  | continue | final   | instanceof | private   | switch       | void
| break    | default  | finally | int        | protected | synchronized | volatile
| byte     | do       | float   | interface  | public    | this         | while
| case     | double   | for     | long       | return    | throw
| catch    | else     | goto    | native     | short     | throws
| char     | enum     | if      | new        | static    | transient

- [ ]  transient 序列化时不进行序列化

## try 
> try catch finally 

- [StackOverFlow: Try-catch-finally in java](https://stackoverflow.com/questions/7143788/try-catch-finally-in-java)

- There are at least 3 OTHER cases where the finally block is not executed: 
    1. if the try block or a catch block goes into an infinite loop, or blocks for ever
    1. if something (e.g. a JNI bug) causes the JVM to crash
    1. if there is a machine outage (power failure, hardware error, etc). 
