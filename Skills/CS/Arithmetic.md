---
title: 算法基础
date: 2018-11-21 10:56:52
tags: 
    - 基础
categories: 
    - 算法
---

**目录 start**
 
1. [算法](#算法)
    1. [时间复杂度](#时间复杂度)
    1. [匹配算法](#匹配算法)
    1. [排序算法](#排序算法)
    1. [安全](#安全)
        1. [密码学](#密码学)
            1. [Diffie-Hellman Key Exchange算法](#diffie-hellman-key-exchange算法)
1. [实际问题](#实际问题)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 算法

> [《编程之法》](https://github.com/julycoding/The-Art-Of-Programming-By-July)


分治算法
动态规划 最值 极值
不直接找问题, 而是根据你的输入, 和答案之前关系的规律

柯里化, continuation 高阶函数, 尾递归

## 时间复杂度
> [Java中的实践](http://www.baeldung.com/java-algorithm-complexity)

*********************
## 匹配算法
- [字符串相似度匹配](http://zjwyhll.blog.163.com/blog/static/75149781201281142630851/)

## 排序算法
> [参考博客: 九种排序算法的可视化及比较](https://zhuanlan.zhihu.com/p/34421623?group_id=955945213303250944)

*********
## 安全

### 密码学

#### Diffie-Hellman Key Exchange算法
> Whitfield Diffie 和 Martin Hellman ，他们于２０１５年获得了计算机科学领域的最高奖：图灵奖

![码农翻身](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/arithmetic/Diffie-HellmanKeyExchange.png)

`最后神奇的魔法发生了， 我们两个得到了同样的值 s = 10！`
-  这个s 的值只有我们两个才知道，  其实就是密钥了， 可以用来做加密解密了（ 当然，这只是一个例子，实际的密钥不会这么短）， 我们俩的通讯从此就安全了。
    -  “数学家小帅哥说了， 原因很简单，(gｘ mod p)ｙ mod p　和　(gｙ mod p)ｘ mod p　是相等的！ ”
    -  “那黑客不能从公开传输的 p = 17, g = 3, a = 6 , b = 12 推算出s = 10 吗？” 我问道。
    -  “当然不能， 不过前提是需要使用非常大的p , x, y,  这样以来，即使黑客动用地球上所有的计算资源， 也推算不出来。 ”

# 实际问题
例如存储一个部门关系, 上下级, 以及同级要有序, 并且, 这个关系树是能随意调整结构的, 每个节点和节点之间任意断开和连接

name/id, parent, index



