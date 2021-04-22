---
title: C语言
date: 2019-01-08 23:43:07
tags: 
    - 基础
categories: 
    - C
---

**目录 start**

1. [C语言](#c语言)
    1. [GCC 环境](#gcc-环境)
    1. [资源](#资源)
1. [基础](#基础)
    1. [基本语法](#基本语法)
    1. [数据类型](#数据类型)
    1. [变量和常量](#变量和常量)
    1. [函数](#函数)
        1. [main函数](#main函数)
1. [抽象设计](#抽象设计)
    1. [使用C实现元组](#使用c实现元组)
    1. [使用C实现面向对象思想](#使用c实现面向对象思想)

**目录 end**|_2021-04-22 21:33_|
****************************************
# C语言
> 个人入门编程语言, 个人觉得比用Python入门更好点, Python入门简单是不错, 但是后面如果要入手别的语言, 有C语言基础更好  

> [Github: 个人学习记录](https://github.com/Kuangcp/LearnC)  

- The C Programming Language, Second Edition, Prentice Hall, 1988 

## GCC 环境
- [mingw64](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/)

## 资源
> [C 语言教程](https://www.runoob.com/cprogramming/c-tutorial.html)  

> [玩转 C语言 基础课堂](https://study.163.com/course/introduction.htm?courseId=334013#/courseDetail?tab=1)  
> [C语言入门](https://www.imooc.com/learn/249)  

> [翁恺：程序设计入门——C语言](https://www.icourse163.org/course/ZJU-199001)  

**************************

# 基础
> 语言规范 
- [C语言代码规范（编程规范）](http://c.biancheng.net/view/158.html)

## 基本语法
- 顺序
    - 按语句声明顺序进行执行
- 选择
    - if switch 等条件判断语句 导致代码执行到该行会选择要执行的语句或语句块
- 循环
    - 语句或语句块 多次执行，依据某条件退出循环 或者依据某条件进行循环 如果条件永远无法满足或永远满足则循环将不停止 也就是死循环

## 数据类型
> [C 数据类型](https://www.runoob.com/cprogramming/c-data-types.html)

## 变量和常量

## 函数

### main函数
> [参考: C语言main()函数详解](http://c.biancheng.net/cpp/html/725.html)

- 返回类型: 推荐第一种
    1. `int main(){return 0;}`
    1. `void main(){}`
- 入参: 为空或者接收参数
    1. `int main(){return 0;}` 有隐式的入参 void
    1. `int main(int argc, char *args[]){return 0;}`

************************

# 抽象设计

## 使用C实现元组
> [making a tuple in c](https://stackoverflow.com/questions/22727404/making-a-tuple-in-c)

## 使用C实现面向对象思想
> [C语言：春节回家过年，我发现只有我没有对象！](https://mp.weixin.qq.com/s/TPZ7yO0sVoneY1ezGtWK2g)

