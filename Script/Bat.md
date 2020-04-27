---
title: Dos
date: 2018-12-15 12:10:06
tags: 
    - DOS
categories: 
    - Windows
---

**目录 start**

1. [Bat](#bat)
    1. [Tips](#tips)
    1. [基础命令](#基础命令)
        1. [常用基础](#常用基础)
    1. [基础语法](#基础语法)
        1. [变量](#变量)
    1. [服务](#服务)
    1. [实用性脚本](#实用性脚本)

**目录 end**|_2020-04-27 23:42_|
****************************************
# Bat

## Tips
- windows下使用VmWare创建的虚拟机如果报错
    - 就找到虚拟机目录下vmx后缀的文件  用记事本打开，手动找到vmci0.present=‘TRUE’,把true改为false 即可。

## 基础命令
### 常用基础

cd 路径 ： 跳转到本盘符下的路径 
cd /d 路径  ：跳转到别的盘符下的路径  
"盘符：” ： 切换盘符  
netstat -an ：查看开启了哪些端口  
netstat -v : 查看正在进行的工作  
netstat -ano ：查看端口占用   


## 基础语法
### 变量
- [参考博客](http://www.jb51.net/article/49196.htm)

## 服务

`记一次在windows上配置服务`
- [将jar程序配置为服务](http://developer.51cto.com/art/201411/456795.htm)
- [将bat后台运行，隐藏黑窗口](http://blog.csdn.net/carl6148/article/details/7905549)
- [按端口找到进程然后杀掉](https://zhidao.baidu.com/question/1430216669082941259.html)
    - [手动方式](https://www.cnblogs.com/moodlxs/p/4145384.html)

*******************************************
## 实用性脚本
- [本人写的bat](https://github.com/Kuangcp/Script/tree/master/bat)`因为后期转用Linux了,所以就没有写了`
    - 其中用的多的就是服务管理的脚本 
