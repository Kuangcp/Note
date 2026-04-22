---
title: SpringBoot
date: 2018-12-21 10:49:39
tags: 
    - SpringBoot
categories: 
    - Java
---

💠

- 1. [SpringBoot](#springboot)
    - 1.1. [思考](#思考)
    - 1.2. [参考教程](#参考教程)
    - 1.3. [使用SpringBootCLI](#使用springbootcli)
    - 1.4. [Profiles](#profiles)
        - 1.4.1. [多种配置文件](#多种配置文件)
            - 1.4.1.1. [yml方式](#yml方式)
            - 1.4.1.2. [yml和properties结合](#yml和properties结合)
        - 1.4.2. [应用配置文件](#应用配置文件)
    - 1.5. [Jpa](#jpa)
        - 1.5.1. [spring.jpa.open-in-view](#springjpaopen-in-view)
    - 1.6. [Events](#events)
    - 1.7. [Logging](#logging)
    - 1.8. [Cache](#cache)
    - 1.9. [Web模块](#web模块)
        - 1.9.1. [Lisener](#lisener)
            - 1.9.1.1. [ServletContextListener](#servletcontextlistener)
        - 1.9.2. [上传下载文件](#上传下载文件)
        - 1.9.3. [错误页面跳转配置](#错误页面跳转配置)
        - 1.9.4. [跨域](#跨域)
        - 1.9.5. [全局异常处理](#全局异常处理)
        - 1.9.6. [Validator](#validator)
        - 1.9.7. [Response](#response)
    - 1.10. [测试模块](#测试模块)
    - 1.11. [运行和部署](#运行和部署)
        - 1.11.1. [mvn 运行](#mvn-运行)
        - 1.11.2. [编译打包jar/war](#编译打包jarwar)
            - 1.11.2.1. [war](#war)
            - 1.11.2.2. [jar](#jar)
        - 1.11.3. [构建Docker镜像](#构建docker镜像)
            - 1.11.3.1. [手动方式](#手动方式)
        - 1.11.4. [热部署](#热部署)
        - 1.11.5. [优雅重启](#优雅重启)
        - 1.11.6. [运行性能优化](#运行性能优化)

💠 2026-04-22 20:30:37
****************************************
# SpringBoot
> [Doc](https://spring.io/projects/spring-boot#learn)

> [SpringBoot2](./SpringBoot2.md)  
> [SpringBoot3](./SpringBoot3.md)  

## 思考
- [SpringBoot优缺点](https://www.zhihu.com/question/39483566) 
    - `大大降低编程门槛, 但是, 将大量细节隐藏在默认配置中, 需要详细阅读文档和源码才能更好的玩转SpringBoot, 不然到处是坑`

- [SpringBoot启动流程解析](https://www.cnblogs.com/trgl/p/7353782.html)`原理才是王道`
- [spring boot应用启动原理分析 ](https://yq.aliyun.com/articles/6056)

- Spring 是单例模式, 全部使用IOC容器进行管理, 那么怎么处理并发下数据共享安全性问题
    - 答案是 ThreadLocal 分别存储了各自的数据, 所以才说, 不能在Controller层 放置属性, 使其具有状态, 从而导致并发问题
    - 那么WebSocket服务器, 处理并发会不会有并发问题?

- [为什么说 Java 程序员到了必须掌握 Spring Boot 的时候？](http://www.ityouknow.com/springboot/2018/06/12/spring-boo-java-simple.html)

## 参考教程
- [SpringBoot中文索引](http://springboot.fun/)
- [参考: Spring Boot 入门系列](http://www.spring4all.com/article/246)
- [Springboot探索](https://juejin.im/post/598dd709f265da3e213f0c57)
- [SpringBoot入门](http://blog.csdn.net/jsyxcjw/article/details/46763639)

> [Guide](https://spring.io/guides/gs/actuator-service/)
> [小马哥书籍《Spring Boot 编程思想》示例工程 ](https://github.com/mercyblitz/thinking-in-spring-boot-samples)

- [Springboot入门系列博客](http://www.cnblogs.com/page12/p/7899380.html)
- [Springboot配置详解](https://segmentfault.com/a/1190000004315890)
- [Springboot启动dubbo](https://coderknock.com/blog/2017/03/01/spring%20boot%E5%90%AF%E5%8A%A8dubbo.html)`等一系列文章`
- [spring boot完美集成dwr3.0.2](http://blog.csdn.net/melody_susan/article/details/78659696)
- [Spring Boot——开发新一代Spring Java应用](https://www.tianmaying.com/tutorial/spring-boot-overview)

> [xiaour/SpringBootDemo: 🍃SpringBoot系列Demo；SpringBoot、MyBatis、Redis、MySql、Kafka、RocketMQ](https://github.com/xiaour/SpringBootDemo)  

`系列`

- [一系列专栏](https://github.com/guoxiaoxu/guo-projects/tree/master/guns-admin/note)
- [个人博客专栏: SpringBoot干货系列](http://tengj.top/tags/Spring-Boot/)
- [SpringBoot系列文章](http://www.ityouknow.com/spring-boot)
- [恒宇少年](https://www.jianshu.com/u/092df3f77bca)

******************

## 使用SpringBootCLI
- 使用 SDKMAN 进行安装
    - 使用git bash运行  `curl -s get.sdkman.io | bash`
    - `source "/Users/{yourname}/.sdkman/bin/sdkman-init.sh" `根据实际目录去运行
    - spring --version
- 官方下载地址 [所有版本](https://repo.spring.io/release/org/springframework/boot/spring-boot-cli/)

## Profiles
> [Spring Profiles](https://www.baeldung.com/spring-profiles)

> 配置文件(`application.properties或者yml`) 加载顺序 | [官方文档说明](https://docs.spring.io/spring-boot/docs/1.5.9.RELEASE/reference/htmlsingle/#boot-features-external-config-application-property-files)  
>1. 当前Jar/War目录下的/config目录 `./config/`  
>1. 当前目录 `./`  
>1. classpath 里的/config目录 `classpath:/config/`  
>1. classpath 根目录 `classpath:/`  

> 自定义配置文件名就要运行时加参数  
>1. `java -jar myproject.jar --spring.config.name=myproject`  
>1. `java -jar myproject.jar --spring.config.location=classpath:/default.properties,classpath:/override.properties`

- [配置文件的使用](http://www.itwendao.com/article/detail/391009.html)
- [Spring boot配置文件 application.properties](https://www.tuicool.com/articles/veUjQba)
- [SpringBoot常用配置](https://my.oschina.net/wangnian/blog/666641)
- [使用Gradle整合SpringBoot+Vue.js-开发调试与打包](https://segmentfault.com/a/1190000008968295)
- [配置文件加密](https://yq.aliyun.com/articles/182720)

- [自定义配置文件](http://www.cnblogs.com/java-zhao/p/5542154.html)`将应用配置外置并注入成bean`
- [配置文件外置](http://www.cnblogs.com/xiaoqi/p/6955288.html)

> [参考: Spring Boot(五) - 外化配置](https://www.hifreud.com/2017/06/23/spring-boot-05-Externalized-Configuration/)

### 多种配置文件
JVM参数 -D 临时设置配置  
例如： -Dlogging.level.com.xxx.service.impl=DEBUG

#### yml方式
- 单文件多环境 `配置文件 application.yml`
    ```yml
        spring:
        profiles:
            active: development # 选用开发模式
        ---
        spring:
        profiles: development
        # 一系列配置
        ---
        spring:
        profiles: production
        #  一系列配置
    ```
- 多文件存放不同环境配置 `application-{profile}.yml`

- jvm参数指定profile： -Dspring.profiles.active=dev

#### yml和properties结合
- 格式：`application-{profile}.properties`
- 将上面的开发部分，发行部分的配置创建两个配置文件 `application-dev.properties` 和 `application-prod.properties`
- 在主配置文件`application.yml`中指明
    ```yml
        spring:
        profiles:
            active: dev # dev或prod,也可以 common,dev 启用两份
    ```

### 应用配置文件
> 依赖于 `org.springframework.boot:spring-boot-configuration-processor`  

配置对应的实体类
```java
    @Data
    @Component
    @ConfigurationProperties(prefix = "graduate.main")
    public class MainConfig {
        private String delimiter;
    }
```
应用配置类
```java
    @Configuration
    @EnableConfigurationProperties(MainConfig.class)
    public class AutoCustomConfig {
    }
```
application.yml
```yml
graduate:
  main:
    delimiter: ,
```
********************
## Jpa

### spring.jpa.open-in-view
默认值为true，意为： 是否允许事务结束后仍然保持数据库连接，直到整个 HTTP 请求处理完（视图渲染完）才关闭连接并提交/回滚 
```
   spring:
     jpa:
       open-in-view: false
```
- 只要有 Spring MVC 请求进来，不管你是否显式开事务，Spring 都会：
    从连接池借一个连接绑定到当前线程（OpenEntityManagerInViewInterceptor）；
    在整个请求生命周期里一直占着它；
    第一次碰到懒加载属性时，还能再发 SQL（俗称“延长会话”）。
- 请求返回后，连接才关闭。

优点

    控制器/视图层里 Entity对象可以随意点 .getCollection() 不会抛 LazyInitializationException，对新手最友好。

缺点

    连接占用时间变长 → 并发高时连接池容易被吃光；
    事务边界模糊：可能在视图渲染阶段再触发 SQL 并隐式提交，出现“看似没事务却写库”的诡异现象；
    隐藏了懒加载性能问题——N+1 在页面渲染时才爆发，监控难发现。

设置为false是RestController+VO对象返回 最佳的实践，即必须要保证
1. 不能在Controller层把 Entity返回（且这个Entity还定义了外部Entity的集合依赖（一对多）或者显式使用了 FetchType.LAZY ），极易触发 LazyInitializationException。

************************

## Events 
> [Note: Spring Events](/Java/Spring/Spring.md#Events)

配置成异步并使用线程池
```java
    @Configuration
    public class AsynchronousSpringEventsConfig {
        @Bean(name = "applicationEventMulticaster")
        public ApplicationEventMulticaster simpleApplicationEventMulticaster() {
            SimpleApplicationEventMulticaster eventMulticaster = new SimpleApplicationEventMulticaster();

            SimpleAsyncTaskExecutor taskExecutor = new SimpleAsyncTaskExecutor();
            eventMulticaster.setTaskExecutor(taskExecutor);
            return eventMulticaster;
        }
    }
```

***************

## Logging
默认可以通过 application.properties 配置框架的日志,以及应用具体到包和类的日志等级,日志文件等等

> [参考: Spring boot——logback 基础使用篇（一）](https://www.cnblogs.com/lixuwu/p/5804793.html)
> [参考: springboot use logback](https://springframework.guru/using-logback-spring-boot/)`能根据Profile配置,还能写if`  
> [spring boot logging](https://www.baeldung.com/spring-boot-logging)

使用logback时需要配置 logback.xml 或者 logback-spring.xml 建议使用后者

- 思考: 能否不同的包使用不同的pattern [pattern](https://stackoverflow.com/questions/30571319/spring-boot-logging-pattern)
    - 但是不利于后续中间件做日志解析
- 配置 pattern 并引用 MDC `logging.pattern.level=%X{mdcData}%5p`

************************

## Cache
> [Caching Data with Spring](https://spring.io/guides/gs/caching) | [SpringBoot: Caching](https://docs.spring.io/spring-boot/reference/io/caching.html)  

> [Spring Boot Cache使用与整合](https://www.cnblogs.com/morganlin/p/12000223.html)

- `@Cacheable`：表示该方法支持缓存。当调用被注解的方法时，如果对应的键已经存在缓存，则不再执行方法体，而从缓存中直接返回。当方法返回null时，将不进行缓存操作。
    - cacheNames/value：缓存组件的名字，即cacheManager中缓存的名称。
    - key：缓存数据时使用的key。默认使用方法参数值，也可以使用SpEL表达式进行编写。
        - 调用静态方法`获取用户id`拼接进SpEL，从而实现用户缓存隔离
    - keyGenerator： *和key二选一使用*
        - 可以默认构造一个自定义的生成器，从线程上下文获取用户id拼接进去实现用户缓存隔离
    - cacheManager：指定使用的缓存管理器。
    - condition：在方法执行开始前检查，在符合condition的情况下，进行缓存。
    - unless：在方法执行完成后检查，在符合unless的情况下，不进行缓存。
    - sync：是否使用同步模式。若使用同步模式，在多个线程同时对一个key进行load时，其他线程将被阻塞。Spring 4.1引入，**规避缓存击穿**
- `@CachePut`：表示执行该方法后，其值将作为最新结果更新到缓存中。
- `@CacheEvict`：表示执行该方法后，将触发清除同名value和key的缓存。
- `@Caching`：可组合前三个注解

注意缓存的本质是将内存对象序列化到三方缓存（JVM，Redis，文件），使用时再反序列化， 所以需要缓存的接口的参数和响应值都需要实现Serializable接口

************************


## Web模块
### Lisener
#### ServletContextListener
```java
    @WebListener
    public class ApplicationContext implements ServletContextListener {
    @Override
    public void contextInitialized(ServletContextEvent event) {
        System.out.println("Servlet容器初始化");
    }

    @Override
    public void contextDestroyed(ServletContextEvent event) {
        System.out.println("Servlet容器销毁");
    }
    }
```
### 上传下载文件
> 第一种直接上传到应用的webroot或者resources目录下，第二种上传到数据库中，第三种使用ftp。

- [Springboot上传文件](http://www.cnblogs.com/studyCenter/p/6665171.html)
- 上传文件有大小限制，使用如下方法进行配置 [参考博客](http://makaidong.com/studyDetail/11882_45833.html)
    ```java
    @Bean
    public MultipartConfigElement multipartConfigElement() {
        MultipartConfigFactory factory = new MultipartConfigFactory();
        //单个文件最大
        factory.setMaxFileSize("80MB"); //KB,MB
        // 设置总上传数据总大小
        factory.setMaxRequestSize("102400KB");
        return factory.createMultipartConfig();
    }
    ```
    
### 错误页面跳转配置
```java
@Configuration
public class MvcConfig extends WebMvcConfigurerAdapter {
    @Bean
    public EmbeddedServletContainerCustomizer containerCustomizer() {
        return (container -> {
            ErrorPage error401Page = new ErrorPage(HttpStatus.FORBIDDEN, "/403.html");
            ErrorPage error404Page = new ErrorPage(HttpStatus.NOT_FOUND, "/404.html");
            ErrorPage error500Page = new ErrorPage(HttpStatus.INTERNAL_SERVER_ERROR, "/500.html");
            container.addErrorPages(error401Page, error404Page, error500Page);
        });
    }
}
```
### 跨域
> 不同的域名（主机）端口都会导致跨域问题

```java
@Configuration
public class CorsConfig {
    private CorsConfiguration buildConfig() {
        CorsConfiguration corsConfiguration = new CorsConfiguration();
        corsConfiguration.addAllowedOrigin("*"); // 允许任何域名使用
        corsConfiguration.addAllowedHeader("*"); // 允许任何头
        corsConfiguration.addAllowedMethod("*"); // 允许任何方法（post、get等）
        return corsConfiguration;
    }
    @Bean
    public CorsFilter corsFilter() {
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", buildConfig()); // 4
        return new CorsFilter(source);
    }
}
```

### 全局异常处理
1. 新建类 并加类注解 ControllerAdvice 或 RestControllerAdvice（省去方法ResponseBody）
2. 新建方法上添加注解 `ExceptionHandler(Exception.class)` 处理对应异常类型
3. 然后返回值的写法和普通Controller一样, 返回JSON就`ResponseBody`

### Validator
> [Validation with Spring Boot](https://reflectoring.io/bean-validation-with-spring-boot/)

> [SpringBoot接口 - 如何对参数进行校验](https://pdai.tech/md/spring/springboot/springboot-x-interface-param.html)

```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-validation</artifactId>
    </dependency>
```

### Response 
> 全局切面增强

1. 自定义一个切面 `implements ResponseBodyAdvice<Object>`
    1. 重写 supports 和 beforeBodyWrite 并依据 后者的 body和returnType参数自行封装成统一结构
    1. 降低Mvc接口层 `Result<List<Item>>` 等结构，简化为 `List<Item>`， 异常返回可以用全局异常处理成Result结构

[Graceful Response](https://github.com/feiniaojin/graceful-response)

************************
## 测试模块
```java
    // 依赖于Springboot环境的测试类的必备注解
    @RunWith(SpringRunner.class)
    @SpringBootTest

    // 使用内存数据库测试
    @ComponentScan("com.github.kuagncp") // 如果有类没注入需要手动设置扫面
    @RunWith(SpringJUnit4ClassRunner.class)
    @DataJpaTest
```

- 可以使用MockMvc来测试Controller层的代码
- 可以使用MockMvc的SpringSecurity支持来测试安全模块
- 使用 WebIntegraionTest 测试运行中的Web容器
	- 启动嵌入式的Servlet容器来进行测试，下断言
- 使用随机端口启动服务器 配置local.server.port=0
- 使用Selenium来测试HTML页面，模拟浏览器的动作，查看系统运行状态

************************

## 运行和部署

### mvn 运行
- [Spring Boot Maven Plugin](https://docs.spring.io/spring-boot/docs/2.1.9.RELEASE/maven-plugin/run-mojo.html)
- 例如开启远程调试 `mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=8000"`

### 编译打包jar/war
#### war
- 部署为war必须的类，一般在创建项目时选war就会自动生成，选jar就要手动添加
```java
    public class ServletInitializer extends SpringBootServletInitializer {
        @Override
        protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
            return application.sources(DemoApplication.class);
        }
    }
```
- maven： `mvn war` 即可 mvn package -DskipTests
- gradle: `gradle war` 然后 `gradle bootRepackage` 即可

#### jar
- 没有特殊的配置，打包即用 `java -jar app.jar`
    - maven: `mvn package` 即可生成可执行的jar
    - gradle:`gradle jar` 然后 `gradle bootRepackage` 也生成可执行jar

************************

二进制执行的Jar
> [Installing Spring Boot Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.installing)  
> [launch.script](https://github.com/spring-projects/spring-boot/blob/v3.0.6/spring-boot-project/spring-boot-tools/spring-boot-loader-tools/src/main/resources/org/springframework/boot/loader/tools/launch.script#start-of-content)`启动脚本`  

### 构建Docker镜像
> [Official Doc: spring boot docker](https://spring.io/guides/gs/spring-boot-docker/)

#### 手动方式
- 先构建得到war或jar，然后根据dockerfile构建一个镜像
```Dockerfile
    FROM frolvlad/alpine-oraclejdk8:slim
    ADD weixin-1.0.0.war app.war
    ENTRYPOINT ["java","-jar","/app.war"]
```

### 热部署
> [参考: SpringBoot热部署](https://nilzzzz.github.io/2017/11/SpringBoot1/)

> IDE调试时： getBean() 报错cannot be cast to class  is in unnamed module of loader 'app'
[Spring Boot DevTools - RestartClassLoader problem](https://stackoverflow.com/questions/69990029/spring-boot-devtools-restartclassloader-problem)  
spring boot dev tools 实现的 RestarterClassLoader类加载器 和 AppClassLoader 共存，会有一些Bean在Restart类加载器里  
方法： `-Dspring.devtools.restart.enabled=false` 禁用或者移除依赖

### 优雅重启
> [Graceful Shutdown :: Spring Boot](https://docs.spring.io/spring-boot/reference/web/graceful-shutdown.html)  

2.3.0+开始支持，配置时间后暂停接受请求

```yaml
# 开启优雅停机（默认 immediate）
server:
  shutdown: graceful

# 给正在处理的请求留多少时间，默认 30 s
spring:
  lifecycle:
    timeout-per-shutdown-phase: 30s
```

可以注意到开启了graceful之后，会有SpringApplicationShutdownHook在处理资源清理，可以声明以下监听器用来停止业务线程

```java
@Slf4j
@Component
public class GracefulPoolShutdown implements SmartLifecycle {
    @Resource
    @Qualifier(ThreadPoolType.CACHE_POOL)
    private ThreadPoolTaskExecutor cachePool;
    @Resource
    @Qualifier(value = ThreadPoolType.ATTACH_POOL)
    private ThreadPoolTaskExecutor attach;
    @Resource
    @Qualifier(ThreadPoolType.SSE_SCHEDULER)
    private ScheduledExecutorService ssePool;

    private volatile boolean running = true;

    @Override
    public void stop() {
        log.info("stop thread pool");
        List<ThreadPoolTaskExecutor> pools = Arrays.asList(
                cachePool, attach
        );
        // 容器关闭时会回调
        running = false;
        // 1. 并行触发 shutdown（不阻塞）
        pools.forEach(ThreadPoolTaskExecutor::shutdown);
        ssePool.shutdown();

        // 2. 一起等，最长 N 秒
        try {
            long remain = Duration.ofSeconds(30).toMillis();
            boolean isBreak = false;
            for (ThreadPoolTaskExecutor pool : pools) {
                long start = System.currentTimeMillis();
                // await 返回 false 说明超时了，立即进入下一轮
                if (!pool.getThreadPoolExecutor().awaitTermination(remain, TimeUnit.MILLISECONDS)) {
                    isBreak = true;
                    log.info("{} pool timeout", pool.getThreadNamePrefix());
                    break;            // 已经总超时，不再等后面的池
                }
                remain -= (System.currentTimeMillis() - start);
            }

            if (!isBreak) {
                boolean normal = ssePool.awaitTermination(remain, TimeUnit.MILLISECONDS);
                if (!normal) {
                    log.info("sse pool timeout");
                }
            }

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // 3. 还有任务没跑完？强制 shutdownNow
        pools.forEach(v -> v.getThreadPoolExecutor().shutdownNow());
        ssePool.shutdownNow();
        log.info("finish shutdown");
    }

    /* 下面三个方法让 Spring 知道这是一个生命周期组件 */
    @Override
    public boolean isRunning() {
        return running;
    }

    @Override
    public int getPhase() {
        return Integer.MAX_VALUE;
    } // 最后关闭
}
```

运行在Docker或者K8S内时，还需要如下配置。 并且要确保Java进程能收到 15 信号，通过 tini 或者 exec 启动java （shell方式会导致Java进程无法收到kill 15信号）
```dockerfile
ENTRYPOINT /sbin/tini java ${OPTS} -jar -Dspring.profiles.active=${SPRING_PROFILES_ACTIVE} /opt/app.jar
```

```yaml
spec:
  template:
    spec:
      terminationGracePeriodSeconds: 120
```

### 运行性能优化
> [Runtime efficiency with Spring (today and tomorrow)](https://spring.io/blog/2023/10/16/runtime-efficiency-with-spring)

