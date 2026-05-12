# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| DRAM Bender | DRAM 测试基础设施 | Page 1-2 | 可向真实 DRAM 发出任意低层命令的 FPGA 平台 | 是 |
| RowHammer | 行锤攻击/行锤现象 | Page 3, Page 9-12 | 频繁激活 aggressor row 导致邻近 victim row bit flip | 是 |
| HCfirst | 首次 bit flip 所需激活数 | Page 10-11 | 衡量 RowHammer 敏感性的指标 | 是 |
| DFI | DDR PHY Interface | Page 3 | memory controller 与 PHY 间标准化接口 | 中 |
| Bit Error Rate (BER) | 比特错误率 | Page 12 | in-DRAM AND/OR 结果错误比例 | 是 |
| RFM | Refresh Management command | Page 13 | DDR5 中触发 refresh management/TRR 的命令 | 中 |
