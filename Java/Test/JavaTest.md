---
title: Java中的测试
date: 2018-11-21 10:56:52
tags: 
    - 测试
categories: 
    - Java
---

**目录 start**

1. [Java的测试](#java的测试)
    1. [断言](#断言)
        1. [正式代码](#正式代码)
        1. [测试代码](#测试代码)
    1. [单元测试](#单元测试)
1. [测试框架](#测试框架)
    1. [Junit](#junit)
        1. [Idea上Junit的使用](#idea上junit的使用)
    1. [TestNG](#testng)
    1. [Mock框架](#mock框架)
        1. [Mockito](#mockito)
        1. [EasyMock](#easymock)
    1. [DBUnit](#dbunit)
    1. [基准测试](#基准测试)
        1. [JMH](#jmh)
1. [感悟](#感悟)

**目录 end**|_2020-05-06 01:45_|
****************************************
# Java的测试
> [测试的基础理论](/Skills/Base/Test.md)

## 断言
### 正式代码
[参考: Java陷阱之assert关键字详解_java](https://yq.aliyun.com/ziliao/131292)
[java 中assert的使用](http://www.cnblogs.com/mylove7/articles/3457157.html)

首先可以用在单元测试代码中。junit侵入性是很强的，如果整个工程大量的代码都使用了junit，就难以去掉或者是选择另外一个框架。如果单元测试代码 很多，并且想复用这些单元测试案例，应该选择assert而不是junit，便于使用别的单元测试框架，比如TestNG。同理正式的功能代码根本就不应 该出现Junit，应该使用assert.

assert主要适合在基类，框架类，接口类，核心代码类，工具类中。换言之，当你的代码的调用者是另外一个程序员写得业务代码，或者是另外一个子系统时，就很有必要使用它。比如你做了一个快速排序的算法 

这种情况下，如果不检查传入参数的正确性，会抛出一个莫名其妙的空指针错误。你的调用者可能并不清楚你代码的细节，在一个系统的深处调试一个空指针错误是很浪费时间的。就应该直接明确的告诉你的调用者是传入的参数有问题。否则他会怀疑你的代码有BUG。使用assert可以避免两个程序员之间互相指责对方写的代码有问题。
assert适用那些你知道具体是什么错误，你和你的调用者已经约定应该由你的调用者去排除或检查的错误。你通过一个断言告诉你的调用者。assert不适用那些外部系统造成的错误，比如用户输入数据的错误，某个外部文件格式错误。这些错误不是你的调用者而是用户造成的，甚至于不属于异常，因为出现输入错误和文件格式错误是经常的，这些错误应该由业务代码去检查。

assert比较适合于被频繁调用的 基类，框架代码，工具类，核心代码，接口代码中，这正是它在运行时被去掉的原因。测试代码应该在测试阶段开启-ea参数，便于对系统深处的核心代码做仔细的测试。

Java较少使用assert的原因是Java有很完整的OO体系，强制类型转换出现得较少，所以不需要类似c那样需要频繁的检查指针的类型是否正确，指针是否为空。同时Java也很少直接管理内存或缓冲区，所以不需要频繁的检查传入的缓冲区是否为空或者是已经越界。

但使用好assert有助于提高框架代码的正确性和减少框架代码的使用者的调试时间。

assert要达到的目的是让程序员方便的发现自己的逻辑错误，并且不影响程序的效率。assert所发现的错误，是完全不应该出现的，是不能用异常代替的。异常，那是系统所允许的，或者是系统不可控的“错误”，它不是程序员的逻辑问题。

assert应该是开发阶段打开，而在发布后关闭。

### 测试代码
> 测试中必须要通过断言来得知测试是否通过, 


## 单元测试
> 单元测试(unit testing)，是指对软件中的最小可测试单元进行检查和验证。

- Assert.assertEquals(a,b) 断言两个对象是相等的
- assert(expression) 断言表达式为真

****************
# 测试框架
## Junit
> [Junit4官网](https://junit.org/junit4/)|[Junit5官网](https://junit.org/junit5/)| [如何上手Junit](/MyBlog/how-to-use-junit.md) | [如何上手Junit5](/MyBlog/how-to-use-junit5.md)

- Before Test 执行顺序：
    - Before在Test之前执行是毋庸置疑的，但是如果有多个Before的话，按定义的先后逆序执行，也就是说AB顺序定义，BA顺序执行
    - `注意` Before的执行顺序不是平常想的那样，如果你有一个共享的对象，需要在两个Before中完成初始化，是办不到的，必然空指针

- 遇到的问题:
    - 如果在加了Test注解的方法中像Main方法一样的去开多个子线程对象并运行起来,并不会得到想要的结果
    - 这几个线程都是开了就立马关闭了,而且也是正常的退出码 0 
    - 原因:

### Idea上Junit的使用
_可以使用TestMe插件_
- Ctrl Shift T 生成测试类 结合Mockit可以更好的模拟测试环境

## TestNG
> [Spring、Spring Boot和TestNG测试指南](https://github.com/chanjarster/spring-test-examples)

**************
## Mock框架
> mock 模拟 , 也就是说对需要测试的模块, 将该模块依赖的相关对象给修改成自己期望的行为方式(伪造一个假对象), 以移除依赖性, 从而针对性的测试该模块
> 但主要还是适用于单元测试，在集成测试，性能测试，自动化测试等其他测试领域使用并不多

> [JMockit官方文档](http://www.vogella.com/tutorials/Mockito/article.html#testing-with-mock-objects)
- [入门博客](http://blog.csdn.net/chjttony/article/details/17838693)
http://www.baeldung.com/mockito-void-methods
https://www.tutorialspoint.com/mockito/mockito_quick_guide.htm
http://static.javadoc.io/org.mockito/mockito-core/2.19.0/org/mockito/Mockito.html#1

### Mockito
> [Officail Site](http://site.mockito.org/) | [Github:mockito](https://github.com/mockito/mockito)
> [Mockito Tutorial](https://www.tutorialspoint.com/mockito/index.htm)
> [Unit tests with Mockito - Tutorial](http://www.vogella.com/tutorials/Mockito/article.html)

> [参考: TDD：什么是桩（stub）和模拟（mock）？](http://www.cnblogs.com/happyframework/p/3595547.html)
> [参考: mockito](http://www.testclass.net/mockito/)
> [mockito](http://static.javadoc.io/org.mockito/mockito-core/2.19.0/org/mockito/Mockito.html#1)

> 官网提示:
>1. Do not mock types you don’t own
>1. Don’t mock value objects
>1. Don’t mock everything
>1. Show love with your tests!

1. **常规使用** when(mock.get(anyInt())).thenReturn(null);
1. **对void方法的mock** doThrow(new RuntimeException()).when(mock).someVoidMethod(anyObject());
1. **使用规则去校验** verify(mock).someMethod(contains("foo"));

> 切忌 不可对非Mock对象使用 mock 的系列方法, 不然会报出南辕北辙的错误,这是首先要排查的一点

一般不用对 void 方法打桩, 事后 verify 就行  
测试代码针对 mock  对象的 void 方法调用本来就没有什么效果，所以一般也无须用 doNothing(), 况且 void 提供不了返回值作进一步 mock，只需要在事后用 verify() 进行验证一下。

### EasyMock
> [Github](https://github.com/easymock/easymock)  

************************

## DBUnit
> 基于Junit的一个数据库测试框架, 方便测试dao层
> [Github](https://github.com/sebastianbergmann/dbunit)`但是已经停止维护了`  

************************

## 基准测试
### JMH
> [详情](/Java/Test/JMH.md)

**********************
# 感悟
>1. 好的测试能大大节省时间, 坏的测试大量延误时间
>1. 应该在项目主体架构明确后, 才大量书写测试, 验证程序, 避免编写大量无用测试代码
>1. 单元测试有多难写, 你的代码就有多高的耦合度
