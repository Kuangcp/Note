---
title: Docker Swarm
date: 2018-12-15 11:24:44
tags: 
    - Docker
categories: 
    - Docker
---

💠

- 1. [Docker Swarm](#docker-swarm)
    - 1.1. [架构](#架构)
    - 1.2. [核心概念](#核心概念)
- 2. [集群管理](#集群管理)
    - 2.1. [初始化集群](#初始化集群)
    - 2.2. [节点管理](#节点管理)
- 3. [Service 管理](#service-管理)
- 4. [Stack 管理](#stack-管理)

💠 2026-06-12 17:31:28
****************************************
# Docker Swarm
> Docker 原生的容器集群管理工具，将多个 Docker 主机组成一个虚拟的 Docker 主机

- 声明式服务部署
- 服务自动扩缩容
- 跨主机网络（Overlay）
- 滚动更新与回滚
- 服务发现与负载均衡

## 架构
> Swarm 采用 **Manager-Worker** 架构

```
┌─────────────────────────────────────┐
│            Swarm Cluster             │
│                                     │
│  ┌──────────────┐  ┌──────────────┐ │
│  │   Manager    │  │   Manager    │ │
│  │  (Leader) ◄──┼──┤  (Follower)  │ │
│  └──────┬───────┘  └──────────────┘ │
│         │ Raft                      │
│  ┌──────┴───────┐  ┌──────────────┐ │
│  │   Worker     │  │   Worker     │ │
│  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────┘
```

**Manager 节点**：维护集群状态（Raft 共识）、调度服务、响应 API 请求
- 奇数个 Manager（1,3,5）以保证 Raft 多数派
- Leader 负责所有调度和编排决策

**Worker 节点**：接收 Manager 分配的任务，实际运行容器
- 不参与集群状态管理
- 不存储集群状态数据

**Raft 共识**：Manager 之间通过 Raft 协议同步状态，确保数据一致性

## 核心概念
> **Service**：描述要运行的任务（镜像、端口、副本数等）
> **Task**：Service 的单个实例，对应一个容器
> **Stack**：一组相关 Service 的集合，通过 docker-compose.yml 定义

- Service 声明期望状态，Swarm 保证实际状态与期望状态一致
- Task 由 Manager 调度到 Worker 节点执行
- Stack 将多个 Service 作为一个单元部署管理

****************************************
# 集群管理

## 初始化集群
```sh
# 初始化 Swarm（当前节点成为 Manager）
docker swarm init --advertise-addr <MANAGER-IP>

# 查看加入令牌
docker swarm join-token manager
docker swarm join-token worker

# 节点加入集群
docker swarm join --token <TOKEN> <MANAGER-IP>:2377

# 离开集群
docker swarm leave          # Worker 退出
docker swarm leave --force  # Manager 强制退出

# 查看集群信息
docker info | grep -i swarm
```

## 节点管理
```sh
# 查看节点
docker node ls
docker node inspect <NODE-ID>

# 提升/降级
docker node promote <NODE-ID>   # Worker → Manager
docker node demote <NODE-ID>    # Manager → Worker

# 更新标签
docker node update --label-add env=prod <NODE-ID>

# 移除节点（需先 drain 或 leave）
docker node rm <NODE-ID>
```

****************************************
# Service 管理
```sh
# 查看服务
docker service ls
docker service inspect myapp_web
docker service inspect --pretty myapp_web

# 查看任务（容器实例）
docker service ps myapp_web
docker service ps myapp_web --no-trunc

# 日志
docker service logs myapp_web
docker service logs -f myapp_web
docker service logs --tail 100 myapp_web

# 扩容/缩容
docker service scale myapp_web=5
docker service scale myapp_web=3 myapp_db=2

# 更新
docker service update --image nginx:1.25 myapp_web
docker service update --env-add KEY=VALUE myapp_web
docker service update --force myapp_web   # 强制重启

# 回滚
docker service update --rollback myapp_web

# 删除
docker service rm myapp_web
```

****************************************
# Stack 管理
> Stack 通过 docker-compose.yml 声明一组服务

```sh
# 部署/更新
docker stack deploy -c docker-compose.yml myapp
docker stack deploy -c docker-compose.yml --with-registry-auth myapp

# 查看
docker stack ls
docker stack ps myapp
docker stack services myapp

# 删除
docker stack rm myapp
```

> 完整工作流
```sh
# 1. 构建并推送镜像
docker build -t registry:5000/myapp:v1.0 .
docker push registry:5000/myapp:v1.0

# 2. 部署
docker stack deploy -c docker-compose.yml --with-registry-auth myapp

# 3. 扩容
docker service scale myapp_web=3

# 4. 更新
docker service update --image registry:5000/myapp:v1.1 myapp_web

# 5. 回滚
docker service update --rollback myapp_web

# 6. 清理
docker stack rm myapp
```
