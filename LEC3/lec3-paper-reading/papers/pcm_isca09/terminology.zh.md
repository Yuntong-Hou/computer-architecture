# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Partial writes | 部分写 | Page 8-9 | 只把 dirty cache lines/words 写入 PCM array，减少磨损。 | 是 |
| Buffer organization | 缓冲组织 | Page 5-7 | 通过 buffer width 和 rows 调节写粒度、局部性和 coalescing。 | 是 |
| Write coalescing | 写合并 | Page 6 | 多个 writes 在 buffer 中合并，减少 array writes。 | 是 |
| Endurance | 写入耐久性 | Page 3 and Page 9 | PCM cell 可可靠写入的次数。 | 是 |
