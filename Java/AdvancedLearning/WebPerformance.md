`目录 start`
 
- [Java性能调优](#java性能调优)
- [Web性能](#web性能)
    - [测试工具](#测试工具)
        - [压力测试](#压力测试)
            - [ApacheBenchMark](#apachebenchmark)
            - [Jmeter](#jmeter)
            - [wrk](#wrk)
    - [数据库性能](#数据库性能)
        - [MySQL](#mysql)
            - [主从复制以及读写分离](#主从复制以及读写分离)

`目录 end` |_2018-08-05_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Java性能调优
> [查看详情>>](/Java/JavaPerformance.md)

# Web性能

## 性能基准
> [参考博客: 系统吞吐量（TPS）、用户并发量、性能测试概念和公式](http://www.cnblogs.com/freeton/archive/2013/05/31/3109815.html)

## 测试工具
### 压力测试

#### ApacheBenchMark
> 简称 ab

- 安装:`sudo apt install apache2-utils`
- 简单使用 `ab -c 并发数 -n 总请求数 URL`
    - 查看文档:`man ab` 或 `ab -h`
- [ab](https://httpd.apache.org/docs/2.4/programs/ab.html) `apt安装这个包即可apache2-utils` 

#### Jmeter
> 具有图形化客户端

- [jmeter](http://jmeter.apache.org/download_jmeter.cgi) `apache 下的开源压测工具`

#### wrk
> [Github地址](https://github.com/wg/wrk) 
> [参考博客:  wrk 压力测试 http benchmark POST接口](http://www.cnblogs.com/felixzh/p/8400729.html)
> [参考博客: 性能测试之－wrk(转)](http://www.cnblogs.com/rainy-shurun/p/5867946.html)

1. 需要手动编译安装 make

******************
## 数据库性能

### MySQL
#### 主从复制以及读写分离
- [读写分离博客](http://www.cnblogs.com/luckcs/articles/2543607.html)
