---
title: Java网络编程
date: 2018-11-21 10:56:52
tags: 
    - Network
categories: 
    - Java
---

💠

- 1. [Java网络编程](#java网络编程)
    - 1.1. [基础](#基础)
        - 1.1.1. [Socket](#socket)
    - 1.2. [Tips](#tips)

💠 2024-03-04 14:39:31
****************************************
# Java网络编程

> [参考: Java网络教程](http://ifeve.com/java-network/)
> [java proxy](https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html)

## 基础
> 获取主机网络信息

- [获取本地ip](https://github.com/looly/hutool/issues/428)  
- [Getting the IP address of the current machine using Java](http://stackoverflow.com/questions/9481865/getting-the-ip-address-of-the-current-machine-using-java)  

### Socket
> [码农翻身:张大胖的socket ](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513387&idx=1&sn=99665948d0b968cf15c5e7a01ffe166c&chksm=80d679e8b7a1f0febad077b57e8ad73bfb4b08de74814c45e1b1bd61ab4017b5041942403afb&scene=21#wechat_redirect)


## Tips

- 得到URL指向文件的输入流
    - `new URL(url).openStream()`

