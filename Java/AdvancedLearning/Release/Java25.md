---
title: Java25
date: 2026-09-16 20:39:04
tags: 
categories: 
---

💠

- 1. [Java25](#java25)
- 2. [Scoped Values 作用域值](#scoped-values-作用域值)
    - 2.1. [为什么替代 ThreadLocal](#为什么替代-threadlocal)
    - 2.2. [ScopedValue 基本用法](#scopedvalue-基本用法)
    - 2.3. [ScopedValue 进阶用法](#scopedvalue-进阶用法)
    - 2.4. [迁移指南](#迁移指南)
- 3. [Structured Concurrency 结构化并发](#structured-concurrency-结构化并发)
    - 3.1. [为什么需要结构化并发](#为什么需要结构化并发)
    - 3.2. [StructuredTaskScope 基本用法](#structuredtaskscope-基本用法)
    - 3.3. [Joiner 策略](#joiner-策略)
    - 3.4. [取消与传播](#取消与传播)
    - 3.5. [与 Scoped Value 配合](#与-scoped-value-配合)
- 4. [Flexible Constructor Bodies 灵活构造器](#flexible-constructor-bodies-灵活构造器)
- 5. [Module Import Declarations 模块导入](#module-import-declarations-模块导入)
- 6. [其他特性速览](#其他特性速览)
    - 6.1. [Primitive Types in Patterns](#primitive-types-in-patterns)
    - 6.2. [Vector API](#vector-api)
    - 6.3. [Stable Values 稳定值](#stable-values-稳定值)
    - 6.4. [KDF API 密钥派生](#kdf-api-密钥派生)
    - 6.5. [PEM 编码](#pem-编码)
    - 6.6. [性能与 JVM](#性能与-jvm)
- 7. [升级与迁移检查清单](#升级与迁移检查清单)

💠 2026-09-16 20:52:46
****************************************
# Java25
> [OpenJDK 25](https://openjdk.org/projects/jdk/25/)  
> [Oracle 正式发布 Java 25 | Oracle 中国](https://www.oracle.com/cn/news/announcement/oracle-releases-java-25-2025-09-16/)  

> JDK 25 是继 JDK 21 之后的下一个 LTS 版本，正式发布日期 2025-09-16。  
> 从 JDK 21 升级到 JDK 25 的全部 JEP 列表见 [JEPs since JDK 21](https://openjdk.org/projects/jdk/25/jeps-since-jdk-21)。

# Scoped Values 作用域值
> [JEP 506: Scoped Values](https://openjdk.org/jeps/506) 在 JDK 25 正式发布（JDK 20 孵化 → 21/22/23/24 预览 → 25 转正）。  
> [JEP 429 / 446 / 464 / 481 / 487 演进历史](https://openjdk.org/jeps/506)

Scoped Value 用于「在同一个线程内、以及其子线程之间」安全地共享不可变数据，是 `ThreadLocal` 的现代替代方案，特别适合与虚拟线程、结构化并发配合。

## 为什么替代 ThreadLocal

`ThreadLocal` 的三个设计缺陷：

| 问题 | ThreadLocal | Scoped Value |
|:---|:---|:---|
| 可变性 | 任何拿到引用的人都能 `set`，数据流是「意大利面条式」的 | 无 `set` 方法，只能由调用方一次性绑定，单向传递 |
| 生命周期 | 线程存活期间一直存在，忘记 `remove` 会内存泄漏/串数据 | 由代码块结构界定，`run`/`call` 结束自动失效 |
| 继承成本 | 子线程会复制父线程的全部 ThreadLocal，内存开销大 | 子线程（StructuredTaskScope）零拷贝继承绑定 |

**结论**：当你的 ThreadLocal 是「一次写入、只读传递」的用法时，就应该换成 Scoped Value；如果是「子线程/深调用向回写数据」的双向用法，则不适合迁移。

## ScopedValue 基本用法

```java
import static java.lang.ScopedValue.where;

class Framework {

    private static final ScopedValue<FrameworkContext> CONTEXT
                        = ScopedValue.newInstance();          // (1)

    void serve(Request request, Response response) {
        var context = createContext(request);
        where(CONTEXT, context)                               // (2) 绑定
            .run(() -> Application.handle(request, response));
    }

    public PersistedObject readKey(String key) {
        var context = CONTEXT.get();                          // (3) 读取
        var db = getDBConnection(context);
        return db.readKey(key);
    }
}
```

- 绑定只对 `run`/`call` 的 lambda 及其直接、间接调用可见
- `run` 结束后绑定立即失效，此时再 `CONTEXT.get()` 会抛 `NoSuchElementException`
- `get()` 读取速度接近局部变量，与调用栈深度无关

常用方法：

| 方法 | 说明 |
|:---|:---|
| `ScopedValue.newInstance()` | 创建实例，通常声明为 `static final` 且 `private` |
| `where(v, value)` | 返回 `Carrier`，用于后续 `run`/`call` |
| `.run(Runnable)` / `.call(Callable)` | 在绑定作用域内执行，`call` 可返回值和抛异常 |
| `get()` | 读取当前线程的绑定值，未绑定抛异常 |
| `orElse(default)` | 未绑定时返回默认值（JDK 25 起 `default` 不允许为 `null`） |
| `isBound()` | 判断当前线程是否有绑定 |

## ScopedValue 进阶用法

**1. 重新绑定（嵌套作用域）**

```java
private static final ScopedValue<String> X = ScopedValue.newInstance();

void foo() {
    where(X, "hello").run(() -> bar());
}

void bar() {
    System.out.println(X.get());          // hello
    where(X, "goodbye").run(() -> baz());
    System.out.println(X.get());          // 仍是 hello
}

void baz() {
    System.out.println(X.get());          // goodbye
}
```

内层绑定只对 `baz` 可见，`bar` 自身看到的仍是外层绑定，保证生命周期有界。

**2. 一次绑定多个值**

```java
where(USER, currentUser)
    .where(TRACE_ID, traceId)
    .run(() -> process());
```

**3. 返回结果 / 抛异常用 `call`**

```java
try {
    String result = where(X, "hello").call(() -> compute());
    // ...
} catch (Exception e) {
    handleFailure(e);
}
```

## 迁移指南

适合迁移的场景：
- Web 框架的请求上下文（用户信息、事务 ID、租户 ID）
- 链路追踪的 `traceId` / `spanId`
- 检测重入（用 `isBound()` 判断是否已在某作用域内）
- 扁平化嵌套事务：外层已存在绑定则并入外层事务

不适合迁移的场景：
- 双向通信：深调用通过 `ThreadLocal.set` 给外层传数据
- 完全无结构的数据流
- 缓存昂贵可变对象（如老的 `SimpleDateFormat`，但更推荐换成 `DateTimeFormatter`）

*注意：旧版 `ForkJoinPool`、普通 `Thread` 等传统线程管理方式**不支持** Scoped Value 继承，只有 `StructuredTaskScope.fork` 出的子线程会继承父线程绑定。*

****************************************

# Structured Concurrency 结构化并发
> [JEP 505: Structured Concurrency (Fifth Preview)](https://openjdk.org/jeps/505) JDK 25 为第五次预览，API 有变化，使用时需 `--enable-preview`。  
> [JEP 428 / 437 / 453 / 462 / 480 / 499 演进历史](https://openjdk.org/jeps/505)

## 为什么需要结构化并发

用 `ExecutorService` + `Future` 的非结构化并发，出错时容易线程泄漏：

```java
Response handle() throws ExecutionException, InterruptedException {
    Future<String> user = executor.submit(() -> findUser());
    Future<Integer> order = executor.submit(() -> fetchOrder());
    String theUser = user.get();   // findUser 抛异常？
    int theOrder = order.get();
    return new Response(theUser, theOrder);
}
```

问题：
- `findUser()` 抛异常时，`fetchOrder()` 仍在后台继续跑 → 线程泄漏
- 执行 `handle()` 的线程被中断，中断不会传播给子任务
- 一个子任务失败，另一个不会被自动取消

结构化并发把「任务-子任务」关系写进代码块结构：**子任务的生命周期被限制在 try-with-resources 的块内，退出块时保证全部子任务已结束**。

## StructuredTaskScope 基本用法

> JDK 25 的重要变化：不再 `new StructuredTaskScope()`，而是用静态工厂方法 `StructuredTaskScope.open()`。

```java
Response handle() throws InterruptedException {
    try (var scope = StructuredTaskScope.open()) {
        Subtask<String> user = scope.fork(() -> findUser());
        Subtask<Integer> order = scope.fork(() -> fetchOrder());

        scope.join();   // 等待全部子任务，有失败则抛异常

        // 走到这里说明两个子任务都成功
        return new Response(user.get(), order.get());
    }
}
```

核心 API（JDK 25）：

```java
public sealed interface StructuredTaskScope<T, R> extends AutoCloseable {
    static <T> StructuredTaskScope<T, Void> open();
    static <T, R> StructuredTaskScope<T, R> open(Joiner<? super T, ? extends R> joiner);

    <U extends T> Subtask<U> fork(Callable<? extends U> task);
    Subtask<? extends T> fork(Runnable task);

    R join() throws InterruptedException;
    void close();
}
```

工作流：`open` 开作用域 → `fork` 派生子任务（默认运行在虚拟线程上）→ `join` 统一等待 → `try-with-resources` 隐式 `close` 收尾。

## Joiner 策略

默认 `open()` 的策略是「任一失败即整体失败，全部成功返回 `null`」。其他策略通过 `Joiner` 选择：

```java
// 任一子任务成功即返回（竞速，成功后取消其余）
<T> T race(Collection<Callable<T>> tasks) throws InterruptedException {
    try (var scope = StructuredTaskScope.open(Joiner.<T>anySuccessfulResultOrThrow())) {
        tasks.forEach(scope::fork);
        return scope.join();
    }
}

// 全部成功，收集所有结果
<T> List<T> runConcurrently(Collection<Callable<T>> tasks) throws InterruptedException {
    try (var scope = StructuredTaskScope.open(Joiner.<T>allSuccessfulOrThrow())) {
        tasks.forEach(scope::fork);
        return scope.join().map(Subtask::get).toList();
    }
}
```

## 取消与传播

- **短路取消**：一个子任务失败，其他未完成子任务被自动 interrupt 取消
- **中断传播**：owner 线程被中断 → `join()` 抛异常 → `close()` 取消并等待全部子任务结束
- **结构化约束**：非 owner 线程调用 `fork`、作用域未正确嵌套等会抛 `StructureViolationException`
- 子任务代码必须对中断友好；阻塞在不可中断方法上会让 `close()` 一直等下去

## 与 Scoped Value 配合

`StructuredTaskScope.fork` 出的子线程**自动继承父线程的 Scoped Value 绑定**（零拷贝）。所以「请求上下文 + 结构化并发」是天然组合：

```java
@Override
public Response handle(Request request, Response response) {
    try (var scope = StructuredTaskScope.open()) {
        Subtask<UserInfo>    user   = scope.fork(() -> readUserInfo());  // 内部可 CONTEXT.get()
        Subtask<List<Offer>> offers = scope.fork(() -> fetchOffers());
        scope.join();
        return new Response(user.get(), offers.get());
    } catch (Exception ex) {
        return reportError(response, ex);
    }
}
```

*两者都还是预览特性，生产环境需 `--enable-preview`，并注意 API 可能继续演进。*

****************************************

# Flexible Constructor Bodies 灵活构造器
> [JEP 513: Flexible Constructor Bodies](https://openjdk.org/jeps/513) JDK 25 正式发布（JDK 22/23/24 三次预览）。

允许在调用 `super(...)` / `this(...)` **之前**写语句，典型场景是「先校验参数再调用父类构造器」：

```java
class Person {
    final int age;
    Person(String name, int age) {
        if (age < 0) throw new IllegalArgumentException(...);
        this.age = age;
    }
}

class Employee extends Person {
    Employee(String name, int age) {
        if (age < 18 || age > 67) {
            throw new IllegalArgumentException("员工年龄必须在 18~67 之间");
        }
        super(name, age);   // 校验通过后才调用父类构造器
    }
}
```

约束：
- `super()`/`this()` 之前的语句**不能引用正在构造的对象**，即不能访问 `this`、不能访问本类实例字段、不能调用本类实例方法
- 可以使用构造器参数、静态成员、局部变量，以及调用静态方法
- 字段赋值必须仍在 `super()`/`this()` 之后

优点：fail-fast（参数非法时不白白执行父类构造器），并保证字段在暴露给父类构造器回调前已初始化，减少「父类构造器调用被重写方法」时的安全隐患。

****************************************

# Module Import Declarations 模块导入
> [JEP 511: Module Import Declarations](https://openjdk.org/jeps/511) JDK 25 正式发布（JDK 23/24 两次预览）。

一条语句导入模块导出的所有包，简化大量 `import`：

```java
import module java.base;   // 等价于 54 个按需包导入（java.io.* java.util.* ...）
import module java.sql;    // 含 java.sql.* javax.sql.* 及其传递依赖
```

- `import module M` 导入：M 导出给当前模块的包 + M 传递依赖模块的导出包
- 不需要调用方自己模块化，普通 classpath 代码也能用
- 简单名冲突时编译报错，用更具体的单类型导入（`import java.util.Date;`）来覆盖解决

```java
import module java.base;

import java.util.Date;   // 解决 Date 歧义

void main() {
    var list = List.of(1, 2, 3);
    var stream = Stream.of("a", "b");
    var path = Path.of("/tmp/x");
}
```

*注意：`import module java.se` 只能在显式模块内（已 `requires java.se`）使用，紧凑源文件中直接使用会失败。*

****************************************

# 其他特性速览

## Primitive Types in Patterns
> [JEP 507 (Third Preview)](https://openjdk.org/jeps/507)

允许基本类型出现在所有模式上下文中，扩展 `instanceof`/`switch` 支持全部基本类型（仍为预览）。

## Vector API
> [JEP 508 (Tenth Incubator)](https://openjdk.org/jeps/508)

仍在孵化，编译为 CPU 最优向量指令。使用需 `--add-modules jdk.incubator.vector`。

## Stable Values 稳定值
> [JEP 502 (Preview)](https://openjdk.org/jeps/502)

`final` 字段的「延迟初始化」版：声明时只创建容器，首次访问时惰性求值，且保证只初始化一次（并发安全），JVM 可做常量折叠优化。

```java
static final StableValue<Logger> logger = StableValue.of();

Logger getLogger() {
    return logger.orElseSet(() -> Logger.create("orders"));
}
```

还有 `StableValue.supplier(...)` 返回惰性 `Supplier`、`StableValue.list(...)` 返回按元素惰性初始化的列表。预览 API，需 `--enable-preview`。

## KDF API 密钥派生
> [JEP 510: Key Derivation Function API](https://openjdk.org/jeps/510) JDK 25 正式发布。

```java
KDF hkdf = KDF.getInstance("HKDF-SHA256");

AlgorithmParameterSpec params =
    HKDFParameterSpec.ofExtract()
                     .addIKM(initialKeyMaterial)
                     .addSalt(salt)
                     .thenExpand(info, 32);

SecretKey key = hkdf.deriveKey("AES", params);
```

为后量子密码（HPKE、ML-KEM 等）铺路；PBKDF2 仍走原有 `SecretKeyFactory`。

## PEM 编码
> [JEP 470 (Preview)](https://openjdk.org/jeps/470)

为密钥、证书、证书吊销列表提供 PEM 格式编解码 API（预览）。

## 性能与 JVM

```sh
    # 紧凑对象头：JDK 24 实验性 → JDK 25 产品特性（不再需要 UnlockExperimentalVMOptions）
    -XX:+UseCompactObjectHeaders

    # 分代 Shenandoah：产品特性（默认仍是非分代）
    -XX:+UseShenandoahGC -XX:ShenandoahGCMode=generational

    # AOT 缓存：一步式训练 + 生成（JEP 514）
    java -XX:AOTCacheOutput=myapp.aot -jar myapp.jar

    # 生产运行使用缓存
    java -XX:AOTCache=myapp.aot -jar myapp.jar

    # AOT 方法剖析（JEP 515）：训练运行收集方法 profile，缩短生产预热时间
    # 配合 AOTCacheOutput 自动生效，无需额外开关
```

> `-XX:AOTCacheOutput` 一步式会在训练运行之外再起一个子进程生成缓存，内存峰值约为 `-Xmx` 的两倍，资源紧张环境用两步式（`AOTMode=record` → `AOTMode=create`）。  
> 差异化环境变量 `JDK_AOT_VM_OPTIONS` 可单独给「生成缓存」子进程传参数。

****************************************

# 升级与迁移检查清单

> [JDK25 更新了哪些特性？一文全部掌握](https://cloud.tencent.com/developer/article/2539734)

**常见误解**：新 JDK 能直接跑所有旧代码。
**真相**：旧代码按规范编写、且不依赖已移除 API → 新 JDK 能跑。

JDK 25 可能破坏兼容的情况：
1. 移除已弃用 API（如 `finalize()` 相关）
2. 强化模块封装（更多内部 API 不可访问）
3. 更改默认行为（安全策略、反射限制等）
4. 第三方库未适配（JDK 25 移除 32 位 x86 端口，JEP 503）

```sh
    # 1. 扫描已弃用 API
    jdeprscan --release 25 your-app.jar

    # 2. 检查非法反射
    java --illegal-access=warn -jar your-app.jar 2>&1 | grep "Illegal reflective access"

    # 3. 分析 JDK 内部 API 依赖
    jdeps --jdk-internals --multi-release 25 --class-path . your-app.jar
```

升级建议：
- 先升级依赖/框架到明确声明支持 JDK 25 的版本
- 用 `jdeprscan`/`jdeps` 提前扫描，而不是直接上生产
- Scoped Values、结构化并发、Stable Values、PEM 等预览/新 API 先在非关键链路验证
- 虚拟线程相关：优先 `StructuredTaskScope` + `ScopedValue` 的组合，替代 `synchronized` 用 `ReentrantLock` 减少 Pinning
