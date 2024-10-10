---
title: Java中的序列化
date: 2019-04-05 22:38:44
tags: 
categories: 
    - Java
---

💠

- 1. [Java中的序列化](#java中的序列化)
    - 1.1. [Serializable](#serializable)
        - 1.1.1. [JDK序列化和反序列化](#jdk序列化和反序列化)
- 2. [编解码框架](#编解码框架)
    - 2.1. [LZ4](#lz4)
    - 2.2. [fast-serialization](#fast-serialization)
    - 2.3. [Snappy](#snappy)
    - 2.4. [Kryo](#kryo)
    - 2.5. [JSON](#json)
    - 2.6. [Protobuf](#protobuf)
    - 2.7. [Marshalling](#marshalling)
- 3. [Tips](#tips)
    - 3.1. [JSON字符串反序列化时泛型丢失问题](#json字符串反序列化时泛型丢失问题)

💠 2024-10-10 20:43:07
****************************************
# Java中的序列化
> [码农翻身:序列化： 一个老家伙的咸鱼翻身](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513589&idx=1&sn=d402d623d9121453f1e570395c7f99d7&chksm=80d67a36b7a1f32054d4c779dd26e8f97a075cf4d9ed1281f16d09f1df50a29319cd37520377&scene=21#wechat_redirect) `对象转化为二进制流`

- 序列化： 将数据结构或对象转换成二进制串的过程
- 反序列化：将在序列化过程中所生成的二进制串转换成数据结构或者对象的过程
    - 反序列化生成对象时不会调用对应类的构造器

> [Note：序列化](/Skills/Serialization/Serialization.md)`语言无关`  
> [jvm-serializers](https://github.com/eishay/jvm-serializers)`多种框架的基准测试`  

> [Java 序列化10倍性能优化对比测试-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2189625)  

默认序列化, 显式序列化, 拷贝不变（trivially copyable） `和FlatBuffers思想类似`

## Serializable
> 简单的说serialVersionUID就是类的版本控制, 标明类序列化时的版本, 版本一致表明这两个类定义一致  
> 在进行反序列化时, JVM会把传来的字节流中的serialVersionUID与本地相应实体（类）的serialVersionUID进行比较，如果相同就认为是一致的，可以进行反序列化，否则就会出现序列化版本不一致的异常。(InvalidCastException)  

- serialVersionUID有两种显示的生成方式： 
    - 一种是固定常量值，例如1L
    - 一种是根据类名、接口名、成员方法及属性等来生成一个64位的哈希字段

> 当你一个类实现了Serializable接口，如果没有定义serialVersionUID，可通过IDE进行提醒显示定义。

### JDK序列化和反序列化
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

- 在做有多态结构的`对象深拷贝`时，使用JDK序列化方式能简单且快速实现。但如果使用JSON序列化方式来实现，需要解决节点**类型信息丢失**的问题
    - 例如一个多叉树上的节点是一个接口的多类型实例。
    ```java
        public interface Node {
            List<Node> getChildes();
        }
        @Data
        public class Dir implements Node {
            private List<Node> childes;
        }
        @Data
        public class File implements Node {
            private List<Node> childes;
        }
    ```
******************************

# 编解码框架
> 因为Java序列化的性能和存储开销都表现不好,而且不能跨语言, 所以一般不使用Java的序列化而是使用以下流行的库

## LZ4
> [Github](https://github.com/lz4/lz4-java)

## fast-serialization
> [Github](https://github.com/RuedigerMoeller/fast-serialization) 10倍于JDK序列化性能而且100%兼容的编码

## Snappy
> [Github](https://github.com/xerial/snappy-java)

## Kryo
> [Github](https://github.com/EsotericSoftware/kryo)  

基准测试中得分最高的框架

## JSON
- [JSR 367: JSON-B](https://jcp.org/en/jsr/detail?id=367)
- [Jackson](https://github.com/FasterXML/jackson)
- [Gson](https://github.com/google/gson)
- [fastjson](https://github.com/alibaba/fastjson) [FASTJSON2](https://github.com/alibaba/fastjson2)

> [Github Topic: java-json](https://github.com/topics/java-json)

## Protobuf
> [Note](/Skills/Serialization/Protobuf.md)  
> [Protocol Buffer Basics: Java](https://protobuf.dev/getting-started/javatutorial/)  

`hi.proto` 快速试用
```protobuf
    package lm;
    message helloworld{
        required int32 id = 1;//ID
        required string str = 2;//str
        optional int32 opt = 3;//optional field
    }
```
- 由 proto 编译生成 Java 类： `mkdir src && protoc --java_out=./src hi.proto`

工程内使用流程简述: 通过插件将proto文件编译到指定目录(该目录设置为source并被git忽略)下的Java类, 项目编译和运行时就可以使用这些类，注意修改了协议文件就需要手动编译一次  
插件： maven-protoc-plugin  或 protobuf-gradle-plugin

*********************

## Marshalling
> JBOSS 内部使用的编解码框架

************************

# Tips
## JSON字符串反序列化时泛型丢失问题

1. Jackson 方式 需要先配置 `objectMapper.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);`
    1. 第一种 `objectMapper.writeValueAsBytes`
    1. 第二种 `objectMapper.readValue(bytes, 0, bytes.length, Object.class)`

