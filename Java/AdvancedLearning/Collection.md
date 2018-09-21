`目录 start`
 
- [集合](#集合)
    - [集合继承和实现关系](#集合继承和实现关系)
    - [Iterator](#iterator)
    - [Map](#map)
        - [HashMap 实现原理](#hashmap-实现原理)
    - [List](#list)
    - [Set](#set)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 集合
> 重要的知识点，面试必问，使用频率也很高

## 集合继承和实现关系

- Collection 接口
    - List 接口  
        - ArrayList
        - LinkedList _也实现了Queue接口_ 双向链表实现
        - Vector
    - Set 接口 _内容不允许重复_
    - Queue 接口 _队列接口_
    - SortedSet 接口 _单值排序接口_

- Map接口
    - HashMap接口 _无序, key不重复_
    - HashTable接口 _无序, key不重复_
    - TreeMap接口 _按key排序, key不重复_
    - IdentityMap接口 _key可重复_
    - WeakHashMap接口 _弱引用Map集合_

## Iterator
> 迭代器

********************
## Map


### HashMap 实现原理
- [HashMap 实现原理](http://www.importnew.com/27043.html)

- [ ] 整理实现

主要看 addVal 方法 以及 resize方法的实现
HashMap的数据结构是 数组加单链表 (数组是只放一个Node对象, 单链表是为了放通过hash计算得到的index一致的元素包装成的Node对象)

n 是数组大小
先 hash (高16和低16做异或)然后 hash&(n-1) 就是结果 (也就是数组的下标) putVal()

Node数组 大小 是 使用容量达到0.75 就扩容(翻倍), 初始化大小也要是2的幂
    - 扩容就要重新分布单链表 resize()
    - 如果是链表的最后一个节点 Hash & (32-1) 计算位数
    - 如果hash 二进制倒数第五位是0, 那么扩容后, 位置就不变 (16 -> 32)
    - 如果是1 1+oldCap(16)

链表就是内部类 Node list方式, 然后 如果节点大于8就转红黑树, 当减少到6后退回到list方式
********************************************

## List
> interface 

包括的方法有:
![List method](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Java/Collection/List/List.png)

List接口有众多实现, 最常用的ArrayList LinkedList 

******************************
[stackoverflow: list add then unsupportedoperationexception](https://stackoverflow.com/questions/5755477/java-list-add-unsupportedoperationexception)
> 有时候会使用 Arrays.asList() 或者 Collections.singletonList() 来快速生成 List  
> 但是 这两个生成的实例都是返回 AbstractList 的实现类, 其 add remove 方法是没有实现的, 如果调用了就会抛出异常

```java
    public void add(int index, E element) {
        throw new UnsupportedOperationException();
    }
```
> 这是因为, 这个类设计就是采用的定长数组来实现List, 所以不能对其中元素进行更改

******************************************
## Set
- Set是无序的，但是StringRedisTemplate的对象操作返回的set竟然是有序的
    - 因为有一个类是SortSet，顾名思义，所以是有序的，要继续多学习和使用Java原生的集合对象了

> [3分钟搞掂Set集合](https://segmentfault.com/a/1190000014391402?utm_source=channel-hottest)


