---
title: Java网络编程
date: 2018-11-21 10:56:52
tags: 
    - 网络
categories: 
    - Java
---

💠

- 1. [Java网络编程](#java网络编程)
    - 1.1. [基础](#基础)
    - 1.2. [Socket](#socket)
        - 1.2.1. [Tuning](#tuning)
    - 1.3. [Tips](#tips)

💠 2025-03-13 10:41:25
****************************************
# Java网络编程

> [参考: Java网络教程](http://ifeve.com/java-network/)
> [java proxy](https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html)

## 基础
> 获取主机网络信息

- [获取本地ip](https://github.com/looly/hutool/issues/428)  
- [Getting the IP address of the current machine using Java](http://stackoverflow.com/questions/9481865/getting-the-ip-address-of-the-current-machine-using-java)  

## Socket
> [码农翻身:张大胖的socket ](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513387&idx=1&sn=99665948d0b968cf15c5e7a01ffe166c&chksm=80d679e8b7a1f0febad077b57e8ad73bfb4b08de74814c45e1b1bd61ab4017b5041942403afb&scene=21#wechat_redirect)


### Tuning
> Connection reset
服务器关闭了Connection会返回“RST”而不是返回“FIN”标志。原因在于Socket.close()方法的语义和TCP的“FIN”标志语义不一样：
- 发送TCP的“FIN” 标志表示 我不再发送数据了
- Socket.close() 表示我不再发送也不接受数据了。
问题就出在“我不接受数据” 上，如果此时客户端还往服务器发送数据，服务器内核接收到数据，但是发现此时Socket已经close了，则会返回“RST”标志给客户端。
此时客户端就会提示：“Connection reset”。

> [Orderly (and Abortive) Connection Release in Java](https://docs.oracle.com/javase/1.5.0/docs/guide/net/articles/connection_release.html)  

************************

## Tips

- 得到URL指向文件的输入流
    - `new URL(url).openStream()`

