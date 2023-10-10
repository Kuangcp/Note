# 响应式编程
> 规范 [Reactivex](https://reactivex.io/)

> [参考: Reactor模式详解](http://www.blogjava.net/DLevin/archive/2015/09/02/427045.html)

优势：在有高IO处理时间的任务中，响应式比同步命令式能带来更高的吞吐量和扩展性。例如：网关

## Java领域
> [Blog: Reactive Systems in Java](https://www.baeldung.com/java-reactive-systems)

[Project Reactor](http://projectreactor.io/) | [RxJava](https://github.com/ReactiveX/RxJava)


Reactive框架 : RxJava, Reactor, Akka, Kotlin Coroutines & Flow  
Web框架 : Spring WebFlux, Vert.x, Micronaut, Helidon  
DAL层 : Spring Data Reactive (Redis: Lettuce MongoDB: )  
通信层 : RSocket, Reactor Netty, Reactor Aeron, Reactive Dubbo  
消息队列: Reactor Kafka, Reactor RabbitMQ, RocketMQ
