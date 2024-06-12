---
title: Jetty
date: 2024-06-12 10:01:19
tags: 
categories: 
---

💠

- 1. [Jetty](#jetty)
    - 1.1. [配置](#配置)

💠 2024-06-12 10:01:44
****************************************
# Jetty

> [Jetty官网](http://www.eclipse.org/jetty/)  
> [jetty-examples](https://github.com/jetty/jetty-examples)  


[参考: Jetty使用教程（一）——开始使用Jetty ](http://www.cnblogs.com/yiwangzhibujian/p/5832597.html)

## 配置
> [相关](http://zetcode.com/java/jetty/logging/) 自身log配置

_resources/jetty-logging.properties_ 内容如下开启DEBUG
```conf
    org.eclipse.jetty.util.log.class=org.eclipse.jetty.util.log.StrErrLog
    org.eclipse.jetty.LEVEL=DEBUG
    jetty.logs=logs
```
