---
title: LinuxUI
date: 2024-02-03 10:39:52
tags: 
categories: 
---

💠

- 1. [GUI](#gui)
    - 1.1. [Display Manager](#display-manager)
    - 1.2. [Window Manager](#window-manager)
    - 1.3. [Desktop environment](#desktop-environment)
- 2. [UI](#ui)
    - 2.1. [Font](#font)
        - 2.1.1. [字体渲染](#字体渲染)
    - 2.2. [Theme](#theme)
    - 2.3. [Icon](#icon)

💠 2024-12-02 11:47:22
****************************************

# GUI
> [GUI Under Linux | Baeldung on Linux](https://www.baeldung.com/linux/gui)  

## Display Manager 
- [LightDM](https://wiki.archlinux.org/title/LightDM)

> [Computer instantly wakes after suspending](https://forums.linuxmint.com/viewtopic.php?t=408260)  

`sudo systemctl restart display-manager`

## Window Manager
- xfwm4 `XFCE4`
- compiz

## Desktop environment
> [Desktop environment](https://wiki.archlinux.org/title/desktop_environment)

1. [Gnome](/Linux/DE/Gnome.md)
2. [Xfce](/Linux/DE/Xfce.md)


************************

- [Top 10 Best Linux Docks 2022](https://www.digitalocean.com/community/tutorials/top-best-linux-docks-2020)
    - plank

************************

# UI

> Linux UI: themes icons fonts

## Font

1. /usr/share/fonts/
2. ~/.local/share/fonts

- 刷新字体缓存 `fc-cache -fv`
  - 注意还有一个32位命令 fc-cache-32

> [字体文件 详情](/FrontEnd/Font.md)  

- npm vue minikube 等命令行的工具输出的日志提示会包含emoji, 需要终端字体支持展示unicode
    - 终端内 Emoji 支持 [emoji](https://blog.sebastian-daschner.com/entries/linux-terminal-font-alacritty-jetbrains-mono-emoji) `noto-color-emoji 字体 支持颜色` 

### 字体渲染

> [Debian8安装Infinality改善字体渲染，安装Ubuntu字体](https://www.linuxdashen.com/debian8%E5%AE%89%E8%A3%85infinality%E6%94%B9%E5%96%84%E5%AD%97%E4%BD%93%E6%B8%B2%E6%9F%93%EF%BC%8C%E5%AE%89%E8%A3%85ubuntu%E5%AD%97%E4%BD%93)
> [一条命令搞定Linux字体渲染](https://www.lulinux.com/archives/278)
> [Font Configuration/Chinese (简体中文)](https://wiki.archlinux.org/index.php/Font_Configuration/Chinese_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
> [参考: Fcitx (简体中文)](https://wiki.archlinux.org/index.php/Fcitx_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))


字体库

[nerd fonts](https://www.nerdfonts.com/)

************************

## Theme

1. /usr/share/themes/ 系统级
2. ~/.themes/  ~/.local/share/themes 用户级

> [McMojave](https://www.xfce-look.org/p/1275087/)

- [Github:vimix](https://github.com/vinceliuice/vimix-gtk-themes) `material design theme`

> [参考: 10 Great Linux GTK Themes For 2018 ](https://www.maketecheasier.com/gtk-themes-for-linux/)

- [catppuccin](https://github.com/catppuccin/catppuccin)
- [pingguo](https://www.gnome-look.org/p/1239453/)
- [Sierra](https://www.gnome-look.org/p/1013714/)
- [GTK3主题：OSX-Arc](https://www.linuxidc.com/Linux/2017-01/139053.htm)

- 某个应用运行时使用指定主题： `GTK_THEME=xxx COMMAND` 
    - 例如 `GTK_THEME=vimix-light-doder /Apps/IDE/mat/MemoryAnalyzer`

************************

## Icon

1. /usr/share/icons
   - 例如： `/usr/share/icons/Papirus/128x128/apps/`

> sudo apt search icon-theme  也能看到很多icon

1. Halo-icon-theme

