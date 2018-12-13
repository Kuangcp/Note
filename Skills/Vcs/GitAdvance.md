---
title: GitAdvance.md
date: 
tags: 
categories: 
---

**目录 start**
 
1. [Git Advance](#git-advance)
    1. [版本控制系统(VCS)](#版本控制系统vcs)
    1. [Tips](#tips)
        1. [清理仓库大文件](#清理仓库大文件)
            1. [gc](#gc)
    1. [提交行为准则](#提交行为准则)

**目录 end**|_2018-12-13 12:06_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Git Advance

## 版本控制系统(VCS)
- [码农翻身:小李的版本管理系统](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513204&idx=1&sn=c4c493d771a167a84ace01c3e016417e&scene=21#wechat_redirect)

*********************

## Tips
- `git ls-files` 列出文件列表
    - `git ls-files | xargs wc -l` 计算文件中程序代码行数 通过工具：`xargs` `wc` (中文命名的文件编码问题无法计算行数)
    - `git ls-files | xargs cat | wc -l` 计算行数总和
- [二分查找捉虫记](http://www.worldhello.net/2016/02/29/git-bisect-on-git.html)`通过分析提交历史查到哪次提交引起的Bug然后检出,修复`

- [API: github开发接口](https://developer.github.com/v3/)

### 清理仓库大文件
- [official:7.6 Git 工具 - 重写历史](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E5%86%99%E5%8E%86%E5%8F%B2)

> [Tool: bfg-cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

> [参考博客 从git中永久删除文件以节省空间](http://blog.csdn.net/meteor1113/article/details/4407209) | 
> [参考博客4 减小磁盘占用](http://zhongmingmao.me/2017/04/19/git-reduce/)  
> [删除仓库的某个时间点之前的历史记录，减少.git 目录大小](https://www.v2ex.com/t/297802)  
> [如何清洗 Git Repo 代码仓库](http://www.open-open.com/lib/view/open1414632626075.html)  

> [参考博客: 寻找并删除Git记录中的大文件](https://www.tuicool.com/articles/vAVVZrA)
1. 找出大文件 `git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10 | awk '{print$1}')"`
1. 删除文件, 重写提交 `git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch 文件的路径' --prune-empty --tag-name-filter cat -- --all`
1. 强制推送 `git push origin --force --all`
    - `git push origin --force --tags`
1. 使用`git pull rebase`来更新分支，而不是 `git merge` 不然大文件又从别的分支回来了

> 要注意, 所有的分支都必须pull rebase , 只要还有一个人留有对大文件的引用, 大文件就一直在仓库

#### gc
> 只能压缩一部分空间
`git gc -h`:
- `--aggressive` 默认使用较快速的方式检查文档库,并完成清理,当需要比较久的时间,偶尔使用即可
- `--prune[=<日期>]` 清除未引用的对
- `--auto` 启用自动垃圾回收模式
- `--force` 强制执行 gc 即使另外一个 gc 正在执行

## 提交行为准则
> [参考博客: SVN提交更新的一个准则](http://www.cnblogs.com/chenlong828/archive/2008/09/22/1296193.html)
1. 提交之前先更新
    - SVN更新的原则是要随时更新，随时提交。当完成了一个小功能，能够通过编译并且并且自己测试之后，谨慎地提交。
    - 如果提交过程中产生了冲突，则需要同之前的开发人员联系，两个人一起协商解决冲突，解决冲突之后，需要两人一起测试保证解决冲突之后，程序不会影响其他功能。
    - 如果提交过程中产生了更新，则也是需要重新编译并且完成自己的一些必要测试，再进行提交。
1. 保持原子性的提交
    - 每次提交的间歇尽可能地短，以一个小时，两个小时的开发工作为宜。如在更改UI界面的时候，可以每完成一个UI界面的修改或者设计，就提交一次。在开发功能模块的时候，可以每完成一个小细节功能的测试，就提交一次，在修改bug的时候，每修改掉一个bug并且确认修改了这个bug，也就提交一次。我们提倡多提交，也就能多为代码添加上保险。
1. 提交时注意不要提交本地自动生成的文件
    - 对于Java来说, IDE自身配置文件, 和字节码文件是无需提交的 例如 .idea目录 iml文件 
1. 不要提交不能通过编译的代码
    - 代码在提交之前，首先要确认自己能够在本地编译。如果在代码中使用了第三方类库，要考虑到项目组成员中有些成员可能没有安装相应的第三方类库，项目经理在准备项目工作区域的时候，需要考虑到这样的情况，确保开发小组成员在签出代码之后能够在统一的环境中进行编译。
1. 不要提交自己不明白的代码
    - 提交之后, 你的代码将被项目成员所分享。如果提交了你不明白的代码，你看不懂，别人也看不懂，如果在以后出现了问题将会成为项目质量的隐患。因此在引入任何第三方代码之前，确保你对这个代码有一个很清晰的了解。
1. 提前协调好项目组成员的工作计划
    - 在自己准备开始进行某项功能的修改之前，先给工作小组的成员谈谈自己的修改计划，让大家都能了解你的思想，了解你即将对软件作出的修改，这样能尽可能的减少在开发过程中可能出现的冲突，提高开发效率。同时你也能够在和成员的交流中发现自己之前设计的不足，完善你的设计。
1. 对提交的信息采用明晰的标注
    - +) 表示增加了功能
    - *) 表示对某些功能进行了更改
    - -) 表示删除了文件，或者对某些功能进行了裁剪，删除，屏蔽。
    - b) 表示修正了具体的某个bug

- [ ] cherry pick 

