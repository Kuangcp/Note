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

💠 2026-07-04 15:49:45
****************************************
# NodeJs

## 安装
1. [官网下载](https://nodejs.org/en/)
2. 进入解压的 `bin/node 和 npm ` 建立软链接到 `/usr/local/bin/` 目录下
3. 执行 node --version 和 npm -v 查看是否配置成功
4. 添加node的真正解压目录到环境变量中， 之后安装的模块才能被找到
```sh
    NODE_HOME=/home/kcp/Application/sdk/node-v8.11.1-linux-x64
    export PATH=$PATH:$NODE_HOME/bin
```

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

