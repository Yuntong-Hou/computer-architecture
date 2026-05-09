# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| RowHammer | RowHammer 行锤击 | Page 1 | 高频激活 aggressor rows 导致 nearby victim rows bit-flips | 是 |
| aggressor row | 侵扰行 | Page 1 | 被反复访问/hammer 的 DRAM row | 是 |
| victim row | 受害行 | Page 1 | 因邻近行被 hammer 而发生 bit-flip 的 row | 是 |
| bit-flip | 位翻转 | Page 1 | DRAM cell 数据从 0 到 1 或 1 到 0 的错误 | 是 |
| RowHammer threshold | RowHammer 阈值 | Page 1 | 触发 bit-flip 所需的 aggressor activation 次数 | 是 |
| TRR | Target Row Refresh | Page 2 | 工业界用于刷新 potential victim rows 的 RowHammer mitigation umbrella term | 是 |
| pTRR | pseudo Target Row Refresh | Page 2 | memory controller 侧 victim row refresh 机制 | 中 |
| TRRespass | TRRespass | Page 2-3 | many-sided RowHammer attack，绕过 TRR | 是 |
| Revisiting RowHammer | Revisiting RowHammer | Page 3 | 大规模真实芯片实验，证明 RowHammer worsening | 是 |
| RFM | Refresh Management | Page 3 | DDR5 中辅助 in-DRAM mitigation 的命令/机制 | 是 |
| system-memory cooperation | 系统-内存协同 | Page 2, Page 6 | 系统侧与 DRAM 侧共同设计 RowHammer defenses | 是 |
| security by obscurity | 依赖隐藏细节的安全 | Page 3 | TRR 不公开实现但仍被逆向/绕过 | 中 |
