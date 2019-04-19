---
title: 多种配置文件格式
date: 2018-11-21 10:56:52
tags: 
    - 基础
categories: 
    - 基础知识
---

**目录 start**
 
1. [配置文件](#配置文件)
    1. [conf或者ini](#conf或者ini)
    1. [properties](#properties)
    1. [XML](#xml)
    1. [YAML](#yaml)
        1. [Java使用](#java使用)
    1. [JSON](#json)
        1. [Jackson](#jackson)

**目录 end**|_2019-04-19 15:38_|
****************************************
# 配置文件

## conf或者ini
```
    [main]
    debug=true
    [client]
    timeOut=10
```

## properties

## XML
> 可阅读性强, 结构清晰, 但是太繁杂, 信息承载比重小

## YAML
> yaml is ain't markup language

- [入门博客](http://blog.csdn.net/liukuan73/article/details/78031693)
- [Python使用YML](http://www.cnblogs.com/c9com/archive/2013/01/05/2845539.html)

### Java使用
- Springboot将这种配置文件引入了我的视野，使用这个用来自定义配置文件要特别注意采用小写（不然影响反射中set方法）

- [Jackson操作yaml](https://dzone.com/articles/read-yaml-in-java-with-jackson)

## JSON
> [Google 规范](https://github.com/darcyliu/google-styleguide/blob/master/JSONStyleGuide.md)

### Jackson
- [Jackcon 注解的讲解](http://blog.csdn.net/sdyy321/article/details/40298081)
