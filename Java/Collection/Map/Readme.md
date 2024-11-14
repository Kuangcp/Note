# Map

AbstractMap 抽象基类，可以基于该类实现自己的Map

## 通用Map

| 类型 | 特征 | key | 并发安全 |
|:---|:---|:---|:---|
|HashMap           | 链表和红黑树 | key和value均允许为空 | 否 |
|Hashtable         | 单线程写入 | key和value的值均不允许为null | 是 |
|Properties        | Hashtable 子类 | | 是 |
|LinkedHashMap     | 保持了数据插入顺序 | key和value均允许为空 | 否 |
|IdentityHashMap   | key非equals比较而是 == 比较 | key和value均允许为空 | 否 |
|TreeMap           | 红黑树实现 | key不允许null | 否|
|WeakHashMap       | key 弱引用 | | 否 |
|ThreadLocalMap    | ThreadLocal, key 弱引用 | | 否 |
|ConcurrentHashMap | 分段锁 | | 是 |

> IdentityHashMap
- java.util.HashMap#getNode  `equals`
- java.util.IdentityHashMap#get `==`

## 专用Map

- java.util.jar.Attributes
- javax.print.attribute.standard.PrinterStateReasons
- java.security.Provider
- java.awt.RenderingHints
- javax.swing.UIDefaults

## 第三方
> [NonBlockingHashMap](https://github.com/h2oai/h2o-3/blob/master/h2o-core/src/main/java/water/nbhm/NonBlockingHashMap.java)  
