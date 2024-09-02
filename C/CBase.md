---
title: C语言
date: 2019-01-08 23:43:07
tags: 
    - 基础
categories: 
    - C
---

💠

- 1. [C语言](#c语言)
    - 1.1. [GCC 环境](#gcc-环境)
    - 1.2. [资源](#资源)
- 2. [基础](#基础)
    - 2.1. [基本语法](#基本语法)
    - 2.2. [数据类型](#数据类型)
    - 2.3. [变量和常量](#变量和常量)
    - 2.4. [函数](#函数)
        - 2.4.1. [main函数](#main函数)
- 3. [抽象设计](#抽象设计)
    - 3.1. [使用C实现元组](#使用c实现元组)
    - 3.2. [使用C实现面向对象思想](#使用c实现面向对象思想)

💠 2024-09-02 17:14:24
****************************************
# C语言
> 个人入门编程语言, 个人觉得比用Python入门更好点, Python入门简单是不错, 但是后面如果要入手别的语言, 有C语言基础更好  

> [Github: 个人学习记录](https://github.com/Kuangcp/LearnC)  

- The C Programming Language, Second Edition, Prentice Hall, 1988 

> [Cosmopolitan](https://github.com/jart/cosmopolitan) `一次编译，处处执行`

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

