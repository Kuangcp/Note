---
title: Jetty
date: 2018-12-17 21:28:44
tags: 
    - Jetty
categories:
    - Java
---

**目录 start**
 
1. [Jetty](#jetty)
    1. [配置](#配置)

**目录 end**|_2019-04-19 15:38_|
****************************************
# Jetty


[参考博客: Jetty使用教程（一）——开始使用Jetty ](http://www.cnblogs.com/yiwangzhibujian/p/5832597.html)

## 配置
_自身log配置_
> [相关](http://zetcode.com/java/jetty/logging/)
_resources/jetty-logging.properties_ 内容如下开启DEBUG
```conf
    org.eclipse.jetty.util.log.class=org.eclipse.jetty.util.log.StrErrLog
    org.eclipse.jetty.LEVEL=DEBUG
    jetty.logs=logs
```

