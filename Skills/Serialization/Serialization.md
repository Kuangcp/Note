---
title: Serialization
date: 2024-04-21 16:35:34
tags: 
categories: 
---

💠

- 1. [序列化](#序列化)
    - 1.1. [序列化协议特性](#序列化协议特性)
    - 1.2. [序列化/反序列化 编码/解码](#序列化反序列化-编码解码)
    - 1.3. [网络通信中序列化和反序列化的组件](#网络通信中序列化和反序列化的组件)
- 2. [编码方式](#编码方式)
    - 2.1. [TLV](#tlv)
- 3. [解决方案](#解决方案)
    - 3.1. [XML](#xml)
    - 3.2. [JSON](#json)
    - 3.3. [MessagePack](#messagepack)
    - 3.4. [Protobuf](#protobuf)
    - 3.5. [FlatBuffers](#flatbuffers)
    - 3.6. [SBE](#sbe)
    - 3.7. [capnproto](#capnproto)
    - 3.8. [Thrift](#thrift)
    - 3.9. [Avro](#avro)

💠 2024-09-20 11:10:09
****************************************
# 序列化
> [参考: 序列化和反序列化](https://tech.meituan.com/2015/02/26/serialization-vs-deserialization.html)  

- [Hessian](http://hessian.caucho.com/)
- [Redisson 数据序列化](https://github.com/redisson/redisson/wiki/4.-%E6%95%B0%E6%8D%AE%E5%BA%8F%E5%88%97%E5%8C%96)`对象编码 方案列表`

## 序列化协议特性
1. 通用性： 跨语言，跨平台，普及流行程度
1. 强健性： 成熟度，语言/平台的公平性
1. 可调试性/可读性： 可读性高调试的成本低，例如JSON和Protobuf在查看序列化后数据，前者直接阅读后者需要工具和IDL文件做反序列化
1. 性能： 时间和空间成本
1. 扩展性：功能和业务的发展需要调整对象的字段，扩展性高的协议可以兼容共存新旧版本

************************

## 序列化/反序列化 编码/解码

> [关于序列化和编码这两个概念的疑惑](https://www.v2ex.com/t/838587)
序列化就是编码的一个实现，序列化强调结果，编码强调方式
- 编码 (一种信息方式转换为另一种信息方式)， 例如音视频的编解码就是音视频信号和二进制之间的转换，DNA编解码则是将遗传信息和碱基序列的转换
- 序列化 通常指各平台或语言将内存中的对象转换为跨平台的二进制串或字符串, 例如 C中的Struct Java中的对象 转换为XML/JSON/Protobuf

## 网络通信中序列化和反序列化的组件
面对实际应用场景里，典型的网络传输（例如 RPC，Websocket）中，序列化和反序列化流程往往需要如下组件：

- IDL（Interface description language）文件
    - 参与通讯的各方需要对通讯的内容需要做相关的约定（Specifications）。为了建立一个与语言和平台无关的约定，这个约定需要采用与具体开发语言、平台无关的语言来进行描述。这种语言被称为接口描述语言（IDL），采用IDL撰写的协议约定称之为IDL文件。
- IDL Compiler：IDL文件中约定的内容为了在各语言和平台可见，需要有一个编译器，将IDL文件转换成各语言对应的动态库。
- Stub/Skeleton Lib：负责序列化和反序列化的工作代码。
    - Stub是一段部署在分布式系统客户端的代码，一方面接收应用层的参数，并对其序列化后通过底层协议栈发送到服务端，另一方面接收服务端序列化后的结果数据，反序列化后交给客户端应用层；
    - Skeleton部署在服务端，其功能与Stub相反，从传输层接收序列化参数，反序列化后交给服务端应用层，并将应用层的执行结果序列化后最终传送给客户端Stub。
- Client/Server：指的是应用层程序代码，他们面对的是IDL所生存的特定语言的class或struct。
- 底层协议栈和互联网：序列化之后的数据通过底层的传输层、网络层、链路层以及物理层协议转换成数字信号在互联网中传递。

************************

> [CyberChef](https://github.com/gchq/CyberChef) `encryption, encoding, compression and data analysis`

# 编码方式
由于通信方式通常是流式的，需要考虑二进制流和结构化信息的正确编码方式来实现可用可靠，例如TCP流中“拆包粘包问题”

## TLV 
TLV 即 Tag - Length - Value。Tag 作为该字段的唯一标识，Length 代表 Value 数据域的长度，最后的 Value 便是数据本身

HTTP协议中有使用到类似的设计思想(在Header部分会声明Body的Length)

# 解决方案
XML序列化（Xstream）无论在性能和简洁性上比较差，JSON和Protobuf使用更为广泛， Protobuf压缩率和性能更好。  
常见的Web服务优先选择JSON有更大普适性，或者后端使用Protobuf，在网关层转为JSON。  

> FlatBuffers 和 Cap'n Proto、simple-binary-encoding，支持“零拷贝”反序列化.

## XML
XML历史悠久，其1.0版本早在1998年就形成标准，并被广泛使用至今。  
XML的最初产生目标是对互联网文档（Document）进行标记，所以它的设计理念中就包含了对于人和机器都具备可读性。 但是，当这种标记文档的设计被用来序列化对象的时候，就显得冗长而复杂（Verbose and Complex）。  
XML本质上是一种描述语言，并且具有自我描述（Self-describing）的属性，所以XML自身就被用于XML序列化的IDL。 标准的XML描述格式有两种：DTD（Document Type Definition）和XSD（XML Schema Definition）。


SOAP（Simple Object Access protocol） 是一种被广泛应用的，基于XML为序列化和反序列化协议的结构化消息传递协议
SOAP是一种采用XML进行序列化和反序列化的协议，它的IDL是WSDL. 而WSDL的描述文件是XSD，而XSD自身是一种XML文件，此时产生了递归定义

## JSON
> Javascript Object Notation

- 优点：具备可读性，自描述性（序列化时无需IDL），数据相较XML更简洁，解析成本低，原生支持JavaScript（已是Ajax事实标准）
- 缺点：数据信息占比仍较低

************************
> 二进制JSON
- JSONB JSON字符串二进制化， 例如MongoDB，PostgreSQL有使用到  
    - [ PostgreSQL JSON Types](https://www.postgresql.org/docs/current/datatype-json.html)
- [CBOR](http://cbor.io/) JSON二进制协议，多语言实现  
- [Amazon Ion](https://amazon-ion.github.io/ion-docs/index.html) 多语言实现  
- [Smile](https://github.com/FasterXML/smile-format-specification)

## MessagePack
> [Github](https://github.com/msgpack) | [Site](https://msgpack.org/)  

MessagePack 是一种高效的二进制序列化格式。它能让你在多种语言之间交换数据，就像 JSON 一样。但它的速度更快，体积更小。小整数被编码成一个字节，而典型的短字符串除了字符串本身外，只需要一个额外的字节。 可以理解为按特定规则压缩的JSON

## Protobuf
[Note: Protobuf](/Skills/Serialization/Protobuf.md)

## FlatBuffers
[Github](https://github.com/google/flatbuffers) | [Doc](https://flatbuffers.dev/index.html)

更轻量快速，适用于性能敏感的应用场景，例如移动端游戏。兼容protocolbuffer的proto文件

> [深入浅出 FlatBuffers 之 Schema](https://halfrost.com/flatbuffers_schema/)

FlatBuffer 是一个二进制 buffer，它使用 offset 组织嵌套对象（struct，table，vectors，等），可以使数据像任何基于指针的数据结构一样，就地访问数据。然而 FlatBuffer 与大多数内存中的数据结构不同，它使用严格的对齐规则和字节顺序来确保 buffer 是跨平台的。此外，对于 table 对象，FlatBuffers 提供前向/后向兼容性和 optional 字段，以支持大多数格式的演变。

FlatBuffers 的主要目标是避免反序列化。这是通过定义二进制数据协议来实现的，一种将定义好的将数据转换为二进制数据的方法。由该协议创建的二进制结构可以 wire 发送，并且无需进一步处理即可读取，即无临时对象和额外内存分配。相比较而言，在传输 JSON 时，我们需要将数据转换为字符串，通过 wire 发送，解析字符串，并将其转换为本地对象。Flatbuffers 不需要这些操作。你用二进制装入数据，发送相同的二进制文件，并直接从二进制文件读取。

## SBE
> [Simple Binary Encoding](https://github.com/real-logic/simple-binary-encoding)

## capnproto
> [Cap’n Proto](https://github.com/capnproto/capnproto)  

## Thrift
> [官网](https://thrift.apache.org/)源于Facebook, 支持多种语言: C++ C# Cocoa Erlang Haskell Java Ocami Perl PHP Python Ruby Smalltalk

它支持数据(对象)序列化和多种类型的`完整RPC服务`, Thrift适用于静态的数据交换, 需要预先定义IDL文件。  
但是由于Thrift的序列化被内嵌于Thrift框架，Thrift框架本身并没有提供序列化和反序列化接口扩展，这导致其很难和其他应用协议共同使用（例如HTTP）。  

## Avro
Avro的产生解决了JSON的冗长和没有IDL的问题，Avro属于Apache Hadoop的一个子项目。  
Avro提供两种序列化格式：JSON格式或者Binary格式。Binary格式在空间开销和解析性能方面可以和Protobuf媲美，JSON格式方便测试阶段的调试。  

由于Avro的设计理念偏向于动态类型语言，对于动态语言为主的应用场景，Avro是更好的选择。

Avro在做序列化时会将IDL定义（Schema）和数据一起传输，因此序列串具有自描述性，非常适合于做Hive、Pig和MapReduce的持久化数据格式