# Spring容器扩展点之Aware接口

在Spring容器中，提供了许多Aware接口，使用这些接口可以更好的对bean进行扩展，获取许多与容器相关的组件；今天，我们大概来看看Spring中提供的一些Aware接口：

-   `BeanNameAware`: 该接口只有一个`setBeanName`方法，如果Spring容器检测到bean实现了该接口，则会将该bean实例的beanName属性注入到该实例中。


-   `ApplicationContextAware`: 该接口只有个`setApplicationContext`方法；如果Spring容器检测到bean实现了该接口，则会将Spring的ApplicationContext注入到bean实例中。但一般不建议通过实现该接口获取容器ApplicationContext，因为通过实现接口的方式会增加代码的耦合度，如果希望获取ApplicationContext实例，可以使用一般的注入方式，如使用注解`@Autowired`,这样便就可以获取ApplicationContext，如：

```java
@Autowired
private ApplicationContext applicationContext;
```

-   `BeanClassLoaderAware`: 该接口有个`setBeanClassLoader`方法，与前两个接口类似，实现了该接口后，可以向bean中注入加载该bean的ClassLoader


-   `BeanFactoryAware`: 该接口有个`setBeanFactory`方法，用来将当前的beanFactory注入到该bean实例中


-   `ApplicationEventPublisherAware`: ApplicationContext事件机制是观察者设计模式的实现，通过ApplicationEvent类和ApplicationListener接口，可以实现ApplicationContext的事件处理。其中`ApplicationEvent`为容器事件。实现接口`ApplicationEventPublisherAware`的bean可获取`ApplicationEventPublisher`实例(因为ApplicationContext已实现接口`ApplicationEventPublisher`接口，所以其实此处默认还是注入了`ApplicationContext`实例)，用于发布事件


-   `MessageSourceAware`: 实现该接口可，可获取`MessageSource`实例，该实例用于解析消息的策略接口,支持该类消息的参数化与国际化(因为ApplicationContext已实现接口`MessageSource`接口，所以其实此处默认还是注入了`ApplicationContext`实例)


-   `NotificationPublisherAware`: 实现该接口的bean，可获取JMX通知发布者

-   `ResourceLoaderAware`: 可获取Spring中配置的加载程序(ResourceLoader)，用于对资源进行访问；可用于访问类l类路径或文件资源

-   `ServletConfigAware`: 该接口仅在wen应用中有效，用于获取ServletConfig

-   `ServletContextAware`: 该接口仅在wen应用中有效，用于获取ServletContext

-   `LoadTimeWeaverAware`: 可获取`LoadTimeWeaver`实例，用于在加载时处理类定义
