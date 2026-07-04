---
title: CachyOS
date: 2026-07-04 16:47:20
tags: 
categories: 
---


💠

- 1. [CachyOS](#cachyos)

💠 2026-07-04 16:47:20
****************************************
# CachyOS

更快的代码编译速度：x86-64-v3 指令集与 Clang + AutoFDO 优化
高并发不卡顿：招牌 BORE-EEVDF CPU 调度器
内存：内核修改了内存预读机制（优化了透明大页 THP 策略），并引入了更高效的内存回收锁机制。
IO： 对多队列 I/O 调度器（如 BFQ、mq-deadline）进行了深度魔改优化，并集成了谷歌最新的 BBR3 网络拥塞控制算法。