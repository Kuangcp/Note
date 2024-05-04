# Java相关缓存框架

> [缓存系列专栏](https://github.com/veezean/JavaBasicSkills?tab=readme-ov-file#%E7%BC%93%E5%AD%98%E7%B3%BB%E5%88%97%E4%B8%93%E6%A0%8F)


如果只是本地简单、少量缓存数据使用的，选择Caffeine；  
如果本地缓存数据量较大、内存不足需要使用磁盘缓存的，选择EhCache；  
如果是大型分布式多节点系统，业务对缓存使用较为重度，且各个节点需要依赖并频繁操作同一个缓存，选择Redis。  
