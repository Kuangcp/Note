---
title: Dubbo
date: 2019-05-09 16:47:23
tags: 
categories: 
    - Java
---

**目录 start**

1. [Dubbo](#dubbo)
    1. [SPI](#spi)
    1. [Tips](#tips)

**目录 end**|_2020-10-12 14:58_|
****************************************
# Dubbo 
> [Official Doc](http://dubbo.apache.org/zh-cn/docs/user/quick-start.html)  | [Github](https://github.com/apache/incubator-dubbo) 
> [Sample](https://github.com/apache/incubator-dubbo-samples)  

RegistryService 通过查看 Type Hierarchy 可以看到所有 Dubbo 支持的注册中心

## SPI
[META-INF 目录结构](https://docs.oracle.com/en/java/javase/11/docs/specs/jar/jar.html#the-meta-inf-directory)


## Tips 
> SpringBoot 整合 Dubbo 使用 XML 方式 只需在Configuration注解类上引入 dubbo 配置文件 例如 引入 dubbo目录下的配置文件 `@ImportResource({"classpath:dubbo/*.xml"})`
