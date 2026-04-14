---
title: Java21
date: 2026-03-11 10:53:50
tags: 
categories: 
---

💠

- 1. [Java21](#java21)
- 2. [虚拟线程 Virtual Threads](#虚拟线程-virtual-threads)
    - 2.1. [Pinning](#pinning)
    - 2.2. [观测](#观测)
    - 2.3. [兼容性问题](#兼容性问题)
    - 2.4. [实践](#实践)

💠 2026-03-11 11:00:43
****************************************
# Java21

# 虚拟线程 Virtual Threads

> [Virtual Threads](https://openjdk.org/jeps/444) 19预览 21Release | 来源于 [OpenJDK: Loom](https://wiki.openjdk.org/display/loom)`项目目标高吞吐量，轻量级并发模型，结构化并发&调度`  
> [Virtual Threads Oracle Doc](https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html#GUID-DC4306FC-D6C1-4BCC-AECE-48C32C1A8DAA)  

> [JEP 491: Synchronize Virtual Threads without Pinning](https://openjdk.org/jeps/491)`JDK24修复了pinned问题`  

类似于GMP的模型，将 Virtual Threads 调度在 carrier Threads 上执行, 执行时先挂载到平台线程上，遇到IO阻塞时从平台线程上卸载 unmount

*试用总结：如果要引入生产，需要关注整个JEP的文档，调试确认细节后才能使用，不然就会陷入到各种诡异的问题上。*

特性：
- 依赖一个公用的ForkJoin线程池执行任务 即 不推荐执行CPU密集型任务，只建议用来执行io密集类任务（21对有可能阻塞cpu的api都加上了特定处理代码）从而提高吞吐量
- 正常线程内代码无法感知 协程内代码的异常，反之也是一样，线程和协程间的局部变量也是隔离的
- 协程的 栈帧 存储在堆内存中，为了规避大量协程导致的栈溢出

> [虚拟线程：Java的新利器？](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247538915&idx=1&sn=b9b6a303a79cea5225e0d445e10eddc8&scene=58&subscene=0)
> [Java19 正式 GA！看虚拟线程如何大幅提高系统吞吐量 ](https://mp.weixin.qq.com/s/yyApBXxpXxVwttr01Hld6Q)  
> [虚拟线程 - VirtualThread源码透视 ](https://www.cnblogs.com/throwable/p/16758997.html)

> ThreadLocal

- JDK 21 的实现：虚拟线程（VirtualThread）在 JVM 内部依然是 java.lang.Thread 的子类。JDK 为每个虚拟线程都保留了独立的 ThreadLocal 存储。
- 上下文拷贝：当虚拟线程在不同的平台线程（Carrier Thread）之间切换（Mount/Unmount）时，JVM 会自动装载和卸载该虚拟线程对应的 ThreadLocal 变量。
- 但是使用ScopedValue替代ThreadLocal会更合适

>> 注意一些过渡时期的框架，会出现线程池的线程名字有VirtualThread的字样，但它又**不是虚拟线程**（虚晃一枪），只看 Thread.isVirtual 返回true 才是虚拟线程。

常规的jstack visualvm只能看到普通的线程（虚拟线程的载体）

- JDK Mission Control (JMC) & JFR (推荐)：
    - 这是观测虚拟线程的唯一权威工具。通过 Java Flight Recorder (JFR)，你可以抓取 jdk.VirtualThreadStart 和 jdk.VirtualThreadPinned 事件。
    - 监控点：查看 Pinned Virtual Thread 事件。如果这个事件频繁发生，说明你的代码在物理上阻塞了内核线程。

- Java Management Extensions (JMX)：
    - JDK 21 引入了新的 MBean。通过 java.lang:type=Threading，你可以获取虚拟线程的计数：
    - ThreadCount: 平台线程数。
    - VirtualThreadCount: 当前活跃的虚拟线程数（对于你的 1000 并发任务，这里应该显示 1000+）。

- Micrometer & Prometheus：
    - 如果你使用 Spring Boot 3.2+，只需引入 micrometer-registry-prometheus。
    - 指标名：jvm.threads.virtual.started (已启动数) 和 jvm.threads.virtual.active (当前活跃数)。

***

虚拟线程宣传的“不阻塞”是指逻辑上的非阻塞（I/O 等待时释放 CPU），但在以下两种场景下，真实的物理阻塞（Pinning） 仍会发生：

> A. 线程锚定 (Pinning) —— 最危险的阻塞
- 当虚拟线程在执行以下操作时，它会“卡死”在底层的载体线程（Carrier Thread）上，导致载体线程无法去处理其他虚拟线程：
    - 在 synchronized 块或方法中执行 I/O（如调用大模型 API、查询数据库）。
    - 调用了本地方法 (JNI)。

    后果：如果你有 1000 个虚拟线程，但载体线程池（通常等于 CPU 核心数）全部被 Pin 住了，你的整个应用会完全失去响应，即使内存还有很多。
    对策：将所有的 synchronized 替换为 ReentrantLock。

> B. 调度器耗尽 (Scheduler Exhaustion)
- 虚拟线程默认运行在 ForkJoinPool 上。如果你的 Node 节点里执行了大量的 计算密集型任务（如复杂的 JSON 解析、加解密），而不是 I/O 等待，那么虚拟线程会长时间占用载体线程。

    后果：吞吐量下降，因为载体线程没机会切换到其他任务。


## Pinning

当虚拟线程处于某种特定状态时，它无法从平台线程上卸载。此时，一旦虚拟线程发生阻塞，底层的平台线程也会被同步阻塞。

你可以通过在启动参数中添加以下指令，在控制台直接打印出发生“物理阻塞”的代码位置：
```bash
    # 当虚拟线程固定在载体线程上时，打印堆栈轨迹
    -Djdk.tracePinnedThreads=full
    # 或
    -Djdk.tracePinnedThreads=short
```

造成 Pinning 的两个主要场景：
- 进入 synchronized 代码块或方法时：目前 JVM 无法在 synchronized 内部卸载虚拟线程（因为 Monitor 对象锁是与操作系统线程深度绑定的）。
- 执行本地方法 (Native Method) 时：如果通过 JNI 调用了 C/C++ 代码，虚拟线程也无法卸载。

后果：如果大量虚拟线程在 Pinning 状态下阻塞，会导致底层的平台线程池（Carrier Pool）被耗尽，整个应用的吞吐量骤降，甚至发生死锁。


## 观测

标准 jstack 只能看到两类线程：

- 平台线程（无论等待/运行）	✅ 总是可见
- 已挂载（mounted）的虚拟线程	✅ 通过 carrier 可见
- 已卸载（unmounted）的虚拟线程	❌ 完全不可见

```sh
    # JDK 21+ 的完整线程 dump，包含所有虚拟线程（含 unmounted 的）
    jcmd <pid> Thread.dump_to_file -format=json /tmp/vt-full-dump.json

    # 或者 text 格式
    jcmd <pid> Thread.dump_to_file -format=text /tmp/vt-full-dump.txt
```

观测指标检查清单

    jvm.threads.live：观察平台线程是否保持稳定（不应随业务并发增加）。
    jvm.gc.memory.allocated：虚拟线程在堆上分配栈，高并发下 Minor GC 频率会上升。
    接口响应时间 (P99)：如果 P99 极高，检查是否因为虚拟线程过多导致了 OS 文件句柄 (ulimit) 竞争。


## 兼容性问题
虽然 JDK 21 正式发布前很多大厂做了适配，但以下三类库在特定版本下仍是“重灾区”：
数据库驱动（关键点：Socket 读写）：
MySQL Connector/J：直到 8.0.33 之前，其内部大量使用了 synchronized。如果你使用的是 5.x 版本或旧版 8.x，在高并发虚拟线程下必崩。
Oracle JDBC：旧版驱动在处理网络 LOB 字段或加密传输时，存在 synchronized 块包裹 I/O 操作的情况。

日志框架（老版本）：
Logback / Log4j2：虽然它们现在都支持异步日志，但如果你配置了 ConsoleAppender（控制台输出），底层依然会撞上 System.out 的锁。此外，某些旧版的 FileAppender 在写文件时也存在 synchronized 导致的 Pinning。

加解密与安全库：
Bouncy Castle：这个库在执行某些复杂的加密算法时，内部会有大量的 synchronized 静态锁，用来初始化算法引擎。

本地缓存：
Ehcache 2.x：内部并发控制大量依赖内置锁。相比之下，Caffeine 对虚拟线程非常友好，因为它底层几乎全都是基于 AQS 和原子类（Unsafe/VarHandle）。

## 实践

```sh
    # 虚拟线程调度优化
    -Djdk.virtualThreadScheduler.parallelism=32        # 默认 CPU 核心数，可适当增大
    -Djdk.virtualThreadScheduler.maxPoolSize=256       # 最大载体线程数
    -Djdk.virtualThreadScheduler.minRunnable=16        # 最小可运行线程

    # Pinning 检测（生产用 warning，调试用 full）
    -Djdk.tracePinnedThreads=short

    # 启用虚拟线程的 ThreadLocal 优化（JDK 21 默认开启）
    -Djdk.virtualThreadScheduler.timedPermitForkJoinPool=true
```

```java
    // 自定义虚拟线程工厂（带监控）
    @Bean
    public ExecutorService virtualThreadExecutor() {
        return Executors.newThreadPerTaskExecutor(
            Thread.ofVirtual()
                .name("agent-vt-", 0)
                .inheritInheritableThreadLocals(false)  // 避免 ThreadLocal 泄漏
                .uncaughtExceptionHandler((t, e) -> 
                    log.error("Virtual thread failed: {}", t.getName(), e))
                .factory()
        );
    }
    // HTTP Client 使用虚拟线程友好配置
    @Bean
    public HttpClient httpClient() {
        return HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(10))
            .executor(Executors.newVirtualThreadPerTaskExecutor())  // 内部也用 VT
            .build();
    }

    // 监控和告警
    @Component
    public class VirtualThreadMonitor {
        
        @Scheduled(fixedRate = 60000)
        public void checkHealth() {
            // 监控载体线程状态
            ThreadMXBean threadBean = ManagementFactory.getThreadMXBean();
            long[] threadIds = threadBean.getAllThreadIds();
            
            long virtualThreads = Arrays.stream(threadIds)
                .mapToObj(id -> {
                    try {
                        return threadBean.getThreadInfo(id);
                    } catch (Exception e) {
                        return null;
                    }
                })
                .filter(info -> info != null && info.getThreadName().startsWith("agent-vt"))
                .count();
                
            // 告警：如果载体线程全部繁忙且虚拟线程堆积
            if (virtualThreads > 10000) {
                alert("High virtual thread count: " + virtualThreads);
            }
        }
    }
```
