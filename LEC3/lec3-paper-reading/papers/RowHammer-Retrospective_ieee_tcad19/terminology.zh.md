# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| RowHammer | 行锤击 | Page 1 | 反复访问 aggressor row 导致相邻 victim row bit flips 的 DRAM disturbance 现象。 | 是 |
| Disturbance error | 扰动错误 | Page 1-3 | 电路组件间干扰导致非目标 cell 状态改变。 | 是 |
| PARA | Probabilistic Adjacent Row Activation | Page 4 | 关闭 row 时以低概率刷新相邻行的防御机制。 | 是 |
| Memory isolation | 内存隔离 | Page 2-4 | 访问一个地址不应影响其他地址的数据，是系统可靠性和安全的基础。 | 是 |
| Targeted refresh | 定向刷新 | Page 8 | 只刷新被认为可能受 hammering 影响的相邻行。 | 是 |
