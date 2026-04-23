---
title: Git深入学习
date: 2018-11-21 10:56:52
tags: 
    - Advanced
categories: 
    - 版本控制
---

💠

- 1. [Git Advance](#git-advance)
    - 1.1. [版本控制系统(VCS)](#版本控制系统vcs)
- 2. [Git实现原理](#git实现原理)
    - 2.1. [Diff算法](#diff算法)

💠 2026-04-23 11:13:12
****************************************
# Git Advance

## 版本控制系统(VCS)
- [码农翻身:小李的版本管理系统](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513204&idx=1&sn=c4c493d771a167a84ace01c3e016417e&scene=21#wechat_redirect)

- [SVN](https://subversion.apache.org/)
    - [submin](https://supermind.nl/submin/)`SVN管理的Web界面`
- [git](https://git-scm.com/) `最好用的vcs`

*********************

# Git实现原理

## Diff算法
默认是 Myers 算法

| 算法             | 特点                  | 适用场景       |
| -------------- | ------------------- | ---------- |
| **Myers** (默认) | 最短编辑脚本，行级对比         | 通用场景，结果紧凑  |
| **Minimal**    | Myers 变体，确保最小差异     | 需要最精确最小差异  |
| **Patience**   | 对有序列表友好，减少错位        | 代码重构、移动块检测 |
| **Histogram**  | Patience 改进，处理重复行更好 | 大文件、重复代码多  |
