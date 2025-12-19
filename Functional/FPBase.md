---
title: 函数式编程基础
date: 2018-11-21 10:56:52
tags: 
    - 函数式编程
categories:
    - 基础
---

💠

- 1. [函数式编程概述](#函数式编程概述)
    - 1.1. [什么是函数式编程](#什么是函数式编程)
    - 1.2. [函数式编程的核心思想](#函数式编程的核心思想)
        - 1.2.1. [1. 函数作为一等公民](#1-函数作为一等公民)
        - 1.2.2. [2. 不可变数据](#2-不可变数据)
        - 1.2.3. [3. 声明式编程风格](#3-声明式编程风格)
    - 1.3. [函数式编程 vs 面向对象编程](#函数式编程-vs-面向对象编程)
        - 1.3.1. [主要区别](#主要区别)
        - 1.3.2. [函数式编程的优势](#函数式编程的优势)
        - 1.3.3. [何时使用函数式编程](#何时使用函数式编程)
- 2. [核心概念与原则](#核心概念与原则)
    - 2.1. [纯函数 (Pure Functions)](#纯函数-pure-functions)
        - 2.1.1. [纯函数的优势](#纯函数的优势)
    - 2.2. [不可变性 (Immutability)](#不可变性-immutability)
        - 2.2.1. [为什么需要不可变性](#为什么需要不可变性)
        - 2.2.2. [实现方式](#实现方式)
    - 2.3. [高阶函数 (Higher-Order Functions)](#高阶函数-higher-order-functions)
    - 2.4. [函数组合 (Function Composition)](#函数组合-function-composition)
        - 2.4.1. [数学表示](#数学表示)
    - 2.5. [柯里化 (Currying)](#柯里化-currying)
    - 2.6. [部分应用 (Partial Application)](#部分应用-partial-application)
        - 2.6.1. [与柯里化的区别](#与柯里化的区别)
- 3. [常见函数式编程模式](#常见函数式编程模式)
    - 3.1. [映射 (Map)](#映射-map)
        - 3.1.1. [数学表示](#数学表示)
    - 3.2. [过滤 (Filter)](#过滤-filter)
    - 3.3. [归约 (Reduce/Fold)](#归约-reducefold)
        - 3.3.1. [Reduce 的工作原理](#reduce-的工作原理)
    - 3.4. [其他常用高阶函数](#其他常用高阶函数)
        - 3.4.1. [FlatMap](#flatmap)
        - 3.4.2. [TakeWhile / DropWhile](#takewhile--dropwhile)
        - 3.4.3. [组合使用](#组合使用)
- 4. [递归与尾递归](#递归与尾递归)
        - 4.0.1. [递归示例](#递归示例)
    - 4.1. [尾递归优化](#尾递归优化)
        - 4.1.1. [尾递归示例](#尾递归示例)
        - 4.1.2. [尾递归优化原理](#尾递归优化原理)
        - 4.1.3. [注意事项](#注意事项)
- 5. [Lambda 表达式与 Lambda 演算](#lambda-表达式与-lambda-演算)
    - 5.1. [Lambda 演算基础](#lambda-演算基础)
        - 5.1.1. [Lambda 演算的组成部分](#lambda-演算的组成部分)
        - 5.1.2. [Lambda 表达式的基本形式](#lambda-表达式的基本形式)
        - 5.1.3. [Lambda 演算的基本规则](#lambda-演算的基本规则)
    - 5.2. [Lambda 表达式在不同语言中的实现](#lambda-表达式在不同语言中的实现)
        - 5.2.1. [Java 8+ Lambda 表达式](#java-8+-lambda-表达式)
        - 5.2.2. [JavaScript Arrow Functions](#javascript-arrow-functions)
        - 5.2.3. [Python Lambda 表达式](#python-lambda-表达式)
    - 5.3. [闭包 (Closure)](#闭包-closure)
        - 5.3.1. [闭包的核心特征](#闭包的核心特征)
        - 5.3.2. [闭包的工作原理](#闭包的工作原理)
        - 5.3.3. [JavaScript 中的闭包示例](#javascript-中的闭包示例)
        - 5.3.4. [Java 中的闭包](#java-中的闭包)
        - 5.3.5. [Python 中的闭包](#python-中的闭包)
        - 5.3.6. [闭包的应用场景](#闭包的应用场景)
        - 5.3.7. [闭包与 Lambda 表达式的关系](#闭包与-lambda-表达式的关系)
        - 5.3.8. [闭包的注意事项](#闭包的注意事项)
        - 5.3.9. [闭包的优势](#闭包的优势)
- 6. [函数式编程的优势与应用](#函数式编程的优势与应用)
    - 6.1. [函数式编程的优势](#函数式编程的优势)
        - 6.1.1. [1. 代码简洁性](#1-代码简洁性)
        - 6.1.2. [2. 可测试性](#2-可测试性)
        - 6.1.3. [3. 并发安全](#3-并发安全)
        - 6.1.4. [4. 可维护性](#4-可维护性)
        - 6.1.5. [5. 可组合性](#5-可组合性)
        - 6.1.6. [6. 声明式风格](#6-声明式风格)
    - 6.2. [适用场景](#适用场景)
        - 6.2.1. [适合使用函数式编程的场景](#适合使用函数式编程的场景)
        - 6.2.2. [不适合使用函数式编程的场景](#不适合使用函数式编程的场景)
    - 6.3. [函数式编程与设计模式](#函数式编程与设计模式)
        - 6.3.1. [传统设计模式 vs 函数式编程](#传统设计模式-vs-函数式编程)
- 7. [实践示例](#实践示例)
    - 7.1. [Java 中的函数式编程](#java-中的函数式编程)
        - 7.1.1. [Stream API 使用](#stream-api-使用)
        - 7.1.2. [Optional 使用](#optional-使用)
        - 7.1.3. [函数式接口](#函数式接口)
    - 7.2. [JavaScript 中的函数式编程](#javascript-中的函数式编程)
        - 7.2.1. [数组操作](#数组操作)
        - 7.2.2. [函数组合](#函数组合)
    - 7.3. [实际应用案例](#实际应用案例)
        - 7.3.1. [案例1：数据处理管道](#案例1数据处理管道)
        - 7.3.2. [案例2：异步处理](#案例2异步处理)
        - 7.3.3. [案例3：配置管理](#案例3配置管理)

💠 2025-12-16 17:49:42
****************************************
# 函数式编程概述

## 什么是函数式编程

函数式编程（Functional Programming，FP）是一种编程范式，它将计算视为数学函数的求值，并避免改变状态和可变数据。

> [码农翻身:函数式编程圣经](http://mp.weixin.qq.com/s/0gErQ3tjDLZuD1bYOhi0mQ)
> [解道: 面向函数范式编程](https://www.jdon.com/functional.html)

- **函数是一等公民**：函数可以像其他数据类型一样被传递、赋值和返回
- **声明式编程**：关注"做什么"而不是"怎么做"
- **避免副作用**：函数应该只依赖于输入参数，不改变外部状态
- **表达式求值**：程序由表达式组成，而不是语句序列

## 函数式编程的核心思想

### 1. 函数作为一等公民

在函数式编程中，函数可以：
- 作为参数传递给其他函数
- 作为返回值从函数中返回
- 赋值给变量
- 存储在数据结构中

### 2. 不可变数据

数据一旦创建就不能被修改，任何"修改"操作都会创建新的数据副本。

### 3. 声明式编程风格

描述问题的本质，而不是描述解决问题的步骤。

**命令式（如何做）**：
```java
List<Integer> result = new ArrayList<>();
for (int i = 0; i < numbers.size(); i++) {
    if (numbers.get(i) > 10) {
        result.add(numbers.get(i) * 2);
    }
}
```

**声明式（做什么）**：
```java
List<Integer> result = numbers.stream()
    .filter(n -> n > 10)
    .map(n -> n * 2)
    .collect(Collectors.toList());
```

## 函数式编程 vs 面向对象编程

### 主要区别

| 特性 | 函数式编程 | 面向对象编程 |
|------|-----------|-------------|
| 核心抽象 | 函数 | 对象 |
| 数据状态 | 不可变 | 可变 |
| 编程风格 | 声明式 | 命令式 |
| 代码重用 | 函数组合 | 继承/组合 |
| 并发处理 | 天然安全 | 需要同步机制 |

### 函数式编程的优势

- **面向对象的主要限制**：不能在现有方法上增加额外的逻辑
- **函数式的解决方案**：将方法（函数）作为参数传入，然后扩展逻辑
- **与AOP的区别**：AOP是重型的基于动态代理类去封装扩展原方法，而函数式编程更加轻量和灵活

### 何时使用函数式编程

- 数据处理和转换
- 并发和并行编程
- 数学计算和算法
- 事件处理和异步编程
- 配置和策略模式

---

# 核心概念与原则

## 纯函数 (Pure Functions)

> 定义

纯函数是指满足以下条件的函数：
1. **相同输入总是产生相同输出**（确定性）
2. **没有副作用**（不修改外部状态、不进行IO操作等）

> 示例

**纯函数**：
```java
// 纯函数：相同输入总是产生相同输出，无副作用
public static int add(int a, int b) {
    return a + b;
}

public static int square(int x) {
    return x * x;
}
```

**非纯函数**：
```java
// 非纯函数：有副作用（修改外部变量）
private int counter = 0;
public int increment() {
    return ++counter; // 副作用：修改了外部状态
}

// 非纯函数：依赖外部状态
public int getCurrentTime() {
    return System.currentTimeMillis(); // 每次调用结果不同
}
```

### 纯函数的优势

- **可测试性**：易于单元测试
- **可预测性**：行为可预测
- **可缓存**：可以缓存结果
- **可并行化**：天然线程安全
- **易于推理**：代码更容易理解

## 不可变性 (Immutability)

> 概念

不可变性是指数据一旦创建就不能被修改。任何"修改"操作都会创建新的数据副本。

### 为什么需要不可变性

1. **线程安全**：不可变对象天然线程安全
2. **避免意外修改**：防止数据被意外改变
3. **易于推理**：不需要追踪状态变化
4. **支持函数式编程**：纯函数需要不可变数据

### 实现方式

**可变对象**：
```java
List<String> list = new ArrayList<>();
list.add("item1"); // 修改了原对象
list.add("item2");
```

**不可变对象**：
```java
// Java 9+ 不可变列表
List<String> list = List.of("item1", "item2");

// 创建新对象而不是修改原对象
List<String> newList = new ArrayList<>(list);
newList.add("item3");
```

## 高阶函数 (Higher-Order Functions)

> 定义

高阶函数是指：
- 接受函数作为参数的函数
- 返回函数的函数
- 或者两者兼而有之

> 示例

```java
// 接受函数作为参数
public static <T, R> List<R> map(List<T> list, Function<T, R> mapper) {
    List<R> result = new ArrayList<>();
    for (T item : list) {
        result.add(mapper.apply(item));
    }
    return result;
}

// 返回函数
public static Function<Integer, Integer> multiplyBy(int factor) {
    return x -> x * factor;
}

// 使用
Function<Integer, Integer> multiplyBy5 = multiplyBy(5);
int result = multiplyBy5.apply(10); // 50
```

## 函数组合 (Function Composition)

> 概念

函数组合是将多个函数组合成一个新函数的过程。新函数的输出是前一个函数的输入。

### 数学表示

如果 `f: A -> B` 和 `g: B -> C`，那么 `g ∘ f: A -> C`

> 示例

```java
// Java 中的函数组合
Function<Integer, Integer> addOne = x -> x + 1;
Function<Integer, Integer> multiplyByTwo = x -> x * 2;

// 组合：先加1，再乘以2
Function<Integer, Integer> composed = addOne.andThen(multiplyByTwo);
int result = composed.apply(5); // (5 + 1) * 2 = 12

// 或者：先乘以2，再加1
Function<Integer, Integer> composed2 = multiplyByTwo.andThen(addOne);
int result2 = composed2.apply(5); // (5 * 2) + 1 = 11
```

> 优势

- **代码复用**：通过组合小函数构建复杂功能
- **可读性**：代码更清晰，表达意图更明确
- **模块化**：每个函数职责单一

## 柯里化 (Currying)

> 定义

柯里化是将接受多个参数的函数转换为接受单个参数并返回接受下一个参数的函数的过程。

> 示例

**普通函数**：
```java
// 接受两个参数的函数
Function<Integer, Function<Integer, Integer>> add = a -> b -> a + b;

// 使用
int result = add.apply(5).apply(3); // 8
```

**更实际的例子**：
```java
// 柯里化的乘法函数
Function<Integer, Function<Integer, Integer>> multiply = a -> b -> a * b;

// 部分应用：创建乘以10的函数
Function<Integer, Integer> multiplyBy10 = multiply.apply(10);
int result = multiplyBy10.apply(5); // 50
```

> 优势

- **部分应用**：可以预先设置一些参数
- **函数复用**：创建更通用的函数
- **延迟求值**：可以延迟函数的执行

## 部分应用 (Partial Application)

> 定义

部分应用是固定函数的一些参数，创建一个接受更少参数的新函数。

### 与柯里化的区别

- **柯里化**：每次只接受一个参数，返回一个新函数
- **部分应用**：可以一次固定多个参数

> 示例

```java
// 原始函数
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;

// 部分应用：固定第一个参数为10
Function<Integer, Integer> add10 = b -> add.apply(10, b);
int result = add10.apply(5); // 15
```

---

# 常见函数式编程模式

## 映射 (Map)

> 概念

`map` 函数将集合中的每个元素通过给定的函数进行转换，返回一个新的集合。

### 数学表示

`map(f, [x1, x2, ..., xn]) = [f(x1), f(x2), ..., f(xn)]`

> 示例

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

// 将每个数字平方
List<Integer> squares = numbers.stream()
    .map(n -> n * n)
    .collect(Collectors.toList());
// 结果: [1, 4, 9, 16, 25]

// 将数字转换为字符串
List<String> strings = numbers.stream()
    .map(n -> "Number: " + n)
    .collect(Collectors.toList());
```

## 过滤 (Filter)

> 概念

`filter` 函数根据给定的谓词（条件）过滤集合中的元素，返回满足条件的新集合。

> 示例

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// 过滤出偶数
List<Integer> evens = numbers.stream()
    .filter(n -> n % 2 == 0)
    .collect(Collectors.toList());
// 结果: [2, 4, 6, 8, 10]

// 过滤出大于5的数
List<Integer> greaterThan5 = numbers.stream()
    .filter(n -> n > 5)
    .collect(Collectors.toList());
// 结果: [6, 7, 8, 9, 10]
```

## 归约 (Reduce/Fold)

> 概念

`reduce`（也称为 `fold`）函数将集合归约为单个值，通过累积函数逐步处理每个元素。

> 示例

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

// 求和
int sum = numbers.stream()
    .reduce(0, (a, b) -> a + b);
// 结果: 15

// 求最大值
int max = numbers.stream()
    .reduce(Integer.MIN_VALUE, Integer::max);
// 结果: 5

// 求乘积
int product = numbers.stream()
    .reduce(1, (a, b) -> a * b);
// 结果: 120
```

### Reduce 的工作原理

```
初始值: 0
[1, 2, 3, 4, 5]
  ↓
0 + 1 = 1
  ↓
1 + 2 = 3
  ↓
3 + 3 = 6
  ↓
6 + 4 = 10
  ↓
10 + 5 = 15
```

## 其他常用高阶函数

### FlatMap

将嵌套集合展平并映射：

```java
List<List<Integer>> nested = Arrays.asList(
    Arrays.asList(1, 2),
    Arrays.asList(3, 4),
    Arrays.asList(5, 6)
);

List<Integer> flattened = nested.stream()
    .flatMap(List::stream)
    .collect(Collectors.toList());
// 结果: [1, 2, 3, 4, 5, 6]
```

### TakeWhile / DropWhile

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8);

// 取满足条件的元素，直到遇到第一个不满足的
List<Integer> taken = numbers.stream()
    .takeWhile(n -> n < 5)
    .collect(Collectors.toList());
// 结果: [1, 2, 3, 4]

// 跳过满足条件的元素，直到遇到第一个不满足的
List<Integer> dropped = numbers.stream()
    .dropWhile(n -> n < 5)
    .collect(Collectors.toList());
// 结果: [5, 6, 7, 8]
```

### 组合使用

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// 过滤偶数 -> 平方 -> 求和
int result = numbers.stream()
    .filter(n -> n % 2 == 0)      // [2, 4, 6, 8, 10]
    .map(n -> n * n)               // [4, 16, 36, 64, 100]
    .reduce(0, Integer::sum);      // 220
```

---

# 递归与尾递归
在函数式编程中，递归是控制流程的主要方式，因为：
- 函数式编程避免使用可变状态，循环通常需要可变计数器
- 递归更符合数学思维，表达算法更自然
- 递归可以更好地利用不可变数据结构

> 递归 vs 循环

**非函数式语言**：尽量使用循环而不是递归（避免栈溢出）
**函数式语言**：使用递归而不是循环（有尾递归优化）

### 递归示例

**阶乘函数（普通递归）**：
```java
public static int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

**斐波那契数列（普通递归）**：
```java
public static int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

## 尾递归优化
尾递归是指递归调用是函数的最后一个操作，且返回值直接返回递归调用的结果。

> 尾递归的优势

尾递归可以将当前运行栈覆盖上一个运行栈，而不是新增一个栈帧，从而减少栈的占用，避免栈溢出。

### 尾递归示例

**阶乘函数（尾递归版本）**：
```java
public static int factorialTailRec(int n) {
    return factorialHelper(n, 1);
}

private static int factorialHelper(int n, int acc) {
    if (n <= 1) {
        return acc;
    }
    return factorialHelper(n - 1, n * acc); // 尾递归调用
}
```

**斐波那契数列（尾递归版本）**：
```java
public static int fibonacciTailRec(int n) {
    return fibonacciHelper(n, 0, 1);
}

private static int fibonacciHelper(int n, int a, int b) {
    if (n == 0) {
        return a;
    }
    if (n == 1) {
        return b;
    }
    return fibonacciHelper(n - 1, b, a + b); // 尾递归调用
}
```

### 尾递归优化原理

**普通递归**（每次调用创建新栈帧）：
```
factorial(5)
  → 5 * factorial(4)
    → 4 * factorial(3)
      → 3 * factorial(2)
        → 2 * factorial(1)
          → 1
```

**尾递归**（可以复用栈帧）：
```
factorialHelper(5, 1)
  → factorialHelper(4, 5)
    → factorialHelper(3, 20)
      → factorialHelper(2, 60)
        → factorialHelper(1, 120)
          → 120
```

### 注意事项

- **Java 不支持尾递归优化**：虽然可以写成尾递归形式，但 JVM 不会自动优化
- **Scala 支持尾递归优化**：使用 `@tailrec` 注解
- **JavaScript (ES6)**：在严格模式下支持尾递归优化
- **递归转循环**：可以将尾递归手动转换为循环

> 相关资源

- [码农翻身:张大胖学递归](http://mp.weixin.qq.com/s/YpG9TvTCBus2FK6LbArvvw)
- [深入了解尾递归](https://segmentfault.com/a/1190000007641519)
- [面试题关于递归的层层优化](https://zhuanlan.zhihu.com/p/24283256)
- [递归化循环](http://www.cnblogs.com/JeffreyZhao/archive/2009/04/01/tail-recursion-explanation.html)

************************

# Lambda 表达式与 Lambda 演算

## Lambda 演算基础

> [Lambda 演算](https://klose911.github.io/html/theory/lambda.html)

λ 演算可看做是一个简单的语义清楚的形式语言，用来解释复杂的程序设计语言或者计算模型。

### Lambda 演算的组成部分

λ 演算通常包含两部分：
- **语法**：合法表达式（λ表达式）的形式系统
- **语义**：变换规则的形式系统

### Lambda 表达式的基本形式

```
λx. M
```

其中：
- `λ` 是 lambda 符号
- `x` 是参数
- `.` 分隔参数和函数体
- `M` 是函数体

### Lambda 演算的基本规则

1. **变量**：`x` 是一个变量
2. **抽象**：`λx.M` 是一个函数，接受参数 `x`，返回 `M`
3. **应用**：`(M N)` 表示将函数 `M` 应用于参数 `N`

> 示例

```
λx. x          // 恒等函数
λx. y          // 常量函数（返回 y）
λx. λy. x      // 返回第一个参数的函数
λx. λy. y      // 返回第二个参数的函数
(λx. x) y      // 应用：结果是 y
```

## Lambda 表达式在不同语言中的实现

### Java 8+ Lambda 表达式

```java
// 无参数
Runnable r = () -> System.out.println("Hello");

// 单个参数
Function<Integer, Integer> square = x -> x * x;

// 多个参数
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;

// 方法引用
Function<String, Integer> parseInt = Integer::parseInt;
```

### JavaScript Arrow Functions

```javascript
// 无参数
const greet = () => console.log("Hello");

// 单个参数
const square = x => x * x;

// 多个参数
const add = (a, b) => a + b;

// 多行函数体
const process = (x) => {
    const doubled = x * 2;
    return doubled + 1;
};
```

### Python Lambda 表达式

```python
# 单个参数
square = lambda x: x * x

# 多个参数
add = lambda a, b: a + b

# 在函数中使用
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
```

************************


## 闭包 (Closure)

闭包是指一个函数能够访问其外部（词法）作用域中的变量，即使该函数在其外部作用域之外被调用。

### 闭包的核心特征

1. **函数嵌套**：函数定义在另一个函数内部
2. **访问外部变量**：内部函数可以访问外部函数的变量
3. **变量持久化**：外部函数的变量在外部函数执行完毕后仍然存在，被内部函数引用

### 闭包的工作原理

当内部函数引用外部函数的变量时，这些变量会被"捕获"并保存在闭包中，即使外部函数已经执行完毕，这些变量仍然可以被内部函数访问。

### JavaScript 中的闭包示例

**基本示例**：
```javascript
function outerFunction(x) {
    // 外部函数的变量
    const outerVariable = x;
    
    // 内部函数（闭包）
    function innerFunction(y) {
        // 访问外部函数的变量
        return outerVariable + y;
    }
    
    return innerFunction;
}

// 创建闭包
const closure = outerFunction(10);
console.log(closure(5)); // 15
// outerFunction 已经执行完毕，但 outerVariable 仍然可以被访问
```

**经典示例：计数器**：
```javascript
function createCounter() {
    let count = 0; // 私有变量
    
    return function() {
        count++; // 访问外部变量
        return count;
    };
}

const counter1 = createCounter();
const counter2 = createCounter();

console.log(counter1()); // 1
console.log(counter1()); // 2
console.log(counter2()); // 1 (独立的闭包)
console.log(counter1()); // 3
```

**循环中的闭包问题**：
```javascript
// 问题：所有函数都引用同一个 i
for (var i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i); // 输出: 3, 3, 3
    }, 100);
}

// 解决方案1：使用 let（块作用域）
for (let i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i); // 输出: 0, 1, 2
    }, 100);
}

// 解决方案2：使用 IIFE（立即执行函数表达式）
for (var i = 0; i < 3; i++) {
    (function(j) {
        setTimeout(function() {
            console.log(j); // 输出: 0, 1, 2
        }, 100);
    })(i);
}
```

### Java 中的闭包

Java 8+ 的 Lambda 表达式和匿名内部类可以形成闭包：

```java
// Lambda 表达式闭包
public static Function<Integer, Integer> createMultiplier(int factor) {
    // factor 被捕获到闭包中
    return x -> x * factor;
}

// 使用
Function<Integer, Integer> multiplyBy5 = createMultiplier(5);
int result = multiplyBy5.apply(10); // 50

// 匿名内部类闭包
public static Runnable createCounter() {
    final int[] count = {0}; // 必须是 final 或 effectively final
    
    return new Runnable() {
        @Override
        public void run() {
            count[0]++; // 访问外部变量
            System.out.println(count[0]);
        }
    };
}
```

**Java 闭包的限制**：
- Lambda 表达式只能访问 `final` 或 `effectively final` 的变量
- 不能修改外部变量的值（但可以修改对象的状态）

```java
// 错误：不能修改外部变量
int count = 0;
Runnable r = () -> count++; // 编译错误

// 正确：使用数组或对象包装
int[] count = {0};
Runnable r = () -> count[0]++; // 可以修改数组元素

// 或者使用 AtomicInteger
AtomicInteger count = new AtomicInteger(0);
Runnable r = () -> count.incrementAndGet();
```

### Python 中的闭包

```python
def outer_function(x):
    # 外部函数的变量
    outer_var = x
    
    def inner_function(y):
        # 访问外部函数的变量
        return outer_var + y
    
    return inner_function

# 创建闭包
closure = outer_function(10)
print(closure(5))  # 15

# 计数器示例
def create_counter():
    count = 0
    
    def counter():
        nonlocal count  # 允许修改外部变量
        count += 1
        return count
    
    return counter

counter1 = create_counter()
counter2 = create_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1
```

### 闭包的应用场景

1. **数据封装和私有变量**
   ```javascript
   function createBankAccount(initialBalance) {
       let balance = initialBalance; // 私有变量
       
       return {
           deposit: function(amount) {
               balance += amount;
               return balance;
           },
           withdraw: function(amount) {
               if (amount <= balance) {
                   balance -= amount;
                   return balance;
               }
               return "Insufficient funds";
           },
           getBalance: function() {
               return balance;
           }
       };
   }
   
   const account = createBankAccount(100);
   account.deposit(50);  // 150
   account.withdraw(30); // 120
   ```

2. **函数工厂**
   ```javascript
   function createValidator(min, max) {
       return function(value) {
           return value >= min && value <= max;
       };
   }
   
   const ageValidator = createValidator(18, 65);
   const scoreValidator = createValidator(0, 100);
   ```

3. **回调函数和事件处理**
   ```javascript
   function setupButton(buttonId, message) {
       const button = document.getElementById(buttonId);
       button.addEventListener('click', function() {
           // 闭包捕获了 message
           alert(message);
       });
   }
   ```

4. **模块模式**
   ```javascript
   const myModule = (function() {
       let privateVar = 0;
       
       return {
           increment: function() {
               privateVar++;
           },
           getValue: function() {
               return privateVar;
           }
       };
   })();
   ```

### 闭包与 Lambda 表达式的关系

- **Lambda 表达式**：匿名函数的语法糖
- **闭包**：函数捕获外部变量的机制

Lambda 表达式经常形成闭包，因为它们可以访问外部作用域的变量：

```java
int factor = 10;
Function<Integer, Integer> multiplier = x -> x * factor; // Lambda + 闭包
```

### 闭包的注意事项

1. **内存泄漏风险**：闭包会保持对外部变量的引用，可能导致内存无法释放
2. **性能考虑**：闭包会占用额外的内存来存储捕获的变量
3. **变量共享**：多个闭包可能共享同一个外部变量

### 闭包的优势

- **数据封装**：创建私有变量
- **函数工厂**：动态创建函数
- **状态保持**：在函数调用之间保持状态
- **模块化**：实现模块模式

---

# 函数式编程的优势与应用

## 函数式编程的优势

### 1. 代码简洁性

函数式编程通常可以用更少的代码表达相同的逻辑。

### 2. 可测试性

纯函数易于测试，不需要设置复杂的环境。

### 3. 并发安全

不可变数据和纯函数天然线程安全，适合并发编程。

### 4. 可维护性

代码更容易理解和维护，副作用更少。

### 5. 可组合性

小函数可以组合成复杂的功能。

### 6. 声明式风格

代码更接近问题描述，而不是实现细节。

## 适用场景

### 适合使用函数式编程的场景

1. **数据处理和转换**
   - 数据清洗
   - 数据转换
   - 数据聚合

2. **并发和并行编程**
   - 多线程处理
   - 并行计算
   - 异步编程

3. **数学计算**
   - 科学计算
   - 算法实现
   - 统计分析

4. **事件处理**
   - 事件流处理
   - 响应式编程
   - 异步事件处理

5. **配置和策略**
   - 策略模式
   - 配置管理
   - 规则引擎

### 不适合使用函数式编程的场景

1. **性能关键的系统调用**
2. **需要大量状态管理的应用**
3. **与外部系统深度集成的场景**

## 函数式编程与设计模式

> [函数式编程实现设计模式](https://klose911.github.io/html/fdp/fdp.html)

**核心观点**：`从某种意义上说，GOF的设计模式是语言表达能力的缺陷`

### 传统设计模式 vs 函数式编程

许多传统设计模式在函数式编程中变得不必要：

| 设计模式 | 函数式替代方案 |
|---------|--------------|
| 策略模式 | 高阶函数 |
| 命令模式 | 函数作为值 |
| 模板方法模式 | 函数组合 |
| 观察者模式 | 函数式响应式编程 |
| 装饰器模式 | 函数组合 |

> 示例：策略模式

**传统面向对象方式**：
```java
interface Strategy {
    int execute(int a, int b);
}

class AddStrategy implements Strategy {
    public int execute(int a, int b) { return a + b; }
}

class MultiplyStrategy implements Strategy {
    public int execute(int a, int b) { return a * b; }
}
```

**函数式方式**：
```java
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
BiFunction<Integer, Integer, Integer> multiply = (a, b) -> a * b;

// 直接使用函数
int result1 = add.apply(5, 3);
int result2 = multiply.apply(5, 3);
```

---

# 实践示例

## Java 中的函数式编程

### Stream API 使用

```java
List<Person> people = Arrays.asList(
    new Person("Alice", 25),
    new Person("Bob", 30),
    new Person("Charlie", 35)
);

// 过滤年龄大于25的人，提取姓名，转换为大写
List<String> names = people.stream()
    .filter(p -> p.getAge() > 25)
    .map(Person::getName)
    .map(String::toUpperCase)
    .collect(Collectors.toList());
```

### Optional 使用

```java
Optional<String> name = Optional.ofNullable(getName())
    .filter(n -> n.length() > 5)
    .map(String::toUpperCase);

String result = name.orElse("DEFAULT");
```

### 函数式接口

```java
// 自定义函数式接口
@FunctionalInterface
interface TriFunction<T, U, V, R> {
    R apply(T t, U u, V v);
}

// 使用
TriFunction<Integer, Integer, Integer, Integer> sum = (a, b, c) -> a + b + c;
int result = sum.apply(1, 2, 3); // 6
```

## JavaScript 中的函数式编程

### 数组操作

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// 函数式处理
const result = numbers
    .filter(n => n % 2 === 0)    // 过滤偶数
    .map(n => n * n)              // 平方
    .reduce((sum, n) => sum + n, 0); // 求和
// 结果: 220
```

### 函数组合

```javascript
// 工具函数
const compose = (...fns) => (x) => fns.reduceRight((v, f) => f(v), x);
const pipe = (...fns) => (x) => fns.reduce((v, f) => f(v), x);

// 使用
const addOne = x => x + 1;
const multiplyByTwo = x => x * 2;
const square = x => x * x;

// 组合：先加1，再乘以2，再平方
const composed = pipe(addOne, multiplyByTwo, square);
const result = composed(5); // ((5 + 1) * 2)^2 = 144
```

## 实际应用案例

### 案例1：数据处理管道

```java
// 处理用户数据：过滤、转换、聚合
List<User> users = getUsers();

Map<String, Long> result = users.stream()
    .filter(u -> u.getAge() >= 18)                    // 过滤成年人
    .filter(u -> u.isActive())                         // 过滤活跃用户
    .map(u -> u.getDepartment())                      // 提取部门
    .collect(Collectors.groupingBy(
        Function.identity(),
        Collectors.counting()                         // 统计每个部门的人数
    ));
```

### 案例2：异步处理

```java
// 使用 CompletableFuture 进行函数式异步编程
CompletableFuture<List<String>> future = CompletableFuture
    .supplyAsync(() -> fetchData())
    .thenApply(data -> data.stream()
        .filter(item -> item.isValid())
        .map(Item::getName)
        .collect(Collectors.toList()))
    .thenApply(names -> names.stream()
        .map(String::toUpperCase)
        .collect(Collectors.toList()));
```

### 案例3：配置管理

```java
// 使用函数式方式处理配置
Function<String, Optional<String>> getConfig = key -> 
    Optional.ofNullable(System.getProperty(key));

Function<String, String> getConfigWithDefault(String defaultValue) {
    return key -> getConfig.apply(key).orElse(defaultValue);
}

String dbHost = getConfigWithDefault("localhost").apply("db.host");
```
