---
title: JMH
date: 2020-05-06 01:44:38
tags: 
categories: 
---

💠

- 1. [JMH](#jmh)
    - 1.1. [简易Demo](#简易demo)
    - 1.2. [最佳实践](#最佳实践)

💠 2024-02-22 14:23:17
****************************************
# JMH
> [Official Site](http://openjdk.java.net/projects/code-tools/jmh/)  

- [JMH 官方示例代码](http://hg.openjdk.java.net/code-tools/jmh/file/tip/jmh-samples/src/main/java/org/openjdk/jmh/samples/)

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
