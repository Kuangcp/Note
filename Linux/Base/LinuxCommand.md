`目录 start`
 
- [系统常用基础命令](#系统常用基础命令)
    - [输入输出](#输入输出)
        - [重定向](#重定向)
    - [管道](#管道)
        - [xargs](#xargs)
    - [time](#time)
    - [date](#date)
    - [grep](#grep)
    - [定时任务](#定时任务)
        - [crontab](#crontab)
        - [Systemd](#systemd)
- [实用的工具](#实用的工具)
    - [终端工具](#终端工具)
    - [图形化工具](#图形化工具)
        - [剪贴板管理](#剪贴板管理)

`目录 end` |_2018-08-30_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# 系统常用基础命令

## 输入输出

### 重定向
- 输出重定向  `> a.log 2>&1` 表示为将2也输出到标准输出 **为了方便记忆也可以将&理解为C中的取地址符:2重定向到1的地址**
    - 2是错误输出
    - 1是标准输出

******************
## 管道
> [参考博客: linux 管道 ](http://www.cnblogs.com/davidwang456/p/3839874.html)
> [参考博客: linux shell 管道命令(pipe)使用及与shell重定向区别](http://www.cnblogs.com/chengmo/archive/2010/10/21/1856577.html)
- [ ] 学习管道的使用

### xargs
- [ ] xargs 让命令更为灵活

***************************
## time
> 可以用于统计命令运行消耗的时间

- bash内置简易time `time` 和 /usr/bin/time `\time`
    - `\time -v ls -al`
## date
> 获取日期和时间 `date +%Y_%m_%d_%H:%M:%S`

- 获取前一天日期 `date --date='1 day ago' -R`
- 将秒时间戳转换为日期 `date --date='@1524738626'`

## grep
> egrep [相关网页](http://man.linuxde.net/grep) 与 grep -E 等价

- 正则 `grep -E "[1-9]+"` 注意` [] 和 ()`的区别 `[]` 是里面单个字符 `()`是里面的全部

- -o 一行内多次匹配 `grep -o 的 total.md | wc -l` 统计所有`的`的数量
- -i 忽略大小写

## 定时任务
### crontab
> [参考博客 shell定时任务crontab](http://www.cnblogs.com/taosim/articles/2007056.html)
`minute hour day-of-month month-of-year day-of-week commands  `

> cron 脚本中的操作命令 最好都使用绝对路径

### Systemd
> [参考博客: Systemd 定时器教程](http://www.ruanyifeng.com/blog/2018/03/systemd-timer.html) `配置和使用上比Crontab更繁杂, 但是有更多的可控制项`


*******************************************

# 实用的工具
## 终端工具
> [详细](/Skills/Application/Terminal.md)

## 图形化工具
### 剪贴板管理
> [参考博客: 面向 Linux 的 10 款最佳剪贴板管理器](https://linux.cn/article-7329-1.html)

- CopyQ 比较好用

> [参考博客: 这9个Linux命令非常危险 请大家慎用](https://www.jb51.net/LINUXjishu/498660.html)

> [参考博客: 关于 Linux 你可能不是非常了解的七件事](https://linux.cn/article-8934-1.html)