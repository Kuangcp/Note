`目录 start`
 
- [注解](#注解)
    - [读取](#读取)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 注解

> 参考博客 [全面解析Java注解](http://blog.csdn.net/chenxiang0207/article/details/8193980) | [Java注解（2）-运行时框架](http://blog.csdn.net/duo2005duo/article/details/50511476)

> 参考项目 [AnnotationDemo](https://github.com/zhuifengshen/AnnotationDemo)

注解定义包含四个元注解，分别为@Target,@Retention,@Documented,@Inherited。各元注解的作用如下：
- ① @Target
    - 表示该注解用于什么地方，可能的 ElemenetType 参数包括：
    - ElemenetType.CONSTRUCTOR 构造器声明。
    - ElemenetType.FIELD 域声明（包括 enum 实例）。
    - ElemenetType.LOCAL_VARIABLE 局部变量声明。
    - ElemenetType.METHOD 方法声明。
    - ElemenetType.PACKAGE 包声明。
    - ElemenetType.PARAMETER 参数声明。
    - ElemenetType.TYPE 类，接口（包括注解类型）或enum声明。

- ② @Retention
    - 表示在什么级别保存该注解信息。可选的 RetentionPolicy 参数包括：
    - RetentionPolicy.SOURCE 注解将被编译器丢弃。
    - RetentionPolicy.CLASS 注解在class文件中可用，但会被VM丢弃。
    - RetentionPolicy.RUNTIME VM将在运行期也保留注释，因此可以通过反射机制读取注解的信息。
> 举一个例子，如@Override里面的Retention设为SOURCE，编译成功了就不要这一些检查的信息，相反，@Deprecated里面的Retention设为RUNTIME，表示除了在编译时会警告我们使用了哪个被Deprecated的方法，在执行的时候也可以查出该方法是否被Deprecated。

- ③ @Documented
    - 将此注解包含在 javadoc 中
- ④ @Inherited
    - 允许子类继承父类中的注解

## 读取
- 判断是否有指定注解类型的注解
    - 在类上的注解就是得到类对象, 然后判断 isAnnotationPresent(ExcelConfig.class)
    - 在方法上的注解就是得到所有方法, 属性同理
- [相关代码片段](https://gitee.com/kcp1104/codes/s148mbplxo06qgn25d3wc23)
