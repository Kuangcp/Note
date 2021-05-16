---
title: Java中的注解
date: 2018-11-21 10:56:52
tags: 
    - 注解
categories: 
    - Java
---

**目录 start**

1. [注解](#注解)
    1. [自定义Annotation](#自定义annotation)
    1. [读取](#读取)

**目录 end**|_2021-05-17 00:15_|
****************************************
# 注解

> 参考博客 [全面解析Java注解](http://blog.csdn.net/chenxiang0207/article/details/8193980) | [Java注解（2）-运行时框架](http://blog.csdn.net/duo2005duo/article/details/50511476)

> 参考项目 [AnnotationDemo](https://github.com/zhuifengshen/AnnotationDemo)

- 注解定义包含四个元注解，分别为@Target,@Retention,@Documented, @Inherited。各元注解的作用如下：
    1. **@Target** 表示该注解用于什么地方，可能的 ElemenetType 参数包括：
        - `ElemenetType.CONSTRUCTOR` 构造器声明。
        - `ElemenetType.FIELD` 域声明（包括 enum 实例）。
        - `ElemenetType.LOCAL_VARIABLE` 局部变量声明。
        - `ElemenetType.METHOD` 方法声明。
        - `ElemenetType.PACKAGE` 包声明。
        - `ElemenetType.PARAMETER` 参数声明。
        - `ElemenetType.TYPE` 类，接口（包括注解类型）或enum声明。

    1. **@Retention**  表示在什么级别保存该注解信息。可选的 RetentionPolicy 参数包括：
        - `RetentionPolicy.SOURCE`  java
        - `RetentionPolicy.CLASS`   java + class
        - `RetentionPolicy.RUNTIME` java + class + jvm, 因此可以通过反射机制读取注解的信息。

        > 举一个例子，如@Override里面的Retention设为SOURCE，编译成功了就不要这一些检查的信息，相反，@Deprecated里面的Retention设为RUNTIME，表示除了在编译时会警告我们使用了哪个被Deprecated的方法，在执行的时候也可以查出该方法是否被Deprecated。

    1. **@Documented**  将此注解包含在 javadoc 中

    1. **@Inherited**  允许子类继承父类中的注解

## 自定义Annotation

```java
  @Retention(value = RetentionPolicy.RUNTIME)
  public @interface GetItem {
      // 设置属性内容
      String name() default "hello";
      String value();
  }
```

> [自定义 JSR303 Validation 注解](https://github.com/Kuangcp/JavaBase/tree/master/web/src/main/java/com/github/kuangcp/validation)

## 读取
> [相关代码片段](https://gitee.com/gin9/codes/s148mbplxo06qgn25d3wc23)

- 判断是否有指定注解类型的注解
    - 在类上的注解就是得到类对象, 然后判断 isAnnotationPresent(ExcelConfig.class)
    - 在方法上的注解就是得到所有方法, 属性同理
