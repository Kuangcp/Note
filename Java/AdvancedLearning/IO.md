`目录 start`
 
- [IO操作的学习](#io操作的学习)
    - [Java IO简史](#java-io简史)
        - [Java1.0到1.3 BIO](#java10到13-bio)
        - [Java1.4 NIO](#java14-nio)
        - [Java1.7 AIO](#java17-aio)
    - [关于普通IO的文件操作](#关于普通io的文件操作)
        - [读取配置文件](#读取配置文件)
            - [可执行jar读取外部配置文件](#可执行jar读取外部配置文件)
            - [Maven项目](#maven项目)
    - [NIO](#nio)
        - [Buffer](#buffer)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# IO操作的学习
> - [个人代码:IO流的相关学习](https://github.com/Kuangcp/JavaBase/tree/master/src/main/java/com/io)

## Java IO简史
> [BIO NIO AIO演变](http://www.cnblogs.com/itdragon/p/8337234.html)

### Java1.0到1.3 BIO
同步阻塞式IO
但是能自己实现 伪异步IO
### Java1.4 NIO
> 非阻塞式IO, 虽然官方名称为New IO, 民间称为No-blocking IO  

> [参考博客: NIO基础详解](http://cmsblogs.com/?p=2467)  

- 对于调用者来说是异步的, 但是实际上是使用的多路复用和一个线程进行轮询, 真的吗? 到底是不是异步的呢?

### Java1.7 AIO
> 真正的异步非阻塞IO, NIO2.0

- 引入了新的异步通道的概念, 以及异步文件通道和异步套接字通道的实现


## 关于普通IO的文件操作
### 读取配置文件
- maven格式路径，会从resources下获取文件例如 /a.xml
- `InputStream is = this.getClass().getResourceAsStream(path);`
    - 读取properties文件 ：`new Properties().load(is);`
    - 按行读取文件 `BufferedReader bf = new BufferedReader(new InputStreamReader(is));`

**************
#### 可执行jar读取外部配置文件
```java
    Properties properties = new Properties();
    File file = new File("something.properties");
    FileInputStream fis = new FileInputStream(file);
    properties.load(fis);
    System.out.println(properties.getProperty("v"));
    fis.close();
``` 
- 只要配置文件和打包的jar同级即可

#### Maven项目
_读取resource目录下配置文件_
```java
    ClassLoader classLoader = MainConfig.class.getClassLoader();
    URL resource = classLoader.getResource("excel.main.yml");
    if(resource!=null){
        String path = resource.getPath();
    }
```
- 这样也可以, 但是会有诡异的问题, 打包后运行是正常的, idea中运行就不正常, `new File("src/main/resources/excel.main.yml")` 

**********************************
## NIO
> [NIO](http://ifeve.com/overview/)
学习真是痛苦, 过程繁杂,又有各种并发 难以调试


### Buffer
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


