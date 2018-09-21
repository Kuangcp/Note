`目录 start`
 
- [Kubernetes](#kubernetes)
    - [相关博客](#相关博客)
    - [安装](#安装)
    - [简单使用](#简单使用)
    - [容器编排](#容器编排)

`目录 end` |_2018-09-10_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Kubernetes
> 又称K8s [Official site](https://kubernetes.io/) | [Github:](https://github.com/kubernetes/kubernetes)

## 相关博客
> [浅谈k8s+docker 资源监控](https://segmentfault.com/a/1190000003898140) | [基于Kubernetes构建Docker集群管理详解](http://www.csdn.net/article/2014-12-24/2823292-Docker-Kubernetes)  
[Kubernetes 学习笔记 ](http://wdxtub.com/2017/06/05/k8s-note/)

> [参考博客: Kubernetes会不会被自身的复杂性压垮？](http://www.infoq.com/cn/articles/will-kubernetes-collapse-under-the-weight-of-its-complexity)


## 安装
> [official doc](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

> [参考博客: kubeadm 搭建 kubernetes 集群](https://mritd.me/2016/10/29/set-up-kubernetes-cluster-by-kubeadm/)

> [参考博客: Kubernetes国内镜像、下载安装包和拉取gcr.io镜像](https://blog.csdn.net/nklinsirui/article/details/80581286)

> [参考博客: 国内服务器安装kubernetes一路坑，求大神指点 ](http://dockone.io/question/1225#!answer_form)

- **注意** Deepin上不要安装 kubernetes-client 这个是 1.7 版本, 类似于 docker.io 这样的老旧版本

> 使用阿里云的镜像进行安装
```sh
# 均以 root 运行
apt update && apt install -y apt-transport-https

curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add -

echo "deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list 

apt install kubelet kubeadm kubectl
```
> `deb http://apt.kubernetes.io/ kubernetes-xenial main` 虽然这才是官方源,奈何是Google服务器

## 简单使用

## 容器编排