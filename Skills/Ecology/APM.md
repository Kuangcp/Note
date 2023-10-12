
💠

- 1. [APM](#apm)
    - 1.1. [SkyWalking](#skywalking)
    - 1.2. [CAT](#cat)

💠 2023-10-12 11:48
****************************************
# APM
> Application performance monitor tool

SkyWalking、Zipkin、Pinpoint、CAT

## SkyWalking
> [Official Site](http://skywalking.apache.org/)  | [Downloads](https://skywalking.apache.org/downloads/)]

[server](https://hub.docker.com/r/apache/skywalking-oap-server) | [ui](https://hub.docker.com/r/apache/skywalking-ui)

```
docker run --name oap -p 12340:1234 -p 11800:11800 -p 12800:12800  -d apache/skywalking-oap-server:8.3.0-es6
docker run --name oap-ui -p 8080:8080 -d -e SW_OAP_ADDRESS=http://192.168.7.54:12800 apache/skywalking-ui
```

应用启动 java -javaagent:/opt/apache-skywalking-apm-bin/agent/skywalking-agent.jar -Dskywalking.agent.service_name=xxxtest -Dskywalking.collector.backend_service=127.0.0.1:11800 -jar application.jar

## CAT
> [陆金所 CAT 优化实践](https://www.infoq.cn/article/XvGZcW312MdatCKFMR8b)

> [Github: cat-docker](https://github.com/lghuntfor/cat-docker)  
