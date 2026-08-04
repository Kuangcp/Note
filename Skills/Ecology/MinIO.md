---
title: MinIO
date: 2024-11-18 15:13:15
tags: 
categories: 
---

💠

- 1. [MinIO](#minio)
- 2. [实践](#实践)

💠 2026-08-04 11:57:30
****************************************
# MinIO
> [min.io](https://min.io/)

同类解决方案： [DFS](/Linux/Base/LinuxFile.md#dfs) | [OSS](/Skills/Ecology/OSS.md)  


# 实践
> Langfuse监控内 海量小文件的优化

```ini
    # 1. 负责在 Go 语言层面清障（继续保留）
    GODEBUG: "madvdontneed=1"
    GOGC: "30" # 调到30，让垃圾回收更频繁
    
    # 2. 💥 真正针对你当前现状、能把 4G 压下来的新增核心（替代之前的并发50）
    MINIO_MAX_IDLE_CONNS_PER_HOST: "2"  # 强制杀死空闲长连接，退还 Socket 缓存
    MINIO_CACHE_EXPIRY: "1m"            # 1分钟自动驱逐小文件元数据，清空内存索引
```
- 查看系统的 Slab 缓存占了多少内存（重点看 dentry 和 inode） cat /proc/meminfo | grep -E "Slab|SReclaimable|SUnreclaim"
    - 注意这个部分是 可回收系统内核缓存
- 一定要设置pod的 最大内存limit，防止操作系统缓存在瞬间内存申请时拖垮整个node。详见 [Go MADV_FREE](/Go/GoGC.md#madv_free)
