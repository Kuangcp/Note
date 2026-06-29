---
title: Java17
date: 2026-06-29 17:42:10
tags: 
categories: 
---


💠

- 1. [Java17](#java17)
    - 1.1. [Sealed Classes](#sealed-classes)
        - 1.1.1. [核心关键字](#核心关键字)
        - 1.1.2. [基本用法](#基本用法)
        - 1.1.3. [密封接口](#密封接口)
        - 1.1.4. [与 switch / 模式匹配联动](#与-switch--模式匹配联动)
        - 1.1.5. [省略 permits 子句](#省略-permits-子句)
        - 1.1.6. [运行时反射](#运行时反射)
        - 1.1.7. [与 `final` 的区别](#与-`final`-的区别)
        - 1.1.8. [适用场景](#适用场景)

💠 2026-06-29 17:42:10
****************************************
# Java17
> [JEP 409: Sealed Classes](https://openjdk.org/jeps/409)

## Sealed Classes
> 密封类（Sealed Classes）允许类和接口控制哪些其他类或接口可以扩展或实现它们。  
> 它提供了一种比访问修饰符更声明性的方式来限制使用超类的权限。

*在 Java 15 中作为预览功能引入，在 Java 17 中正式发布。*

**`目的`**
- 让库作者可以显式声明类型层次结构的 API 边界，而不是简单地交给访问控制
- 与模式匹配（Pattern Matching）配合，编译器能够检查 switch 是否覆盖所有可能的子类型
- 在建模有界层次结构（如代数数据类型）时提供编译期安全性

### 核心关键字

| 关键字 | 作用 |
|:---|---|
| `sealed` | 声明一个密封类/接口，限定哪些类可以继承/实现它 |
| `permits` | 显式列出允许的子类/实现类 |
| `non-sealed` | 子类声明自己不密封，允许多层继承，对继承层级无限制 |
| `final` | 子类声明自己不能再被继承 |

### 基本用法

```java
// 密封类，只允许 Circle, Rectangle, Triangle 继承
public sealed class Shape
    permits Circle, Rectangle, Triangle { }

// 三个子类必须声明继承策略：
// 1. 声明为 final —— 终止继承链
public final class Circle extends Shape { }

// 2. 声明为 non-sealed —— 开放继承（任意类可继承 Circle）
public non-sealed class Rectangle extends Shape { }

// 3. 声明为 sealed —— 继续密封继承链
public sealed class Triangle extends Shape permits EquilateralTriangle { }
```

**约束规则：**
1. 密封类与其允许的子类必须在同一个模块（module）中；如果未使用模块系统，则必须在同一个包（package）中
2. `permits` 子句可以省略——此时编译器从同一源文件或同一包中推断子类
3. 每个允许的子类必须显式声明自己是 `final`、`sealed` 还是 `non-sealed`
4. 密封类不能阻止其允许的子类做同样的事情（递归约束）

### 密封接口

```java
// 密封接口同样适用
public sealed interface Expr
    permits Constant, Add, Multiply, Negate { }

record Constant(int value) implements Expr { }
record Add(Expr left, Expr right) implements Expr { }
record Multiply(Expr left, Expr right) implements Expr { }
record Negate(Expr expr) implements Expr { }
```

> Record 天然是 `final` 的，因此非常适合作为密封接口的实现。

### 与 switch / 模式匹配联动

```java
// 编译器知道 Expr 只有 4 种子类型，能检查 switch 是否穷举
static int eval(Expr expr) {
    return switch (expr) {
        case Constant(int value) -> value;
        case Add(Expr left, Expr right) -> eval(left) + eval(right);
        case Multiply(Expr left, Expr right) -> eval(left) * eval(right);
        case Negate(Expr e) -> -eval(e);
        // 如果遗漏任何一种子类型，编译器会报错
        // 如果覆盖全部，default 分支不需要
    };
}
```

> 因为 switch 表达式的编译器知道 `Expr` 的所有可能子类，所以它可以检查 switch 是否穷举完整。

### 省略 permits 子句

```java
// Shape.java —— 同一个源文件内的嵌套子类
public sealed class Shape {
    public static final class Circle extends Shape { }
    public static final class Rectangle extends Shape { }
}

// 或者同一个包内的独立文件（模块内也一样）
// Shape.java
public sealed class Shape { }
// Circle.java —— 同包下
public final class Circle extends Shape { }
```

### 运行时反射

```java
// 检查类是否密封
Class<?> clazz = Shape.class;
if (clazz.isSealed()) {
    // 获取允许的子类
    Class<?>[] permitted = clazz.getPermittedSubclasses();
    for (Class<?> p : permitted) {
        System.out.println(p.getName());
    }
}
```

### 与 `final` 的区别

| | `final` | `sealed` |
|:---|:---|:---|
| 继承 | 完全禁止 | 有限制的允许 |
| 子类数量 | 0 | 明确限定的有限个 |
| 编译期穷举 | 不适用 | switch 可穷举检查 |
| 适用场景 | 不应被继承的工具类 | 有意限定层次结构的领域模型 |

### 适用场景
- **抽象语法树（AST）**：表达式、语句等节点类型有限且明确
- **状态机**：有限的状态枚举，每个状态作为密封类的子类建模
- **请求/响应模型**：API 的请求或返回类型有界
- **领域建模**：替代枚举，当每种类型需要携带不同数据时（配合 Record）

*******************************
