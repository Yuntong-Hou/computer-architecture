# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| GenASM | GenASM 框架 | Page 1-2 | 面向 genome ASM 的算法/硬件框架 | 是 |
| Approximate String Matching (ASM) | 近似字符串匹配 | Page 1-3 | 允许 edits 的字符串匹配 | 是 |
| Bitap | Bitap 算法 | Page 2-4 | bitvector-based ASM algorithm | 是 |
| GenASM-DC | distance calculation 单元 | Page 5 | 生成 bitvectors 并计算 edit distance | 是 |
| GenASM-TB | traceback 单元 | Page 6 | 从 bitvectors 恢复 alignment/CIGAR | 是 |
| Systolic Array | 脉动阵列 | Page 7 | 高并行硬件结构 | 是 |
| DC-SRAM/TB-SRAM | DC/TB 专用 SRAM | Page 7-8 | 存储中间 bitvectors，降低带宽 | 是 |
| CIGAR String | CIGAR 字符串 | Page 3, Page 6 | 表示 alignment edits 的格式 | 中 |
| False Accept Rate | 错误接受率 | Page 12 | dissimilar sequences 被误认为相似 | 是 |
| False Reject Rate | 错误拒绝率 | Page 12 | similar sequences 被误丢弃 | 是 |
| 3D-Stacked Memory | 3D 堆叠内存 | Page 8 | logic layer + vault parallelism | 是 |
