---
title: 图像格式
date: 2020-05-04 19:34:08
tags: 
categories: 
---

💠

- 1. [图片格式](#图片格式)
    - 1.1. [有损](#有损)
        - 1.1.1. [Webp](#webp)
        - 1.1.2. [JPEG](#jpeg)
        - 1.1.3. [HEIF](#heif)
    - 1.2. [无损](#无损)
        - 1.2.1. [BMP](#bmp)
        - 1.2.2. [PNG](#png)
        - 1.2.3. [SVG](#svg)

💠 2024-09-06 11:36:43
****************************************
# 图片格式
> [参考: 图片格式 jpg、png、gif各有什么优缺点？什么情况下用什么格式的图片呢？](https://www.zhihu.com/question/20028452)  

图片的格式，表面上是后缀不同，实际上是图片的压缩标准不一样

## 有损

### Webp
> [webp_server_go](https://github.com/webp-sh/webp_server_go)

### JPEG

JPEG文件必须以`0xFF DB`开头和以 `0xFF D9` 结尾（EOI）

### HEIF
High Efficiency Image File Format

************************

## 无损
### BMP

### PNG
> [PNG文件格式详解](https://blog.mythsman.com/post/5d2d62b4a2005d74040ef7eb/)  

- 数据标识总是IEND（49 45 4E 44），因此，CRC码也总是AE 42 60 82。 `00 00 00 00 49 45 4E 44 AE 42 60 82`

> [oxipng](https://github.com/shssoichiro/oxipng)`PNG压缩`

### SVG

> 作为网站icon `<link rel="icon" type="image/svg+xml" href="favicon.svg"/>`
