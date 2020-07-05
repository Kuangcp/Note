---
title: 多种配置文件格式
date: 2018-11-21 10:56:52
tags: 
    - 基础
categories: 
    - 计算机基础
---

**目录 start**

1. [配置文件格式](#配置文件格式)
    1. [conf或者ini](#conf或者ini)
    1. [Toml](#toml)
    1. [HOCON](#hocon)
    1. [Properties](#properties)
        1. [Java中的使用](#java中的使用)
    1. [XML](#xml)
    1. [YAML](#yaml)
        1. [Java中的使用](#java中的使用)
    1. [JSON](#json)
        1. [BSON](#bson)
        1. [Smile](#smile)

**目录 end**|_2020-07-05 14:58_|
****************************************
# 配置文件格式

## conf或者ini

```ini
    [main]
    debug=true
    [client]
    timeOut=10
```

************************
## Toml
> [Github: toml](https://github.com/toml-lang/toml)

## HOCON
Human-Optimized Config Object Notation

> [Official Doc](https://docs.spongepowered.org/stable/zh-CN/server/getting-started/configuration/hocon.html)

> Nginx 的配置文件就是使用该格式

************************
## Properties

### Java中的使用

通过ResourceBundle获取classPath下的属性文件
```java
    ResourceBundle bundle = ResourceBundle.getBundle("test");
    String city = bundle.getString("name");
```

通过Properties对象获取配置文件
```java
    Properties pro = new Properties();
    pro.load(new FileInputStream(new File("./test.properties")));
    String name = (String) pro.get("name");
```

使用Properties保存配置文件
```java
    Properties pro = new Properties();
    pro.setProperty("name", "java");
    pro.setProperty("study", "sdf");
    pro.store(new FileOutputStream(new File("test.properties")), "one file");
```

************************
## XML
> 可阅读性强, 结构清晰, 但是太繁杂, 信息承载比重小

************************
## YAML
> yaml is ain't markup language

- [入门博客](http://blog.csdn.net/liukuan73/article/details/78031693)
- [Python使用YML](http://www.cnblogs.com/c9com/archive/2013/01/05/2845539.html)

### Java中的使用
- Springboot将这种配置文件引入了我的视野，使用这个用来自定义配置文件要特别注意采用小写（不然影响反射中set方法）

- [Jackson操作yaml](https://dzone.com/articles/read-yaml-in-java-with-jackson)

************************

## JSON
> [Google 规范](https://github.com/darcyliu/google-styleguide/blob/master/JSONStyleGuide.md)

> [JSON in Java](https://www.baeldung.com/java-json)  

### BSON

### Smile
> 二进制的JSON [Wikipedia: Smile](https://en.wikipedia.org/wiki/Smile_%28data_interchange_format%29)
