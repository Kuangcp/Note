---
title: Scala
date: 2018-12-15 12:09:46
tags: 
    - 基础
categories: 
    - Scala
---

**目录 start**

1. [Scala](#scala)
    1. [安装](#安装)
    1. [基础了解](#基础了解)
    1. [基础语法](#基础语法)
    1. [适合Scala使用的场景](#适合scala使用的场景)
        1. [Scala和Java的比较](#scala和java的比较)
        1. [Scala特性](#scala特性)
            1. [类型推断](#类型推断)
            1. [方法](#方法)
            1. [导入](#导入)
            1. [循环控制结构](#循环控制结构)
            1. [函数式编程](#函数式编程)
        1. [Scala对象模型](#scala对象模型)
        1. [数据结构和集合](#数据结构和集合)
        1. [actor](#actor)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Scala
> [Official tour](https://docs.scala-lang.org/tour/tour-of-scala.html)

> [Groovy创始人：Java面临终结 Scala将取而代之](http://developer.51cto.com/art/200907/134785.htm)

> [参考: 20 Best Scala Books To Go From Beginner To Expert](https://whatpixel.com/best-scala-books/)
## 安装
- 通过sdkman安装，或者下载解压配置环境变量 [sdkman使用](/Skills/usually_app.md)

## 基础了解
`特性`
- Scala语言的精炼，包括类型推断的能力
- match 表达式， 以及模式和case类等相关概念
- Scala的并发，采用消息和acto机制，而不是像Java代码那样用老旧机制的锁机制

`简洁的基础语法`
- 类的定义和类的构造方法是同一个东西。Scala中可以有其他的辅助构造方法，
- 类默认是公开的，所以没必要加上public关键字
- 方法的返回类型是通过类型推断确定的，但要在定义的方法的def从句中用等号高数编译器做类型推断
- 如果方法体只是一条语句或表达式， 那就没有必要用大括号括起来
- Scala不像Java一样有原始类型。数字类型也是对象

*****************
```scala
    object HelloWorld {
        def main(args:Array[String]){
            val hello = "Hello World!"
            println(hello)
        }
    }
```
`针对这个简单示例的语法特性`
- 关键字object声明这个类是单例类
- main方法 缺省了关键字 public static 
- 不必声明hello的类型，编译器会自行推断
- 无需声明main方法的返回类型 编译器会自动设为 Unit 等价于Java中的void
- 和Java Groovy不一样的是，变量的类型在变量之后
- 方括号 [] 表示泛型，所以类型参数的表示方法是`Array[String]` 不是 String[]
- Array是纯正的泛型
- 集合类型必须指明泛型 不能像Java那样声明生类型（指不带类型参数的泛型类或接口。）
    - 例如泛型类 `Box<T>` 创建其参数化类型时要指明类型参数的真实类型 Box<Integer>intBox = new Box<>(); 
    - 如果忽略了类型参数，Box rawBox = new Box();则是创建了一个生类型
- 分号绝对是可选的
- val 就相当于Java中的final变量，用于声明一个不可变量
- Scala应用程序的初始入口总是在Object中

`match表达式`
- 最简单的match用法跟Java的switch差不多，但是match表达力更强
```scala
    var transFer = args(0) match{
        case "one" => "1"
        case "Two" => "2"
        case _ => "Error: '"+args(0)+"' "
    }
    println(transFer)
```

- 从语言的纯粹性来看，Scala语法比Java更清晰，也更正规：
    - 默认case 不需要另外一个不同的关键字
    - 单个case 不会像Java那样进入下一个case，所以也就不需要break
- 关键字var 用来声明一个可变（非final）变量。没有必要尽量不要使用它
- 数组用圆括号访问 argvs(0) 就是main方法的第一个参数
- 默认case 就是case _
- Scala支持间接方法调用，所以可以把args(0).match({...}) 写成 args(0) match({...})

```scala
    def autoType(obj: Any) = obj match{
        case s: String => s.length
        case i: Int  => 4
        case _:   => -1
    }
```
- 这个方法以一个未知类型值为参数，然后用模式分别处理String Int类型的值

`case类`
- match 表达式的最强用法之一就是和case类（可以看成是枚举概念面向对象的扩展）相结合
- 例如一个 温度过高发出警告的例子：
    - `case class TemperatureAlarm(temp: Double)` 这一行就定义个一个有效的case类，相比于Java简化了很多
    - `var alarm = TemperatureAlarm(99.9)` 创建case实例不需要关键字 new
    - 这进一步强化了case类是类似于 参数化枚举类型 或某种形式的值类型的观点
- Scala中的相等：Scala认为Java用 == 表示引用相等是个错误。所以在Scala中，== 和 equals是一样的，如果需要判断引用相等，可以用 ===
    - case类 equals 方法只有在两个实例的所有参数值都一样时才会返回true
- caes类和构造器模式非常合

`actor`
- Scala选择actor机制来实现并发编程。提供了一个异步并发模型，通过在代码单元间传递消息实现并发。这种并发模型比Java提供的基于锁的机制，默认共享的并发模型更易用，不过Scala的底层模型也是JVM

*******************************
## 基础语法
`运行`
1. 可以进入REPL终端，和Python类似
1. 也可以使用`scalac scala`就像`javac java`先进行编译然后再运行字节码
1. 或者`scala 文件`解释运行

`包`
1. 第一种方法和 Java 一样，在文件的头定义包名，这种方法就后续所有代码都放在该包中。 比如：
    ```scala
        package com.runoob
        class HelloWorld
    ```
1. 第二种方法有些类似 C#，如：
    ```scala
        package com.runoob {
        class HelloWorld 
        }
    ```

`Scala数据类型`
|数据类型|描述|
|:---|:---|
|Byte 	|8位有符号补码整数。数值区间为 -128 到 127|
|Short 	|16位有符号补码整数。数值区间为 -32768 到 32767|
|Int 	|32位有符号补码整数。数值区间为 -2147483648 到 2147483647|
|Long 	|64位有符号补码整数。数值区间为 -9223372036854775808 到 9223372036854775807|
|Float 	|32位IEEE754单精度浮点数|
|Double 	|64位IEEE754单精度浮点数|
|Char 	|16位无符号Unicode字符, 区间值为 U+0000 到 U+FFFF|
|String 	|字符序列|
|Boolean 	|true或false|
|Unit 	|表示无值，和其他语言中void等同。用作不返回任何结果的方法的结果类型。Unit只有一个实例值，写成()。|
|Null 	|null 或空引用|
|Nothing 	|Nothing类型在Scala的类层级的最低端；它是任何其他类型的子类型。|
|Any 	|Any是所有其他类的超类|
|AnyRef 	|AnyRef类是Scala里所有引用类(reference class)的基类|

`定义变量`
- 定义无类型 变量 `var name` 常量 `val name`
- 定义变量加上类型 `var VariableName : DataType [=  Initial Value]` 常量同理
- 如果在没有指明数据类型的情况下声明变量或常量必须要给出其初始值，否则将会报错。
    - 变量`var myVar = 10;`
    - 常量`val myVal = "Hello, Scala!";`
- 声明多个变量 `val xmax, ymax = 100  // xmax, ymax都声明为100`

- Scala 访问修饰符基本和Java的一样，分别有：`private，protected，public`
- [Scala操作符](http://www.runoob.com/scala/scala-operators.html)

*******************
`函数`
- 函数签名： `def functionName ([参数列表]) : [return type] ={}`
    - 如果你不写等于号和方法主体，那么方法会被隐式声明为"抽象(abstract)"，包含它的类型于是也是一个抽象类型。
    - 方法定义由一个`def`关键字开始，紧接着是可选的参数列表，`一个冒号"：" 和方法的返回类型`，`一个等于号"="，最后是方法的主体`。
    - 以上代码中 return type 可以是任意合法的 Scala 数据类型。参数列表中的参数可以使用逗号分隔。
    - 如果函数没有返回值，就是返回为 Unit，这个类似于 Java 的 void,
- 函数调用：
    - functionName( 参数列表 )
    - [instance.]functionName( 参数列表 )
- [函数的概念解析](http://www.runoob.com/scala/scala-functions.html)

## 适合Scala使用的场景
### Scala和Java的比较
- ![比较Scala和Java](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Book/Java7Developer/p220.jpg)
- 该表主要对这两种语言的主要差异做了汇总，语言的表皮层是指该语言关键字的数量和开发人员用它干活必须掌握的独立语言结构的数量

### Scala特性
#### 类型推断
- Scala是静态语言，但是Scala能根据上下文推断变量类型，所以让Scala更有动态语言的感觉
    - Java也有类型推断，例如泛型钻石语法，Java的类型推断通常是用在赋值语句等号右边的值上。
    - Scala通常是推断变量而不是值的类型，但是Scala的确也能推断值的类型

```scala
def len(obj: AnyRef) = {
    obj.toString.length
}
```
- 这是一个类型推断的方法。通过检查返回代码中的java.lang.String#length的类型（int），编译器知道这个方法要返回Int类型的值。
- 注意这个方法没有显式的指定返回类型，不需要return关键字，如果用了return反而是错误的
- 如果连def中的 = 也省略，编译器就会返回Unit
- 类型推断有两个受限的情况：
    - 方法声明中参数的类型，传给方法的参数必须指定类型
    - 递归函数，Scala不能推断递归函数的返回类型

#### 方法
- Scala没有static关键字，与之相对应的是 object结构中的方法，其中有个 伴生对象
- 与Groovy和Clojure相比，Scala语言的运行要重的多，Scala类，会有很多由平台自动生成的额外方法
- 方法调用是Scala的核心概念， Scala中没有Java那种意义上的操作符
- Scala的方法名是灵活的，甚至可以出现操作符，例如 `+` 这个方法。Scala不再把操作符当做一个独立概念

> Scala认为所有的东西都是对象，所以可以在任何东西上调用方法，即使是Java里的原始变量

```scala
def fact(base: Int) : Int = {
    if(base < 0){
        print("负数没有阶乘 ：")
        return base
    }
    if(base == 0){
        return 1
    }else{
        return base * fact(base - 1)
    }
}
```
- 这个方法的定义和Java很相似，都有返回值，并用return关键字明确返回值，唯一的差别就是 函数代码块定义之前加 = 
- Scala还有一个Java中没有的概念：局部函数。像一个私有的内部类，封装了具体细节

#### 导入
- `import java.io.File` 普通导入
- `import java.net._` 通配导入
- `import scala.collection.{Map, Seq}` 导入包下多个类
- `import java.util.{Date => UDate}` 导入类并取别名
- import语句不像Java一样只能放在文件顶部，可以将import单独分离出来，Scala也有默认导入 即：scala._

#### 循环控制结构
- for循环
> Scala采用函数式编程中的概念 列表推导式 来实现for循环
```scala
    // 条件for循环
    for (i <- 1 to 10; if i%2 ==0){
        println(i)
    }
    // 多变量循环
    for(x<- 1 to 16; y<- 1 to x){
        println(" "*(x-y) + x.toString * y)
    }
    // 一次新建，多次使用
    val xs = for(x <- 2 to 11) yield x
    for(factx <- xs) println(factx)
```
- 列表推导式的一般概念是对一个列表中的元素进行转换，这会产生一个新列表。
    - 例如上的的例子，就是先生成一个xs集合，然后第二个for进行遍历。 创建一次，使用多次

#### 函数式编程
- 函数字面值或者是匿名函数， 其中的关键是 => Scala用它来表示取得参数列表并传递到代码块中 `(<函数参数列表>) => {...}`
- 普通函数，入参是int，返回值是int：`val doubler = (x: Int) => {2*x}`
- 入参是函数字面值，返回值是函数字面值： `val adder = (n: Int) => {(x: Int) => x+n}`定义一个可以加任意数的函数 
    - `val plus2 = adder(2)` 定义一个将入参 加2的函数

### Scala对象模型
### 数据结构和集合
### actor


********
`何时以及如何开始使用Scala`
- 有信心评估所需的工作量
- 问题域边界明确，定义清晰
- 需求说明明确
- 与其他组件的互操作需求已知
- 确定了愿意学习新语言的开发人员

`可能不适合当前项目的迹象`
- 受到了业务小组和其他程序支持小组的抵制或缺乏动力
- 开发团队没有明显的学习Scala的动力
- 小组中存在分帮结派或政治上存在巨大分歧
- 小组中高级技术人员的支持力度不够
- 截止日期太紧张

