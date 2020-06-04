---
title: Jacoco
date: 2018-12-17 21:27:14
tags: 
    - CI
categories: 
    - Java
    - Blog
---
**目录 start**

1. [Jacoco](#jacoco)
    1. [安装](#安装)
        1. [Maven插件方式](#maven插件方式)
        1. [Jenkins集成](#jenkins集成)

**目录 end**|_2020-06-04 19:41_|
****************************************

# Jacoco
> 一款Java平台的代码覆盖率工具 

## 安装

### Maven插件方式
1. 添加插件

```xml
    <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.2</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals>
              <goal>prepare-agent</goal>
            </goals>
          </execution>
          <execution>
            <id>report</id>
            <phase>prepare-package</phase>
            <goals>
              <goal>report</goal>
            </goals>
          </execution>
          <execution>
            <id>post-unit-test</id>
            <phase>test</phase>
            <goals>
              <goal>report</goal>
            </goals>
            <configuration>
              <!-- Sets the path to the file which contains the execution data. -->
              <dataFile>target/jacoco.exec</dataFile>
              <!-- Sets the output directory for the code coverage report. -->
              <outputDirectory>target/jacoco-ut</outputDirectory>
            </configuration>
          </execution>
        </executions>
        <configuration>
        </configuration>
      </plugin>
```

2. 执行: `mvn test`

### Jenkins集成
> [Official Doc](https://wiki.jenkins.io/display/JENKINS/JaCoCo+Plugin)
