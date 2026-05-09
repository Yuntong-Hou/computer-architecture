# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Variable Read Disturbance (VRD) | 可变读扰动 | Page 1 | 同一 row 的 RDT 随时间变化 | 是 |
| Read Disturbance Threshold (RDT) | 读扰动阈值 | Page 3 | 触发 bitflip 所需 activation/access 数 | 是 |
| Temporal Variation | 时间变化 | Page 1-3 | 同一对象随时间的脆弱性变化 | 是 |
| Spatial Variation | 空间变化 | Page 2-3 | 不同位置 row 之间的差异 | 是 |
| Guardband | 安全裕量 | Page 14-16 | 在测得阈值基础上进一步保守设置 | 是 |
| SECDED | Single Error Correction, Double Error Detection | Page 14-16 | 常见 ECC 能力 | 中 |
| Chipkill-like SSC | 类 Chipkill 符号级纠错 | Page 14-16 | 更强 ECC 组织形式 | 中 |
| tAggON | aggressor row 开启时间 | Page 8-12 | RowPress 相关参数 | 是 |
| Online RDT Profiling | 在线 RDT 剖析 | Page 16-17 | 运行时更新阈值估计 | 是 |
