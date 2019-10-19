---
title: Java中的序列化
date: 2019-04-05 22:38:44
tags: 
categories: 
    - Java
---

**目录 start**
 
1. [序列化](#序列化)
    1. [serialVersionUID](#serialversionuid)
1. [主流编解码框架](#主流编解码框架)
    1. [MessagePack](#messagepack)
    1. [Protobuf](#protobuf)
    1. [Thrift](#thrift)
        1. [Marshalling](#marshalling)

**目录 end**|_2019-10-19 17:04_|
****************************************
# 序列化
> [码农翻身:序列化： 一个老家伙的咸鱼翻身](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513589&idx=1&sn=d402d623d9121453f1e570395c7f99d7&chksm=80d67a36b7a1f32054d4c779dd26e8f97a075cf4d9ed1281f16d09f1df50a29319cd37520377&scene=21#wechat_redirect) `对象转化为二进制流`

## serialVersionUID
> 简单的说就是类的版本控制, 标明类序列化时的版本, 版本一致表明这两个类定义一致  
> 在进行反序列化时, JVM会把传来的字节流中的serialVersionUID与本地相应实体（类）的serialVersionUID进行比较，如果相同就认为是一致的，可以进行反序列化，否则就会出现序列化版本不一致的异常。(InvalidCastException)  
[参考博客](http://swiftlet.net/archives/1268)

- serialVersionUID有两种显示的生成方式： 
    -  一个是默认的1L
    -  一个是根据类名、接口名、成员方法及属性等来生成一个64位的哈希字段

> 当你一个类实现了Serializable接口，如果没有定义serialVersionUID，Eclipse会提供这个提示功能告诉你去定义 。
在Eclipse中点击类中warning的图标一下，Eclipse就会自动给定两种生成的方式。
如果不想定义它，在Eclipse的设置中也可以把它关掉的，设置如下：
Window ==> Preferences ==> Java ==> Compiler ==> Error/Warnings ==>Potential programming problems
将Serializable class without serialVersionUID的warning改成ignore即可。

******************************

# 主流编解码框架
> 因为Java序列化的性能和存储开销都表现不好,而且不能跨语言, 所以一般不使用Java的序列化而是使用以下流行的库

## MessagePack
> [Github:msgpack](https://github.com/msgpack) | [参考博客: MessagePack：一种高效二进制序列化格式](http://hao.jobbole.com/messagepack/)

## Protobuf
> [protobuf-gradle-plugin](https://github.com/google/protobuf-gradle-plugin)

`hi.proto`
```protobuf
    package lm;
    message helloworld{
        required int32 id = 1;//ID
        required string str = 2;//str
        optional int32 opt = 3;//optional field
    }
```
- 由 proto 生成 Java 文件 `mkdir src && protoc --java_out=./src hi.proto`

*********************

## Thrift
> [官网](https://thrift.apache.org/)源于Facebook, 支持多种语言: C++ C# Cocoa Erlang Haskell Java Ocami Perl PHP Python Ruby Smalltalk

- 它支持数据(对象)序列化和多种类型的RPC服务, Thrift适用于静态的数据交换, 需要预先确定好他的数据结构, 当数据结构发生变化时,需要重新编辑IDL文件
### Marshalling
> JBOSS 内部使用的编解码框架
