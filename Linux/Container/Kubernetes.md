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
- 2. [使用](#使用)
    - 2.1. [网络](#网络)
    - 2.2. [实践](#实践)
- 3. [安全](#安全)

💠 2024-09-06 11:36:43
****************************************

# Kubernetes
> [Official site](https://kubernetes.io/) | [Github](https://github.com/kubernetes/kubernetes) | [中文文档](https://kubernetes.io/zh-cn/docs/concepts/)

> [kwok](https://github.com/kubernetes-sigs/kwok) `模拟 K8s 集群的工具。它可以在几秒钟内搭建一个由数千个节点组成的 Kubernetes 集群`

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

************************

# 使用
> 大多数命令和 Docker 是类似的，只不过加上了 namespace 的概念

- 查看日志： kubectl logs --namespace namespace pod

> [Java client for Kubernetes](https://github.com/fabric8io/kubernetes-client)

## 网络
> [Kubernetes 疑难杂症排查分享：神秘的溢出与丢包 ](https://tencentcloudcontainerteam.github.io/2020/01/13/kubernetes-overflow-and-drop/)

## 实践
> Pod调度资源倾斜
- [你真的理解 K8s 中的 requests 和 limits 吗？](https://kubesphere.io/zh/blogs/deep-dive-into-the-k8s-request-and-limit) | [K8S: QoS](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/)
- [管理容器的计算资源](https://kuboard.cn/learning/k8s-intermediate/config/computing-resource.html)
- [Kubernetes 节点标签和定向调度](http://zongming.net/read-1333/)

结论：pod尽量按过往监控的情况设置合理的 requests 和 limits, 如果仍有明显的倾斜，可以配置节点亲和 nodeAffinity

例如如下配置只会将pod调度到03和04两个Node上, 对应于Kuboard的操作路径为 高级设置 -> 节点调度策略 -> 根据【节点亲和性】选择节点 -> 选择标签和值
```yml
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: kubernetes.io/hostname
                    operator: In
                    values:
                      - node03
                      - node04
```

# 安全
> [从零开始的Kubernetes攻防](https://github.com/neargle/my-re0-k8s-security)
