# Netty Design
> [Netty序章之BIO NIO AIO演变](https://segmentfault.com/a/1190000012976683)

> 源码解读
> [官方Demo](https://github.com/netty/netty/tree/4.1/example/src/main/java/io/netty/example)
> [Netty实战配套源码](https://github.com/ReactivePlatform/netty-in-action-cn)
> [Netty权威指南2 源码](https://github.com/Kuangcp/NettyBook2)

## 线程模型
[主次Reactor多线程模型](/Skills/CS/IO.md#reactor)

Netty
![](/Java/Ecosystem/Netty/img/001-reactor-netty.drawio.svg)

## 内存设计

> 直接内存

- -Dio.netty.noPreferDirect 是否运行通过底层api直接访问直接内存，默认：允许
- -Dio.netty.noUnsafe 是否允许使用sun.misc.Unsafe，默认：允许
- -Dio.netty.maxDirectMemory 设置最大值

************************
