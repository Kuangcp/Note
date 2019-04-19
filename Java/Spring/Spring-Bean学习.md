# 容器

接口`org.springframework.context.ApplicationContext`表示Spring IoC容器，负责实例化，配置和组装bean。容器通过读取配置元数据获取有关要实例化、配置和组装的对象的指令。

# Bean概述

在容器内bean的定义包含以下信息:

-   `包限定的类名`：通常定义ben的实现类
-   `bean的行为元素`:包含bean的范围、生命周期等
-   `依赖项`：该bean所引用的依赖项
-   `设置其他属性配置`：如配置连接池bean中使用的连接数等

# Bean的实例化

-   使用静态方法实例化bean

    -   指定本类中的静态方法实例化对象(単例模式),官方实例配置如下

    ```
    <bean id="clientService"
        class="examples.ClientService"
        factory-method="createInstance"/>
    ```

    ```
    public class ClientService {
        private static ClientService clientService = new ClientService();
        private ClientService() {}

        public static ClientService createInstance() {
            return clientService;
        }
    }
    ```

    -   调用容器中其他类的方法实例化bean,官方实例如下

    ```
    <bean id="serviceLocator" class="examples.DefaultServiceLocator">
    </bean>

    <!-- 该bean的定义中class属性为空 -->
    <bean id="clientService"
        factory-bean="serviceLocator"
        factory-method="createClientServiceInstance"/>
    ```

    ```
    public class DefaultServiceLocator {

        private static ClientService clientService = new ClientServiceImpl();

        public ClientService createClientServiceInstance() {
            return clientService;
        }
    }
    ```

# Bean的作用域

在Spring2.0之前spring中bean的作用域只有`singleton（単例）`及`prototype（原型）`两种。在Spring2.0后便又增加了`request`、`session`及`application`三种作用域，且这三种作用域都只用于基于web的Spring ApplicationContext。直到现在，Spring又增加了作用与`webSocket`的作用域，该作用域与2.0之后增加的三种作用域一样都只作用与基于web的Spring ApplicationContext。一下便依次介绍者六中作用域

-   `singleton`: 该作用域是Spring bean默认的作用域；使用该作用域时，在Spring IOC容器中只会存在一个共享的bean实例。所有的对该bean的请求（如通过注入或getBean方法获取实例）都只会获取同一个实例。针对于该作用域，Spring容器可进行比较全面的生命周期的管理

-   `prototype`: 使用该作用域时，所有对于该bean的请求都会返回一个新的实例，即每次请求，都会创建一个新的实例

-   `request`: 该作用域将bean的作用范围限定在单个HTTP请求中，即每次HTTP请求都会创建一个新的bean实例，是的每次HTTP请求都有一个自己的实例。该作用域只用于基于web的Spring ApplicationContext。

-   `session`: 该作用域将bean的作用范围限定在HTTP请求中的Session的生命周期内。即bean的生命周期与Session一致，当Session存活时，该bean的实例也存活，但当Session销毁时，该Session内的bean实例也将被销毁。适合于基于web的Spring ApplicationContext

-   `application`: 使用该作用域时，在整个web程序中，只会存在一个该bean的实例。如果只存在一个web应用，则该bean的作用域与`singleton`类似。适合于基于web的Spring ApplicationContext。

-   `websocket`： 该作用域是Spring新增的作用域，该作用域将该bean实例作用范围限定在一个生命周期的WebSocket中。适合于基于web的Spring ApplicationContext。

