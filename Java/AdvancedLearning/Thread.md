`目录 start`
 
- [线程的基础学习](#线程的基础学习)
    - [TODO](#todo)
    - [基础](#基础)
    - [线程的意义](#线程的意义)
    - [线程的生命周期](#线程的生命周期)
        - [创建](#创建)
        - [控制](#控制)
        - [销毁](#销毁)
    - [线程的优先级](#线程的优先级)
    - [线程池](#线程池)

`目录 end` |_2018-08-10_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 线程的基础学习
> [个人相关代码](https://github.com/Kuangcp/JavaBase/tree/master/src/main/java/com/threads)

## TODO
- [ ] 线程的多种创建方式
- [ ] 线程池的创建方式
- [ ] 线程的状态转化

## 基础
- [码农翻身:我是一个线程](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=416915373&idx=1&sn=f80a13b099237534a3ef777d511d831a&scene=21#wechat_redirect) | [码农翻身:编程世界的那把锁](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513653&idx=1&sn=e30c18c0c1780fb3ef0cdb858ee5201e&chksm=80d67af6b7a1f3e059466302c2c04c14d097c1a5de01cf986df84d4677299542f12b974dfde3&scene=21#wechat_redirect) | [码农翻身:加锁还是不加锁，这是一个问题 ](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513692&idx=1&sn=ef2416a4bb96d64db77e32d5b4c7967e&chksm=80d67a9fb7a1f3898e513cc1d9e96841610bb84aed2dc24cab2d403e74e317e3c447e45e7611&scene=21#wechat_redirect)

## 线程的意义
## 线程的生命周期
> [参考博客](https://segmentfault.com/a/1190000005006079) | [Blog: 线程详解](http://www.cnblogs.com/riskyer/p/3263032.html) | [参考Java-learning仓库](https://github.com/brianway/java-learning)


### 创建
- 创建线程有三种创建方式： 继承，实现接口，实例化匿名内部方法。-> [示例代码](https://github.com/Kuangcp/JavaBase/blob/master/src/main/java/com/threads/HowToCreateThread.java)

> 查看Thread类源码 看看Thread类源码，捋清Runnable，target,run,start关系
- Runnable是一个接口
- target是Thread类中类型为Runnable，名为target的属性
- run是Thread类实现了Runnable的接口，重写的方法。
- start是启动线程的方法
- 在Thread类中，调用关系为：_start->start0->run->target.run_

_Thread类的run方法源码_
```java
    public void run() {
        if (target != null) {
            target.run();
        }
    }
```
_Thread类的target属性_
```java
    /* What will be run. */
    private Runnable target;
```
- target属性由 `private void init(ThreadGroup g, Runnable target, String name,long stackSize, AccessControlContext acc)`方法初始化。
    - init方法在Thread类的构造方法里被调用

### 控制
- 当调用 `Thread.join()` 时，_调用线程_将阻塞，直到_目标线程_完成为止。 

### 销毁

************************
## 线程的优先级
> 多个线程同时运行时,由线程调度器来决定哪些线程运行,哪些等待以及线程切换的时间点. 由于各个操作系统的线程调度器的实现各不相同, 所以依赖JDK来设置线程优先级策略是错误和非平台可移植性的.

***************************
## 线程池
> [线程池 BlockingQueue synchronized volatile](https://segmentfault.com/a/1190000012916473)
> [参考博客: Java(Android)线程池](http://www.trinea.cn/android/java-android-thread-pool/)
> [参考博客: Java ThreadPoolExecutor线程池使用的一个误区](http://codefine.site/2941.html)
> [参考博客: 聊聊并发（三）Java线程池的分析和使用](http://ifeve.com/java-threadpool/)
> [参考博客: 线程池](http://ifeve.com/thread-pools/)



