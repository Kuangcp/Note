---
title: Xfce
date: 2019-10-19 16:47:01
tags: 
    - 桌面环境
categories:
    - Linux
---

💠

- 1. [Xfce](#xfce)
    - 1.1. [Panel](#panel)
        - 1.1.1. [Plugin](#plugin)
- 2. [Tips](#tips)

💠 2026-03-03 16:00:09
****************************************
# Xfce 
> [www.xfce-look.org](https://www.xfce-look.org)  

1. notify-send 发送新通知 [使用notify-send发送桌面通知](https://blog.csdn.net/lujun9972/article/details/53292620)
    - notify-send -i iconFilePath title detail -t 1500
    - -A 
        - `notify-send Tips -A 1=Active -A 0=Reject` 消息弹窗带按钮（Active和Reject） 命令的返回是按钮的值 1或0
        - `notify-send Tips -A Active -A Reject` 不指定值默认返回下标，即返回0或1
    - -t 指定通知过期时长 单位s
    - -p 打印出通知的id
    - `-r id` 当前通知替换掉指定id的通知

1. xflock4 锁屏
1. zenity GTK实现，各种输入组件，弹窗提示

[xfce4 install xrdp](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop?tabs=azure-cli)


## Panel 

### Plugin
> [Xfce Panel Plugins How To](https://wiki.xfce.org/dev/howto/panel_plugins)  
> [Create my own panel plugin](https://askubuntu.com/questions/633952/create-my-own-panel-plugin-xubuntu)  

`可参考项目`
> [xfce4-weather-plugin](https://gitlab.xfce.org/panel-plugins/xfce4-weather-plugin)  
> [xfce4-sensors-plugin](https://launchpad.net/ubuntu/+source/xfce4-sensors-plugin)  

# Tips 
1. Dock相关软件 出现阴影 `Window Manager Tweaks -> Compositor -> 关闭 Show shadow under dock windows`
1. 键盘持续按键，延迟速度 Keyboard -> Behavior -> Repeat delay 调低延迟时间
1. 重新加载配置重启 `xfwm4 --replace &`

> 切换窗口卡顿
- 