---
title: Eclipse
date: 2018-12-17 21:30:46
tags: 
    - Eclipse
categories: 
    - Java
    - IDE
---

**目录 start**

1. [Eclipse](#eclipse)
    1. [Mars](#mars)
    1. [Eclipse Che](#eclipse-che)
        1. [Install](#install)

**目录 end**|_2020-06-04 19:41_|
****************************************
# Eclipse 
## Mars

* 这里的Tomcat是使用了你所导入的必要执行文件，但是运行的必要配置文件在eclipse Server项目里另有一份
* 而且运行时也是使用这份配置文件，这样的结果是可以使用一份Tomcat目录，在eclipse配置运行多个Tomcat
* 但是奇怪的是 访问不了Tomcat主页即：localhost:8080 所以也就不能管理Tomcat 查看运行状态

资源下载 archive.eclipse.org/eclipse/downloads/ 

*********************

## Eclipse Che
> Next Generation IDE [Github](https://github.com/eclipse/che)|[Official Site](https://www.eclipse.org/che/)

> [Quick Start](https://www.eclipse.org/che/docs/quick-start.html)


### Install 
> [Install By Docker](https://www.eclipse.org/che/docs/docker-single-user.html)

- docker pull eclipse/che
- docker run -ti -v /var/run/docker.sock:/var/run/docker.sock -v /home/kcp/App/eclipse/che:/data eclipse/che start

