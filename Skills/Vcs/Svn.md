---
title: SVN
date: 2018-11-21 10:56:52
tags: 
    - 基础
categories: 
    - 版本控制
---

**目录 start**

1. [SVN](#svn)
    1. [服务端安装](#服务端安装)
        1. [svnadmin使用](#svnadmin使用)
        1. [备份和恢复](#备份和恢复)
            1. [远程](#远程)
    1. [客户端安装](#客户端安装)
        1. [GUI](#gui)
    1. [使用](#使用)
        1. [添加文件](#添加文件)
        1. [配置忽略文件](#配置忽略文件)
        1. [提交](#提交)
        1. [查看仓库](#查看仓库)
        1. [处理冲突](#处理冲突)
            1. [树冲突](#树冲突)
        1. [回滚到指定版本](#回滚到指定版本)
1. [Tips](#tips)
    1. [下载Github子目录](#下载github子目录)

**目录 end**|_2020-04-27 23:42_|
****************************************
# SVN
> 传统的中心化版本控制工具,能够精确控制每个目录的权限, Apache顶级项目  
> [SVN 官网](http://subversion.apache.org/) | [SVN中文网](http://www.svn.org.cn) [Subversion 与版本控制 书籍](http://svnbook.red-bean.com/)

> [参考: SVN与Git比较的优缺点差异](https://www.cnblogs.com/Sungeek/p/9152223.html)

> svn 不能提交单个文件里的部分提交, 要么就整个文件提交, 要么不提交, git则可以

## 服务端安装
> 安装 svnadmin

### svnadmin使用
> [参考 建立一个仓库](http://www.cnblogs.com/xkops/p/5457935.html)
`svnadmin create /yc/svn/rep-ops`

### 备份和恢复
> [SVN版本库的备份、还原、移植（初级篇、中级篇和高级篇）](https://blog.csdn.net/windone0109/article/details/2908133)  
> [svn备份一般采用三种方式](https://blog.csdn.net/beyondlpf/article/details/54138865)

1. 备份 svndump /svn/repos > a.dump
2. 恢复 svnadmin load /svn/repos < a.dump

#### 远程
> [详细文档](http://svnbook.red-bean.com/en/1.7/svn.ref.svnrdump.html#svn.ref.svnrdump.sw.incremental)
> | [问题的解决](https://www.saas-secure.com/svn-hosting/svn-dump-restore.html#svn-remote-backup-restore)
> | [参考](https://www.saas-secure.com/svn-hosting/svn-dump-restore.html)

1. 增量备份 `svnrdump dump http://192.168.10.200/svn/test/ --username kuangchengping --password 123456 -r 3:4 --incremental > b4.dump`
2. 恢复 `svnrdump load http://192.168.10.200/svn/test/ --username kuangchengping --password 123456 < b4.dump`

**********************************
## 客户端安装

**Ubuntu**
> `sudo apt install subversion` 安装后可使用的命令就是svn

### GUI

*********************************
## 使用
> [参考: linux-svn命令](http://blog.csdn.net/gexiaobaohelloworld/article/details/7752862) | [SVN常用命令](http://www.cnblogs.com/SanMaoSpace/p/5102878.html)
> | [Linux下SVN客户端使用教程（全）](https://blog.csdn.net/qq_27968607/article/details/55253997)  

- _下拉代码_ `svn co URL`  
### 添加文件
- `svn add filename` , 或者 `*.java`是添加当前目录下java文件,
-  或者 文件夹, 一般使用文件夹好点,也就是src目录
- 强制添加所有文件`svn add * --force`  
- 将改动的文件提交到版本库 `svn ci -m "update"` 
    - 因为是中心化的仓库, 所以提交就是推送到总仓库了, 不像Git那样先提到到本地仓库, 然后推送至远程仓库
- _更新本地代码_ `svn up`  
> svn update如果后面没有目录，默认将当前目录以及子目录下的所有文件都更新到最新版本

- _删除文件_ `svn remove|rm path`

> [参考: svn下忽略文件和文件夹](http://blog.sina.com.cn/s/blog_6e165cc101017m0j.html)
> [参考: svn 忽略文件、文件夹](https://ztgame.shenyu.me/svn/svn-ignore.html)

### 配置忽略文件
> svn:ignore 和 svn:global-ignores

1. 作用范围
    - svn:ignore：只对当前目录有效； 
    - global-ignores：是全局有效，就是所有目前都有效；
1. 配置方式
    - svn:ignore：必须在项目的每个工作目录都要设置；相同配置时,优先级高于全局的
    - global-ignores：只需要配置一次；

- `svn propedit svn:ignore 项目文件夹` 会打开默认配置,  和gitignore一样的配置, 然后保存即可
    - 文件夹就是项目, 所以要在项目根目录的上级目录执行这条命令
    - 如果上面没有调起编辑器, 就要在 .bashrc 中 `export SVN_EDITOR=vim`

- 然后提交到仓库( svn co -m "xxx" ), 即可完成 忽略文件的配置, 为了可见性, 一般和.gitignore一样的配置即可
    - 导入忽略文件 `svn propset -F .svnignore .`

### 提交
> [参考: SVN提交注意点](http://www.cnblogs.com/masb/archive/2012/01/12/2320182.html) 

> 部分提交 [参考](https://blog.mimvp.com/article/15666.html)

- 提交指定文件以及目录 `svn ci readme.md src/* -m "1.update readme 2.add src change"`
- `svn ci -m "msg"` 提交所有已添加到版本库的操作(新建, 修改, 删除)

### 查看仓库
> [查看最后修改的文件](https://java-er.com/blog/svn-last-files/) | [svn历史版本对比以及还原到历史版本](http://www.cnblogs.com/simonote/articles/3086717.html)

- `svn log | less` 这样能更为方便和干净
- `svn cat -r 版本号 文件` 输出某个版本的某文件(文件必须在本地存在)
- `svn diff -r 版本号:版本号 文件` 对比两个版本的某文件

> svn st 
  
![svn code](https://raw.githubusercontent.com/Kuangcp/ImageRepos/master/Tech/svn/svn_codes.png)

### 处理冲突
> 冲突的产生: 因为多个开发人员进行修改了同一个文件夹(修改,删除文件夹), 同一个文件. 

#### 树冲突
> 多个开发人员修改了同一个文件夹, 并且一方修改, 一方做了删除 

> [参考: SVN 树冲突解决详解](https://blog.csdn.net/xgf415/article/details/75196714)
> [参考: 使用SVN命令行解决树冲突(tree conflict)](https://www.jianshu.com/p/e3cc83ca512d)

1. 标记冲突已解决(使用本地的状态, 本地该文件的状态是Delete, 提交后服务端对应的文件就会被删除)
    - `svn resolve --accept=working file/dir`

### 回滚到指定版本

```sh
    svn update 
    svn merge -r 100:99 .
    svn ci -m "rolled back to r99"
```

# Tips
## 下载Github子目录
> [Doc](https://help.github.com/en/articles/support-for-subversion-clients)

- svn co URL
    - /tree/master/ 换成 /trunk/ 
    - /tree/master/ 换成 /branches/branchname/ 

************************

> 删除认证信息

`rm -rf ~/.subversion/auth`

***********************

1. 表现: IDEA 报错 uncongnized character scheme in 2019-01-03_15:25:42.log 
1. 后果: svn 所有操作都无响应, 相当于 idea的 svn 功能废了
1. 解决方案: 直接删除 .svn 目录, svn co 另一个目录, 把那份 .svn 目录拿过来
1. 分析: 很有可能文件名, 或者日志内容具有 svn 不认识的编码, 导致的问题

**********

