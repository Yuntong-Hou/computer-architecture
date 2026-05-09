# Limitations and Questions

## 1. 作者明确承认的局限
- 需要端到端加速整个 read mapping，而不只是单个阶段；位置：Page 8。
- 数据移动、硬件灵活性和数据格式仍是采用障碍；位置：Page 8-9。

## 2. 论文中隐含的局限
- 本文是综述，缺少统一实验平台和公平横向复现。
- 2020 年后的 pangenome/graph reference、ultra-long reads、GPU/AI-era hardware 未完整覆盖。

## 3. 实验设计可能存在的问题
- 引用结果来自不同输入数据、硬件平台和实现，不能直接比较绝对数值。

## 4. 方法可能不适用的场景
- 对 privacy-sensitive clinical workflows，cloud/hardware offload 方案还需要数据保护机制。
- 对快速变化的 sequencing technology，固定功能 ASIC 可能过早过时。

## 5. 我阅读时应该追问的问题
- 如何定义 read mapper 的端到端吞吐指标？
- pre-alignment filter 的 false accept/false reject 如何影响 variant calling？
- GenASM 与 DRAGEN/Darwin/GenAx 的适用范围如何区分？
- 更硬件友好的 genome data format 为什么难以普及？

## 6. 后续可以继续阅读的方向
- GenASM MICRO 2020。
- GateKeeper/Shouji/SneakySnake/GRIM-Filter。
- Darwin、GenAx、DRAGEN。
