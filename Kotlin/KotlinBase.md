---
title: KotlinBase
date: 2026-06-14 12:03:15
tags: 
categories: 
---

💠

- 1. [Kotlin](#kotlin)
    - 1.1. [协程](#协程)
        - 1.1.1. [异常处理](#异常处理)

💠 2026-07-04 16:06:53
****************************************
# Kotlin
> [Kotlin官网](https://kotlinlang.org/)  
> 一个能够跨越多个平台和领域的语言 

**实践项目**
> [mirai](https://github.com/mamoe/mirai)`Kotlin写的QQ客户端`  
> [square/okhttp](https://github.com/square/okhttp)  
> [Kuangcp/Api-X: Like postman via Kotlin Compose Desktop](https://github.com/Kuangcp/Api-X)  

**教程资源**
- [Learn Kotlin by Example](https://play.kotlinlang.org/byExample/overview)
- [Kotlin For Android](https://github.com/wangjiegulu/kotlin-for-android-developers-zh)`中文教程`
- [EasyKotlin组织](https://github.com/EasyKotlin)
    - [《Kotlin极简教程》书籍第一章](https://github.com/EasyKotlin/easy_kotlin_chapter_1)

> [Why Kotlin isn't becoming mainstream on server side ](https://www.reddit.com/r/Kotlin/comments/12o03tu/why_kotlin_isnt_becoming_mainstream_on_server_side/)


## 协程
> [Kotlin 实现](https://github.com/Kotlin/kotlinx.coroutines)

Kotlin 的协程是目前高阶现代语言中，在工程设计上走得最远的。

底层原理（CPS 变换）：
- Kotlin 的协程是无栈的。编译器在编译时，会把你的 suspend（挂起）函数转化为 CPS（Continuation-Passing Style，延续体传递样式）。
- 通俗来说，每个挂起点都会被注入一个 Continuation 参数，这个参数就像是一个“书签”，记录了代码执行到哪了。当异步操作完成后，拿着这个“书签”继续往下读。

杀手锏：结构化并发 (Structured Concurrency)：
- 这是 Kotlin 相比其他所有语言最优秀的地方。在 Go 或 Rust 中，你启动一个协程，它就像断了线的风筝，如果父任务取消了，子协程很难自动感知并跟着取消。
- 而 Kotlin 引入了 CoroutineScope。父协程会等待所有子协程结束；如果父协程失败，所有子协程会自动被级联取消。这在写复杂的业务逻辑（如 Android App 或复杂的后端微服务）时，能极大地避免协程泄漏。

与 Java 虚拟线程的区别：
- Java 21 的虚拟线程是 JVM 级别的，它欺骗了老旧的同步 API；而 Kotlin 的协程是语法层面的（可以运行在 JVM、JavaScript、甚至 Native 裸机上）。现在很多 Kotlin 后端项目选择将 Kotlin 协程的底层调度器替换为 Java 21 的虚拟线程，强强联合。

### 异常处理

* 崩溃影响：优雅的“结构化级联取消”——子协程崩溃，会联动取消兄弟协程，并将异常抛给父协程。
* 底层根源：Kotlin 是一门极其重视工程实践的语言，它在语言层面原生引入了“结构化并发（Structured Concurrency）”。所有的协程必须在某个 CoroutineScope（作用域）内启动。当一个子协程发生未捕获异常时：
1. 它会立刻把这个异常向上汇报给它的父协程。
   2. 父协程收到后，会自动向该作用域下的所有其他子协程（兄弟协程）发送取消信号。
   3. 最终，如果最外层没有配置 CoroutineExceptionHandler（异常处理器），才会让整个进程崩溃。
* 语言的取舍：牺牲了一定的运行时纯粹性，换取了“最完美的工程容错与资源管理”。

Kotlin 认为，在实际业务中，多个并发任务通常是属于同一个业务逻辑的（例如同时请求用户信息和用户订单）。如果其中一个子任务由于网络彻底崩溃了，那么继续执行另一个兄弟任务也是浪费算力。所以，它用一套极其精致的级联机制，在“进程直接死掉”和“子任务悄悄死掉”之间，找到了最符合业务直觉的解法。

