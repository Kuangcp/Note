# Dubbo学习(均使用XML配置)

## 一、架构

![dubbo结构图](http://dubbo.apache.org/img/architecture.png)


1.   服务容器(Container）负责启动、加载及运行服务提供者（Provider）
2.   服务提供者在启动时,告诉注册中心(Registry)自己的服务
3.   服务消费者(Consumer)在启动时，向注册中心d明月自己需要的服务
4.   注册中心将返回提供者地址列表给消费者，如果有变更，注册中心将基于长连接推送b变更数据给消费者
5.   消费者从提供者地址列表中基于软负载均衡算法,选择一台提供者进行调用,如果调用失败，则选择另一台调用
6.   x消费者和提供者，在内存中累计调用次数和时间,定时每分钟发送一次统计数据到监控中心(Monitor)

## 二、XML配置重要标签

| 标签  |   标签描述    |   特殊说明    |
| -------------------------------------- |-------------------------------------- |-------------------------------------- |
|\<dubbo:application />| 用于配置当前应用信息，不管该应用是提供者还是消费者 | 应用配置  |
|\<dubbo:service/>| 用于暴露一个服务，定义服务的元信息，一个服务可以用多个协议暴露，一个服务也可以注册到多个注册中心  |  服务配置 |
|\<dubbo:reference/>|   用于创建一个远程服务代理，一个引用可以指向多个注册中心| 引用配置 |
|\<dubbo:protocol/>|  用于配置提供服务的协议信息，协议由提供方指定，消费方被动接受| 协议配置 |
|\<dubbo:module/>|  用于配置当前模块信息，可选| 模块配置 |
|\<dubbo:registry/>|    用于配置连接注册中心相关信息| 注册中心配置  |
|\<dubbo:monitor/>|用于配置连接监控中心相关信息，可选| 监控中心配置  |
|\<dubbo:provider/>|当 ProtocolConfig 和 ServiceConfig 某属性没有配置时，采用此缺省值，可选| 提供方配置 |
|\<dubbo:consumer/>| 当 ReferenceConfig 某属性没有配置时，采用此缺省值，可选| 消费方配置 |
|\<dubbo:method/>|用于 ServiceConfig 和 ReferenceConfig 指定方法级的配置信息| 方法配置|
|\<dubbo:argument/>|用于指定方法参数配置|参数配置|

## 三、其他标签属性

###   1、启动检查

> Dubbo默认在启动时检查依赖的服务是否可用，若需要关闭该检查可使用`check`属性

-   关闭某个服务的启动时检查`<dubbo:reference interface="hht.dragon.TestService" check="false" />`

-   关闭所有服务的启动时检查`<dubbo:consumer check="false" />`

-   关闭注册中心启动时检查`<dubbo:registry check="false" />`

###     2、集群容错


###     3、线程模型

-   在dubbo中可配置线程池，如`<dubbo:protocol name="dubbo" dispatcher="all" threadpool="fixed" threads="100" />`

-   各参数说明

    -   Dispatcher
    
        -  `all` : 所有消息都派发到线程池，包括请求，响应，连接事件，断开事件，心跳等
        
        -   `direct` : 所有消息都不派发到线程池，全部在 IO 线程上直接执行
        
        -   `message` : 只有请求响应消息派发到线程池，其它连接断开事件，心跳等消息，直接在 IO 线程上执行
        
        -   `execution` : 只请求消息派发到线程池，不含响应，响应和其它连接断开事件，心跳等消息，直接在 IO 线程上执行
        
        -   `connection` : 在 IO 线程上，将连接断开事件放入队列，有序逐个执行，其它消息派发到线程池
        
    -   ThreadPool
    
        -   `fixed` : 固定大小线程池，启动时建立线程，不关闭，一直持有,默认值
        
        -   `cached` : 缓存线程池，空闲一分钟自动删除，需要时重建
        
        -   `limited` : 可伸缩线程池，但池中的线程数只会增长不会收缩。只增长不收缩的目的是为了避免收缩时突然来了大流量引起的性能问题
        
        -   `eager` : 优先创建`Worker`线程池。在任务数量大于`corePoolSize`但是小于`maximumPoolSize`时，优先创建`Worker`来处理任务。当任务数量大于`maximumPoolSize`时，将任务放入阻塞队列中。阻塞队列充满时抛出`RejectedExecutionException`。(相比于`cached:cached`在任务数量超过`maximumPoolSize`时直接抛出异常而不是将任务放入阻塞队列)   

###     4、直连提供者(建议生产环境不要使用，可在测试阶段中使用)

-   在需要将消费者与提供者直接连接，即绕过注册中心的情况时，可在`\<dubbo:reference>`中配置提供者的url，如`\<dubbo:reference id="xxxService" interface="com.alibaba.xxx.XxxService" url="dubbo://localhost:20890" />
`

## 四、使用ZooKeeper

-   添加依赖

```
<dependency>
    <groupId>org.apache.zookeeper</groupId>
    <artifactId>zookeeper</artifactId>
    <version>3.4.11</version>
</dependency>

<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-recipes</artifactId>
    <version>4.0.1</version>
</dependency>
```

-   服务提供端配置： `\<dubbo:registry address="zookeeper://127.0.0.1:2181" />`

-   服务消费端配置： `\<dubbo:registry address="zookeeper://127.0.0.1:2181" />`


## 五、与Spring Boot整合

-   服务提供端

    -   在Service实现类中使用`Dubbo`的`@Service`注解

    ```kotlin
    @Service
    class SayHelloServiceImp : HelloService {
        override fun Hello() {
            println("你好!!!")
        }

        override fun sayWord(name: String): String {
            return "$name: 你好"
        }

    }
    ```

    -   全局Dubbo配置

    ```kotlin
    @Configuration
    open class DubboConfig {

        @Bean
        open fun applicationConfig() : ApplicationConfig {
            val applicationConfig = ApplicationConfig()
            applicationConfig.name = "spring-boot-provider"
            return applicationConfig
        }

        @Bean
        open fun registryConfig() : RegistryConfig {
            val registryConfig = RegistryConfig()
            registryConfig.address = "zookeeper://127.0.0.1:2181"
            return registryConfig
        }

    }
    ```

    -   在Spring Boot启动类中添加注解`@DubboComponentScan`，自定需暴露的服务的实现

    ```
    @SpringBootApplication
    @DubboComponentScan(basePackages = ["hht.dragon.spring.boot.provider.service.impl"])
    open class SpringBootProviderApplication

    fun main(args: Array<String>) {
        runApplication<SpringBootProviderApplication>(*args)
    }
    ```

-   服务消费端

    -   在需要使用服务端服务的类中使用注解`@Reference`,引用服务端服务

    ```kotlin
    @Service
    class ConsumerService {

        @Reference
        lateinit var helloService: HelloService

        fun sayHello() {
            helloService.Hello()
            val say = helloService.sayWord("消费端调用")
            println(say)
        }

    }
    ```

    -   全局Dubbo配置

    ```kotlin
    @Configuration
    open class MyConsumerConfig {

        @Bean
        open fun applicationCofig() : ApplicationConfig {
            val applicationConfig = ApplicationConfig()
            applicationConfig.name = "consumer-name"
            return applicationConfig
        }

        @Bean
        open fun consumerConfig() : ConsumerConfig {
            val consumerConfig = ConsumerConfig()
            consumerConfig.timeout = 3000
            return consumerConfig
        }

        @Bean
        open fun registryConfig() : RegistryConfig {
            val registryConfig = RegistryConfig()
            registryConfig.address = "zookeeper://127.0.0.1:2181"
            return registryConfig
        }

    }
    ```

    -   在Spring Boot启动类中使用`@DubboComponentScan`,指定service包

    ```kotlin
    @SpringBootApplication
    @DubboComponentScan(basePackages = ["hht.dragon.consumer.service"])
    open class SpringBootConsumerApplication

    fun main(args: Array<String>) {
        runApplication<SpringBootConsumerApplication>(*args)
    }
    ```
