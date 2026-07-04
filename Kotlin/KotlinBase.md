---
title: KotlinBase
date: 2026-06-14 12:03:15
tags: 
categories: 
---

💠

- 1. [Kotlin](#kotlin)
    - 1.1. [协程](#协程)

💠 2026-07-04 15:49:45
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

