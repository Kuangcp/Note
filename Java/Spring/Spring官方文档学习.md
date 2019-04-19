# Spring官方文档学习

## １、Spring Bean的生命周期

-   初始化(当一个bean配置和了多个生命周期时，执行顺序如下顺序)

    -   在方法上使用`@PostConstruct`注解(推荐使用，同xml中的`init-method`属性一致)

    -   实现接口`InitializingBean`，在方法`afterPropertiesSet()`中可进行bean的初始化操作(在容器设置完bean的必须属性后执行，不建议使用接口，推荐使用注解或xml配置)
    
    -   在bean的xml配置中在`<beans>`标签上使用类似于属性`default-init-method="init"`的配置后,在beans下配置的bean会在初始化时调用bean中定义的方法名为`init`的方法

    -   实现接口`BeanPostProcessor`中的`postProcessBeforeInitialization`及`postProcessAfterInitialization`方法。该接口会处理他可以找到的所有回调接口    

-   销毁(当一个bean配置和了多个生命周期时，执行顺序如下顺序)

    -   在方法上使用`@PreDestroy`注解(同上，及与xml配置中的`destroy-method`属性一致)

    -   实现接口`DisposableBean`,在方法`destroy()`中，可进行bean的销毁时的操作
    
    -   在bean的xml配置中在`<beans>`标签上使用类似于属性`default-destroy-method="destroy"`的配置后,在beans下配置的bean会在销毁时调用bean中定义的方法名为`destroy`的方法
    
-   关闭与启动

    -   实现接口`Lifecycle`
    
    
-   在非Web应用中关闭spring IOC容器

    -   调用`ConfigurableApplicationContext`中的`registerShutdownHook()`方法，这样便就能调用销毁的回调函数
    
-   为Bean提供`ApplicationContext`实例

    -   实现`ApplicationContextAware`,则就可以为该bean实例获取`ApplicationContext`
    
-   让Bean获取自身在BeanFactory中的名称(id或name)

    -   实现`BeanNameAware`接口中,则咎可以获取名称(该方法在初始化之前)
    
## 2、Spring容器的扩展点

-  [BeanPostProcessor](https://github.com/dragonhht/Notes/blob/master/Java/Spring%E5%AE%B9%E5%99%A8%E6%89%A9%E5%B1%95%E7%82%B9%E4%B9%8BBeanPostProcessor.md)
