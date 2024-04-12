---
title: Practice
date: 2024-03-06 14:10:23
tags: 
categories: 
---

💠

- 1. [问题实践](#问题实践)
    - 1.1. [IDEA调优](#idea调优)
    - 1.2. [FD泄漏： Unable to Open Socket File](#fd泄漏-unable-to-open-socket-file)
        - 1.2.1. [查找JVMSocket泄漏](#查找jvmsocket泄漏)

💠 2024-04-12 17:19:59
****************************************
# 问题实践
## IDEA调优
```conf
    -server
    -Xms1700m  # 最小堆
    -Xmx1700m  # 最大堆 配成一样是为了避免扩容
    -XX:MetaspaceSize=350m # 只是一个阈值, 达到该阈值才进行 GC
    -XX:MaxMetaspaceSize=350m # 最大值

    -Xnoclassgc 
    -Xverify:none # 不进行字节码校验
    -XX:+AggressiveOpts # 激进式优化

    -XX:ReservedCodeCacheSize=320m # IDEA JIT 缓存
```

> [参考: Java’s -XX:+AggressiveOpts: Can it slow you down?](https://www.opsian.com/blog/aggressive-opts/)  
> [参考: JVM参数MetaspaceSize的误解 ](https://mp.weixin.qq.com/s/jqfppqqd98DfAJHZhFbmxA?)

************************

## FD泄漏： Unable to Open Socket File
> [jmap Error “Unable to Open Socket File”](https://www.baeldung.com/linux/jmap-unable-to-open-socket-file-heap-dump)
- 不是同用户及用户组 uid和gid
- 目标JVM不健康
- 目标JVM使用了`-XX:+DisableAttachMechanism`JVM参数
- 执行工具的JVM和目标JVM不是同一个版本（最好保持一致，如果版本相差过大，内存布局设计不一样，就会无法正常解析结果）
- /tmp 目录下无法创建命令使用的临时文件，或是来不及使用就被`systemd-tmpfiles`清理了 `/tmp/.java_pidXXX`

### 查找JVMSocket泄漏
- [一次由于网络套接字文件描述符泄露导致线上服务事故原因的排查经历](https://www.wangbo.im/posts/a-production-bug-leaking-sockets-fd-reproducing-practice/)
- `strace -t -T -f -p pid -e trace=network,close -o strace.out`
    - 尝试找到创建socket并没有关闭socket的线程号， 然后进制转换后查看jstack找到线程持有栈关联到相关代码

- 处理过的案例： [Apache DolphinScheduler V1.3.6 channel 未关闭导致socket泄漏](https://github.com/apache/dolphinscheduler/blob/d21eb7b1809aa513ced920d5d08575502bde8911/dolphinscheduler-server/src/main/java/org/apache/dolphinscheduler/server/worker/processor/TaskCallbackService.java#L156)
    - 单纯从服务器现场看只能看到worker对master建立了大量socket，而且fd的特殊性无法判断socket真实建立时间
    - 从worker和master的内存Dump入手，查看大量的socket（出问题时已4w+）会和哪些对象数量异常增多有关
    - 排查可能异常的对象（优先看Netty和Socket有关的对象），对比上下文代码（优先关注对象创建和销毁处代码），最终定位到泄漏对象为NettyRemoteChannel，以及上述泄漏点
    - 处理方式： remove前先关闭Channel

