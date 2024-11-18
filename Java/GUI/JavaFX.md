---
title: JavaFX
date: 2024-11-14 16:30:00
tags: 
    - GUI
categories: 
---

💠

- 1. [JavaFX](#javafx)

💠 2024-11-18 14:31:55
****************************************
# JavaFX
> [OpenJFX](https://wiki.openjdk.java.net/display/OpenJFX) | [official site](https://openjfx.io)

> [JavaFX Tutorial](https://jenkov.com/tutorials/javafx/index.html)  
- [xJavaFxTool](https://gitee.com/xwintop/xJavaFxTool)`基于JavaFX的工具集`
- [Adding HTML Content to JavaFX Applications](https://docs.oracle.com/javafx/2/webview/jfxpub-webview.htm)

************************

> [jjenkov/javafx-examples](https://github.com/jjenkov/javafx-examples)  

1. 下载对应系统的SDK，不是jmod[JavaFX - Gluon](https://gluonhq.com/products/javafx/)  
1. IDE中调试时增加对应JVM参数 --module-path /path/to/javafx-sdk-17.0.13/lib/ --add-modules=javafx.controls,javafx.fxml
1. [Maven 插件配置打包单个可执行Jar](/Java/Tool/Maven.md#assembly)  
1. 运行： java --module-path /path/to/javafx-sdk-17.0.13/lib/ --add-modules=javafx.controls,javafx.fxml  -jar  target/javafx-examples-0.0.1-SNAPSHOT.jar
