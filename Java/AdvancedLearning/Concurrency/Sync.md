---
title: Java中保证同步的方式
date: 2019-06-04 19:44:41
tags: 
categories: 
    - Java
---

**目录 start**
 
1. [保证同步的方式](#保证同步的方式)
1. [关键字 synchronized](#关键字-synchronized)
    1. [使用wait() notify() 和 notifyAll()](#使用wait-notify-和-notifyall)
1. [使用Lock](#使用lock)
1. [4、使用读写锁实现同步数据访问](#4、使用读写锁实现同步数据访问)
1. [5、使用`Condition`](#5、使用`condition`)
1. [1、信号量：`Semaphore`](#1、信号量`semaphore`)
1. [2、使用`CountDownLatch`等待并发事件完成](#2、使用`countdownlatch`等待并发事件完成)
1. [3、使用`CyclicBarrier`让多个线程同步](#3、使用`cyclicbarrier`让多个线程同步)
1. [4、使用`Phaser`控制并发阶段任务的运行](#4、使用`phaser`控制并发阶段任务的运行)
1. [5、使用`Exchanger`控制并发任务间的数据交换](#5、使用`exchanger`控制并发任务间的数据交换)

**目录 end**|_2019-06-04 19:53_|
****************************************
# 保证同步的方式

# 关键字 synchronized

- 一个对象使用synchronized关键字声明，则只有一个执行线程可访问它，如果其他线程试图访问，这些线程将会被挂起，直到第一个拥有的的线程执行完

- 当使用synchronized修饰一个对象的非静态方法时，当一个线程访问该方法时，其他线程不能访问该对象的其他被synchronized修饰的方法，但可以访问未被synchronized修饰的方法

- 当使用synchronized修饰静态方法时，该方法同时只能被同一线程访问，但其他线程可访问该对象的其他非静态方法

## 使用wait() notify() 和 notifyAll()

-   `wait()`方法可让线程挂起
-   `notify()`和`notifyAll()`用于唤醒线程
-   使用队列实现生产-消费者模型

    ```java
    public class WaitAndNotify {

        /**
        * 模拟存储的队列.
        */
        @Data
        private class Storage {
            private int maxSize;
            private LinkedList<Integer> data;

            public Storage(int maxSize) {
                this.maxSize = maxSize;
                this.data = new LinkedList<>();
            }

            /**
            * 添加数据.
            */
            public synchronized void add(Integer data) {
                while (this.data.size() == maxSize) {
                    try {
                        System.out.println("队列已满");
                        wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.println("添加数据");
                this.data.add(data);
                notifyAll();
            }

            /**
             * 获取数据
             */
            public synchronized Integer get() {
                while (this.data.size() == 0) {
                    try {
                        System.out.println("队列已空");
                        wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                Integer result = this.data.poll();
                System.out.println("获取数据: " + result);
                notifyAll();
                return result;
            }
        }

        public void run() {
            Random random = new Random();
            Storage storage = new Storage(20);
            Thread producer = new Thread(() -> {
                for (int i = 0; i < 100; i++) {
                    int n = random.nextInt(100);
                    storage.add(n);
                }
            });
            Thread consumer = new Thread(() -> {
            for (int i = 0; i < 100; i++) {
                storage.get();
            }
            });
            producer.start();
            consumer.start();
        }

        public static void main(String[] args) {
            WaitAndNotify test = new WaitAndNotify();
            test.run();
        }

    }
    ```

# 使用Lock

>   Java除了使用`synchronized`实现同步代码块外，还提供了另一种同步代码块机制，这种机制基于`Lock`及其实现类(如：ReentrantLock)

-   `Lock`与`synchronized`的区别

    -   `Lock`更加灵活：使用`synchronized`关键字，只能在同一块`synchronized`块结构中获取和释放。而`Lock`可实现更复杂的临界结构，如获取和释放不再同一块结构中

    -   `Lock`提供了更多的功能：如`tryLock()`

    -   `Lock`接口允许读写分离操作，允许多个读线程和一个写线程

    -   `Lock`的性能更好

# 4、使用读写锁实现同步数据访问

> 接口`ReadWriteLock`和其唯一实现类`ReentrantReadWriteLock`(该类有两个锁，分别为读操作锁和写操作锁)可实现读写锁

-   读写锁示例

    ```java
    public class ReadAndWriter {

        private int price1;
        private int price2;

        ReadWriteLock readWriteLock;

        public ReadAndWriter(int price1, int price2) {
            this.price1 = price1;
            this.price2 = price2;
            this.readWriteLock = new ReentrantReadWriteLock();
        }

        /**
        * 获取数据(使用读操作锁)
        * @return
        */
        public int getPrice1() {
            readWriteLock.readLock().lock();
            int price = this.price1;
            readWriteLock.readLock().unlock();
            return price;
        }

        /**
        * 获取数据(使用读操作锁)
        * @return
        */
        public int getPrice2() {
            readWriteLock.readLock().lock();
            int price = this.price2;
            readWriteLock.readLock().unlock();
            return price;
        }

        /**
        * 设置数据(使用写操作锁)
        * @param price1
        * @param price2
        */
        public void setPrices(int price1, int price2) {
            readWriteLock.writeLock().lock();
            this.price1 = price1;
            this.price2 = price2;
            readWriteLock.writeLock().unlock();
        }

        public static void main(String[] args) {
            ReadAndWriter readAndWriter = new ReadAndWriter(0, 1);
            Random random = new Random();
            new Thread(() -> {
                for (int i = 0; i < 3; i++) {
                    System.out.println("writer");
                    readAndWriter.setPrices(random.nextInt(10000), random.nextInt(10000));
                    System.out.println("modified");
                    try {
                        Thread.sleep(2000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }).start();

            for (int i = 0; i < 5; i++) {
                new Thread(() -> {
                    for (int j = 0; j < 5; j++) {
                        System.out.println(Thread.currentThread().getName() + " : " + readAndWriter.getPrice1());
                        System.out.println(Thread.currentThread().getName() + " : " + readAndWriter.getPrice2());
                    }
                }).start();
            }
        }
    }
    ```

# 5、使用`Condition`

> 一个锁可能关联一个或多个条件，这些条件通过`Condition`接口声明，`Condition`接口提供了线程的挂起和唤醒机制

-   与锁绑定的条件对象都是通过`Lock`接口声明的`newCondition()`方法创建的。

-   在使用条件时，必须拥有绑定的锁，即，所有带条件的代码必须在调用`Lock`对象的`lock()`和`unlock()`方法之间

-   当线程调用条件`await()`时，会自动释放绑定的锁

-   如果调用了条件`await()`，但没有调用他的`signal()`，这个线程将会永远休眠

-   生产-消费者模型

```java
public class ConditionTest {

    private static class Storage {
        private LinkedList<Double> storage = new LinkedList<>();
        private int maxSize;
        // 创建Lock
        private Lock lock = new ReentrantLock();
        private Condition producer = lock.newCondition();
        private Condition consumer = lock.newCondition();

        public Storage(int maxSize) {
            this.maxSize = maxSize;
        }

        public Double get() {
            Double n = 0.0;
            lock.lock();
            try {
                while (this.storage.size() < 1) {
                    System.out.println("等待生产");
                    consumer.await();
                }
                System.out.println(Thread.currentThread().getName() + " consumer" );
                n = this.storage.poll();
                producer.signalAll();
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                lock.unlock();
            }
            return n;
        }

        public void add(Double n) {
            lock.lock();
            try {
                while (this.storage.size() >= this.maxSize) {
                    System.out.println("等待消费");
                    producer.await();
                }
                System.out.println(Thread.currentThread().getName() + " producer" );
                this.storage.add(n);
                consumer.signalAll();
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                lock.unlock();
            }
        }
    }


    public static void main(String[] args) {
        Storage storage = new Storage(20);
            new Thread(() -> {
                while (true) {
                    storage.add(Math.random());
                }
            }).start();
            for (int i = 0; i < 5; i++) {
                new Thread(() -> {
                    while (true) {
                        System.out.println(storage.get());
                    }
                }).start();
            }
    }

}
```

# 1、信号量：`Semaphore`

> 信号量是一个计数器，用来保护一个或多个共享资源的访问。当线程访问一个一个共享资源时，它必须得先获取信号量，如果信号量大于0，则信号量减一，该线程允许访问共享资源。当信号量等于0,则线程将会被置于休眠，直到信号量大于0  

-   注意：`当线程用完某个共享资源后，信号量必须释放，释放操作将会是信号量的内部计数器加1`

-   使用`二进制信号量`控制队列中数据的添加和获取的同步(此处使用`公平模式`，在非公平模式下，多个死循环线程中出现信号量一直被一个线程占用的情况)

```java
public class SemaphoreTest {

    /** 声明一个信号量对象. */
    private Semaphore semaphore;
    /** 存储数据. */
    private LinkedList<Double> storage = new LinkedList<>();
    /** 存储的最大数量. */
    private int maxSize = 20;

    public SemaphoreTest() {
        // 此处传入的参数为1，则该信号量为二进制信号量，即信号量的计数器的值只有0和1
        // 第二个参数表示是否公平
        this.semaphore = new Semaphore(1, true);
    }

    /**
     * 添加
     * @param d
     */
    public void add(Double d) {
        try {
            // 获取信号量
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() +": add start");
            if (this.storage.size() < this.maxSize) {
                this.storage.add(d);
            }
            Thread.sleep(1000);
            System.out.println(Thread.currentThread().getName() +": add end");
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            // 释放信号量
            semaphore.release();
        }
    }

    /**
     * 获取
     */
    public Double get() {
        try {
            // 获取信号量
            semaphore.acquire();
            double d = 0.0;
            System.out.println(Thread.currentThread().getName() +": get start");
            if (this.storage.size() > 0 ) {
                d = this.storage.poll();
            }
            Thread.sleep(1000);
            System.out.println(Thread.currentThread().getName() +": get end");
            return d;
        } catch (InterruptedException e) {
            e.printStackTrace();
            return 0.0;
        } finally {
            // 释放信号量
            semaphore.release();
        }
    }

    public static void main(String[] args) {
        SemaphoreTest test = new SemaphoreTest();
        for (int i = 0; i < 3; i++) {
            new Thread(() -> {
                while (true) {
                    test.add(Math.random());
                }
            }).start();
        }

        for (int i = 0; i < 3; i++) {
            new Thread(() -> {
                while (true) {
                    System.out.println(test.get());
                }
            }).start();
        }
    }

}
```

-   除二进制信号量外，信号量还可以让实现被多个线程同时访问的临界区

# 2、使用`CountDownLatch`等待并发事件完成

-   `CountDownLatch`可以完成一组正在其他线程中执行的操作前，允许他一直等待

-   实例：在20个线程完全准备好前，让线程等待

```java
public class CountDownLatchTest {

    public static void main(String[] args) {
        int size = 20;
        // 创建CountDownLatch对象
        CountDownLatch latch = new CountDownLatch(size);
        Lock lock = new ReentrantLock();
        for (int i = 0; i < 20; i++) {
            new Thread(() -> {
                System.out.println("等待线程全部准备...");
                try {
                    try {
                        // 为了 latch.getCount() 顺序所以加锁控制
                        lock.lock();
                        // 减一操作，表示该线程以准备完成
                        latch.countDown();
                        System.out.println("还有 " + latch.getCount() + " 个线程需准备");
                    } finally {
                        lock.unlock();
                    }
                    // 等待其他线程准备
                    latch.await();
                    System.out.println(Thread.currentThread().getName() + ": 准备完成, 开始执行任务...");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }).start();
        }
    }

}
```

# 3、使用`CyclicBarrier`让多个线程同步

-   `CyclicBarrier`与`CountDownLatch`很相似，但`CyclicBarrier`的功能要更强大些。`CyclicBarrier`除了可以让线程在某个集合点同步外，还能在所有线程都达到集合点后再运行一个新的线程。这可以很好的实现分治思想

-   `CyclicBarrier`可使用`reset()`方法，将内部计数器重置为初始化的值。重置后，正在await()方法中等待的线程将会收到`BrokenBarrierException`异常，这是可处理异常或将操作重新执行或恢复到被中断时的状态

-   `损坏的CyclicBarrier`：Cyclicbarrier对象有一种特殊的状态即`损坏状态(Broken)`。当很多线程在`await()`方法上等待的时候，如果其中一个线程被中断，这个线程将抛出`Interruptedexception`异常，其他的等待线程将抛出`Brokenbarrierexception`异常，于是Cyclicbarrier对象就处于损坏状态了。Cyclicbarrier类提供了`isBroken()`方法，如果处于损坏状态就返回true,否则返回false。

-   使用`CyclicBarrier`，计算某个数值再二维数组中出现的次数(先将二维数组分为若干个一维数组，每个线程计算各自分配的一维数组中数值出现的次数。当所有线程计算完各自一维数组后，再使用另一个线程计算前面每个线程所计算出的数量的总和)

```java
public class CyclicBarrierStudy {

    private int[][] storage;

    public CyclicBarrierStudy(int size, int length, int number) {
        // 初始化二维数组数据，并记录所要查找的数字出现的次数
        this.storage = new int[size][length];
        Random random = new Random();
        int count = 0;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < length; j++) {
                storage[i][j] = random.nextInt(150);
                if (storage[i][j] == number) {
                    count++;
                }
            }
        }
        // 打印正确结果信息，用于后面的校验
        System.out.printf("需查找的数值 %d 共出现 %d 次发\n", number, count);
    }

    public int[] getData(int index) {
        return this.storage[index];
    }

    public static void main(String[] args) {
        final int size = 10, length = 50, number = 100;
        int[] countData = new int[size];
        CyclicBarrierStudy study = new CyclicBarrierStudy(size, length, number);

        // 创建CyclicBarrier对象，并指定等待 size个线程结束，结束后运行另一个线程计算总数
        CyclicBarrier cyclicBarrier = new CyclicBarrier(size, () -> {
            // 计算总数
            int count = 0;
            for (int n : countData) {
                count += n;
            }
            System.out.printf("查找结束，数值 %d 共出现 %d 次\n", number, count);
        });

        // 用线程计算每组的出现的数量
        for (int i = 0; i < size; i++) {
            final int index = i;
            new Thread(() -> {
                // 将二维数组分组进行查询
                int[] data = study.getData(index);
                int count = 0;
                for (int n : data) {
                    if (n == number) {
                        count++;
                    }
                }
                // 保存该组数组中出现指定数据的次数
                countData[index] = count;
                System.out.println(Thread.currentThread().getName() + " search end");
                try {
                    // 等待其他线程完成，当其他线程都完成后，await()方法后面的代码才会执行
                    cyclicBarrier.await();
                } catch (InterruptedException | BrokenBarrierException e) {
                    e.printStackTrace();
                }
            }).start();
        }
    }

}
```

# 4、使用`Phaser`控制并发阶段任务的运行

-   `Phaser`在每一步结束的位置对线程进行同步，当所有线程都完成到该处后，才允许执行下一步

-   必须对`Phaser`中参与同步操作的任务数进行初始化，我们可以动态的添加和减少任务数

-   几个重要方法:

    -   `arriveAndAwaitAdvance()`: 当一个线程调用该方法后，`Phaser`对象减一，并且把该线程置为休眠状态，直到其他线程完成该阶段

    -   `arriveAndDeregister()`: 该方法主要用于通知`Phaser`参与同步的线程数减一，表示不参与下一阶段的任务，因此`Phaser`在开始下一阶段时不会等待该线程

    -   `onAdvance`: `Phaser`提供的一个方法，可覆盖该方法。`onAdvance()`会在阶段改变的时候被调用。方法的返回值，`true`表示`phaser`已经执行完成并进入了终止态，`false`表示`phaser`在继续执行。我们可通过覆盖`onAdvance`方法，在每个阶段改变的时候执行某些操作

-   `Phaser`示例，控制各阶段的同步

```java
public class PhaserTest {

    public static void main(String[] args) {
        Random random = new Random();
        int len = 20, size = 20;
        // 创建Phaser,有20个参与线程
        Phaser phaser = new Phaser(len);
        int[][] data = new int[len][size];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < size; j++) {
                data[i][j] = random.nextInt(2);
            }
        }

        for (int i = 0; i < len; i++) {
            final int index = i;
            new Thread(() -> {
                // 让所有线程在都创建完成后运行
                System.out.println(Thread.currentThread().getName() + ": 准备第一阶段");
                phaser.arriveAndAwaitAdvance();
                if (data[index][0] == 0) {
                    System.out.println(Thread.currentThread().getName() + " : 当前线程已结束");
                    phaser.arriveAndDeregister();
                    return;
                } else {
                    System.out.println(Thread.currentThread().getName() + " : 已完成第二阶段");
                    phaser.arriveAndAwaitAdvance();
                }
                System.out.println(Thread.currentThread().getName() + ": 开始第三阶段");
                System.out.println(Thread.currentThread().getName() + ": " + Arrays.toString(data[index]));
            }).start();
        }
    }
}
```

# 5、使用`Exchanger`控制并发任务间的数据交换

-   `Exchanger`允许在两个线程之间定义同步点，当两个线程都到达同步点时，他们交换数据

-   消费者与生产者交换数据

```java
public class ExchangerTest {

    public static void main(String[] args) {
        LinkedList<Integer> producerData = new LinkedList<>();
        LinkedList<Integer> consumerData = new LinkedList<>();
        Exchanger<LinkedList<Integer>> exchanger = new Exchanger<>();
        new Thread(new Producer(producerData, exchanger)).start();
        new Thread(new Consumer(consumerData, exchanger)).start();
    }

    static class Producer implements Runnable{
        private LinkedList<Integer> data;
        private final Exchanger<LinkedList<Integer>> exchanger;

        public Producer(LinkedList<Integer> data, Exchanger<LinkedList<Integer>> exchangerData) {
            this.data = data;
            this.exchanger = exchangerData;
        }

        @Override
        public void run() {
            int index = 1;
            int size = 10;
            Random random = new Random();
            for (int i =0;i < size; i++) {
                System.out.printf("生产者第 %d 次交换\n", index);
                int n = random.nextInt();
                System.out.println("生产的数据: " + n);
                data.add(n);

                try {
                    // 与消费者交换数据
                    data = exchanger.exchange(data);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("消费者现有数据数量: " + data.size());
                index++;
            }
        }
    }

    static class Consumer implements Runnable {

        private LinkedList<Integer> data;
        private final Exchanger<LinkedList<Integer>> exchanger;

        public Consumer(LinkedList<Integer> data, Exchanger<LinkedList<Integer>> exchanger) {
            this.data = data;
            this.exchanger = exchanger;
        }

        @Override
        public void run() {
            int index = 1;
            int size = 10;
            for (int i =0;i < size; i++) {
                System.out.printf("消费者第 %d 次交换\n", index);
                try {
                    // 与生产者交换数据
                    data = exchanger.exchange(data);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("消费的数据: " + data.poll());
                index++;
            }
        }
    }
}
```
