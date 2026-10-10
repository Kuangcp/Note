---
title: 图像格式
date: 2020-05-04 19:34:08
tags: 
categories: 
---

💠

- 1. [图片格式](#图片格式)
    - 1.1. [有损](#有损)
        - 1.1.1. [JPEG](#jpeg)
        - 1.1.2. [WebP](#webp)
        - 1.1.3. [HEIF](#heif)
        - 1.1.4. [AVIF](#avif)
        - 1.1.5. [JPEG XL](#jpeg-xl)
    - 1.2. [无损](#无损)
        - 1.2.1. [PNG](#png)
        - 1.2.2. [BMP](#bmp)
        - 1.2.3. [GIF](#gif)
        - 1.2.4. [TIFF](#tiff)
    - 1.3. [矢量](#矢量)
        - 1.3.1. [SVG](#svg)
        - 1.3.2. [PDF](#pdf)
        - 1.3.3. [EPS](#eps)
        - 1.3.4. [AI](#ai)
    - 1.4. [RAW](#raw)
        - 1.4.1. [CR3](#cr3)
        - 1.4.2. [NEF](#nef)
        - 1.4.3. [ARW](#arw)
        - 1.4.4. [DNG](#dng)
        - 1.4.5. [RAF](#raf)
    - 1.5. [动画](#动画)
        - 1.5.1. [GIF 动画](#gif-动画)
        - 1.5.2. [APNG](#apng)
        - 1.5.3. [WebP 动画](#webp-动画)
        - 1.5.4. [AVIF 动画](#avif-动画)
    - 1.6. [专业/中间格式](#专业中间格式)
        - 1.6.1. [TIFF容器](#tiff容器)
        - 1.6.2. [PSD](#psd)
        - 1.6.3. [EXR](#exr)
        - 1.6.4. [DDS](#dds)

💠 2026-10-10 14:08:50
****************************************
# 图片格式

> [参考: 图片格式 jpg、png、gif各有什么优缺点？什么情况下用什么格式的图片呢？](https://www.zhihu.com/question/20028452)  

图片的格式，表面上是后缀不同，实际上是图片的压缩标准不一样。

## 有损

### JPEG
> JPG（另一种后缀写法）是最通用、兼容性最好的有损格式。

JPEG文件必须以 `0xFF DB` 开头和以 `0xFF D9` 结尾（EOI）。

### WebP
> [webp_server_go](https://github.com/webp-sh/webp_server_go)

Google 出品，有损/无损/动画三合一。支持静态和动图。

### HEIF
High Efficiency Image File Format，Apple 生态主推，本质是一种容器格式（内部可封装 HEVC 编码图像）。

### AVIF
下一代格式，基于 AV1 编码，压缩率优于 WebP/JPEG，支持 HDR。

### JPEG XL
下一代格式，有损/无损统一，压缩率和画质均优于 JPEG。

## 无损

### PNG
> 最通用，支持透明。 [PNG文件格式详解](https://blog.mythsman.com/post/5d2d62b4a2005d74040ef7eb/)  

- 数据标识总是IEND（49 45 4E 44），因此，CRC码也总是AE 42 60 82。 `00 00 00 00 49 45 4E 44 AE 42 60 82`

> [oxipng](https://github.com/shssoichiro/oxipng)`PNG压缩`

### BMP
Windows 原生格式，无压缩，文件体积大。

### GIF
无损但限 256 色，已基本被淘汰（动画用途见 [动画](#动画)）。

### TIFF
可无损可有损，打印/专业领域常用（详见 [专业/中间格式](#专业中间格式)）。

## 矢量

### SVG
Web 矢量标准。
> 作为网站icon `<link rel="icon" type="image/svg+xml" href="favicon.svg"/>`

### PDF
文档矢量格式，跨平台。

### EPS
印刷矢量格式。

### AI
Adobe Illustrator 工程文件。

## RAW
私有/相机原始格式，保留传感器最原始的感光数据，便于后期调整白平衡、曝光等。

### CR3
佳能（Canon）。Windows平台可以安装 DPP Digital Photo Professional 将CR3转换为JPG。

Linux平台可以选择 darktable，开多线程 效率比Windows高10倍

```sh
docker run --name canon -it  -v ~/test/cannon:/data ubuntu:22.04
apt-get update && apt-get install -y darktable parallel

find . -maxdepth 1 -name '*.CR3' | parallel -j 4 darktable-cli {} {.}.jpg --apply-custom-presets false --core --library :memory: --conf opencl=off --conf plugins/imageio/format/jpeg/quality=90
```

- parallel -j 4 四个线程并发
- --library :memory:  纯内存，避免磁盘db锁
- --conf opencl=off 禁用显卡加速
- --conf plugins/imageio/format/jpeg/quality=90 画质控制滑块。数值可以设置为 5 到 100 之间的任意整数。
    - 90（推荐） 网络分享、屏幕观看的最优比例，肉眼几乎无法分辨与 100% 的区别
    - 85（极致压缩） 如果你需要追求更小的空间占用，可以调至 85

### NEF
尼康（Nikon）。

### ARW
索尼（Sony）。

### DNG
Adobe 开放的通用 RAW 格式。

### RAF
富士（Fujifilm）。

## 动画

### GIF 动画
经典，限 256 色。

### APNG
PNG 动画扩展，支持全彩和透明。

### WebP 动画
体积小，兼容性较好（见 [WebP](#webp)）。

### AVIF 动画
基于 AV1，体积和画质优势明显（见 [AVIF](#avif)）。

## 专业/中间格式

### TIFF容器
印刷、扫描领域常用，可无损可有损，支持多页和图层。

### PSD
Photoshop 工程文件，支持图层、蒙版等编辑信息。

### EXR
电影级 HDR 格式，浮点高动态范围。

### DDS
游戏纹理格式，支持 GPU 直接压缩（如 DXT/BC 系列）。
