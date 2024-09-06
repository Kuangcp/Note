---
title: Alpine基础
date: 2018-11-21 10:56:52
tags: 
    - Alpine
    - 基础
categories: 
    - Linux
---

💠

- 1. [Alpine](#alpine)
    - 1.1. [BusyBox](#busybox)

💠 2024-09-06 11:36:43
****************************************
# Alpine 
> [Official Site](https://www.alpinelinux.org/)

> 从K8S及应用层兼容考虑，都不推荐Alpine做基础镜像！  
> [是否适合用作Docker基础镜像](https://cloud.tencent.com/developer/article/1632733)  
> [Alpine Linux，一个只有 5M 的 Docker 镜像](https://www.infoq.cn/article/2016/01/Alpine-Linux-5M-Docker)  

- [Does Alpine have known DNS issue within Kubernetes?](https://stackoverflow.com/questions/65181012/does-alpine-have-known-dns-issue-within-kubernetes)
- 优点是镜像很小 但是缺点是工具集和相关底层库实现和Ubuntu等主流发行版不一致，可能导致应用出现不一致情况，终端内的工具集也是不统一的  
    - alpine 使用的musl 主流使用的glibc
    - 即使从优点来说 由于镜像底层的文件系统是多层，所以多次分发镜像时，基础镜像小也就没有了优势

## BusyBox
> 里面各种工具命令能满足大部分需求, 但是命令参数，实现的功能都和原始的工具有差异，有裁剪

- 真正的 ls 属于`coreutils`包 
- 真正的 ps 属于 `procps` 包

