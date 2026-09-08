---
title: NodeJS
date: 2018-11-21 10:56:52
tags: 
    - NodeJS
categories: 
    - JavaScript
---

💠

- 1. [NodeJs](#nodejs)
    - 1.1. [安装](#安装)
    - 1.2. [配置](#配置)
        - 1.2.1. [镜像](#镜像)
    - 1.3. [协程](#协程)

💠 2026-09-08 15:26:24
****************************************
# NodeJs

## 安装
> [Node.js — Download Node.js®](https://nodejs.org/en/download)`nvm 管理多版本`  

包管理：默认的npm(隔离，复制) 扩展的pnpm（硬链接，省空间）  
运行：  npx 不安装依赖 执行后删除依赖  

npm root -g 查看全局安装路径
npm root 查看本地安装位置，也就是局部安装

## 配置
### 镜像
> [镜像地址](http://npm.taobao.org/) `还包括各种常用软件`

可使用 nrm 管理 `npm instal -g nrm`

## 协程

JS 的 async/await 在前端和 Node.js 后端应用极广，它是无栈协程的典型代表。

底层语义（事件循环 Event Loop）：
- JS 是单线程的。当你在 JS 里写 await fetch() 时，它的语义是：“我把这个网络请求交给操作系统，当前函数暂停并退出执行栈；等网络数据回来了，把它放进‘微任务队列’，等主线程空闲了再捞起来继续。”

与 Rust 的区别：
- JS 因为是单线程的，所以绝对不会遇到 Rust 那种跨线程的 Send 报错，也永远不需要加锁。但代价是，如果你的 JS 协程里写了一个死循环或者耗时计算，整个网页或整个 Node.js 服务就会瞬间卡死。

