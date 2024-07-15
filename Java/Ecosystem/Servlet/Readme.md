# Servlet容器
> [Comparing Embedded Servlet Containers in Spring Boot](https://www.baeldung.com/spring-boot-servlet-containers)  

## Tomcat
> 更多查看 `Tomcat那些事儿` 公众号  
> [Tomcat目录部署与Context描述文件context.xml ](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=2650859355&idx=1&sn=2122baf040ae337dba90201a48b4e11c&chksm=f1329888c645119eec4473e11beaf988c48ce02c52151502086595de59b65dd4bd7cf129530e&scene=21#wechat_redirect)
> | [Tomcat配置文件解析与Digester](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=2650859293&idx=1&sn=3c017b2675bb59fda8ae037b7a1e6cb4&chksm=f13298cec64511d8183a23f1b3110bc6b65e8742c6e76391a51c552d86c0bc81a34fab8d0a60&scene=21#wechat_redirect)  
> | [Servlet到底是单例还是多例你了解吗？](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=401278436&idx=1&sn=7d28750b7cff1f706efb82c7fcaa73c5&scene=21#wechat_redirect)
> | [Tomcat类加载器以及应用间class隔离与共享 ](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=2650859298&idx=1&sn=8856375f2268fc33a6bb3fbc6932eca7&chksm=f13298f1c64511e77ef1d77d28272840ca56f62da6e11928c78827e8ec53f937f812a4b49aa0&scene=21#wechat_redirect)  
> | [啥，Tomcat里竟然还有特权应用? ](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=2650859476&idx=1&sn=8be7a37b59a5d167998f6695a1606d39&chksm=f1329807c6451111d2a1c379221655dc87dd105b067f894bfb202d1f9f283bad310a5cdc2277&scene=21#wechat_redirect)
> | [你了解JMX在Tomcat的应用吗?](https://mp.weixin.qq.com/s?__biz=MzI3MTEwODc5Ng==&mid=401135587&idx=1&sn=610950fda2eceb3683a9fe45078f1a83&scene=21#wechat_redirect)

************************

> [参考: Jetty和Tomcat的选择：按场景而定](http://www.open-open.com/lib/view/open1322622094390.html)
> [详解web容器 - Jetty与Tomcat孰强孰弱](https://developer.aliyun.com/article/441105)

```
    一个简单项目, 就是index.jsp 里面放了个 Hello 字符串
    经过对比 8.5.29 jetty 9.2 
    启动时间 jetty花费时间是Tomcat2倍
    启动后内存 Jetty480M Tomcat300M
    1000并发 20000总量 
    Tomcat涨到 460M 第二次480M  连续5次后上660M了 10次900M 最长时间时而220ms 时而 70ms
    Jetty涨到770M 第二次压测直接上900M了 十次后也是900M 最长响应时间稳定在 220ms
```

## Undertow
> [Official Site](http://undertow.io/)  
