# 分布式
> [系统设计入门](https://github.com/donnemartin/system-design-primer)  
> [分布式系统核心技术](https://yeasy.gitbook.io/blockchain_guide/04_distributed_system)   
> [分布式系统 - 知识体系详解](https://pdai.tech/md/arch/arch-z-overview.html)  

要考虑采用该种方式后带来的技术复杂度的问题, 当前的问题需不需要上升到分布式的体量上

- [ ] CAP Paxos Zab Raft Gossip Billy


[Paxos](https://en.wikipedia.org/wiki/Paxos_%28computer_science%29)  
[Paxos H2O实现](https://github.com/h2oai/h2o-3/blob/master/h2o-core/src/main/java/water/Paxos.java)  



************************

### Raft
> [Wikipedia](https://en.wikipedia.org/wiki/Raft_(algorithm)) | [Github Raft](https://raft.github.io/)  

快速理解：基于状态复制机模式，所有节点从相同的状态开始通过一系列log达到一致的状态，例如Redis的RDS一样将数据变化日志化  
通过其中的选举算法实现集群里始终只有一个leader多follower的状态  
客户端发起的所有修改动作都会交由leader完成并复制给其他节点（当集群内N/2+1的节点确认复制成功后给客户端响应操作成功），如果请求到了follwer节点也会转发给leader节点处理  

- 解决的问题： 实现分布式系统的数据一致性和高可用。例如 Etcd、Consul、Zookeeper 组件中用到


[Raft 实战系列，日志复制是什么？怎么实现？日志不一致怎么办？](https://blog.51cto.com/u_15009384/2568224)

https://zhuanlan.zhihu.com/p/28560167
https://www.cnblogs.com/mindwind/p/5231986.html
[Raft](https://zhuanlan.zhihu.com/p/32052223)


[动态变更节点](https://segmentfault.com/a/1190000022796386)

### CAP定理
CAP： Consistency Availability Partition tolerance

> [码农翻身:张大胖和CAP定理](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513560&idx=1&sn=ba861726537c57bd34253cbce010b5f)

https://github.com/aliyun/alibabacloud-microservice-demo.git

### BASE 
