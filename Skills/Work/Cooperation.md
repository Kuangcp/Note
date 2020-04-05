---
title: 开发中的团队协作
date: 2019-01-27 23:37:38
tags: 
categories: 
    - 团队
---

**目录 start**
 
1. [协作](#协作)
    1. [代码规范](#代码规范)
    1. [Code Review](#code-review)

**目录 end**|_2020-04-05 19:41_|
****************************************
# 协作 

## 代码规范
> [Google Guide](https://google.github.io/styleguide/javaguide.html)| [FaceBook Guide](https://github.com/facebook/jcommon/wiki/Coding-Standards) | [阿里巴巴Java开发手册](https://github.com/alibaba/p3c) | [Twitter Java Style Guide](https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md)


## Code Review
> [知乎: 大家的公司的 Code Review 都是怎么做的？遇到过哪些问题？](https://www.zhihu.com/question/41089988/)

> 相关工具
- Crucible Atlassian 内部使用
- Gerrit Google 开源
- PullRequest, LGTM, Reviewable, Sider : Github体系基于PullRequest模型
- Phabricator Facebook 开源的
- [Upsource](https://www.jetbrains.com/upsource/download/#section=docker)`JetBrain`

> [Code Review 是一场苦涩但有意思的修行](https://mp.weixin.qq.com/s?__biz=MzU4NzU0MDIzOQ==&mid=2247489170&idx=1&sn=e47dcf2227517172ff97105e8a0543d0&chksm=fdeb24f2ca9cade4985b11abd05d4c8e2fdf2cf9b5a73dbe27d320a036d684563679e8d5c565&mpshare=1&scene=1&srcid=&sharer_sharetime=1586018672545&sharer_shareid=246c4b52c1cb45eaa580c985c95107f3#rd)  

- 代码是讲道理的
    - 优秀的代码，就是在小流量、单线程没有问题，在高流量、高并发时还是没有问题，你的限流，你的容灾，你的降级各种导弹防御系统一样自动打开并正确地发挥价值。很多人的思维觉得，代码只要在场景和逻辑上没有问题就行，那是因为夜路走得不够多，还没有碰到鬼。
- 每一行代码的存在是有意义的
    - 更加严格地说，每一个字符的存在都应该是有意义的。如果某行代码的存在完全是可有可无的，这个时候，我们考虑过 JVM 的感受吗？凭白无故地要编译这些字节码，然后栈进栈出的忙活一阵子，然后告诉它，你的劳动是没有任何价值的。
- 多个 return 的语句，概率高的一定先进行判定
    - if(condition1) return; if(condition2) return; if(condition3) return ; 
    - 那么需要评估一下 condition1/2/3 出现概率的大小，概念大的在最前边，尽可能快地进行 return ，不需要进行后续无谓的匹配。
- 我们比拼的不是代码行数
    - 如果在同样的效果上， 3 行代码能够实现功能的价值，就不应该用 4 行来实现。我们经常说晒出代码行数，并非是单纯地鼓励代码行数多，而是提倡大家去写代码，写优质的代码，优质的代码一定是少即是多的原则。
- 用户视角的成功与失败
    - 后台调用服务失败，就应该明确告诉前台，服务出错了，这个用户有没有数据。
    - 系统出错的信息给用户看，合适吗？不合适。前后端的用户交界面上，往往飞着两类信息：错误码、错误信息。这样够了吗？
        - 用户提示需要额外地再给出来，往往根据不同的错误码，有不同的用户提示，可能是一个多对多的关系。
        - 多个错误码，提示给用户的信息：请输入必填项。多个用户信息，可能也对应一个错误码。一般来说后台承包这三者的联动关系， json 串推送给前端时，前端拿来主义即可。
- 有重复使用的量一定要找个地方集中隔离
    - 不管是变量，还是常量，工具类，如果是多个地方同时用到，那么如果硬编码在代码或者沉淀在包里，未来一定是一个灾难。
- 单测没必要代码 Code Review ?
    - 单测是否需要 MOCK ，是否进行边界值测试，是否用例覆盖到业务场景，这都也是 CR 的一部分。单测写得好， BUG 肯定少。
- 良好的日志和异常机制，是不应该出现调试的。
    - 打日志和抛异常，一定要把上下文给出来，否则，等于在毁灭命案现场，把后边处理问题的人，往歪路上带。
    - 别人传一个参数进来，发现是 null ，立马抛出来一个参数异常提示，然后也不返回哪一个参数是 null ，这在调用参数很多的情况下，简直就是字谜游戏一样。
    - 到底是抛异常，还是抛错误码？我不管抛什么，反正错了什么东西，都应该透明出来。到底是抛受检异常，还是非受检异常，我只想说，没有充足的理由，不要乱抛受检异常。异常抛出时，一定要自己消化干净，告诉别人说我的方法签名抛的是 AbcException ，实际运行中，代码某个地方直接抛出 EfgException ，这也是不负责任的。

- 吝啬空行
    - 感觉空行是廉价的，到处乱扔是一种；另一种是感觉空行是昂贵的，舍不得用，这种情况更多见。50 行代码没有一个空行，就像英语 50 句话，没有任何标点符号一样。既然标点符号起到隔断和语义区分作用，我们的空行不是同一个道理吗？
    - 在以下情形：
        1. 在方法的 return、break、continue、这样断开性语句后必须是空行。
        2. 在不同语义块之间。
        3. 循环之前和之后一般有空行。另外，方法和类定义下方就不需要空行了吧。
- 命名太随意
    - 英语不好的同学，要么用错英文单词，要么翻词典，整出一个专八的词汇，任何人都不认得这个单词，在 CR 时，还需要打开在线翻译时的命名，绝对不是好命名。 当然如果在线翻译都翻不出来的时候，那更头疼。如果表意错误，那更要命。
