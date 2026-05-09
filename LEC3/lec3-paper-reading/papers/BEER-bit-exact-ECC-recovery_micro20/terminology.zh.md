# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| On-Die ECC | 片上 ECC | Page 1 | DRAM 芯片内部不可见纠错机制 | 是 |
| BEER | Bit-Exact ECC Recovery | Page 1 | 恢复完整 on-die ECC function 的方法 | 是 |
| BEEP | Bit-Exact Error Profiling | Page 10 | 利用已知 ECC function 恢复 raw error locations | 是 |
| Parity-Check Matrix | 校验矩阵 | Page 1-2 | 定义线性 ECC function 的矩阵 | 是 |
| Miscorrection | 误纠正 | Page 2, Page 5 | ECC 在 uncorrectable pattern 下翻转非错误 bit | 是 |
| Pre-Correction Error | 纠错前错误 | Page 1 | 物理上真实发生的 raw bit error | 是 |
| Post-Correction Error | 纠错后可见错误 | Page 1 | ECC 作用后软件可观察的错误 | 是 |
| SAT Solver | 可满足性求解器 | Page 4-7 | 求解布尔约束的工具 | 是 |
| Data-Retention Error | 数据保持错误 | Page 4-5 | refresh 间隔过长导致 cell 电荷丢失 | 是 |
| SEC Hamming Code | 单错纠正 Hamming 码 | Page 1-3 | on-die ECC 可能采用的线性纠错码 | 中 |
