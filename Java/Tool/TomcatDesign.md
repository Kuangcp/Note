---
title: TomcatDesign
date: 2024-05-14 17:22:24
tags: 
categories: 
---

💠

- 1. [Tomcat Design](#tomcat-design)
    - 1.1. [线程池](#线程池)
    - 1.2. [连接器](#连接器)
        - 1.2.1. [NioEndpoint](#nioendpoint)

💠 2024-06-02 15:58:25
****************************************
# Tomcat Design

## 线程池
> [Doc: Tomcat Executor](https://tomcat.apache.org/tomcat-9.0-doc/config/executor.html)

Tomcat没有使用JDK的原生线程池，因为JUC原生线程池在提交任务时，当工作线程数达到核心线程数后，继续提交任务会尝试将任务放入阻塞队列中，只有当前运行线程数未达到最大设定值且在任务队列任务满后，才会继续创建新的工作线程来处理任务，因此JUC原生线程池无法满足Tomcat快速响应的诉求。

Tomcat为什么使用无界队列？

Tomcat在EndPoint中通过acceptCount和maxConnections两个参数来避免过多请求积压。
其中maxConnections为Tomcat在任意时刻接收和处理的最大连接数，当Tomcat接收的连接数达到maxConnections时，Acceptor不会读取accept队列中的连接；
这时accept队列中的线程会一直阻塞着，直到Tomcat接收的连接数小于maxConnections（maxConnections默认为10000，如果设置为-1，则连接数不受限制）。
acceptCount为accept队列的长度，当accept队列中连接的个数达到acceptCount时，即队列满，此时进来的请求一律被拒绝，默认值是100（基于Tomcat 8.5.43版本）。
因此，通过acceptCount和maxConnections两个参数作用后，Tomcat默认的无界任务队列通常不会造成OOM。



## 连接器
### NioEndpoint
NioEndpoint 要完成三件事情：接收连接、检测 I/O 事件以及处理请求，那么最核心的就是把这三件事情分开，用不同规模的线程数去处理.
比如用专门的线程组去跑 Acceptor，并且 Acceptor 的个数可以配置；
用专门的线程组去跑 Poller，Poller 的个数也可以配置；
最后具体任务的执行也由专门的线程池Executor来处理，也可以配置线程池的大小。
