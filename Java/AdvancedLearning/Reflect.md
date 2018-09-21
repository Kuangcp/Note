`目录 start`
 
- [反射](#反射)
    - [获取属性](#获取属性)
    - [获得方法](#获得方法)
        - [性能问题](#性能问题)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 反射
> [ Java反射异常处理之InvocationTargetException ](https://blog.csdn.net/zhangzeyuaaa/article/details/39611467)

> [参考博客: java8--类加载机制与反射(java疯狂讲义3复习笔记)](https://www.cnblogs.com/lakeslove/p/5978382.html)
> [参考博客: Java8替代传统反射动态获取成员变量值的一个示例](https://segmentfault.com/a/1190000007492958)
> [参考博客: java反射的性能问题](http://www.cnblogs.com/zhishan/p/3195771.html)

## 获取属性
_通过属性名得到对象属性的值_
```java
    PropertyDescriptor propertyDescriptor = new PropertyDescriptor(meta.getField().getName(), target);
    Method method = propertyDescriptor.getReadMethod();
    Object result = method.invoke(model);
```
或者如下方式更为简洁
```java
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

## 获得方法

### 性能问题
> [参考博客: java反射的性能问题 ](http://www.cnblogs.com/zhishan/p/3195771.html)

