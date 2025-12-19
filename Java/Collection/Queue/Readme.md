# Queue

## Disruptor
环形数组+CAS+缓存行独占（解决伪共享）

凡是 Producer-Consumer 且延迟敏感的地方，都可以用它替换 BlockingQueue：
- Log4j2 异步模式
