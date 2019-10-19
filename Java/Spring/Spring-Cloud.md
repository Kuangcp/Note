---
title: Spring-Cloud.md
date: 2019-10-19 17:04:24
tags: 
categories: 
---

**目录 start**
 
1. [Spring Cloud 学习](#spring-cloud-学习)
    1. [一、[注册中心(服务注册与发现)](https://github.com/dragonhht/spring-cloud-study2/cloud-study-registration-center)(Eureka)](#一、[注册中心服务注册与发现]httpsgithubcomdragonhhtspring-cloud-study2cloud-study-registration-centereureka)
        1. [使用](#使用)
    1. [二、[服务提供者](https://github.com/dragonhht/spring-cloud-study2/cloud-study-service)](#二、[服务提供者]httpsgithubcomdragonhhtspring-cloud-study2cloud-study-service)
        1. [使用](#使用)
    1. [三、[(消费者使用)负载均衡](https://github.com/dragonhht/spring-cloud-study2/cloud-study-consumer-using-loadbalancer/src/main/java/spring/cloud/study2/consumer/ConsumerApplication_9999.java)(Ribbon)](#三、[消费者使用负载均衡]httpsgithubcomdragonhhtspring-cloud-study2cloud-study-consumer-using-loadbalancersrcmainjavaspringcloudstudy2consumerconsumerapplication_9999javaribbon)
        1. [使用](#使用)
    1. [四、[断路器](https://github.com/dragonhht/spring-cloud-study2/cloud-study-consumer-using-loadbalancer/src/main/java/spring/cloud/study2/consumer/service/ConsumerService.java)(Hystrix)](#四、[断路器]httpsgithubcomdragonhhtspring-cloud-study2cloud-study-consumer-using-loadbalancersrcmainjavaspringcloudstudy2consumerserviceconsumerservicejavahystrix)
        1. [使用](#使用)
    1. [五、[配置中心](https://github.com/dragonhht/spring-cloud-study2/cloud-study-config-server)(采用git来存储配置信息)](#五、[配置中心]httpsgithubcomdragonhhtspring-cloud-study2cloud-study-config-server采用git来存储配置信息)
        1. [使用](#使用)
        1. [在应用中获取配置信息](#在应用中获取配置信息)
    1. [六、[服务网关(内提供负载均衡)](https://github.com/dragonhht/spring-cloud-study2/cloud-study-service-gateway)(Zuul)](#六、[服务网关内提供负载均衡]httpsgithubcomdragonhhtspring-cloud-study2cloud-study-service-gatewayzuul)
        1. [使用](#使用)
        1. [服务过滤](#服务过滤)
            1. [使用](#使用)

**目录 end**|_2019-10-19 17:04_|
****************************************
# Spring Cloud 学习

## 一、[注册中心(服务注册与发现)](https://github.com/dragonhht/spring-cloud-study2/cloud-study-registration-center)(Eureka)

### 使用

-   maven依赖

    ```
    <dependency>
          <groupId>org.springframework.cloud</groupId>
          <artifactId>spring-cloud-starter-eureka-server</artifactId>
    </dependency>
    ```

-   在启动类上使用注解`@EnableEurekaServer`启动一个服务注册中心提供给其他应用进行对话

-   配置：在默认设置下，该服务注册中心也会将自己作为客户端来尝试注册它自己，所以我们需要禁用它的客户端注册行为，配置如下：

    ```
    server:
        port: 8080
    
    eureka:
        client:
            register-with-eureka: false
            fetch-registry: false
            serviceUrl.defaultZone: http://localhost:${server.port}/eureka/
    ```
    
## 二、[服务提供者](https://github.com/dragonhht/spring-cloud-study2/cloud-study-service)

### 使用

-   在启动类类上使用`@EnableEurekaClient`注解，开启eureka客户端，可以注册服务及发现调用服务

-   配置：

    ```
    server:
      port: 8081
    
    spring:
      application:
        name: provider-service    # 指定微服务的名称后续在调用的时候只需要使用该名称就可以进行服务的访问。
    
    eureka:
      client:
        serviceUrl:
          defaultZone:  http://localhost:8080/eureka/   # 指定服务注册中心的位置。
    ```
    
## 三、[(消费者使用)负载均衡](https://github.com/dragonhht/spring-cloud-study2/cloud-study-consumer-using-loadbalancer/src/main/java/spring/cloud/study2/consumer/ConsumerApplication_9999.java)(Ribbon)

> Ribbon是一个基于HTTP和TCP客户端的负载均衡器。

### 使用

-   maven依赖

    ```
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-ribbon</artifactId>
    </dependency>
    ```

-   在启动类上使用`@EnableEurekaClient`,使服务被发现注册。创建RestTemplate实例，并通过`@LoadBalanced`注解开启均衡负载能力。

## 四、[断路器](https://github.com/dragonhht/spring-cloud-study2/cloud-study-consumer-using-loadbalancer/src/main/java/spring/cloud/study2/consumer/service/ConsumerService.java)(Hystrix)

### 使用

-   maven依赖

    ```
    <dependency>
         <groupId>org.springframework.cloud</groupId>
         <artifactId>spring-cloud-starter-hystrix</artifactId>
    </dependency>
    ```
    
-   在启动类上使用`@EnableCircuitBreaker`注解，注解开启断路器功能

-   在需要的方法上添加`@HystrixCommand(fallbackMethod = "回调方法名")`注解，指定回调方法

## 五、[配置中心](https://github.com/dragonhht/spring-cloud-study2/cloud-study-config-server)(采用git来存储配置信息)

### 使用

-   maven依赖

    ```
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-config-server</artifactId>
    </dependency>
    ```
    
-   在启动类上使用`@EnableConfigServer`注解，开启Config Server

-   配置(配置文件命令格式`{application}-{profile}.{yml | properties}`)

    -   使用本地配置文件
    
    ```
    server:
      port: 9998
    
    spring:
      application:
        name: config-server
    
      # 使用本地配置
      profiles:
          active: native
      cloud:
        config:
          server:
            native:
              searchLocations:  /home/huang/Work_Space/Idea_Space/spring-cloud-study2/cloud-study-config-server/config-pero
    ```
    
    -   使用git远程配置文件（推荐，默认使用）
    
    ```
    server:
      port: 9998
    
    spring:
      application:
        name: config-server
        
      profiles:
          active: git # spring cloud默认为从git获取
      cloud:
        config:
          server:
            git:
              uri: https://github.com/dragonhht/spring-cloud-study2   # 配置git仓库位置
              search-paths: cloud-study-config-server/config-pero     # 配置仓库路径下的相对搜索位置，可以配置多个

    ```
    
-   访问路径:如，`http://localhost:9998/{application}/{profile}/{git分支}`
    
### 在应用中获取配置信息

-   maven依赖

    ```
    <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
         <groupId>org.springframework.cloud</groupId>
         <artifactId>spring-cloud-starter-config</artifactId>
    </dependency>
    ```
    
-   创建`bootstrap.yml`配置，来指定config server(这些属性必须配置在`bootstrap.yml`中，config部分内容才能被正确加载。因为config的相关配置会先于`application.yml`，而`bootstrap.yml`的加载也是先于`application.yml`)

    ```
    spring:
      application:
        name: config      # 对应配置文件的{application}部分
      cloud:
        config:
          profile: one    # 对应配置文件{profile}部分
          label: master   # 对应git分支
          uri: http://localhost:9998/    # 配置中心的地址
    ```

-   [获取](https://github.com/dragonhht/spring-cloud-study2/cloud-study-config-client/src/main/java/spring/cloud/study2/config/client/controller/ConfigController.java)：在需要注入的地方使用`@Value("${test}")`注解，便可注入服务配置中的test属性 

## 六、[服务网关(内提供负载均衡)](https://github.com/dragonhht/spring-cloud-study2/cloud-study-service-gateway)(Zuul)

### 使用

-   maven依赖

    ```
    <dependency>
         <groupId>org.springframework.cloud</groupId>
         <artifactId>spring-cloud-starter-zuul</artifactId>
    </dependency>
    <dependency>
         <groupId>org.springframework.cloud</groupId>
         <artifactId>spring-cloud-starter-eureka</artifactId>
    </dependency>
    ```
    
-   在启动类上使用`@EnableZuulProxy`注解开启Zuul，使用`@SpringCloudApplication`注解(该注解包含`@SpringBootApplication`，`@EnableDiscoveryClient`，`@EnableCircuitBreaker`注解)

-   配置Zuul

    -   基础信息(应用名、服务端口等)
    
    ```
    server:
      port: 9990
    
    spring:
      application:
        name: api-gateway
    ```
    
    -   配置服务路由(以下配置中的`api-a-url`和`api-b-url`为路由名(可以任意定义，但是一组映射关系的path和url(serviceId)要相同))
    
        -   通过url直接映射
        
        ```
        zuul:
          routes:
            api-a-url:
              path: /api-service1/**
              url:  http://localhost:8081
            api-b-url:
              path: /api-service2/**
              url:  http://localhost:8082
        ```
        
        -   将Zuul注册到eureka server上,从而去发现其他服务(推荐)
        
        ```
        zuul:
          routes:
            api-a-url:
              path: /api-service1/**
              serviceId:  provider-service1
            api-b-url:
              path: /api-service2/**
              serviceId:  provider-service2     # serviceId为eureka server中注册的服务,serviceId映射方式还支持了断路器
        eureka:
          client:
            serviceUrl:
              defaultZone:  http://localhost:8080/eureka/   # 指定服务注册中心的位置。
        ```
        
### 服务过滤

> 为对外开放服务提供一些安全措施，从而保护客户端只能访问它应该访问到的资源

#### 使用

-   [定义过滤器](https://github.com/dragonhht/spring-cloud-study2/cloud-study-service-gateway/src/main/java/spring/cloud/study2/gateway/filter/AccessFilter.java)(创建类，使该类继承`ZuulFilter`)

-   实例化过滤器

    ```
    @Bean
        public AccessFilter getAccessFilter() {
            return new AccessFilter();
        }
    ```   
