---
title: NodeJS
date: 2018-11-21 10:56:52
tags: 
    - NodeJS
categories: 
    - JavaScript
---

**目录 start**

1. [NodeJs](#nodejs)
    1. [安装](#安装)
    1. [配置](#配置)
        1. [镜像](#镜像)

**目录 end**|_2020-12-18 15:50_|
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

## 配置
### 镜像
> [镜像地址](http://npm.taobao.org/) `还包括各种常用软件`

可使用 nrm 管理 `npm instal -g nrm`
