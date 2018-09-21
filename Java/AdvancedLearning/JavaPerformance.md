`目录 start`
 
- [Java的性能调优](#java的性能调优)
    - [JVM参数配置](#jvm参数配置)
    - [内存优化](#内存优化)
        - [处理内存泄露问题](#处理内存泄露问题)
        - [内存监测工具](#内存监测工具)
            - [jvisualvm](#jvisualvm)
            - [MAT](#mat)
- [记录](#记录)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Java的性能调优

## JVM参数配置

## 内存优化

- [Blog:java优化占用内存的方法(一)](http://blog.csdn.net/zheng0518/article/details/48182437)

- [GC 性能优化 专栏](https://blog.csdn.net/column/details/14851.html)

### 处理内存泄露问题
> [参考博客: java内存泄漏的定位与分析](https://blog.csdn.net/lc0817/article/details/67014499)

### 内存监测工具
#### jvisualvm
> [详情](/Java/AdvancedLearning/JDKAndJRE.md#jvisualvm)

#### MAT
> Memory Analyzer tool(MAT) [官网](http://www.eclipse.org/mat/)

> [参考博客: JAVA Shallow heap & Retained heap](http://www.cnblogs.com/lipeineng/p/5824799.html)

**************

# 记录

1. 表象
    - 使用Tomcat进行部署的, 然后机器上两个Tomcat都僵死了, 进程还在, 但已经不能提供服务了, 日志也停止了记录
1. 分析
    - 由于第一次遇到这种情况, 没有把现场保留, 直接就重启Tomcat了, 然后老大经过分析 一个堆栈快照文件(?), 发现有几个对象大量存在, 没有被GC
    - 然后启动本地Tomcat, 用 jvisualvm 进行调试, 发现有几个类的实例一直无法释放, 
    - 初步 分析这几个类的 **生命周期** , 以为是项目中使用的缓存, 没有好好清理, 又因为项目中缓存种类比较多, 调试分析了比较久
    - 最后是老大, 看到有个注册定时任务的地方, 当中的代码有比较严重的 隐患 
1. 原因
    - 在一个方法中调用了一个异步的定时任务, 并且声明了一个final 变量 给这个任务操作, 并且任务中的代码没有做好安全防护(try catch), 直接就一溜写下去
    - 这里就存在一个隐患了, 如果任务执行失败抛出异常 主线程并不能收到错误提示, 后面的资源回收就无法执行, 然后该任务在定时的报错, 自己和所持有的final 变量也无法释放
    - 主线程也不知情.......
1. 结论
    - final 使用时, 要考虑为什么要用, 
    - 如果是有了异步的行为, 就要将异步中的代码好好审视, 不能没有忽视代码所有可能的异常


