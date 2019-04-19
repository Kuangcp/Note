在Spring中。我们可以定义bean的初始化方法，从而完成某些初始化动作。但当我们需要在bean的初始化之前或之后完成某些操作该怎么办呢？对于优秀的Spring，当然已经想到了这一点，那便就是我们今天的主角`BeanPostProcessor`接口了。
那么什么是`BeanPostProcessor`呢，他怎么使用呢？首先让我们来看下源码中对该接口的解释吧！

![BeanPostProcessor](https://github.com/dragonhht/GitImgs/blob/master/Spring/beanPostProcessor_1.png)

该接口的注释大意是这样的

> 工厂钩子，允许自定义修改新的bean实例，例如 检查标记接口或用代理包装它们。  
> ApplicationContexts可以在其bean定义中自动检测 BeanPostProcessor bean，并将它们应用于随后创建的任何bean。bean factories允许对后处理器进行编程注册，适用于通过该工厂创建的所有bean。

简单来说，就是我们可以在Spring创建bean实例后，bean初始化之前和初始化之后完成一些自定义的操作。

然后让我们来看看它的两个方法：

-   `postProcessBeforeInitialization`

-   `postProcessAfterInitialization`

顾名思义，这两个方法，一个是在bean初始化之前执行，一个是在bean初始化之后执行。

> 假如有个定义好的Student，现在希望在不改变原有代码的情况下将它的address字段赋上某个值。

-   Student

```java
@Component
@Data
public class Student {

    private int id;
    private String name;
    private String address;

}
```

-   扩展

```java
@Component
public class StudentExpansion implements BeanPostProcessor {

    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        if (bean instanceof Student) {
            Student student = (Student) bean;
            student.setAddress("中国");
        }
        return bean;
    }
}
```