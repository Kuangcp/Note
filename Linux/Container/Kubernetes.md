---
title: Kubernetes
date: 2018-12-15 11:28:19
tags:
  - 基础
categories:
  - Kubernetes
---

💠

- 1. [Kubernetes](#kubernetes)
    - 1.1. [相关博客](#相关博客)
    - 1.2. [安装](#安装)
        - 1.2.1. [minikube](#minikube)
    - 1.3. [简单使用](#简单使用)
    - 1.4. [容器编排](#容器编排)
- 2. [Kubeless](#kubeless)

💠 2024-03-04 17:26:01
****************************************

# Kubernetes

> 又称 k8s [Official site](https://kubernetes.io/) | [Github:](https://github.com/kubernetes/kubernetes)

## 相关博客

> [浅谈 k8s+docker 资源监控](https://segmentfault.com/a/1190000003898140) | [基于 Kubernetes 构建 Docker 集群管理详解](http://www.csdn.net/article/2014-12-24/2823292-Docker-Kubernetes)  
> [Kubernetes 学习笔记 ](http://wdxtub.com/2017/06/05/k8s-note/)   
> [Kubernetes 中文社区](https://www.kubernetes.org.cn/doc-45)  
> [Kubernetes 使用教程](https://github.com/chaseSpace/k8s-tutorial-cn)

> [参考: Kubernetes 会不会被自身的复杂性压垮？](http://www.infoq.com/cn/articles/will-kubernetes-collapse-under-the-weight-of-its-complexity)  
> [参考: 一文带你看透 kubernetes 容器编排系统](https://my.oschina.net/qcloudcommunity/blog/2998211)

## 安装

> [official doc](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

> [参考: kubeadm 搭建 kubernetes 集群](https://mritd.me/2016/10/29/set-up-kubernetes-cluster-by-kubeadm/)  
> [参考: Kubernetes 国内镜像、下载安装包和拉取 gcr.io 镜像](https://blog.csdn.net/nklinsirui/article/details/80581286)  
> [参考: 国内服务器安装 kubernetes 一路坑，求大神指点 ](http://dockone.io/question/1225#!answer_form)

- **注意** Deepin 上不要安装 kubernetes-client 这个是 1.7 版本, 类似于 docker.io 这样的老旧版本

> 使用阿里云的镜像进行安装

```sh
    # 均以 root 运行
    apt update && apt install -y apt-transport-https

    curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add -

    echo "deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list

    apt install kubelet kubeadm kubectl
```

> `deb http://apt.kubernetes.io/ kubernetes-xenial main` 虽然这才是官方源,奈何是 Google 服务器

************************

### minikube
> [minikube](https://minikube.sigs.k8s.io/docs/start/)

## 简单使用

> 大多数命令和 Docker 是类似的，只不过加上了 namespace 的概念

- kubectl logs --namespace namespace pod

## 容器编排

# Kubeless

> [Official](https://kubeless.io/docs/quick-start/)
