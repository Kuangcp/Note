---
title: 计算机中的IO
date: 2019-04-20 12:16:10
tags: 
    - IO
categories: 
    - 计算机基础
---

💠

- 1. [计算机中的IO](#计算机中的io)
    - 1.1. [IO模型](#io模型)
        - 1.1.1. [Blocking IO](#blocking-io)
        - 1.1.2. [Nonblocking IO](#nonblocking-io)
        - 1.1.3. [IO multiplexing](#io-multiplexing)
        - 1.1.4. [Signal driven IO](#signal-driven-io)
        - 1.1.5. [Asynchronous IO](#asynchronous-io)
        - 1.1.6. [经典比喻](#经典比喻)
    - 1.2. [阻塞和非阻塞](#阻塞和非阻塞)
    - 1.3. [同步和异步](#同步和异步)
    - 1.4. [同异步和阻塞](#同异步和阻塞)
- 2. [多路复用](#多路复用)
    - 2.1. [多路复用模型](#多路复用模型)
        - 2.1.1. [Reactor](#reactor)
        - 2.1.2. [Proactor](#proactor)
        - 2.1.3. [忙轮询](#忙轮询)
        - 2.1.4. [无差别轮询](#无差别轮询)
        - 2.1.5. [最小轮询](#最小轮询)
    - 2.2. [IO多路复用函数](#io多路复用函数)
        - 2.2.1. [select](#select)
        - 2.2.2. [poll](#poll)
        - 2.2.3. [epoll](#epoll)

💠 2024-06-16 16:40:46
****************************************
# 计算机中的IO
> [参考: IO - 同步，异步，阻塞，非阻塞 ](https://blog.csdn.net/historyasamirror/article/details/5778378)  

IO在计算机中指 Input/Output，也就是输入和输出。由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。

> [Linux IO](/Linux/Base/LinuxFile.md#io)

## IO模型

- Blocking IO
- Nonblocking IO
- IO multiplexing
- Signal driven IO
- Asynchronous IO

> [参考: 使用异步 I/O 大大提高应用程序的性能](https://www.ibm.com/developerworks/cn/linux/l-async/)  

### Blocking IO
> Blocking IO的特点就是在IO执行的两个阶段都被 block了

### Nonblocking IO
> 用户进程不断询问内核数据有没有好, 一旦kernel中的数据准备好了，并且又再次收到了用户进程的询问(system call)，那么它马上就将数据拷贝到了用户内存，然后返回。

### IO multiplexing
> 当用户进程调用了select，那么整个进程会被block，而同时，kernel会“监视”所有select负责的socket，当任何一个socket中的数据准备好了，select就会返回。这个时候用户进程再调用read操作，将数据从kernel拷贝到用户进程。

在IO multiplexing Model中，实际中，对于每一个socket，一般都设置成为non-blocking，但是 整个用户的process其实是一直被block的。只不过process是被select这个函数block，而不是被socket IO被block。

如果处理的连接数不是很高的话，使用select/epoll的web server不一定比使用multi-threading + blocking IO的web server性能更好，可能延迟还更大。  
select/epoll的优势`不在于单个连接能处理得更快，而在于能处理更多的连接`。

### Signal driven IO 
> 使用较少

在信号驱动IO模型中，当用户线程发起一个IO请求操作，会给对应的socket注册一个信号函数，然后用户线程会继续执行  
当内核数据就绪时会发送一个信号给用户线程，用户线程接收到信号之后，便在信号函数中调用IO读写操作来进行实际的IO请求操作。

### Asynchronous IO
> [参考: 异步AIO的研究](http://rango.swoole.com/archives/282)  

用户进程发起read操作之后，立刻就可以开始去做其它的事。而另一方面，从kernel的角度，当它受到一个asynchronous read之后，首先它会立刻返回，所以不会对用户进程产生任何block。  
然后kernel会等待数据准备完成，然后将数据拷贝到用户内存，当这一切都完成之后，kernel会给用户进程发送一个signal，告诉它read操作完成了。  

AIO适用于 IO操作量大，读写过程长的场景，但是缺点是应用系统处理异步API麻烦。

### 经典比喻
有 A，B，C，D 四个人在钓鱼 (BIO, NIO, IO multiplexing, AIO) : 
- A 用的是最老式的鱼竿（只有线和竿），所以得一直守着，等到鱼上钩了再拉杆；
- B 用的鱼竿有浮漂，B就能旁边泡茶，隔会再看看有没有鱼上钩，有的话就迅速拉杆；
- C 用的鱼竿和B差不多，但他想了一个好办法，`就是同时放好几根鱼竿`，然后守在旁边，一旦提示鱼上钩了，它就将对应的鱼竿拉起来； 这样一个人就能处理好多个鱼竿
- D 是个有钱人，干脆雇了一个人帮他钓鱼，一旦那个人把鱼钓上来了，就给D发个短信。

************************

## 阻塞和非阻塞
阻塞和非阻塞关注的是程序在等待调用结果（消息，返回值）时的状态.  

阻塞调用是指调用结果返回之前，当前线程会被挂起。调用线程只有在得到结果之后才会返回。  
非阻塞调用指在不能立刻得到结果之前，该调用不会阻塞当前线程。  

调用 blocking IO 会一直 block 住对应的进程直到操作完成, 该操作就是阻塞的  
而 non-blocking IO 在 kernel 还未准备好数据的情况下会立刻返回, 该操作就是非阻塞的  

## 同步和异步
同步和异步关注的是消息通信机制 (synchronous communication/ asynchronous communication)

所谓同步，就是在发出一个*调用*时，在没有得到结果之前，该*调用*就不返回。但是一旦调用返回，就得到返回值了。 换句话说，就是由*调用者*主动等待这个*调用*的结果。
异步则是调用者调用就返回了，等操作系统来完成IO行为，并通知调用者（由于应用场景多变，这种方式下会受限于操作系统的调度不可控，所以一直没有得到广泛应用）。

在说明synchronous IO和asynchronous IO的区别之前，需要先给出两者的定义。Stevens给出的定义（其实是POSIX的定义）是这样子的：
```
    A synchronous I/O operation causes the requesting process to be blocked until that I/O operation completes;
    An asynchronous I/O operation does not cause the requesting process to be blocked;
```

两者的区别就在于 synchronous IO 做 `IO operation` 的时候会将应用的 process 阻塞。  
按照这个定义，之前所述的 blocking IO，non-blocking IO，IO multiplexing `都属于 synchronous IO`。   
`在处理 IO 的时候，阻塞和非阻塞都是同步 IO`，只有使用特定API才是异步 IO： Linux aio, Windows IOCP   

有人可能会说，non-blocking IO 并没有被 block， 这是因为在第一阶段, 数据没有准备好就直接返回这里没有阻塞, 等数据准备好了就要执行第二阶段 数据复制 的操作, 这个操作是会阻塞对应的进程  
而 asynchronous IO 则不一样，当进程发起 IO 操作之后，就直接返回，直到 kernel 发送一个信号，通知应用进程说IO完成 `也就是数据复制完成后才通知`  
在这整个过程中，进程完全没有被block。  

************************
## 同异步和阻塞
> [Linux AIO](https://oxnz.github.io/2016/10/13/linux-aio/)

|  | 阻塞 | 非阻塞 |
|:---|:---|:---|
| 同步 | read/write | read/write<br/> (O_NONBLOCK) |
| 异步 | I/O multiplexing <br/>(select/poll/epoll) | AIO |

阻塞，非阻塞：进程/线程要访问的数据是否就绪，进程/线程是否需要等待；  
同步，异步：访问数据的方式，同步需要主动读写数据，在读写数据的过程中还是会阻塞；异步只需要I/O操作完成的通知，并不主动读写数据，由操作系统内核完成数据的读写。  

> [知乎: 阻塞非阻塞和同步异步的区别](https://www.zhihu.com/question/19732473/answer/117012135)  

讨论究竟是异步还是同步，一定要严格说明说的是哪一部分。  
`非阻塞是同步而不是异步`，这毫无疑问是正确的，然而说某个框架是异步IO的框架，这也是正确的，因为说的其实是框架提供给业务代码的接口是异步的  
不管是回调还是协程，比如说我们可以说某个库是异步的HTTPClient，并没有什么问题，因为说的是给业务代码的接口。

> [参考](https://www.zhihu.com/question/19732473/answer/88599695)  

我认为同步、异步、阻塞、非阻塞，是分3个层次的：CPU层次；线程层次；程序员感知层次。 这几个概念之所以容易混淆，是因为没有分清楚是在哪个层次进行讨论。

**CPU层次**

在CPU层次，或者说操作系统进行IO和任务调度的层次，现代操作系统通常使用异步非阻塞方式进行IO（有少部分IO可能会使用同步非阻塞轮询），即发出IO请求之后，并不等待IO操作完成，而是继续执行下面的指令（非阻塞），IO操作和CPU指令互不干扰（异步），最后通过中断的方式来通知IO操作完成结果。

**线程层次**

在线程层次，或者说操作系统调度单元的层次，操作系统为了减轻程序员的思考负担，将底层的异步非阻塞的IO方式进行封装，把相关系统调用（如read，write等）以同步的方式展现出来。然而，同步阻塞的IO会使线程挂起，同步非阻塞的IO会消耗CPU资源在轮询上。为了解决这一问题，就有3种思路：多线程（同步阻塞）；IO多路复用（select，poll，epoll）（同步非阻塞，严格地来讲，是把阻塞点改变了位置）；直接暴露出异步的IO接口，如kernel-aio和IOCP（异步非阻塞）。

**程序员感知层次**

在Linux中，上面提到的第2种思路用得比较广泛，也是比较理想的解决方案。然而，直接使用select之类的接口，依然比较复杂，所以各种库和框架百花齐放，都试图对IO多路复用进行封装。此时，库和框架提供的API又可以选择是以同步的方式还是异步的方式来展现。如python的asyncio库中，就通过协程，提供了同步阻塞式的API；如node.js中，就通过回调函数，提供了异步非阻塞式的API。

总结因此，我们在讨论同步、异步、阻塞、非阻塞时，必须先明确是在哪个层次进行讨论。比如node.js，我们可以说她在程序员感知层次提供了异步非阻塞的API，也可以说在Linux下，她在线程层次以同步非阻塞的epoll来实现。

************************

# 多路复用
> [参考: IO多路复用](https://blog.csdn.net/chewbee/article/details/78108223)   

## 多路复用模型
Reactor 和 Proactor: 前者 使用同步IO, 后者使用异步IO

> [Comparing Two High-Performance I/O Design Patterns](https://www.artima.com/articles/io_design_patternsP.html)  

> [高性能网络模式：Reactor 和 Proactor](https://www.xiaolincoding.com/os/8_network_system/reactor.html)

Reactor 可以理解为「来了事件操作系统通知应用进程，让应用进程来处理」，而 Proactor 可以理解为「来了事件操作系统来处理，处理完再通知应用进程」。
因此，真正的大杀器还是 Proactor，它是采用异步 I/O 实现的异步网络模型，感知的是已完成的读写事件，而不需要像 Reactor 感知到事件后，还需要调用 read 来从内核中获取数据。
不过，无论是 Reactor，还是 Proactor，都是一种基于「事件分发」的网络编程模式，区别在于 Reactor 模式是基于「待完成」的 I/O 事件，而 Proactor 模式则是基于「已完成」的 I/O 事件。

### Reactor
- Redis：单 Reactor 单进程 
- Netty & Memcache: 主从多Reactor 多线程
- Nginx： 主从Reactor 多进程 *进程职责做了调整*

> [【Netty】模型篇一：Netty 线程模型架构 & 工作原理 解读](https://blog.csdn.net/qq_36389060/article/details/124232377)`包含了Reactor多种模式的图`  

![](/Skills/CS/img/001-reactor-multiple.drawio.svg)

> [TCP Server处理多Client请求的方法—非阻塞accept与select](http://velep.com/archives/1137.html)`可以看到系统调用层面也是先调用select发现新连接后调用accept和read write` [Github: Code](https://github.com/Kuangcp/LearnC/blob/master/network/tcp/nio-tcp.c)

### Proactor


### 忙轮询
忙轮询方式是通过不停的把所有的流从头到尾轮询一遍，查询是否有流已经准备就绪，然后又从头开始。如果所有流都没有准备就绪，那么只会白白浪费CPU时间。

### 无差别轮询
为了避免白白浪费CPU时间，我们采用另外一种轮询方式，无差别的轮询方式。即通过引进一个代理，这个代理为 select/poll ,这个代理可以同时观察多个流的I/O事件。  
当所有的流都没有准备就绪时，会把当前线程阻塞掉；当有一个或多个流的I/O事件就绪时，就从阻塞状态中醒来，然后轮询一遍所有的流，处理已经准备好的I/O事件。

如果I/O事件准备就绪，那么我们的程序就会阻塞在select处。我们通过select那里只是知道了有I/O事件准备好了，但不知道具体是哪几个流（可能有一个，也可能有多个），所以需要无差别的轮询所有的流，找出已经准备就绪的流。  
可以看到，使用select时，我们需要O(n)的时间复杂度来处理流，需要处理的流越多，消耗的时间也就越多。

### 最小轮询

通过epoll方式来观察多个流，epoll`只把发生了I/O事件的流`通知我们，我们对这些流的操作都是有意义的，时间复杂度降低到O（k），其中k为产生I/O事件的流个数。

## IO多路复用函数
> [参考: IO多路复用之select、poll、epoll详解](https://www.cnblogs.com/jeakeven/p/5435916.html)   
> [参考: select、poll、epoll之间的区别总结](https://www.cnblogs.com/Anker/p/3265058.html)  

IO复用机制可以同时监控多个描述符，当某个描述符就绪（读或写就绪），则立即通知相应程序进行读或写操作。   
select/poll/epoll都是采用I/O多路复用机制的，其中select/poll是采用无差别轮询方式，而epoll是采用最小的轮询方式。  
但 select，poll，epoll本质上都是同步I/O， 因为他们都需要在读写事件就绪后`自己`负责进行读写，也就是说这个读写过程是阻塞的    
所以 select poll epoll 都是 Reactor 模型

************************

### select

系统提供Select函数来实现多路复用输入/输出模型，Select系统调用是用来让我们的程序监视多个文件句柄的状态变化。程序会阻塞在select函数上，直到被监视的文件句柄中有一个或多个发生了状态变化。

`缺点`
1. 每次调用select，都需要把fd集合(存放所有fd)从用户态拷贝到内核态，这个开销在fd很多时会很大
1. 同时每次调用select, 都需要在内核`遍历`传递进来的所有fd，这个开销在fd很多时也很大
1. select支持的文件描述符数量太小了，默认是1024, 由FD_SETSIZE设置

************************

### poll
Poll的处理机制与Select类似，只是Poll选择了 pollfd 结构体 而不是 select 的 fd_set 结构来处理文件描述符的相关操作

但是它没有最大连接数的限制，原因是它是`基于链表`来存储的, 但是同样的需要将所有的文件描述符复制来复制去

poll还有一个特点是“水平触发”，如果报告了fd后，没有被处理，那么下次poll时会再次报告该fd。

************************

### epoll
> [参考: 从 linux 源码看 epoll](https://my.oschina.net/alchemystar/blog/3008840)  

epoll是在Linux内核2.6引进的，是select和poll函数的增强版。与select相比，epoll没有文件描述符数量的限制。  
epoll使用一个文件描述符管理多个文件描述符，将用户关心的文件描述符事件存放到`内核的一个事件列表`中  
这样在用户空间和内核空间`只需拷贝一次`, 因为用户空间和内核空间共用一块内存

epoll提供了三个函数:
- epoll_create是创建一个epoll句柄；
- epoll_ctl是注册要监听的事件类型；
- epoll_wait则是等待事件的产生。

epoll支持水平触发和边缘触发，最大的特点在于边缘触发，它只告诉进程哪些fd刚刚变为就绪态，并且只会通知一次。
还有一个特点是，epoll使用“事件”的就绪通知方式，通过epoll_ctl注册fd，一旦该fd就绪，内核就会采用类似callback的回调机制来激活该fd，epoll_wait便可以收到通知。

epoll的优点：
1. 没有最大并发连接的限制，能打开的FD的上限远大于1024（1G的内存能监听约10万个端口）。
2. 效率提升，不是轮询的方式，不会随着FD数目的增加效率下降。只有活跃可用的FD才会调用callback函数；
    - 即Epoll最大的优点就在于它`只处理“活跃”的连接`，而跟连接总数无关，因此在实际的网络环境中，epoll 的效率就会远远高于 select和poll。
3. 内存拷贝，利用 mmap() 文件映射内存加速与内核空间的消息传递；即 epoll 使用 mmap 减少复制开销。

> 如果没有大量的 idle-connection 或者 dead-connection，epoll 的效率并不会比 select/poll 高很多  
> 但是当遇到大量的 idle-connection，就会发现 epoll 的效率大大高于 select/poll。

> [百万 Go TCP 连接的思考2: 百万连接的吞吐率和延迟 ](https://colobu.com/2019/02/27/1m-go-tcp-connection-2/)


