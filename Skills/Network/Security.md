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

💠 2023-10-09 17:53
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

