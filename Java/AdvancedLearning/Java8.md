`目录 start`
 
1. [Java8](#java8)
    1. [Funcational](#funcational)
    1. [Lambda](#lambda)
        1. [行为参数化](#行为参数化)
        1. [Lambda基础](#lambda基础)
        1. [利用Lambda开发DSL框架](#利用lambda开发dsl框架)
    1. [Stream](#stream)
    1. [Optional](#optional)
    1. [集合](#集合)
    1. [时间处理](#时间处理)
        1. [Instant](#instant)
        1. [LocalDateTime](#localdatetime)

`目录 end` |_2018-11-18_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Java8
> [doc: Java8](https://docs.oracle.com/javase/8/) | [API](https://docs.oracle.com/javase/8/docs/api/)
> [Java8 JDK Readme](http://www.oracle.com/technetwork/java/javase/jdk-8-readme-2095712.html) | [Jre8 Readme](http://www.oracle.com/technetwork/java/javase/jre-8-readme-2095710.html)`有说明哪些是JRE运行不必要的文件`  

> [Java8 tools](https://docs.oracle.com/javase/8/docs/technotes/tools/)`介绍目录 bin/* 下的工具`
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
    1. **Supplier** (无参数返回值的函数或 lambda)， 方法是 `T get();`

- 为什么要使用 Function 以及闭包呢？
    - 在语法上比定义回调接口、创建匿名类更加简洁；
    - 尝试使用新的语言特性，理解多样化的编程思想，提升编程表达能力。

*******************************

## Lambda

> [参考博客: 你真的了解lambda吗？一文让你明白lambda用法与源码分析 ](https://mp.weixin.qq.com/s?__biz=MzAxODcyNjEzNQ==&mid=2247485682&idx=1&sn=f3fb281b49a029b607f9377853a644bf&chksm=9bd0a56aaca72c7c8beebbea8f9471446cb444bd8e1e7d21016e906d1227e8f87770e2f8f31e&mpshare=1&scene=1&srcid=0810geQnLXB2oMjfoAOEJ39L#rd)
> [参考博客: 级联 lambda 表达式的函数重用与代码简短问题](http://www.techug.com/post/java-lambda.html)

- [ ] 排序 Comparator 
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
但是泛型（比如Consumer<T>中的T）只能绑定到引用类型。这是由泛型内部的实现方式造成的。
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
| Predicate< T > | T->boolean | IntPredicate<br/>LongPredicate<br/> DoublePredicate|
| Consumer< T > | T->void | IntConsumer<br/>LongConsumer<br/> DoubleConsumer |
| Function<T,R> | T->R | IntFunction< R > <br/> IntToDoubleFunction <br/> IntToLongFunction <br/> LongFunction< R > <br/> LongToDoubleFunction <br/> LongToIntFunction <br/> DoubleFunction< R > <br/>ToIntFunction< T ><br/>ToDoubleFunction< T ><br/>ToLongFunction< T >|
| Supplier< T > | ()->T | BooleanSupplier<br/>IntSupplier<br/> LongSupplier<br/> DoubleSupplier|
| UnaryOperator< T > | T->T |IntUnaryOperator<br/>LongUnaryOperator<br/>DoubleUnaryOperator|
| BinaryOperator< T > | (T,T)-> T | IntBinaryOperator<br/>LongBinaryOperator<br/>DoubleBinaryOperator|
| BiPredicate<L,R> | (L,R)->boolean | |
| BiConsumer<T,U> | (T,U)->void | ObjIntConsumer< T ><br/>ObjLongConsumer< T ><br/>ObjDoubleConsumer< T >|
| BiFunction<T,U,R> | (T,U)->R | ToIntBiFunction<T,U><br/>ToLongBiFunction<T,U><br/>ToDoubleBiFunction<T,U>|

**`Lambdas及函数式接口的例子`**
| 使用案例 | Lambda例子 | 对应的函数式接口 |
|:----|:----|:----|
| 布尔表达式 | (List<String> list) -> list.isEmpty() | Predicate<List< String >>|
| 创建对象 |() -> new Apple(10) |Supplier< Apple >
| 消费一个对象 | (Apple a) ->System.out.println(a.getWeight())|Consumer< Apple >|
| 从一个对象中 选择/提取 | (String s) -> s.length() | Function<String, Integer> 或 ToIntFunction< String >
| 合并两个值 | (int a, int b) -> a * b |  IntBinaryOperator|
| 比较两个对象 | (Apple a1, Apple a2) -> a1.getWeight().compareTo(a2.getWeight()) | Comparator< Apple > 或 BiFunction<Apple, Apple, Integer> 或 ToIntBiFunction<Apple, Apple>

- 请注意，任何函数式接口都不允许抛出受检异常（checked exception）。如果你需要Lambda 表达式来抛出异常，有两种办法：
    - 定义一个自己的函数式接口，并声明受检异常，
    - 或者把Lambda 包在一个try/catch块中。
- 比如，在3.3节我们介绍了一个新的函数式接口BufferedReaderProcessor，它显式声明了一个IOException：
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

- 比如，前面提到的Callable和PrivilegedAction，这两个接口 都代表着什么也不接受且返回一个泛型T的函数。 因此，下面两个赋值是有效的：
    ```java
        Callable<Integer> c = () -> 42;
        PrivilegedAction<Integer> p = () -> 42;
    ```

### 利用Lambda开发DSL框架
- [ ] 可以将mythpoi改造一下

**********************************

## Stream
> [参考博客: Java 8 中的 Streams API 详解](https://www.ibm.com/developerworks/cn/java/j-lo-java8streamapi/)

1. filter 满足该条件的元素保留下来
1. map 将一个流中的每个元素通过 一种映射 得到新的元素组成的流
1. collect 将流收集起来
1. forEach 遍历流
1. flatMap 使用流时， flatMap方法接受一个函数作为参数，这个函数的返回值是另一个流。这个方法会应用到流中的每一个元素，最终形成一个新的流的流。

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


**`Optional类和Stream接口的相似之处`**
1. map
    1. 使用 map 从 Optional 对象中提取和转换值: 可以将 Optional 看成只有一个元素的集合, 像Stream一样的使用 map
    1. 处理两个Optional对象: `person.flatMap(p -> car.map(c -> findCheapestInsurance(p, c)));` 原始的写法就是要判断两个对象同时存在(person 和 car )才调用find...方法
1. flatMap
    1. 流式获取 Optional 约束的属性 `Optional<String> name = a.flatMap(A::getB).flatMap(B::getC).map(C::getName)`
    - 其中 C是B的成员属性, B是A的成员属性, 且都是 Optional 的, 如果直接使用 map 就会发生 Optional 嵌套, 所以需要 flatMap 
1. filter 
    1. persion 存在且满足条件就返回自身否则返回空 `person.filter(o -> "name".equals(o.getName()))`

**`Tips`**
1. 注意: Optional 无法序列化, 也就是说不能作为 PO 的字段, 但是可以在get上下功夫, 手动声明 Optional 式的方法

1. 异常与Optional的对比
    - 当一个方法由于某些原因无法返回期望值, 常见的做法是抛出异常, 或者返回null(不建议). 但是这时候多了一个选择, 返回Optional
    - 例如 Integer.parseInt() 方法 若参数字符串不合法就会抛出异常, 这时候就可以自己定义一个工具方法, catch住异常 返回 空 (如下 stringToInt 方法)

1. 应该避免使用使用基础类型的 Optional 对象
    - OptionalInt OptionalLong OptionalDouble, 因为他们不支持 Stream 操作
    - 即使 OptionalInt 能简化 Optional<Integer>

**`演练`**
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