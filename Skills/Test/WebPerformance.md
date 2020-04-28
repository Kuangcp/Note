---
title: Web性能调优
date: 2018-12-13 16:02:57
tags: 
    - Performance
categories: 
---

**目录 start**

1. [Web性能](#web性能)
    1. [性能基准](#性能基准)
    1. [测试工具](#测试工具)
        1. [Apache BenchMark](#apache-benchmark)
        1. [Jmeter](#jmeter)
        1. [wrk](#wrk)
        1. [hey](#hey)
    1. [数据库性能](#数据库性能)
        1. [MySQL](#mysql)
            1. [主从复制以及读写分离](#主从复制以及读写分离)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Web性能

## 性能基准
> [参考: 系统吞吐量（TPS）、用户并发量、性能测试概念和公式](http://www.cnblogs.com/freeton/archive/2013/05/31/3109815.html)

`超出应用性能上限的表现`
1. 对于web后端来说就是请求过多, 数据库连接池不够用, 线程池大量等待的线程, 请求非常缓慢, 直接返回 5xx 错误码...

************************

## 测试工具
> [Github: HTTP(S) Benchmark Tools](https://github.com/denji/awesome-http-benchmark)

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

************************

## 数据库性能

### MySQL
#### 主从复制以及读写分离
- [读写分离博客](http://www.cnblogs.com/luckcs/articles/2543607.html)
