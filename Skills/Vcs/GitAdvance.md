---
title: Git深入学习
date: 2018-11-21 10:56:52
tags: 
    - Advanced
categories: 
    - Git
---

**目录 start**
 
1. [Git Advance](#git-advance)
    1. [版本控制系统(VCS)](#版本控制系统vcs)
    1. [Tips](#tips)
        1. [清理仓库大文件](#清理仓库大文件)
            1. [gc](#gc)
        1. [CRLF与LF](#crlf与lf)

**目录 end**|_2019-01-17 15:13_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Git Advance

## 版本控制系统(VCS)
- [码农翻身:小李的版本管理系统](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513204&idx=1&sn=c4c493d771a167a84ace01c3e016417e&scene=21#wechat_redirect)

*********************

## Tips
- `git ls-files` 列出文件列表
    - `git ls-files | xargs wc -l` 计算文件中程序代码行数 通过工具：`xargs` `wc` (中文命名的文件编码问题无法计算行数)
    - `git ls-files | xargs cat | wc -l` 计算行数总和

- [git bisect 命令教程](http://www.ruanyifeng.com/blog/2018/12/git-bisect.html)
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

### CRLF与LF
> 由于系统的不同 Windows是 CRLF *nix 是 LF Mac 是 CR | [wiki: CRLF](https://en.wikipedia.org/wiki/Newline)  

```sh
    git config --global core.autocrlf false 
    git config --global core.safecrlf true
```
> [参考博客: CRLF和LF](https://www.tuicool.com/articles/IJjQVb)
> [参考博客: git 换行符LF与CRLF转换问题](https://www.cnblogs.com/sdgf/p/6237847.html)

>1. CRLF -> LF `sed -i 's/\r//g' file` 配合git 就是 `git ls-files| sed -i 's/\r//g' `

- [ ] cherry pick 

