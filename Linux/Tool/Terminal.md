`目录 start`
 
- [Terminal](#terminal)
    - [终端模拟器对比](#终端模拟器对比)
    - [终端工具命令](#终端工具命令)
        - [Shell内建命令](#shell内建命令)
        - [需用户安装](#需用户安装)
        - [效率工具](#效率工具)
            - [Autojump](#autojump)
            - [tmux](#tmux)
            - [notes](#notes)
            - [todo.txt-cli](#todotxt-cli)
        - [文本操作](#文本操作)
            - [xclip](#xclip)
        - [文件操作](#文件操作)
            - [zssh](#zssh)
        - [分享](#分享)
            - [asciinema](#asciinema)

`目录 end` |_2018-08-27_| [码云](https://gitee.com/gin9) | [CSDN](http://blog.csdn.net/kcp606) | [OSChina](https://my.oschina.net/kcp1104) | [cnblogs](http://www.cnblogs.com/kuangcp)
****************************************
# Terminal
> 终端模拟器是吸引我放弃习惯的Windows而转投Linux怀抱的主要原因

## 终端模拟器对比
> 列举出系统可安装终端 `sudo apt search terminal | grep -E terminal.+amd64`

- `qterminal` 可定制标签页位置以及透明度，很简洁,挺好用,但是不能内容和窗体大小自适配, 0.7.1已没有这个bug, 还是很好用的模拟器, 但是多标签的时候, 会有内存泄露
- `mate-terminal` 和gnome-terminal 基本配置什么的几乎一样，只是标题栏简洁一丢丢，如果使用选择即复制,那么在跨标签页复制粘贴有bug
- `gnome-terminal` 很简洁，但是多标签时，标签栏太大,标签页底部有白边
- `sakura` 外观上和前两个几乎一样，标签页可以更简洁，但是设置不好调, 而且不能自定义快捷键
- `deepin-terminal` 功能很多，主题很多，功能最为强大，但是字体可以选的很少
- `terminator` 可以定制背景图片，但是在我这deppin系统里有bug，多标签是假的，命令全是在共享的，不能用。。
- `tmux` 运维必备软件，入门有些繁琐
- `tilda` 内嵌于桌面上, 小命令方便, 需要查看文件就不方便了

> [更多可安装终端](https://gitee.com/kcp1104/codes/gca14wtqvm67l9j5r0deb56#Terminals.md)

************************
## 终端工具命令
> /bin/* 系统自带命令

- which 命令的位置
- false 以失败码退出程序
- `stty -a` 查看键映射

### Shell内建命令
- whence 查看命令的真实面貌 (zsh中的内建命令)
- where 查找命令的位置 (Zsh中内建命令)

### 需用户安装
> 最终都会安装到 /usr/bin/*  目录下

- wc -l file _统计文件行数_
- md5sum 报文摘要算法 Message-Digest Algorithm 5 的实现 
    - `md5sum file` 计算出md5值
    - `md5sum -c file.md5` file 和 file.md5 在同一目录下, 执行这个命令就是检查md5是否匹配, 确保文件的完整性和正确性

- last _查看Linux登录信息_
    - last -n 5 最近五次登录
- w | uptime _查看启动情况_
- colrm
    - ps | clorm 20 30 `colrm` _删除输出的20 到30 列_
- xsel 
    - `cat a.md | xsel -b` _将文件所有内容复制到剪贴板_ 但是处理大文件时会失效 xclip 更有效

- htop _终端里的任务管理器_
- strace -p PID _查看系统调用_
- cmatrix _装13,字符雨_
- logkeys 记录键盘输入 [Github](https://github.com/kernc/logkeys)
- expect [用于自动输入密码](http://www.cnblogs.com/iloveyoucc/archive/2012/05/11/2496433.html)

- [WTF](https://wtfutil.com/posts/overview/) | [Github Repo](https://github.com/senorprogrammer/wtf)
    - 丰富的功能, 一个方便的终端控制面板

- ag `快速当前目录下, 全文内容搜索, 快到可怕` ubuntu:silversearcher-ag  alpine:the_silver_searcher
    - [The Silver Searcher](https://github.com/ggreer/the_silver_searcher)

### 效率工具
> 提高工作和开发效率

#### Autojump
> 统计cd 目录，方便目录跳转  *shrc 中要有 : `. /usr/share/autojump/autojump.sh`  

- `apt install autojump` 设置为自动运行 `echo '. /usr/share/autojump/autojump.sh' >> ~/.bashrc`
    - `j -v` 查看安装版本
    - `j --stat` 查看统计信息
    - `j --help`
    - `jo code` 打开code文件夹
    - `jco c` 打开子目录
- `ls -l ~/.local/share/autojump/` 统计信息的目录，清除就相当于卸载重装了

#### tmux
> 好用的管理会话的软件, 在服务器上是很有用的

- [ ] 学习使用 

> [tmux 入门](http://blog.jobbole.com/87278/)

- 新建会话 `tmux new -s myth`  
- 连接会话 `tmux a -t test`
- 显示所有 `tmux ls` 
- `Ctrl B`  再 `C`  新建一个窗口 `Ctrl B` `数字键`切换指定窗口
- 断开会话但是后台运行 `ctrl+B D`

#### notes
> 管理笔记
> [Github](https://github.com/pimterry/notes)

#### todo.txt-cli
> 终端内的 todo 
> [Github](https://github.com/todotxt/todo.txt-cli)

*************
### 文本操作
#### xclip
> 便捷的文本复制
- `cat README.md | xclip -sel clip` 将文件复制到剪贴板

***********
### 文件操作
#### zssh
> 便捷的文件传输

- [参考博客](http://blog.csdn.net/ygm_linux/article/details/32321729)

***********
### 分享
#### asciinema
> 终端录制工具

- 执行 `asciinema`或`asciinema rec` 即可开始录制
- 要注册就运行 `asciinema auth` 进入输出的网址，填邮箱和名字即可（每次登录都要这样。或者使用邮件来确认，麻烦ing）

