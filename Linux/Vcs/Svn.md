`目录 start`
 
- [SVN](#svn)
    - [服务端安装](#服务端安装)
        - [svnadmin使用](#svnadmin使用)
        - [备份和恢复](#备份和恢复)
            - [远程](#远程)
    - [客户端安装](#客户端安装)
    - [使用](#使用)
        - [添加文件](#添加文件)
        - [配置忽略文件](#配置忽略文件)
        - [提交](#提交)
        - [查看仓库](#查看仓库)
        - [处理冲突](#处理冲突)
            - [树冲突](#树冲突)

`目录 end` |_2018-08-04_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# SVN
> 传统的中心化版本控制工具,能够精确控制每个目录的权限, Apache顶级项目  
> [SVN 官网](http://subversion.apache.org/) | [SVN中文网](http://www.svn.org.cn) [Subversion 与版本控制 书籍](http://svnbook.red-bean.com/)

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

*********************************
## 使用
> [参考博客: linux-svn命令](http://blog.csdn.net/gexiaobaohelloworld/article/details/7752862) | [SVN常用命令](http://www.cnblogs.com/SanMaoSpace/p/5102878.html)
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

- _删除文件_ `svn remove path`

> [参考博客: svn下忽略文件和文件夹](http://blog.sina.com.cn/s/blog_6e165cc101017m0j.html)
> [参考博客: svn 忽略文件、文件夹](https://ztgame.shenyu.me/svn/svn-ignore.html)

### 配置忽略文件
- `svn propedit svn:ignore 项目文件夹` 会打开默认配置,  和gitignore一样的配置, 然后保存即可
    - 文件夹就是项目, 所以要在项目根目录的上级目录之心这个命令
    - 如果上面没有调起编辑器, 就要在 .bashrc 中 `export SVN_EDITOR=vim`
- 然后提交到仓库, 即可完成 忽略文件的配置, 为了可见性, 一般和.gitignore一样的配置即可
    - 导入忽略文件 `svn propset -F .svnignore .`

### 提交
> [参考博客: SVN提交注意点](http://www.cnblogs.com/masb/archive/2012/01/12/2320182.html) 

### 查看仓库
> [查看最后修改的文件](https://java-er.com/blog/svn-last-files/) | [svn历史版本对比以及还原到历史版本](http://www.cnblogs.com/simonote/articles/3086717.html)

- `svn log | less` 这样能更为方便和干净
- `svn cat -r 版本号 文件` 输出某个版本的某文件(文件必须在本地存在)
- `svn diff -r 版本号:版本号 文件` 对比两个版本的某文件

### 处理冲突
> 冲突的产生: 因为多个开发人员进行修改了同一个文件夹(修改,删除文件夹), 同一个文件. 

#### 树冲突
> 多个开发人员修改了同一个文件夹, 并且一方修改, 一方做了删除 

> [参考博客: SVN 树冲突解决详解](https://blog.csdn.net/xgf415/article/details/75196714)
> [参考博客: 使用SVN命令行解决树冲突(tree conflict)](https://www.jianshu.com/p/e3cc83ca512d)

1. 标记冲突已解决(使用本地的状态, 本地该文件的状态是Delete, 提交后服务端对应的文件就会被删除)
    - `svn resolve --accept=working file/dir`

