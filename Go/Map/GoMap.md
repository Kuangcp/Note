---
title: GoMap
date: 2025-01-07 09:56:23
tags: 
categories: 
---


💠

- 1. [Golang map](#golang-map)
    - 1.1. [sync.map](#syncmap)

💠 2025-01-07 09:56:23
****************************************
# Golang map 

map 不仅仅是一个哈希表，它是一套为了极致性能和内存利用率而设计的复杂数据结构

> [参考: Java HashMap和Go map源码对比](https://juejin.im/post/5c020b145188250e8601f2a2)  

在 Go 语言中，map 是最常用的数据结构之一。不同于 Java 的 HashMap（数组+链表/红黑树），Go 的 map 采用了 底层桶（Bucket）结构 + 溢出桶 的设计。
一、 核心数据结构：hmap 与 bmap
map 的底层由 runtime/map.go 中的 hmap 结构体表示。
1. hmap (Header of Map)  这是控制中心，记录了 map 的全局信息：
    - count: 键值对数量。
    - B: 桶的数量是  2的幂次个。
    - buckets: 指向桶数组的指针。
    - oldbuckets: 扩容时指向旧桶的指针。
    - nevacuate: 扩容进度计数器。
    - extra: 溢出桶的相关信息。

2. bmap (Bucket of Map)  这是数据的真正存储单元。每个 bmap（即 bucket）固定存储 8 个键值对。
    - tophash: 存储 8 个 Key 哈希值的高 8 位。用于快速定位 Key 是否在桶内。
    - keys/values: 紧凑排列。注意：Go 采用 k1k2.../v1v2... 的排列方式，而不是 k1v1/k2v2。这通过内存对齐减少了 padding 空间。
    - overflow: 指向下一个溢出桶的指针（拉链法解决哈希冲突）。

二、 查找流程：两步定位法
当我们执行 v := m[key] 时，发生了什么？

1. 计算哈希：通过 hash(key) 得到一个 64 位的哈希值。
1. 定位桶 (Low bits)：取哈希值的 低 B 位。例如 B=5 ，则取后 5 位，定位到 32 个桶中的某一个。
1. 快速匹配 (High bits)：取哈希值的 高 8 位（tophash）。
1. 遍历对比：在桶内循环对比 tophash。如果 tophash 匹配，再对比真正的 key。
1. 追踪溢出桶：如果当前桶没找到，沿着 overflow 指针继续往后找。

三、 扩容机制：平滑切换的艺术
Go 的 map 不会像 Redis 那样瞬间阻塞扩容，而是采用 渐进式扩容。
1. 触发条件

    装载因子 (Load Factor) > 6.5：意味着桶快满了，冲突严重。触发 翻倍扩容。
    溢出桶过多：意味着大量由于插入删除导致的内存碎片。触发 等量扩容（整理碎片）。

2. 渐进式搬迁 (Evacuation)

    扩容发生时，oldbuckets 指向旧数组，buckets 指向新数组。
    不一次性搬完：每次对 map 进行 插入或删除 操作时，都会顺带搬迁 1~2 个桶的数据。
    查询兼容：查询时，先看 oldbuckets 是否搬迁完，没搬完则去旧桶找。

四、 为什么 Map 是无序的？
这是初学者常问的问题。原因有二：

    哈希随机性：哈希函数本身保证了分布的随机。
    扩容位移：扩容后，原本在同一个桶的 Key 可能会分流到不同的新桶，顺序彻底改变。
    官方限制：为了防止开发者依赖特定顺序，Go 运行时在迭代 map 时会故意引入一个 随机起始桶。

五、 并发不安全：致命的读写冲突
map 原生 并发读写不安全。

    原因：由于渐进式扩容的存在，写操作会修改 hmap 的状态。如果在写的同时读取，可能会读到搬迁中途的脏数据。
    检测机制：map 内部有一个 flags 标志位。一旦检测到并发读写，会直接抛出 fatal error: concurrent map read and map write，导致程序崩溃。
    解决方案：
        使用 sync.Mutex 加锁。
        读多写少场景下使用 sync.Map。

六、 总结与最佳实践

    预设容量：如果知道数据量，使用 make(map[K]V, hint)。预设容量能极大地减少扩容导致的内存重分配开销。
    内存泄露风险：map 的桶只会增加不会减少。即使删除了所有 Key，hmap 占用的内存（桶数组）依然存在。如果 map 曾存过百万数据，建议定期手动替换旧 map 或重启。
    Key 选型：避免使用结构体作为 Key，哈希计算开销大。简单的 int 或 string 性能更优。

