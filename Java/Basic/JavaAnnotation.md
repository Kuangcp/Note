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

- 注解定义包含6个元注解: @Target,@Retention,@Documented, @Inherited, @Repeatable, @Native 。各元注解的作用如下：
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

    1. **@Repeatable** 1.8新增，允许一个注解在一个元素上使用多次 

    1. **@Native**1.8新增，修饰成员变量，表示这个变量可以被本地代码引用，常常被代码生成工具使用

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

## 读取类上注解
> [相关代码片段](https://gitee.com/gin9/codes/s148mbplxo06qgn25d3wc23)

- 判断是否有指定注解类型的注解
    - 在类上的注解就是得到类对象, 然后判断 isAnnotationPresent(ExcelConfig.class)
    - 在方法上的注解就是得到所有方法, 属性同理

## Java中常用注解使用

@Override 表示当前方法覆盖了父类的方法

@Deprecated 表示方法已经过时,方法上有横线，使用时会有警告。

@SuppressWarnings 表示关闭一些警告信息(通知java编译器忽略特定的编译警告)

@SafeVarargs (jdk1.7更新) 表示：专门为抑制“堆污染”警告提供的。

@FunctionalInterface (jdk1.8更新) 表示：用来指定某个接口必须是函数式接口，否则就会编译出错。

### Spring常用注解

@Configuration把一个类作为一个IoC容器，它的某个方法头上如果注册了@Bean，就会作为这个Spring容器中的Bean。

@Scope注解 作用域

@Lazy(true) 表示延迟初始化

@Service用于标注业务层组件

@Controller用于标注控制层组件@Repository用于标注数据访问组件，即DAO组件。

@Component泛指组件，当组件不好归类的时候，我们可以使用这个注解进行标注。

@Scope用于指定scope作用域的（用在类上）

@PostConstruct用于指定初始化方法（用在方法上）

@PreDestory用于指定销毁方法（用在方法上）

@DependsOn：定义Bean初始化及销毁时的顺序

@Primary：自动装配时当出现多个Bean候选者时，被注解为@Primary的Bean将作为首选者，否则将抛出异常

@Autowired 默认按类型装配，如果我们想使用按名称装配，可以结合@Qualifier注解一起使用。如下： @Autowired @Qualifier("personDaoBean") 存在多个实例配合使用

@Resource默认按名称装配，当找不到与名称匹配的bean才会按类型装配。

@PostConstruct 初始化注解

@PreDestroy 摧毁注解 默认 单例 启动就加载