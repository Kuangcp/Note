`目录 start`
 
1. [Java8](#java8)
    1. [Funcational](#funcational)
    1. [Lambda](#lambda)
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

- 常用函数接口主要有:
    1. Consumer (接收单参数无返回值的函数或lambda表达式)， 方法是 void accept(T t);
    1. BiConsumer (接收双参数无返回值的函数或 lambda表达式)，方法是 void accept(T t, U u) ;
    1. Function (接收单参数有返回值的函数或lambda表达式)， 方法是 R apply(T t);
    1. BiFunction (接收双参数有返回值的函数或lambda表达式)，方法是 R apply(T t, U u);
    1. Predicate （接收单参数返回布尔值的函数或lambda表达式），方法是 boolean test(T t);
    1. Supplier (无参数返回值的函数或 lambda)， 方法是 T get();

> 接受原子类型参数的函数接口，这里不一一列举了。可参考 java8 package java.util.function;

- 为什么要使用 Function 以及闭包呢？
    - 在语法上比定义回调接口、创建匿名类更加简洁；
    - 尝试使用新的语言特性，理解多样化的编程思想，提升编程表达能力。

*******************************

## Lambda
> [参考博客: 你真的了解lambda吗？一文让你明白lambda用法与源码分析 ](https://mp.weixin.qq.com/s?__biz=MzAxODcyNjEzNQ==&mid=2247485682&idx=1&sn=f3fb281b49a029b607f9377853a644bf&chksm=9bd0a56aaca72c7c8beebbea8f9471446cb444bd8e1e7d21016e906d1227e8f87770e2f8f31e&mpshare=1&scene=1&srcid=0810geQnLXB2oMjfoAOEJ39L#rd)
> [参考博客: 级联 lambda 表达式的函数重用与代码简短问题](http://www.techug.com/post/java-lambda.html)

- [ ] 排序 Comparator 
> [参考博客: Java8：Lambda表达式增强版Comparator和排序](http://www.importnew.com/15259.html)




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