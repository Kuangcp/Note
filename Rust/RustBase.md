---
title: Rust基础
date: 2020-03-22 12:34:33
tags: 
categories: 
---

💠

- 1. [Rust](#rust)
    - 1.1. [异步](#异步)
        - 1.1.1. [协程](#协程)

💠 2026-07-05 17:38:32
****************************************
# Rust 
> [get started](https://www.rust-lang.org/zh-CN/learn/get-started)

1. 安装 rustup
1. rustup default stable/nightly 安装发行版或开发版
    - rustup update 更新工具链到最新
1. 装好后就有了 rustc cargo 工具链
1. [Kuangcp/RustBase](https://github.com/Kuangcp/RustBase)`实验项目`  


## 异步
> [Tokio - An asynchronous Rust runtime](https://tokio.rs/)`Discord、Cloudflare、AWS`  


### 协程

> 🕵️‍♂️ 为什么会发生这个报错？（底层原理） `Future cannot be sent between threads safely`

当你使用 tokio::spawn(async move { ... }) 时，Tokio 默认使用的是多线程工作窃取（Work-Stealing）调度器。这意味着：

* 你的这个异步任务（也就是那张“便签纸”）最初可能在线程 A 上运行。
* 当运行到某个 .await 挂起时，线程 A 把这张“便签纸”收起来，放回任务队列。
* 下次被唤醒时，线程 B 刚好空闲，它会把这张“便签纸”捡起来，在线程 B 上继续运行。

关键冲突点来了：
如果你的“便签纸”上，记录了一个不能在线程之间安全传递的变量（比如非线程安全的指针 Rc、或者是未加锁的普通的 RefCell）。
当这个任务从线程 A 转移到线程 B 时，Rust 的类型系统就会发现危险：“等等！你怎么能在线程 B 里去读一个属于线程 A 且不支持跨线程的变量呢？！”
于是，编译器大手指一挥，直接抛出 Send trait 缺失的错误，拒绝编译。

当你面对长达几页的 Future is not Send 报错不知所措时，教你一个看懂报错的秘诀：

   1. 从下往上看：Rust 的编译器非常贴心，它会在报错信息的最后几行，明确用一个箭头指向具体的代码行，告诉你：...which opens a scope that contains a non-Send type。
   2. 找那个 .await：顺着代码找那一行附近的 .await，看看在它上方创建的哪个变量，生命周期一直延续到了 .await 的下方。把它干掉或者换成 Arc/Atomic 类型，问题迎刃而解。

如果Web服务里需要在多个路由之间共享状态（比如让 /v1/chat/completions 能读写一个全局的配置或计数器），我们可以直接写一个用 `Arc<Mutex<...>>` 在 Axum 中安全共享状态的标准模版！

