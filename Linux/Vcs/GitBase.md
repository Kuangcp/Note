`目录 start`
 
- [Git基础](#git基础)
    - [版本控制系统(VCS)](#版本控制系统vcs)
    - [Git常用命令](#git常用命令)
        - [Tips](#tips)
        - [清理仓库](#清理仓库)
            - [gc](#gc)
        - [fork相关操作](#fork相关操作)
        - [仓库基本命令](#仓库基本命令)
            - [config](#config)
            - [status](#status)
            - [rm](#rm)
            - [commit](#commit)
                - [提交行为准则](#提交行为准则)
            - [remote](#remote)
            - [submodule](#submodule)
            - [show](#show)
            - [push](#push)
            - [log](#log)
                - [对比两个分支的差异](#对比两个分支的差异)
            - [diff](#diff)
            - [tag](#tag)
        - [分支操作](#分支操作)
            - [开发流程的常用分支操作](#开发流程的常用分支操作)
            - [clone](#clone)
            - [branch](#branch)
            - [checkout](#checkout)
            - [fetch](#fetch)
            - [pull](#pull)
            - [merge](#merge)
            - [rebase](#rebase)
            - [grep](#grep)
        - [常用文件](#常用文件)
            - [.gitignore](#gitignore)
- [注释](#注释)
            - [gitattributes](#gitattributes)
        - [Tools](#tools)
            - [git-svn](#git-svn)
            - [Submodules](#submodules)
    - [各个VCS工具的区别以及优缺点](#各个vcs工具的区别以及优缺点)
        - [Git](#git)
        - [SVN](#svn)
    - [repos的使用](#repos的使用)

`目录 end` |_2018-09-14_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Git基础
> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. --[git-scm.com](https://git-scm.com/)

> [Github:git](https://github.com/git/git)  
> [official doc: git](https://git-scm.com/docs) 
> [Git官网中文教程](https://git-scm.com/book/zh/v2) | [对应的仓库](https://github.com/progit/progit2)  

***************************
## 版本控制系统(VCS)
- [码农翻身:小李的版本管理系统](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513204&idx=1&sn=c4c493d771a167a84ace01c3e016417e&scene=21#wechat_redirect)

**********************
## Git常用命令
> [git-tips](https://github.com/521xueweihan/git-tips)`学习Git的仓库`  
> [git权威指南的组织](https://github.com/gotgit)`完整书籍,以及相关测试题`

> [使用原理视角看 Git](https://coding.net/help/doc/practice/git-principle.html)
> [如何高效地使用 Git](https://zhuanlan.zhihu.com/p/30561653)

> [参考博客: 重看”Linus Torvalds on Git”视频](http://www.techug.com/post/review-of-linus-torvalds-on-git.html)
> [GUI客户端](https://git-scm.com/downloads/guisQ)

- [tig](http://jonas.nitro.dk/tig/manual.html) `tig命令，git的加强版`
### Tips
- `git ls-files` 列出文件列表
    - `git ls-files | xargs wc -l` 计算文件中程序代码行数 通过工具：`xargs` `wc` (中文命名的文件编码问题无法计算行数)
    - `git ls-files | xargs cat | wc -l` 计算行数总和
- [二分查找捉虫记](http://www.worldhello.net/2016/02/29/git-bisect-on-git.html)`通过分析提交历史查到哪次提交引起的Bug然后检出,修复`

- [API: github开发接口](https://developer.github.com/v3/)

### 清理仓库
> [bfg-cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

> [参考博客1 彻底删除](http://www.itwendao.com/article/detail/413282.html) | 
> [参考博客2 彻底删除](http://blog.csdn.net/meteor1113/article/details/4407209) | 
> [参考博客3 删除大文件](http://www.gzhphb.com/article/78/784131.html)  
> [参考博客4 减小磁盘占用](http://zhongmingmao.me/2017/04/19/git-reduce/)  
> [删除仓库的某个时间点之前的历史记录，减少.git 目录大小](https://www.v2ex.com/t/297802)  
> [如何清洗 Git Repo 代码仓库](http://www.open-open.com/lib/view/open1414632626075.html)  
- 因为删除的文件是会留在仓库，为了以后恢复用，但是这样的话仓库就会越来越大了
- `强制删除`，并且从git索引中也去掉，相当于彻底删除 
    - `git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch 文件的路径' --prune-empty --tag-name-filter cat -- --all`
    - `git push origin --force --all`
    - `git push origin --force --tags`
    - 使用`git rebase`来更新分支，而不是 `git merge` 不然文件又回来了

- 然而这个笔记仓库，之前将图片文件也放在了仓库里，删除之前也改动了名字，现在根本找不到文件了,如果要减小仓库大小只能重建了
    - 猜测他的文件都在 `.git/objects/pack/` 里留有备份
    - 最简单的减小传输的大小的是clone时加上 `--depth 1` 对之前的分支延迟下载

#### gc
> 只能压缩一部分空间
`git gc -h`:
- `--aggressive` 默认使用较快速的方式检查文档库,并完成清理,当需要比较久的时间,偶尔使用即可
- `--prune[=<日期>]` 清除未引用的对
- `--auto` 启用自动垃圾回收模式
- `--force` 强制执行 gc 即使另外一个 gc 正在执行

### fork相关操作
- fork之后，想要更新原作者的分支：`git remote add 名称 原作者URL`
- 拉取更新 ：`git fetch 名称`
> 在合并别人仓库源码时,相当于两个不同源的分支之间的合并操作

***************
### 仓库基本命令
> 如果没有一个Github 码云这样的平台, 而只是单独的两个点, 两个用户或者IP之间要使用同一个仓库进行开发  
> 两个人互为对方的远程库, 互为服务器即可完成, 即使使用的是动态IP, 应该也不会受太大影响  
> 使用 `git help 加上命令`, 就能看到命令对应的文档

#### config
- `git config user.email ***`  和   `git config user.name ***` 这两个是必须的，
    - 如果想统一配置不想每个仓库单独配置就 `git config --global user.name` email同理
- `git config http.postBuffer 524288000` 设置缓存区大小为 500m
- `git config core.fileMode false` 忽略文件的mode变化，一般发生在文件的复制粘贴之后（跨系统?）

#### status
- `-s --short` 简化输出
    - ?? 表示新添加未跟踪
    - A 新添加到暂存区
    - M 修改过的文件
    - MM 修改了但是没有暂存

#### rm
- 删除文件 `git rm 文件`
- 从git仓库中删除文件, 但是文件系统中保留文件 `git rm --cached 文件`
    - 如果仅仅是想从仓库中剔除, 那么执行完命令还要在 `.gitignore` 文件中注明, 不然又add回去了

#### commit
- [官方文档](https://git-scm.com/docs/git-commit)
- `git commit -am "init" `: a git库已有文件的修改进行添加, m 注释
    - `git add * ` 如果有新建立文件就要add 再之后commit就不要a参数了 `git commit -m ""`
    - 如果只是修改文件没有新建 `git commit -am ""`
- `git commit ` 会自动进入VI编辑器
    - 第一行：用一行文字简述提交的更改内容
    - 第二行：空行
    - 第三行：记述更改的原因和详细内容
    - 使用下面方法关闭退出

##### 提交行为准则
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

#### remote
> [官方文档](https://git-scm.com/docs/git-remote)

1. **常用参数**
    - `add name URL地址` 添加远程关联仓库 不唯一，可以关联多个, 一般默认是origin
    - `set-url name URL地址` 修改关联仓库的URL
    - `rm URL` 删除和远程文档库的关系
    - `rename origin myth` 更改远程文档库的名称
    - `show origin` 查看远程分支的状态和信息

1. 删除远程库某分支`git push 远程名称 --delete 分支名称` 
1. `git ls-remote` 显示本地仓库跟踪的那个远程仓库
1. `git remote -v` 查看关联远程仓库的详情(push和pull的地址)

- [删除，重命名远程分支](http://zengrong.net/post/1746.htm)

#### submodule
> 子模块

- [ ] 完成

#### show
> 展示提交信息

- 显示当前提交的差异 `git show HEAD` HEAD替换成commit的sha值就是显示指定提交的修改
- `git show -h` 查看更多

#### push
- _常用参数_
    - `-h` 查看所有参数和说明
    - `-q` 控制台不输出任何信息
    - `-f` 强制 **使用这个参数时要再三考虑清楚**
    - `--all` 推送所有引用
    - `-u` upstream 设置 git pull/status 的上游
        - `git push origin master`和`git push -u origin master` 区别在于 前者是使用该远程和分支进行推送
        - 后者也是推送, 并设置origin为默认推送的远程, 以后push就不用注明远程名了(多远程的情况下要注意)
    - `-d` 删除引用
    - `--tags` 推送标签（不能使用 --all or --mirror）

- 出现 `RPC failed; result=22, HTTP code = 411` 的错误
    - 就是因为一次提交的文件太大，需要改大缓冲区 
    - > 例如改成500m  `git config http.postBuffer 524288000`

- 提交本地所有分支 `git push --all` pull时同理
- 删除远程分支 `git push 远程名称 --delete 分支名称`

- _第一次与远程建立连接_
    - `git push -u origin master ` | `git push --set-uptream master` | `git push -all` 
    - 这几个都是可以的,最后那个简单, 还能将别的分支一起推上去

#### log
> 更多说明 查看 `git help log` | [官网文档](https://www.git-scm.com/docs/git-log)

- `-p` 显示每次提交的内容差异 `git log -p -2` 仅显示最近两次提交的差异
- `--stat` 查看提交对仓库修改的总览
- `---pretty=[online/short/full/fuller/format]` 使用预定义格式显示
    - format 是可以自定义格式和占位符
- `--graph` 图形的样子显示分支图

- `git log --author='A' `输出所有A开头的作者日志
- `git log 文件名 文件名` 输出更改指定文件的所有commit 要文件在当前路径才可
- `git log --after='2016-03-23 9:20' --before='2017-05-10 12:00' ` 输出指定日期的日志

- `git shortlog` 按字母顺序输出每个人的日志 
    - `--numbered` 按提交数排序
    - `-s` 只显示每个提交者以及提交数量

**彩色输出**
```sh
alias glogc="git log --graph --pretty=format:'%Cred%h%Creset %Cgreen%ad%Creset | %C(bold cyan)<%an>%Creset %C(yellow)%d%Creset %s ' --abbrev-commit --date=short" # 彩色输出
alias gloga='git log --oneline --decorate --graph --all' # 简短彩色输出
alias glo='git log --oneline --decorate' # 最简单
alias glol='git log --graph --pretty='\''%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'
alias glola='git log --graph --pretty='\''%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'' --all'
```
##### 对比两个分支的差异
> [参考博客](http://blog.csdn.net/u011240877/article/details/52586664)

- 查看 dev 有，而 master 中没有的 `git log dev ^master` 反之 `git log master ^dev`
- 查看 dev 中比 master 中多提交了哪些内容：`git log master..dev`
- 不知道谁提交的多谁提交的少，单纯想知道有什么不一样：`git log dev...master`
- 在上述情况下，再显示出每个提交是在哪个分支上:`git log --left-right dev...master`
    - 注意 commit 后面的箭头，根据我们在 –left-right dev…master 的顺序，左箭头 < 表示是 dev 的，右箭头 > 表示是 master的。

#### diff
- `--cached` 查看已暂存起来的变化 等同于`--staged`
```
    git diff [options] [<commit>] [--] [<path>...]
    git diff [options] --cached [<commit>] [--] [<path>...]
    git diff [options] <commit> <commit> [--] [<path>...]
    git diff [options] <blob> <blob>
    git diff [options] [--no-index] [--] <path> <path>
```

> [Github:diff-so-fancy](https://github.com/so-fancy/diff-so-fancy)`一个更方便查看diff的工具`
- 最简单的就是 `npm install -g diff-so-fancy` 安装 

#### tag
> [官方文档](https://git-scm.com/docs/git-tag/2.10.2)

- 查看所有标签 `git tag` 
    - `-l 'v1.0.*'` 列出v1.0.*
    - 展示标签注释信息 `git show tagname`
- 新建一个标签并打上注释 `git tag -a v1.0.0 -m "初始版本"` 
    - 由指定的commit打标签  `git tag -a v1.2.4 commit-id` 
- 切换标签 `git checkout tagname` 和切换分支一样的，但是标签只是一个镜像，不能修改
- 如果要在某tag上新建一个分支， `git checkout -b branchname tagname`
- 提交指定的tag `git push origin tagname` （默认不会自动提交标签）
    - 提交所有的tag `git push --tags` 

- 删除本地标签 `git tag -d tagname` 
- 删除远程的tag `git push origin --delete tag <tagname>` 

******
### 分支操作
> [stash的争论](http://www.cppblog.com/deercoder/archive/2011/11/13/160007.html)

#### 开发流程的常用分支操作
- 一般的开发过程中会使用到三种临时分支（用完就删）和两个主分支 master develop
    - 功能分支 `feature-*` 
    - 预发布分支 `release`
    - 修复bug `fixbug`

*******
- `git checkout -b feature-x develop` 从develop的分支生成一个功能分支，并切换过去
- 完成功能后：`git checkout develop `
    - 合并： `git merge --no-ff feature-x`
    - 删除： `git branch -d feature-x`

*****
- `git checkout -b release-1.2 develop` 新建一个预发布分支
    - `git checkout master` 确认没有问题后 `git merge --no-ff release-1.2` 合并到master分支
    - `git tag -a 1.2` 打标签，这就是github上软件的版本控制
    - 没有问题后 合并到develop分支`git checkout develop` `git merge --no-ff release-1.2`
    - 删除预发布分支 `git branch -d release-1.2`

*****
- `git checkout -b fixbug-0.1 master` 新建修复bug的分支 
- `git checkout master ``git merge --no-ff fixbug-0.1 ``git tag -a 0.1.1` 修补结束后合并到master分支
- `git checkout develop` `　git merge --no-ff fixbug-0.1` 再合并到develop分支
- 删除分支 `git branch -d fixbug-0.1` 
- 删除远程没有本地有的分支`git fetch -p`

#### clone
- `git clone branchname URL` 克隆指定分支
- `git clone URL 目录` 克隆下来后更名为指定目录
- `git clone --depth 1 URL` 只克隆最近一次提交的历史, 能大大减小拉取的大小, 但是如果要用到之前的提交历史就还是要下拉下来的 类似于懒加载
    - 但是在新建一个远程仓库后, 推送时会报错:`shallow update not allowed` 因为本地库是残缺的
    - 所以需要新建一个目录, 把原仓库全拉下来, 再添加远程进行推送, 然后删除该目录, 残缺版的仓库也能正常向新远程推送提交了

> 克隆在指定tag状态的仓库 `git clone URL --branch=name ` 然后 Git会提示 
```
您正处于分离头指针状态。您可以查看、做试验性的修改及提交，并且您可以通过另外
的检出分支操作丢弃在这个状态下所做的任何提交。
如果您想要通过创建分支来保留在此状态下所做的提交，您可以通过在检出命令添加
参数 -b 来实现（现在或稍后）。例如：
  git checkout -b <new-branch-name>
```
按他提示来就行了 

#### branch 
- 列出远程分支 `git branch -r`
- 创建分支 `git branch name`

#### checkout
> [官方文档 : git checkout](https://git-scm.com/docs/git-checkout)

- `git checkout 文件名 文件名` git会在索引中找文件，有就取出，没有就从最新的commit回找，取出第一个找到的版本，
    - 每个文件都是这样，也就是说如果有被删除的文件，是可以通过此来找回的
    - `git checkout . `取出文档库中所有文件的最新版本
- `git checkout commit 节点标识符或者标签 文件名 文件名。。。` 
    - 取出指定节点状态的某文件，而且执行完命令后，取出的那个状态会成为head状态，
    - 需要执行  `git reset HEAD` 来清除这种状态

> 撤销当前对文件的所有修改 `git checkout -- 文件名` 就会使用上次提交的文件来覆盖当前文件

- [ ] 有没有 svn cat 类似的功能


#### fetch
> 访问远程仓库, 拉取本地没有的数据
- `git fetch origin dev-test` 下拉指定远程的指定分支到本地, 本地没有就会自动新建
- `git fetch --all` 下拉默认远程的所有分支的代码

#### pull
> 不仅仅是下拉代码, 还会进行merge合并, 所以安全起见, 是先fetch然后再进行合并操作  
- `git pull origin dev` 下拉指定远程的指定分支
- `git pull --all` 下拉默认远程的所有分支代码并自动合并


#### merge
- [官方文档](https://git-scm.com/docs/git-merge)

> [Official Doc: 高级合并](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%AB%98%E7%BA%A7%E5%90%88%E5%B9%B6)
> [参考博客: 解决 Git 冲突的 14 个建议和工具](http://blog.jobbole.com/97911/)

- `git merge develop `默认会直接将当前分支指向Develop分支。(一条拐弯的分支线)
- 推荐: `git merge --no-ff develop` 在当前分支`主动合并`分支Develop，在当前分支上生成一个新节点(有一个环的线)

1. merge 就是获取对方的修改, 与自己这一份进行合并(对 对方没有任何影响)
    - `master merge dev` 就是 master 下载 dev 的那一份代码, 与自己的这份代码合并为一份

- 如果遇到冲突：
    - `git mergetool` 使用工具进行分析冲突文件方便修改

> 配置mergetool工具：
- `git config --global merge.tool kdiff3`
- `git config --global mergetool.kdiff3.cmd "'D:/kdiff3.exe' \"\$BASE\" \"\$LOCAL\" \"\$REMOTE\" -o \"\$MERGED\""`
- `git config --global mergetool.prompt false`
- `git config --global mergetool.kdiff3.trustExitCode true`
- `git config --global mergetool.keepBackup false`

#### rebase
> 衍和操作 [参考博客](http://blog.csdn.net/endlu/article/details/51605861) | 
> [Git rebase -i 交互变基](http://blog.csdn.net/zwlove5280/article/details/46649799) | 
> [git rebase的原理之多人合作分支管理](http://blog.csdn.net/zwlove5280/article/details/46708969)    
> 他会将分支中的圈, 消除掉, 成为线性结构

- 效果和merge差不多，但是分支图更清晰?TODO 有待详细学习
- 与master合并：`git merge master` 换成 `git rebase master`
- 当遇到冲突：
    - `git rebase --abort` 放弃rebase
    - `git rebase --continue` 修改好冲突后继续

#### grep  
- 搜索文字 `git grep docker`
    - `-n`搜索并显示行号 
    - `--name-only` 只显示文件名，不显示内容
    - `-c` 查看每个文件里有多少行匹配内容(line matches):
    - 查找git仓库里某个特定版本里的内容, 在命令行末尾加上标签名(tag reference):  `git grep xmmap v1.5.0`
    - `git grep --all-match -e '#define' -e SORT_DIRENT` 匹配两个字符串
    
*************
### 常用文件
#### .gitignore
```
# 注释
*/ 忽略所有文件
build/ 所有build目录
/build 只忽略当前目录的build, 子目录的不忽略
*.iml 所有iml文件
?.log 忽略所有 后缀为log, 文件名字只有一个字母
!*.java 不忽略所有java文件
a.[abc] 忽略 后缀为 a或者b或者c 的文件
doc/*.txt 忽略 doc一级子目录的txt文件, 不忽略多级子目录中txt

```

#### gitattributes
> [gitattributes](http://schacon.github.io/git/gitattributes.html)

*****************
### Tools

#### git-svn
> [git-svn 文档](https://git-scm.com/docs/git-svn)

#### Submodules
> [官方文档](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
> [git submodule的使用](https://blog.csdn.net/wangjia55/article/details/24400501)

- 能够在一个git仓库中将一个文件夹作为一些独立的子仓库进行管理

***************************************************
## 各个VCS工具的区别以及优缺点

### Git
> 分布式的去中心化的, 个人也是习惯性用Git了

### SVN
> [Svn笔记](/Linux/Svn.md)

1. 中心化的, 代码统一保存, 如果中心发生错误, 代码会全部毁掉, 提交是必须要和服务端通信才能完成
2. 允许部分的进行修改, 下拉, 提交. 而对于Git来说一个仓库就是一个整体(Git submodule 目前也能完成, 但是还是没有SVN灵活)
3. 优点: 能够精确控制每个目录的每个人的访问权限

可以通过 git-svn 使用Git的命令与SVN服务器进行交互
> [Official doc: git-svn](https://git-scm.com/docs/git-svn)

> 但是个人目前在用的方式是直接 git 和 svn 一起用  
> [参考博客: 为啥要同时用 SVN 和 Git 管理项目](https://www.cnblogs.com/dasusu/p/7774469.html)

1. IDEA中移除git相关插件, 防止混乱, 而且最好是先把SVN项目拉下来,
    - 达到 先让IDEA使用SVN管理项目 的目的 然后 git init 
1. 避免LRLF LF 问题
```sh
    git config --global core.autocrlf false
    git config --global core.safecrlf false
```
1. 互相忽略各自配置目录 .svn .git

- 至此, 就能和团队保持一致的使用SVN, 然后自己多任务开发时, 又能使用git优秀的分支模型
- 当然该场景是有限的, 也就是说只有你一个人在用git 而且团队中使用SVN时没有使用SVN的分支模型, 这个是没有问题的
    - 如果SVN也用了分支, 那么就要命了, 这么多分支和状态, 要靠大脑记住实时的状态就....

## repos的使用
> 综合各个VCS的管理方式
