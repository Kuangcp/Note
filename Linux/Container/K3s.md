---
title: K3s
date: 2023-10-26 00:19:02
tags: 
categories: 
---

💠

- 1. [K3s](#k3s)
    - 1.1. [安装&配置](#安装&配置)
        - 1.1.1. [单机安装](#单机安装)

💠 2023-10-26 00:19
****************************************
# K3s 

## 安装&配置
### 单机安装
> [单机部署k3s](https://jasonkayzk.github.io/2022/10/21/%E5%8D%95%E6%9C%BA%E9%83%A8%E7%BD%B2k3s/)  

```sh
    curl -sfL https://get.k3s.io | sh -
    # 国内使用镜像源加速
    curl -sfL https://rancher-mirror.oss-cn-beijing.aliyuncs.com/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn sh -
```

- k3s 安装完成后会将 kubeconfig 文件写入到/etc/rancher/k3s/k3s.yaml，对于有多个集群的来说，需要配置这个；
- 同时 K3S_TOKEN 会存在你的服务器节点上的/var/lib/rancher/k3s/server/node-token路径下；
- 安装后会生成卸载脚本： `/usr/local/bin/k3s-uninstall.sh`

> [k3s部署kuboard面板](https://www.cnblogs.com/sstu/p/16760138.html)

添加Dockerhub作为ImagePullSecret: server字段配置为 https://docker.io 