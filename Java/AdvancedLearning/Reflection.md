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
    1. [基础类](#基础类)
        1. [AccessibleObject](#accessibleobject)
        1. [Modifier](#modifier)
    1. [使用](#使用)
        1. [属性](#属性)
        1. [方法](#方法)
1. [反射的性能问题](#反射的性能问题)

**目录 end**|_2019-03-15 10:14_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 反射
> Reflection is powerful, but should not be used indiscriminately.  
> If it is possible to perform an operation without using reflection, then it is preferable to avoid using it. 

> [Java8 doc: reflection](https://docs.oracle.com/javase/tutorial/reflect/index.html)

> [ Java反射异常处理之InvocationTargetException ](https://blog.csdn.net/zhangzeyuaaa/article/details/39611467)

> [参考博客: java8--类加载机制与反射(java疯狂讲义3复习笔记)](https://www.cnblogs.com/lakeslove/p/5978382.html)
> [参考博客: Java8替代传统反射动态获取成员变量值的一个示例](https://segmentfault.com/a/1190000007492958)

> [参考博客: java反射的性能问题](http://www.cnblogs.com/zhishan/p/3195771.html)

## 基础类
> Field Method ...

### AccessibleObject
> The AccessibleObject class is the base class for Field, Method and Constructor objects. It provides the ability to flag a reflected object as suppressing default Java language access control checks when it is used.  
> AccessibleObject 类是 Field、Method 和 Constructor 对象的基类。它提供了将反射的对象标记为 具有在使用时禁止默认Java语言访问控制检查的能力。

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

### Modifier
> The Modifier class provides static methods and constants to decode class and member access modifiers.   
> [API: modifier](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Modifier.html)

`Java的访问权限信息啥的都是以2的N次幂来作为表示的 一共有12个常用修饰符 也就使用了12位来标记`
```java
    // 公共的, 意义一致
    PUBLIC           = 0x00000001;
    PRIVATE          = 0x00000002;
    PROTECTED        = 0x00000004;
    STATIC           = 0x00000008;
    FINAL            = 0x00000010;
    SYNCHRONIZED     = 0x00000020;
    VOLATILE         = 0x00000040;
    TRANSIENT        = 0x00000080;
    NATIVE           = 0x00000100;
    INTERFACE        = 0x00000200;
    ABSTRACT         = 0x00000400;
    STRICT           = 0x00000800;

    // 不公开, 意义依据方法或者属性不定
    BRIDGE    = 0x00000040;
    VARARGS   = 0x00000080;
    SYNTHETIC = 0x00001000;
    ANNOTATION  = 0x00002000;
    ENUM      = 0x00004000;
    MANDATED  = 0x00008000;
```
- 判断属性是否被 final 修饰 `(field.getModifiers() & Modifier.FINAL) != 0`
- 移除 final 修饰符 `field.getModifiers() & ~Modifier.FINAL`

`去除属性上的final修饰符`
```java
    Field modifiersField = Field.class.getDeclaredField("modifiers");
    modifiersField.setAccessible(true);
    modifiersField.setInt(field, field.getModifiers() & ~Modifier.FINAL);
```

*****************************
## 使用
> [Github: 反射获取属性](https://github.com/Kuangcp/JavaBase/blob/master/java-class/src/test/java/com/github/kuangcp/reflects/ObtainFieldsTest.java)

### 属性
> _获取以及修改属性的值_
```java
    // 1. 通过描述对象获取值, 但是该属性要有对应的正确的 set get 方法
    PropertyDescriptor propertyDescriptor = new PropertyDescriptor("age", A.class);
    Method method = propertyDescriptor.getReadMethod();
    Object result = method.invoke(object);

    // 2. 直接通过Field对象
    // set
    A a = new A();
    Field field = a.getClass().getDeclaredField("age");
    field.setAccessible(true);
    field.set(a, 1);
    // get
    field.setAccessible(true);
    System.out.println(field.get(a));
```

> [doc: java8](https://docs.oracle.com/javase/8/docs/api/) `Field.set()`的文档

被final修饰过的变量，只是说栈存储的地址不能再改变，但是却没有说地址指向的内容不能改变，所以反射可以破final，因为它修改该了以前地址的具体内容，但是没有改地址的信息。

### 方法

**********************

# 反射的性能问题
> [参考博客: java反射的性能问题 ](http://www.cnblogs.com/zhishan/p/3195771.html)

