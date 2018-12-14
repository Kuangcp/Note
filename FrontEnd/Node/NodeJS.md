---
title: NodeJS.md
date: 
tags: 
    - NodeJS
categories: 
    - JavaScript
---

**目录 start**
 
1. [NodeJs](#nodejs)
    1. [安装](#安装)
    1. [配置](#配置)
        1. [使用淘宝的镜像](#使用淘宝的镜像)
    1. [使用](#使用)
        1. [安装Vue](#安装vue)

**目录 end**|_2018-12-13 20:53_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
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
### 使用淘宝的镜像
> [镜像地址](http://npm.taobao.org/) `还包括各种常用软件`

1. 临时使用 `npm --registry https://registry.npm.taobao.org install express`
2. 永久使用 `npm config set registry https://registry.npm.taobao.org`
3. 通过cnpm使用 `npm install -g cnpm --registry=https://registry.npm.taobao.org` _emmm, 为什么我就配置不成功_

> 查看配置是否成功: `npm config get registry`

## 使用

> [Hexo](/Skills/View/Hexo.md)


### 安装Vue
> `npm install -g vue-cli --registry=https://registry.npm.taobao.org`


