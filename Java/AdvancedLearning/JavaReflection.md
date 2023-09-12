---
title: Java反射原理以及使用
date: 2018-11-21 10:56:52
tags: 
    - Reflect
categories: 
    - Java
---

**目录 start**

1. [反射](#反射)
1. [概念](#概念)
1. [实现原理](#实现原理)
    1. [Inflation](#inflation)
1. [基础类](#基础类)
    1. [AccessibleObject](#accessibleobject)
    1. [Annotation](#annotation)
    1. [Class](#class)
    1. [Field](#field)
    1. [Method](#method)
    1. [Constructor](#constructor)
    1. [Modifier](#modifier)
1. [使用](#使用)
    1. [获取Class对象的方式](#获取class对象的方式)
    1. [反射的基本使用](#反射的基本使用)
        1. [操作构造方法](#操作构造方法)
        1. [操作类中方法](#操作类中方法)
        1. [操作类的成员属性](#操作类的成员属性)
        1. [操作注解](#操作注解)
1. [反射的性能问题](#反射的性能问题)

**目录 end**|_2023-08-25 15:50_|
****************************************
# 反射
> Reflection is powerful, but should not be used indiscriminately.  
> If it is possible to perform an operation without using reflection, then it is preferable to avoid using it. 

> [Offcial Tutorials: reflection](https://docs.oracle.com/javase/tutorial/reflect/index.html)

> [ Java反射异常处理之InvocationTargetException ](https://blog.csdn.net/zhangzeyuaaa/article/details/39611467)

> [参考: java8--类加载机制与反射(java疯狂讲义3复习笔记)](https://www.cnblogs.com/lakeslove/p/5978382.html)
> [参考: Java8替代传统反射动态获取成员变量值的一个示例](https://segmentfault.com/a/1190000007492958)

> [参考: java反射的性能问题](http://www.cnblogs.com/zhishan/p/3195771.html)  

# 概念

在运行时 反射使程序能够在运行时探知类的结构信息:构造器,方法,字段... 并且依赖这些结构信息完成相应的操作,比如创建对象,方法调用,字段赋值...  
这种动态获取的信息以及动态调用对象的方法的功能称为java语言的反射机制。

# 实现原理
> [参考: RednaxelaFX 关于反射调用方法的一个log ](https://www.iteye.com/blog/rednaxelafx-548536)  
> [Java 虚拟机：JVM是如何实现反射的？](https://cloud.tencent.com/developer/article/1786456)  

## Inflation
考虑到许多反射调用仅会执行一次，Java 虚拟机设置了一个阈值 15（可以通过 -Dsun.reflect.inflationThreshold= 来调整），当某个反射调用的调用次数在 15 之下时，采用本地实现；当达到 15 时，便开始动态生成字节码，并将委派实现的委派对象切换至动态实现，这个过程我们称之为 Inflation。


https://www.jianshu.com/p/20b7ab284c0a
https://cloud.tencent.com/developer/news/663586

************************

# 基础类
> Java 反射的实现类

## AccessibleObject
> The AccessibleObject class is the base class for Field, Method and Constructor objects. It provides the ability to flag a reflected object as suppressing default Java language access control checks when it is used.  

> AccessibleObject 类是 Field、Method 和 Constructor 对象的基类。它提供了将反射的对象标记为 具有在使用时禁止Java语言的`默认访问控制检查`的能力。

对于公共成员、默认（打包）访问成员、受保护成员和私有成员，在分别使用 Field、Method 或 Constructor 对象来设置或获得字段、调用方法，或者创建和初始化类的新实例的时候，会执行访问检查。  
在反射对象中设置 accessible 标志允许具有足够特权的复杂应用程序（比如 Java Object Serialization 或其他持久性机制）以某种通常禁止使用的方式来操作对象。  

> 将此对象的 accessible 标志设置为指示的布尔值。  
> true 表示反射的对象在使用时应该取消 Java 语言访问检查， 反之则要进行。   
> 此标志不会告诉您java访问修饰符是否可以访问该字段，它会告诉您当前是否忽略这些修饰符。  

实际上setAccessible是启用和禁用访问安全检查的开关,并不是为true就能访问，为false就不能访问，一般情况下，我们并不能对类的私有字段进行操作，利用反射也不例外，  
但有的时候，例如要序列化的时候，我们又必须有能力去处理这些字段，这时候，我们就需要调用`AccessibleObject`上的`setAccessible(true)`方法来允许这种访问，  
而由于反射类中的Field，Method和Constructor继承自AccessibleObject，因此，通过在这些类上调用setAccessible()方法，我们可以实现对这些字段的操作。  
但有的时候这将会成为一个安全隐患，为此，我们可以启用java.security.manager来判断程序是否具有调用setAccessible()的权限。  

> 默认情况下，`内核API`和`扩展目录`的代码具有该权限，而`类路径`或`通过URLClassLoader加载`的应用程序不拥有此权限。

- [ ] 仍然存疑, 什么情况下才是 默认可访问的。什么情况下 true 不能访问

## Annotation
## Class
## Field
## Method
## Constructor

## Modifier
> The Modifier class provides static methods and constants to decode class and member access modifiers.   
> [API: modifier](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/reflect/Modifier.html)

`Java的访问权限信息是以2的N次幂也就是bitmap的方式进行存储 一共有12个常用修饰符 也就使用了12位来标记`
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

    // 不公开, 意义依据方法或者属性而定， 最大到16位
    BRIDGE      = 0x00000040;
    VARARGS     = 0x00000080;
    SYNTHETIC   = 0x00001000;
    ANNOTATION  = 0x00002000;
    ENUM        = 0x00004000;
    MANDATED    = 0x00008000;
```

- 判断属性是否被 final 修饰 `Modifier.isFinal(field.getModifiers())`
- 移除 final 修饰符 `field.getModifiers() & ~Modifier.FINAL`

```java
    Field field = ReflectTargetObject.class.getDeclaredField("staticFinalString");
    Field modifiersField = Field.class.getDeclaredField("modifiers");
    modifiersField.setAccessible(true);
    modifiersField.setInt(field, field.getModifiers() & ~Modifier.FINAL);
```

*****************************

# 使用
> 具有的功能
1. 在运行时获取任意一个类所具有的成员变量和方法以及泛型类型；
1. 在运行时构造任意一个类的对象；
1. 在运行时调用任意一个对象的方法；
1. 生成动态代理。

> 泛型擦除的存在, 但是泛型如果被用来进行声明, 类上,字段上,方法参数和方法返回值上,这些属于类的结构信息其实是会被编译进Class文件中的;  
> 而泛型如果被用来使用,常见的方法体中带泛型的局部变量,其类型信息不会被编译进Class文件中。  
> 前者因为存在于Class文件中，所以运行时通过反射还是能够获得其类型信息的;

## 获取Class对象的方式
> 所有的反射操作的入口都是从Class对象开始的, 获取Class对象有多种方式

1. 通过类加载器加载class文件
    - `Class<?> clazz = Thread.currentThread().getContextClassLoader().loadClass("com.takumiCX.reflect.ClassTest");`
1. 通过静态方法 Class.forName() 获取,需要传入类的全限定名字符串作参数
    - `Class<?> clazz = Class.forName("com.takumiCX.reflect.ClassTest");`
1. 通过 类.class 获得类的Class对象
    - `Class<ClassTest> clazz = ClassTest.class;`

除了获得的Class对象的泛型类型信息不一样外,还有一个不同点值得注意。只有 forName() 方式 在获得class对象的同时会引起类的初始化

************************

## 反射的基本使用

### 操作构造方法 
使用newInstance()操作无参构造方法  
> 使用Class类中的newInstance()方法进行实例化操作， 但该方法必须要求类有无参构造方法

使用Class类中的getConstructors()获取所有构造方法
```java
    Class<?> cls = Class.forName("first.Book");
    Constructor<?>[] constructors = cls.getConstructors();
```

使用Class类中的getConstructor获取指定参数类型的构造方法
```java
  Class<?> cls = Class.forName("first.Book");
  Constructor constructor = cls.getConstructor(String.class, String.class);
  // 实例化对象
  Book book = (Book) constructor.newInstance("java", "123");
  System.out.println(book);
```

### 操作类中方法
`getDeclaredMethods()` 获取类本身定义的所有方法， 不包含由继承获取到的方法
```java
    Class<?> cls = Class.forName("first.Book");
    Method[] methods = cls.getDeclaredMethods();
    for (Method method : methods) {
        System.out.println(method);
    }
```

获取指定的方法
```java
    // 传入方法名和参数类型
    Method method = cls.getDeclaredMethod("setName", String.class);
```

`getMethods()` 获取所有方法， 包含由继承获取到的方法, 但无法取得自身私有方法
```java
    Class<?> cls = Class.forName("first.Book");
    Method[] methods = cls.getMethods();
    for (Method method : methods) {
        System.out.println(method);
    }
```

获取指定的方法
```java
    Method method = cls.getMethod("setName", String.class);
```

调用方法
```java
    Class<?> cls = Class.forName("first.Book");
    Object object = cls.newInstance();
    Method method = cls.getMethod("setName", String.class);
    // 调用方法
    method.invoke(object, "hello");
```
### 操作类的成员属性

> 取得所有成员
```java
    Class<?> cls = Class.forName("first.Book");
    Field[] fields = cls.getDeclaredFields();
    for (Field field : fields) {
        System.out.println(field);
    }
```

> 获取单个成员
```java
    Class<?> cls = Class.forName("first.Book");
    Field field = cls.getDeclaredField("name");
    System.out.println(field);
```

> 取得所有成员， 包含由继承获取的成员， 但无法取得自身私有成员
```java
    Class<?> cls = Class.forName("first.Book");
    Field[] fields = cls.getFields();
    for (Field field : fields) {
        System.out.println(field);
    }
```

> set 和 get 属性的值
```java
    Class<?> cls = Class.forName("first.Book");
    Object object = cls.newInstance();
    Field field = cls.getDeclaredField("name");
    // 取消Java安全性检查
    field.setAccessible(true);
    // 设置值
    field.set(object, "你好");
    System.out.println(field.get(object));
```

### 操作注解
> 获取类的注解
```java
    Class<?> cls = Class.forName("first.Book");
    Annotation[] as = cls.getAnnotations();
    for (Annotation a : as) {
        System.out.println(a);
    }
```

> 获取指定的Annotation
```java
    Class<?> cls = Class.forName("first.Book");
    GetItem annotation = cls.getAnnotation(Deprecated.class);
    System.out.println(annotation.name());
    System.out.println(annotation.value());
```

************************

[Github: 更多反射Demo](https://github.com/Kuangcp/JavaBase/tree/class/src/test/java/com/github/kuangcp/reflects)

正常情况下 final修饰的类，变量，方法, 表示不可继承，不可修改，不可重写(override), 但是使用反射能在一定程度上进行修改  
被final修饰过的变量，只是说栈存储的地址不能再改变，但是却没有说地址指向的内容不能改变，所以反射可以破final，因为它修改该了以前地址的具体内容，但是没有改地址的信息。  
> 参考 [JavaDoc: Java8](https://docs.oracle.com/javase/8/docs/api/) `Field.set()`的文档说明

**********************

# 反射的性能问题
> [参考: java反射的性能问题 ](http://www.cnblogs.com/zhishan/p/3195771.html)
> [性能测试对比: 反射 set/get cglib mapstruct](https://github.com/Kuangcp/JavaBase/blob/class/src/test/java/com/github/kuangcp/reflects/ReflectPerformanceTest.java)

Spring 中的 IOC 主要是依据反射来实现的, 只在启动阶段性能有所损耗, 关注性能以及热点代码最好避免使用反射 例如常见的BeanCopy

[从一起GC血案谈到反射原理](https://club.perfma.com/article/54786)`总结： Method等Accessor对象每次get时会复制构造出新的对象，所以一般需要缓存； 反射数据是软引用`

> 优化方案
1. [使用 MapStruct 预生成转换代码避免反射](/Java/Tool/MapStruct.md)

