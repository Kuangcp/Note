---
title: TestNG
date: 2018-11-21 10:56:52
tags: 
    - 测试
    - TestNG
categories: 
    - Java
---

**目录 start**

1. [TestNG](#testng)
    1. [使用](#使用)
        1. [基本注解](#基本注解)

**目录 end**|_2020-04-27 23:42_|
****************************************
# TestNG
> [Official Doc](http://testng.org/doc/documentation-main.html) 

> [易百: TestNG教程](https://www.yiibai.com/testng/)  
> [TestNG 入门教程](http://www.cnblogs.com/TankXiao/p/3888070.html) 
> [testNG官方文档](http://testng.org/doc/index.html) | [Github:TestNG](https://github.com/cbeust/testng)  
> [tools](http://toolsqa.com/selenium-webdriver/testng-introduction/)

## 使用
> 基本使用

**Gradle使用**
```groovy
    testCompile group: 'org.testng', name: 'testng', version: '6.14.3'
```
然后和Junit使用是一致的, 在方法上打上 @Test 注解即可运行, 注意Test注解的包为 `import org.testng.annotations.Test;`

### 基本注解
1. @Test
    - threadPoolSize
    - invocationCount
    - timeOut
    - invocationTimeOut

> 测试方法中使用多线程, 和Junit是一致的, 只要主线程退出了, 其中创建的线程也会立即退出  
> 但是 TestNG 并行执行测试方法会更方便

