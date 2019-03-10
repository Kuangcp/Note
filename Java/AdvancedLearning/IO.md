---
title: Java的IO
date: 2018-11-21 10:56:52
tags: 
    - IO
categories: 
    - Java
---

**目录 start**
 
1. [IO操作的学习](#io操作的学习)
    1. [Java IO简史](#java-io简史)
        1. [BIO](#bio)
        1. [NIO](#nio)
        1. [AIO](#aio)
    1. [基本文件IO操作](#基本文件io操作)
        1. [读取配置文件](#读取配置文件)
            1. [可执行jar读取外部配置文件](#可执行jar读取外部配置文件)
            1. [Maven项目](#maven项目)
1. [NIO](#nio)
    1. [Buffer](#buffer)

**目录 end**|_2019-02-28 17:43_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Java IO
> - [个人代码:IO流的相关学习](https://github.com/Kuangcp/JavaBase/tree/master/src/main/java/com/io)

## Java IO 简史
> [BIO NIO AIO演变](http://www.cnblogs.com/itdragon/p/8337234.html)

### BIO
> Java1.0 到 Java1.3

同步阻塞式IO
但是能自己实现 伪异步IO

### NIO
> Java1.4 引入; 非阻塞式IO, 虽然官方名称为New IO, 民间称为No-blocking IO  

> [参考博客: NIO基础详解](http://cmsblogs.com/?p=2467)  

- 对于调用者来说是异步的, 但是实际上是使用的多路复用和一个线程进行轮询, 真的吗? 到底是不是异步的呢?

### AIO
> Java1.7 引入; 真正的异步非阻塞IO, NIO2.0

- 引入了新的异步通道的概念, 以及异步文件通道和异步套接字通道的实现

**************
## 字节流 
> OutputStream InputStream

ByteArrayOutputStream, FileOutputStream, FilterOutputStream, ObjectOutputStream, OutputStream, PipedOutputStream

> [参考博客:  FilterInputStream 与 装饰者模式](https://blog.csdn.net/zhao123h/article/details/52826682)

- FilterInputStream
    - DataInputStream
    - BufferedInputStream

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

***************

## 字符流
> Reader Writer

Reader类的核心就是read()这个方法，由于这里直接操作InputStream进行read()，因此可以读取出2个字节，java中每两个字节转成一个字符。
这就是Reader可以读取字符的原因，只不过是利用InputStream先将字节读取出来，再按照一定的编码方式转码.

***************

## 应用
### 文件IO
> [参考博客: Read a text file from Java classpath](https://www.java-success.com/read-a-text-file-from-java-classpath/)
> [Java：利用I/O流读取文件内容](https://blog.csdn.net/xuehyunyu/article/details/77873420)

#### 读取配置文件
- maven格式路径，会从resources下获取文件例如 /a.xml
- `InputStream is = this.getClass().getResourceAsStream(path);`
    - 读取properties文件 ：`new Properties().load(is);`
    - 按行读取文件 `BufferedReader bf = new BufferedReader(new InputStreamReader(is));`

**************
##### 可执行jar读取外部配置文件
```java
    Properties properties = new Properties();
    File file = new File("something.properties");
    FileInputStream fis = new FileInputStream(file);
    properties.load(fis);
    System.out.println(properties.getProperty("v"));
    fis.close();
``` 
- 只要配置文件和打包的jar同级即可

##### Maven项目
_读取resource目录下配置文件_
```java
    ClassLoader classLoader = MainConfig.class.getClassLoader();
    URL resource = classLoader.getResource("excel.main.yml");
    if(resource!=null){
        String path = resource.getPath();
    }
```
- 这样也可以, 但是会有诡异的问题, 打包后运行是正常的, idea中运行就不正常, `new File("src/main/resources/excel.main.yml")` 

### 网络IO
> [参考博客:网络IO之阻塞、非阻塞、同步、异步总结 ](https://www.cnblogs.com/Anker/p/3254269.html)

> [参考博客: Java IO: 网络](http://ifeve.com/java-io-network/)
当两个进程之间建立了网络连接之后，他们通信的方式如同操作文件一样：利用InputStream读取数据，利用OutputStream写入数据。换句话来说，Java网络API用来在不同进程之间建立网络连接，而Java IO则用来在建立了连接之后的进程之间交换数据。

**********************************
# NIO
> [Java NIO 系列教程](http://ifeve.com/java-nio-all/) 

## Buffer
> [Java NIO系列教程（三） Buffer](http://ifeve.com/buffers/)

- Buffer的基本用法: 使用Buffer读写数据一般遵循以下四个步骤：  
>   
    写入数据到Buffer  
    调用flip()方法   
    从Buffer中读取数据
    调用clear()方法或者compact()方法

- 当向buffer写入数据时，buffer会记录下写了多少数据。一旦要读取数据，需要通过flip()方法将Buffer从写模式切换到读模式。在读模式下，可以读取之前写入到buffer的所有数据。

- 一旦读完了所有的数据，就需要清空缓冲区，让它可以再次被写入。有两种方式能清空缓冲区：
    - 调用clear()或compact()方法。
- clear()方法会清空整个缓冲区。compact()方法只会清除已经读过的数据。任何未读的数据都被移到缓冲区的起始处，新写入的数据将放到缓冲区未读数据的后面。


