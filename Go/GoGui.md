---
title: GoGui
date: 2026-11-05 16:46:13
tags: 
categories: 
---

💠

- 1. [Go GUI](#go-gui)
- 2. [概述](#概述)
    - 2.1. [选择指南](#选择指南)
- 3. [Fyne](#fyne)
    - 3.1. [安装与运行](#安装与运行)
- 4. [Gio (GioUi)](#gio-gioui)
    - 4.1. [特性](#特性)
- 5. [Walk](#walk)
    - 5.1. [特性](#特性)
- 6. [GoGTK (gtk3)](#gogtk-gtk3)
    - 6.1. [安装依赖](#安装依赖)
- 7. [TUI (终端界面)](#tui-终端界面)
    - 7.1. [6.1 Bubbletea + Tview](#61-bubbletea--tview)
    - 7.2. [6.2 Football](#62-football)
- 8. [Web-based GUI](#web-based-gui)
    - 8.1. [7.1 Wails](#71-wails)
        - 8.1.1. [快速开始](#快速开始)
    - 8.2. [7.2 Flutter+Go](#72-fluttergo)

💠 2026-11-09 00:13:24
****************************************
# Go GUI

# 概述

Go 生态中有多种 GUI 开发方式，按渲染方式分为三类：

| 方式 | 代表框架 | 特点 |
|------|----------|------|
| **原生控件** | Walk, GoGTK | 调用系统原生控件，外观与平台一致 |
| **自绘引擎** | Fyne, Gio | 自己绘制所有控件，跨平台一致性高 |
| **Web技术** | Wails | 用 HTML/CSS/JS 做 UI，Go 做后端 |
| **终端界面** | Bubbletea, Tview, Football | 在终端里创建富文本界面 |

## 选择指南
> [go-gtk alternatives](https://go.libhunt.com/go-gtk-alternatives) `gui框架对比`

```
需要原生外观？          → Walk (Windows), GoGTK (Linux/GTK)
需要跨平台一致性？      → Fyne (推荐), Gio
想要现代 UI / 移动端？  → Gio (支持 iOS/Android)
想用 Web 技术栈？       → Wails + Vue/React
只需要终端工具？        → Bubbletea / Tview
追求简单快速上手？      → Fyne（纯 Go，无需 C 依赖）
```

- [egoist/mygo: Develop desktop apps with native UI or web frontend in Go](https://github.com/egoist/mygo)`原生且跨平台`  


- [awesome-go GUI section](https://github.com/avelino/awesome-go#gui)
- [Go GUI 框架评测文章](https://www.calhoun.com/gui-programming-with-go/)
- [The Complete Guide to Building Cross-Platform Desktop Apps with Go and Fyne](https://dev.to/jordan_d_burton/the-complete-guide-to-building-cross-platform-desktop-apps-with-go-and-fyne-2394)
- [Building Desktop Applications with Go - by @ebitengine](https://ebiten.org/)

> [oneo-me/nsgo: A cross-platform native UI engine with a Go backend: write apps in Go with signals, memos and flexbox layout, and each platform draws with its own native views — iOS, macOS, Windows, Android, Linux and the web](https://github.com/oneo-me/nsgo)  

---

# Fyne

> [Official](https://fyne.io/) | [GitHub](https://github.com/fyne-io/fyne)

最流行的跨平台 Go GUI 框架，纯 Go 实现，自绘引擎，API 简洁。

## 安装与运行

```sh
# 安装 fyne 命令行工具
go install fyne.io/fyne/v2/cmd/fyne@latest

# 导入依赖
go get fyne.io/fyne/v2
```

> **注意**：构建时需要 C 编译器（用于 CGO），因为底层调用 OpenGL/native 库。
> Linux 需要安装相关 dev 包（见下方依赖章节）。


> 跨平台打包

```sh
# macOS 打包
fyne package --os darwin

# Windows 打包
fyne package --os windows

# Linux 打包
fyne package --os linux

# 指定图标
fyne package --icon icon.png

# 生成安装包 (.app/.exe/.deb)
fyne bundle --overwrite --output bundled.go resources/
```

---

# Gio (GioUi)

> [Official](https://gioui.org/) | [GitHub](https://github.com/google/gioui)

Google 出品的图形/UI 框架，高性能自绘引擎，支持桌面 + 移动端。

## 特性

- **自绘引擎** — 所有渲染走自己管线，不依赖系统 GUI toolkit
- **跨平台** — Windows, macOS, Linux, Android, iOS, WebGL
- **高性能** — GPU 加速，适合动画密集型应用
- **纯 Go** — 无 CGO 依赖（某些后端可能例外）
- **操作式编程模型** — 每帧重新执行 UI 布局代码，类似 Flutter 的 build


> Gio API 比较复杂，建议使用 [`gioui.org/example`](https://gitlab.gunstone.dev/gioui/example) 作为起点。实际项目中可以搭配 [`gioui.org/shap`](https://gioui.org/) 做自定义绘制。推荐使用更上层的封装项目来降低门槛。

---

# Walk

> [GitHub](https://github.com/lxn/walk)

Windows 专属的原生 GUI 框架，基于 Win32 API。

## 特性

- **Windows 专用** — 仅支持 Windows (amd64/386)
- **原生控件** — 调用 Win32 原生控件，性能极好
- **声明式 UI** — 支持 declarative 语法，写法简洁
- **Signal/Slot** — 信号槽机制连接事件
- **MVC 模式** — 内置 Model-View-Controller 架构

---

# GoGTK (gtk3)

> [GitHub: go-gtk/go-gtk](https://github.com/go-gtk/go-gtk) | [mattn/go-gtk](https://github.com/mattn/go-gtk) (`deprecated`, 仍可用)

通过 CGO 绑定 GTK3，需要 C 语言环境的 GUI 框架。

## 安装依赖

```sh
# Ubuntu/Debian
sudo apt install libgtk-3-dev pkg-config

# Fedora
sudo dnf install gtk3-devel pkgconfig

# Arch
sudo pacman -S gtk3
```

> GoGTK 社区维护较不活跃，新项目建议考虑 **Fyne** 或 **Gio** 替代。

---

# TUI (终端界面)

Go 在终端富文本界面领域非常强大，以下框架适合 CLI 工具的可视化。

## 6.1 Bubbletea + Tview

[Charmbracelet/bubbletea](https://github.com/charmbracelet/bubbletea): A powerful little TUI framework 🏗
[gloryoo/tview](https://github.com/charmbracelet/bubbles) | [gladchinda/go-tviews](https://github.com/glaind/go-tviews)


## 6.2 Football

[tionix/football](https://github.com/ionux/football)

---

# Web-based GUI

使用 Web 技术构建界面，Go 负责业务逻辑。

## 7.1 Wails

[wailsapp/wails](https://wails.io/) - 将 Go 后端 + 前端框架结合

### 快速开始

```sh
# 安装 wails CLI
go install github.com/wailsapp/wails/v2/cmd/wails@latest

# 初始化项目
wails init -n MyApp -t vue-spa

# 运行
wails dev

# 打包发布
wails build
```

> 优点：前端开发者友好，可直接使用 Vue/React/Svelte；Go 端通过 JSON RPC 通信。

## 7.2 Flutter+Go

[flutter/flutter_for_go](https://github.com/buger/flingo) / [gonderov/flgo](https://github.com/gonderov/flgo)

利用 [Gonimogo](https://github.com/buger/gingo) + Flutter 混合开发。

