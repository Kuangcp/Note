---
title: Java应用的部署
date: 2018-11-21 10:56:52
tags: 
    - 部署
categories: 
    - Java
---

💠

- 1. [部署运行](#部署运行)
    - 1.1. [打包Jar](#打包jar)
    - 1.2. [打包可执行Jar](#打包可执行jar)
    - 1.3. [打包War](#打包war)
    - 1.4. [打包Docker镜像](#打包docker镜像)
- 2. [配置文件](#配置文件)
    - 2.1. [命令行参数](#命令行参数)
- 3. [Tips](#tips)
    - 3.1. [Java在Linux上的时区问题](#java在linux上的时区问题)
    - 3.2. [容器中Jvm信号及参数接收问题](#容器中jvm信号及参数接收问题)

💠 2024-10-08 15:07:46
****************************************
# 部署运行
> 传统的可执行jar, war 以及Docker镜像

> [参考: JAR 文件揭密](https://www.ibm.com/developerworks/cn/java/j-jar/index.html)
> [参考: maven-assembly-plugin 入门指南](https://www.jianshu.com/p/14bcb17b99e0)

> [Maven 打包部署](/Java/Tool/Maven.md#打包部署)  |  [Gradle 打包部署](/Java/Tool/Gradle.md#打包部署)  

## 打包Jar
1. 平铺式
    - 所有依赖的jar和自身项目class都平铺在目录里
    - 运行main方法类 `java -cp . xxx.Main` 需要将资源所在目录都加入classpath
1. FatJar
    - 所有依赖和自身项目class都打包在一个jar里
    - `java -jar app.jar` 或者 `java -cp app.jar xxx.Main`(没有mainfest文件) 

> 注意
- -cp -jar 混合使用时 -cp 会被忽略

## 打包可执行Jar
> [关于MANIFEST.MF文件](https://blog.csdn.net/baileyfu/article/details/1808023)`这个文件很重要, 如果自己手动配置就需要编写该文件`
_MANIFEST.MF示例_
```yml
    Manifest-Version: 1.0
    Archiver-Version: Plexus Archiver
    Built-By: kcp
    Created-By: Apache Maven 3.5.3
    Build-Jdk: 1.8.0_152
    Main-Class: com.youaishujuhui.minigame.Main
```
- 编译文件       `javac -d *.java `
- 打包字节码成jar `jar -cvf hello.jar com/test/*.*` 
- 打包成可执行jar `jar -cvfm hello.jar mainfest *.*` 
    - 其中 `mainfest` 文本文件： `Main-Class: com.test.Main` 
    - 冒号后一定要有空格，文件最后一行一定留空行

> FatJar 所有的依赖都在一个jar里
- [Maven方式](/Java/Tool/Maven.md#打包部署)

*************************

## 打包War
> 最终将生成的war 放到 tomcat 的 webapps 目录下或者 Jetty的 webapps 目录下

## 打包Docker镜像
> 以一个基础镜像,然后将war放进去构建成一个镜像, 然后推送到服务器上构建容器进行运行

1. 简要概括: from jdk基础镜像, 将jar 复制进去, 设置好 CMD

> [jib](https://github.com/GoogleContainerTools/jib)
> - 结合 Maven Gradle 能更方便的构建 Docker镜像

************************

# 配置文件
> 多目标应用环境的发布, 可以使用Maven 多 Profile; Spring 的多profiles; 环境变量; ...

> 在环境中存储配置
- 通常，应用的 配置 在不同 部署 (预发布、生产环境、开发环境等等)间会有很大差异。这其中包括：
    - 数据库，Memcached，以及其他 后端服务 的配置
    - 第三方服务的证书，如 Amazon S3、Twitter 等
    - 每份部署特有的配置，如域名等

> [参考: 在环境中存储配置](https://12factor.net/zh_cn/config)  
> [从jar包中读取资源文件](https://pdai.tech/md/develop/usage/dev-usage-jar-readfile.html)  


```java
    /**
     * @param path 例如 传入 /redis/lock.lua 意味着： 读取SpringBoot打包成一个UberJar里某子模块的 resources 目录下的 redis/lock.lua 文件。
     * 即使子模块被打包成jar被主模块依赖也不影响，因为文件在classpath的路径都是 /redis/lock.lua
     */
    private static String readFile(String path) {
        try {
            InputStream is = RedisSemaphore.class.getResourceAsStream(path);
            if (Objects.isNull(is)) {
                throw new RuntimeException("NULL");
            }

            BufferedReader br = new BufferedReader(new InputStreamReader(is));
            String s;
            StringBuilder bb = new StringBuilder();
            while ((s = br.readLine()) != null) {
                bb.append(s).append("\n");
            }
            return bb.toString();
        } catch (Exception re) {
            log.error("Load failed {}", path, re);
            return "";
        }
    }
```

## 命令行参数
> [jcommander](https://jcommander.org/)  

************************

# Tips

## Java在Linux上的时区问题
- 表象
    - Docker容器中运行的Linux上时区是正确的, 但是Java应用的时区不对
- 原因 
    - JVM获取时区配置的顺序
    1. 查看 环境变量 TZ 
        - `export TZ=Asia/Shanghai`
    1. /etc/sysconfig/clock 中查找 ZONE 的值
        ```conf
        ZONE="Asia/Shanghai"
        UTC=false
        ARC=false
        ```
    1. /etc/localtime 或者 /usr/share/zoneinfo 
        - `ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`
    - 也可以加JVM参数 `-Duser.timezone=GMT+8`
    - 或者硬编码设置时区

> 快速测试Java获取到的时区
```java
    import java.util.Date;
    import java.time.ZoneOffset;

    public class TimeTest {
        public static void main(String[] args){
            System.out.println(new Date());
            System.out.println(ZoneOffset.systemDefault());
        }
    }
```

## 容器中Jvm信号及参数接收问题
需要避免Java进程为容器中的1号进程，因为会带来很多问题，包括但不限：
- 无法正常接收Linux信号量
- Arthas无法注入
- 无法合理管理派生出的进程生命周期
- JDK中的工具有些也会无法正常使用例如 jstack
