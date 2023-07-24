---
title: Java中的IO
date: 2018-11-21 10:56:52
tags: 
    - IO
categories: 
    - Java
---

**目录 start**

1. [Java中的IO](#java中的io)
    1. [IO 简史](#io-简史)
        1. [BIO](#bio)
        1. [NIO](#nio)
        1. [AIO](#aio)
    1. [字节流](#字节流)
    1. [字符流](#字符流)
    1. [应用](#应用)
        1. [文件IO](#文件io)
            1. [读取配置文件](#读取配置文件)
                1. [可执行jar读取外部配置文件](#可执行jar读取外部配置文件)
                1. [Maven项目](#maven项目)
        1. [网络IO](#网络io)
1. [NIO](#nio)
    1. [Buffer](#buffer)

**目录 end**|_2023-07-24 18:06_|
****************************************
# Java中的IO
> [Note：操作系统中的IO模型](/Skills/CS/IO.md)  
> [Oracle Doc: Java I/O, NIO, and NIO.2](https://docs.oracle.com/javase/8/docs/technotes/guides/io/index.html)  

> [Github: IO demo](https://github.com/Kuangcp/JavaBase/tree/io) 

> [参考: 五种IO模型](https://www.jianshu.com/p/6a6845464770)  

## IO 简史
> [BIO NIO AIO演变](http://www.cnblogs.com/itdragon/p/8337234.html)

### BIO
> Java1.0 到 Java1.3

同步阻塞式IO 但是能基于 BIO 手动实现 伪异步IO

### NIO
> Java1.4 引入; 同步非阻塞式IO, 虽然官方名称为 New IO, 民间称为 `No-blocking IO`

这个NIO和是基于操作系统NIO相关函数实现的, 所以称为`No-blocking IO`
```java
    //  进入Selector.open(); 方法可以看到
    public static Selector open() throws IOException {
        return SelectorProvider.provider().openSelector();
    }
    // 进入 provider() 方法
    // 然后看到 sun.nio.ch.DefaultSelectorProvider.create();
    public static SelectorProvider create() {
        String var0 = (String)AccessController.doPrivileged(new GetPropertyAction("os.name"));
        if (var0.equals("SunOS")) {
            return createProvider("sun.nio.ch.DevPollSelectorProvider");
        } else {
            return (SelectorProvider)(var0.equals("Linux") ? 
                createProvider("sun.nio.ch.EPollSelectorProvider") : new PollSelectorProvider());
        }
    }
```

在Linux上使用的是 epoll, Windows 则是 poll 

实现模型和操作系统的NIO也是一致的, 一个 Selector 注册多个 SelectionKey, SelectionKey 具有多个状态并且和Channel绑定

| 事件名 | 对应值 |
|:----|:----|
| 服务端接收客户端连接事件 	| SelectionKey.OP_ACCEPT(16)
| 客户端连接服务端事件 	   | SelectionKey.OP_CONNECT(8)
| 读事件 	             | SelectionKey.OP_READ(1)
| 写事件 	             | SelectionKey.OP_WRITE(4)

************************

类似的思想还有定时器   
- 需求: 实现一个 10s 后调用一个方法的定时器  
- 简单: `Thread.sleep(10000);` 但是这种方式下, 定时器和任务是一一对应的  
- 复用模式: 一个线程睡眠很短的时间, 不停去检查 方法的时间到了没有, 到了就执行, 这样就只要一个线程就能处理多个任务  

### AIO
> Java1.7 引入; 真正的异步非阻塞IO

- 引入了新的异步通道的概念, 以及异步文件通道和异步套接字通道的实现

Asynchronous*的类 读写操作都被Future封装了，均交给操作系统异步完成，需要应用系统手动处理

**************
## 字节流 
> OutputStream InputStream

ByteArrayOutputStream, FileOutputStream, FilterOutputStream, ObjectOutputStream, OutputStream, PipedOutputStream

> [参考:  FilterInputStream 与 装饰器模式](https://blog.csdn.net/zhao123h/article/details/52826682)

- FilterInputStream
    - DataInputStream
    - BufferedInputStream

***************

## 字符流
> Reader Writer

Reader类的核心就是read()这个方法，由于这里直接操作InputStream进行read()，因此可以读取出2个字节，java中每两个字节转成一个字符。
这就是Reader可以读取字符的原因，只不过是利用InputStream先将字节读取出来，再按照一定的编码方式转码.

> Java8 快速读取字符流
```java
    String text = new BufferedReader(
        new InputStreamReader(((Response.InputStreamBody) response.body).inputStream, StandardCharsets.UTF_8))
        .lines()
        .collect(Collectors.joining("\n"));
```
***************

## 应用
### 文件IO
> [参考: Read a text file from Java classpath](https://www.java-success.com/read-a-text-file-from-java-classpath/)  
> [Java：利用I/O流读取文件内容](https://blog.csdn.net/xuehyunyu/article/details/77873420)

#### 读取配置文件
- maven项目，从resources下获取文件 例如 /a.xml `InputStream is = this.getClass().getResourceAsStream("/a.xml");`
    1. 读取properties文件 ：`new Properties().load(is);`
    1. 按行读取文件 `BufferedReader bf = new BufferedReader(new InputStreamReader(is));`

************************

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

> [参考: Java IO: 网络](http://ifeve.com/java-io-network/)
当两个进程之间建立了网络连接之后，他们通信的方式如同操作文件一样：利用InputStream读取数据，利用OutputStream写入数据。换句话来说，Java网络API用来在不同进程之间建立网络连接，而Java IO则用来在建立了连接之后的进程之间交换数据。

**********************************
# NIO
> [Java NIO 系列教程](http://ifeve.com/java-nio-all/) 

## Buffer
> [Java NIO系列教程（三） Buffer](http://ifeve.com/buffers/)

- Buffer的基本用法: 使用Buffer读写数据一般遵循以下四个步骤：  
    1. 写入数据到Buffer  
    1. 调用flip()方法   
    1. 从Buffer中读取数据
    1. 调用clear()方法或者compact()方法

- 当向buffer写入数据时，buffer会记录下写了多少数据。一旦要读取数据，需要通过flip()方法将Buffer从写模式切换到读模式。在读模式下，可以读取之前写入到buffer的所有数据。

- 一旦读完了所有的数据，就需要清空缓冲区，让它可以再次被写入。有两种方式能清空缓冲区：
    - 调用clear()或compact()方法。
- clear()方法会清空整个缓冲区。compact()方法只会清除已经读过的数据。任何未读的数据都被移到缓冲区的起始处，新写入的数据将放到缓冲区未读数据的后面。


