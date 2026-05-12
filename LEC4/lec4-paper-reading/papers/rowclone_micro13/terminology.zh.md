# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| RowClone | DRAM 内复制/初始化机制 | Page 1 | 通过 DRAM 内部 row buffer 和 internal bus 完成 bulk operations | 是 |
| Fast Parallel Mode (FPM) | 快速并行模式 | Page 4 | 同 subarray 内用背靠背 ACTIVATE 复制整行 | 是 |
| Pipelined Serial Mode (PSM) | 流水串行模式 | Page 5 | 跨 bank 用 internal bus 逐 cache line 流水复制 | 是 |
| Bulk Zeroing (BuZ) | 批量置零 | Page 5 | 通过复制预置零行初始化目标行 | 是 |
| FMTC | copy 造成的内存流量比例 | Page 9 | Fraction of Memory Traffic due to Copies，用于解释 forkbench 收益 | 是 |
| RowClone-Zero-Insert (RowClone-ZI) | RowClone 零插入 | Page 10 | zeroing 后同时把 zero cache lines 插入 cache，避免后续低 MLP miss | 是 |
