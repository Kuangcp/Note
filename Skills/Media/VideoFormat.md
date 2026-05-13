---
title: 视频格式
date: 2021-04-14 14:37:45
tags: 
categories: 
---

💠

- 1. [音视频格式](#音视频格式)
    - 1.1. [音频格式](#音频格式)
        - 1.1.1. [无损 有损 音频格式](#无损-有损-音频格式)
        - 1.1.2. [WAV](#wav)
        - 1.1.3. [FLAC](#flac)
        - 1.1.4. [MP3](#mp3)
        - 1.1.5. [HLS](#hls)

💠 2026-05-13 19:48:25
****************************************
# 音视频格式

> [digital_video_introduction](https://github.com/leandromoreira/digital_video_introduction)

## 音频格式

WAV MP3 AAC FLAC

PCM + Header = WAV(只是一层容器)

> [PCM 格式 - 認識音檔（公開版本）](https://zonble.github.io/understanding_audio_files/pcm/)  
> [audio - Convert from PCM to WAV. Is it Possible? - Stack Overflow](https://stackoverflow.com/questions/21131595/convert-from-pcm-to-wav-is-it-possible)  

### 无损 有损 音频格式
- 无损 WAV格式： 大声和小声只是二进制数值的不同（例如：静音记为 0000，大声记为 1111），但它们占用的存储空间（比特数）是完全一样的。
- MP3 / AAC / OGG： 这些格式利用了人耳听觉心理学。在完全静音或声音极度简单的片段，压缩算法会分配极少的敏感数据；在声音复杂、响度动态变化剧烈的片段，会分配更多的数据。因此，静音的 MP3 会比嘈杂的 MP3 文件体积更小。

### WAV
WAV 是一种无损、未压缩的音频格式（通常采用 PCM 编码）。

WAV 文件就像一张格子严格固定的像素画。
PCM 编码的工作方式是：无论声音大还是小，它都会以固定的频率去记录声音。
每次记录（采样），它都使用固定长度的二进制位数来存储数据。

### FLAC

### MP3

### HLS
> [RFC 8216 - HTTP Live Streaming](https://datatracker.ietf.org/doc/html/rfc8216)  


