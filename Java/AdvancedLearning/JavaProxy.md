---
title: Java中的代理
date: 2019-01-27 21:06:14
tags: 
categories: 
    - Java
---

**目录 start**

1. [Java中的代理](#java中的代理)
    1. [静态代理](#静态代理)
    1. [动态代理](#动态代理)
        1. [JDK动态代理](#jdk动态代理)
        1. [cglib](#cglib)
        1. [ASM](#asm)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Java中的代理

> [参考: Java代理模式汇编](https://blog.csdn.net/JQ_AK47/article/details/85344634)

在某些情况下，一个客户不想或者不能直接引用一个对象，此时可以通过一个称之为“代理”的第三者来实现间接引用。代理对象可以在客户端和目标对象之间起到中介的作用，并且可以通过代理对象去掉客户不能看到的内容和服务或者添加客户需要的额外服务。

通过引入一个新的对象来实现对真实对象的操作或者将新的对象作为真实对象的一个替身，这种实现机制即为代理模式，通过引入代理对象来间接访问一个对象，这就是代理模式的模式动机。

> 代理模式(Proxy Pattern) ：给某一个对象提供一个代理，并由代理对象控制对原对象的引用。

按照代理类的创建时期，代理类可分为两种，即动态代理类和静态代理类. 
就是我们经常提到的静态代理和动态代理中主要用到的类。静态代理和动态代理的主要区别就是代理类创建的时间不同。

静态代理通常只代理一个类，动态代理是代理一个接口下的多个实现类。静态代理事先知道要代理的是什么，而动态代理不知道要代理什么东西，只有在运行时才知道。

## 静态代理
> 静态代理类：由程序员创建或由特定工具自动生成源代码，再对其编译。在程序运行前，代理类的.class文件就已经存在了。

```java
    //  接口以及实现类 (目标接口和目标对象)
    public interface HelloSerivice {
        public void say();
    }
    public class HelloSeriviceImpl implements HelloSerivice{
        @Override
        public void say() {
            System.out.println("hello world");
        }
    }
    
    // 代理类(同样实现目标接口), 并扩展了对应的方法
    public class HelloSeriviceProxy implements HelloSerivice{
        private HelloSerivice target;
        public HelloSeriviceProxy(HelloSerivice target) {
            this.target = target;
        }
        @Override
        public void say() {
            System.out.println("记录日志");
            target.say();
            System.out.println("回收资源");
        }
    }

    // 单元测试
    @Test
    public void testProxy(){
        //目标对象
        HelloSerivice target = new HelloSeriviceImpl();
        //代理对象
        HelloSeriviceProxy proxy = new HelloSeriviceProxy(target);
        proxy.say();
    }
```

这就是一个简单的静态的代理模式的实现。代理模式中的所有角色（代理对象、目标对象、目标对象的接口）等都是在编译期就确定好的。

- 静态代理的用途
    - 控制真实对象的访问权限：通过代理对象控制对真实对象的使用权限。
    - 避免创建大对象：通过使用一个代理小对象来代表一个真实的大对象，可以减少系统资源的消耗，对系统进行优化并提高运行速度。
    - 增强真实对象的功能：通过代理可以在调用真实对象的方法的前后增加额外功能。

************************

## 动态代理
> 动态代理类：在程序运行时，运用反射机制动态创建而成。动态代理中的代理类并不要求在编译期就确定，而是可以在运行期动态生成，从而实现对目标对象的代理功能。

> [参考: Java动态代理机制详解（JDK 和CGLIB，Javassist，ASM）](https://blog.csdn.net/luanlouis/article/details/24589193)

静态代理的缺点是想用这样的代理就必须要手动硬编码实现, 比较繁琐, 尤其是接口中的方法很多的时候, 动态代理就能解决这个问题  
在我们平时使用的框架中，像servlet的filter、包括spring提供的aop以及struts2的拦截器, mybatis分页插件，以及日志拦截、事务拦截、权限拦截这些几乎全部有动态代理的身影。

- 往往实现动态代理有两种方式:
    - JDK动态代理: `java.lang.reflect` 包中的`Proxy`类和`InvocationHandler`接口提供了生成动态代理类的能力。
    - Cglib: 是一个第三方代码生成类库，运行时在内存中动态生成一个子类对象从而实现对目标对象功能的扩展。

### JDK动态代理
> [Oracle api](https://docs.oracle.com/javase/8/docs/api/) 

jdk动态代理是由java内部的反射机制来实现的
JDK动态代理有一个限制，就是使用动态代理的对象必须实现一个或多个接口。因为JDK动态代理只能对接口产生代理，不能对类产生代理

### cglib
> `It is used by AOP, testing, data access frameworks to generate dynamic proxy objects and intercept field access.`

[Cglib (Byte Code Generation Library)](https://github.com/cglib/cglib) 

Cglib是针对类来实现代理的(所以无需声明接口)，他的原理是对代理的目标类生成一个子类，并覆盖其中方法实现增强，因为底层是基于创建被代理类的一个子类，所以它避免了JDK动态代理类的缺陷.  
Cglib包的底层是通过使用一个小而快的字节码处理框架ASM，来转换字节码并生成新的类。不鼓励直接使用ASM，因为它需要你对JVM内部结构包括class文件的格式和指令集都很熟悉。

这就不得不说到CgLib的特点：创建速度慢但执行速度快，而JDK的动态代理与其刚好相反：创建速度快但执行速度慢。
如果在程序运行时不断地使用CgLib去创建代理的话，系统运行的性能会大打折扣，所以建议一般在系统初始化时采用CgLib来创建代理，并放入Spring的ApplicationContext中。

### ASM
> [Official site](https://asm.ow2.io/) | [Github](https://github.com/llbit/ow2-asm)

> [使用 ASM 实现 Java 语言的“多重继承”](https://www.ibm.com/developerworks/cn/java/j-lo-asm/)
