---
title: Java7
date: 2018-11-21 10:56:52
tags: 
categories: 
    - Java
---

**目录 start**

1. [Java7](#java7)
    1. [异常处理](#异常处理)
    1. [TWR](#twr)
    1. [NIO 2.0](#nio-20)
        1. [Path](#path)
        1. [文件系统 I/O](#文件系统-io)
        1. [异步 I/O](#异步-io)

**目录 end**|_2020-07-05 16:28_|
****************************************

> [参考: JDK各个版本比较 JDK5~JDK10](https://blog.csdn.net/tieselingzhi/article/details/79764048s)

# Java7
- [Official: Java 7 API](https://docs.oracle.com/javase/7/docs/api/)

_小特性_
- Switch 支持 String
    - Java6之前case语句中的常亮只支持 byte, char, short, int或枚举变量,Java7中增加了String
- 二进制数值的转换
    - 原本是 `int x = Integer.parseInt("1010100", 2);`Java7之后`int x = 0b110110;`
- 数字下划线 `10_0100__1000__0011`
- 钻石语法: 泛型右部直接`<>`不用写类型变量

## 异常处理
- 异常处理
    - 允许异常的`或`操作 `catch(IOException | NullPointException e)`
    - final关键字: `catch (final Exception e){throw e;}` 抛出后的是原异常类型的异常而不是Exception

## TWR
- TWR(try with resources)
```java
    // 从URL下载文件, 其中的资源都会自动关闭
    // 但是要注意发生异常后,资源也不会自动关闭, 所以确保TWR生效,正确的用法是为各个资源声明独立变量.
    try(OutputStream out = new FileOutputStream(file);
        InputStream is = url.openStream()){
            byte[] buf = new byte[1024];
            int len; 
            while ((len = is.read(buf)) > 0){
                out.write(buf, 0, len);
            }
    }
```
- 另一个好处就是改善了错误跟踪的能力, 能够更准确地跟踪堆栈中的异常, 在Java7之前,处理资源时抛出的异常经常会被覆盖,TWR也可能会出现这种情况.
```java
    try((InputStream in = getNullStream())){
        in.available();
    }
```
- 在这种改进后的跟踪堆栈中能看到提示, 其中的NullPointException是能够抛出来看到的.没有被隐藏

> 目前TWR特性依靠一个接口来实现 AutoCloseable. TWR的try从句中出现的资源类都必须实现这个接口. Java7中大部分资源类都修改过  
> 但不是所有的资源类都采用了这项技术, JDBC是已经具备了这个特性. _官方提倡尽量采用TWR替代原有的方式_  

*********************
> 简化变参方法调用
```java
    // 不允许创建已知类型的泛型数组, 编译报错
    HashMap<String, String>[] array = new HashMap<>[2];

    // 只能这样写  这样的编写也只是权宜之计, 编译器会警告: 
    // 可以将array定义为HashMap<String, String>数组,但是又不能创建这个类型的实例  所以这里只是将原始类型实例化了放进去.
    HashMap<String, String>[] array = new HashMap[2];

    // 现在能够这样编写:
    public static <T> Collection<T> doSomething(T... entries){}
```
## NIO 2.0 
### Path
```java
    // 创建路径
    Path list = Paths.get("xmlStudy");
    // 获取文件名
    System.out.println(list.getFileName());
    // 获取名称元素数量
    System.out.println(list.getNameCount());

    File file = new File("test.xml");
    // 将旧API的File转换成新的Path
    Path path = file.toPath();
    // 将Path转换成File
    File fiel2 = path.toFile();
```

### 文件系统 I/O
```java
    // 创建文件
    Path path = Paths.get("test2.xml");
    Path file = Files.createFile(path);
    // 删除文件
    Files.delete(path);

    // 复制
    Path source = Paths.get("test2.xml");
    Path path = Paths.get("src/test2.xml");
    Files.copy(source, path);
    // 移动
    Path path = Paths.get("test2.xml");
    Path source = Paths.get("src/test2.xml");
    Files.move(source, path);
```

-	读写数据 (可指定文件的打开方式, WRITE, READ, APPEND (StandardOpenOption.WRITE))
```java
    Path path = Paths.get("test.txt");
    // 打开一个带缓冲区的读取器
    try (BufferedReader reader = Files.newBufferedReader(path, StandardCharsets.UTF_8)) {
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
    }

    // 打开带有一个缓冲区的写入器
    try (BufferedWriter writer = Files.newBufferedWriter(path)) {
        writer.write("测试");
    }
    
    // java7简化后的读取全部行和字节
    List<String> lines = Files.readAllLines(path);
    byte[] bytes = Files.readAllBytes(path);
    System.out.println(lines);
```

### 异步 I/O
- 将来式
	
```java
    Path path = Paths.get("test.txt");
    // 异步打开文件
    AsynchronousFileChannel channel = AsynchronousFileChannel.open(path);
    // 读取100000字节
    ByteBuffer buffer = ByteBuffer.allocate(100_000);
    Future<Integer> result = channel.read(buffer, 0);
    while (!result.isDone()) {
        System.out.println("其他事");
    }
    // 获取结果
    Integer bytesRead = result.get();
    System.out.println(bytesRead);
```
- 回调式

```java
    Path path = Paths.get("test.txt");
    // 异步打开文件
    AsynchronousFileChannel channel = AsynchronousFileChannel.open(path);
    // 读取100000字节
    ByteBuffer buffer = ByteBuffer.allocate(100_000);
    
    channel.read(buffer, 0, buffer, new CompletionHandler<Integer, ByteBuffer>() {
        // 读取调取完成时的回调方法
        @Override
        public void completed(Integer result, ByteBuffer attachment) {
            System.out.println(result);
        }
        @Override
        public void failed(Throwable exc, ByteBuffer attachment) {
            System.out.println(exc.getMessage());
        }
    });
```

