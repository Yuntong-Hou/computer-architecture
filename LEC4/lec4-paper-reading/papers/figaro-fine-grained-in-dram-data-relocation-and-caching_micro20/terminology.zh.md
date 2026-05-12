# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| FIGARO | 细粒度 DRAM 内重定位 substrate | Page 1-2 | 通过 global row buffer 支持 bank 内 cache-block granularity relocation | 是 |
| FIGCache | 基于 FIGARO 的 DRAM 内缓存 | Page 1-2 | 缓存 row segments 而不是完整 DRAM rows | 是 |
| Global Row Buffer (GRB) | 全局行缓冲 | Page 1-3 | 连接同一 bank 内 subarrays 与 I/O 的共享缓冲 | 是 |
| Local Row Buffer (LRB) | 本地行缓冲 | Page 1-3 | 每个 subarray 的 sense amplifier row buffer | 是 |
| Row segment | 行片段 | Page 2 | DRAM row 的小片段，可小到 cache block | 是 |
| FTS | FIGCache Tag Store | Page 11 | memory controller 中保存缓存 row segment metadata 的表 | 是 |
