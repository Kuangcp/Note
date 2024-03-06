## OOM 
> 注意OOM并不代表Java进程一定会退出，如果导致OOM的地方能被catch，且泄漏点能随着这次任务的终止而可回收的话，JVM将继续正常运行。  
> [Why JVM can recovery from OOM Java heap space by itself](https://stackoverflow.com/questions/72865015/why-jvm-can-recovery-from-oom-java-heap-space-by-itself)

例如最简单的案例
```java
    public static void main(String[] args) {
        try {
            List<byte[]> data = new ArrayList<>();
            while (true) {
                try {
                    TimeUnit.MILLISECONDS.sleep(100);
                } catch (InterruptedException e) {
                    log.error("", e);
                }
                log.info("size={}", data.size());
                data.add(new byte[1024 * 1024]);
            }
        } catch (Throwable e) {
            log.error("", e);
        }

        while (true) {
            try {
                TimeUnit.MILLISECONDS.sleep(500);
            } catch (InterruptedException e) {
                log.error("", e);
            }
            log.info("do something");
        }
    }
```

又或者常见的SpringMVC服务
```java
    @GetMapping("/oom")
    public String oom() {
        List<byte[]> data = new ArrayList<>();
        while (true) {
            try {
                TimeUnit.MILLISECONDS.sleep(100);
            } catch (InterruptedException e) {
                log.error("", e);
            }
            log.info("size={}", data.size());
            data.add(new byte[1024 * 1024]);
        }
    }
```

注意 `org.springframework.web.servlet.DispatcherServlet` 中的 `doDispatch` catch了Error也包装成了Exception，方便统一异常处理器。  
这只会导致Tomcat的NIO线程终止了这次请求，局部变量 data 就可以回收掉了，整个服务仍正常进行，只是在快要OOM时高频的GC影响了系统的吞吐量而已。

```java
    catch (Exception ex) {
        dispatchException = ex;
    }
    catch (Throwable err) {
        // As of 4.3, we're processing Errors thrown from handler methods as well,
        // making them available for @ExceptionHandler methods and other scenarios.
        dispatchException = new NestedServletException("Handler dispatch failed", err);
    }
```

### Heap space OOM
异常信息：

java.lang.OutOfMemoryError: Java heap space
java.lang.OutOfMemoryError: Requested array size exceeds VM limit

### Metaspace OOM
[一次Metaspace OutOfMemoryError问题排查记录](https://juejin.cn/post/7114516283290288158)`很多GeneratedMethodAccessor类`

原理理解比较复杂，但定位和解决问题会比较简单，经常会出问题的几个点有 Orika 的 classMap、JSON 的 ASMSerializer、Groovy动态加载类等，基本都集中在 反射、Javasisit字节码增强、CGLIB动态代理、OSGi自定义类加载器等技术点上
> [参考: Metaspace 之一：Metaspace整体介绍](https://www.cnblogs.com/duanxz/p/3520829.html)  


https://heapdump.cn/article/1924890
https://heapdump.cn/article/54786?from=pc
https://heapdump.cn/article/2152817

-XX:+TraceClassLoading -XX:+TraceClassUnloading
-verbose:class

https://developer.aliyun.com/article/780535

https://www.mastertheboss.com/java/solving-java-lang-outofmemoryerror-metaspace-error/#google_vignette

https://javakk.com/805.html
https://www.dongcb.com/818.html

https://juejin.cn/post/7114516283290288158


### Compressed Class Space OOM

### Direct Memory OOM 

[Netty堆外内存泄露排查盛宴](https://tech.meituan.com/2018/10/18/netty-direct-memory-screening.html)
