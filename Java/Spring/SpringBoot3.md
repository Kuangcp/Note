---
title: SpringBoot3
date: 2024-11-18 14:49:27
tags: 
categories: 
---

💠

- 1. [SpringBoot 3](#springboot-3)
    - 1.1. [VirtualThread](#virtualthread)

💠 2026-03-05 20:29:01
****************************************
# SpringBoot 3
> [Spring Boot 3.0 Release Notes · spring-projects/spring-boot Wiki](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Release-Notes)  

1. JDK最低支持JDK17
1. Java EE相关包名变更 javax -> jakarta
1. httpclient5, hibernate, spring security 


CRaC

> [Effective Scaling of Hot Application Instances with OpenJDK CRaC Help in Containers | Baeldung](https://www.baeldung.com/openjdk-crac-hot-application-instances-scaling)  



## VirtualThread

当开启之后,会对Web容器开启虚拟线程  spring.threads.virtual.enabled true

```java
    @GetMapping("/vtRun")
    public String vtRun() {
        var vtPool = new VirtualThreadTaskExecutor("vt-");
        Object lock = new Object();
        for (int i = 0; i < 10; i++) {
            int taskId = i;
            vtPool.execute(() -> {
                try {
                    synchronized (lock) {
                        System.out.println("Task " + taskId + ": hi (IN LOCK)");
                    }
                    System.out.println("Task " + taskId + ": 2 (AFTER LOCK)");
                } catch (Exception e) {
                    System.out.println("Task " + taskId + " ERROR: " + e);
                    e.printStackTrace();
                }
            });
        }
        return "OK";
    }
```
以上是 SpringBoot3.5 + JDK21.0.10 的环境

> 猜测

虚拟线程在 synchronized 块中会被"固定"（pinned）到 carrier thread 上，无法被调度！
但这里的关键是：多个虚拟线程在尝试进入 synchronized 时，JVM 的 monitor 实现出现了问题！

具体流程：
所有 10 个虚拟线程几乎同时启动
它们都尝试获取 synchronized (lock) 的 monitor
在虚拟线程环境下，JVM 的 monitor 机制（对象头的 markword）可能出现了竞态条件
没有任何一个虚拟线程成功获取到 monitor
所有虚拟线程都卡在了 monitor enter 指令上
这是一个 JVM 层面的 bug 或限制！

而且当出现了这个死锁导致了虚拟线程池里的载体线程都没法卸载的时候，这个服务已经处理不了任何请求了

SpringBoot4.x 就没有这个问题

