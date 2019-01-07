---
title: Java反射
date: 2018-11-21 10:56:52
tags: 
    - Reflect
categories: 
    - Java
---

**目录 start**
 
1. [反射](#反射)
    1. [获取属性](#获取属性)
    1. [获得方法](#获得方法)
        1. [性能问题](#性能问题)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 反射
> Reflection is powerful, but should not be used indiscriminately.  
> If it is possible to perform an operation without using reflection, then it is preferable to avoid using it. 

> [Java8 doc: reflection](https://docs.oracle.com/javase/tutorial/reflect/index.html)

> [ Java反射异常处理之InvocationTargetException ](https://blog.csdn.net/zhangzeyuaaa/article/details/39611467)

> [参考博客: java8--类加载机制与反射(java疯狂讲义3复习笔记)](https://www.cnblogs.com/lakeslove/p/5978382.html)
> [参考博客: Java8替代传统反射动态获取成员变量值的一个示例](https://segmentfault.com/a/1190000007492958)

> [参考博客: java反射的性能问题](http://www.cnblogs.com/zhishan/p/3195771.html)

## AccessibleObject
> AccessibleObject 类是 Field、Method 和 Constructor 对象的基类。它提供了将反射的对象标记为在使用时取消默认 Java 语言访问控制检查的能力。

对于公共成员、默认（打包）访问成员、受保护成员和私有成员，在分别使用 Field、Method 或 Constructor 对象来设置或获得字段、调用方法，或者创建和初始化类的新实例的时候，会执行访问检查。  
在反射对象中设置 accessible 标志允许具有足够特权的复杂应用程序（比如 Java Object Serialization 或其他持久性机制）以某种通常禁止使用的方式来操作对象。  

> 将此对象的 accessible 标志设置为指示的布尔值。值为 true 则指示反射的对象在使用时应该取消 Java 语言访问检查。值为 false 则指示反射的对象应该实施 Java 语言访问检查。  
> 此标志不会告诉您java访问修饰符是否可以访问该字段，它会告诉您当前是否忽略这些修饰符。  

实际上setAccessible是启用和禁用访问安全检查的开关,并不是为true就能访问为false就不能访问，一般情况下，我们并不能对类的私有字段进行操作，利用反射也不例外，  
但有的时候，例如要序列化的时候，我们又必须有能力去处理这些字段，这时候，我们就需要调用`AccessibleObject`上的`setAccessible(true)`方法来允许这种访问，  
而由于反射类中的Field，Method和Constructor继承自AccessibleObject，因此，通过在这些类上调用setAccessible()方法，我们可以实现对这些字段的操作。  
但有的时候这将会成为一个安全隐患，为此，我们可以启用java.security.manager来判断程序是否具有调用setAccessible()的权限。  

> 默认情况下，`内核API`和`扩展目录`的代码具有该权限，而`类路径`或`通过URLClassLoader加载`的应用程序不拥有此权限。

- [ ] 仍然存疑, 什么情况下才是 默认可访问的

*****************************

## 获取属性
> _通过属性名得到对象属性的值_
```java
    // 1. 通过描述对象获取值, 但是该属性要有对应的正确的 set get 方法
    PropertyDescriptor propertyDescriptor = new PropertyDescriptor("age", A.class);
    Method method = propertyDescriptor.getReadMethod();
    Object result = method.invoke(object);

    // 2. 直接通过Field对象
    // set
    A a = new A();
    Field field = a.getClass().getDeclaredField("x");
    field.setAccessible(true);
    field.set(a, 1);
    // get
    Field f = a.getClass().getDeclaredField("x");
    f.setAccessible(true);
    System.out.println(f.get(a));
```

## 获取方法

### 性能问题
> [参考博客: java反射的性能问题 ](http://www.cnblogs.com/zhishan/p/3195771.html)

