---
title: IO
date: 2019-04-20 12:16:10
tags: 
categories: 
---

**目录 start**
 
1. [IO](#io)
    1. [IO模型](#io模型)
        1. [Blocking IO](#blocking-io)
        1. [Nonblocking IO](#nonblocking-io)
        1. [IO multiplexing](#io-multiplexing)
        1. [Asynchronous IO](#asynchronous-io)
        1. [经典比喻](#经典比喻)
    1. [阻塞和非阻塞](#阻塞和非阻塞)
    1. [同步和异步](#同步和异步)
1. [多路复用](#多路复用)
    1. [多路复用模型](#多路复用模型)
        1. [忙轮询](#忙轮询)
        1. [无差别轮询](#无差别轮询)
        1. [最小轮询](#最小轮询)
    1. [IO多路复用函数](#io多路复用函数)
        1. [select](#select)
        1. [poll](#poll)
        1. [epoll](#epoll)

**目录 end**|_2019-04-20 12:32_|
****************************************
# IO
> [参考博客: IO - 同步，异步，阻塞，非阻塞 ](https://blog.csdn.net/historyasamirror/article/details/5778378)  

IO在计算机中指Input/Output，也就是输入和输出。由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。

## IO模型

- Blocking IO
- Nonblocking IO
- IO multiplexing
- Signal driven IO
- Asynchronous IO

> [参考博客: 使用异步 I/O 大大提高应用程序的性能](https://www.ibm.com/developerworks/cn/linux/l-async/)  

对于一个network IO (这里我们以read举例)，它会涉及到两个系统对象: 
- 调用这个IO的process (or thread)
- 系统内核(kernel)。  

当一个read操作发生时，它会经历两个阶段：
1. `等待数据准备` (Waiting for the data to be ready)
1. `将数据从内核拷贝到进程中` (Copying the data from the kernel to the process)

记住这两点很重要，因为这些IO Model的区别就是在两个阶段上各有不同的情况。

### Blocking IO
> Blocking IO的特点就是在IO执行的两个阶段都被 block了

### Nonblocking IO
> 用户进程不断询问内核数据有没有好, 一旦kernel中的数据准备好了，并且又再次收到了用户进程的询问(system call)，那么它马上就将数据拷贝到了用户内存，然后返回。

### IO multiplexing
> 当用户进程调用了select，那么整个进程会被block，而同时，kernel会“监视”所有select负责的socket，当任何一个socket中的数据准备好了，select就会返回。这个时候用户进程再调用read操作，将数据从kernel拷贝到用户进程。

在IO multiplexing Model中，实际中，对于每一个socket，一般都设置成为non-blocking，但是 整个用户的process其实是一直被block的。只不过process是被select这个函数block，而不是被socket IO被block。

如果处理的连接数不是很高的话，使用select/epoll的web server不一定比使用multi-threading + blocking IO的web server性能更好，可能延迟还更大。select/epoll的优势并不是对于单个连接能处理得更快，而是在于能处理更多的连接。

### Asynchronous IO
> 用的比较少 

> [参考博客: 异步AIO的研究](http://rango.swoole.com/archives/282)  

用户进程发起read操作之后，立刻就可以开始去做其它的事。而另一方面，从kernel的角度，当它受到一个asynchronous read之后，首先它会立刻返回，所以不会对用户进程产生任何block。  
然后kernel会等待数据准备完成，然后将数据拷贝到用户内存，当这一切都完成之后，kernel会给用户进程发送一个signal，告诉它read操作完成了。  

### 经典比喻
有 A，B，C，D 四个人在钓鱼：
- A 用的是最老式的鱼竿，所以呢，得一直守着，等到鱼上钩了再拉杆；
- B 用的鱼竿有浮漂，所以呢，B就和旁边的MM聊天，隔会再看看有没有鱼上钩，有的话就迅速拉杆；
- C 用的鱼竿和B差不多，但他想了一个好办法，就是同时放好几根鱼竿，然后守在旁边，一旦有显示说鱼上钩了，它就将对应的鱼竿拉起来； 这样一个人就能处理好多个鱼竿
- D 是个有钱人，干脆雇了一个人帮他钓鱼，一旦那个人把鱼钓上来了，就给D发个短信。

************************

## 阻塞和非阻塞
调用blocking IO 会一直 block 住对应的进程直到操作完成, 该操作就是阻塞的  
而 non-blocking IO 在 kernel 还未准备好数据的情况下会立刻返回, 该操作就是非阻塞的  

## 同步和异步

在说明synchronous IO和asynchronous IO的区别之前，需要先给出两者的定义。Stevens给出的定义（其实是POSIX的定义）是这样子的：
```
    A synchronous I/O operation causes the requesting process to be blocked until that I/O operation completes;
    An asynchronous I/O operation does not cause the requesting process to be blocked;
```

两者的区别就在于 synchronous IO 做 `IO operation` 的时候会将process阻塞。  
按照这个定义，之前所述的 blocking IO，non-blocking IO，IO multiplexing 都属于 synchronous IO。  

有人可能会说，non-blocking IO并没有被block啊。 这是因为在第一阶段, 数据没有准备好就直接返回没有阻塞, 但是如果数据准备好了就要执行第二阶段 数据复制 的操作, 这个操作是会阻塞对应的进程的  
而asynchronous IO则不一样，当进程发起IO 操作之后，就直接返回再也不理睬了，直到kernel发送一个信号，告诉进程说IO完成。在这整个过程中，进程完全没有被block。  

# 多路复用
> [参考博客: IO多路复用](https://blog.csdn.net/chewbee/article/details/78108223)   

## 多路复用模型
### 忙轮询
忙轮询方式是通过不停的把所有的流从头到尾轮询一遍，查询是否有流已经准备就绪，然后又从头开始。如果所有流都没有准备就绪，那么只会白白浪费CPU时间。

### 无差别轮询
为了避免白白浪费CPU时间，我们采用另外一种轮询方式，无差别的轮询方式。即通过引进一个代理，这个代理为 select/poll ,这个代理可以同时观察多个流的I/O事件。  
当所有的流都没有准备就绪时，会把当前线程阻塞掉；当有一个或多个流的I/O事件就绪时，就从阻塞状态中醒来，然后轮询一遍所有的流，处理已经准备好的I/O事件。

如果I/O事件准备就绪，那么我们的程序就会阻塞在select处。我们通过select那里只是知道了有I/O事件准备好了，但不知道具体是哪几个流（可能有一个，也可能有多个），所以需要无差别的轮询所有的流，找出已经准备就绪的流。可以看到，使用select时，我们需要O(n)的时间复杂度来处理流，处理的流越多，消耗的时间也就越多。

### 最小轮询

即通过epoll方式来观察多个流，epoll只会把发生了I/O事件的流通知我们，我们对这些流的操作都是有意义的，时间复杂度降低到O（k），其中k为产生I/O事件的流个数。

## IO多路复用函数
> [参考博客: IO多路复用之select、poll、epoll详解](https://www.cnblogs.com/jeakeven/p/5435916.html)   

select/poll/epoll都是采用I/O多路复用机制的，其中select/poll是采用无差别轮询方式，而epoll是采用最小的轮询方式。  
IO复用机制可以同时监控多个描述符，当某个描述符就绪（读或写就绪），则立即通知相应程序进行读或写操作。  
但select，poll，epoll本质上都是同步I/O，因为他们都需要在读写事件就绪后自己负责进行读写，也就是说这个读写过程是阻塞的  

### select

系统提供Select函数来实现多路复用输入/输出模型，Select系统调用是用来让我们的程序监视多个文件句柄的状态变化。程序会阻塞在select函数上，直到被监视的文件句柄中有一个或多个发生了状态变化。

### poll
Poll的处理机制与Select类似，只是Poll选择了pollfd结构体来处理文件描述符的相关操作

### epoll
epoll是在Linux内核2.6引进的，是select和poll函数的增强版。与select相比，epoll没有文件描述符数量的限制。  
epoll使用一个文件描述符管理多个文件描述符，将用户关心的文件描述符事件存放到内核的一个事件列表中，这样在用户空间和内核空间只需拷贝一次。

> epoll是Linux所特有


