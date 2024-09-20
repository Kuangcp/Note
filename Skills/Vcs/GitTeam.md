---
title: Git在团队协作时的使用
date: 2018-12-20 10:29:41
tags: 
    - 软件工程
categories: 
    - 版本控制
---

💠

- 1. [使用Git进行团队协作](#使用git进行团队协作)
    - 1.1. [基础思想](#基础思想)
        - 1.1.1. [Git Flow](#git-flow)
        - 1.1.2. [Github Flow](#github-flow)
        - 1.1.3. [Trunk-Based](#trunk-based)
    - 1.2. [提交准则](#提交准则)
        - 1.2.1. [commit template](#commit-template)
    - 1.3. [Tips](#tips)
        - 1.3.1. [master作为线上分支时，误提交功能并推送怎么处理](#master作为线上分支时误提交功能并推送怎么处理)
- 2. [GUI](#gui)
    - 2.1. [git-cola](#git-cola)
    - 2.2. [Gitnuro](#gitnuro)
    - 2.3. [GitBlade](#gitblade)
    - 2.4. [gitg](#gitg)
    - 2.5. [tig](#tig)
    - 2.6. [Guitar](#guitar)
    - 2.7. [Gittyup](#gittyup)
    - 2.8. [SourceTree](#sourcetree)
- 3. [小规模团队使用码云组织的总结](#小规模团队使用码云组织的总结)
    - 3.1. [最终方案](#最终方案)

💠 2024-09-20 18:39:25
****************************************
# 使用Git进行团队协作

> [在阿里，我们如何管理代码分支？](https://blog.csdn.net/maoreyou/article/details/79877829)
> [版本控制最佳实践](https://www.git-tower.com/blog/version-control-best-practices/)

> [阮一峰 Git 使用规范流程](http://www.ruanyifeng.com/blog/2015/08/git-use-process.html)

> Github gitee gitlab bitbucket 等各大平台都是这样一种模式:
> 个人和个人开发者之间是并行master，只适合偶尔开发提交一些代码
> 组织就是适合给多个人，等同的稳定开发时，分支就会比较明确，这个笔记就是记录组织中git的使用

- 《Git团队协作》

## 基础思想

### Git Flow

> [Vincent Driessen 提出了 A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/)  
> [Gitflow workflow ](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)  

- [依据以上思想开发的 git flow工具](https://github.com/nvie/gitflow)
  - [介绍 Git Flow](https://datasift.github.io/gitflow/IntroducingGitFlow.html)
- [参考:  Git 在团队中的最佳实践--如何正确使用Git Flow](http://www.cnblogs.com/cnblogsfans/p/5075073.html)
  - [参考: Getting Started – Git-Flow](https://yakiloo.com/getting-started-git-flow/)

![规范的分支图](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/Git/git-team-model.png)

- Git Flow常用的分支
  - Production 分支
    - 也就是我们经常使用的Master分支，这个分支最近发布到生产环境的代码，最近发布的Release， 这个分支只能从其他分支合并，不能在这个分支直接修改
  - Develop 分支
    - 这个分支是我们是我们的主开发分支，包含所有要发布到下一个Release的代码，这个主要合并与其他分支，比如Feature分支
  - Feature 分支
    - 这个分支主要是用来开发一个新的功能，一旦开发完成，我们合并回Develop分支进入下一个Release
  - Release分支
    - 当你需要一个发布一个新Release的时候，我们基于Develop分支创建一个Release分支，完成Release后，我们合并到Master和Develop分支
  - Hotfix分支
    - 当我们在Production发现新的Bug时候，我们需要创建一个Hotfix, 完成Hotfix后，我们合并回Master和Develop分支，所以Hotfix的改动会进入下一个Release

### Github Flow

> [Understanding the GitHub flow](https://guides.github.com/introduction/flow/?from=singlemessage)

- [分支图复杂的一个项目](https://github.com/Netflix/eureka/network) `只是演示分支的复杂度`

### Trunk-Based
> [Trunk-Based Development](https://trunkbaseddevelopment.com/)`基于主干的单分支模型，不使用多分支`  

## 提交准则

> [参考: SVN提交更新的一个准则](http://www.cnblogs.com/chenlong828/archive/2008/09/22/1296193.html)

1. 提交之前先更新
   - SVN更新的原则是要随时更新，随时提交。当完成了一个小功能，能够通过编译并且并且自己测试之后，谨慎地提交。
   - 如果提交过程中产生了冲突，则需要同之前的开发人员联系，两个人一起协商解决冲突，解决冲突之后，需要两人一起测试保证解决冲突之后，程序不会影响其他功能。
   - 如果提交过程中产生了更新，则也是需要重新编译并且完成自己的一些必要测试，再进行提交。
2. 保持原子性的提交
   - 每次提交的间歇尽可能地短，以一个小时，两个小时的开发工作为宜。如在更改UI界面的时候，可以每完成一个UI界面的修改或者设计，就提交一次。在开发功能模块的时候，可以每完成一个小细节功能的测试，就提交一次，在修改bug的时候，每修改掉一个bug并且确认修改了这个bug，也就提交一次。我们提倡多提交，也就能多为代码添加上保险。
3. 提交时注意不要提交本地自动生成的文件
   - 对于Java来说, IDE自身配置文件, 和字节码文件是无需提交的 例如 .idea目录 iml文件
4. 不要提交不能通过编译的代码
   - 代码在提交之前，首先要确认自己能够在本地编译。如果在代码中使用了第三方类库，要考虑到项目组成员中有些成员可能没有安装相应的第三方类库，项目经理在准备项目工作区域的时候，需要考虑到这样的情况，确保开发小组成员在签出代码之后能够在统一的环境中进行编译。
5. 不要提交自己不明白的代码
   - 提交之后, 你的代码将被项目成员所分享。如果提交了你不明白的代码，你看不懂，别人也看不懂，如果在以后出现了问题将会成为项目质量的隐患。因此在引入任何第三方代码之前，确保你对这个代码有一个很清晰的了解。
6. 提前协调好项目组成员的工作计划
   - 在自己准备开始进行某项功能的修改之前，先给工作小组的成员谈谈自己的修改计划，让大家都能了解你的思想，了解你即将对软件作出的修改，这样能尽可能的减少在开发过程中可能出现的冲突，提高开发效率。同时你也能够在和成员的交流中发现自己之前设计的不足，完善你的设计。
7. 对提交的信息采用明晰的标注
   - `+)` 表示增加了功能
   - `*)` 表示对某些功能进行了更改
   - `-)` 表示删除了文件，或者对某些功能进行了裁剪，删除，屏蔽。
   - `b)` 表示修正了具体的某个bug

> [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

### commit template

> git commit message 的模板化

commit message 包含三个部分，header, body和footer，其中header必须有，body和footer可以按情况省略。

- `type` 字段
  - feat：新功能（feature）
  - fix：修补bug
  - docs：文档（documentation）
  - style： 格式（不影响代码运行的变动）
  - refactor：重构（即不是新增功能，也不是修改bug的代码变动）
  - test：增加测试
  - chore：构建过程或辅助工具的变动
- `scope` 用于说明 commit 影响的范围，比如数据层、控制层、视图层等等，视项目不同而不同。 也就是写用户会感觉到改变在哪个地方。
- `subject` 是 commit 目的的简短描述，不超过50个字符
  - 以动词开头，使用第一人称现在时，比如change，而不是 changed 或 changes 第一个字母小写 结尾不加句号（.）
- `Body` 部分是对本次 commit 的详细描述，可以分成多行
  - 使用第一人称现在时，比如使用change而不是changed或changes。
  - 应该说明代码变动的动机，以及与以前行为的对比。
- `Footer`
  - 如果当前代码与上一个版本不兼容，则 Footer 部分以BREAKING CHANGE开头，后面是对变动的描述、以及变动理由和迁移方法。
  - 关闭 Issue

1. 新建 ~/.gitmessage 文件
2. ~/.gitconfig 中添加

```
    [commit]
    template = ~/.gitmessage
```

> 配置好后 git commit 不指定-m 参数就会调用该模板

---

## Tips

### master作为线上分支时，误提交功能并推送怎么处理

> master 分支

```log
* 259cf80 2021-01-23 18:20:46 五 (HEAD -> master) kcp fea2: remove
*   46e3af2 2021-01-23 18:20:32 五 kcp Merge branch 'fea-1'
|\  
| * abf3d18 2021-01-23 18:12:14 五 (fea-1) kcp fea1: add
* | 7d7d5a3 2021-01-23 18:10:50 五 kcp fea2: update
* | e5d95da 2021-01-23 18:10:40 五 kcp fea2: add
|/  
* a75d6fd 2021-01-23 18:10:16 五 kcp release 1.0
* ebffe4d 2021-01-23 18:09:53 五 kcp init
```

> fea-1 分支

```log
* abf3d18 2021-01-23 18:12:14 五 (HEAD -> fea-1) kcp fea1: add
* a75d6fd 2021-01-23 18:10:16 五 kcp release 1.0
* ebffe4d 2021-01-23 18:09:53 五 kcp init
```

目标： master分支撤销所有 fea2 提交信息的提交(*错误提交*)

1. 从 master 分支新建功能分支 dev
2. 切换 dev 分支。 通过 `git reset --soft HEAD^` 把 *错误提交* 全部撤销到工作区 并 git stash
3. 切换 master分支。 使用 git revert 撤销 master 分支上的所有 *错误提交*
   - 在回滚 merge 时，需要 通过 -m 指定 revert到哪个commit
   - (git log 中看到的合并commit下的 `commit id` 信息 左为1 右为2) 此处 1 为 7d7d5a3 2 为 abf3d18
4. 切换 dev 分支 合并master, pop stash 的内容，并提交， 此时就已经把 fea2 代码 拆分到 dev 分支上，保证了master分支的正确性
5. *注意* 此时 fea-1 的代码 已经被回滚了，master 上 fea-1 的修改全部消失
6. 切换到 fea-1 分支，依次 `git reset --soft HEAD^` 所有功能提交， 使得fea-1 指向master旧提交节点(此时 fea-1等价于master，但是落后了若干个commit)
   - stash 所有修改， 合并 master, pop 并提交
7. 切换 dev 合并 fea-1 等待下次上线
8. 此时就保证了 master 分支和 错误提交前 基本一致，但是丢失了 fea-1 的功能，其他人需要开发新功能 合并入 fea-1 即可
9. dev 上线后, 合并入master， master分支就具有了 fea-1 fea-2 分支的功能

> 经过这系列操作后，master分支会多出很多 revert 提交，但是不会对其他人的部分产生影响，最后功能上线后，也能正确的合入master

---

# GUI

> 诚然, 命令行是高效的, 在单兵作战或者说没有使用多分支的情况下是没有问题的
> 当多人协作时, 需要Review代码，处理代码冲突, 查看每个人每次提交的修改内容时, 图形化工具会更高效

> [Git官方收纳的GUI列表](https://git-scm.com/downloads/guis)
> [client on linux ](https://unix.stackexchange.com/questions/144100/is-there-a-usable-gui-front-end-to-git-on-linux)

giggle

## git-cola

> [Github: repo](https://github.com/git-cola/git-cola) `轻量, 简洁, 跨平台`

从源码安装是最快最简单的, 而且能安装到最新的

1. git clone --depth 1 git://github.com/git-cola/git-cola.git
2. sudo make prefix=/usr install

> Tips

- [X] 无法输入中文问题： 需要安装 fcitx-qt5 模块

## Gitnuro

> [Github: Gitnuro](https://github.com/JetpackDuba/Gitnuro) `Java17 + Compose`

## GitBlade

- 功能强大 付费软件 Sublime作者所开发

## gitg

> [Official](https://wiki.gnome.org/Apps/Gitg)

## tig

> [Github](https://github.com/jonas/tig)

## Guitar

> [Github](https://github.com/soramimi/Guitar)

## Gittyup

> [Gittyup](https://github.com/Murmele/Gittyup)

> [Github](https://github.com/gitahead/gitahead) | [Official Site](https://gitahead.com)

## SourceTree

> [Official site](https://sourcetreeapp.com) 仅支持 Windows 和 Mac

---

# 小规模团队使用码云组织的总结

> `master`发行分支 `dev`开发主分支 `dev-*`开发者分支 `fea-*`开发者自己的功能性分支

- 在码云上创建私有仓库，然后管理成员，将开发者一一邀请进来，然后这时候就有了一个问题：
  - 所有的开发者都具有master的所有权限，所以这时候就会很容易出现冲突,所以就需要设置master和开发主分支dev为保护模式，只有管理员负责进行推送
  - 管理员， 新建若干分支：`git branch 分支` 提交到远程 `git push --all`
  - 对应的开发者克隆项目，然后 `git checkout 对应的自己的分支` 就可以开始工作了
    - （ 如果没有分支就下拉命令 `git fetch origin 对应的分支`）
  - 然后各个开发者写自己的，然后提交 `git push` 就行了
  - 管理员需要 `git fetch origin 分支`得到所有分支
    - 针对每个分支进行拉取： 切换过去 `git checkout 开发者分支`，然后 `git pull 开发者分支`下拉最新
    - 然后选择合并 `git merge --no-ff 开发者分支` ，处理冲突然后提交
  - 开发者下拉自己的分支 或者开发主分支 dev 即可

---

`分支的处理的一次实验 2017-10-21 23:57:34`

- `git fetch --all` 获取远程所有分支（新分支）
- `git pull --all` 获取所有分支最新提交 这个就会自动合并？？？越来越不理解了
- dev-test 分支进行修改，然后提交一次，然后push
- master： `git merge --no-ff dev-test` 进行合并，就会在分支图上得到一个环

  - master 分支本地会多出2个提交
- dev-test 进行修改，然后1次提交，push
- master : `git pull origin dev-test ` 执行merge命令就会提示没有可以合并的修改。

  - 这是为什么？？？？

## 最终方案

`双方都有修改`

- 开发人员提交完后，主分支管理人员切换到开发人员的分支然后 `git pull 开发人员分支`，然后切换回主分支上 `git merge --no-ff 开发人员分支`（填写注释） 然后push
  - 然后切换到开发人员分支上执行 `git merge master 然后 git push` 还是 `git pull origin master`
  - 然后通知开发人员下拉其自己的开发分支即可

`只有一方修改`

- 主分支进行修改了开发分支没有动，那么开发分支 直接下拉 `git pull origin master`下拉修改代码即可
- 如果是开发分支修改，主分支没有动，那么管理员负责切换到开发分支 然后pull 然后merge 然后 push 然后切换开发分支 然后 pull
