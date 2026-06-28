# 分布式
> [系统设计入门](https://github.com/donnemartin/system-design-primer)  
> [分布式系统核心技术](https://yeasy.gitbook.io/blockchain_guide/04_distributed_system)   
> [分布式系统 - 知识体系详解](https://pdai.tech/md/arch/arch-z-overview.html)  
> [分布式系统学习资料汇总 - Golang编程语言知识介绍](http://shanks.link/blog/2024/01/24/%e5%88%86%e5%b8%83%e5%bc%8f%e7%b3%bb%e7%bb%9f%e5%ad%a6%e4%b9%a0%e8%b5%84%e6%96%99%e6%b1%87%e6%80%bb/)  
> [分布式系统 - 理论基础,理论及一致性算法 | Java 全栈知识体系](https://pdai.tech/md/arch/arch-z-theory.html#cap%E7%90%86%E8%AE%BA)  


要考虑采用该种方式后带来的技术复杂度的问题, 当前的问题需不需要上升到分布式的体量上

**书籍**
《构建数据密集型应用》
《分布式系统》

## 目录
- [共识算法](#共识算法)
  - [CAP定理](#cap定理)
  - [BASE理论](#base理论)
  - [Paxos](#paxos)
  - [Zab](#zab)
  - [Raft](#raft)
  - [Gossip](#gossip)
- [分布式事务](Transaction/Readme.md)
- [高可用](HA/Readme.md)
  - [限流](HA/RateLimit.md)
- [配置中心](ConfigCenter/Readme.md)
- [服务发现](ServiceDiscovery/Readme.md)
- [消息队列](MQ/MQ.md)
- [RPC](RPC.md)

## 共识算法
> [learn_blockchain/consensus.md](https://github.com/chaseSpace/learn_blockchain/blob/main/consensus.md)  

- [x] CAP定理
- [x] BASE理论
- [x] Raft
- [ ] Paxos - 需深入理解 Multi-Paxos 优化
- [ ] Zab - Zookeeper 原子广播协议
- [ ] Gossip - 最终一致性协议
- [ ] 分布式锁实现方案对比

************************

### CAP定理

CAP： Consistency Availability Partition tolerance

**核心概念**
- **C (Consistency)**: 一致性，所有节点在同一时间看到相同的数据
- **A (Availability)**: 可用性，每个请求都能在合理时间内得到响应
- **P (Partition Tolerance)**: 分区容错性，系统在网络分区时仍能继续运行

**为什么只能满足两个？**
- 网络分区是必然存在的（P必须保证）
- 当发生网络分区时，要保证一致性(C)就不能响应请求（牺牲A）
- 要保证可用性(A)就可能返回旧数据（牺牲C）

**典型系统分类**
| 类型 | 说明 | 系统示例 |
|------|------|----------|
| CP系统 | 保证一致性，牺牲可用性 | Zookeeper, Etcd, MongoDB |
| AP系统 | 保证可用性，牺牲一致性 | Eureka, Cassandra, DynamoDB |

https://github.com/aliyun/alibabacloud-microservice-demo.git

### BASE理论

BASE 是对 CAP 中一致性和可用性权衡的结果，源于大规模互联网系统演进的实践总结

**核心概念**
- **BA (Basically Available)**: 基本可用，允许系统在某些功能上有所损失
- **S (Soft State)**: 软状态，允许系统中的数据存在中间状态
- **E (Eventually Consistent)**: 最终一致性，保证数据最终达到一致状态

**与 ACID 的对比**
| ACID | BASE |
|------|------|
| 强一致性 | 最终一致性 |
| 保证事务 | 允许中间状态 |
| 可能牺牲性能 | 保证高可用 |

**实际应用场景**
- 消息队列：允许消息短暂延迟
- 分布式缓存：允许短暂的数据不一致
- 电商库存：允许超卖后补偿

### Paxos
> [Wikipedia](https://en.wikipedia.org/wiki/Paxos_%28computer_science%29)

Paxos 是最著名的共识算法，由 Leslie Lamport 提出

**核心角色**
- **Proposer**: 提案者，发起提案
- **Acceptor**: 接受者，投票决定是否接受提案
- **Learner**: 学习者，学习被接受的提案

**两阶段过程**
1. **Prepare阶段**: Proposer 发送 prepare(n) 请求
2. **Accept阶段**: 如果收到多数响应，发送 accept(n, v) 请求

**问题**
- 算法复杂，难以理解和实现
- 存在活锁问题（需要 Multi-Paxos 优化）

[Paxos H2O实现](https://github.com/h2oai/h2o-3/blob/master/h2o-core/src/main/java/water/Paxos.java)  

### Zab
> [Zookeeper 官方文档](https://zookeeper.apache.org/doc/current/zookeeperInternals.html)

Zab (Zookeeper Atomic Broadcast) 是 Zookeeper 使用的共识协议

**核心特点**
- 选举机制：使用 ZXID（事务ID）进行选举
- 原子广播：类似 2PC 的提交协议
- 崩溃恢复：leader 故障时自动选举新 leader

**与 Paxos 的区别**
- Zab 更注重可用性
- Zab 有明确的 leader 角色
- Zab 使用 epoch 表示 leader 轮次

### Raft
> [Wikipedia](https://en.wikipedia.org/wiki/Raft_(algorithm)) | [Github Raft](https://raft.github.io/)  

快速理解：基于状态复制机模式，所有节点从相同的状态开始通过一系列log达到一致的状态，例如Redis的RDS一样将数据变化日志化  
通过其中的选举算法实现集群里始终只有一个leader多follower的状态  
客户端发起的所有修改动作都会交由leader完成并复制给其他节点（当集群内N/2+1的节点确认复制成功后给客户端响应操作成功），如果请求到了follwer节点也会转发给leader节点处理  

**三个核心机制**
1. **Leader选举**: 超时触发选举，获得多数票成为 leader
2. **日志复制**: Leader 接收客户端请求，复制到多数节点后提交
3. **安全性**: 保证已提交的日志不会被覆盖

- 解决的问题： 实现分布式系统的数据一致性和高可用。例如 Etcd、Consul、Zookeeper 组件中用到

[Raft 实战系列，日志复制是什么？怎么实现？日志不一致怎么办？](https://blog.51cto.com/u_15009384/2568224)
[动态变更节点](https://segmentfault.com/a/1190000022796386)

### Gossip
> [Gossip协议详解](https://www.cnblogs.com/xybaby/p/7762094.html)

Gossip 是一种去中心化的最终一致性协议

**工作原理**
- 每个节点随机选择其他节点传播信息
- 信息通过指数级传播最终达到全局一致
- 类似病毒传播的方式

**优缺点**
- 优点：去中心化、容错性好、可扩展性强
- 缺点：收敛慢、带宽消耗大、可能产生冗余消息

**应用场景**
- Redis Cluster 节点间通信
- Cassandra 数据同步
- Consul 服务发现

## 其他专题
- 分布式锁 Redis/Zookeeper/数据库实现
- 分布式ID  雪花算法/UUID/号段模式
- 分布式缓存 缓存一致性/穿透/击穿/雪崩 
