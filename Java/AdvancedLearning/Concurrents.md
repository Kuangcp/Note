`目录 start`
 
- [Java并发](#java并发)
    - [Java内存模型](#java内存模型)
    - [【理论知识】](#理论知识)
        - [可能的问题](#可能的问题)
        - [好的习惯](#好的习惯)
    - [【块结构并发】 Java5之前](#块结构并发-java5之前)
        - [synchronized](#synchronized)
            - [正确使用锁](#正确使用锁)
        - [volatile](#volatile)
            - [正确使用](#正确使用)
    - [【现代并发】JUC](#现代并发juc)
        - [概念](#概念)
            - [CAS指令](#cas指令)
            - [原子类](#原子类)
            - [读写锁](#读写锁)
        - [具体实现](#具体实现)
            - [线程锁](#线程锁)
            - [CountDownLatch 锁存器](#countdownlatch-锁存器)
            - [ConcurrentHashMap](#concurrenthashmap)
            - [CopyOnWriteArrayList](#copyonwritearraylist)
    - [【Queue】](#queue)
        - [BlockingQueue](#blockingqueue)
        - [TransferQueue](#transferqueue)
    - [【控制执行】](#控制执行)
        - [任务建模](#任务建模)
            - [ScheduleThreadPoolExecutor](#schedulethreadpoolexecutor)
    - [【分支合并框架】](#分支合并框架)
    - [【Java内存模型】](#java内存模型)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Java并发
> [个人相关代码](https://github.com/Kuangcp/JavaBase/tree/master/src/main/java/com/concurrents)  
> 主要知识来源 Java程序员修炼之道  | [并发编程网](http://ifeve.com/)  
> 该模块最早在1.5引入,由[Doug Lea](http://g.oswego.edu/)开发 |  [doug lea博客中文版](http://ifeve.com/doug-lea/)

> [参考博客: 并发编程 ](http://www.jdon.com/concurrency.html)
> [参考博客: 不可变真的意味线程安全？](http://www.jdon.com/concurrent/immutable.html)

## Java内存模型

## 【理论知识】
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
- 系统开销之源
    - 锁与监测
    - 环境切换的次数
    - 线程的个数
    - 调度
    - 内存的局部性
    - 算法设计
    
## 【块结构并发】 Java5之前
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
      

![线程状态模型](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Java/concurrent/Model.jpg)  
- 线程的状态模型：
    - 线程创建时处于准备（Ready）状态，然后调度器会准备执行
    
- 完全同步对象 策略 一个满足下面所有条件的类就是完全同步类：
    - 所有域在任何公共构造方法中的初始化都能达到一致的状态
    - 没有公共域
    - 从任何非私有方法返回后，都可以保证对象实例处于一致的状态  假定调用方法时状态是一致的
    - 所有方法经证明都可在有限时间内终止
    - 所有方法都是同步的
    - 当处于非一致的状态时，不会调用其他实例的方法，以及调用非私有方法
  
### synchronized
- 在synchronized代码块执行完成后，对锁定对象所做的所有修改全部会在线程释放锁之前同步到内存中
    - 保证了在同一时刻,只有一个线程可以执行某一个方法或者代码块.
    - 所以这个关键字的作用就是同步 在不同线程中锁定（操作）的对象的内存块
        - 同步的作用不仅仅是互斥,另一个作用就是共享可变性, 当某个线程修改了可变数据并释放锁,其他线程可以获取变量的最新值
        - 如果没有正确的同步,这种修改对其他线程是不可见的

>1. 如果锁定的是类的成员属性,或者this, 就是对该对象进行了加锁变成了'单线程', 就影响了整体性能
>2. 使用局部变量就会多线程且保证了数据的一致性
>3. 切记不能锁常量（或者显式声明的String）从而引起死锁

#### 正确使用锁
> 查看JDK源码 ForkJoinTask 的 externalAwaitDone 方法

- 1.wait方法用来使线程等待某个条件, 他必须在同步块内部被调用,这个同步块通常会锁定当前对象实例.
```java
// 这个模块的标准使用方式
synchronized(this){
    while(condition){
        Object.wait();
    }
}
```
- 2.始终使用wait循环来调用wait方法, 永远不要在循环之外调用wait方法
    - 因为有时候, 即使并不满足被唤醒条件,但是由于其他线程调用notifyAll()方法会导致被阻塞的线程意外唤醒,从而导致不可预料的结果
- 3.唤醒线程,保守的做法是使用notifyAll唤醒所有等待的线程,从优化的角度看,如果处于等待的所有线程都在等待同一个条件,而每次只有一个线程可以从这个条件中被唤醒, 那么就应该选择调用notify
> 当多个线程共享一个变量的时候,每个读写都必须加锁进行同步, 如果没有正确的同步,就容易造成程序的活性失败和安全性失败,这样的失败是很难复现的.所以务必要保证锁的正确使用

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

### volatile
> [Java多线程i++线程安全问题，volatile和AtomicInteger解释？](https://segmentfault.com/q/1010000006733274)

- 线程所读的值在使用之前总会从内存中读出来
- 线程所写的值总会在指令完成之前同步回内存中
    - 可以把围绕该域的操作看成成是一个小的同步块
    - volatile 变量不会引入线程锁，所以不可能发生死锁
    - [ ] TODO 矛盾
    - volatile 变量是真正线程安全的，但只有写入时不依赖当前状态（读取的状态）的变量才应该声明为volatile变量

#### 正确使用
> 打开Netty中NioEventLoop的源码 有一个属性 `private volatile int ioRatio = 50;` 该变量是用于控制IO操作和其他任务运行比例的
- volatile是Java提供的最轻量级的同步机制,Java内存模型为volatile专门定义了一些特殊的访问规则:
    - 当一个变量被volatile修饰后:
        - 线程可见性: 当一个线程修改了被volatile修饰的变量后,无论是否加锁,其他线程都能立即看到最新的修改
        - 禁止指令重排序优化, 普通的变量仅仅保证在该方法的执行过程中, 所有依赖赋值结果的地方都能获取正确的结果
            - 而不能保证变量赋值操作的顺序和程序代码的执行顺序一致
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

- 以上示例代码在Java8中是正常运行的, 并不会一直执行下去, 所以还需要找个别的Demo过来

> 一些人认为volatile可以替代传统锁,提升并发性能, 这个认识是错误的. volatile仅仅解决了可见性的问题, 并不能保证互斥性
>> volatile最适合使用的是一个线程写, 其他线程读的场景. 
>> 如果有多个线程并发`写`操作,仍然需要使用`锁`或者`线程安全的容器`或者`原子变量`来代替

****************************
- 不可变性：
    - 这些对象或者没有状态（属性）或者只有final域。因为他们的状态不可变，所以是安全而又活泼，不会出现不一致的情况
    - 初始化就会遇上问题，如果是需要初始化很多属性，可以采用工厂模式，但是构建器模式更好。
        - 一个是实现了构建器泛型接口的内部静态类，另一个是构建不可变类实例的私有构造方法 
        - [思想实现代码](./src/main/java/com/concurrents/old/BuildFactory.java)
    - 不可变对象中的final域特别要注意：
        - final声明的对象的引用是不可变的， 但是如果引用的是对象，该对象自身的属性的引用是可变的
    - 不可变对象的使用十分广泛，但是开发效率不行，每修改对象的状态都要构建一个新对象

## 【现代并发】JUC
> 简称为J.U.C (java.util.concurrent) | [The j.u.c Synchronizer Framework中文翻译版](http://ifeve.com/aqs/)
- 建议通过使用`线程池`,`Task(Runnable/Callable)`,`读写锁`,`原子类`和`线程安全容器`来代替传统的同步锁,wait和notify
    - 提升并发访问的性能, 降低多线程编程的难度, Netty就是这么做的

> 线程安全容器底层使用了CAS,volatile,和ReadWriteLock实现

- ReentrantLock 和 sync 加解锁机制的区别?  
    - 一个作用于线程一个作用于临界变量
- 不要依赖线程优先级
### 概念
#### CAS指令
> 互斥同步最主要的问题就是进行线程阻塞和唤醒所带来的性能额外损耗, 因此这种同步也被称为阻塞同步,悲观锁
>> 与之对应的乐观锁是, 先进行操作, 操作完成之后再判断操作是否成功, 是否有并发问题, 如果有则进行失败补偿, 如果没有就算操作成功. 

> Java中的非阻塞同步就是CAS 1.5就有了

#### 原子类 
> `java.util.concurrent.atomic` 提供适当的原子方法 避免在共享数据上出现竞争危害的方法  
> 使用Java自带的原子类, 可以避免同步锁带来的并发访问性能降低的问题, 减少犯错的机会. 对于 int, long, boolean 等成员变量大量使用原子类
>> 但是使用者必须通过类似 compareAndSet或者set或者与这些操作等价的`原子操作`来保证更新的原子性.

- 常见的操作系统的支持， 他们是非阻塞的（无需线程锁）， 常见的方法是实现序列号机制（和数据库里的序列号机制类似），在`AtomicInteger`或`AtomicLong`上用原子
    - 操作`getAndIncrement()`方法， 并且提供了nextId 方法得到唯一的完全增长的数值
- 注意： 原子类不是相似的类继承而来，所以 AtomicBoolean不能当Boolean用

#### 读写锁
> 在读多写少的场景下, 使用同步锁比同步块性能要好

- 读锁 ReentranReadWriteLock 是共享锁
*****************
### 具体实现
#### 线程锁 
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
    
#### CountDownLatch 锁存器
- 是一种简单的同步模式，这种模式允许线程在通过同步屏障之前做少量的准备工作
    - 构建实例时，需要提供一个数值（计数器），通过两个方法来实现这个机制
    - `countDown()` 作用：计数器减一
        - 如果当前计数大于零，则将计数减少。然后什么都不做
            - 如果减后的计数为零，出于线程调度目的，将重新启用所有的等待线程 
        - 如果当前计数等于零，则不发生任何操作。
        
    - `await()` 作用：让线程在计数器到0之前一直等待，
        - 如果大于 0 ， 休眠这语句所处的当前线程 
            - 例如 `a.await()` 如果锁存器a的Count不为0 ，就把当前线程休眠掉
        - 如果已经是小于等于0 就什么都不做
        
- 能做到： 当一堆线程之间的同步，为了确保有指定数量正常初始化的线程 创建成功，才能开始同步 

#### ConcurrentHashMap
- `ConcurrentHashMap` 是 HashMap的并发版本
- 修改HashMap，并不需要将整个结构都锁住，只要锁住即将修改的桶（就是单个元素）
    - 好的HashMap 实现，在读取时不需要锁，写入时只要锁住要修改的单个桶 Java能达到这个标准，但是需要程序员去操作底层的细节才能实现
- `ConcurrentHashMap`类 还实现了ConcurrentMap接口，有些提供了还提供了原子操作的新方法
    - `putIfAbsent()` 如果还没有对应键，就把键/值添加进去
    - `remove()` 如果键存在而且值与当前状态相等，则用原子方式移除键值对
    - `replace()` API 为HashMap中原子替换的操作方法提供了两种不同的形式
- 例如之前的完全同步类里的公共 Map实现就是HashMap，如果换成ConcurrentHashMap 那些synchronized关键字修饰的方法就可以换成普通方法了
- 该类不仅提供了多线程的安全性，性能也很好

#### CopyOnWriteArrayList
- 标准的ArrayList的替代，通过写时复制语义来实现线程安全性，也就是说修改列表的任何操作都会创建一个列表底层数组的新副本
    - 这就意味着所有成形的迭代器都不会遇到意料之外的修改 （脏读）
    
- 这一般需要很大的开销，但是当遍历操作的数量大大超过可变操作的数量时，这种方法可能比其他替代方法更 有效。在不能或不想进行同步遍历
    - 当读操作大于写操作会比较好用，
- 但又需要从并发线程中排除冲突时，它也很有用。“快照”风格的迭代器方法在创建迭代器时使用了对数组状态的引用。此数组在迭代器的生存期内不会更改，
- 因此不可能发生冲突，并且迭代器保证不会抛出 ConcurrentModificationException。创建迭代器以后，迭代器就不会反映列表的添加、移除或者更改。
- 在迭代器上进行的元素更改操作（remove、set 和 add）不受支持。这些方法将抛出 UnsupportedOperationException。

***********************

## 【Queue】

- Queue接口全是泛型的，这样就更为方便， 自己再封装一个层

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

    
### BlockingQueue
> 并发扩展类， 

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

### TransferQueue 
- 本质上是多了一项 transfer()操作的BlockingQueue， 如果接收线程处于等待状态， 该操作会马上把工作项传给他。
- 否则就会阻塞直到取走工作项的线程出现 即 正在处理工作项的线程在交付当前工作项之前不会开始其他工作项的处理工作，
- 这样系统就可以调控上游线程获取新工作项的速度 用限定大小的阻塞队列也能达到同样的效果，TransferQueue 执行效率更高
    - 但是这个只有链表的实现版本
    - 相比于BlockingQueue 用法一致， offer() 等价于 tryTransfer() 参数也是一致的，代码基本不需要改动

************************

## 【控制执行】
### 任务建模
> 要把目标代码做成可调用（执行者调用）的结构，而不是单独开线程运行
> [展示代码](./src/main/java/com/concurrents/schedule/CreateModel.groovy)

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

#### ScheduleThreadPoolExecutor
> ScheduleThreadPoolExecutor  简称 STPE 线程池类中很重要的类

- 线程池的大小可以预定义， 也可自适应
- 所安排的任务可以定期执行，也可只运行一次
- STPE扩展了ThreadPoolExecutor类，很相似但不具备定期调度能力
    - STPE和并发包里的类结合使用是常见的模式之一

**************************

## 【分支合并框架】 
- 引入一种新的执行者服务，称为 ForkJoinPool
- ForkJoinPool 服务处理一种比线程更小的并发单元 ForkJoinTask
    - ForkJoinTask是一种由ForkJoinPool以更轻量的方式所调度的抽象
- 通常使用两种任务
    - 小型 无需处理器耗时太久的任务
    - 大型 需要在直接执行前进行分解（可能多次）的任务
- 提供了支持大型任务分解的基本方法，还有自动调度和重新调度的能力

- 这个框架的关键特性之一就是：这些轻量的任务都能够生成新的ForkJoinTask实例，而这些实例仍然由执行他们父任务的线程池来安排调度，这就是分而治之
- 工作窃取：
- [一个简单的例子](./src/main/java/com/concurrents/forkjoin/ForkJoinEasyDemo.groovy)

- 由 RecursiveAction 或者 RecursiveTask 派生出来的才能作为任务单元 这俩也是派生ForkJoinTask而来
    - RecursiveAction 要重写的方法：`protected void compute()`  
    - RecursiveTask 要重写的的方法：`protected Object compute()`
- ForkJoinTask里的 invoke 和 invokeAll 
    - `public final V invoke()`
    - invoke  执行此任务的开始，如果有必要，等待它的完成，并返回其结果，或者在底层计算完成时抛出一个(未检查的)RuntimeException或错误。
    - `public static <T extends ForkJoinTask<?>> Collection<T> invokeAll(Collection<T> tasks)`
    - invokeAll 方法的特点是多个执行，但是只有其中有一个是出现了异常，就会取消所有的task

`ForkJoinTask和工作窃取`
- ForkJoinTask作为RecursiveAction的超类，他是从动作中返回结果的泛型类型，所以这个类扩展了ForkJoinTask<Void> 
    - 这使得ForkJoinTask非常适合用MapReduce方式（Google踢出的软件架构，用于大规模数据集的并行计算）返回数据集中归结出的结果
- ForkJoinTask由ForkJoinPool调度安排，这个池是一个特殊的执行者服务。这个服务维护每个线程的任务列表，并且当某个任务完成的时候，
    - 他能把挂在满负荷线程上的任务重新安排到空闲线程上去 这就是 `工作窃取`

`并行问题`
- 可以使用分支合并方法解决的问题：
    - 模拟大量简单对象的运动，例如粒子效果
    - 日志文件分析
    - 从输入中计数的数据操作，比如mapreduce操作
- 以下的列表检查当前问题及其子任务是一个切实有效的方法，确认是否能用分支合并来解决问题
    - 问题的子任务是否无需与其他子任务有显式的协作或同步也可以工作？
    - 子任务是不是不会对数据进行修改，只是经过计算得出些结果？
    - 对于子任务来说，分而治之是不是很自然的事？子任务是不是会创建更多的子任务，而且他们要比派生出他们的任务粒度更细？
    - 如果思考的结果是肯定的，就可以适用，如果思考结果是不确定的，用其他的同步方式更合适

## 【Java内存模型】
> Java Memory Model   JMM

- 同步动作和被称为偏序的数据结构描述JMM， 
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
