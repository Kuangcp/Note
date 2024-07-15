---
title: TomcatDesign
date: 2024-05-14 17:22:24
tags: 
categories: 
---

💠

- 1. [Tomcat Design](#tomcat-design)
    - 1.1. [架构设计](#架构设计)
    - 1.2. [线程池](#线程池)
    - 1.3. [连接器](#连接器)
        - 1.3.1. [NioEndpoint](#nioendpoint)

💠 2024-06-02 17:50:57
****************************************
# Tomcat Design
> [Github Tomcat](https://github.com/apache/tomcat)  
> [Compiling Tomcat Source Code By Maven](https://programmer.group/tomcat-source-analysis-i-compiling-tomcat-source-code.html) | [9.0.48 Source Repo](https://gitee.com/gin9/tomcat9-source)

> [♥Tomcat源码详解知识体系详解♥](https://pdai.tech/md/framework/tomcat/tomcat-overview.html)  
> [深入拆解Tomcat](https://time.geekbang.org/column/intro/100027701?tab=catalog)  

## 宏观架构


## 线程池
> [Doc: Tomcat Executor](https://tomcat.apache.org/tomcat-9.0-doc/config/executor.html)

> StandardThreadExecutor

Tomcat没有直接使用ThreadPoolExecutor而是扩展了 `threads.ThreadPoolExecutor`，一是可以隔离依赖，二是做定制化调整(核心改动为队列和提交任务，适配Tomcat生命周期管理)。

1. 执行逻辑调整 `StandardThreadExecutor#execute(java.lang.Runnable)` 当提交的任务触发拒绝策略时,尝试一次重新入队列。可能这段时间就有任务被消费了，可以提高一些服务可用性。

2. 队列自定义为 TaskQueue `public class TaskQueue extends LinkedBlockingQueue<Runnable>` 默认无界

Tomcat在EndPoint中通过acceptCount和maxConnections两个参数作用后，Tomcat默认的无界任务队列通常不会造成过多任务积压导致OOM。

其中maxConnections为Tomcat在任意时刻接收和处理的最大连接数，当Tomcat接收的连接数达到maxConnections时，Acceptor不会读取accept队列`对应于TCP连接中的全连接accept队列`中的连接；  
这时accept队列中的线程会一直阻塞着，直到Tomcat接收的连接数小于maxConnections（maxConnections默认为10000，如果设置为-1，则连接数不受限制）。  
acceptCount为accept队列的长度，当accept队列中连接的个数达到acceptCount时，即队列满，此时进来的请求一律被拒绝，默认值是100（基于Tomcat 8.5.43版本）。  

3. 生命周期管理 LifecycleMBeanBase 

任务结束时，上下文关闭时，停止所有线程，设置线程池参数，清理依赖资源。

************************

> StandardVirtualThreadExecutor 需Java 21，Tomcat9.0.76可用，最早可追溯到2022年随Loom项目开始筹备

内部实现为 VirtualThreadExecutor，并依据JreCompat做不同JDK版本的实现适配，最终通过 VirtualThreadBuilder 创建虚拟线程。


## 连接器
### NioEndpoint
NioEndpoint 要完成三件事情：接收连接、检测 I/O 事件以及处理请求，那么最核心的就是把这三件事情分开，用不同规模的线程数去处理.
比如用专门的线程组去跑 Acceptor，并且 Acceptor 的个数可以配置；
用专门的线程组去跑 Poller，Poller 的个数也可以配置；
最后具体任务的执行也由专门的线程池Executor来处理，也可以配置线程池的大小。
