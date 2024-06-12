# Jetty

> [Jetty官网](http://www.eclipse.org/jetty/)  
> [jetty-examples](https://github.com/jetty/jetty-examples)  



[参考: Jetty使用教程（一）——开始使用Jetty ](http://www.cnblogs.com/yiwangzhibujian/p/5832597.html)

### 配置
_自身log配置_
> [相关](http://zetcode.com/java/jetty/logging/)
_resources/jetty-logging.properties_ 内容如下开启DEBUG
```conf
    org.eclipse.jetty.util.log.class=org.eclipse.jetty.util.log.StrErrLog
    org.eclipse.jetty.LEVEL=DEBUG
    jetty.logs=logs
```

> [参考: Jetty和Tomcat的选择：按场景而定](http://www.open-open.com/lib/view/open1322622094390.html)

```
    一个简单项目, 就是index.jsp 里面放了个 Hello 字符串
    经过对比 8.5.29 jetty 9.2 
    启动时间 jetty花费时间是Tomcat2倍
    启动后内存 Jetty480M Tomcat300M
    1000并发 20000总量 
    Tomcat涨到 460M 第二次480M  连续5次后上660M了 10次900M 最长时间时而220ms 时而 70ms
    Jetty涨到770M 第二次压测直接上900M了 十次后也是900M 最长响应时间稳定在 220ms
```