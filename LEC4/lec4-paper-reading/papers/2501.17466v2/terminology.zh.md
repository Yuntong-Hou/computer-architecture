# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Dynamic bit-precision | 动态位精度 | Page 1-2 | 根据运行时数据实际范围选择更小 bit-width | 是 |
| Narrow values | 窄值 | Page 1-2 | 虽然存为 32/64-bit，但有效位很少的值 | 是 |
| Redundant Binary Representation (RBR) | 冗余二进制表示 | Page 2 | 用多个 digit 组合表示同一值，限制 carry propagation | 是 |
| µProgram | 微程序 | Page 1-2 | 实现一个 PUD operation 的 DRAM command sequence | 是 |
| Parallelism-Aware µProgram Library | 并行性感知微程序库 | Page 2 | 保存不同算法/表示/位宽下的 µProgram 和 cost model | 是 |
| Dynamic Bit-Precision Engine | 动态位精度引擎 | Page 2 | 在数据转置/写回过程中识别对象所需位宽 | 是 |
