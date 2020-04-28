---
title: MulticaseRegistry
date: 2019-05-09 20:31:03
tags: 
categories: 
---

**目录 start**

1. [Dubbo 的 Multicast 实现](#dubbo-的-multicast-实现)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Dubbo 的 Multicast 实现
> [参考: Dubbo Multicast 注册中心即相关代码实现](http://www.cnblogs.com/ghj1976/p/5328376.html)  

- 通过 wireshark 抓包， 可以看到大致的流程
    - provider 或者 customer 都是先 register 然后 subscribe

```
    register dubbo://UUUU?application=first-dubbo-provider

    subscribe provider://UUUU?application=first-dubbo-provider&bind.ip=172.17.0.1&bind.port=20880&category=configurators&check=false

    * register consumer://172.17.0.1/org.apache.dubbo.samples.api.GreetingsService?application=first-dubbo-consumer&category=consumers&check=false&default.generic=false&dubbo=2.0.2&generic=false&interface=org.apache.dubbo.samples.api.GreetingsService&methods=sayHi&pid=27381&release=2.7.0&side=consumer&timestamp=1557386946272

    * subscribe consumer://172.17.0.1/org.apache.dubbo.samples.api.GreetingsService?application=first-dubbo-consumer&category=providers,configurators,routers&default.generic=false&dubbo=2.0.2&generic=false&interface=org.apache.dubbo.samples.api.GreetingsService&methods=sayHi&pid=27381&release=2.7.0&side=consumer&timestamp=1557386946272

    // provider 进程开始停止

    unregister dubbo://UUUU?application=first-dubbo-provider

    unregister provider://UUUU?application=first-dubbo-provider&bind.ip=172.17.0.1&bind.port=20880&category=configurators&check=false

    unsubscribe provider://UUUU?application=first-dubbo-provider&bind.ip=172.17.0.1&bind.port=20880&category=configurators&check=false

    unregister dubbo://UUUU?application=first-dubbo-provider

    unregister provider://UUUU?application=first-dubbo-provider&bind.ip=172.17.0.1&bind.port=20880&category=configurators&check=false

    unsubscribe provider://UUUU?application=first-dubbo-provider&bind.ip=172.17.0.1&bind.port=20880&category=configurators&check=false
```
> UUU表示 172.17.0.1:20880/org.apache.dubbo.samples.api.GreetingsService  
> * 是customer, 其他的是 provider

