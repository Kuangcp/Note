---
title: 限流
date: 2022-08-03 10:33:45
tags: 
categories: 
---

**目录 start**

1. [限流](#限流)
    1. [算法](#算法)
        1. [令牌桶](#令牌桶)
        1. [漏桶](#漏桶)
        1. [滑动窗口](#滑动窗口)
1. [组件方案](#组件方案)
    1. [Nginx](#nginx)
    1. [Guava](#guava)
    1. [Redis](#redis)
    1. [Hystrix](#hystrix)

**目录 end**|_2022-10-22 22:59_|
****************************************
# 限流
## 算法
### 令牌桶
固定速率生成令牌放入桶中，并支持预取，通过限制获得令牌来实现限流
- 允许当前请求获取超量资源（大于并发限制），下一次请求需要等待超额的时间

> [Guava ratelimiter 实现原理](https://cloud.tencent.com/developer/article/1408819)

### 漏桶
不支持突发流量, 通过限制流出速率，丢弃突发的流入流量来实现限流

### 滑动窗口

************************

# 组件方案

## Nginx 

## Guava
RateLimiter 令牌桶实现
- 支持平滑发放令牌（例如限制每秒5并发，每个令牌的获取间隔大概在200ms左右）

## Redis
zset 使用时间戳值来做滑动窗口

## Hystrix

