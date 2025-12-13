
# ConcurrentSkipListMap


## ConcurrentSkipListMap vs ConcurrentHashMap
ConcurrentHashMap = 无序 + O(1) + 内存省 → 90% 并发场景默认选它
ConcurrentSkipListMap = 有序 + O(log n) + 内存占用大 → 只有“既要线程安全又要排序/范围查询”才考虑它

| 维度       | ConcurrentHashMap       | ConcurrentSkipListMap                       |
| -------- | ----------------------- | ------------------------------------------- |
| 数据结构     | 数组+链表+红黑树               | 跳表（多层索引链表）                                  |
| 时间复杂度    | 读写 O(1) 平均              | 读写 O(log n) 平均                              |
| 是否有序     | 否（哈希散列）                 | 是（自然序或 Comparator）                          |
| 线程安全手段   | CAS + synchronized（桶头锁） | 无锁 CAS+自旋                                   |
| 并发度      | 桶级锁，热点 key 会冲突          | 全无锁，理论 CPU 数并行                              |
| 内存占用     | 低（仅数组+节点）               | 高（节点+多层索引，约 1.5~2 倍）                        |
| 功能扩展     | 无                       | 支持 `subMap()/headMap()/tailMap()`、平均排名、TopK |
| null 键/值 | 都不允许                    | 都不允许                                        |
| 代码体积&维护  | 简单，API 与 HashMap 几乎一致   | 复杂，跳表+ CAS 算法少见                             |

选型：
- 要排序/范围/排名 → 只此一家，必须用 ConcurrentSkipListMap。
- 纯 KV 读写，流量大，内存抠 → 用 ConcurrentHashMap。
- 数据量极大且 99% 读，偶尔排个序 → 可以先 CHM 缓存，排序时 dump 到数组 + 外部排序，也比全程 CSLM 省钱。



