---
title: PythonGame
date: 2018-12-13 16:01:52
tags: 
    - Game
categories: 
    - Python
---

**目录 start**

1. [pygame](#pygame)
    1. [安装](#安装)

**目录 end**|_2020-04-27 23:42_|
****************************************
# pygame
## 安装
*python2 安装 pygame*
- `sudo apt install python-pygame`
  *python3 安装 pygame*
- `sudo apt install python3-dev mercurial`
- `sudo apt install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev`
  *安装一些声音的功能*
- `sudo apt install libsdl-mixer1.2-dev libimportmidi-dev`
- `sudo apt install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev`
- `sudo apt install python-numpy`

  *执行这个安装pygame 如果必要换成 pip3*
- `pip install --user hg+http://bitbucket.org/pygame/pygame`
  *我使用上面的方式安装报错，使用这个完成了安装*
- `sudo pip install pygame`

*********
`检验是否安装成功`
- `import pygame ` 查看版本 `pygame.ver`

