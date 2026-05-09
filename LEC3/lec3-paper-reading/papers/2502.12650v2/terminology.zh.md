# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Chronus | Chronus 防护机制 | Page 1, Page 6-9 | 改进 PRAC 的片内/控制器协同防护 | 是 |
| PRAC | Per-Row Activation Counting | Page 1-3 | DDR5 row activation tracking 机制 | 是 |
| RFM | Refresh Management | Page 1-3 | 保护刷新命令/机制 | 是 |
| Preventive Refresh | 预防性刷新 | Page 3-8 | 在 bitflip 前刷新潜在 victim row | 是 |
| Wave Attack | 波形攻击 | Page 4-5 | 利用固定刷新/延迟窗口累积扰动的攻击 | 是 |
| Feinting Attack | 佯攻攻击 | Page 4-5 | 诱导防护误判或分散资源的访问模式 | 是 |
| Delay Period | 延迟期 | Page 3-8 | RFM 后控制器/DRAM 等待窗口 | 是 |
| Counter-Data Separation | 计数器与数据路径分离 | Page 6-7 | Chronus 避免计数更新阻塞关键路径的设计 | 是 |
| NRH | RowHammer threshold | Page 4-13 | 触发 bitflip 所需 activation 数 | 是 |
