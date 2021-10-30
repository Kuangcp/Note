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

实现方式为 通过注解在编译期生成对应接口的实现类（模板代码 手动 get set） 到 target/generated-sources 目录下, 并将该目录加入 class-path

优点：
- 生成get set 模板代码 性能好

缺点： 
- 类改动需要重新清空并编译，可能造成新加字段没有正常生成对应的 get set 代码
- 集合属性的null值转换为 空List，Map等需要手动注解声明。
- 泛型集合会自动做类型转换可能引发问题
