`目录 start`
 
- [函数式编程思想](#函数式编程思想)
        - [和其他思想的对比](#和其他思想的对比)
    - [函数式特性](#函数式特性)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 函数式编程思想
> [码农翻身:函数式编程圣经](http://mp.weixin.qq.com/s/0gErQ3tjDLZuD1bYOhi0mQ)

### 和其他思想的对比

- 面向对象的主要限制是不能在现有方法上增加额外的逻辑，函数式就能将方法（函数）作为参数传入进行扩展
    - 和AOP的区别：AOP是重型的基于动态代理类去封装扩展原方法

_关于递归_
- 非函数式语言中尽量是使用循环而不是递归, 函数式语言就要使用递归而不是循环 
    - 还有尾递归的概念,尾递归是将当前运行栈覆盖上一个运行栈而不是新增一个,减少栈的占用
    - [码农翻身:张大胖学递归](http://mp.weixin.qq.com/s/YpG9TvTCBus2FK6LbArvvw)
    - [深入了解尾递归](https://segmentfault.com/a/1190000007641519)
    - [面试题关于递归的层层优化](https://zhuanlan.zhihu.com/p/24283256)
    - [递归化循环](http://www.cnblogs.com/JeffreyZhao/archive/2009/04/01/tail-recursion-explanation.html)

## 函数式特性
- `map 映射`
- `filter 过滤`
