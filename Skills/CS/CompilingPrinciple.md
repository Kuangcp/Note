---
title: 编译原理
date: 2019-01-06 14:33:13
tags: 
categories: 
    - 基础
---

**目录 start**
 
1. [编译原理](#编译原理)
    1. [编译技术](#编译技术)
        1. [JIT](#jit)
        1. [AOT](#aot)
    1. [AST](#ast)

**目录 end**|_2019-10-19 17:04_|
****************************************
# 编译原理

## 编译技术
### JIT
> Just in time 

在运行时才将源码编译成机器码

### AOT
> Ahead of time 

预先将所源码编译成机器码

## AST
> Abstract Syntax Tree 

用处: 错误提示、自动补全、重构、语法检查, 代码混淆, 静态代码分析, 自动生成测试代码 ...

> [参考博客: 从现在起-彻底学会 js ast](https://segmentfault.com/a/1190000017992387)
> [参考博客: Java代码分析器(一): JDT入门](https://segmentfault.com/a/1190000000609246)

- [Github: java parser](https://github.com/javaparser/javaparser)`Java生成AST`
