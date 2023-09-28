---
title: 密码学
date: 2023-09-08 11:54:36
tags: 
categories: 
---

**目录 start**

1. [密码学](#密码学)
1. [古典密码学](#古典密码学)
    1. [凯撒密码](#凯撒密码)
    1. [简单替换密码](#简单替换密码)
    1. [多表加密](#多表加密)
    1. [一次性密码本](#一次性密码本)
1. [现代密码学](#现代密码学)
    1. [编码](#编码)
    1. [伪随机数生成器](#伪随机数生成器)
    1. [对称密码](#对称密码)
        1. [DES](#des)
        1. [AES](#aes)
        1. [分组密码和流密码](#分组密码和流密码)
        1. [分组密码的模式](#分组密码的模式)
    1. [公钥密码](#公钥密码)
        1. [RSA](#rsa)
            1. [生成密钥对](#生成密钥对)
            1. [模拟完整的RSA过程](#模拟完整的rsa过程)
            1. [对RSA的攻击](#对rsa的攻击)
    1. [混合密码系统](#混合密码系统)
    1. [散列函数](#散列函数)
        1. [MD4 MD5](#md4-md5)
        1. [SHA-1](#sha-1)
        1. [RIPEMD-160](#ripemd-160)
    1. [消息认证码](#消息认证码)
    1. [数字签名](#数字签名)
        1. [签名与验签](#签名与验签)
    1. [证书](#证书)
    1. [密钥](#密钥)
    1. [随机数](#随机数)
1. [集大成者](#集大成者)
    1. [PGP](#pgp)
    1. [SSL TLS](#ssl-tls)
1. [扩展](#扩展)

**目录 end**|_2023-09-22 19:13_|
****************************************
# 密码学
> [wikipedia](https://zh.wikipedia.org/wiki/%E5%AF%86%E7%A0%81%E5%AD%A6)


> 基础概念：
- 此处的密码不等同于常见的信息系统中的用户 **"登录密码"**，严格意义上讲`password`只能称为口令，作为信息系统认证的一部分，密码是指信息的加解密等完整生态。
- 明文(plaintext) 加密(encrypt) 得到 密文(ciphertext)，解密则是逆向过程
    - 加密 解密算法合称 密码算法，密码算法中通常都需要密钥（key）
- 对称密码 和 公钥密码：保证数据的机密性
    - 对称密码即加密和解密使用同一个密钥，公钥密码则是加密和解密使用不同的密钥（分为公钥和私钥）。还有混合密码系统则是结合两种方式一起使用
- hash函数： 为了保证数据的完整性，即数据没有被篡改过。
- 消息认证码： 保证完整性并提供认证机制，例如身份证中的校验位
- 数字签名：保证完整性，提供认证机制，防止否认
- 伪随机数生成器： 模拟产生随机数的算法。如果生成随机数的算法设计不好，则攻击者容易推测出密钥
- 隐写术：将消息藏入明文，密码隐藏的是明文，隐写术隐藏的明文消息
    - 计算机中的数字水印就使用了该技术设计，例如将需要嵌入的消息加密得到密文再通过隐写术藏到载体上（图片，视频，音频），达到签名，溯源的目的
- 社会工程学（social engineering）攻击: 安全系统内的短板在于人类自身。
- 密钥加密密钥（Key Encrypting Key， KEK）

最佳实践：
- 不要使用保密的密码算法，而应该使用市面上公开的高强度的密码算法
- 使用低强度的密码比不进行任何加密更危险
- 任何密码总有一天都会被破解，重点在于攻击的投入产出比
- 密码只是信息安全的一部分
- 低强度加密算法对明文的多轮加密的安全性等同于单次加密

参考：
- [可汗学院： 计算机科学-密码学](https://zh.khanacademy.org/computing/computer-science/cryptography)
- 《图解密码技术》


************************

# 古典密码学
> [wikipedia](https://zh.wikipedia.org/wiki/%E5%8F%A4%E5%85%B8%E5%AF%86%E7%A2%BC)  

> [异或与一次性密码本](https://zh.khanacademy.org/computing/computer-science/cryptography/ciphers/a/xor-and-the-one-time-pad)`异或运算后，原始信息无法辨别了`

## 凯撒密码
凯撒密码是一种移位密码，将明文按固定偏移量将明文转换为密文。

例如：明文 you 经过3个移位得到密文brx。
缺陷：
- 英文语句中每个字母的出现频率是有固定的差异，可以从密文的字母出现频率对照原始字母的频率从而推算出偏移量
- 密钥只有26种，密钥空间极小，可以暴力计算（又称 穷举搜索）所有的密钥解密得到明文

## 简单替换密码
将原始的26个字母，打乱后得到替换表，将明文中的字母一一对应并替换，从而将明文加密为密文

改进点： 密钥空间从26种扩大到 26！种
缺陷： 
- 同样可以通过字母频率分析，结合单词组（类似数独的解法），推算出替换表
- 密文越长越容易破解（给出了更多的信息）

## 多表加密
将一个单词设置为密钥，单词内的每个字符的自然序循环使用作为偏移量对明文进行加密

例如：明文 how are you 密钥 yes（25，5，19） 计算得到密文：__
缺陷：密钥一般短于明文，还是能得到偏移的规律

## 一次性密码本
> 一次性密码本(one time pad)是一种绝对无法被破译的密码  
> 一次性密码本由 G.S.Vernam 在1917年提出 并由 香农(C.E.Shannon) 在1949年数学方法证明，它是无条件安全的(unconditionally secure)，在理论上是无法破译的(theoretically unbreakable)。

设置一个与明文长度一致的字符串作为密码本，对明文每个字母按密码本对应的字母的自然序进行移位。

如果在计算机的范畴，一次性密码本则是与明文编码后二进制串等长的二进制串。而且明文二进制串通过和密码本异或运算得到密文（且和或会保留大量的明文信息特征）。

例如： 明文 how are you 密钥 uwoiufpqx 计算得到密文：__

一次性密码本是无法破译的： 因为即使拿到了密文，穷举了密钥，得到明文，但是会发现得到多个情况的明文，无法判断哪个明文才是这个密文真正要携带信息的明文。

即使理论上是无法破译的，但是在实用性上几乎是无法使用： 密钥每次都是需要和密文一起发送给接受方，密文中的信息才能有效被传达，然后矛盾点来了，如何安全的传输与明文等长的密钥。

一次性密码本和明文长度一样，是否可以压缩。答案：否，因为压缩过程是对重复序列的再编码，得到短序列，从而实现压缩，但是一次性密码本是随机的，不包含任何冗余重复序列。

************************

# 现代密码学

## 编码
现代密码学都是建立在计算机的基础上，因此需要编码（将 文字，图像，音视频 等 转换成比特序列）。


************************

## 伪随机数生成器
计算机领域没有真随机事件，所以只能称为伪随机数，但是可用利用外部的信息熵来提高随机性。  

需要具备的性质：
- 事实上不可能根据过去的随机数序列来预测未来的随机数序列。

常见的编程语言中random的最简单实现都是固定序列的伪随机数生成器(如果使用此生成器计算的密钥做加密，容易被攻击者攻破)  
改进版则是使用操作系统中随机数设备`/dev/urandom`（采集硬件上的信息熵，电压，温度，键盘鼠标等输入事件）来生成不固定序列

伪随机数生成算法

线性同余 （linear congruential generator, LCG）： `X[n+1] = (a·X[n] + c) mod m`

************************

## 对称密码

### DES
Data Encryption Standard 是 1977年美国联邦信息处理标准中所采用的对称密码。 

DES是一种将64比特的明文加密成64位比特的密文的对称加密算法(分组密码的一种)，密钥长度为64位： 56位+错误检验的8比特（每隔7位设置一位）  
使用Feistel网络作为基本结构，经过多轮分组加密得到密文（轮函数和网络结构解耦）。详细过程参考书籍《图解密码技术》

`三重DES`
加密过程：明文 密钥1加密 密钥2解密 密钥3加密 得到密文。 解密过程相反： 密钥3解密 密钥2加密 密钥1解密  
优点：增加了DES算法的强度（加大了密钥空间）， 缺陷： 计算量大

> DES 密钥空间是 2^56种， 三重DES则是 2^168种。

### AES 
Advanced Encryption Standard。在全世界范围进行公开竞选， 有15个算法进入候选范围，最终 Rijndael 获胜成为AES

同为分组加密算法，分组长度为128比特，密钥长度可选（128，192，256位），使用SPN结构进行多轮加密。 详细过程参考书籍《图解密码技术》  
而且加密过程的步骤可以并行计算，性能较DES也更好。  
Rijndael算法背后是严谨的数学论证：明文到密文的计算过程全部可以用数学公式来表达。  

> AES-CCM
- AES算法采用CTR/CBC模式

> AES-GCM 
- AES算法采用CTR模式，并带有GMAC消息认证码。能防篡改（认证码实现） [wiki: GCM](https://en.wikipedia.org/wiki/Galois/Counter_Mode)

### 分组密码和流密码
分组密码(block cipher)是指每次只能处理固定长度数据的一类密码算法。例如 DES，AES等
流密码(stream cipher)是对数据流连续处理的一类密码算法。

分组密码处理完一个分组就结束了，因此不需要内部状态来记录维护加密的进度，反之流密码是对一串数据流进行连续处理，是有状态的。

> 由于明文不可能总是密钥的整数倍长，因此需要对最后一个明文分组进行数据填充(padding)达到对齐

### 分组密码的模式
> 分组密码算法需要对分段的明文进行迭代加密，迭代的方法称为模式。

《实用密码学》中指出，推荐使用CBC模式和CTR模式。

- ECB：Electronic CodeBook mode 电子密码本模式
- CBC：Cipher Block Chaining mode 密码分组链接模式
- CFB：Cipher FeekBack mode 密文反馈模式
- OFB：Output FeedBack mode 输出反馈模式
- CTR：CounTeR mode 计数器模式

ECB模式是按序迭代，也是最容易有安全漏洞的算法，通常不被实际使用。
- 因为ECB模式下，明文分组和密文分组是按序一一对应的，那理论上可以通过对密文分组的 复制，调序，剪切 等操作，从而达到篡改明文的目的。
- 但是如果使用消息认证码，则可以发现密文被篡改

CBC模式相较于ECB，在每个明文分组加密为密文分组前，都需要拿前一个密文分组对当前明文分组做异或（XOR）运算。第一个分组则需要一个初始化向量(IV initialization vector)做异或运算。 每个分组依赖前一个分组像一个链条，因此得名。

CFB，OFB和CBC类似都需要IV，只是当前明文分组的处理方式不同。

************************

## 公钥密码
> 非对称加密

类比场景： 
- 对称加密，传统房门的锁需要同钥匙来开关门，则密钥是相同的：钥匙；
- 公钥加密：超市中的付费购物车，需要投币开锁，推入前一个购物车后完成加锁，则密钥是不同的，加锁密钥：前一个购物车，解锁密钥：硬币。

相较于对称密码，安全性大为加强，但是目前的公钥密码算法性能只有对称密码算法的几百分之一。

EIGamal算法利用了mod N 下求离散对数的难度（但是密文长度是明文的两倍），RSA利用了质因数分解的难度，Rabin算法利用了mod N下求平方根的难度

椭圆曲线密码 (Elliptic Curve Cryptosystems, ECC), 通过将椭圆曲线上特定点进行特殊的乘法运算来实现，利用了乘法运算的逆运算的困难度。
特点是所需密钥长度比RSA短。

### RSA
> [模运算](/Skills/CS/BasicOperator.md#模运算)`RSA公私钥理论基础`

RSA 可以被用于公钥密码和数字签名。
在RSA中，明文，密钥和密文都是数字。

加密： `密文 = 明文^E mod N` 元组(E,N) 是公钥
解密： `明文 = 密文^D mod N` 元组(D,N) 是密钥

#### 生成密钥对

1. 求 N
    - 首先准备两个大质数 p 和 q : `N = p * q` **p和q如果太小密码容易被破解，太大的话加解密时间会很长**
2. 求 L (中间值)
    - `L = lcm(p-1, q-1)` **lcm 最小公倍数**
3. 求 E
    - `1 < E < L` 且 `gcd(E,L)=1` **E和L互质**
4. 求 D
    -  `1 < D < L` 且 `E * D mod L = 1`

> 判断质数的方法： 费马测试和米勒·拉宾测试等。  
> 计算gcd最快速的方法则是欧几里得算法（辗转相除法）。  

#### 模拟完整的RSA过程

模拟密钥生成过程以及加解密过程：
1. 求 N， 准备质数 p = 17 q = 19, N = 323 **注意：实际使用中pq的长度在512位以上，N的长度在1024位以上**
2. 求 L， lcm(16,18) = 144
3. 求 E， gcd(E,L)=1 有很多数满足条件，有和L互质的合数，也有质数。假设选择5作为E
4. 求 D， 5 * D mod 144 = 1 计算出D=29时可满足

此时得到公钥 (E,N) = (5,323) 私钥 (D,N)=(28,323)

> 注意明文必须是小于N的数，如果大于N就会有多个解，造成解密数据不等于明文的情况  

- 加密：明文^E mod N = 123^5 mod 323 = 225
- 解密：明文^D mod N = 225^29 mod 323 = 123

#### 对RSA的攻击

攻击者拥有的信息：密文， E， N，不知道的信息：明文， D， p, q, L

1. 密文求解明文： 密文=明文^E mod N , 对明文的求解是求离散对数，成本很大
2. 暴力求解D，由于pq及N位数很长，E和D长度和N差不多，暴力迭代求解D的成本很大
3. 对N进行质因数分解求解pq，从而求解D。目前未发明对大整数的质因数分解高效算法，成本很大
4. 中间人攻击 mitm attack:
    - 不破解RSA加密算法本身，而是在通信过程中通过对两端的公钥替换，从而窃听两端的通信
    - A <=> B 变成了 A <=> M <=> B
    - 为了防御该攻击需要使用公钥的证书来让对端确保接受到的公钥是自己端的。

************************

## 混合密码系统
> PGP, SSL/TLS都使用了混合密码系统。

1. 用对称密码加密消息
2. 通过伪随机数生成器生成对称密码中使用的会话密钥
3. 用公钥密码加密会话密钥
4. 从混合密码系统外部赋予公钥（CA）

密钥强度：通常公钥密码的强度应该要高于对称密码，如果对称密码被破译只会泄漏本次通信内容，如果公钥密码破译，所有使用该供公钥加密的通信内容都会被破译

************************

## 散列函数
散列函数也称消息摘要函数，哈希函数, 信息指纹，常用于保障信息的完整性，但是无法保障信息的真实性。

> 需要注意 散列函数不是加密算法，因为散列值无法解密为原文。

由于此类函数的特点是 输入消息 输出散列值，具有单向性特点，也称单向散列函数。  
输入的消息为二进制序列，长度可以任意长，计算输出的散列值是定长，例如SHA-1输出散列值为20byte。  

单向散列函数的性质：
- 依据任意长度的消息计算出定长的散列值
- 能快速计算出散列值
- 消息不同散列值也完全不同
    - 不同的消息得到了相同的散列值被称为碰撞 collision，理论上无法避免（因为散列函数的输入端信息量大于输出端），但是散列函数要保障很难被人为构造出碰撞，即强抗碰撞性
- 函数必须具备单向性。即无法通过散列值反推出原始消息的性质。

> 实际应用
- 监测下载的软件是否被篡改
- 基于口令的加密（Password Based Encryption）。PBE的原理是将口令(Password)和盐(salt 通过伪随机数生成器生成的随机值)混合后计算其散列值，将这个散列值作为加密的密钥。
    - 加盐是为了防止针对口令的散列字典（又称彩虹表）攻击
- 消息认证码： 将发送方和接受方之间的共享密钥和消息（明文的分片）混合计算后的散列值，可以检测并防止通信过程中的错误，篡改，伪装。在SSL/TLS中也有应用
- 数字签名： 是现实社会中签名和盖章这样的行为在数字世界的实现。通常不会对完整消息加数字签名，而是先计算出内容的散列值，再对散列值加数字签名
- 一次性口令： one-time password. 通常用于服务端对客户端的合法性认证。

### MD4 MD5
MD4 是由Rivest于1990年设计，能产生128bit的散列值，之后Dobbertin提出寻找MD4散列碰撞的方法，已经不安全了。
MD5 是由Rivest于1991年设计，能产生128bit的散列值， 但是MD5的强抗碰撞性已经被攻破，也已经不安全了。

### SHA-1
SHA-1 SHA-256 SHA-384 SHA-512

SHA-1 是由 NIST（National Institute of Standards and Technology）设计，能产生160bit的散列值，
1993年发布的是SHA，1995年发布的SHA-1，SHA-1处理的消息长度存在上限，但该理论值接近于264bit，实际使用时不容易遇到问题。


### RIPEMD-160

************************

## 消息认证码

用于判断消息的完整性和真实性

************************

## 数字签名
散利函数和公钥密码组合而成

### 签名与验签
> 常见于外部接口的签名验证，安全防护

[企点： 消息加解密指引](https://api.qidian.qq.com/wiki/doc/open/epko939s7aq8br19gz0i)`对接企点API对消息的加解密`

## 证书
公钥和数字签名组合而成

1. 基本概念：
    1. `CA (Certificate Authority)`  证书授权中心，是数字证书发放和管理的机构
    1. `根证书` 根证书是CA认证中心给自己颁发的证书,是信任链的起始点。安装根证书意味着对这个CA认证中心的信任。
    1. `数字证书` 数字证书颁发过程一般为：
        1. 用户首先产生自己的密钥对，并将公共密钥及部分个人身份信息传送给认证中心。
        1. 认证中心在核实身份后，将执行一些必要的步骤，以确信请求确实由用户发送而来。
        1. 认证中心将发给用户一个数字证书，该证书内包含用户的个人信息和他的公钥信息，同时还附有认证中心的签名信息。

- [Githhub:mkcert](https://github.com/FiloSottile/mkcert)`签发证书工具`

## 密钥

## 随机数

************************

# 集大成者
## PGP

## SSL TLS
> [SSL/TLS协议运行机制的概述](http://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)
> [SSL，TLS，HTTPS](https://www.cnblogs.com/songhan/archive/2012/08/01/2617970.html)


************************

# 扩展

电子投票
电子货币
盲签名 blind signature
零知识证明 zero knowledge proof