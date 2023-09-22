---
title: Java加密
date: 2023-09-22 19:03:18
tags: 
categories: 
---

**目录 start**

1. [Security](#security)
    1. [伪随机数生成器](#伪随机数生成器)

**目录 end**|_2023-09-22 19:03_|
****************************************
# Security
> [Java Cryptography Architecture Standard Algorithm Name Documentation for JDK 8](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html)`列出各种用途的算法,以及加密模式，信息摘要算法`

1. Provider 类 提供DSA，RSA，MD5算法
1. Security 类 管理Provider
1. MessageDigest 类 提供了信息摘要算法：MD2 MD5 SHA-1(SHA) SHA-256 SHA-384 SHA-512.

************************

## 伪随机数生成器
Random 
- 依据设置的seed作为初始值，随机序列采用[线性同余法](/Algorithm/Cryptography.md#伪随机数生成器)生成，特点是当前值需要依赖上一个随机数值更新seed。
- 因此Random用了一个AtomicLong来保存当前seed，在并发高的时候会出现忙等待

ThreadLocalRandom
- 不将seed作为共享内存，而是跟随线程绑定，Java7在ThreadLocal中，Java8则内置在了Thread类上

SecureRandom
- 不使用构造的seed，而是从操作系统的 /dev/random 和 /dev/urandom 特殊设备获取字节序列作为seed `注意如果操作系统刚启动设备内熵值不够，这个类获取随机数的话会报错`

