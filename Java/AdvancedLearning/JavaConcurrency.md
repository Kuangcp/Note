---
title: Java并发
date: 2018-11-21 10:56:52
tags: 
    - Concurrency
categories: 
    - Java
---

💠

- 1. [Java并发](#java并发)
    - 1.1. [JMM Java内存模型](#jmm-java内存模型)
    - 1.2. [理论知识](#理论知识)
        - 1.2.1. [可能的问题](#可能的问题)
        - 1.2.2. [好的习惯](#好的习惯)
- 2. [关键字](#关键字)
    - 2.1. [synchronized](#synchronized)
        - 2.1.1. [正确使用](#正确使用)
    - 2.2. [volatile](#volatile)
        - 2.2.1. [正确使用](#正确使用)
- 3. [现代并发JUC包](#现代并发juc包)
    - 3.1. [概念](#概念)
        - 3.1.1. [读写锁](#读写锁)
    - 3.2. [实现类](#实现类)
        - 3.2.1. [原子类](#原子类)
        - 3.2.2. [Lock](#lock)
        - 3.2.3. [CountDownLatch](#countdownlatch)
        - 3.2.4. [CyclicBarrier](#cyclicbarrier)
        - 3.2.5. [Semaphore](#semaphore)
        - 3.2.6. [Phaser](#phaser)
        - 3.2.7. [Exchanger](#exchanger)
        - 3.2.8. [ConcurrentHashMap](#concurrenthashmap)
        - 3.2.9. [ConcurrentSkipListMap](#concurrentskiplistmap)
        - 3.2.10. [CopyOnWriteArrayList](#copyonwritearraylist)
- 4. [结构化并发](#结构化并发)
- 5. [实践](#实践)
    - 5.1. [任务建模](#任务建模)
    - 5.2. [Queue](#queue)
        - 5.2.1. [BlockingQueue interface](#blockingqueue-interface)
            - 5.2.1.1. [TransferQueue interface](#transferqueue-interface)

💠 2024-09-25 13:38:51
****************************************
# Java并发
> [个人相关代码](https://github.com/Kuangcp/JavaBase/tree/concurrency)  

> 主要知识来源 Java程序员修炼之道  | [并发编程网](http://ifeve.com/)  

> 该模块最早在JDK1.5引入,由 [Doug Lea](http://g.oswego.edu/) 开发 |  [doug lea博客中文版](http://ifeve.com/doug-lea/)

> [参考: 并发编程 ](http://www.jdon.com/concurrency.html)
> [参考: 不可变真的意味线程安全？](http://www.jdon.com/concurrent/immutable.html)
> [Java Concurrency and Multithreading Tutorial](http://tutorials.jenkov.com/java-concurrency/index.html)  

![](/Java/AdvancedLearning/Concurrency/img/001-concurrency-base.km.svg)

************************

## JMM Java内存模型
> Java Memory Model

> [Java内存模型是什么](https://mp.weixin.qq.com/s?__biz=MjM5OTMyNzQzMg==&mid=2257483738&idx=1&sn=856847463cc602962d027aa80dd55a6f&chksm=a447f47d93307d6b4f7bc74bf5dc502d306c01915c10da7ee924926dd8258c241b4265c23f4e&mpshare=1&scene=1&srcid=#rd)`借助CPU的多级缓存的概念理解线程间内存模型`

- JMM 的主要规则：
    - 在监测对象上的解锁操作与后续的所操作之间存在同步约束关系
    - 对易失性变量的写入与后续对该变量的读取之间存在同步约束关系
    - 如果动作A受到动作B的同步约束，则A在B之前发生
    - 如果在程序中的线程内A出现B之前，则A在B之前发生
    - 前两个简称为先存后取 
- 敏感行为：
    - 构造方法要在那个对象的终结期之前完成（一个对象被终结之前必须已经构造完整）
    - 开始一个线程的动作受到这个新线程的第一个动作的同步制约
    - Thread.join() 受到被合并的线程的最后一个动作的同步制约
    - 如果X在Y之前发生，并且Y在Z之前发生， 则X在Z之前发生（传递性）
- 重要概念： `如果对象不可改变，确保改变对所有线程可见的相关问题就不会出现`

- 代码块之间的 `之前发生（Happens-Before）` 和 `同步约束（Synchronizes-With）`关系
    - 之前发生 这种关系表明一段代码在其他代码开始之前就已经全部完成了
    - 同步约束 这意味着动作继续执行之前必须把他的对象视图与主内存同步

************************

## 理论知识
`线程模型`
- 共享的，默认可见的可变状态
- 抢占式线程调度

`concurrent包的设计理念`
- 安全性 （并发类型安全性）
    - 并发类型安全：不管发生多少操作都能保证对象保持自相一致。一般采用的是将所有属性私有化
- 活跃度
    - 在一个活跃的系统中，所有做出尝试的活动最终或者取得进展，或者失败
    - 可能出现瞬时故障的情况：
        - 处于锁定状态，或者在等待得到线程锁
        - 等待输入
        - 资源的暂时故障
        - CPU没有足够的空闲时间运行该线程 
    - 永久故障的常见原因：
        - 死锁
        - 不可恢复的资源问题（例如 NFS不可访问）
        - 信号丢失
- 性能
    - 测量系统用给定的资源能做多少工作
- 可重用性

- 完全同步对象 策略 一个满足下面所有条件的类就是完全同步类：
    - 所有域在任何公共构造方法中的初始化都能达到一致的状态
    - 没有公共域
    - 从任何非私有方法返回后，都可以保证对象实例处于一致的状态  假定调用方法时状态是一致的
    - 所有方法经证明都可在有限时间内终止
    - 所有方法都是同步的
    - 当处于非一致的状态时，不会调用其他实例的方法，以及调用非私有方法

- 不可变性：
    - 这些对象或者没有状态（属性）或者只有final域。因为他们的状态不可变，所以是安全而又活泼，不会出现不一致的情况
    - 初始化就会遇上问题，如果是需要初始化很多属性，可以采用工厂模式，但是构建器模式更好。
        - 一个是实现了构建器泛型接口的内部静态类，另一个是构建不可变类实例的私有构造方法 
        - [实现代码](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/main/java/com/github/kuangcp/old/BuildFactory.java)
    - 不可变对象中的final域特别要注意：
        - final声明的对象的引用是不可变的， 但是如果引用的是对象，该对象自身的属性的引用是可变的
    - 不可变对象的使用十分广泛，但是开发效率不行，每修改对象的状态都要构建一个新对象


### 可能的问题
- 安全性与活跃度相对立，安全性求稳定安全，活跃度是求进展
- 可重用的系统倾向于对外开放内核，这会引发安全问题
- 一个安全但是编写幼稚的系统性能通常不会好，因为里面会用大量的锁来保证安全

### 好的习惯
1. 尽可能限制子系统之间的通信，隐藏数据对安全性非常有帮助
2. 尽可能保证子系统内部结构的确定性，
    - 比如：即便子系统会以并发的，非确定性的方式进行交互，子系统内部的设计也应该按照线程和对象的静态知识
3. 采用客户端应用必须遵守的规则。
    - 这个技巧虽然强大，但是依赖于用户应用程序的合作程度，如果某个糟糕的应用不遵守规则，排查问题很困难
4. 在文档中记录所要求的行为，这是最逊的方法，但如果代码要部署在非常通用的环境下，就必须采用这个方法

***********

- 系统开销之源: 锁与监测, 环境切换的次数, 线程的个数, 调度, 内存的局部性, 算法设计

# 关键字
## synchronized
在synchronized代码块执行完成后，对锁定对象所做的所有修改全部会在线程释放锁之前同步到内存中, 具有可重入性

- 同步和锁 synchronized：
    - 只能锁定对象，不能锁定原始类型
    - 锁的范围要尽可能的小
    - 被锁定的兑现给数组中的单个对象不会被锁定
    - 同步方法可以视为包含整个方法的同步 `(this){...}`代码块 但是两者的二进制码的表示是不同的
    - 静态方法会锁定其Class对象，因为没有实例对象可以锁定
    - 如果要锁定一个对象，请慎重考虑使用显式锁定，还是getClass()， 两种方式对子类影响不同
    - 内部类的同步是独立于外部类的
    - synchronized 并不是方法签名的组成部分，所以不能出现在接口的方法声明中
    - 非同步的方法不查看或关心任何锁的状态，而且在同步方法运行时，他们仍能继续运行
    - Java的线程锁是可重入的。也就是说持有线程锁的线程在遇到同一个锁的同步点 时是可以继续的
        - 比如 一个同步方法调用另一个类的另一个同步方法

- [JDK15 将移除 偏向锁](https://openjdk.java.net/jeps/374)

- 保证了在同一时刻,只有一个线程可以执行某一个方法或者代码块. 保证了线程对变量访问的可见性和排他性
- 所以这个关键字的作用就是同步 在不同线程中锁定（操作）的对象的内存块
    - 同步的作用不仅仅是互斥,另一个作用就是共享可变性, 当某个线程修改了可变数据并释放锁,其他线程可以获取变量的最新值
    - 如果没有正确的同步,这种修改对其他线程是不可见的

>1. 如果锁定的是类的成员属性,或者this, 就是对该对象进行了加锁, 该对象上的线程串行化, 影响了整体性能
>2. 使用局部变量能保持多线程性能 且保证了数据的一致性
>3. 切记不能锁常量（或者显式声明的String）从而引发死锁

对应于字节码中的指令是 monitorenter 和 monitorexit 

### 正确使用
> 查看JDK源码 ForkJoinTask 的 externalAwaitDone 方法

1. wait方法用来使线程等待某个条件, 他必须在同步块内部被调用,这个同步块通常会锁定当前对象实例.
    ```java
        // 这个模块的标准使用方式
        synchronized(this){
            while(condition){
                Object.wait();
            }
        }
    ```
2. 始终使用wait循环来调用wait方法, 永远不要在循环之外调用wait方法
    - 因为有时候, 即使并不满足被唤醒条件,但是由于其他线程调用notifyAll()方法会导致被阻塞的线程意外唤醒,从而导致不可预料的结果
3. 唤醒线程,保守的做法是使用notifyAll唤醒所有等待的线程,从优化的角度看,如果处于等待的所有线程都在等待同一个条件,而每次只有一个线程可以从这个条件中被唤醒, 那么就应该选择调用notify
> 当多个线程共享一个变量的时候,每个读写都必须加锁进行同步, 如果没有正确的同步,就容易造成程序的活性失败和安全性失败,这样的失败是很难复现的.所以务必要保证锁的正确使用

************************

```java
// 这个就是个错误使用的案例
int size = 0;
public synchronized void increase(){
    size++;
}
public int current(){
    return size;
}
```
> 这个案例保证了多线程下并发时,对size变量的正确修改,但是不能保证实时读取到的变量值是正确的  
> 正确的做法是 current 方法也要加上synchronized关键字

## volatile
> [Java多线程i++线程安全问题，volatile和AtomicInteger解释？](https://segmentfault.com/q/1010000006733274)
> [DCL的单例一定是线程安全的吗](https://www.cnblogs.com/amberJava/p/12546798.html)`如果new 还需要自定义初始化逻辑，需要使用本地变量初始化完成后赋值给对象属性`

- 线程所读的值在使用之前总会从内存中读入线程缓存
- 线程所写的值总会在指令完成之前同步回内存中
    - 可以把围绕该域的操作看成是一个小的同步块
    - volatile 变量不会引入线程锁，所以不可能发生死锁
    - volatile 变量是真正线程安全的，但只有`写入时不依赖当前状态的变量`才应该声明为volatile变量

- volatile是Java提供的最轻量级的同步机制,Java内存模型为volatile专门定义了一些特殊的访问规则, 当一个变量被volatile修饰后:
    - `线程可见性`  当一个线程修改了被volatile修饰的变量后,无论是否加锁,其他线程都能立即看到最新的修改
    - `禁止指令重排序优化` 普通的变量仅仅保证在该方法的执行过程中, 所有依赖赋值结果的地方都能获取正确的结果,而不能保证变量赋值操作的顺序和程序代码的执行顺序一致
        - 实现原理是在指令序列中插入了内存屏障： 
            - volatile 写操作前 StoreStore 后 StoreLoad
            - volatile 读操作前 LoadLoad 后 LoadStore


### 正确使用
> 打开Netty中NioEventLoop的源码 有一个属性 `private volatile int ioRatio = 50;` 该变量是用于控制IO操作和其他任务运行比例的

```java
    public class ResortJavaDemo {
        private static boolean stop;
        public static void main(String[]s) throws InterruptedException {
            Thread workThread = new Thread(() -> {
                int i = 0;
                while(!stop){
                    i++;
                    try {
                        TimeUnit.SECONDS.sleep(1);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println("i"+i);
                }
            });
            workThread.start();
            TimeUnit.SECONDS.sleep(3);
            stop = true;
        }
    }
```
> 我们预期程序会在3s后停止, 但是实际上它会一直执行下去, 原因就是虚拟机对代码进行了指令重排序和优化, 优化后的指令如下:
```java
    if (!stop)
        while(true)
```
> 所以需要在stop前加上volatile修饰符, 解决了如下两个问题
>> 1. main线程对stop的修改在workThread中可见
>> 2. 禁止指令重排序, 防止因为重排序导致的并发访问逻辑混乱

- 注意 以上示例代码在Java8中是正常运行的, 并不会一直执行下去, 所以还需要找个别的Demo过来

> 一些人认为volatile可以替代传统锁,提升并发性能, 这个认识是错误的. volatile仅仅解决了可见性的问题, 并不能保证互斥性
>> volatile最适合使用的是一个线程写, 其他线程读的场景. 
>> 如果有多个线程并发`写`操作,仍然需要使用`锁`或者`线程安全的容器`或者`原子变量`来代替

****************************

# 现代并发JUC包
> 简称为J.U.C (java.util.concurrent) | [The j.u.c Synchronizer Framework中文翻译版](http://ifeve.com/aqs/)
- 建议通过使用`线程池`,`Task(Runnable/Callable)`,`读写锁`,`原子类`和`线程安全容器`来代替传统的同步锁,wait和notify
    - 提升并发访问的性能, 降低多线程编程的难度, Netty就是这么做的

> 线程安全容器底层使用了CAS,volatile,和ReadWriteLock实现

- ReentrantLock 和 sync 加解锁机制的区别?  
    - 一个作用于线程一个作用于临界变量
- 不要依赖线程优先级

> [The java.util.concurrent Synchronizer FrameworkDoug Le](http://gee.cs.oswego.edu/dl/papers/aqs.pdf) `AQS`

## 概念
### 读写锁
> 在读多写少的场景下, 使用读写锁比同步块性能要好

- 获取的读锁是共享锁
- 获取写锁时会阻塞所有读锁和写锁

*****************

## 实现类
> [JUC - 类汇总和学习指南](https://pdai.tech/md/java/thread/java-thread-x-juc-overview.html)

### 原子类 
> [原子类](/Java/AdvancedLearning/Concurrency/Atomic.md)  

### Lock 
> `java.util.concurrent.locks`
- 块结构同步方式基于锁这样的的概念，具有缺点
    - 锁只有一种类型
    - 对被锁住的对象的所有同步操作都是一样的作用
    - 在同步代码块或方法开始时取得线程锁
    - 在同步代码块或方法结束时释放线程锁
    - 线程或者得到锁，或者阻塞，没有其他可能
    
- 如果要重构对线程锁的支持， 事实上该包下Lock接口也都实现了：
    - 添加不同类型的锁，例如 读取锁和写入锁
    - 对锁的阻塞没有限制，允许在一个方法中加锁，另一个方法中解锁
    - 如果线程得不到锁（例如已经被线程加锁），就允许该线程后退或者继续执行，或者做别的事情 tryLock()
    - 允许线程尝试锁，并可以在超过时间后放弃
    - Lock接口的实现类：ReentrantLock 本质上和用在同步块上的锁是一样的，但是稍微灵活些
        - `lock()`: [官方API1.8 lock](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/locks/ReentrantLock.html#lock--)
        - 如果该锁没有被另一个线程保持，则获取该锁并立即返回，将锁的保持计数设置为 1。
        - 如果当前线程已经保持该锁，则将保持计数加 1，并且该方法立即返回。
        - 如果该锁被另一个线程保持，则出于线程调度的目的，禁用当前线程，并且在获得锁之前，该线程将一直处于休眠状态，此时锁保持计数被设置为 1。
        - `trylock()`: [官方API1.8 trylock](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/locks/ReentrantLock.html#tryLock--)
    - Lock接口的实现类：ReentrantWriteLock 在需要读取很多线程而写入很少线程时，用这个性能更好
    
### CountDownLatch
是一种简单的同步模式，这种模式允许线程在通过同步屏障之前做少量的准备工作, 构建实例时，需要提供一个数值（计数器），通过两个方法来实现这个机制

- `countDown()` 作用：计数器减一
    - 如果当前计数大于零，则将计数减少。然后什么都不做
        - 如果减后的计数为零，出于线程调度目的，将重新启用所有的等待线程 
    - 如果当前计数等于零，则不发生任何操作。
- `await()` 作用：让线程在计数器到0之前一直等待，
    - 如果大于 0 ， 休眠这语句所处的当前线程 
        - 例如 `a.await()` 如果锁存器a的Count不为0 ，就把当前线程休眠掉
    - 如果已经是小于等于0 就什么都不做
        
支持场景：一堆线程间的状态同步，为了确保有指定数量正常初始化的线程 创建成功 后 继续执行逻辑 

### CyclicBarrier

### Semaphore
> 最早用来解决进程同步与互斥问题的机制, 整体设计来自于操作系统。[Linux Semaphore](/Linux/Base/LinuxBase.md#信号量-semaphore)

> [JUC工具类: Semaphore详解](https://pdai.tech/md/java/thread/java-thread-x-juc-tool-semaphore.html)

### Phaser

### Exchanger


### ConcurrentHashMap
- `ConcurrentHashMap` 是 HashMap的并发版本
- 修改HashMap，并不需要将整个结构都锁住，只要锁住即将修改的桶（就是单个元素）
    - 好的HashMap 实现，在读取时不需要锁，写入时只要锁住要修改的单个桶 Java能达到这个标准，但是需要程序员去操作底层的细节才能实现
- `ConcurrentHashMap`类 还实现了ConcurrentMap接口，有些提供了还提供了原子操作的新方法
    - `putIfAbsent()` 如果还没有对应键，就把键/值添加进去
    - `remove()` 如果键存在而且值与当前状态相等，则用原子方式移除键值对
    - `replace()` API 为HashMap中原子替换的操作方法提供了两种不同的形式
- key value 均不允许为null

> 1.7 到 1.8 改动
- 数据结构：取消了 Segment 分段锁的数据结构，取而代之的是数组+链表+红黑树的结构。
- 保证线程安全机制：JDK1.7 采用Segment 的分段锁机制实现线程安全，其中 Segment 继承自 ReentrantLock 。JDK1.8采用CAS+synchronized保证线程安全。
- 锁的粒度：JDK1.7 是对需要进行数据操作的 Segment 加锁，JDK1.8调整为对每个数组元素加锁（Node）。
- 链表转化为红黑树：定位节点的 hash 算法简化会带来弊端，hash冲突加剧，因此在链表节点数量大于 8（且数据总量大于等于 64）时，会将链表转化为红黑树进行存储。
- 查询时间复杂度：从JDK1.7的遍历链表O(n)， JDK1.8 变成遍历红黑树O(logN)。

ConcurrentHashMap的迭代器是弱一致性

### ConcurrentSkipListMap
基于跳表实现的并发有序Map

ConcurrentSkipListMap的迭代器是弱一致性的，它不会抛出ConcurrentModificationException异常，但是无法保证迭代器遍历的元素是一个完整的快照。因此，在迭代器遍历ConcurrentSkipListMap时，可能会遗漏或重复遍历某些元素。

### CopyOnWriteArrayList
- 标准的ArrayList的替代，通过写时复制语义来实现线程安全性，也就是说修改列表的任何操作都会创建一个列表底层数组的新副本
    - 这就意味着所有成形的迭代器都不会遇到意料之外的修改 （脏读）
- 这一般需要很大的开销，但是当遍历操作的数量大大超过可变操作的数量时，这种方法可能比其他替代方法更 有效。在不能或不想进行同步遍历
    - 适用于读操作多于写操作时，比如事件监听器、缓存等
- 但又需要从并发线程中排除冲突时，它也很有用。“快照”风格的迭代器方法在创建迭代器时使用了对数组状态的引用。此数组在迭代器的生存期内不会更改，
- 因此不可能发生冲突，并且迭代器保证不会抛出 ConcurrentModificationException。创建迭代器以后，迭代器就不会反映列表的添加、移除或者更改。
- 在迭代器上进行的元素更改操作（remove、set 和 add）不受支持。这些方法将抛出 UnsupportedOperationException。

***********************
# 结构化并发
[Structured Concurrency](https://openjdk.org/jeps/453)  

************************

# 实践
目标：需要合理设计线程模型，尽量不要让线程阻塞，因为一阻塞，CPU 就闲下来了。

> [Java线程](/Java/AdvancedLearning/JavaThread.md)  [Java线程池](/Java/AdvancedLearning/Concurrency/ExecutorAndPool.md)  

在技术和业务角度，都应该考虑抽象和分层，将近似的事情放在一个线程池内，更有利于针对性设置参数达到整体的效率优化。  
例如Tomcat中的 [NioEndpoint](/Java/Ecosystem/Servlet/TomcatDesign.md#nioendpoint) 将 接受连接，收连接数据，执行连接任务和发送响应，拆分成三个线程池   

## 任务建模
> 要把目标代码做成可调用（执行者调用）的结构，而不是单独开线程运行 [示例代码](https://github.com/Kuangcp/JavaBase/blob/master/concurrency/src/main/java/com/github/kuangcp/schedule/CreateModel.groovy)  

`Callable接口`
- 通常是匿名内部实现类 

`Future接口`
- 用来表示异步任务，是还没有完成的任务的未来结果，主要方法：
    - get() 用来获取结果，如果结果还没准备好就会阻塞直到它能去到结果，有一个可以设置超时的版本，这个版本永远不会阻塞
    - cancel() 运算结束前取消
    - isDone() 调用者用它来判断运算是否结束

`FutureTask类`
- FutureTask是Future接口的常用实现类， 并且是实现了Runnable接口。所以提供的方法是俩接口的方法
    - 提供了两个构造器，一个是Callable为参数，另一个以Runnable为参数
- 可以基于FutureTask的Runnable特性，把任务写成Callable然后封装进一个有执行者地调度并在必要时可以取消的FutureTask

************************

## Queue

|队列| 	有界性| 	锁| 	数据结构|
|:---|:---|:---|:---|
| ArrayBlockingQueue     | 	bounded     | 加锁| 	arraylist|
| LinkedBlockingQueue    | 	optionally-bounded | 加锁|	linkedlist|
| ConcurrentLinkedQueue  | 	unbounded | 无锁| 	linkedlist|
| LinkedTransferQueue    | 	unbounded | 无锁| 	linkedlist|
| PriorityBlockingQueue  | 	unbounded | 加锁| 	heap|
| DelayQueue             | 	unbounded | 加锁| 	heap|

> [高性能队列——Disruptor](https://tech.meituan.com/2016/11/18/disruptor.html)
- [Github](https://github.com/LMAX-Exchange/disruptor) [User Guide](https://lmax-exchange.github.io/disruptor/user-guide/index.html)  
- 经过验证可以发现由于控制是使用无锁的CAS实现，当队列空置时，CPU空耗高占用很明显。也就是说这个队列适合对繁忙且延迟敏感的业务。

### BlockingQueue interface

- 基本方法
    - put() 如果队列已满，会让放入的线程等待 队列腾出空间
    - take() 如果队列为空，会导致取出的线程阻塞
    - offer() 将指定元素插入此队列中（如果立即可行且不会违反容量限制），成功时返回 true，如果当前没有可用的空间，则返回 false。
        - 当使用有容量限制的队列时，此方法通常要优于 add(E)，后者可能无法插入元素，而只是抛出一个异常。
        - 另一个重载方法：将指定元素插入此队列中，在到达指定的等待时间前等待可用的空间（如果有必要）。
    - poll() 获取并移除此队列的头部，在指定的等待时间前等待可用的元素（如果有必要）。
- 基本实现
    - LinkedBlockingQueue 看名字就知道实现方式以及优缺点了
    - ArrayBlockingQueue
- BlockingQueue 不接受 null 元素。试图 add、put 或 offer 一个 null 元素时，某些实现会抛出 NullPointerException。
- BlockingQueue 的实现主要用于生产者-使用者队列


`BlockingQueue<Pro<Author>>`
```java
    public class Pro<T>{
        private T pro;
        public T getPro(){
            return pro;
        }
        public Pro(T pro){
            this.pro = pro;
        }
    }
```
- 有了这层间接引用， 不用牺牲所包含类型（Author）在概念上的完整性，就能够添加额外的元数据了。方便统一性的修改
    - 用上额外元数据的用例：
    - 测试： 比如 展示一个对象的修改历史
    - 性能指标： 比如 到达时间，服务质量
    - 运行时系统信息： 比如 Author实例是如何排到队列的


#### TransferQueue interface
- 本质上是多了一项 transfer()操作的BlockingQueue， 如果接收线程处于等待状态， 该操作会马上把工作项传给他。
- 否则就会阻塞直到取走工作项的线程出现 即 正在处理工作项的线程在交付当前工作项之前不会开始其他工作项的处理工作，
- 这样系统就可以调控上游线程获取新工作项的速度 用限定大小的阻塞队列也能达到同样的效果，TransferQueue 执行效率更高
    - 但是这个只有链表的实现版本
    - 相比于BlockingQueue 用法一致， offer() 等价于 tryTransfer() 参数也是一致的，代码基本不需要改动
