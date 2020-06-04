---
title: Git基础
date: 2018-11-21 10:56:52
tags: 
    - 基础
categories: 
    - 版本控制
---

**目录 start**

1. [Git基础](#git基础)
1. [开源许可证](#开源许可证)
1. [Git常用命令](#git常用命令)
    1. [基本命令](#基本命令)
        1. [config](#config)
        1. [clone](#clone)
            1. [Shallow Clone](#shallow-clone)
        1. [add](#add)
        1. [rm](#rm)
        1. [status](#status)
        1. [commit](#commit)
        1. [restore](#restore)
        1. [revert](#revert)
        1. [show](#show)
        1. [log](#log)
            1. [对比两个分支的差异](#对比两个分支的差异)
            1. [查看文件的修改记录](#查看文件的修改记录)
        1. [blame](#blame)
        1. [diff](#diff)
            1. [diff 创建 patch](#diff-创建-patch)
        1. [apply](#apply)
        1. [format-patch](#format-patch)
        1. [am](#am)
        1. [tag](#tag)
        1. [notes](#notes)
        1. [reset](#reset)
            1. [回滚add操作](#回滚add操作)
            1. [回滚最近一次commit](#回滚最近一次commit)
            1. [回滚最近几次的commit并添加到一个新建的分支上去](#回滚最近几次的commit并添加到一个新建的分支上去)
            1. [回滚merge和pull操作](#回滚merge和pull操作)
            1. [在index已有修改的状态回滚merge或者pull](#在index已有修改的状态回滚merge或者pull)
            1. [被中断的工作流程](#被中断的工作流程)
        1. [gc](#gc)
        1. [clean](#clean)
    1. [本地分支](#本地分支)
        1. [show-branch](#show-branch)
        1. [stash](#stash)
            1. [stash 创建 patch](#stash-创建-patch)
            1. [恢复被drop的stash](#恢复被drop的stash)
        1. [branch](#branch)
        1. [checkout](#checkout)
        1. [switch](#switch)
        1. [merge](#merge)
        1. [rebase](#rebase)
        1. [cherry-pick](#cherry-pick)
        1. [bisect](#bisect)
        1. [worktree](#worktree)
    1. [远程操作](#远程操作)
        1. [remote](#remote)
        1. [push](#push)
        1. [fetch](#fetch)
        1. [pull](#pull)
    1. [Submodule](#submodule)
    1. [其他](#其他)
        1. [gitk](#gitk)
        1. [grep](#grep)
        1. [archive](#archive)
        1. [reflog](#reflog)
        1. [rev-parse](#rev-parse)
1. [配置文件](#配置文件)
    1. [.gitignore](#gitignore)
    1. [gitattributes](#gitattributes)
1. [自定义插件](#自定义插件)

**目录 end**|_2020-05-30 15:48_|
****************************************
# Git基础
> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. -- [git-scm.com](https://git-scm.com/)

> [Github:git](https://github.com/git/git) | [official doc: git](https://git-scm.com/docs)  
> [arch wiki: Git](https://wiki.archlinux.org/index.php/Git)  

> [Gitee: about git](https://gitee.com/all-about-git)  

- index stage work 三个概念上的区域
    - index: 已经 commit 的内容, 不可更改历史commit 
    - stage: 执行 add 命令, 将文件缓存到该区
    - work: 工作目录, 日常做修改的就是该分区

- [tig](https://github.com/jonas/tig)

# 开源许可证
> [License](/Skills/Document/License.md)

**********************
# Git常用命令
> [git-tips](https://github.com/521xueweihan/git-tips)`学习Git的仓库`  
> [git权威指南的组织](https://github.com/gotgit)`完整书籍,以及相关测试题`

> [使用原理视角看 Git](https://coding.net/help/doc/practice/git-principle.html)
> [如何高效地使用 Git](https://zhuanlan.zhihu.com/p/30561653)

> [参考: 重看”Linus Torvalds on Git”视频](http://www.techug.com/post/review-of-linus-torvalds-on-git.html)
> [GUI客户端](https://git-scm.com/downloads/guisQ)

- [tig](http://jonas.nitro.dk/tig/manual.html) `tig命令，git的加强版`

***************

## 基本命令
> 使用 `git help 加上命令`, 就能看到命令对应的文档

### config
- 三种配置方式 作用范围越大, 生效优先级越低
    - `--system` 作用所有用户, 对应文件 `/etc/gitconfig`
    - `--global` 作用当前用户, 对应文件 `~/.gitconfig` 
    - (缺省) `--local`作用当前项目, 对应文件 `./.git/gitconfig`

- `git config user.email ***`  和   `git config user.name ***` 这两个是必须的，
- `git config http.postBuffer 524288000` 设置缓存区大小为 500m
- `git config core.fileMode false` 忽略文件的mode变化，一般发生在文件放在挂载盘的时(默认755)

打开`~/.gitconfig`文件能够发现这是 ini 格式的配置文件
```ini
[user]
    email = kuangcp@aliyun.com
    name = kuangcp
[core]
    quotepath = false # 配置路径显示为中文
    autocrlf = false
    safecrlf = false
[credential]
    helper = store
[merge]
    tool = kdiff3 # 用于比较差异时使用的工具
[diff]    
    tool = meld # 配置在merge中发生冲突时的编辑工具,和diff中的tool近乎一致
```

> 可用： opendiff kdiff3 tkdiff xxdiff meld kompare gvimdiff diffuse diffmerge ecmerge p4merge araxis bc codecompare smerge vimdiff emerge  
> [工具 详细](/Linux/Base/LinuxFile.md#比较文件内容)

************************

### clone
- `git clone URL 目录` 克隆下来后更名为指定目录
- `-b branch` 克隆远程仓库的指定分支  **从Git 1.7.10开始支持**
- `--single-branch` 只克隆当前分支

#### Shallow Clone
- `git clone --depth 1 URL` 只克隆最近一次提交的历史, 能大大减小拉取的大小 
    - 但是如果要新建一个远程仓库, 并推送过去，会报错:`shallow update not allowed` 因为本地库是残缺的
        - 此时需要 `git remote set-branches origin '*'` 然后 `git pull` 就会拉取所有信息成为完整的仓库
    - 由于库是残缺的，拉取远程分支到本地不能直接用 `git checkout -b branch origin/branch` 的方式，
        - 只能用 `git fetch origin branch:branch`
        - 并且跟踪远程也需手动执行 `git push -u origin branch`
        - 并且 git log 的输出不会显示 origin/branch 的指针信息，需要在对应分支上手动执行 `git remote set-branches origin branch` 再 `git fetch`

1. 只克隆 指定标签或分支 且不包含内容 `git clone -b <tag_name> --single-branch --depth 1 <repo_url>` **大大缩减需下载的仓库大小**
1. TODO 变基 补充 shallow commit

************************

### add 

- 添加文件或目录 `git add file dir ...`
- 添加当前文件夹以及子文件夹 `git add .`
- 交互式添加每个文件的每部分修改 `git add -p`

************************

### rm

- 删除文件 `git rm file1 file2 ...`
- 仅从git仓库中删除文件, 但是文件系统中保留文件 `git rm --cached 文件`
    - 如果仅仅是想从仓库中剔除, 那么执行完命令还要在 `.gitignore` 文件中注明, 不然又add回去了

************************

### status
> git status --help 查看详细介绍

- `-s --short` 简化输出
    - ?? 表示新添加未跟踪
    - A 新添加到暂存区
    - M 修改过的文件
    - MM 修改了但是没有暂存

************************

### commit
> [Official Doc](https://git-scm.com/docs/git-commit)

- `git commit -am "init" `: a git库已有文件的修改进行添加, m 注释
    - `git add * ` 如果有新建立文件就要add 再之后commit就不要a参数了 `git commit -m ""`
    - 如果只是修改文件没有新建 `git commit -am ""`

- `git commit ` 会自动进入VI编辑器
    - 第一行：用一行文字简述提交的更改内容
    - 第二行：空行
    - 第三行：记述更改的原因和详细内容
    - 使用下面方法关闭退出

- `--amend` 追加文件到上次commit
    - 如果上次提交漏了文件, 只需把漏的文件加入到 index区中, 然后执行 git commit --amend 即可
    - 注意: 如果没有将前一个提交推送到远程, 那么没有任何影响, 
    - 如果已经推送上去了, 就相当于该次 --amend 操作是新开了个分支完成的修改, git log 里会出现一个分支的环
- `--no-edit` 沿用上次 commit msg
- `--allow-empty` 提交空提交

************************

### restore

- 将 Readme.md 回滚到 master倒数第三个 commit 的状态 `git restore -s master~2 Readme.md`
    - 回滚至指定提交 `git restore -s commitid filepath`
- 撤销所有Java文件修改 `git restore '*.java'` 注意支持 regex
- 撤销工作目录所有修改 `git restore :/`

************************

### revert 

> [Doc](https://git-scm.com/docs/git-revert)

1. 取消所有暂存 `git revert .`
1. 回滚上一次提交 `git revert HEAD`
1. 撤销某次提交 `git revert commitId` 注意该操作可嵌套 即 撤销撤销某次提交
1. 回滚代码至指定提交 `git revert --no-commit 032ac94ad...HEAD`
    - `git commit -m "rolled back"`

> 场景: 一个特性分支不该合并到主开发分支, 但是已经合并了, 并且合并后又做了很多其他修改, 这时候怎么影响最小地撤销这次错误的合并? 
1. 找到 merge 的 commitId，git show commitId 找到 Merge: 后两个commitId 分别记为 1 2 
1. 如果保留1, 删除2节点提交的内容 则 `git revert commitId -m 1`

************************

### show
> 展示提交信息

- 显示当前提交的差异 `git show HEAD` 
    - HEAD替换成具体的 commit id就是显示指定提交的修改内容
    - 注意这里有个 `^` 语法 HEAD^ 就是HEAD的前一次，两个就是前两次，commit id 同理 
    - 还有一个 `~` 语法 例如 ~2 ~3 就等价于 ^^ ^^^
        - 特别注意 `git show HEAD~2^2` 表示取第前两次提交的第二个父提交， 如果这是一个merge节点的话，否则会报错
        - `第一父提交`是合并时所在分支，`第二父提交`是所合并的分支
    - 可借助 git reflog 命令的输出找到对应的位置 例如 `HEAD{10}`

************************

### log
> 更多说明 查看 `git help log` | [Official Doc](https://www.git-scm.com/docs/git-log)

- `-g` 包含 reflog 信息
- `-p` 显示所有提交的修改内容 `git log -p -2` 则仅显示最近两次提交的差异
- `--stat` 查看每一次提交的修改文件修改概述  也就是在pull时能看到的那些++--的内容

- `---pretty=[online/short/full/fuller/format]` 使用预定义格式显示
    - format 可自定义格式和占位符 详情查看 -h

- 图形的样子显示分支图 `--graph` 
- 显示每个分支最近的提交 `--simplify-by-decoration`
- 输出简短且唯一的 SHA-1 值 `--abbrev-commit` 
    - 注意 SHA-1 20 byte长度 出现冲突的概率是 (n*(n-1)/2) / 2^160

- `git log --author='A' `输出所有A开头的作者日志
- `git log 文件名 文件名` 输出更改指定文件的所有commit 要文件在当前路径才可
- `git log --after='2016-03-23 9:20' --before='2017-05-10 12:00' ` 输出指定日期的日志

- `git shortlog` 按字母顺序输出每个人的日志 
    - `--numbered` 按提交数排序
    - `-s` 只显示每个提交者以及提交数量

> **`彩色输出Log`**
```sh
    alias glogc="git log --graph --pretty=format:'%Cred%h%Creset %Cgreen%ad%Creset | %C(bold cyan)<%an>%Creset %C(yellow)%d%Creset %s ' --abbrev-commit --date=short" # 彩色输出
    alias gloga='git log --oneline --decorate --graph --all' # 简短彩色输出
    alias glo='git log --oneline --decorate' # 最简单
    alias glol='git log --graph --pretty='\''%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'
    alias glola='git log --graph --pretty='\''%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'' --all'
```

#### 对比两个分支的差异
> [参考博客 git 对比两个分支差异](http://blog.csdn.net/u011240877/article/details/52586664)

> commit 差异
- 查看在dev分支，而不在master分支上的 commit. 
    - `git log master..dev`
    - 或者 `git log dev ^master` (^表示非，等价于 --not) 
        - 但是 ^ 语法支持多个分支 例如 `git log dev ^master ^fea/feature1` 意为：在dev分支但是不在后两个分支中的commit
    - 还可对比远程分支和本地分支的差别 `git log origin/master..master`

- 对比分支的差别 `git log dev...master` 也就是那些非两个分支共有的commit
    - 显示出每个提交是在哪个分支上 `git log --left-right dev...master`
    - 注意 commit 后面的箭头，根据我们在 –left-right dev…master 的顺序，左箭头 < 表示是 dev 的，右箭头 > 表示是 master的。

> 内容差异
- `git diff dev master` 可以理解为 从 dev 分支切换到 master 分支将发生的修改

#### 查看文件的修改记录
1. git log fileName 或者 git log --pretty=oneline fileName 更容易看到 sha-1 值
1. git show sha-1的值 就能看到该次提交的所有修改

************************

### blame
> 查看文件修改记录 追责

`git blame file`

************************

### diff
- 默认是将 work 区 和 index 区 进行比较
    - `--cached` stage 区 和 index 区 进行比较, 等同于`--staged`

```
    git diff [options] [<commit>] [--] [<path>...]
    git diff [options] --cached [<commit>] [--] [<path>...]
    git diff [options] <commit> <commit> [--] [<path>...]
    git diff [options] <blob> <blob>
    git diff [options] [--no-index] [--] <path> <path>
```

> [Github:diff-so-fancy](https://github.com/so-fancy/diff-so-fancy)`一个更方便查看diff的工具`
- 最简单的就是 `npm install -g diff-so-fancy` 安装 

#### diff 创建 patch 

- 创建分支之间的patch `git diff branch1 branch2 > first.patch`
- 创建分支之间具体文件的patch `git diff branch1 branch2 path/file1 path/file2 > first.patch`
    - 注意文件是命令行当前路径的相对路径
- 创建单文件的patch `git diff filePath > first.patch` 路径为Git项目根路径的相对路径

************************

### apply
> 使用 diff 或者 stash 得到的 patch 文件

- `git apply --ignore-space-change --ignore-whitespace first.patch`
- `patch -p1 < first.patch`

************************

### format-patch
> Prepare patches for e-mail submission  
> [参考: How To Create and Apply Git Patch Files](https://devconnected.com/how-to-create-and-apply-git-patch-files/)  

- `git format-patch -1 commit-sha` 指定commit 创建 patch
    - 参数选项可以为 `-2` `-3`... 数字表示 commit id 之前的 几个 commit 也创建 patch
- `git format-patch master -o patches` 对那些 master分支 中有而当前分支没有的 commit 创建 patch 到 patches 目录

- `git format-patch master  --stdout > total.patch` 将所有patch文件合并为一个 

************************

### am
> Apply a series of patches from a mailbox  

- git am patches/1.patch

- 如果是单纯的搬运 commit 使用 format-patch 创建 patch 然后 使用 am 应用的方式 比 diff  然后 apply 更好， 因为会保留原有commit信息

************************

### tag
> [Official Doc](https://git-scm.com/docs/git-tag/2.10.2)

- 查看所有标签 `git tag` 
    - `-l 'v1.0.*'` 列出v1.0.*
    - `git show tagname`　展示标签注释信息
- 新建一个标签并打上注释 `git tag -a v1.0.0 -m "初始版本"` 
    - 由指定的commit打标签  `git tag -a v1.2.4 commit-id` 
- 切换标签 `git checkout tagname` 和切换分支一样的，但是标签只是一个镜像，不能做提交
- 在某tag上新建一个分支 `git checkout -b branchname tagname`

- 删除本地标签 `git tag -d tagname` 
- 删除远程的tag 
    - `git push origin -d tag <tagname>` 
    - 如果本地已经删除了标签, 就可以 `git push origin :refs/tags/<tagname>`

### notes
> [doc](https://git-scm.com/docs/git-notes)

*******************

### reset
> git reset -h 
```
用法：git reset [--mixed | --soft | --hard | --merge | --keep] [-q] [<提交>]
  或：git reset [-q] [<树或提交>] [--] <路径>...
  或：git reset --patch [<树或提交>] [--] [<路径>...]

    -q, --quiet           安静模式，只报告错误
    --mixed               重置 HEAD 和索引
    --soft                只重置 HEAD
    --hard                重置 HEAD、索引和工作区
    --merge               重置 HEAD、索引和工作区
    --keep                重置 HEAD 但保存本地变更
    --recurse-submodules[=<reset>]  control recursive updating of submodules
    -p, --patch           交互式挑选数据块
    -N, --intent-to-add   将删除的路径标记为稍后添加
```

> [参考: 使用reset回滚代码](https://www.v2ex.com/t/296286)

#### 回滚add操作
- 当执行了 git add 命令, 将文件存入暂存区
- 可以使用 `git reset 文件` 将指定文件 或者 `git reset .` 当前目录(递归) 都取消暂存
- 文件内容没有改变, 这个用于选指定文件提交时

#### 回滚最近一次commit

1. `git reset --soft HEAD^` 撤销最近那次 commit 行为
1. 修改代码的内容
1. `git commit -c ORIG_HEAD` 使用撤销的那次 commit 的注释进行提交

> 注意 reset 操作会将老的HEAD会备份到文件 .git/ORIG_HEAD 中，命令中就是引用了这个老的相关信息
> -c 参数是复用指定节点的提交信息

#### 回滚最近几次的commit并添加到一个新建的分支上去
1. 新建分支 `git branch feature/new`
1. 删除master分支最近3次提交 `git reset --hard HEAD^3`
1. 切换到新分支上 `git checkout feature/new` 

> 相当于是将master上这三次的修改都转移到了这个分支上, master 从来没有过这三次提交一样
> 如果没有在 执行 reset --hard 之前新建分支的话, 这三次提交就永远删除了

> 注意: 这个操作在多人的协作中, reset --hard 比较危险, 可能引起别人分支的混乱

#### 回滚merge和pull操作
1. 执行了merge 或者 pull 操作后 
1. `git reset --hard ORIG_HEAD` 注意: 该命令会将 index 和 stage 的修改清空

#### 在index已有修改的状态回滚merge或者pull
1. `git pull`
1. `reset --merge ORIG_HEAD` 

> 使用 --hard 会直接回滚,直接丢失当前未提交的所有更改

#### 被中断的工作流程
> 在开发一个功能的时候, 突然有别的需求插进来了, 就可以通过 commit 一次, 然后回滚该次 commit 的方式  
> 将工作状态暂存, 且不会产生垃圾提交

**************************

### gc

`git gc -h`:
- `--aggressive` 默认使用较快速的方式检查文档库,并完成清理,当需要比较久的时间,偶尔使用即可
- `--prune[=<日期>]` 清除未引用的对
- `--auto` 启用自动垃圾回收模式
- `--force` 强制执行 gc 即使另外一个 gc 正在执行


************************

### clean

> Remove untracked files from the working tree `git clean --help`

`-n` 参数预览删除文件列表

************************

## 本地分支
> Git 的分支是轻量型的, 能够快速创建和销毁

************************

- 获取当前分支名 `git symbolic-ref --short -q HEAD`

- 拉取远程分支到本地并建立同名分支 
    - 拉取元数据 `git fetch --all` 
    - 建立和远程分支对应的本地分支 `git pull <远程主机名> <远程分支名>:<本地分支名>`

### show-branch 
> 按颜色列出分支上的提交和图示

### stash
> [Official Doc](https://git-scm.com/docs/git-stash)  

> 将当前修改缓存起来, 避免不必要的残缺提交 stash命令的缓存都是基于某个提交上的修改, 是一个栈的用法

> [参考: Git Stash的用法](http://www.cppblog.com/deercoder/archive/2011/11/13/160007.html)`底下的评论也很有价值, 值得思考`
> [参考: git-stash用法小结](https://www.cnblogs.com/tocy/p/git-stash-reference.html)

> git stash --help 查看完整的使用说明

`基本动作`
- push
    - save命令的进化版，该动作是缺省动作
- list
    - 输出大致为: `stash@{num}: On branchName : comment`
- save
    - save comment 已被废弃
- pop 
    - 将最近的stash 应用到当前仓库上, 原有的 stash 就丢弃了，如果pop缓存时发生了冲突 则不会丢弃对应的缓存
- apply 
    - 将指定的stash 应用到仓库上, 不丢弃原有的stash
- drop
    - 丢弃指定的stash, 如果想丢弃当前项目所有更改就可以将所有更改 save stash 然后 drop
- clear 
    - 清除所有 stash 
- branch 
    - 从创建缓存处创建新分支出来并pop 默认栈顶缓存，相比于pop和apply，这种方式更贴近缓存被创建时的场景

> push动作 实用参数
1. `--keep-index` `-k` stash 将不缓存 已经被add进index区的内容
1. `--include-untracked` 或 `-u` stash 将缓存未被track的文件
1. `--patch` 交互式选择哪些内容需stash缓存哪些进入index区

1. 如果需要恢复 `stash@{0}: On feature-test: test` 
    - 就在 feature-test 分支上建立新分支, 然后 apply stash@{0}
    - 不推荐用 pop, 当stash多了以后 人不一定都记得每个stash都改了啥, 可能会有冲突以及修改覆盖的问题
    - 最好用新分支装起来, 然后合并分支, 或者是 cherry-pick, 修改也不会丢失

> *注意* stash 是一个项目范围内的栈结构, 所以如果多个分支执行了stash, 那缓存都是共用的
> 要先确定好当前分支 stash 的 id (通过记录comment的方式会更好) 再 pop 或者 apply (不能无脑pop 血泪教训)  

- 使用该别名能展示当前分支的stash `alias wip='git stash list | grep $(git branch --show-current)' `

#### stash 创建 patch 
- 查看stash栈某下标(提交)的差异 `git stash show -p stash@{0}`
    - 简化别名 `alias gsh.st='__gshst(){ index=$1; if test -z $index; then index=0; fi; git stash show -p stash@{$index} }; __gshst'`
- 创建 patch `gsh.st > dev.patch`

#### 恢复被drop的stash
> [How to recover a dropped stash in Git?](https://stackoverflow.com/questions/89332/how-to-recover-a-dropped-stash-in-git)  

可以恢复 误操作 stash drop 或者 clean 的内容 

- `git fsck --no-reflog | awk '/dangling commit/ {print $3}'`
- WIP 开头的就是 stash 对应的 commit , 找到对应的 sha1 id 建立新分支即可
    - 也就是说 stash 仍然是采用 分支 来实现的, 在某个分支stash 就相当于在该分支进行 commit
    - 所以不是我一开始认为的是游离的数据, gc 会被清理

************************

### branch 
> 查看所有参数 `git branch --help`

- 列出所有分支(包含本地和远程) `-a --all`
- 按条件显示分支 `--list 'feature*'`
- 列出远程分支 `-r --remote`
- 查看分支详细信息 `-vv` 本地分支和远程分支的关联状态
- 查看包含指定 commit(可以多个) 的分支 `--contains [<commit>]` 
    - 对应的则是不包含 `--no-contains [<commit>]` commit 缺省为 HEAD(也就是最近的一次提交) 

- 创建分支 `git branch name` 并设置当前分支的对应远程分支 `-t <remote>/<branch>`
- 重命名分支 `-m old new` 对于远程来说就是先要删除再新建分支
- 删除分支 `-d 分支`
    - 如果该分支没有被完全合并, 就会提醒使用 `-D` 强制删除. 等价于 `--delete --force`

- 设置当前分支跟踪的远程分支 `--set-upstream-to=<remote>/<branch> <branch>`

### checkout
> [Official Doc: git checkout](https://git-scm.com/docs/git-checkout)

> alias gh='git checkout'

1. 切换分支 `gh feature/a`
1. 切换分支并设置该分支的远程分支 `gh feature/a origin/feature/a`

> 撤销文件修改
- `gh .` 取出最近的一次提交, 覆盖掉 work 区下当前目录(递归)下所有已更改(包括删除操作), 且未进入 stage 的内容, 已经进入 stage 区的文件内容则不受影响
    - `gh 文件1 文件2...` 同上, 但是只操作指定的文件

- `gh [commit-hash] 文件1 文件2...` 根据指定的 commit 对应hash值, 作如上操作, 但是区别在于 从 index 直接覆盖掉 stage 区, 并丢弃 work 区
    - `gh [commit-hash] .` **`如在项目根目录执行该命令, 会将当前项目的所有未提交修改全部丢失, 不可恢复!!!!`**

- `git checkout [commit-hash] 节点标识符或者标签 文件名 文件名 ...` 
    - 取出指定节点状态的某文件，而且执行完命令后，取出的那个状态会成为head状态，
    - 需要执行  `git reset HEAD` 来清除这种状态

### switch 
> switch branch 


### merge
- [官方文档](https://git-scm.com/docs/git-merge)

> [Official Doc: 高级合并](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%AB%98%E7%BA%A7%E5%90%88%E5%B9%B6)
> [参考: 解决 Git 冲突的 14 个建议和工具](http://blog.jobbole.com/97911/)

- `git merge develop `默认会直接将当前分支指向Develop分支。(一条拐弯的分支线)
- 推荐: `git merge --no-ff develop` 在当前分支`主动合并`分支Develop，在当前分支上生成一个新节点(有一个环的线)

1. merge 就是获取对方的修改, 与自己这一份进行合并(对 对方没有任何影响)
    - `master merge dev` 就是 master 下载 dev 的那一份代码, 与自己的这份代码合并为一份

- 如果遇到冲突：
    - `git mergetool` 使用工具进行分析冲突文件方便修改

> 配置mergetool工具kdiff3, 同类的还有meld：
- `git config --global merge.tool kdiff3`
- `git config --global mergetool.kdiff3.cmd "'D:/kdiff3.exe' \"\$BASE\" \"\$LOCAL\" \"\$REMOTE\" -o \"\$MERGED\""`
- `git config --global mergetool.prompt false`
- `git config --global mergetool.kdiff3.trustExitCode true`
- `git config --global mergetool.keepBackup false`

### rebase
> [Official Doc](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) 

> 衍和操作 [参考博客](http://blog.csdn.net/endlu/article/details/51605861) | 
> [Git rebase -i 交互变基](http://blog.csdn.net/zwlove5280/article/details/46649799) | 
> [git rebase的原理之多人合作分支管理](http://blog.csdn.net/zwlove5280/article/details/46708969)    
> 他会将分支中的圈, 消除掉, 成为线性结构

- 效果和merge差不多，但是分支图更清晰?TODO 有待详细学习
- 与master合并：`git merge master` 换成 `git rebase master`
- 当遇到冲突：
    - `git rebase --abort` 放弃rebase
    - `git rebase --continue` 修改好冲突后继续

> master 提交了 b,c  
> dev 提交了 d,e   

```
merge master: 

master: a - b - c 
             \   \
dev:          d - e

rebase master: 

master: a - b - c - d' - e'
```

merge 会保留分支图, rebase 会保持提交记录为单分支

### cherry-pick
> [Official Doc](https://git-scm.com/docs/git-cherry-pick)

- `git cherry-pick <commit-id>`

简单来讲, 就是将指定的某个提交(任意分支上的)上的修改, 重放到当前分支上  
和 stash pop 命令相比, 在重放上是一致的

> 用途
1. 可用于合并已有的若干个提交, 为了改动最小, 一般新建分支来做这件事
    - 例如 功能分支 `fea/something` 上的四个提交其实可以合并, 使得提交信息更清晰, 不冗余, 就可以从 `fea/something`
    - 创建处新建一个分支, 将该分支所有提交进行重放, 需要合并的那几个放一起重放 然后 将四个提交 reset, 再次提交即可

### bisect

- [git bisect 命令教程](http://www.ruanyifeng.com/blog/2018/12/git-bisect.html)
- [二分查找捉虫记](http://www.worldhello.net/2016/02/29/git-bisect-on-git.html)`通过分析提交历史查到哪次提交引起的Bug然后检出,修复`

### worktree 
> Manage multiple working trees [doc](https://git-scm.com/docs/git-worktree)

***************************

## 远程操作

> 大部分命令都是本地的, 所以执行效率很高, 但是协同开发肯定需要有同步的操作了

> 其实单独的两个主机也能完成同步, 两个IP之间要使用同一个仓库进行开发  
> 两个人互为对方的远程库(使用 git daemon 即可搭建简易服务端), 互为服务器即可完成(即使使用的是动态IP, 应该也不会受太大影响???)

- 指定本地开发分支和远程的绑定关系 `git branch --set-upstream dev origin/dev` 而且 一个本地库是能够绑定多个远程的

*****************

> Github上的fork

**合并对方最新代码**
> 1. 首先fork一个项目, 然后clone自己所属的该项目下来,假设 原作者为A 自己为B  
> 1. 添加原作者项目的URL 到该项目的远程分支列表中 `git add remote A A_URL`  
> 1. fetch作者的代码到本地 `git fetch A`  
> 1. 新建本地分支, 并与A的远程分支绑定 `git branch A A/master` 
> 1. 合并两个分支代码 `git merge --no-ff A/master`  
> 1. push即可  

************************

> Github上PR  

[Using git to prepare your PR to have a clean history](https://github.com/mockito/mockito/wiki/Using-git-to-prepare-your-PR-to-have-a-clean-history)

********************

### remote
> [Official Doc](https://git-scm.com/docs/git-remote)

1. **常用参数**
    - `add name URL地址` 添加远程关联仓库 不唯一，可以关联多个, 一般默认是origin
    - `set-url name URL地址` 修改关联仓库的URL
    - `rm URL` 删除和远程文档库的关系
    - `rename origin myth` 更改远程文档库的名称
    - `show origin` 查看远程分支的状态和信息

1. 显示本地仓库跟踪的那个远程仓库 `git ls-remote` 
1. 查看关联远程仓库的详情(push和pull的地址) `git remote -v` 

- [参考: 删除，重命名远程分支](http://zengrong.net/post/1746.htm)

### push
- _常用参数_
    - `-q` 控制台不输出任何信息
    - `-f` 强制推送提交 **使用这个参数时要再三考虑清楚**
    - `--all` 推送所有分支
    - `-u` upstream 设置 git pull/status 的上游
        - `git push origin master`和`git push -u origin master` 区别在于 前者是使用该远程和分支进行推送
        - 后者也是推送, 并设置origin为默认推送的远程, 以后push就不用注明远程名了(多远程的情况下要注意)
    - `-d --delete` 删除引用(分支或标签)

- 删除远程分支 
    - `git push origin -d 分支名称`
    - 如果本地已经删除了该分支，就可以`git push origin :分支名称`

- 第一次将本地分支与远程建立关系
    - `git push -u origin master ` | `git push --set-uptream master` | `git push -all` (会将所有分支一起push)

- 提交指定tag `git push origin tagname`
    - 提交所有tag `git push --tags`

- 出现 `RPC failed; result=22, HTTP code = 411` 的错误
    - 就是因为一次提交的文件太大，需要改大缓冲区 例如改成500m  `git config http.postBuffer 524288000`

### fetch
> 访问远程仓库, 拉取本地没有的远程数据 

- 注意 fetch 是一个分支一个分支进行拉取的, 在此基础上可以优化网络不稳定时clone代码的问题 
    - 关键是分支之间独立拉取不会像clone拉取所有分支，有分支拉取失败就要从头再来
    - 操作过程: 创建空目录并进入， `git init` 然后 `git fetch URL`
    - 创建 msater分支 `git checkout -b master FETCH_HEAD`
    - 拉取其他分支 `git fetch --all`

- 拉取本地没有的分支（两种方式）
    1. **推荐** 拉取 origin 信息 `git fetch --all` 由远程分支创建新分支并设定跟踪 `git checkout -b dev origin/dev`
    1. 拉取 origin 的 dev 分支 并在本地创建 dev 分支 `git fetch origin dev:dev`
        - 但此时本地的分支并没有 track 远程分支，需要执行 `git push -u origin dev` 进行设置
- 删除远程没有但本地有的那些分支 `git fetch -p`

- `git fetch origin dev-test` 下拉指定远程的指定分支 至 origin/dev-test 但不会创建本地分支

> fetch 不到所有远程分支的原因和解决方案
- 查看fetch的源 `git config --get remote.origin.fetch`
- 需要配置为通配方式 `git config --add remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"`

### pull
> 不仅仅是 fetch 代码, 还会进行 merge 操作, 所以安全起见, 是先 fetch 然后再手动 merge

- `git pull origin dev` 下拉指定远程的指定分支
- `git pull --all` 下拉默认远程的所有分支代码并自动合并

************************

## Submodule
> [Official Doc](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

> [git submodule的使用](https://blog.csdn.net/wangjia55/article/details/24400501)
> [参考: Git Submodule使用完整教程](http://www.kafeitu.me/git/2012/03/27/git-submodule.html)

- 能够在一个git仓库中将一个文件夹作为一些独立的子仓库进行管理
- 添加子模块 `git submodule add url dir` 目录为可选项

当主仓库 clone 时 只会将子模块作为空目录克隆下来
- 读取 .gitmodules 文件完成子模块的注册 `git submodule init`
- 拉取子模块代码 `git submodule update`

以上两条命令等价于 `git submodule update --init --recursive`

`删除子模块`
1. 删除.gitsubmodule里相关部分
1. 删除.git/config 文件里相关字段
1. 删除子仓库目录

***************

## 其他
### gitk
> 图形化展示分支 需要依赖 tcl tk 

### grep  
- 搜索文字 `git grep docker`
    - `-n`搜索并显示行号 
    - `--name-only` 只显示文件名，不显示内容
    - `-c` 查看每个文件里有多少行匹配内容(line matches):
    - 查找git仓库里某个特定版本里的内容, 在命令行末尾加上标签名(tag reference):  `git grep xmmap v1.5.0`
    - `git grep --all-match -e '#define' -e SORT_DIRENT` 匹配两个字符串
    
### archive
1. 将某版本打包成压缩包 `git archive -v --format=zip v0.1 > v0.1.zip`

### reflog
- 查看仓库的本地操作日志 仅记录HEAD以及所有分支引用所指向的历史 

1. `git reflog` 显示commit操作详情，仅本地保存

### rev-parse 
> 该工具是Git内部命令 往往被其他子命令使用

1. 查看分支指向具体的commit id `git rev-parse fea/new`

************************

# 配置文件
## .gitignore
> [Github: gitignore](https://github.com/github/gitignore) | 一行是一个配置, 是独占一行的

- 使用 `#` 注释一行
- `test.txt`  忽略该文件
- `*.html`  忽略所有HTML后缀文件
- `*[o/a]`  忽略所有o和a后缀的文件
- `!foo.html`  不忽略该文件

```conf
    */ #忽略所有文件
    build/ #所有build目录
    /build #只忽略当前目录的build, 子目录的不忽略
    *.iml #所有iml文件
    ?.log #忽略所有 后缀为log, 文件名字只有一个字母
    !*.java #不忽略所有java文件
    a.[abc] #忽略 后缀为 a或者b或者c 的文件
    doc/*.txt #忽略 doc一级子目录的txt文件, 不忽略多级子目录中txt
```

## gitattributes
> [gitattributes](http://schacon.github.io/git/gitattributes.html)

1. 配置文件的换行符 eol
1. working-tree-encoding
1. ident
1. filter
1. merge
1. whitespace
1. export-ignore
1. delta 
1. encoding

************************

# 自定义插件
> [how-to-create-git-plugin](https://adamcod.es/2013/07/12/how-to-create-git-plugin.html)
