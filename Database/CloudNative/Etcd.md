---
title: Etcd
date: 2025-09-16 17:08:17
tags: 
categories: 
---

💠

- 1. [etcd](#etcd)
    - 1.1. [部署](#部署)

💠 2026-02-02 10:23:38
****************************************
# etcd
> [etcd](https://etcd.io/)  

**管理工具**

> [Etcd Workbench | Etcd Desktop Manager](https://tzfun.github.io/etcd-workbench/)  
`docker run --name my-etcd-workbench -p 8002:8002 -d tzfun/etcd-workbench:latest`  


## 部署
**单机部署**

快速实验功能，但是由于单点问题，一旦etcd崩溃，apisix数据会不一致，无法修改，无法代理等问题

> [cilium/examples/kubernetes/addons/etcd/standalone-etcd.yaml at main · cilium/cilium](https://github.com/cilium/cilium/blob/main/examples/kubernetes/addons/etcd/standalone-etcd.yaml)  
> Copy：[DockerfileList/k8s/ectd-standalone.yaml at master · Kuangcp/DockerfileList](https://github.com/Kuangcp/DockerfileList/blob/master/k8s/ectd-standalone.yaml)  


**集群部署**

