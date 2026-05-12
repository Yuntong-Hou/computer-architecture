# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Logic-in-memory array | 逻辑内存阵列 | Page 1 | 每个 storage element 附带组合逻辑的 memory array | 是 |
| Logic-enhanced cache | 逻辑增强 cache | Page 1-3 | 作为 CPU 与主存之间高速 buffer 的 logic-in-memory array | 是 |
| Sector | 扇区/数据块 | Page 1-4 | logic-in-memory operations 的块级操作单位 | 是 |
| Associative search | 关联搜索 | Page 3 | 在 sector 内按 masked equality/threshold 查找 words | 是 |
| Sector ADD | 扇区加法 | Page 4 | 两个 sectors 对应 words 并行相加 | 是 |
| Bit-slice mode | 位片模式 | Page 5 | 从许多 words 中取同一 bit slice 放入 cache 并并行处理 | 是 |
| High-level language mismatch | 高层语言不匹配 | Page 6 | 语言语义无法表达机器强指令导致其难以被编译器使用 | 是 |
