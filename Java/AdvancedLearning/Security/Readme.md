# Security
> [Java Cryptography Architecture Standard Algorithm Name Documentation for JDK 8](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html)`列出各种用途的算法`

AES 分为多个模式，ACM/GCM 会校验，防止篡改密钥，CTR并发性能好，但是没校验，CBC有 字节反转攻击的问题