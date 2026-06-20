# Windows 

> [Atlas-OS/Atlas](https://github.com/Atlas-OS/Atlas)`裁剪优化版本`  

## 安装激活
> win10

https://www.microsoft.com/en-gb/software-download/windows10ISO
https://pureinfotech.com/create-windows-10-virtual-machine-virtualbox/

https://blog.csdn.net/qq_37700257/article/details/126284196#commentBox

> 常用路径 
1. Windows 所有字体 C盘Windows/Fonts 目录下

> tasklist 
- 相当于 Linux的 ps 命令, 查看帮助为 `tasklist /?`
- 按可执行文件查找运行的进程 `TASKLIST  /FI "IMAGENAME eq idea64.exe"`

- 资源管理器插件, 支持多标签, 类似于Chrome的使用 [clover](http://cn.ejie.me/)`但是有广告`
- 可以用来根据鼠标查询进程 [process-explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)`有效定位广告窗口`

## 工具
> Windows Terminal 
- Alt Shift -/= 横向/竖向切分窗口

### 终端 
CMD
PowerShell

- git-for-windows
- [cygin](http://x.cygwin.com/)
- MSYS2
    - 最佳Posix兼容层

#### MSYS2
> 完成兼容性的配置后, 配置上 zsh, tmux 就可以实现类似Linux上的体验了, 但是会卡顿一些, 使用习惯能保持一致

/etc/profile

```sh
# 把 Windows 的 PATH 合并进来
export PATH="$PATH:/c/Windows/System32:/c/Windows:/c/Program Files:/c/Program Files (x86):/c/Program Files/Go/bin"

# 如果你有特定的 Windows 环境变量需要导入
export JAVA_HOME=$(cygpath -u "$JAVA_HOME") 2>/dev/null || true
export MAVEN_HOME=$(cygpath -u "$MAVEN_HOME") 2>/dev/null || true
```
注意改配置需要重启MSYS2. 然后可以装tmux 多会话的持久化和窗口管理了

注意默认 ln -s 时会直接降级为复制, 需要配置 `export MSYS="winsymlinks:nativestrict"` 才会建符号链接

## 性能测试
- Msi after burner 显卡超频 硬件监控
- Aida64 电脑信息检测，稳定性测试
- As ssd Benchmark 硬盘测试
- HD Tune 硬盘测试
- Ctystal Disk Mark 更专业硬盘测试
- 3D Mark 电脑性能测试


## 网络
- tracert 等同于Linux的 traceroute
- ipconfig 等同于Linux的 ifconfig

## 影音
[Potplayer](http://potplayer.tv/?lang=zh_CN)

# Tips
## 寻找占用文件的进程
> 任务管理器 -> 性能tab 右上角打开 资源监视器 -> CPU的tab 关联的句柄窗口 搜索文件名



> [Win11 的效率模式和 EcoQoS 是糊弄人的东西 - V2EX](https://v2ex.com/t/928682)  
> [Quality of Service - Win32 apps | Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/procthread/quality-of-service)效能模式  
