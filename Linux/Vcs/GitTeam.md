`目录 start`
 
- [基于Git进行团队开发](#基于git进行团队开发)
    - [基础思想](#基础思想)
        - [Git Flow](#git-flow)
        - [本地和远程](#本地和远程)
        - [模板化提交信息](#模板化提交信息)
    - [小规模团队使用码云组织的总结](#小规模团队使用码云组织的总结)
        - [最终方案](#最终方案)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************

# 基于Git进行团队开发
> [在阿里，我们如何管理代码分支？](https://blog.csdn.net/maoreyou/article/details/79877829)

- [ ] 整理和学习这几种管理方式

> Github gitee gitlab bitbucket 等各大平台都是这样一种模式:   
> 个人和个人开发者之间是并行master，只适合偶尔开发提交一些代码  
> 组织就是适合给多个人，等同的稳定开发时，分支就会比较明确，这个笔记就是记录组织中git的使用

## 基础思想
### Git Flow
> [Vincent Driessen 提出了 A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/)

- [依据以上思想开发的 git flow工具](https://github.com/nvie/gitflow)
    - [介绍 Git Flow](https://datasift.github.io/gitflow/IntroducingGitFlow.html)
- [参考博客:  Git 在团队中的最佳实践--如何正确使用Git Flow](http://www.cnblogs.com/cnblogsfans/p/5075073.html)
    - [参考博客: Getting Started – Git-Flow](https://yakiloo.com/getting-started-git-flow/)

`规范的分支图`
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

### 本地和远程
- 指定本地开发分支和远程的绑定关系 `git branch --set-upstream dev origin/dev` master同理
    - 一个本地库是能够绑定多个远程的

- [分支图复杂的一个项目](https://github.com/Netflix/eureka/network) `只是演示分支的复杂度`


### 模板化提交信息
> git commit message 的模板化

1. 新建 ~/.gitmessage 文件
2. ~/.gitconfig 中添加
```
[commit]
template = ~/.gitmessage
```

> 那么效果就是 git commit 不指定-m 参数就会调用该模板显示
*******************
## 小规模团队使用码云组织的总结
> `master`发行分支 `dev`开发主分支 `dev-*`开发者分支 `fea-*`开发者自己的功能性分支

- 在码云上创建私有仓库，然后管理成员，将开发者一一邀请进来，然后这时候就有了一个问题：
    - 所有的开发者都具有master的所有权限，所以这时候就会很容易出现冲突,所以就需要设置master和开发主分支dev为保护模式，只有管理员负责进行推送
    - 管理员， 新建若干分支：`git branch 分支` 提交到远程 `git push --all` 
    - 对应的开发者克隆项目，然后 `git checkout 对应的自己的分支` 就可以开始工作了 
        - （ 如果没有分支就下拉命令`git fetch origin 对应的分支`）
    - 然后各个开发者写自己的，然后提交`git push` 就行了
    - 管理员需要 `git fetch origin 分支`得到所有分支
        - 针对每个分支进行拉取： 切换过去`git checkout 开发者分支`，然后`git pull 开发者分支`下拉最新
        - 然后选择合并`git merge --no-ff 开发者分支` ，处理冲突然后提交
    - 开发者下拉自己的分支 或者开发主分支 dev 即可

********

`分支的处理的一次实验 2017-10-21 23:57:34`
- `git fetch --all` 获取远程所有分支（新分支）
- `git pull --all` 获取所有分支最新提交 这个就会自动合并？？？越来越不理解了

- dev-test 分支进行修改，然后提交一次，然后push 
- master： `git merge --no-ff dev-test` 进行合并，就会在分支图上得到一个环
    - master 分支本地会多出2个提交

- dev-test 进行修改，然后1次提交，push
- master : `git pull origin dev-test ` 执行merge命令就会提示没有可以合并的修改。
    - 这是为什么？？？？


### 最终方案
`双方都有修改`
- 开发人员提交完后，主分支管理人员切换到开发人员的分支然后 `git pull 开发人员分支`，然后切换回主分支上 `git merge --no-ff 开发人员分支`（填写注释） 然后push
    - 然后切换到开发人员分支上执行 `git merge master 然后 git push` 还是`git pull origin master`
    - 然后通知开发人员下拉其自己的开发分支即可

`只有一方修改`
- 主分支进行修改了开发分支没有动，那么开发分支 直接下拉 `git pull origin master`下拉修改代码即可
- 如果是开发分支修改，主分支没有动，那么管理员负责切换到开发分支 然后pull 然后merge 然后 push 然后切换开发分支 然后 pull 
