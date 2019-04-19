在Java中HashMap算是比较常用的集合框架，是Java中比较典型的数据结构。
在本文中主要探究HashMap中常用的put和get方法。
在HashMap中，其最主要的数据结构为自定义的节点数组`Node<K,V>[]`,用该数组存储数据，下面来看看自定义的Node节点结构。

```java
    static class Node<K,V> implements Map.Entry<K,V> {
        final int hash;
        final K key;
        V value;
        Node<K,V> next;

        Node(int hash, K key, V value, Node<K,V> next) {
            this.hash = hash;
            this.key = key;
            this.value = value;
            this.next = next;
        }
        // 其余省略...
    }

```

如上代码所示(java1.8)，在Node节点中主要存储了`hash`，`key`,`value`及下一节点信息。从该节点中不难看出这是链表结构。看到这里应该便就能想象出HasMap的数据结构了(数组加链表)，其结构如下图所示。

![HashMap主要数据结构](https://github.com/dragonhht/GitImgs/blob/master/Notes/HashMap_1.png?raw=true)

在我们写Java代码中，用于比较最常用的便就是`equals`方法了，但在HashMap中，在添加值时对每个对象都进行equals这是一个比较好性能的一个操作，所以采用了哈希表来管理所有元素。在每次`put`操作时先通过Hash值来迅速查找到元素的存放位置，但会出现多个元素都找到同一位置的情况，这种情况称为碰撞。当碰撞发生时，才会使用到`equals`方法，去和该位置中已存在的元素进行比较，若最终发现hashcode与equals都相同，则使用新值来替换旧值。
好吧让我们来看看具体的代码吧！

``` java
    final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
        Node<K,V>[] tab;    // 存放所有值的数组
        Node<K,V> p;        // 存放单个值的节点
        int n, i; 
        // 判断存放的数组的大小，若为空则创建或设置大小
        if ((tab = table) == null || (n = tab.length) == 0)
            n = (tab = resize()).length;
        // 在哈希表中未找到值
        if ((p = tab[i = (n - 1) & hash]) == null)
            // 创建新的节点
            tab[i] = newNode(hash, key, value, null);
        else {
            Node<K,V> e; K k;
            // 判断节点的哈希值与键是否一致（判断是否为同一个）
            if (p.hash == hash &&
                ((k = p.key) == key || (key != null && key.equals(k))))
                e = p;
            else if (p instanceof TreeNode)
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            else {
                for (int binCount = 0; ; ++binCount) {
                    // 判断是否为最后一个
                    if ((e = p.next) == null) {
                        p.next = newNode(hash, key, value, null);
                        if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                            treeifyBin(tab, hash);
                        break;
                    }
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                        break;
                    p = e;
                }
            }
            if (e != null) { // existing mapping for key
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null)
                    e.value = value;
                afterNodeAccess(e);
                return oldValue;
            }
        }
        ++modCount;
        if (++size > threshold)
            resize();
        afterNodeInsertion(evict);
        return null;
    }
```

在代码中，通过`tab[i = (n - 1) & hash]`来推算出元素在数组中的位置(即通过hash来迅速查找位置)，若发现该位置为空，则在该位置创建元素节点。若该元素已存在元素，则通过hash与equals来判断是否为该元素，`if (p.hash == hash && ((k = p.key) == key || (key != null && key.equals(k))))`，若为该元素，则用新值替换旧值。但如果发现该位置的第一个节点不是该元素，则循环从之后的节点中查找。