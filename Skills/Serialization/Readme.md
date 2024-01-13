# 序列化

- [Github : Protobuf](https://github.com/google/protobuf)  
- [Hessian](http://hessian.caucho.com/)

## TLV 
TLV 即 Tag - Length - Value。Tag 作为该字段的唯一标识，Length 代表 Value 数据域的长度，最后的 Value 便是数据本身

HTTP协议中有使用到类似的设计思想(在Header部分会声明Body的Length)

