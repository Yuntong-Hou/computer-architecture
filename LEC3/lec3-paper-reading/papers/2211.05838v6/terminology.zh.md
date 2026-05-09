# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| DRAM Bender | DRAM Bender 测试平台 | Page 1 | FPGA-based open source DRAM testing infrastructure | 是 |
| DRAM testing infrastructure | DRAM 测试基础设施 | Page 1 | 用于直接实验真实 DRAM chip 的平台 | 是 |
| SoftMC | SoftMC | Page 1-2 | 早期 FPGA-based DRAM testing infrastructure | 是 |
| LiteX RowHammer Tester (LRT) | LiteX RowHammer Tester | Page 1-2 | 另一个开源 RowHammer 测试平台 | 是 |
| DFI | DDR PHY Interface | Page 3 | memory controller 与 PHY 之间的标准接口 | 中 |
| RowHammer | RowHammer 行锤击 | Page 3 | 高频激活 aggressor row 导致 victim row bit-flips | 是 |
| aggressor row | 攻击行/侵扰行 | Page 9 | 被反复激活的 row | 是 |
| victim row | 受害行 | Page 9 | 发生 bit-flips 的邻近 row | 是 |
| interleaving parameter T | 交替参数 T | Page 9 | 切换 aggressor 前连续 hammer 的次数 | 是 |
| HCfirst | 首次翻转 hammer count | Page 9-11 | 出现第一个 bit-flip 前所需 ACT commands | 是 |
| data pattern | 数据模式 | Page 11 | 初始化 rows 的 bit pattern | 是 |
| in-DRAM bitwise operation | DRAM 内部位运算 | Page 11-12 | 通过 DRAM analog behavior 实现 AND/OR | 是 |
| BER | 位错误率（Bit Error Rate） | Page 12 | in-DRAM operation 结果错误比例 | 是 |
| ACT / PRE | 激活 / 预充电命令 | Page 3-5 | DRAM low-level commands | 是 |
