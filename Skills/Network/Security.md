---
title: 网络安全
date: 2023-08-01 13:42:57
tags: 
categories: 
---

💠

- 1. [网络安全](#网络安全)
    - 1.1. [发现](#发现)
        - 1.1.1. [网络](#网络)
            - 1.1.1.1. [fping](#fping)
    - 1.2. [攻击](#攻击)
        - 1.2.1. [tcp syn flood](#tcp-syn-flood)
        - 1.2.2. [上传文件](#上传文件)

💠 2024-09-06 11:36:43
****************************************

# 网络安全
## 发现
### 网络
#### fping

`fping -a -g 192.168.0.1/24`
`nmap -sP 192.168.0.1/24`

************************

## 攻击

### tcp syn flood 
调整内核参数，加快tcp连接回收

sysctl -w net.ipv4.tcp_fin_timeout=30 # 默认60s
sysctl -w net.ipv4.tcp_tw_reuse=1

### 上传文件
> [upload-labs](https://github.com/c0ny1/upload-labs)`使用php语言编写的，专门收集渗透测试和CTF中遇到的各种上传漏洞的靶场`

