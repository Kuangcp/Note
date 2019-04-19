# Spring容器扩展点之BeanFactoryPostProcessor

`BeanFactoryPostProcessor`?怎么命名与前面讲过[BeanPostProcessor](https://github.com/dragonhht/Notes/blob/master/Java/Spring%E5%AE%B9%E5%99%A8%E6%89%A9%E5%B1%95%E7%82%B9%E4%B9%8BBeanPostProcessor.md)那么像呢?  
没错，他们都是Spring用于初始化Bean的扩展点，但他们的触发时间可是完全不一样的哦。`BeanFactoryPostProcessor`的执行时间是在Spring容器对bean进行实例化之前，而`BeanPostProcessor`的时间则是在Spring容器对bean进行实例化之后。  
`BeanFactoryPostProcessor`允许对bean的定义(配置的元数据)进行修改。例如我们常见的下列配置：

```
<!--加载配置文件-->
<context:property-placeholder        location="classpath:jdbc.properties"/>

<!--配置c3p0连接池-->
<bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
    <property name="driverClass" value="${jdbc.driver}"/>
    <property name="jdbcUrl" value="${jdbc.url}"/>
    <property name="user" value="${jdbc.user}"/>
    <property name="password" value="${jdbc.password}"/>
</bean>
```

在以上对于数据库的配置中，我们引用了配置文件`jdbc.properties`中的值

```
jdbc.driver = com.mysql.jdbc.Driver
jdbc.url = jdbc:mysql:///BookManager
jdbc.user = root
jdbc.password =123
```

那么问题来了，在Spring将bean实例化时是如何将配置元数据中的`${jdbc.driver}`替换成真实的`com.mysql.jdbc.Driver`的呢？这便就是`BeanFactoryPostProcessor`在Spring容器中的最典型的使用场景之一。该处理的实现类为`PropertyPlaceholderConfigurer`，它实现了接口`BeanFactoryPostProcessor`中的`postProcessBeanFactory`方法，负责在bean实例化之前将配置元数据中的如同`${jdbc.driver}`的配置替换为它真实的值，然后Spring便就可以正常的实例化了。  

-   在`PropertyPlaceholderConfigurer`中`postProcessBeanFactory`方法的实现如下：

```java
/**
    * {@linkplain #mergeProperties Merge}, {@linkplain #convertProperties convert} and
    * {@linkplain #processProperties process} properties against the given bean factory.
    * @throws BeanInitializationException if any properties cannot be loaded
    */
@Override
public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
    try {
        // 读取配置中配置的properties文件
        Properties mergedProps = mergeProperties();

        // Convert the merged properties, if necessary.
        convertProperties(mergedProps);

        // Let the subclass process the properties.
        processProperties(beanFactory, mergedProps);
    }
    catch (IOException ex) {
        throw new BeanInitializationException("Could not load properties", ex);
    }
}
```

-   其中`processProperties`方法在`PropertyPlaceholderConfigurer`中的实现为

```java
/**
    * Visit each bean definition in the given bean factory and attempt to replace ${...} property
    * placeholders with values from the given properties.
    */
@Override
protected void processProperties(ConfigurableListableBeanFactory beanFactoryToProcess, Properties props)
        throws BeansException {

    StringValueResolver valueResolver = new PlaceholderResolvingStringValueResolver(props);
    doProcessProperties(beanFactoryToProcess, valueResolver);
}
```

好了，如果有兴趣的同学可以去仔细看看源码哦，这里只是简单的阐述下`BeanFactoryPostProcessor`的使用场景