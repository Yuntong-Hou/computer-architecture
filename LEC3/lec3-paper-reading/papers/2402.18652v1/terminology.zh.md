# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Spatial Variation | 空间变化 | Page 1 | 不同物理位置 row 的脆弱性差异 | 是 |
| Read Disturbance | 读扰动 | Page 1 | 访问某些 row 对其他 row 的影响 | 是 |
| HCfirst | 首错 hammer count | Page 5-8 | 第一个 bitflip 出现所需 activation 数 | 是 |
| Bit Error Rate (BER) | 位错误率 | Page 5-8 | bitflip 数与测试位数比例 | 是 |
| Subarray | 子阵列 | Page 5-8 | DRAM bank 内共享局部电路的 row group | 是 |
| Svärd | 空间变化感知防护框架 | Page 10-12 | 根据 row vulnerability profile 调整防护强度 | 是 |
| AQUA | RowHammer 防护方案 | Page 12-15 | Svärd 评估中的 base mitigation | 中 |
| BlockHammer | RowHammer 防护方案 | Page 12-15 | 通过限制高风险访问降低攻击能力 | 中 |
| Hydra | RowHammer 防护方案 | Page 12-15 | 计数/跟踪型防护 | 中 |
| PARA | Probabilistic Adjacent Row Activation | Page 12-15 | 概率刷新相邻 row 的经典方案 | 是 |
| RRS | Reactive Refresh Scheme | Page 12-15 | 响应式刷新防护 | 中 |
