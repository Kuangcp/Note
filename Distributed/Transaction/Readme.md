# 分布式事务
> [凤凰架构： 分布式事务](https://icyfenix.cn/architect-perspective/general-architecture/transaction/distributed.html)  

TODO 实现方式 场景

 Seata
 LCN做分布式事务
 柔性事务

在业务、范式、性能、维护发生冲突时，各自如何解决,其中有很多折中的思想

> [Seata AT 模式](https://seata.apache.org/zh-cn/docs/dev/mode/at-mode)
> [DTM](https://dtm.pub/guide/start.html)

> 2PC
CanCommit、DoCommit

单个协调者，多个参与者
过程：
1. 所有参与者开始上报可处理
1. 所有参与者确认能处理后，协调者通知参与者本地提交

规则：

1. 协调者单点故障
1. 出现参与者响应为不能处理或者事务提交失败，协调者通知所有参与者回滚

问题：
1. 性能问题。参与者越多，事务越复杂，提交过程就越耗时，对数据库性能影响大
1. 协调者单点问题。
1. 数据不一致。 第二阶段协调者通知参与者时，消息或调用丢失

> 3PC

CanCommit、PreCommit、DoCommit

三阶段提交又称3PC，其在两阶段提交的基础上增加了CanCommit阶段，并引入了超时机制。一旦事务参与者迟迟没有收到协调者的Commit请求，就会自动进行本地commit

> TCC

try confirm commit

补偿式事务  针对每个操作都要注册一个与其对应的确认和补偿（撤销操作）
- Try阶段：主要是对业务系统做检测及资源预留。
- Confirm阶段：确认执行业务操作。
- Cancel阶段：取消执行业务操作。


TCC事务的处理流程与2PC两阶段提交类似，不过2PC通常都是在跨库的DB层面，而TCC本质上就是一个应用层面的2PC，需要通过业务逻辑来实现。  
这种分布式事务的实现方式的优势在于，可以让应用自己定义数据库操作的粒度，使得降低锁冲突、提高吞吐量成为可能。

而不足之处则在于对应用的侵入性非常强，业务逻辑的每个分支都需要实现try、confirm、cancel三个操作。  
此外，其实现难度也比较大，需要按照网络状态、系统故障等不同的失败原因实现不同的回滚策略。为了满足一致性的要求，confirm和cancel接口还必须实现幂等。
