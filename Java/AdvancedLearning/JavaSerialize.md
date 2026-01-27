---
title: Java中的序列化
date: 2019-04-05 22:38:44
tags: 
categories: 
    - Java
    - 序列化
---

💠

- 1. [Java中的序列化](#java中的序列化)
    - 1.1. [Serializable](#serializable)
        - 1.1.1. [JDK序列化和反序列化](#jdk序列化和反序列化)
    - 1.2. [Externalizable (基本不用到)](#externalizable-基本不用到)
        - 1.2.1. [与 Serializable 的区别](#与-serializable-的区别)
        - 1.2.2. [基本使用](#基本使用)
        - 1.2.3. [序列化和反序列化示例](#序列化和反序列化示例)
        - 1.2.4. [注意事项](#注意事项)
        - 1.2.5. [使用场景](#使用场景)
- 2. [编解码框架](#编解码框架)
    - 2.1. [LZ4](#lz4)
    - 2.2. [fast-serialization](#fast-serialization)
    - 2.3. [Snappy](#snappy)
    - 2.4. [Kryo](#kryo)
    - 2.5. [JSON](#json)
    - 2.6. [Protobuf](#protobuf)
    - 2.7. [protostuff](#protostuff)
    - 2.8. [Marshalling](#marshalling)
- 3. [Tips](#tips)
    - 3.1. [JSON字符串反序列化时泛型丢失问题](#json字符串反序列化时泛型丢失问题)

💠 2026-01-27 19:13:38
****************************************
# Java中的序列化
> [码农翻身:序列化： 一个老家伙的咸鱼翻身](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513589&idx=1&sn=d402d623d9121453f1e570395c7f99d7&chksm=80d67a36b7a1f32054d4c779dd26e8f97a075cf4d9ed1281f16d09f1df50a29319cd37520377&scene=21#wechat_redirect) `对象转化为二进制流`

- 序列化： 将数据结构或对象转换成二进制串的过程
- 反序列化：将在序列化过程中所生成的二进制串转换成数据结构或者对象的过程
    - 反序列化生成对象时不会调用对应类的构造器

> [Note：序列化](/Skills/Serialization/Serialization.md)`语言无关`  
> [jvm-serializers](https://github.com/eishay/jvm-serializers)`多种框架的基准测试`  

> 默认序列化, 显式序列化, 拷贝不变（trivially copyable） `和FlatBuffers思想类似`

- [Java 序列化10倍性能优化对比测试-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2189625)  
- [OpenHFT/Chronicle-Queue: Micro second messaging that stores everything to disk](https://github.com/OpenHFT/Chronicle-Queue)  

## Serializable
> 简单的说serialVersionUID就是类的版本控制, 标明类序列化时的版本, 版本一致表明这两个类定义一致  
> 在进行反序列化时, JVM会把传来的字节流中的serialVersionUID与本地相应实体（类）的serialVersionUID进行比较，如果相同就认为是一致的，可以进行反序列化，否则就会出现序列化版本不一致的异常。(InvalidCastException)  

- serialVersionUID有两种显示的生成方式： 
    - 一种是固定常量值，例如1L
    - 一种是根据类名、接口名、成员方法及属性等来生成一个64位的哈希字段

> 当你一个类实现了Serializable接口，如果没有定义serialVersionUID，可通过IDE进行提醒显示定义。如果要使用JDK的序列方式, 一定要显式定义, 且后续不能改, 除非业务上确认不兼容. 

> 子接口 Externalizable， 实现writeExternal()和readExternal()⽅法可以指定序列化哪些属性

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

## Externalizable (基本不用到)
> `Externalizable` 是 `Serializable` 的子接口，提供了更细粒度的序列化控制。通过实现 `writeExternal()` 和 `readExternal()` 方法，可以完全自定义序列化和反序列化的过程。

### 与 Serializable 的区别

| 特性 | Serializable | Externalizable |
|------|-------------|----------------|
| 序列化方式 | 自动序列化所有非 transient 字段 | 手动控制序列化哪些字段 |
| 方法实现 | 无需实现方法（可选 writeObject/readObject） | 必须实现 writeExternal() 和 readExternal() |
| 性能 | 相对较慢（反射机制） | 相对较快（直接控制） |
| 灵活性 | 较低 | 较高 |
| 构造器调用 | 反序列化时不调用构造器 | 反序列化时会先调用无参构造器 |

### 基本使用

```java
import java.io.*;

public class User implements Externalizable {
    private String name;
    private int age;
    private transient String password; // transient 字段不会被自动序列化
    
    // Externalizable 要求必须有无参构造器
    public User() {
        System.out.println("无参构造器被调用");
    }
    
    public User(String name, int age, String password) {
        this.name = name;
        this.age = age;
        this.password = password;
    }
    
    // 自定义序列化逻辑
    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeObject(name);
        out.writeInt(age);
        // 可以选择不序列化 password，或者进行加密后序列化
        // out.writeObject(password);
    }
    
    // 自定义反序列化逻辑
    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
        name = (String) in.readObject();
        age = in.readInt();
        // 对应 writeExternal 中的读取顺序
        // password = (String) in.readObject();
    }
    
    // getter/setter 方法...
}
```

### 序列化和反序列化示例

```java
// 序列化
User user = new User("张三", 25, "secret123");
ByteArrayOutputStream byteOutput = new ByteArrayOutputStream();
ObjectOutputStream output = new ObjectOutputStream(byteOutput);
output.writeObject(user);
output.close();

// 反序列化
ByteArrayInputStream byteInput = new ByteArrayInputStream(byteOutput.toByteArray());
ObjectInputStream input = new ObjectInputStream(byteInput);
User deserializedUser = (User) input.readObject();
input.close();

// 注意：反序列化时会先调用无参构造器，然后调用 readExternal 方法
```

### 注意事项

1. **必须有无参构造器**：`Externalizable` 要求类必须提供 public 无参构造器，因为反序列化时会先调用它
2. **读写顺序一致**：`writeExternal()` 和 `readExternal()` 中的字段读写顺序必须完全一致
3. **版本兼容性**：与 `Serializable` 一样，修改类结构时需要注意版本兼容性
4. **性能考虑**：虽然性能更好，但需要手动维护序列化逻辑，代码复杂度更高

### 使用场景

- 需要精确控制序列化哪些字段
- 需要对某些字段进行加密或特殊处理
- 性能敏感的场景
- 需要序列化 transient 字段（通过手动实现）

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

Jackson在将Date对象序列化成时间时，默认使用的是UTC零时区，Fastjson是使用系统时区。

```conf
# 设置jackson序列化时区
spring.jackson.time-zone=Asia/Shanghai
spring.jackson.serialization.write-dates-as-timestamps=false
```

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

## protostuff

> [protostuff/protostuff: Java serialization library, proto compiler, code generator](https://github.com/protostuff/protostuff)`无需proto文件`  

原理： 它在运行时动态生成了一份与 .proto 等价的 Schema——这份 Schema 完全由 Java 类元信息（类名、字段名、字段类型、顺序）推导出来，随后像 protobuf 一样按序号编码，因此序列化/反序列化时不再需要静态的 .proto IDL文件。

*********************

## Marshalling
> JBOSS 内部使用的编解码框架

************************

# Tips
## JSON字符串反序列化时泛型丢失问题

1. Jackson 方式 需要先配置 `objectMapper.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);`
    1. 第一种 `objectMapper.writeValueAsBytes`
    1. 第二种 `objectMapper.readValue(bytes, 0, bytes.length, Object.class)`

