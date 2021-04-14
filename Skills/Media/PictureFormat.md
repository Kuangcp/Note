---
title: 图像格式
date: 2020-05-04 19:34:08
tags: 
categories: 
---

**目录 start**

1. [图片格式](#图片格式)
    1. [压缩](#压缩)
        1. [Webp](#webp)
        1. [JPEG](#jpeg)
        1. [HEIF](#heif)
    1. [无损](#无损)
        1. [BMP](#bmp)
        1. [PNG](#png)
        1. [SVG](#svg)

**目录 end**|_2021-02-02 15:04_|
****************************************
# 图片格式
> [参考: 图片格式 jpg、png、gif各有什么优缺点？什么情况下用什么格式的图片呢？](https://www.zhihu.com/question/20028452)  

图片的格式，表面上是后缀不同，实际上是图片的压缩标准不一样

## 压缩

### Webp

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

### SVG

> 作为网站icon `<link rel="icon" type="image/svg+xml" href="favicon.svg"/>`