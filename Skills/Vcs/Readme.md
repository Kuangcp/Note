# 常见VCS

## Git
> 分布式的去中心化的, 大多数操作是本地化操作, 速度快, 更方便
> 缺点有 处理大仓库时会很慢, 没有访问权限的控制， 不适用二进制文件管理， submodules使用不方便
- 最大的区别是其他的 VCS 都是 一个增量式的文件集合, git 是文件的一系列快照, 类似于 AUFS 文件系统一层一层那样

## Repo
Repo 简化了跨多个代码库运行的流程，与 Git 相辅相成

## SVN
> [Svn笔记](/Skills/Vcs/Svn.md)

1. 中心化的, 代码统一保存, 如果中心发生错误, 代码会全部毁掉, 提交是必须要和服务端通信才能完成
2. 允许部分的进行修改, 下拉, 提交. 而对于Git来说一个仓库就是一个整体(Git submodule 目前也能完成, 但是还是没有SVN灵活)
3. 优点: 能够精确控制每个目录的每个人的访问权限

************************

**`Git和SVN同时使用`**

可以通过 git-svn 使用Git的命令与SVN服务器进行交互
> [Official doc: git-svn](https://git-scm.com/docs/git-svn)

> 但是个人目前在用的方式是直接 git 和 svn 一起用, 因为项目只能用SVN的原因  
> [参考: 为啥要同时用 SVN 和 Git 管理项目](https://www.cnblogs.com/dasusu/p/7774469.html)

1. 避免 CRLF LF 问题
```sh
    git config --global core.autocrlf false
    git config --global core.safecrlf false
```
1. 互相忽略各自配置目录 .svn .git

- 至此, 就能和团队保持一致的使用SVN, 然后自己多任务开发时, 又能使用git优秀的分支模型
- 当然该场景是有限的, 也就是说只有你一个人在用git 而且团队中使用SVN时没有使用SVN的分支模型, 这个是没有问题的
    - 如果SVN也用了分支, 那么就要命了, 这么多分支和状态, 要靠大脑记住实时的状态就....
- 还有一个点就是分工比较明确，开发中没有互相依赖，不然就需要在Git SVN都需要频繁解决冲突
- 所以这只是权宜之计

## PerForce

## Mercurial

## CVS
