---
title: PGO
date: 2024-04-30 22:26:23
tags: 
categories: 
---

💠

- 1. [Profile-guided optimization](#profile-guided-optimization)

💠 2024-04-30 23:06:06
****************************************
# Profile-guided optimization
> [Profile-guided optimization](https://en.wikipedia.org/wiki/Profile-guided_optimization)  

- PGO Profile-guided optimization
- PDO feedback-directed optimization 
- PDF profile-directed feedback


核心思想为记录一份可靠的运行期profile，然后指导后续的应用对运行效率做针对性的优化。
相较于静态代码分析（通常由语言的编译包（编译器 优化器等）实现），运行期的分析能感知不同代码的运行频率和分支执行情况，有选择性的做JIT等优化。

