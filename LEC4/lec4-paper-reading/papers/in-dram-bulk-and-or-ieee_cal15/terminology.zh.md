# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Triple-row activation | 三行同时激活 | Page 2 | 同时把三行 cell 接到 bitline，让 sense amplifier 输出多数值 | 是 |
| Sense amplifier | 感测放大器 | Page 1-2 | DRAM 中把微小 bitline 电压偏移放大为 0/1 的电路 | 是 |
| RowClone-FPM | RowClone 快速并行模式 | Page 2 | 同 subarray 内通过背靠背 ACTIVATE 复制整行 | 是 |
| Bulk bitwise operation | 批量按位操作 | Page 1 | 对 KB/MB 级 bitvector 执行 AND/OR | 是 |
| FastBit | bitmap index 库 | Page 4 | 论文用来估算真实 range query 收益的开源 bitmap index 实现 | 是 |
