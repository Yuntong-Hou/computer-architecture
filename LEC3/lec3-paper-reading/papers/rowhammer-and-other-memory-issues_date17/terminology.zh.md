# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| RowHammer | 行锤击 | Page 1-2 | 反复 activate/precharge 一个 row 导致相邻 rows bit flips 的 DRAM disturbance error。 | 是 |
| Disturbance error | 扰动错误 | Page 1 | cell-to-cell interference 导致非目标 cell 被破坏。 | 是 |
| Memory isolation | 内存隔离 | Page 1-2 | 访问一个地址不应影响其他地址，是安全系统基础。 | 是 |
| PARA | Probabilistic Adjacent Row Activation | Page 3 | 以低概率刷新相邻 rows 的 RowHammer 长期缓解机制。 | 是 |
| System-memory co-design | 系统-内存协同设计 | Page 3 | controller、DRAM、系统软件共同暴露/处理可靠性问题。 | 是 |
