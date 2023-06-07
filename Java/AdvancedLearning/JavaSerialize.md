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
1. [Tips](#tips)
    1. [动态对JSON字符串反序列化时泛型丢失问题](#动态对json字符串反序列化时泛型丢失问题)

**目录 end**|_2023-06-07 11:00_|
****************************************
# 序列化
> [码农翻身:序列化： 一个老家伙的咸鱼翻身](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513589&idx=1&sn=d402d623d9121453f1e570395c7f99d7&chksm=80d67a36b7a1f32054d4c779dd26e8f97a075cf4d9ed1281f16d09f1df50a29319cd37520377&scene=21#wechat_redirect) `对象转化为二进制流`

> 反序列化生成对象时不会调用构造器

## serialVersionUID
> 简单的说就是类的版本控制, 标明类序列化时的版本, 版本一致表明这两个类定义一致  
> 在进行反序列化时, JVM会把传来的字节流中的serialVersionUID与本地相应实体（类）的serialVersionUID进行比较，如果相同就认为是一致的，可以进行反序列化，否则就会出现序列化版本不一致的异常。(InvalidCastException)  
[参考博客](http://swiftlet.net/archives/1268)

- serialVersionUID有两种显示的生成方式： 
    - 一种是固定常量值，例如1L
    - 一种是根据类名、接口名、成员方法及属性等来生成一个64位的哈希字段

> 当你一个类实现了Serializable接口，如果没有定义serialVersionUID，可通过IDE进行提醒显示定义。

`序列化以及反序列化一个对象`
```java
    TargetObject targetObject = new TargetObject("name");

    ByteArrayOutputStream byteOutput = new ByteArrayOutputStream();
    ObjectOutputStream output = new ObjectOutputStream(byteOutput);
    output.writeObject(targetObject);

    ByteArrayInputStream byteInput = new ByteArrayInputStream(byteOutput.toByteArray());

    ObjectInputStream input = new ObjectInputStream(byteInput);
    TargetObject result = (TargetObject) input.readObject();
    assertThat(result.getName(), equalTo("name"));
```

******************************

# 主流编解码框架
> 因为Java序列化的性能和存储开销都表现不好,而且不能跨语言, 所以一般不使用Java的序列化而是使用以下流行的库

## MessagePack
> [Github:msgpack](https://github.com/msgpack) | [参考: MessagePack：一种高效二进制序列化格式](http://hao.jobbole.com/messagepack/)

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

## Marshalling
> JBOSS 内部使用的编解码框架

# Tips
## 动态对JSON字符串反序列化时泛型丢失问题
1. 使用JDK Object序列化和反序列化
1. Jackson 方式 需要先配置 `objectMapper.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);`
    1. 第一种 objectMapper.writeValueAsBytes 
    1. 第二种 objectMapper.readValue(bytes, 0, bytes.length, Object.class)
