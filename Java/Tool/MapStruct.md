---
title: MapStruct
date: 2021-05-17 00:27:57
tags: 
categories: 
---

**目录 start**

1. [MapStruct](#mapstruct)

**目录 end**|_2021-05-17 00:27_|
****************************************
# MapStruct
> [Official Site](https://mapstruct.org/)  

实现方式是 通过注解在编译期生成对应接口的实现类（模板代码 手动 get set） 到 target/generated-sources 目录下

缺点： 
- 类改动需要重新清空并编译，不然可能造成新加字段没有正常 get set
- null转换为空List，Map等需要手动标记。
- 泛型集合会自动做类型转换可能引发问题
