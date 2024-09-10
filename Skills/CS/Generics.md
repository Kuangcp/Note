---
title: 泛型设计
date: 2019-04-20 12:16:10
tags: 
categories: 
    - 计算机基础
---

💠

- 1. [Generics](#generics)
    - 1.1. [协变 逆变](#协变-逆变)
- 2. [元编程](#元编程)

💠 2024-05-17 19:49:18
****************************************

# Generics

> [泛型和元编程的模型：Java, Go, Rust, Swift, D等](https://zhuanlan.zhihu.com/p/287965990)
> [generics](https://thume.ca/2019/07/14/a-tour-of-metaprogramming-models-for-generics/)

## 协变 逆变
协变(covariant)和逆变(contravariant) [.NET 泛型中的协变和逆变](https://learn.microsoft.com/zh-cn/dotnet/standard/generics/covariance-and-contravariance)

- 协变 是指能够使用与原始指定的派生类型相比，派生程度更大的类型。
    - 例如 String -> Object
- 逆变 是指能够使用派生程度更小的类型。
    - 例如 Object -> String 

> [Java 数组协变带来的静态类型漏洞](https://www.iteye.com/blog/rednaxelafx-379703)

************************

# 元编程

![Alt text](./img/generic_and_meta.webp)

