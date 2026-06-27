---
title: FluxConcept
date: 2025-01-07 09:56:23
tags: 
categories: 
---

💠

- 1. [WebFlux 设计概念](#webflux-设计概念)
    - 1.1. [Reactor 中 ThreadLocal 的问题](#reactor-中-threadlocal-的问题)
        - 1.1.1. [问题根源：反应式链路的线程切换](#问题根源反应式链路的线程切换)
        - 1.1.2. [Reactor 的上下文传递机制](#reactor-的上下文传递机制)
            - 1.1.2.1. [MDC 配合 WebFlux](#mdc-配合-webflux)
        - 1.1.3. [与虚拟线程的对比](#与虚拟线程的对比)

💠 2026-06-27 22:57:30
****************************************
# WebFlux 设计概念

************************

## Reactor 中 ThreadLocal 的问题

### 问题根源：反应式链路的线程切换

ThreadLocal 将数据绑定在 OS 线程上，而 Reactor 的异步执行模型中，Mono/Flux 链路各阶段的操作符可能在不同线程执行，导致 ThreadLocal 值错位——读到的是别的请求遗留在线程上的旧值。

```java
// 反例：在 WebFlux 中用 ThreadLocal 传递 userId
@RestController
public class OrderController {

    private static final ThreadLocal<String> CURRENT_USER = new ThreadLocal<>();

    @Autowired private OrderService orderService;

    @PostMapping("/order")
    public Mono<String> createOrder(ServerWebExchange exchange) {
        String userId = extractUserId(exchange);
        CURRENT_USER.set(userId); // ❌ 此时 set 在线程 T1

        return orderService.queryBalance(userId)
                .flatMap(balance -> {
                    // ❌ flatMap 可能在线程 T2/T3 执行
                    // CURRENT_USER.get() 拿到的可能是其他请求的 userId
                    String user = CURRENT_USER.get();
                    return placeOrder(user, balance);
                })
                .doFinally(s -> CURRENT_USER.remove()); // remove 也不一定在线程 T1
    }
}
```

### Reactor 的上下文传递机制

Reactor 提供与 ThreadLocal 无关的 Context 机制，上下文存储在每次操作的 Subscription 内部，跟随信号链路传递。

- **Reactor 3.5+**：`Mono.deferContextual()` / `Flux.deferContextual()` + `contextWrite()`
- **Reactor 3.1-3.4**：`subscriberContext()`（已废弃）
- **全局 hook**：`Hooks.onEachOperator()` 可以在每个操作符执行前将 context 中的值注入 MDC

```java
// Reactor Context 正确用法
public Mono<String> createOrder(ServerWebExchange exchange) {
    String userId = extractUserId(exchange);

    return orderService.queryBalance(userId)
            .flatMap(balance -> Mono.deferContextual(ctx -> {
                String user = ctx.get("userId"); // ✅ 从 Reactor Context 取值
                return placeOrder(user, balance);
            }))
            .contextWrite(ctx -> ctx.put("userId", userId)); // 写入 Context
}
```

> [Reactor Doc: Context](https://projectreactor.io/docs/core/release/reference/#context)

#### MDC 配合 WebFlux

slf4j MDC 底层同样基于 ThreadLocal，在 WebFlux 中需要借助 `Hooks.onEachOperator` 或 `Scheduler` hook 将 Reactor Context 中的 traceId 同步到 MDC，并在操作符完成后清理。

> [WebFlux MDC Logging](https://docs.spring.io/spring-framework/reference/web/webflux/logging.html)

### 与虚拟线程的对比

虚拟线程在 mount/unmount 时拷贝 ThreadLocal 存储，因此功能上 ThreadLocal 在虚拟线程中是**正确但昂贵**的——每个虚拟线程持有一份独立副本，大量虚拟线程时内存开销显著。

ScopedValue 是 JDK 21 引入的更优替代：不可变、可继承、作用域结束自动清理，与结构化并发更为契合。

关键差别：**WebFlux 不受益于虚拟线程或 ScopedValue**，因为反应式模型的线程切换不是在虚拟线程 mount/unmount 语义内进行的——操作符级别的线程切换是 Scheduler 决定的，不会触发 ThreadLocal 拷贝或 ScopedValue 作用域传递。Reactor Context 才是 WebFlux 中传递上下文的正解。

> [Note: ThreadLocal & ScopedValue](/Java/AdvancedLearning/JavaThread.md#threadlocal)

