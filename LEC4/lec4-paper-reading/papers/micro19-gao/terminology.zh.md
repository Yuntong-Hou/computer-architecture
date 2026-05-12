# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| ComputeDRAM | 商用 DRAM 内计算机制 | Page 1 | 通过越界 timing command sequence 在未改 DRAM 中执行计算 | 是 |
| Timing-violating command sequence | 违反时序的命令序列 | Page 3 | 故意缩短 DRAM command intervals 以触发非标准 charge sharing 行为 | 是 |
| Row copy | 行复制 | Page 3-4 | 把一行数据复制到另一行的 in-memory primitive | 是 |
| Column success ratio | 列成功率 | Page 8-10 | 某列在重复测试中产生正确结果的比例 | 是 |
| Error table | 错误表 | Page 7 | 记录坏 rows/columns，运行时避免使用 | 是 |
| Bit-serial computing | 位串行计算 | Page 6-7 | 按 bit slice 在大量元素上并行执行计算 | 是 |
