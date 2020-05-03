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
    1. [标准输入输出](#标准输入输出)
    1. [Runtime](#runtime)
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
        1. [finalize](#finalize)
    1. [JavaDoc](#javadoc)
1. [抽象类](#抽象类)
1. [对象](#对象)
1. [继承和接口](#继承和接口)
    1. [常见接口](#常见接口)
        1. [Serializable](#serializable)
1. [Object](#object)
    1. [VO](#vo)
    1. [PO](#po)
    1. [TO](#to)
    1. [BO](#bo)
    1. [POJO](#pojo)
    1. [DAO](#dao)
1. [关键字](#关键字)
    1. [try](#try)
    1. [transient](#transient)

**目录 end**|_2020-04-27 23:42_|
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
    - `for(Object item:list){}` 注意 list对象如果是通过`调用一个对象的方法`返回的，那么只会调用一次该方法

## 标准输入输出
> 系统标准输入
- `Scanner scanner = new Scanner(System.in);`

> 系统标准输出
- `System.out.println("")` 并在末尾追加换行
    - .print() 输出, 行末不换行
    - .printf() 格式化输出, 和C语法类似

## Runtime
> Runtime.getRuntime().addShutdownHook(Thread thread) 
1. 在JVM正常退出时会调用注册的Hook
1. 例如 System.exit(), 或者 Java 进程收到退出的信号 SIGTERM SIGINT SIGQUIT 等等, 但是暴力退出是不会被调用到Hook的

***********************
# 数据类型
> [Primitive Data Types](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)

## 自动拆装箱
> 在日常Java开发中, 基本数据类型和包装类型是可以视为等价的(唯一差别就是包装类型能表达null), 就是因为自动拆装箱的存在

| 基本数据类型 | 包装类型 |
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

> 区别
- 存储方式及位置的不同，基本类型是直接存储变量的值保存在堆栈中能高效的存取，包装类型需要通过引用指向实例，具体的实例保存在堆中。
- 初始值的不同，封装类型的初始值为 null，基本类型的的初始值视具体的类型而定，比如int类型的初始值为0，boolean类型为false；
- 使用方式的不同, 在泛型场合只能使用包装类型, 基本类型无法表达 null

> 存在的意义
1. 基本类型无法作为对象看待, 扩充了语义
1. 为了泛型

> 弊端
1. 性能问题, 需要构造对象

************************

> 注意自动拆装箱是编译器的语法糖   
> 自动装箱都是通过包装类的 valueOf() 方法来实现的.  
> 自动拆箱都是通过包装类对象的 xxxValue() 来实现的.

## 基础数据类型
> 八种基本数据类型 byte char boolean short int long float double

以特定进制声明数值 0b 二进制 0 八进制 0x 十六进制

> [The Java™ Tutorials: Primitive Data Types](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)  

> [参考: Java 有值类型吗？](http://www.yinwang.org/blog-cn/2016/06/08/java-value-type)

确实, 这样来看Java没有值类型才是更统一的, 不过有没有对程序都是一样的, 因为Java没有解引用, 基本数据类型又没有成员, 所以值还是引用, 没差

### byte
> 字节 -128, 127, 表示 8位 一个字节 的值

### char

用 2 个字节来表示 Unicode 值 取值范围: '\u0000' (or 0) , '\uffff' (or 65,535 inclusive).

> [参考: isn't the size of character in java 2 bytes](https://stackoverflow.com/questions/5078314/isnt-the-size-of-character-in-java-2-bytes)  

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
> `wrapper class` 基本类型和包装类型不能混为一谈 本质上的 class是不同的, 只不过自动拆装箱才让人感觉没差别

|  |  |
|:----|:----|
| Integer.TYPE | int.class |
| Byte.TYPE    | byte.class |
| Boolean.TYPE | boolean.class |
| Double.TYPE  | double.class |
| Void.TYPE    | void.class |

***************************

> 封装类型的缓存行为 

Integer, 有 IntegerCache 类缓存 [-128, 127] 范围内的值. 可以通过 `-XX:AutoBoxCacheMax` 修改上限值  
且 Byte Short Long Character 都有对应的缓存对象和缓存值范围, 但是只有Integer的缓存范围可变  

Byte, Short, Long 有固定范围: [-128, 127]   
Character  范围是 ‘\u0000’ 至 ‘\u007f’ 即 [0,127]  

true 和 false 也是缓存了的

> 可能造成的困惑
```java
    assert Integer.valueOf(1) == Integer.valueOf(1);
    assert Integer.valueOf(128) != Integer.valueOf(128);
```

### String
> 该类是final修饰的, 原因:[知乎问题](https://www.zhihu.com/question/31345592)

字符串对象是不可变的，这意味着一旦创建，它们的值就不能更改。 String类在技术上不是基本数据类型，但考虑到语言给予它的特殊支持，倾向于将其视为基本数据类型。

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

无符号Long: `Long.parseUnsignedLong();` `Long.toUnsignedString();` 

> [参考: Java 中的无符号类型是怎么回事儿？](https://www.cnblogs.com/yuanyq/p/java_unsigned_types.html)

### Boolean
> 内含两个单例 TRUE FALSE

### Void
- void 的包装类型, 常用于反射时对应上 返回值为void的方法(总得有个类型 Void.TYPE) 该类型在 jdk1.1就有了, 1.5出了泛型后, 又多了一个用途(因为泛型不支持原始类型)

> The Void class is an uninstantiable placeholder class to hold a reference to the Class object representing the Java keyword void.

> [参考: What is the need of Void class in Java](https://stackoverflow.com/questions/2352447/what-is-the-need-of-void-class-in-java)

> [参考: Uses for the Java Void Reference Type?](https://stackoverflow.com/questions/643906/uses-for-the-java-void-reference-type)

1. 在AOP中, 增强根据切点的返回值类型, 做出不同的逻辑, 有可能用到Void
1. Void 强调 the nothing, null 强调 nothing
1. Void 作为方法的返回值时, 只能返回 null 

- 案例:
    - Future<Void>
    - ResponseEntity<Void> 
    - A `Consumer<T>` can be viewed as a `Function<T, Void>`, 没有返回值,只有入参
    - A `Supplier<T>` can be viewed as a `Function<Void, T>`, 没有入参,只有返回值

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

************************

## 枚举类型
> [official doc: enum](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html)

枚举类的构造器必须是 private 或者 package private (也就是缺省)

> [参考: Java 语言中 Enum 类型的使用介绍](https://www.ibm.com/developerworks/cn/java/j-lo-enum/index.html)

从上面的定义形式来看，似乎 Java 中的枚举类型很简单，但实际上 Java 语言规范赋予枚举类型的功能非常的强大，它不仅是简单地将整形数值转换成对象，而是将枚举类型定义转变成一个完整功能的类定义。

- 简单定义
    - `public enum Color {RED, GREEN, GRAY, BLUE, YELLOW, WHITE, PURPLE, BLACK}`

> 简单单例
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

> [参考: 关于java枚举类型的疑问 ](https://segmentfault.com/q/1010000000306839)  
> [compilation-error-switch-with-enum](https://stackoverflow.com/questions/5551568/compilation-error-switch-with-enum)  

***************************
## 内部类
> 可看做一种特殊的成员变量, 其特征和成员属性是一致的

- https://www.tutorialspoint.com/java/java_innerclasses.htm
- https://www.geeksforgeeks.org/anonymous-inner-class-java/

**************************

## 类型强转
> 数学运算时,数据类型自动往大数据类型转: int float double

- Double -> int 直接(int)num;
- int/Integer -> Long 不能隐式转, 需要 Long.valueOf()

**********************

## 时间类型
> java.time 包

> [Java8 JavaDoc: DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html)`注意格式化中字符的准确含义`

1. 最早常用是 Date 然后 Calendar  目前Java8: Instant LocalDateTime Duration ...

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

************************

# 运算
## 除法
整数相除会向下取整, 浮点数相除则是正常数学运算

- `3 / 2 => 1`
- `3 / 2.0 => 1.5`

## 取余
> a % b => `a - (a / b) * b`

取模运算（Modulo Operation）和取余运算（Complementation）两个概念有重叠的部分但又不完全一致。  
主要的区别在于对负整数进行除法运算时操作不同。取模主要是用于计算机术语中。取余则更多是数学概念。

对于整型数a，b来说，取模运算或者求余运算的方法都是：
1. 求整数商： c = a / b;
2. 计算模或者余数： r = a - c * b.

求模运算和求余运算在第一步不同: 取余运算在取c的值时，向0 方向舍入(fix()函数)；而取模运算在计算c的值时，向负无穷方向舍入(floor()函数)。  

例如计算：-7 Mod 4 :  a = -7；b = 4；  
- 第一步：求整数商c，如进行求模运算c = -2（向负无穷方向舍入），求余c = -1（向0方向舍入）；  
- 第二步：计算模和余数的公式相同，但因c的值不同，求模时r = 1，求余时r = -3。

归纳：  
当a和b符号一致时，求模运算和求余运算所得的c的值一致，因此结果一致。  
当符号不一致时，结果不一样。求模运算结果的符号和b一致，求余运算结果的符号和a一致。

另外各个环境下%运算符的含义不同，比如c/c++，java 为取余，而python则为取模。

## 位运算
> [Bitwise and Bit Shift Operators](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op3.html)

当length是2的n次方: hash%length==hash&(length-1) 

******************
# 类的结构
## 修饰符

### 权限修饰符
> [参考: java 权限修饰符](https://blog.csdn.net/yan8024/article/details/6426451)

| 权限修饰符 | 范围 | 注释 |
|:----|:----|:----|
| public | 任意范围 |  |
| protected | 子类/同包 | 子类是可以在任意包的 |
| package private | 同包 | 顾名思义就是包级别的private(缺省) |
| private | 当前类 | 当前类级别private, 内部类从属于当前类 |

> 同包是指 `package xxx;` 语句完全一样, 而 `package a;` 与 `package a.b;` 不是同包  

### final

### static 

### abstract 

***************

## 成员属性
作为Java的bean, 或者大多数情况下, 属性都是私有的, 然后提供setter getter 方法,而且 一般来说, setter和getter方法是不能包含逻辑的, 也就是简单的赋值 取值
乍一看相比于C语言, 似乎这是多此一举, 但是注意面向对象思想, 一个对象对外提供的应该只是行为, 具有较强的语义性, 什么对象执行了什么方法, 而直接引用就可能将对象属性和静态属性混淆

## 方法
- 方法签名 [Defining Methods](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html)
    - 作用域
    - 泛型列表 可选
    - 返回类型
    - 方法名 
    - 参数列表 可选
    - 异常列表 可选
    - 方法体

>1. 关于方法上参数使用 final 修饰的作用: 明确该方法内部不能对参数进行修改

### 方法的传参方式
> [Java 有值类型吗？](http://www.yinwang.org/blog-cn/2016/06/08/java-value-type)`仅作思考`  
> [这一次，彻底解决Java的值传递和引用传递](https://juejin.im/post/5bce68226fb9a05ce46a0476)`C++ C# 都支持，C Java 仅支持值传递`  

- `实参`：方法调用前就完成初始化或为null，方法调用时传入，在Java中就是调用时被复制
- `形参`： 声明在方法参数列表内，仅在函数调用的时候进行申请内存空间，函数调用结束就释放该内存空间

- `值类型`: 存储在线程栈中的数据类型，如int型, 以及对象的引用变量  
- `引用类型` :存储在堆中数据的数据类型，如Date型，或自定义class对象；

- `值传递`: 每次传递变量时，都是对栈里的原始值进行拷贝
    - 如栈地址0001处存放一个整数值4，值传递时，先copy整数值4，将之存放在栈地址0002处的内存空间，再将栈地址0002作为形参传入方法；
- `引用传递`: 每次传递变量时，直接传递栈地址，如栈地址0001处存放一个整数值4，引用传递时，直接传递栈地址0001，而不做复制。

> 总结: Java只有值传递  
- 值传递  会创建副本(copy) 所以 函数无法改变实参对象的`值`(值类型) 
    - 但是如果传入的是引用类型 会复制一份地址值，就可以通过地址值更改实参对象的`成员属性值`

注意 如果是 引用传递 不创建副本, 实参和形参地址是一致，所以 函数中一定可以改变原始对象

### equals
> [Java提高篇——equals()与hashCode()方法详解](http://www.cnblogs.com/Qian123/p/5703507.html)
> [参考: equals()和hashCode()区别？](https://www.cnblogs.com/jesonjason/p/5492208.html)

- Object中equals是比较内存地址， hashcode是比较散列函数的值， 后者性能更好，但是可能出现哈希碰撞  
- equals相等hashcode一定相等，equals不等 hashcode可能一致可能不一致

> 重写equals方法  
> [参考: 关于重写entity的equals()和hashCode()方法的必要性](https://blog.csdn.net/hiroyuki/article/details/6247244) 

Double, Integer, Math, String 都是重写了equals方法， 因此比较的都是值不是内存地址

### hashcode

java.lnag.Object中对hashCode的约定：
1. 在一个应用程序执行期间，如果一个对象的equals方法做比较所用到的信息没有被修改的话，则对该对象调用hashCode方法多次，它必须始终如一地返回同一个整数。
2. 如果两个对象根据equals(Object o)方法是相等的，则调用这两个对象中任一对象的hashCode方法必须产生相同的整数结果。
3. 如果两个对象根据equals(Object o)方法是不相等的，则调用这两个对象中任一个对象的hashCode方法，不要求产生不同的整数结果。但如果能不同，则可能提高散列表的性能。

### finalize

************************

## JavaDoc

- @author
- @version
- @param
- @return
- @exception/@throws
- @see
- @since
- @serial/@serialField/@serialData
- @deprecated

- {@link BurgersManager} 指向一个类
- {@link BurgersManager burgers manager} 指向带有标签的类
- {@link #eat(Burger, boolean)} 指向此类中的某个方法
- {@link #eat(Burger, boolean) eat} 指向此类中带有标签的某个方法
- {@link BurgersManagers#eat(Burger, boolean)} 指向其他类中的某个方法
- {@link BurgersManagers#eat(Burger, boolean) burgers manager eat} 指向其他带有标签的类的某个方法

************************

# 抽象类
1. Concrete and Abstract Class

************************

# 对象
> [参考: 计算Java对象内存大小](https://www.cnblogs.com/E-star/p/10222250.html)  

************************

# 继承和接口
> [Lesson: Interfaces and Inheritance](https://docs.oracle.com/javase/tutorial/java/IandI/index.html)

## 常见接口

### Serializable
> 序列化接口

1. serialVersionUID
    - 该属性可显式声明，若没有则编译器会 根据类名、接口名、成员方法及属性等来生成一个64位的哈希字段 
    - 该属性的作用：如果显式声明且值保持一致，那么类的变动(增加或删除属性)能被兼容(改动的属性忽略或没有值))，如果没有设置则会导致反序列化异常


************************

# Object 

> [参考:  java的(PO,VO,TO,BO,DAO,POJO)解释](http://www.cnblogs.com/yxnchinahlj/archive/2012/02/24/2366110.html) | [VO DAO BO 等缩写的意义](https://zhuanlan.zhihu.com/p/35762537?group_id=969493512006373376)

- [ ] 原因? 场景是 类继承了一个实现了自定义接口的自定义抽象类

Warning:(18, 1) java: Generating equals/hashCode implementation but without a call to superclass, even though this class does not extend java.lang.Object. If this is intentional, add '@EqualsAndHashCode(callSuper=false)' to your type.

## VO
> view object 前端展示对象
1. 前后端分离项目中VO代表给前端展示接口使用

************************

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
- 例如 RPC 接口中的对象 UserTO

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

## try 
> try catch finally 

- [StackOverFlow: Try-catch-finally in java](https://stackoverflow.com/questions/7143788/try-catch-finally-in-java)

- There are at least 3 OTHER cases where the finally block is not executed: 
    1. if the try block or a catch block goes into an infinite loop, or blocks for ever
    1. if something (e.g. a JNI bug) causes the JVM to crash
    1. if there is a machine outage (power failure, hardware error, etc). 

## transient
> 该关键字修饰的属性 在对象序列化时不参与序列化
