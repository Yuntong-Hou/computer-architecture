# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| PRAC | Per-Row Activation Counting | Page 1-3 | DDR5 中片内跟踪 row activation 的机制 | 是 |
| RFM | Refresh Management | Page 1-3 | memory controller 触发 DRAM 执行额外保护刷新 | 是 |
| Back-off Signal | 回退信号 | Page 2 | DRAM 通知控制器暂停普通请求并执行 RFM | 是 |
| NRH | RowHammer threshold | Page 3-6 | 触发 RowHammer bitflip 所需 activation 数 | 是 |
| tRP/tRC | DRAM timing 参数 | Page 2-3 | precharge/row cycle 等关键时序 | 是 |
| Graphene | RowHammer 防护方案 | Page 6 | 计数型 memory controller defense | 中 |
| Hydra | RowHammer 防护方案 | Page 6 | 低开销 tracking defense | 中 |
| PARA | Probabilistic Adjacent Row Activation | Page 6 | 概率性相邻行刷新方案 | 中 |
| Memory Performance Attack | 内存性能攻击 | Page 7 | 利用防护机制降低系统吞吐 | 是 |
