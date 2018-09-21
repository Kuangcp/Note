`目录 start`
 
- [Java7](#java7)
    - [异常处理](#异常处理)
    - [TWR](#twr)

`目录 end` |_2018-08-26_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Java7
- [Java8](https://docs.oracle.com/javase/8/docs/api/)

_小特性_
- | Switch 支持 String
- | 二进制的实例化 原本是 `int x = Integer.parseInt("1010100", 2);`Java7之后`int x = 0b110110;`
- | 数字下划线 `10_0100__1000__0011`
- | 钻石语法: 泛型右部直接`<>`不用写类型变量


## 异常处理
- | 异常处理
    - 允许异常的`或`操作 `catch(IOException | NullPointException e)`
    - final关键字: `catch (final Exception e){throw e;}` 抛出后的是原异常类型的异常而不是Exception

## TWR
- | TWR(try with resources)
```java
    // 从URL下载文件, 其中的资源都会自动关闭
    // 但是要注意发生异常后,资源也不会自动关闭, 所以确保TWR生效,正确的用法是为各个资源声明独立变量.
    try(OutputStream out = new FileOutputStream(file);
        InputStream is = url.openStream()
    ){
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
- | 简化变参方法调用:
    - `HashMap<String, String>[] array = new HashMap<>[2];` 不允许创建已知类型的泛型数组
    - 只能这样写 `HashMap<String, String> array = new HashMap[2];`
        - 这样的编写也只是一个敷衍, 编译器会警告: 可以将array定义为HashMap<String, String>数组,但是又不能创建这个类型的实例. 所以这里只是将原始类型实例化了放进去.
    - 现在能够这样编写: `public static <T> Collection<T> doSomething(T... entries){}`

**********************
- [ ] 反射的简化和加强

