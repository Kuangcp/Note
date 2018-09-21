`目录 start`
 
- [Jetty](#jetty)
    - [配置](#配置)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Jetty


[参考博客: Jetty使用教程（一）——开始使用Jetty ](http://www.cnblogs.com/yiwangzhibujian/p/5832597.html)

## 配置
_自身log配置_
> [相关](http://zetcode.com/java/jetty/logging/)
_resources/jetty-logging.properties_ 内容如下开启DEBUG
```conf
    org.eclipse.jetty.util.log.class=org.eclipse.jetty.util.log.StrErrLog
    org.eclipse.jetty.LEVEL=DEBUG
    jetty.logs=logs
```

