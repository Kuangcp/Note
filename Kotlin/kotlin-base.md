# Kotlin学习

## 1、基础学习

### 1、[变量](./src/main/kotlin/hht/dragon/java/variable/VariableStudy.kt)

#### 1、申明变量和值

Kotlin的变量分为可变的`var`和不可变的`val`

-   `var`：可写的，在生命周期中可被多次赋值

-   `val`：只读的，仅能一次赋值，后面就不能被重新赋值

### 2、变量类型推断

在Kotlin中，大部分情况不需要说明你使用对象的类型，编译器可以直接推断出它的类型。但是，类型推断不是所有的。例如，整型变量Int不能赋值Long变量

-   使用`is`运算符进行类型检测

```
if (obj is String) {
            // 在该处obj自动转换成String
            println(obj::class)
            result = obj.length
            println(result)
        }
```

### 3、原始字符串与模板表达式

-   原始字符串：有三重引号`"""`分隔（与Python一样），原始字符串可以包含换行符和任何其他字符

```
fun rawString() {
        val rawString = """
             // 使用is进行类型检测
    fun getLength(obj: Any): Int? {
        var result = 0
        if (obj is String) {
            // 在该处obj自动转换成String
            println(obj::class)
            result = obj.length
            println(result)
        }
        println(obj::class)
        return result
    }/n
        """.trimIndent()
        println(rawString)
    }
```

-   模板表达式：以美元符号开始

```
// 模板表达式
val s = "$rawString has ${rawString.length} characters."
println(s)
```

### 2、流程控制语句

-   [If表达式](./src/main/kotlin/hht/dragon/java/processcontrol/IfExpression.kt)
    
    > Kotlin中的if是一个表达式，可返回一个值， 这种情况下类似于Java中的三元表达式
    
    ```
    val max = if (a > b) a else b
    ```
    > 也可向传统的If表达式样使用。
    
    -   if-else语句规则（与Java中的基本相同）
    
        -   if后的括号不能省略，括号内的表达式的值必须为布尔值
        
        -   如果条件体内只有一条语句执行，那么if后面的大括号可以省略，但建议加上大括号
        
        -   对于给定的if，else语句是可选的，else if也是可选的
        
        -   else和else if同时出现时，else必须出现在else if后面
        
        -   如果有多条else if语句同时出现，那么如果有一条else if语句的表达式测试成功，那么会忽略其他所有else if和else分支
        
        -   如果出现多个if，只有一个else的情况，else子句归属于内层的if语句
        
-   [when表达式](./src/main/kotlin/hht/dragon/java/processcontrol/WhenExpression.kt)

    > 类似与switch-case表达式
    
    -   如果有多个分支需要用相同的操作，则可以将多个分支条件放在一起，用逗号分开
    
    ```
    when (obj) {
         -1, 0 -> println("-1 or 0")
         else -> {
             println("else")
         }
    }
    ```
    
    -   也可以检测一个是否在一个区间或集合中
    
    ```kotlin
    fun whenIn(x: Int) {
        val nums = arrayOf(1, 2, 3, 21)
        when (x) {
            in 1..10 -> print("在1~10之中")
            in nums -> print("在数组中")
            !in 10..20 -> print("不在10~20中")
        }
    }
    ```
   
-   [for循环](./src/main/kotlin/hht/dragon/java/processcontrol/ForWxpression.kt)

    -   格式
    
    ```
    for (item in collection) {
        ...
    }
    ```

-   while循环

    > while和do..while循环和Java中的类似
    
-   break、continue和return的使用与Java中的一致,但Kotlin中也可使用`=`来直接返回一个函数的值，如`fun sum(a: Int, b: Int) = a + b`

-   [标签](./src/main/kotlin/hht/dragon/java/processcontrol/LabelExpression.kt)

    > 可显示的指定标签，也可隐式的使用标签，当隐式的使用标签时，该标签与接收lambda的函数同名
    
-   throw表达式

    > 在Kotlin中throw是表达式，它的类型是特殊类型：Nothing，该类型没有值，与Java中的void的意思相同  
    > 如果把一个throw表达式的值赋给一个变量，需要显示声明类型为Nothing。
    
### 3、关键字

-   this

> 基本使用方法与Java类似，指持有当前对象的引用。但如果this没有限定符，则它指的是最内层的包含他的作用域，如果想要引用其他作用域中的this则可以使用`this@label`标签，如[事例](./src/main/kotlin/hht/dragon/java/keywords/ThisKeyword.kt)

-   super

> 与Java中的super关键字类似，指持有指向其父类的引用

### 4、与Java中不同的操作符

-   相等与不等操作符

    -   引用相等与不等：`===`和`!==`,判断两个引用是否是指向同一对象
    
    -   结构相等与不等：`==`和`!=`,是使用equals()进行判断
    
-   Elvis操作符`?:`

    > 特定是和null比较，主要用来做null安全检查, 如`y = x?:0`,等价于`val y = if (x !=== null) x else 0`  
    > Elvis操作符和Java中的三元条件运算符相似，但在Kotlin中没有三元条件运算符，Elvis操作符也为二元运算符
    
-   [扩展函数和扩展属性](./src/main/kotlin/hht/dragon/java/expand/Expand.kt)

    -   扩展函数,大多数情况可以在顶层定义扩展，即直接在包中定义，这样便可在这整个包中使用。如下，在String中扩展notEmpty()方法
    
    ```kotlin
    fun String.notEmpty(): Boolean {
        return !this.isEmpty()
    }
    
    fun main(args: Array<String>) {
        "123".notEmpty()
    }
    ```
    
    -   扩展属性,如：`val <T> List<T>.lastIndex: Int get() = size - 1`
    
-   空指针安全

    -   一个非空引用不能直接赋为null
    
    -   若需要为空，则可以在变量的类型后面加上`?`声明一个变量可空，如：`var s: String? = "ad"`
    
    -   若声明了一个可空的String，然后调用length属性时，编译器将报错，这是可使用安全调用`?.`和非空断言调用`!!.`, 如`s?.length`和`s!!.length`。可空变量的安全调用符`y?.length`等价于是Java中的`y != null ? Integer.valueOf(yy.length()) : null`，可空变量的断言调用`y!!.length`等价的Java代码为：`if (y == null) { Internsics.throwNpe(); } return Integer.valueOf(y.length());`
    
    -   如果只对非空值进行操作，那么安全调用操作符可与`let`一起使用，如：`s?.let { println(s) }`
    
### 5、异常捕获

-   Kotlin中仍然可使用`try...catch`捕获并处理异常

### 6、Unit类型

> Kotlin中的Unit类型实现了与Java中的void一样的功能。不同的是，当一个函数没有返回值时，我们用Unit来表示这个特征，而不是null。  
> 大多数情况下，我们并不需要显示地返回Unit类型，或者声明一个函数的返回类型为Unit。编译器会自动推断它

### 7、Nothing类型

> Kotlin中没有Java和C中的类似函数灭有返回值的标记void，但是拥有一个对应的Nothing。在Java中，返回void的方法，其返回值void是无法被访问到的。

-   Unit和Noting的区别

    > Unit类型表达式计算结果的返回值类型是Unit。Noting类型的表达式计算结果是永远不会被返回的。
    
## 2、 集合类

> Kotlin的集合类分为：`可变集合类`和`不可变集合类`, 集合类型主要分为：`List`、`set`和`map`

### 1、List

#### 1、创建

-   不可变集合类List(ReadOnly, Immutable)
    
    > 使用`listOf`函数构建一个不可变的List
    
    -   使用listOf()构建一个没有元素的List, 该情况下必须指定类型
        `val list: List<Int> = listOf()`
        
    -   使用listOf创建一个只有1个元素的List
        `val list_1 = listOf(1)`
        
    -   使用listOf创建一个有多个元素的List
        `val list_2 = listOf(0, 1, 2)`
        
    -   使用arrayListOf创建一个list
        `val list_3 = arrayListOf(9, 3, 4)` 
        
-   可变集合类MutableList(Read&Write, Mutable), 与不可变的List相比，添加了add/addAll、remove/removeAll/removeAt、set、clear、retainAll等更新修改的操作

    > 创建可变List对象与创建不可比and额List类似，前面加上`mutable`
    
    -   使用mutableListOf创建可变的List
        `val list = mutableListOf(123, 23)`
        
    -   使用arrayListOf创建可变的List
        `val list_3 = arrayListOf(9, 3, 4)` 
        
#### 2、遍历

-   使用`Iterator`迭代器
    ```
    // 使用迭代器遍历
            val iterator = list.iterator()
            while (iterator.hasNext()) {
                println(iterator.next())
            }
    ```

-   使用`forEach`遍历
    ```
    list.forEach {
                println(it)
            }
    ```
    还可使用`list.forEach(::println)`
    
## 3、面向对象编程

### 1、类与构造器

> Kotlin中的类与Java中类似，使用`class`声明

-   构造函数

    > Kotlin中，一个类可以有一个主构造函数，同时也可拥有一个或多个次构造函数
    
    -   主构造函数
    
        > 主构造函数是类头的一部分，直接放在类名后面, 如下所示。如果主构造函数没有任何注解或者可见性修饰符，可以省略constructor关键字，如果构造函数有注解或可见性修饰符，constructor关键词则是必须的，并且这些修饰符在它前面。主构造函数中声明的属性可以是可变的或不可变的。主构造函数不能包含任何代码。初始化的代码可以放在以`init`关键字作为前缀的初始化块中，如下所示
        
        ```kotlin
        open class Student constructor(var name: String, var age: Int) {
        
            init {
                println("name is $name, and age is $age")
            }
        
        }
        ```
        
    -   次构造函数
    
        > 在类体中，可以声明前缀有`constructor`的次构造函数，次构造函数不能有声明val或var。如下所示
        
        ```
        class Teacher {
            
            constructor(name: String) {
                
            }
            
            constructor(name: String, age: Int) {
                
            }
            
        }
        ```
        
    > 如果一个非抽象类没有声明任何构造函数，他会有一个生成的不带参数的主构造函数。构造函数的可见性是public
    
    -   私有构造函数
    
        声明如下：
        
        ```kotlin
        class Test private constructor(){
        }
        ```
        
-   抽象类

    > 含有抽象函数的类（该类需用abstract修饰）,称为抽象类
    
    -   抽象函数
    
        -   抽象函数必须用abstract关键字修饰
        
        -   抽象函数不能手动添加open，默认为open修饰
        
        -   抽象函数没有具体的实现
        
        -   含有抽象函数的类成为抽象类，必须有abstract关键字修饰。抽象类可以由具体实现的函数，这样的函数默认是final，如果想要重写这个函数，给这个函数加上open关键字
        
    -   抽象属性
    
        -   抽象属性在抽象类中不能被初始化
        
        -   如果在子类中没有主构造器，要对抽象属性手动初始化。如果子类中有主构造器函数，抽象属性可以在主构造函数中声明
        
-   接口

    -   [定义接口](./src/main/kotlin/hht/dragon/java/interfaces/InterfaceDefinition.kt)：`interface InterfacesName`
    
    > Kotlin的接口可以包含抽象的方法及方法的实现
    
    -   [实现接口](./src/main/kotlin/hht/dragon/java/interfaces/InterfaceImpl.kt)
    
    > 使用冒号`:`来实现一个接口，如果有一个多个用逗号隔开
    
-   [继承](./src/main/kotlin/hht/dragon/java/extend/ExtendClass.kt)

    -   [`open`关键字](./src/main/kotlin/hht/dragon/java/extend/OpenClass.kt)
        
        > 当一个类使用open关键字修饰后，这样的类便可被继承。在Kotlin中若果方法需要被重写则应在方法上标注`open`关键字

> 在子类中同实现接口一样，使用冒号进行继承,  
> 如果父类有构造函数，那么必须在子类的主构造函数laingge中进行继承，没有的话则可以选择主构造函数后二级构造函数

```
class ExtendClass : OpenClass() {

    override fun save() {
        super.save()
    }
}

class ExtendClassTwo(name: String) : Base(name) {

}
```

-   [枚举](./src/main/kotlin/hht/dragon/java/enums/Color.kt)

-   [协程](./src/main/kotlin/hht/dragon/java/thread/Thread.kt)


## 4、[Kotlin与Java互操作](./src/test/kotlin/hht/dragon/java/withjava/UsingJava.kt)

-   [调用静态方法与反射](./src/main/kotlin/hht/dragon/java/withjava/WithJava.kt)