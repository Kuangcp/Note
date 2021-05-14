---
title: Web性能调优
date: 2018-12-13 16:02:57
tags: 
    - Performance
categories: 
---

**目录 start**

1. [APM](#apm)
1. [客户端](#客户端)
1. [服务端](#服务端)
    1. [压力测试准备](#压力测试准备)
    1. [性能基准 指标](#性能基准-指标)
        1. [性能监控平台](#性能监控平台)
    1. [测试工具](#测试工具)
        1. [Apache BenchMark](#apache-benchmark)
        1. [Jmeter](#jmeter)
        1. [wrk](#wrk)
        1. [hey](#hey)
        1. [ali](#ali)
        1. [Httperf](#httperf)
1. [数据库](#数据库)
        1. [MySQL](#mysql)
            1. [主从复制以及读写分离](#主从复制以及读写分离)

**目录 end**|_2020-10-18 13:59_|
****************************************
# 应用性能优化

> [参考: 怎样正确做 Web 应用的压力测试？](https://www.zhihu.com/question/19867883)  

> 负载测试、压力测试和性能测试
- 测试手段相似，但是目的不同，负载测试是为了发现系统性能问题，性能测试是为了获取性能指标，压力测试是高负载下的负载测试

对于web应用来说 从前端渲染速度，到页面大小，session存储效率，ajax性能，缓存命中率，数据库设计及访问速度 都要考虑。

# 客户端


# 服务端
`超出应用性能上限的表现`
1. 对于web后端来说就是请求过多, 数据库连接池不够用, 线程池大量等待的线程, 请求非常缓慢, 直接返回 5xx 错误码...

## 压力测试准备

1. 软硬件版本要和正式服务器保持一致。
2. 网络也需要和正式服务器保持一致。
3. 在测试高并发的场景下，也要修改linux的默认并发数。

## 性能基准 指标
> [参考: 系统吞吐量（TPS）、用户并发量、性能测试概念和公式](http://www.cnblogs.com/freeton/archive/2013/05/31/3109815.html)

> 外在指标
1.  吞吐量。每秒钟处理的请求数量；
2.  响应时间。应用处理一个请求的耗时；
3.  错误率。一批请求中出错的请求占比。

> 内在指标
1.  CPU。linux下使用top命令；
2.  内存。linux下使用top命令；
3.  服务器负载。linux下使用uptime命令,按照经验值，服务器负载应位于阀值的70%-80%；
4.  网络。主要包括网络流量和网络连接状态的监控,使用nmon工具；
5.  磁盘IO linux下可以用iostat监控磁盘状态。

### 性能监控平台
- [cat](https://github.com/dianping/cat)
- Prometheus

************************

## 测试工具
> [Github: HTTP(S) Benchmark Tools](https://github.com/denji/awesome-http-benchmark)

可以通过压力测试工具或者流量重放，复制 等方式模拟高并发业务场景

### Apache BenchMark
> 简称 ab [Doc](https://httpd.apache.org/docs/2.4/programs/ab.html) 

- 安装 `sudo apt install apache2-utils`| `sudo pacman -S apache-tools`
- 简单使用 `ab -c 并发数 -n 总请求数 URL`
    - 查看文档:`man ab` 或 `ab -h`


- 测试本机超过100连接报错 104: 
    - [Blog:解决问题](http://www.cnblogs.com/archoncap/p/5883723.html)

- `ab -c 5 -n 1000 -X 127.0.0.1:8888 -T application/json -p list.json -C 'JSESSIONID=xxx' URL` 使用 Cookie 使用代理 对json接口发起请求

### Jmeter
> 具有图形化客户端

- [jmeter](http://jmeter.apache.org/download_jmeter.cgi) `apache 下的开源压测工具`

### wrk
> [Github地址](https://github.com/wg/wrk)  
> [参考:  wrk 压力测试 http benchmark POST接口](http://www.cnblogs.com/felixzh/p/8400729.html)  
> [参考: 性能测试之－wrk(转)](http://www.cnblogs.com/rainy-shurun/p/5867946.html)  

1. 需要手动编译安装 make

### hey
> [Github](https://github.com/rakyll/hey)

### ali
> [ali](https://github.com/nakabonne/ali)`终端内图形化展示结果`

### Httperf
> [Github](https://github.com/httperf/httperf) `比 ab 更强大，能测试出 web 服务能承载的最大服务量及发现潜在问题；比如：内存使用、稳定性。最大优势：可以指定规律进行压力测试，模拟真实环境。`

************************

# 数据库

### MySQL
#### 主从复制以及读写分离
- [读写分离博客](http://www.cnblogs.com/luckcs/articles/2543607.html)
