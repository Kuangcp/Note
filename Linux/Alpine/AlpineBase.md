---
title: Alpine基础
date: 2018-11-21 10:56:52
tags: 
    - Alpine
    - 基础
categories: 
    - Linux
---

**目录 start**
 
1. [Alpine](#alpine)
    1. [BusyBox](#busybox)
        1. [ls](#ls)
        1. [ps](#ps)

**目录 end**|_2020-01-02 20:57_|
****************************************
# Alpine 
> [Official Site](https://www.alpinelinux.org/)

> 精简的linux 适合用于Docker 基础镜像

优点是镜像很小 但是缺点是工具集和相关库实现和Ubuntu等主流发行版不一致，可能导致应用出现不一致情况，终端内的工具集也是不统一的  
即使从优点来说 由于镜像底层的文件系统是多层，所以多次分发镜像时，镜像大小也没有了优势

## BusyBox
> 里面各种工具的实现能满足大部分需求, 但是有些参数和原始的工具有些差异

### ls
真正的 ls 属于`coreutils`包 

### ps
真正的 ps 属于 `procps` 包
