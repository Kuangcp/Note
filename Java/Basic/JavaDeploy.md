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
        - 1.4.1. [基础镜像的选择](#基础镜像的选择)
- 2. [配置文件](#配置文件)
    - 2.1. [命令行参数](#命令行参数)
- 3. [安全加固](#安全加固)
    - 3.1. [代码混淆](#代码混淆)
    - 3.2. [加密Class](#加密class)
    - 3.3. [花指令](#花指令)
- 4. [Tips](#tips)
    - 4.1. [Java在Linux上的时区问题](#java在linux上的时区问题)
    - 4.2. [容器中Jvm信号及参数接收问题](#容器中jvm信号及参数接收问题)

💠 2026-08-31 11:13:45
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

1. 简要概括: from jdk基础镜像, 将jar 复制进去, 设置好 ENTRYPOINT

> [jib](https://github.com/GoogleContainerTools/jib)
> - 结合 Maven Gradle 能更方便的构建 Docker镜像

### 基础镜像的选择
首先是 musl libc(alpine) 和 glibc 两大阵营。

早年间（Docker 刚流行时），大家都*迷恋 Alpine 那只有 5MB 的极致体积*。但随着微服务进入深水区，Java 开发者发现 Alpine 带来了三个难以忍受的“隐形成本”

1. musl-libc 的性能天花板：
   Java 虚拟机（JVM）本身是一个极度依赖底层 C 库（尤其是线程調度、内存分配 malloc/free）的复杂软件。标准 JDK 都是基于 glibc 开发和优化的。Alpine 的 musl-libc 为了追求代码极简，在高并发的锁竞争、高频的堆内存碎片整理、以及底层加密算法（JCE）的实现一致性（PKCS5Padding问题）和寻址性能，明显弱于 glibc。
2. 隐藏的 1.8S/2.8S 崩溃大坑（DNS 解析缺陷）：
   这是 Alpine 最著名的生产事故来源。musl-libc 的 DNS 解析不支持 search 域的并发查询，在高并发调用内网 Java 接口（比如你调用内网的 Java 服务的接口）时，有概率触发 DNS 超时假死，导致服务莫名其妙卡顿。
3. 排查工具极其匮乏（可以通过二次构建镜像解决）：
   当你想线上排查问题时，Alpine 默认连 bash、curl、top都没有，你必须进去现装。

如果不用 Alpine，直接用传统的 ubuntu:latest 镜像又太胖了（动辄 100M+，包含大量无用的音视频驱动、帮助文档），会拉低 CI/CD 部署抽取的效率。
目前一线大厂和开源社区最推荐以下两种平衡了「性能（glibc）」与「体积（精简）」的黄金发行版：

> 1. Debian-slim 系列（目前行业绝对的主流 ⭐⭐⭐⭐⭐）
像官方的 OpenJDK 镜像、或者 Spring 官方推荐的 eclipse-temurin 镜像 [eclipse-temurin](https://hub.docker.com/_/eclipse-temurin/tags?name=8-jdk-focal)，现在默认的后缀都是 -debian-slim。

* 核心优势：它是 Debian（Ubuntu 的母体）的官方极简版，去掉了所有不必要的包，但保留了最纯正、高性能的 glibc 库。
* 体积与性能：镜像大小只有 30MB ~ 40MB 左右。在具备 Alpine 级小体积的同时，拥有 100% 完整的标准 JDK 密码学和垃圾回收性能。

> 2. Google Distroless 镜像（极致安全与性能）
谷歌开源的专为运行程序设计的镜像。

* 核心优势：里面只有你的运行环境（如 Java 8 或 Java 17）和最基础的 glibc 库，甚至连 Shell（/bin/sh）都直接干掉了，从根本上杜绝了黑客入侵和安全漏洞。
* 体积：体积同样极小，但运行的是纯正的 glibc，性能拉满。

- [内存管理区别](/Linux/Base/LinuxBase.md#内存管理)

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
# 安全加固
主流方案有：class混淆;加密class;花指令； 但是总结下来混淆是投入产出比最高的方案。


## 代码混淆
引入低成本且影响小，防护效果好（因为复杂业务本身难懂，混淆后更难理解了），并引申出别的用途（压缩apk大小😅）

> [obfuscation - Best Java obfuscator? - Stack Overflow](https://stackoverflow.com/questions/2537568/best-java-obfuscator)  
> [Open Source Obfuscators in Java](https://java-source.net/open-source/obfuscators)  

工具列表

> [Allatori Java Obfuscator - Professional Java Obfuscation](https://allatori.com/)  
> [ProGuard Manual: Usage | Guardsquare](https://www.guardsquare.com/manual/configuration/usage)  
> [jar-analyzer/class-obf](https://github.com/jar-analyzer/class-obf)  

## 加密Class
难点在于即使自定义了类加载器，加载进JVM运行的时候内存上仍是明文字节，还是有手段dump到真实的class

> [encryption - How can you protect/encrypt your Java classes? - Stack Overflow](https://stackoverflow.com/questions/4257027/how-can-you-protect-encrypt-your-java-classes)  

> [Cracking Java byte-code encryption | InfoWorld](https://www.infoworld.com/article/2171002/cracking-java-byte-code-encryption.html)  

> [serengil/encrypted-class-loader: Enabling to run encrypted java classes](https://github.com/serengil/encrypted-class-loader)  

## 花指令
> [花指令 - CTF Wiki](https://ctf-wiki.org/reverse/obfuscate/junk-code/)  
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
- 无法正常接收Linux信号量，也就无法做Graceful Shutdown。
- Arthas无法注入
- 无法正常管理派生出的进程生命周期
- JDK中的工具有些也会无法正常使用例如 jstack

可以通过 tini 来解决问题， 但是需要注意使用不同基础镜像时 各个shell的默认行为差异。
> alpine 系列 默认ash

`ENTRYPOINT /sbin/tini java ${OPTS} -jar -Dspring.profiles.active=${SPRING_PROFILES_ACTIVE} /opt/app.jar`

可以发现ash很简洁，因为exec自动优化（单命令，无管道无分号无逻辑与）会自动追加 exec。如果继续按这个写法，在换了dash作为默认shell的镜像时会报错：  
dash对参数扩展的解析极其严苛（JVM参数 报 invalid option -- 'X'）：dash 在宏展开替换 ${OPTS} 的时候，如果外面没有硬性的中括号 [] 数组保护，它在切分字符串空格时，由于它不支持 ash 的某些非标准语法扩展，会产生错误的参数边界划分，从而导致 -Xms 被当成 tini 自己的参数传了过去，引发报错。

**最佳实践**: 使用 focal的声明方式 方括号参数+exec顶替sh进程。 避免系统方言带来的差异

> eclipse-temurin debian-focal 系列镜像 默认dash。

`ENTRYPOINT ["/usr/bin/tini", "--", "sh", "-c", "exec java ${OPTS} -jar -Dspring.profiles.active=${SPRING_PROFILES_ACTIVE} /opt/app.jar"]`

