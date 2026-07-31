---
title: Go之GC
date: 2026-03-24 14:00:00
tags: 
categories: 
---

💠

- 1. [GC 核心概念](#gc-核心概念)
    - 1.1. [三色标记法](#三色标记法)
    - 1.2. [STW (Stop The World)](#stw-stop-the-world)
    - 1.3. [写屏障 (Write Barrier)](#写屏障-write-barrier)
        - 1.3.1. [插入写屏障 (Dijkstra)](#插入写屏障-dijkstra)
        - 1.3.2. [删除写屏障 (Yuasa)](#删除写屏障-yuasa)
        - 1.3.3. [混合写屏障 (Hybrid)](#混合写屏障-hybrid)
    - 1.4. [辅助回收 (Mark Assist)](#辅助回收-mark-assist)
    - 1.5. [Pacer (调步算法)](#pacer-调步算法)
- 2. [GC 演进与版本差异](#gc-演进与版本差异)
    - 2.1. [Go 1.3：标记-清除 (Mark-Sweep)](#go-13标记-清除-mark-sweep)
    - 2.2. [Go 1.5：并发三色标记](#go-15并发三色标记)
    - 2.3. [Go 1.8：混合写屏障](#go-18混合写屏障)
    - 2.4. [Go 1.18：Pacer 重构](#go-118pacer-重构)
    - 2.5. [Go 1.19：软内存限制 (Soft Memory Limit)](#go-119软内存限制-soft-memory-limit)
    - 2.6. [Go 1.26：GreenTea GC (Span-based Scanning)](#go-126greentea-gc-span-based-scanning)
- 3. [GC 参数与调优](#gc-参数与调优)
- 4. [内存归还：MADV_FREE 与 MADV_DONTNEED](#内存归还madv_free-与-madv_dontneed)
    - 4.1. [MADV_DONTNEED](#madv_dontneed)
    - 4.2. [MADV_FREE](#madv_free)
    - 4.3. [版本演进](#版本演进)
    - 4.4. [控制方式](#控制方式)
- 5. [最佳实践](#最佳实践)

💠 2026-07-31 18:55:08
****************************************
# GC 核心概念
> Go Garbage Collection

Go 的 GC 是一种 **并发 (Concurrent)**、**三色标记 (Tricolor Mark)**、**非分代 (Non-generational)**、**非紧缩 (Non-compacting)** 的垃圾回收器。

## 三色标记法
将对象分为三种颜色，用于并发标记过程：
- **白色**：潜在的垃圾，其内存可能会被回收。
- **灰色**：活跃对象，但其引用的对象尚未被扫描。
- **黑色**：活跃对象，且其引用的对象已全部扫描完成。

**标记过程**：
1. GC 开始时，所有对象都是白色。
2. 从 GC Root（栈、全局变量）开始，将直接引用的对象标记为灰色。
3. 遍历灰色对象，将其引用的对象标记为灰色，自身标记为黑色。
4. 重复步骤 3，直到没有灰色对象。
5. 清除所有白色对象。

## STW (Stop The World)
Go GC 极力减少 STW 时间。目前 STW 主要发生在：
- **开启 GC**：清理写屏障缓冲区，开启写屏障。
- **结束标记 (Mark Termination)**：计算下一次 GC 的触发阈值，关闭写屏障。

## 写屏障 (Write Barrier)
为了在标记阶段允许用户代码（Mutator）并发运行，必须通过写屏障维持 **强三色不变性** 或 **弱三色不变性**，防止“对象丢失”。

### 插入写屏障 (Dijkstra)
- **原理**：当对象 A 引用对象 B 时，将 B 标记为灰色。
- **缺点**：为了性能，栈上不开启写屏障。这导致标记结束后需要 STW 重新扫描栈（Stack Rescan）。

### 删除写屏障 (Yuasa)
- **原理**：被删除引用的对象如果原本是白色，则标记为灰色。
- **优点**：不需要重新扫描栈。
- **缺点**：回收精度低，一个对象即使被删除了引用也会活过这一轮。

### 混合写屏障 (Hybrid)
> Go 1.8 引入，结合了两者优点。
- **规则**：
    1. GC 开始时，将栈上所有对象标记为黑色（无需重新扫描）。
    2. GC 期间，任何在栈上创建的新对象均为黑色。
    3. 被删除引用的对象标记为灰色。
    4. 被添加引用的对象标记为灰色。

## 辅助回收 (Mark Assist)
如果用户协程（Goroutine）分配内存的速度超过了 GC 标记的速度，GC 会强制该协程停下来协助标记工作，以防止内存溢出。

## Pacer (调步算法)
Pacer 负责决定何时启动 GC。
- **目标**：在堆大小达到目标值（Heap Goal）时正好完成 GC，同时将 GC CPU 占用控制在 25% 左右。

****************************************
# GC 演进与版本差异

| 版本 | GC 算法 | STW 时长 | 重大改进 |
| :--- | :--- | :--- | :--- |
| **Go 1.3** | 标记-清除 (Mark-Sweep) | 百毫秒级 | 引入并行清扫，标记过程仍需 STW |
| **Go 1.5** | 并发三色标记 | 十毫秒级 | 引入 Dijkstra 插入写屏障，支持并发标记 |
| **Go 1.8** | 混合写屏障 | < 1ms | 引入混合写屏障，彻底消除栈重扫 (Stack Rescan) |
| **Go 1.18** | Pacer 重构 | < 0.5ms | 改进调步算法，解决小堆频繁 GC 和大堆延迟问题 |
| **Go 1.19** | 软内存限制 | < 0.5ms | 引入 `GOMEMLIMIT`，支持设定触发 GC 的内存上限 |
| **Go 1.26** | GreenTea GC | < 0.3ms | 引入基于 Span 的扫描，利用 SIMD 加速，大幅提升缓存局部性 |

## Go 1.3：标记-清除 (Mark-Sweep)
- **过程**：STW 标记 -> STW 清除。
- **改进**：将清除过程改为并行（与用户代码并发），但标记依然需要 STW。

## Go 1.5：并发三色标记
- **突破**：首次实现并发标记，极大降低了 STW。
- **局限**：由于使用插入写屏障，在标记结束时需要 STW 重新扫描栈，停顿时间随栈大小增长。

## Go 1.8：混合写屏障
- **突破**：通过混合写屏障，避免了栈重扫。STW 时间降至微秒级，且不再随堆栈大小线性增长。

## Go 1.18：Pacer 重构
- **改进**：使用控制理论（PI 控制器）重新设计 Pacer，使 GC 触发时机更加平滑，减少了在极端负载下的抖动。

## Go 1.19：软内存限制 (Soft Memory Limit)
- **新特性**：引入 `GOMEMLIMIT` 环境变量。
- **作用**：在内存接近限制时强制触发 GC，有效防止 OOM（Out of Memory），特别是在容器环境下。

## Go 1.26：GreenTea GC (Span-based Scanning)
- **核心突破**：从“逐个对象扫描”演进为“基于 Span 的批量扫描”。
- **原理**：
    - **Span-based Scanning**：将内存中连续的 Span 作为扫描单位，极大提升了空间局部性（Spatial Locality）。
    - **双位图标记 (Dual Mark Bits)**：引入 `marks` 和 `scans` 两套位图，通过位运算（Union/Intersection）快速确定 Span 内需要扫描的对象。
    - **SIMD 加速**：在支持 AVX-512 的架构上，利用向量指令集加速对象扫描过程，GC 开销降低 10-40%。
- **代价**：由于引入了更复杂的元数据管理，常驻内存 (RSS) 可能会有 8-15% 的小幅增加。

****************************************
# GC 参数与调优

- `GOGC`：默认 100。表示当新分配内存达到上一次 GC 后存活内存的 100% 时触发 GC。 例如GC后占用200M内存，那么直到再申请200M内存才会触发GC
    - 设置为 `off` 可彻底禁用 GC。
- `GOMEMLIMIT`：Go 1.19 引入。设置运行时的软内存上限。
- `debug.SetGCPercent()`：动态修改 `GOGC`。
- `runtime.GC()`：手动触发一次 GC。

****************************************
# 内存归还：MADV_FREE 与 MADV_DONTNEED

GC 只负责回收堆内对象，真正把空闲内存归还给操作系统的是 **Scavenger（清道夫）**。Scavenger 在后台持续通过 `madvise()` 将不再使用的内存归还内核，不同平台/版本的策略不同：

## MADV_DONTNEED
- **行为**：立即丢弃页面，RSS 立刻下降；之后再次访问会触发缺页（Page Fault），需重新分配。
- **代价**：调用开销较高，频繁归还与再分配的成本大。

## MADV_FREE
- **行为**：懒释放。页面先标记为可回收，只有在内核内存紧张时才真正回收，RSS 不会立即下降。
- **优点**：归还开销小，且页面可被复用，性能更好。
- **缺点**：`top` 等监控工具中的 RSS 不下降，容易被误判为"内存泄漏"，与依赖内存指标做弹性伸缩/管理的系统配合不佳。

例如MinIO这类本身还有对象池，就容易导致如果有大批量的文件写入，会让内存居高不下不归还系统

> 假如同一个主机上还部署了Java应用，然后MinIO已经占用了很高内存没归还的前提下，Java应用也开始大额申请内存时，会有以下风险

场景 1：MinIO 被部署在有硬性限制（Limit）的 Docker/K8s 容器中

* 致命点：Docker 的内存限制（如 resources.limits.memory: 15G）是通过 Linux 的 Cgroups 机制实现的。
* 结果：Cgroups 在很多旧版本 Linux 内核中，并不屑于去识别 MADV_FREE 的标记。当 MinIO 容器内的 Go 内存积压到 15G 时，Cgroups 误以为这 15G 全是活的数据，从而直接触发 OOM，把 MinIO 容器一枪干掉（Exit Code 137）。

场景 2：Java 的 -Xms 和 -Xmx 设得太大

* 致命点：如果 Java 进程启动时设置了 -Xms15G -Xmx15G（启动即锁定 15G 物理内存），或者并发流量极高，导致 Java 申请内存的速度快过了 Linux 内核回收 MADV_FREE 页面的速度。
* 结果：内核来不及回收，就会瞬间触发操作系统的保护机制（OOM-Killer），它会根据 OOM Score 算出一个最耗内存的“倒霉蛋”（通常不是 MinIO 就是 Java），然后随机杀掉其中一个进程。

## 版本演进
| 版本 | 默认行为 |
| :--- | :--- |
| **Go 1.12** | Linux 上默认改用 MADV_FREE（内核不支持时回退 MADV_DONTNEED），见 issue #23687 |
| **Go 1.16** | 回退为默认使用 MADV_DONTNEED，因 MADV_FREE 导致 RSS 统计不直观，见 commit 05e6d28 / issue #42330 |

## 控制方式
- `GODEBUG=madvdontneed=1`：Linux 默认，使用 MADV_DONTNEED。
- `GODEBUG=madvdontneed=0`：Linux 改用 MADV_FREE（效率更高，但 RSS 只在内存压力下才下降）。
- **BSD 系 / Illumos / Solaris** 默认使用 MADV_FREE，设置 `GODEBUG=madvdontneed=1` 可切回 MADV_DONTNEED。
- **macOS** 使用 `MADV_FREE_REUSABLE` / `MADV_FREE_REUSE`。
- `debug.FreeOSMemory()`：强制触发一次 GC 并尽量将内存归还给操作系统。
- `GODEBUG=scavtrace=1`：输出 Scavenger 的归还统计，用于排查内存问题。
- 设置 `GOMEMLIMIT` 后，Scavenger 会采取更积极的归还（Eager Scavenging）以遵守内存上限。

****************************************
# 最佳实践
1. **控制分配频率**：减少临时对象的创建，复用对象（使用 `sync.Pool`）。
2. **合理设置 GOGC**：内存充足时可调大 `GOGC` 以减少 GC 频率，提升吞吐。
3. **利用 GOMEMLIMIT**：在容器化部署时，将 `GOMEMLIMIT` 设置为容器限制的 80%-90%，防止 OOM。
4. **监控 GC 指标**：通过 `runtime.ReadMemStats` 或 `prometheus` 监控 `gc_pauses` 和 `heap_alloc`。
