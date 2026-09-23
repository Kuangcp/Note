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

> [microsoft/PowerToys: Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows](https://github.com/microsoft/powertoys)  

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

> Tips

- 注意默认 ln -s 时会直接降级为复制, 需要配置 `export MSYS="winsymlinks:nativestrict"` 才会建符号链接
- 新建一个tab的卡顿原因是 Linux上是fork() 基于COW特性毫秒级别,但是windows没有, 所以需要 `fork() 模拟:  挂起父进程 → 复制地址空间 → 创建子进程 → 恢复`  
    - 这个"复制地址空间"在 Windows 上不是内核 COW，是用户态手动复制，如果父进程（tmux server）内存占用大，复制时间显著增加。
- 首次进入一个git仓库时, 会遇到刷新索引, 所有文件都会有修改记录, 但是没有修改内容, 还是因为文件权限的问题, 继续配置`export MSYS="winsymlinks:nativestrict noacl"`
    - noacl: 告诉 cygwin 不要模拟 ACL，简化权限视图
    - 也可以一次性的修改, 就做一次所有内容的stash, 然后drop掉, 索引就会刷新成MSYS2的格式后续就不会有问题了, 但是这时候索引会改为MSYS的格式, 在Windows端的git-bash里会认为git索引乱了 因为是两套格式, 互相会认为互相是错的格式

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

> Win11 系统崩溃，花屏，重启后无法调节屏幕亮度
- 设备管理器看到 显示适配器 里的 AMD Radeon 设备状态有问题
- 解决： 先禁用，再启用。 就恢复了
- 原因？ 

对于 ThinkBook 锐龙版 这种采用核显（iGPU）的轻薄本，显存（UMA Framebuffer）是动态从系统物理内存中划分出来的。当你在跑 Gradle 编译（尤其是混合了 Compose Multiplatform、Kotlin 大项目或多模块并行构建）时，JVM 和编译器会瞬间吃掉极高的物理内存。
如果此时物理内存几乎被完全榨干，操作系统在面临极端内存压力（OOM 边缘）时，可能会发生以下连锁反应：

   1. 显存分配失败/被抢占：显卡驱动在执行某些渲染指令或尝试申请动态显存时，系统无法提供连续的物理内存。
   2. 驱动超时崩溃（TDR）：AMD 显卡驱动因为拿不到关键的内存资源，或者内部硬件响应超时，直接引发 TDR（Timeout Detection and Recovery） 机制。这在表现上就是屏幕突然闪烁、花屏、绿屏，随后为了保护系统，Windows 强制卸载或锁死了该驱动，从而在设备管理器中抛出代码 31。
   3. 功能缺失：由于驱动处于不可用的 Fallback 状态，底层的亮度调节（PWM 信号控制）自然就失效了，只能维持在硬件默认的最高亮度。

> 🛠️ 针对性解决策略
既然定位到了是 Gradle 编译引发的内存挤压与显卡驱动冲突，我们可以从以下几个维度来彻底根治这个问题：
> 1. 锁死（加大）BIOS 中的固定显存（最有效）
默认情况下，联想的 UMA 显存设置是 Auto（动态分配）。当系统内存吃紧时，核显的生存空间就会被严重压缩。

* 操作方法：重启电脑，开机连续按下 F2（或 Fn + F2）进入 BIOS 界面。
* 寻找设置：切换到 Configuration 或 Advanced 选项卡，找到 UMA Frame Buffer Size（或显存大小设置）。
* 修改参数：将原本的 Auto 强制修改为固定的 2G 或 4G（根据你总内存是 16G 还是 32G 来决定）。
* 效果：这会在硬件层面强行划出一块显卡专属的“自留地”，无论 Gradle 怎么抢占物理内存，这部分显存都绝不会被剥夺，从而避免驱动因内存耗尽而崩溃。

> 2. 限制 Gradle 与 JVM 的狂暴内存占用
你之前的编译可能触发了 Gradle 的多进程并行以及高额 Heap 分配。可以通过限制编译器的最大内存来给系统留出呼吸口。

* 修改你项目根目录下的 gradle.properties，或者全局的 ~/.gradle/gradle.properties：

> 限制 Gradle Daemon 的最大堆内存（根据实际调整，不要把系统内存占满）
org.gradle.jvmargs=-Xmx3g -XX:MaxMetaspaceSize=512m -XX:+UseG1GC

> 限制并行编译的线程数（减少并发垃圾回收和内存突发）
org.gradle.workers.max=4


> 3. 开启 AMD 驱动的 TDR 宽容度（防止花屏后直接死锁）
Windows 默认检测到显卡 2 秒没响应就会重启驱动（从而变成代码 31）。我们可以通过注册表延长这个检测时间。

   1. 按下 Win + R 输入 regedit 打开注册表。
   2. 导航至：HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers
   3. 在右侧空白处右键 -> 新建 DWORD (32位)值，命名为 TdrDelay。
   4. 双击它，将基数改为十进制，数值数据改为 8（代表允许显卡最多卡顿 8 秒而不崩溃）。
   5. 再新建一个 DWORD (32位)值，命名为 TdrDdiDelay，数值同样设为 8。
   6. 重启电脑生效。

> 4. 禁用硬件加速缓解显卡压力
如果是在 IntelliJ IDEA 或 Android Studio 中跑编译，可以尝试暂时关闭 IDE 的硬件加速渲染，减轻编译时显卡的负担。

* 在 IDEA 中双击 Shift 搜索 Registry...。
* 找到 sun.java2d.opengl 或相关的硬件加速选项，尝试将其关闭，观察是否能缓解花屏崩溃。
