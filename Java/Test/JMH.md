---
title: JMH
date: 2020-05-06 01:44:38
tags: 
categories: 
---

**目录 start**

1. [JMH](#jmh)
    1. [简易Demo](#简易demo)
    1. [最佳实践](#最佳实践)

**目录 end**|_2020-05-06 01:45_|
****************************************
# JMH
> [Official Site](http://openjdk.java.net/projects/code-tools/jmh/)  

- [jmh demos](http://hg.openjdk.java.net/code-tools/jmh/file/tip/jmh-samples/src/main/java/org/openjdk/jmh/samples/)

> [参考: Java微基准测试框架JMH](https://www.xncoding.com/2018/01/07/java/jmh.html)  

> [Benchmark comparing serialization libraries on the JVM ](https://github.com/eishay/jvm-serializers)  

## 简易Demo
```java
    @BenchmarkMode(Mode.Throughput)
    @Warmup(iterations = 5)
    @Measurement(iterations = 10, time = 1)
    @Threads(2)
    @OutputTimeUnit(TimeUnit.MILLISECONDS)
    class Target{
        @Benchmark
        public void max(){

        }
    }

    // 运行 JMH
    new Runner(new OptionsBuilder().include(Target.class.getSimpleName()).build()).run();
```

## 最佳实践
