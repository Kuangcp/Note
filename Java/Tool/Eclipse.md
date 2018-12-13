---
title: Eclipse.md
date: 
tags: 
categories: 
---

**目录 start**
 
1. [Eclipse](#eclipse)
    1. [Eclipse Che](#eclipse-che)
        1. [Install](#install)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Eclipse 

## Eclipse Che
> Next Generation IDE [Github](https://github.com/eclipse/che)|[Official Site](https://www.eclipse.org/che/)

> [Quick Start](https://www.eclipse.org/che/docs/quick-start.html)


### Install 
> [Install By Docker](https://www.eclipse.org/che/docs/docker-single-user.html)

- docker pull eclipse/che
- docker run -ti -v /var/run/docker.sock:/var/run/docker.sock -v /home/kcp/App/eclipse/che:/data eclipse/che start
