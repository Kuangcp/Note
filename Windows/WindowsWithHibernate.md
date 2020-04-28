---
title: Windows的快速启动
date: 2019-01-16 20:49:28
tags: 
categories: 
    - Windows
---

**目录 start**

1. [Windows的快速启动](#windows的快速启动)
    1. [解决Linux下挂载hibernate状态分区的问题](#解决linux下挂载hibernate状态分区的问题)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Windows的快速启动 
> [参考: Windows快速启动背后的功臣：休眠](https://zhuanlan.zhihu.com/p/28639474)

- 从8开始, Windows开机速度显著加快了, 因为引入了快速启动这个东西, 也就是在关机的时候将一些数据缓存到 hiberfil.sys 文件上, 下次开机能加载该文件从而快速开机

- 开了快速启动之后, 之后的关机就不是纯粹的关机, 而是混合模式关机 先进入休眠状态, 然后关机
1. `shutdown /s /full / t 0`
1. 或者选择重启

> 分区为 hibernate 状态后, Linux挂载就只能是只读模式了

## 解决Linux下挂载hibernate状态分区的问题
> [Unable to mount Windows (NTFS) filesystem due to hibernation](https://askubuntu.com/questions/145902/unable-to-mount-windows-ntfs-filesystem-due-to-hibernation) `原因以及解决方案`

1. 尝试该方法  `sudo ntfsfix /dev/sdXY` 
1. 强制挂载为读写模式 `sudo mount -t ntfs-3g -o ro /dev/xx /media/xx`
1. 强制解除 hibernate 状态 `sudo mount -t ntfs-3g -o remove_hiberfile /dev/xxx /media/xxx` 依赖 ntfs-3g 包

> 最后一种最为暴力, 也是通常能解决问题, 但是会造成Windows数据的丢失
