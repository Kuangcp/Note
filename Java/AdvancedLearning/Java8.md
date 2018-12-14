---
title: Java8
date: 2018-12-13 16:05:51
tags: 
    - Java8
    - 基础
categories: 
    - Java
---

**目录 start**
 
1. [Java8](#java8)
    1. [Funcational](#funcational)
    1. [Lambda](#lambda)
        1. [行为参数化](#行为参数化)
        1. [Lambda基础](#lambda基础)
        1. [原始类型特化](#原始类型特化)
        1. [类型检查、类型推断以及限制](#类型检查、类型推断以及限制)
            1. [类型检查](#类型检查)
            1. [同样的Lambda 不同的函数式接口](#同样的lambda-不同的函数式接口)
            1. [类型推断](#类型推断)
            1. [使用局部变量](#使用局部变量)
        1. [方法引用](#方法引用)
        1. [复合 Lambda 表达式](#复合-lambda-表达式)
            1. [比较器复合](#比较器复合)
            1. [谓词复合](#谓词复合)
            1. [函数复合](#函数复合)
        1. [利用Lambda开发DSL框架](#利用lambda开发dsl框架)
    1. [Stream](#stream)
        1. [Stream与集合](#stream与集合)
            1. [只能遍历一次](#只能遍历一次)
            1. [外部迭代和内部迭代](#外部迭代和内部迭代)
        1. [Stream操作](#stream操作)
            1. [中间操作](#中间操作)
            1. [终端操作](#终端操作)
        1. [使用Stream](#使用stream)
            1. [筛选](#筛选)
            1. [映射](#映射)
            1. [查找和匹配](#查找和匹配)
            1. [归约](#归约)
                1. [求和](#求和)
                1. [极值](#极值)
                1. [归约的优势与并行化](#归约的优势与并行化)
                1. [总结](#总结)
            1. [数值流](#数值流)
                1. [原始类型特化](#原始类型特化)
                1. [数值范围](#数值范围)
            1. [构建流](#构建流)
                1. [由值创建流](#由值创建流)
                1. [由数组创建流](#由数组创建流)
                1. [由文件生成流](#由文件生成流)
                1. [由函数生成流：创建无限流](#由函数生成流创建无限流)
        1. [使用流收集数据](#使用流收集数据)
            1. [预定义收集器](#预定义收集器)
                1. [汇总](#汇总)
                1. [规约](#规约)
                1. [分组](#分组)
                    1. [多级分组](#多级分组)
                    1. [按子组收集数据](#按子组收集数据)
                1. [分区](#分区)
    1. [Optional](#optional)
        1. [Optional类和Stream接口的相似之处](#optional类和stream接口的相似之处)
        1. [Tips](#tips)
        1. [实践:读取Properties某属性](#实践读取properties某属性)
    1. [集合](#集合)
    1. [时间处理](#时间处理)
        1. [Instant](#instant)
        1. [LocalDateTime](#localdatetime)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Java8
> [doc: Java8](https://docs.oracle.com/javase/8/) | [API](https://docs.oracle.com/javase/8/docs/api/)
> [Java8 JDK Readme](http://www.oracle.com/technetwork/java/javase/jdk-8-readme-2095712.html) | [Jre8 Readme](http://www.oracle.com/technetwork/java/javase/jre-8-readme-2095710.html)`有说明哪些是JRE运行不必要的文件`  

> [Java8 tools](https://docs.oracle.com/javase/8/docs/technotes/tools/)`介绍目录 bin/* 下的工具` | [jdk structure](https://docs.oracle.com/javase/8/docs/technotes/guides/desc_jdk_structure.html)  
- [Oracle:Java8故障排除指南](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/)

**`参考书籍`**
>1. Java8 in action 

*****************************

## Funcational
> [参考  Java8函数接口实现回调及Groovy闭包的代码示例](http://www.cnblogs.com/lovesqcc/p/6083759.html)
> [Function接口 – Java8中java.util.function包下的函数式接口](http://ifeve.com/jjava-util-function-java8/)

**`@FunctionalInterface`**
- An informative annotation type used to indicate that an interface type declaration is intended to be a functional interface as defined by the Java Language Specification.

- 这个标注用于表示该接口会设计成一个函数式接口。如果你用@FunctionalInterface定义了一个接口，而它却不是函数式接口的话，编译器将返回一个提示原因的错误。

- 如果使用此批注类型对类型进行批注，则编译器需要生成错误消息，除非：
    - 类型是接口类型，而不是注释类型，枚举或类。
    - 带注释的类型满足功能接口的要求。
- 但是，无论接口声明中是否存在功能接口注释，编译器都会将满足功能接口定义的任何接口视为 FunctionalInterface。

- 函数式接口很有用，抽象方法的签名可以描述Lambda表达式的签名。函数式接口的抽象方法的签名称为函数描述符。
- 常用函数接口: (详细可参考 java.util.function; 包下的类)
    1. **Consumer** (接收`单参数无返回值`的函数或lambda表达式)， 方法是 `void accept(T t);`
    1. **BiConsumer** (接收`双参数无返回值`的函数或 lambda表达式)，方法是 `void accept(T t, U u);`
    1. **Function** (接收`单参数有返回值`的函数或lambda表达式)， 方法是 `R apply(T t);`
    1. **BiFunction** (接收`双参数有返回值`的函数或lambda表达式)，方法是 `R apply(T t, U u);`
    1. **Predicate** （接收`单参数返回布尔值`的函数或lambda表达式），方法是 `boolean test(T t);`
    1. **BiPredicate** （接收`双参数返回布尔值`的函数或lambda表达式），方法是 `boolean test(T t, U u);`
    1. **Supplier** (无参数但具有返回值的函数或 lambda表达式)， 方法是 `T get();`

- 为什么要使用 Function 以及闭包呢？
    - 在语法上比定义回调接口、创建匿名类更加简洁；
    - 尝试使用新的语言特性，理解多样化的编程思想，提升编程表达能力。

*******************************

## Lambda

1. Lambda表达式可以理解为一种匿名函数：它没有名称，但有参数列表、函数主体、返回类型，可能还有一个可以抛出的异常的列表。
1. Lambda表达式让你可以简洁地传递代码。
1. 函数式接口就是仅仅声明了一个抽象方法的接口。
1. 只有在接受函数式接口的地方才可以使用Lambda表达式。
1. Lambda表达式允许你直接内联，为函数式接口的抽象方法提供实现，并且将整个表达式作为函数式接口的一个实例。
1. Java 8自带一些常用的函数式接口，放在java.util.function包里，包括`Predicate<T>、 Function<T,R>、 Supplier<T>、Consumer<T> 和BinaryOperator<T>`
1. 为了避免装箱操作，对`Predicate<T>`和`Function<T, R>`等通用函数式接口的原始类型特化： IntPredicate、 IntToLongFunction等。
1. 环绕执行模式（即在方法所必需的代码中间，你需要执行点儿什么操作，比如资源分配和清理）可以配合Lambda提高灵活性和可重用性。
1. Lambda表达式所需要代表的类型称为目标类型。
1. 方法引用让你重复使用现有的方法实现并直接传递它们。
1. Comparator、 Predicate和Function等函数式接口都有几个可以用来结合Lambda表达式的默认方法。

> [参考博客: 你真的了解lambda吗？一文让你明白lambda用法与源码分析 ](https://mp.weixin.qq.com/s?__biz=MzAxODcyNjEzNQ==&mid=2247485682&idx=1&sn=f3fb281b49a029b607f9377853a644bf&chksm=9bd0a56aaca72c7c8beebbea8f9471446cb444bd8e1e7d21016e906d1227e8f87770e2f8f31e&mpshare=1&scene=1&srcid=0810geQnLXB2oMjfoAOEJ39L#rd)
> [参考博客: 级联 lambda 表达式的函数重用与代码简短问题](http://www.techug.com/post/java-lambda.html)

- [ ] 学习常见排序 Comparator int float double time string...

> [参考博客: Java8：Lambda表达式增强版Comparator和排序](http://www.importnew.com/15259.html)

### 行为参数化
>1. 行为参数化，就是一个方法接受多个不同的行为作为参数，并在内部使用它们， 完成不同行为的能力。
>1. 行为参数化可让代码更好地适应不断变化的要求，减轻未来的工作量。
>1. 传递代码，就是将新行为作为参数传递给方法。但在Java 8之前这实现起来很啰嗦。为接
>1. 声明许多只用一次的实体类而造成的啰嗦代码，在Java 8之前可以用匿名类来减少。
>1. Java API包含很多可以用不同行为进行参数化的方法，包括排序、线程和GUI处理。

> 这种模式可以把一个行为（一段代码）封装起来，并通过传递和使用创建的行为, 将方法的行为参数化。前面提到过，这种做法类似于策略设计模式  
> Java API中的很多方法都可以用不同的行为来参数化。这些方法往往与匿名类一起使用

### Lambda基础
- 可以把Lambda表达式理解为简洁地表示可传递的匿名函数的一种方式：它没有名称，但它有参数列表、函数主体、返回类型，可能还有一个可以抛出的异常列表。
    - `匿名`  我们说匿名，是因为它不像普通的方法那样有一个明确的名称：写得少而想得多！
    - `函数`  我们说它是函数，是因为Lambda函数不像方法那样属于某个特定的类。但和方法签名的组成是一致的
    - `传递`  Lambda表达式可以作为参数传递给方法或存储在变量中。
    - `简洁`  无需像匿名类那样写很多模板代码。

- Lambda基础语法: `(parameters) -> expression` 或者 `(parameters) -> { statements; }`

例如 `() -> void` 是一个参数列表为空 返回值为void的函数, Runnable 的 run 方法
```java
    public Callable<String> fetch() {
        // 返回的方法的方法签名是 () -> String
        return () -> "Tricky example ;-)";
    }

    // 方法签名为 () -> void
    execute(() -> {});
    public void execute(Runnable r){
        r.run();
    }
```

**`实践`**
- 资源处理（例如处理文件或数据库）时一个常见的模式就是打开一个资源，做一些处理，然后关闭资源。这个设置和清理阶段总是很类似
    - 并且会围绕着执行处理的那些重要代码。这就是所谓的环绕执行（execute around） 模式
```java
    // 简单的从文件读取一行
    public static String processFile() throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
            return br.readLine();
        }
    }

    // 如果将行为参数化, 就能通用的完成需求
    @FunctionalInterface
    public interface BufferedReaderProcessor {
    String process(BufferedReader b) throws IOException;
    }
    public static String processFile(BufferedReaderProcessor p) throws IOException {}
    // 处理一行
    String twoLines =processFile((BufferedReader br) -> br.readLine());
    // 处理两行
    String result = processFile((BufferedReader br) -> br.readLine() + br.readLine());
```

### 原始类型特化 
> Primitive Specializations

> Java类型要么是引用类型（比如Byte、 Integer、 Object、 List） ，要么是原始类型（比如int、 double、 byte、 char）。
但是泛型（比如`Consumer<T>`中的T）只能绑定到引用类型。这是由泛型内部的实现方式造成的。
因此，在Java里有一个将原始类型转换为对应的引用类型的机制。这个机制叫作装箱（boxing） 。
相反的操作，也就是将引用类型转换为对应的原始类型，叫作拆箱（unboxing）。 Java还有一个自动装箱机制来帮助程序员执行这一任务：装箱和拆箱操作是自动完成的。但这在性能方面是要付出代价的。装箱后的值本质上就是把原始类型包裹起来，并保存在堆里。因此，装箱后的值需要更多的内存，
并需要额外的内存搜索来获取被包裹的原始值。Java 8为我们前面所说的函数式接口带来了一个专门的版本，以便在输入和输出都是原始类型时避免自动装箱的操作。
比如，在下面的代码中，使用IntPredicate就避免了对值1000进行装箱操作，但要是用Predicate<Integer>就会把参数1000装箱到一个Integer对象中 -- Java8 in action

一般来说，针对专门的输入参数类型的函数式接口的名称都要加上对应的原始类型前缀，比如DoublePredicate、 IntConsumer、 LongBinaryOperator、 IntFunction等。 
Function接口还有针对输出参数类型的变种： ToIntFunction<T>、 IntToDoubleFunction等。
请记得这只是一个起点。如果有需要，你可以自己设计一个。请记住， (T,U) -> R的表达方式展示了应当如何思考一个函数描述符。
表的左侧代表了参数类型。这里它代表一个函数，具有两个参数，分别为泛型T和U，返回类型为R。

| 函数式接口 | 函数描述符 | 原始类型特化 |
|:----|:----|:----|
| `Predicate<T>` | T->boolean | IntPredicate<br/>LongPredicate<br/> DoublePredicate|
| `Consumer<T>` | T->void | IntConsumer<br/>LongConsumer<br/> DoubleConsumer |
| Function<T,R> | T->R | `IntFunction<R>` <br/> IntToDoubleFunction <br/> IntToLongFunction <br/> `LongFunction<R>`<br/> LongToDoubleFunction <br/> LongToIntFunction <br/> `DoubleFunction<R>` <br/>`ToIntFunction<T>`<br/>`ToDoubleFunction<T>`<br/>`ToLongFunction<T>`|
| `Supplier<T>` | ()->T | BooleanSupplier<br/>IntSupplier<br/> LongSupplier<br/> DoubleSupplier|
| `UnaryOperator<T>` | T->T |IntUnaryOperator<br/>LongUnaryOperator<br/>DoubleUnaryOperator|
| `BinaryOperator<T>` | (T,T)-> T | IntBinaryOperator<br/>LongBinaryOperator<br/>DoubleBinaryOperator|
| BiPredicate<L,R> | (L,R)->boolean | |
| BiConsumer<T,U> | (T,U)->void | `ObjIntConsumer<T>`<br/>`ObjLongConsumer<T>`<br/>`ObjDoubleConsumer<T>`|
| BiFunction<T,U,R> | (T,U)->R | ToIntBiFunction<T,U><br/>ToLongBiFunction<T,U><br/>ToDoubleBiFunction<T,U>|

**`Lambdas及函数式接口的例子`**
| 使用案例 | Lambda例子 | 对应的函数式接口 |
|:----|:----|:----|
| 布尔表达式 | (List<String> list) -> list.isEmpty() | `Predicate<List<String>>`|
| 创建对象 |() -> new Apple(10) |`Supplier<Apple>`
| 消费一个对象 | (Apple a) ->System.out.println(a.getWeight())|`Consumer<Apple>`|
| 从一个对象中 选择/提取 | (String s) -> s.length() | Function<String, Integer> 或 `ToIntFunction<String>`
| 合并两个值 | (int a, int b) -> a * b |  IntBinaryOperator|
| 比较两个对象 | (Apple a1, Apple a2) -> a1.getWeight().compareTo(a2.getWeight()) | Comparator< Apple > 或 BiFunction<Apple, Apple, Integer> 或 ToIntBiFunction<Apple, Apple>

- 请注意，任何函数式接口都不允许抛出受检异常（checked exception）。如果你需要Lambda 表达式来抛出异常，有两种办法：
    - 定义一个自己的函数式接口，并声明受检异常，
    - 或者把Lambda 包在一个try/catch块中。
- 比如函数式接口BufferedReaderProcessor，它显式声明了一个IOException：
    ```java
        @FunctionalInterface
        public interface BufferedReaderProcessor {
            String process(BufferedReader b) throws IOException;
        }
        BufferedReaderProcessor p = (BufferedReader br) -> br.readLine();
    ```
- 但是你可能是在使用一个接受函数式接口的API，比如Function<T, R>，没有办法自己创建一个。这种情况下， 你可以显式捕捉受检异常：
    ```java
        Function<BufferedReader, String> f = (BufferedReader b) -> {
            try {
                return b.readLine();
            } catch(IOException e) {
                throw new RuntimeException(e);
            }
        };
    ```

### 类型检查、类型推断以及限制
当我们第一次提到Lambda表达式时，说它可以为函数式接口生成一个实例。然而， Lambda 表达式本身并不包含它在实现哪个函数式接口的信息。

#### 类型检查
> Lambda的类型是从使用Lambda的上下文推断出来的。上下文（比如，接受它传递的方法的参数，或接受它的值的局部变量）中Lambda表达式需要的类型称为目标类型。
> 请注意，如果Lambda表达式抛出一个异常，那么抽象方法所声明的throws语句也必须与之匹配。

#### 同样的Lambda 不同的函数式接口
> 有了目标类型的概念，同一个Lambda表达式就可以与不同的函数式接口联系起来，只要它们的抽象方法签名能够兼容。

比如，前面提到的Callable和PrivilegedAction，这两个接口 都代表着什么也不接受且返回一个泛型T的函数。 因此，下面两个赋值是有效的：
```java
    Callable<Integer> c = () -> 42;
    PrivilegedAction<Integer> p = () -> 42;
```

**`特殊的void兼容规则`**
如果一个Lambda的主体是一个语句表达式， 它就和一个返回void的函数描述符兼容（当然需要参数列表也兼容）。
例如，以下两行都是合法的，尽管List的add方法返回了一个 boolean，而不是Consumer上下文（T -> void） 所要求的void：
```java
    // Predicate返回了一个boolean
    Predicate<String> p = s -> list.add(s);
    // Consumer返回了一个void
    Consumer<String> b = s -> list.add(s);
```

1. `Object o = () -> {System.out.println("Tricky example"); };` 不能通过编译
    - Lambda表达式的上下文是Object（目标类型）。但Object不是一个函数式接口。
    - 为了解决这个问题，你可以把目标类型改成Runnable，它的函数描述符是() -> void

既可以利用目标类型来检查一个Lambda是否可以用于某个特定的上下文. 也可以用来做一些略有不同的事：推断Lambda参数的类型。

#### 类型推断
> 你还可以进一步简化你的代码。 Java编译器会从上下文（目标类型）推断出用什么函数式接口来配合Lambda表达式，
> 这意味着它也可以推断出适合Lambda的签名，因为函数描述符可以通过目标类型来得到。  
> 这样做的好处在于，编译器可以了解Lambda表达式的参数类型，这样就可以在Lambda语法中省去标注参数类型。

```java
    // 无类型推断
    Comparator<Apple> c = (Apple a1, Apple a2) -> a1.getWeight().compareTo(a2.getWeight());
    // 有类型推断
    Comparator<Apple> c = (a1, a2) -> a1.getWeight().compareTo(a2.getWeight());
```

#### 使用局部变量
我们迄今为止所介绍的所有Lambda表达式都只用到了其主体里面的参数。但Lambda表达式也允许使用自由变量（不是参数，而是在外层作用域中定义的变量），
就像匿名类一样。 它们被称作捕获Lambda。例如，下面的Lambda捕获了portNumber变量：
```java
    int portNumber = 1337;
    Runnable r = () -> System.out.println(portNumber);
```
尽管如此，还有一点点小麻烦：关于能对这些变量做什么有一些限制。 Lambda可以没有限制地捕获（也就是在其主体中引用）实例变量和静态变量。
但局部变量必须显式声明为final，或事实上是final。
换句话说， Lambda表达式只能捕获指派给它们的局部变量一次。（注：捕获实例变量可以被看作捕获最终局部变量this。）

例如，下面的代码无法编译，因为portNumber 变量被赋值两次：
```java
    int portNumber = 1337;
    Runnable r = () -> System.out.println(portNumber);
    portNumber = 31337;
```
**`对局部变量的限制`**
- 你可能会问自己，为什么局部变量有这些限制。
    1. 第一，实例变量和局部变量背后的实现有一个关键不同。实例变量都存储在堆中，而局部变量则保存在栈上。
        - 如果Lambda可以直接访问局部变量，而且Lambda是在一个线程中使用的，则使用Lambda的线程，可能会在分配该变量的线程将这个变量收回之后，去访问该变量。
        - 因此， Java在访问自由局部变量时，实际上是在访问它的副本，而不是访问原始变量。如果局部变量仅仅赋值一次那就没有什么区别了——因此就有了这个限制。
    1. 第二，这一限制不鼓励你使用改变外部变量的典型命令式编程模式（这种模式会阻碍很容易做到的并行处理）。

**`闭包`**

你可能已经听说过闭包（closure，不要和Clojure编程语言混淆）这个词，你可能会想Lambda是否满足闭包的定义。
用科学的说法来说，闭包就是一个函数的实例，且它可以无限制地访问那个函数的非本地变量。例如，闭包可以作为参数传递给另一个函数。
它也可以访问和修改其作用域之外的变量。现在， Java 8的Lambda和匿名类可以做类似于闭包的事情：
它们可以作为参数传递给方法，并且可以访问其作用域之外的变量。但有一个限制：它们不能修改定义Lambda的方法的局部变量的内容。
这些变量必须是隐式最终的。可以认为Lambda是对值封闭，而不是对变量封闭。如前所述，这种限制存在的原因在于局部变量保存在栈上，
并且隐式表示它们仅限于其所在线程。如果允许捕获可改变的局部变量，就会引发造成线程不安全的新的可能性，
而这是我们不想看到的（实例变量可以，因为它们保存在堆中，而堆是在线程之间共享的） 。

### 方法引用
> 通过 :: 操作符 简化代码

| Lambda | 方法引用 |
|:----|:----|
| (Apple a) -> a.getWeight() | Apple::getWeight
| () -> Thread.currentThread().dumpStack() | Thread.currentThread()::dumpStack
| (str, i) -> str.substring(i) | String::substring
| (String s) -> System.out.println(s) | System.out::println

- 构建方法引用
    1. 指向静态方法的方法引用（例如Integer的parseInt方法，写作Integer::parseInt）
    1. 指向任意类型实例方法的方法引用 （ 例 如 String 的 length 方 法 ， 写作String::length）。
    1. 指向现有对象的实例方法的方法引用
        - 假设你有一个局部变量expensiveTransaction 用于存放Transaction类型的对象，它支持实例方法getValue，
        - 那么你就可以写expensiveTransaction::getValue

**`构造函数的引用`**
1. 空构造函数 等价于 `() -> T` 
    - 例如 `Supplier<Apple> c1 = Apple::new;`
    - 之后 `Apple a1 = c1.get();` 调用接口的get方法实例化Apple对象

不将构造函数实例化却能够引用它，这个功能有一些有趣的应用。例如，你可以使用Map来将构造函数映射到字符串值。
你可以创建一个giveMeFruit方法，给它一个String和一个Integer，它就可以创建出不同重量的各种水果：
```java
    static Map<String, Function<Integer, Fruit>> map = new HashMap<>();
    static {
        map.put("apple", Apple::new);
        map.put("orange", Orange::new);
    // etc...
    }
    public static Fruit giveMeFruit(String fruit, Integer weight){
        return map.get(fruit.toLowerCase()).apply(weight);
    }
```

> 利用JDK提供的函数式接口 可以实现将一个,两个参数的构造函数转变为构造函数引用, 那么可以自定义实现三个参数的接口
```java
    public interface TriFunction<T, U, V, R>{
        R apply(T t, U u, V v);
    }
    TriFunction<Integer, Integer, Integer, Color> colorFactory = Color::new;
```

### 复合 Lambda 表达式
在实践中，这意味着你可以把多个简单的Lambda复合成复杂的表达式。比如，你可以让两个谓词之间做一个or操作，组合成一个更大的谓词。
而且，你还可以让一个函数的结果成为另一个函数的输入。
窍门在于，我们即将介绍的方法都是**默认方法**，也就是说它们不是抽象方法。

#### 比较器复合
1. 单一属性比较 `Comparator<Apple> c = Comparator.comparing(Apple::getWeight);` (实用的**Comparator.comparing**方法)
    - 顺序(小到大) 逆序则再调用下 reversed()
1. 按重量排序, 重量一致则再按国家排序 `inventory.sort(comparing(Apple::getWeight).thenComparing(Apple::getCountry));`

#### 谓词复合
> 谓词接口包括三个方法： negate、 and和or，让你可以重用已有的Predicate来创建更复杂的谓词。  
> 请注意， and和or方法是按照在表达式链中的位置，从左向右确定优先级的。因此， a.or(b).and(c)可以看作(a || b) && c。

1. 不红 `Predicate<Apple> notRedApple = redApple.negate();`
1. 红且重`Predicate<Apple> redAndHeavyApple = redApple.and(a -> a.getWeight() > 150);`
1. 红且重或者是绿的 `Predicate<Apple> redAndHeavyAppleOrGreen = redApple.and(a -> a.getWeight() > 150).or(a -> "green".equals(a.getColor()));`

#### 函数复合
可以把Function接口所代表的Lambda表达式复合起来。 Function接口为此配了andThen和compose两个默认方法，它们都会返回Function的一个实例。

```java
    Function<Integer, Integer> f = x -> x + 1;
    Function<Integer, Integer> g = x -> x * 2;
    Function<Integer, Integer> h = f.andThen(g); // g(f(x))
    int result = h.apply(1);

    Function<Integer, Integer> f = x -> x + 1;
    Function<Integer, Integer> g = x -> x * 2;
    Function<Integer, Integer> h = f.compose(g); // f(g(x))
    int result = h.apply(1);
```

> 使用场景 用String表示的一封信做文本转换：现在你可以通过复合这些工具方法来创建各种转型流水线了  
> 比如创建一个流水线：先加上抬头，然后进行拼写检查，最后加上一个落款，
```java
    Function<String, String> addHeader = Letter::addHeader;
    Function<String, String> transformationPipeline = addHeader
        .andThen(Letter::checkSpelling)
        .andThen(Letter::addFooter);
```

**`和数学对比`**
例如 根据给定的某个函数 以及上下限, 求积分: 定义函数 integrate `integrate(f, 3, 7)`

```java
    public double integrate(DoubleFunction<Double> f, double a, double b) {
        return (f.apply(a) + f.apply(b)) * (b-a) / 2.0;
    }
```
### 利用Lambda开发DSL框架
- [ ] 可以将mythpoi改造一下

**********************************

## Stream
> [参考博客: Java 8 中的 Streams API 详解](https://www.ibm.com/developerworks/cn/java/j-lo-java8streamapi/)

- Java 8中的Stream API可以让你写出这样的代码
    1. 声明性, 更简洁, 更易读
    1. 可复合, 更灵活
    1. 可并行, 性能更好

- Stream 简短的定义就是“从支持数据处理操作的源生成的元素序列”
    - **元素序列** 
        - 就像集合一样，流也提供了一个接口，可以访问特定元素类型的一组有序值。
        - 因为集合是数据结构，所以它的主要目的是以特定的时间/空间复杂度存储和素（如ArrayList与LinkedList）。
        - 但流的目的在于表达计算，比如你前面见到的filter、sorted 和map。集合讲的是数据，流讲的是计算。
    - **源** 
        - 流会使用一个提供数据的源，如集合、数组或输入/输出资源。请注意，从有序集合生成流时会保留原有的顺序。由列表生成的流，其元素顺序与列表一致。
    - **数据处理操作**
        -  流的数据处理功能支持类似于数据库的操作，以及函数式编程语言中的常用操作，如filter、map、reduce、find、match、sort等。流操作可以顺序执行，也可并行执行
    - **内部迭代**
        - 与使用迭代器显式迭代的集合不同，流的迭代操作是在背后进行的。

### Stream与集合

粗略地说，集合与流之间的差异就在于什么时候进行计算。集合是一个内存中的数据结构，它包含数据结构中目前所有的值——集合中的每个元素都得先算出来才能添加到集合中。  
（你可以往集合里加东西或者删东西，但是不管什么时候，集合中的每个元素都是放在内存里的，元素都得先算出来才能成为集合的一部分）  
相比之下，流则是在概念上固定的数据结构（你不能添加或删除元素），其元素则是按需计算的。

例如构建一个质数流, 对所有的质数处理, 如果使用集合就要把所有的质数构建出来, 然后做下一步操作, 但是流只会按需生成。这是一种生产者－消费者的关系. 从另一个角度来说，流就像是一个延迟创建的集合：只有在消费者要求的时候才会计算值

#### 只能遍历一次
> 和迭代器类似，流只能遍历一次, 遍历完之后，我们就说这个流已经被消费掉了  
> 从哲学的角度看, 集合是空间中分布的一组值, 而流是时间中分布的一组值

#### 外部迭代和内部迭代
- 使用Collection接口需要用户去做迭代（比如用for-each），这称为外部迭代。  
- 相反，Streams库使用内部迭代——它帮你把迭代做了，还把得到的流值存在了某个地方，你只要给出一个函数声明迭代中执行的操作即可。

- 外部迭代
    - 显式的迭代集合, 命令式的执行操作
- 内部迭代
    - 将迭代的细节隐藏起来, 方便优化

### Stream操作
因为filter、sorted、map 和collect 等操作是与具体线程模型无关的高层次构件, 所以它们的内部实现可以是单线程的，也可能透明地充分利用你的多核架构

#### 中间操作
诸如 filter 或 sorted  map flatMap limit distinct 等中间操作会返回另一个流。这让多个操作可以连接起来形成一个查询。 
重要的是，除非流水线上触发一个终端操作，否则中间操作不会执行任何处理因为中间操作一般都可以合并起来，在终端操作时一次性全部处理 (循环合并)

1. filter 满足该条件的元素保留下来
1. map 将一个流中的每个元素通过 一种映射 得到新的元素组成的流
1. flatMap 使用流时， flatMap方法接受一个函数作为参数，这个函数的返回值是另一个流。这个方法会应用到流中的每一个元素，最终形成一个新的流的流。

#### 终端操作
| 操作 | 目的 |
|:----|:----|
| forEach | 消费流中的每个元素并对其应用 Lambda。这一操作返回 void  |
| count | 返回流中元素的个数。这一操作返回 long |
| collect | 把流归约成一个集合，比如List、Map甚至是Integer |

### 使用Stream
- 流的使用一般包括三件事：
    - 一个数据源（如集合）来执行一个查询；
    - 一个中间操作链，形成一条流的流水线；
    - 一个终端操作，执行流水线，并能生成结果。
    > 流的流水线背后的理念类似于构建器模式 在构建器模式中有一个调用链用来设置一套配置（对流来说这就是一个中间操作链），接着是调用 build方法 （对流来说就是终端操作）

#### 筛选
1. 利用 filter 使用谓词 Predicate 筛选
1. 去重 distinct()
1. 截断 limit(n) 只能按流的长度单向截断
1. 跳过元素 skip(n)

#### 映射
- 流支持map方法，它会接受一个函数作为参数。这个函数会被应用到每个元素上，并将其映射成一个新的元素
    - （使用映射一词，是因为它和转换类似，但其中的细微差别在于它是“创建一个新版本”而不是去“修改”）

```java
List<Integer> dishNameLengths = menu.stream() 
        .map(Dish::getName) .map(String::length) .collect(toList()); 
```
**`flatMap`**
```java
List<String> uniqueCharacters = words.stream() 
        .map(w -> w.split(""))  // Stream<Arrays>
        .flatMap(Arrays::stream) // 扁平化流 (合并)
        .distinct() 
        .collect(Collectors.toList()); 
```

**使用流的方式嵌套迭代**
```java
// 给定两个数字列表，如何返回所有的数对呢？例如，给定列表[1, 2, 3]和列表[3, 4]，应该返回[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
List<Integer> numbers1 = Arrays.asList(1, 2, 3); 
List<Integer> numbers2 = Arrays.asList(3, 4); 
List<int[]> pairs = numbers1.stream() 
    .flatMap(i -> 
        numbers2.stream() .map(j -> new int[]{i, j})
    ).collect(toList()); 
```

#### 查找和匹配
> allMatch、anyMatch、noneMatch、findFirst findAny

- 都是接受一个 谓词 函数, 都用到了我们所谓的短路,不需要处理所有的流，这就是大家熟悉的Java中&&和||运算符短路在流中的版本
    - allMatch、anyMatch、noneMatch 是 匹配 返回值是boolean
    - findFirst findAny 是查找 返回 ``Optional<T>`` findFirst 针对有序的流
        - 如果你不关心返回的元素是哪个，请使用 findAny ，因为它在使用并行流时限制较少。

#### 归约
- 如何把一个流中的元素组合起来，使用 reduce 操作来表达更复杂的查询 此类查询需要将流中所有元素反复结合起来，得到一个值
- 这样的查询可以被归类为归约操作（将流归约成一个值）。用函数式编程语言的术语来说，这称为折叠（fold）

> map 和 reduce 的连接通常称为 map-reduce 模式，因 Google 用它来进行网络搜索而出名，因为它很容易并行化。

##### 求和

```java
    int sum = 0; 
    for (int x : numbers){
        sum += x;
    }

    // reduce 参数: 初始值 函数
    int sum = numbers.stream().reduce(0, (a, b) -> a + b);

    int sum = numbers.stream().reduce(0, Integer::sum);

    // 无初始值 返回 Optional 对象
    Optional<Integer> sum = numbers.stream().reduce((a, b) -> (a + b));
```

##### 极值

```java
    // 最大值
    Optional<Integer> max = numbers.stream().reduce(Integer::max);

    // 最小值
    Optional<Integer> min = numbers.stream().reduce(Integer::min);
    Optional<Integer> min = numbers.stream().reduce((x, y) -> x < y ? x : y);
```

##### 归约的优势与并行化
相比于前面写的逐步迭代求和，使用 reduce 的好处在于，这里的迭代被内部迭代抽象掉了，这让内部实现得以选择并行执行reduce 操作。  
而迭代式求和例子要更新共享变量 sum ，这不是那么容易并行化的。如果你加入了同步，很可能会发现线程竞争抵消了并行本应带来的性能提升！  
这种计算的并行化需要另一种办法：将输入分块，分块求和，最后再合并起来。

`int sum = numbers.parallelStream().reduce(0, Integer::sum); `

但要并行执行这段代码也要付一定代价，传递给 reduce 的Lambda不能更改状态（如实例变量），而且操作必须满足结合律才可以按任意顺序执行。

##### 总结
| 操作 | 类型 | 返回类型 | 参数 | 函数描述符 |
|:----|:----|:----|:----|:----|
| filter  | 中间 | `Stream<T>` | ``Predicate<T>`` | T -> boolean |
|distinct|中间 有状态 无界|`Stream<T>`|||
|skip|中间 有状态 有界|`Stream<T>`|long||
|limit|中间 有状态 有界|`Stream<T>`|long||
|map|中间|`Stream<R>`|`Function<T, R>`| T -> R|
|flatMap|中间|`Stream<R>`|`Function<T, Stream<R>>`| T -> `Stream<R>`|
|sorted|中间 有状态 无界|`Stream<T>`|`Comparator<T>`|(T,T) -> int|
|anyMatch|终端|boolean|``Predicate<T>``| T -> boolean |
|noneMatch|终端|boolean|``Predicate<T>``|T -> boolean|
|allMatch|终端|boolean|``Predicate<T>``|T->boolean|
|findAny|终端|`Optional<T>`|||
|findFirst|终端|`Optional<T>`|||
|forEach|终端|void|``Consumer<T>``| T -> void|
|collect|终端|R|`Collector<T, A, R>`||
|reduce|终端 有状态 有界|`Optional<T>`|`BinaryOprator<T>`|(T, T) -> T|
|count|终端|long|||

> joining 替换 字符串直接拼接

```java
    // 该方案 效率不高, 所有字符串被反复连接, 每次迭代都需创建新String对象
    strings.stream().sorted().reduce("", (a,b) -> a+b);
    // joining 内部会使用 StringBuilder
    strings.stream().sorted().collect(Collectors.joining());
```

#### 数值流

##### 原始类型特化
Java8 引入了三个原始类型特化流接口来解决这个问题： `IntStream、DoubleStream 和 LongStream`，分别将流中的元素特化为int、long和double，从而避免了暗含的装箱成本。

**映射到数值流**
```java
    // 例如求和, 里面有一个隐含的拆箱操作 再求和
    numbers.parallelStream().reduce(0, Integer::sum);

    // 请注意，如果流是空的，sum默认返回 0
    numbers.parallelStream().mapToInt(Integer::intValue).sum() 
```

**映射到对象流**
使用 boxed() 方法即可

**默认值OptionalInt**
```java
    OptionalInt maxCalories = menu.stream().mapToInt(Dish::getCalories).max(); 
```
##### 数值范围
IntStream和LongStream 的 range() 或者 rangeClose() 方法能产生一个数值流
> 例如 IntStream.rangeClose(1,100).filter(num->num%2==0).count() 统计100以内的偶数

> **获取勾股数流**
```java
    Stream<int[]> pythagoreanTriples = IntStream.rangeClosed(1, 100).boxed() .flatMap(a -> 
        IntStream.rangeClosed(a, 100) 
                .filter(b -> Math.sqrt(a*a + b*b) % 1 == 0) 
                .mapToObj(b -> new int[]{a, b, (int)Math.sqrt(a * a + b * b)}) 
            ); 
    
    pythagoreanTriples.limit(5) .forEach(t -> System.out.println(t[0] + ", " + t[1] + ", " + t[2])); 
```
#### 构建流
> 从值序列、数组、文件来创建流，甚至由函数创建无限流

##### 由值创建流
`Stream<String> stream = Stream.of("Java 8 ", "Lambdas ", "In ", "Action"); `

##### 由数组创建流
```java
    int[] numbers = {2, 3, 5, 7, 11, 13}; 
    int sum = Arrays.stream(numbers).sum(); 
```

##### 由文件生成流
Java中用于处理文件等I/O操作的NIO  API（非阻塞I/O）已更新，以便利用Stream  API。java.nio.file.Files中的很多静态方法都会返回一个流。

```java
    long uniqueWords = 0; 
    try(Stream<String> lines = Files.lines(Paths.get("data.txt"), Charset.defaultCharset())){ 
        uniqueWords = lines.flatMap(line -> Arrays.stream(line.split(" "))).distinct() .count(); 
    }catch(IOException e){} 
```

##### 由函数生成流：创建无限流
> Stream API提供了两个静态方法来从函数生成流：Stream.iterate和Stream.generate。这两个操作可以创建所谓的 无限流  
> 同样，你不能对无限流做排序或归约，因为所有元素都需要处理，而这永远也完不成！

**`迭代`**
```java
    Stream.iterate(0, n -> n + 2).limit(10).forEach(System.out::println); 

    // 获取斐波那契序列 元组
    Stream.iterate(new int[]{0, 1}, t -> new int[]{t[1], t[0]+t[1]}) 
      .limit(20) 
      .forEach(t -> System.out.println("(" + t[0] + "," + t[1] +")")); 
```

**`生成`**
```java
    Stream.generate(Math::random).limit(5).forEach(System.out::println); 
    // 很重要的一点是，在并行代码中使用有状态的供应源是不安全的。因此下面的代码仅仅是为了内容完整，应尽量避免使用！
    IntSupplier fib = new IntSupplier(){ 
        private int previous = 0; 
        private int current = 1; 
        public int getAsInt(){ 
            int oldPrevious = this.previous; 
            int nextValue = this.previous + this.current; 
            this.previous = this.current; 
            this.current = nextValue; 
            return oldPrevious; 
        } 
    }; 
    IntStream.generate(fib).limit(10).forEach(System.out::println); 
```

### 使用流收集数据
> 函数式编程相对于指令式编程的一个主要优势：你只需指出希望的结果——“做什么”，而不用操心执行的步骤——“如何做”


#### 预定义收集器
Collectors所提供的工厂方法 它们主要提供了三大功能：将流元素归约和汇总为一个值 元素分组 元素分区

- toList toMap toSet 等方法

##### 汇总
> Collectors类专门为汇总提供了一个工厂方法：Collectors.summingInt 它可接受一个把对象映射为求和所需int的函数，并返回一个收集器；该收集器在传递给普通的collect方法后即执行我们需要的汇总操作  
> 求平均数 Collectors.averagingInt
> summarizing操作你可以得出元素的个数，并得到总和、平均值、最大值和最小值

```java
IntSummaryStatistics menuStatistics = menu.stream().collect(summarizingInt(Dish::getCalories)); 
// toString(): IntSummaryStatistics{count=9, sum=4300, min=120, average=477.777778, max=800} 
```
**`连接字符串`**
joining工厂方法返回的收集器会把对流中每一个对象应用toString方法得到的所有字符串连接成一个字符串。
`String shortMenu = menu.stream().collect(joining()); `

##### 规约
事实上，我们已经讨论的所有收集器，都是一个可以用reducing工厂方法定义的归约过程的特殊情况而已。Collectors.reducing工厂方法是所有这些特殊情况的一般化。

- 例如 计算总热量 `int totalCalories = menu.stream().collect(reducing(0, Dish::getCalories, (i, j) -> i + j));`
    - 第一个参数: 规约操作的起始值 也是当流为空时的返回值
    - 第二个参数: 转换函数
    - 第三个参数: BinaryOperator  将两个项目累积成一个同类型的值

你可以把单参数reducing工厂方法创建的收集器看作三参数方法的特殊情况，它把流中的第一个项目作为起点，把恒等函数（即一个函数仅仅是返回其输入参数）作为一个转换函数。
这也意味着，要是把单参数reducing收集器传递给空流的collect方法，收集器就没有起点;它将因此而返回一个Optional<Dish>对象。

> 1. 收集框架的灵活性：以不同的方法执行同样的操作

1. 使用Integer的sum方法简化以上的求和 `int totalCalories = menu.stream().collect(reducing(0, Dish::getCalories,Integer::sum));`
1. 将对象映射为 int 然后规约求和 `int totalCalories = menu.stream().map(Dish::getCalories).reduce(Integer::sum).get(); `
1. 或者转为 IntStream `int totalCalories = menu.stream().mapToInt(Dish::getCalories).sum(); `

> 2. 根据情况选择最佳解决方案  

函数式编程（特别是Java 8的Collections框架中加入的基于函数式风格原理设计的新API）通常提供了多种方法来执行同一个操作。
这个例子还说明，收集器在某种程度上比Stream接口上直接提供的方法用起来更复杂，但好处在于它们能提供更高水平的抽象和概括，也更容易重用和自定义。

##### 分组
一个常见的数据库操作是根据一个或多个属性对集合中的项目进行分组。

- 使用 groupingBy `Map<Dish.Type, List<Dish>> dishesByType = menu.stream().collect(groupingBy(Dish::getType));`
    - groupingBy 方法的入参为一个 Function 一般称为分类函数

```java
    // 实现复杂的分类函数
    public enum CaloricLevel { DIET, NORMAL, FAT } 
    Map<CaloricLevel, List<Dish>> dishesByCaloricLevel = menu.stream().collect( 
            groupingBy(dish -> { 
                if (dish.getCalories() <= 400){
                    return CaloricLevel.DIET; 
                } 
                else if (dish.getCalories() <= 700){ 
                    return CaloricLevel.NORMAL; 
                }else{
                    return CaloricLevel.FAT; 
                }
            })); 
```

###### 多级分组
> 要实现多级分组，我们可以使用一个由双参数版本的 Collectors.groupingBy 工厂方法创建的收集器，它除了普通的分类函数之外，还可以接受collector类型的第二个参数。

```java
    Map<Dish.Type, Map<CaloricLevel, List<Dish>>> dishesByTypeCaloricLevel = 
    menu.stream().collect( 
        groupingBy(Dish::getType,  
            groupingBy(dish -> {  
                if (dish.getCalories() <= 400){
                    return CaloricLevel.DIET; 
                }else if (dish.getCalories() <= 700) {
                    return CaloricLevel.NORMAL;
                }else{ 
                    return CaloricLevel.FAT; 
                }
            } ) 
        ) 
    ); 
```

###### 按子组收集数据
> 可以把第二个groupingBy收集器传递给外层收集器来实现多级分组。但进一步说，传递给第一个groupingBy的第二个收集器可以是任何类型 
>> 例如: `Map<Dish.Type, Long> typesCount = menu.stream().collect(groupingBy(Dish::getType, counting())); `

```java
    Map<Dish.Type, Optional<Dish>> mostCaloricByType = menu.stream()
            .collect(groupingBy(
                Dish::getType,
                maxBy(
                    comparingInt(Dish::getCalories)
                )
            )); 
```
- 这个分组的结果显然是一个map，以Dish的类型作为键，以包装了该类型中热量最高的Dish的Optional<Dish>作为值
    - 但是这里的 Optional 存在的意义不大, 因为先有的类型 进行分组, 才会进行 maxBy 所以值是一定存在的

> 1. 把收集器的结果转换为另一种类型

因为前述例子中的Optional存在意义不是很大, 所以 把收集器返回的结果转换为另一种类型，你可以使用Collectors.collectingAndThen工厂方法返回的收集器

```java
    Map<Dish.Type, Dish> mostCaloricByType = menu.stream()
                .collect(groupingBy(
                    Dish::getType,
                    collectingAndThen(
                        maxBy(comparingInt(Dish::getCalories)),
                        Optional::get)
                    ));  
```
- 这个工厂方法接受两个参数——要转换的收集器以及转换函数，并返回另一个收集器。
- 这个收集器相当于旧收集器的一个包装，collect操作的最后一步就是将返回值用转换函数做一个映射。
- 在这里，被包起来的收集器就是用maxBy建立的那个，而转换函数Optional::get则把返回的Optional中的值提取出来。
- 前面已经说过，这个操作放在这里是安全的，因为reducing收集器永远都不会返回Optional.empty()。

> 2. 与 groupingBy 联合使用的其他收集器的例子

一般来说，通过groupingBy工厂方法的第二个参数传递的收集器将会对分到同一组中的所有流元素执行进一步归约操作。
```java
    // 对每一组Dish求和
    Map<Dish.Type, Integer> totalCaloriesByType = menu.stream().collect(groupingBy(Dish::getType, 
                summingInt(Dish::getCalories))); 
```
然而常常和groupingBy联合使用的另一个收集器是mapping方法生成的。这个方法接受两个参数：一个函数对流中的元素做变换，另一个则将变换的结果对象收集起来。
其目的是在累加之前对每个输入元素应用一个映射函数，这样就可以让接受特定类型元素的收集器适应不同类型的对象。我们来看一个使用这个收集器的实际例子。
比方说你想要知道，对于每种类型的Dish，菜单中都有哪些CaloricLevel。我们可以把groupingBy和mapping收集器结合起来，如下所示：
```java
    Map<Dish.Type, Set<CaloricLevel>> caloricLevelsByType = menu.stream().collect( 
        groupingBy(Dish::getType, mapping(dish -> {
            if (dish.getCalories() <= 400) return CaloricLevel.DIET; 
            else if (dish.getCalories() <= 700) return CaloricLevel.NORMAL; 
            else return CaloricLevel.FAT; 
        }, toSet()))); 
```
这里，就像我们前面见到过的，传递给映射方法的转换函数将Dish映射成了它的CaloricLevel：生成的CaloricLevel流传递给一个toSet收集器，它和toList类似，
不过是把流中的元素累积到一个Set而不是List中，以便仅保留各不相同的值。如先前的示例所示，这个映射收集器将会收集分组函数生成的各个子流中的元素
```java
    // 可以给它传递一个构造函数引用来要求 HashSet
    Map<Dish.Type, Set<CaloricLevel>> caloricLevelsByType = menu.stream().collect( 
        groupingBy(Dish::getType, mapping(dish -> { 
            if (dish.getCalories() <= 400) return CaloricLevel.DIET; 
            else if (dish.getCalories() <= 700) return CaloricLevel.NORMAL; 
            else return CaloricLevel.FAT; 
        },toCollection(HashSet::new) ))); 
```

##### 分区

****************************************

## Optional
>1. null引用在历史上被引入到程序设计语言中，目的是为了表示变量值的缺失。
>1. Java 8中引入了一个新的类java.util.Optional<T>，对存在或缺失的变量值进行建模。
>1. 你可以使用静态工厂方法Optional.empty、 Optional.of以及Optional.ofNullable创建Optional对象。
>1. Optional类支持多种方法，比如map、 flatMap、 filter，它们在概念上与Stream类中对应的方法十分相似。
>1. 使用Optional会迫使你更积极地解引用Optional对象，以应对变量值缺失的问题，最终，你能更有效地防止代码中出现不期而至的空指针异常。
>1. 使用Optional能帮助你设计更好的API，用户只需要阅读方法签名，就能了解该方法是否接受一个Optional类型的值。

1. 能够显式的在方法签名上就表明返回值可能为 "空" (下文中的空都指 Optional.empty())
    - 增强了建模的表达能力 域模型中使用Optional，将允许缺失或者暂无定义的变量值用特殊的形式标记出来
    - 约束调用方需判断才能使用, 但是这个并不是万能的, 例如集合类型的返回的时候, 就不用 Optional 包住 显得繁琐, 直接返回 new 空集合即可
1. 如果Optional约束了返回值, 就在语义上表明该方法的返回值可能为空, 如果这个方法是初始化方法等具有特殊含义的方法, 不能返回空, 那就不能使用Optional
    - 这样虽然代码安全了, 但是将该方法的语义混淆了.所以 不仅不能用 Optional, 还需在方法中加上 断言 以尽早暴露该方法的异常
    - 虽然该方法在设计上是不能返回空, 但是还是有可能返回空, 为了健壮性, 还是需要调用方做非空检查

- 常用方法
    - `of(T value)` 封装对象到Optional内部, 若对象为null会立即抛出 NPE
    - `ofNullable(T value)` 同上但是允许放入null
    - `get()` 获取封装内的对象值, 但是若Optional为空 抛出 NoSuchElementException 异常
    - `orElse(T other)` 当Optional为空时提供默认值
    - `orElseGet(Supplier<? extends T> other)` 延迟提供默认值, 当为空执行传入的函数得到默认值
    - `orElseThrow(Supplier<? extends X> exceptionSupplier)` 与 get() 一致,但是可以自定义异常
    - `ifPresent(Consumer<? super T>)` 当不为空执行传入的函数

### Optional类和Stream接口的相似之处
1. map
    1. 使用 map 从 Optional 对象中提取和转换值: 可以将 Optional 看成只有一个元素的集合, 像Stream一样的使用 map
    1. 处理两个Optional对象: `person.flatMap(p -> car.map(c -> findCheapestInsurance(p, c)));` 原始的写法就是要判断两个对象同时存在(person 和 car )才调用find...方法
1. flatMap
    1. 流式获取 Optional 约束的属性 `Optional<String> name = a.flatMap(A::getB).flatMap(B::getC).map(C::getName)`
    - 其中 C是B的成员属性, B是A的成员属性, 且都是 Optional 的, 如果直接使用 map 就会发生 Optional 嵌套, 所以需要 flatMap 
1. filter 
    1. persion 存在且满足条件就返回自身否则返回空 `person.filter(o -> "name".equals(o.getName()))`

### Tips
1. **注意**: Optional 无法序列化, 也就是说不能作为 PO 的字段, 但是可以在get上下功夫: `public Optional<String> getName(){return this.name}`

1. 异常与Optional的对比
    - 当一个方法由于某些原因无法返回期望值, 常见的做法是抛出异常, 或者返回null(不建议). 但是这时候多了一个选择, 返回Optional
    - 例如 Integer.parseInt() 方法 若参数字符串不合法就会抛出异常, 这时候就可以自己定义一个工具方法, catch住异常 返回 空 (如下 stringToInt 方法)

1. 应该避免使用使用基础类型的 Optional 对象
    - OptionalInt OptionalLong OptionalDouble, 因为他们不支持 Stream 操作
    - 即使 OptionalInt 能简化 Optional<Integer>

### 实践:读取Properties某属性
> 从properties文件中读取某个属性, 正整数就返回该值, 否则返回0  

```java
// 原始写法
public int readDuration(Properties props, String name) {
    String value = props.getProperty(name);
    if (value != null) {
        try {
            int i = Integer.parseInt(value);
            if (i > 0) {
                return i;
            }
        } catch (NumberFormatException nfe) { }
    }
    return 0;
}
// 改进
public static Optional<Integer> stringToInt(String s) {
    try {
        return Optional.of(Integer.parseInt(s));
    } catch (NumberFormatException e) {
        return Optional.empty();
    }
}

public int readDuration(Properties props, String name) {
    return Optional.ofNullable(props.getProperty(name))
        .flatMap(OptionalUtility::stringToInt)
        .filter(i -> i > 0)
        .orElse(0);
}
```
***********************************
## 集合

_集合的Lambda迭代方式_
- [参考博客: List、Map的循环迭代](http://blog.csdn.net/xf_87/article/details/53931207)

对集合中的对象进行求和
*******************************
## 时间处理

### Instant 
- [ ] 暂时没有学会怎么用上

### LocalDateTime
> 方便的新时间处理类, 用于替代Date

```java
    // LocalDateTime 获取毫秒以及秒  也可以手动指定中国的时区 ZoneOffset.of("+8")
    ZonedDateTime zonedDateTime = datetime.atZone(ZoneOffset.systemDefault());
    Instant instant = zonedDateTime.toInstant();
    long seconds = instant.getEpochSecond(); 
    long millis = instant.toEpochMilli();
    Date date = Date.from(instant);
```
