# Java应用 Tuning 

当遇到需要对某个Java应用性能调优，故障处理时的技能或思路汇总

![](./img/mind.drawio.svg)

`性能调优`
> [Linux 性能分析](/Linux/Base/LinuxPerformance.md)  
> [Linux 网络](/Linux/Base/LinuxNetwork.md)  
> [Java 性能调优](/Java/AdvancedLearning/JvmPerformance.md)  
> [Java GC](/Java/AdvancedLearning/JvmGC.md#Tuning)  

`不可用故障处理` **重要且紧急**

> 基础设施层：寻求方式快速搭建新的一层（例如K8S的命名空间下全部服务重建），立马切换解析或网关流量  
> JVM层：记录好后续排查分析故障现场的必要信息后（dump，日志，linux系统日志），立马重启，释放本该释放的资源或中断已经异常的流程  

