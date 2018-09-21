`目录 start`
 
- [并发](#并发)
    - [同步](#同步)
        - [锁](#锁)
    - [异步](#异步)
    - [线程和进程](#线程和进程)
    - [协程](#协程)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 并发
> 无关语言 涉及 同步 异步 线程 协程

## 同步
> [码农翻身:那些烦人的同步和互斥问题](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513371&idx=1&sn=c875f64af83306bffca8dd748f1462ff&chksm=80d679d8b7a1f0ce98a0e3a12409805757cd2e958586c54049121f961cf5b2d236530cd019c7&scene=21#wechat_redirect)

> 这种对`共享变量， 共享内存，共享资源`进行访问的程序片段叫做`临界区`， 代码在进入临界区之前一定要做好同步或者互斥的操作。  
- 例如在Java JDK中， 已经对线程的同步做了封装了， 对于生产者-消费者问题，可以直接使用BlockingQueue
   - 非常简单， 完全不用你去考虑这些 wait ,signal , full, empty

### 锁
> 锁是用来锁临界区资源的 , 而不是锁代码块, 锁函数. 那么在Java中: `synchronized` 锁住的是不同线程对同一个对象的访问 [知乎: 锁代码块和锁方法有啥区别啊？](https://www.zhihu.com/question/21295770)

**********************
## 异步

****************
## 线程和进程

*****************
## 协程

- [知乎:协程的讨论](https://www.zhihu.com/question/20511233)
- [协程以及Python实现](http://www.cnblogs.com/zingp/p/5911537.html)


