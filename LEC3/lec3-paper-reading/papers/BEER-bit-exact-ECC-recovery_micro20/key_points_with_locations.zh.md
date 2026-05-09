# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | on-die ECC 隐藏 pre-correction errors | Page 1, Introduction | ECC metadata 对系统不可见，post-correction 位置可能不匹配物理错误 | 高 | 可靠性研究的观测层被扭曲 |
| 2 | 同类型 ECC code 的不同 function 会产生不同可见错误分布 | Page 1-2, Figure 1 | 三个 SEC Hamming functions 的 post-correction 分布不同 | 高 | 知道 code 类型不够，必须知道 parity-check matrix |
| 3 | BEER 不需要硬件工具、先验知识或 syndrome/parity | Page 1-2, Contributions | 只观察 software-visible post-correction patterns | 高 | 方法的实际价值所在 |
| 4 | BEER 利用 crafted retention errors 和 miscorrections | Page 4-6, Section 4 | CHARGED patterns + SAT constraints | 高 | 物理错误特性和编码理论结合 |
| 5 | BEER 在 80 颗 LPDDR4 chips 上应用 | Page 2-3, Section 5 | 三大厂商芯片实验 | 高 | 证明不是纯理论 |
| 6 | 缺少真实 ground truth 且不能公开 ECC functions | Page 2-3, Section 2.1/5 | 厂商保密限制 | 高 | 阅读时必须注意验证限制 |
| 7 | 仿真验证覆盖 115,300 个 SEC Hamming codes | Page 2-3, Section 6 | codeword 4-247 bits | 高 | 这是正确性主证据 |
| 8 | SAT runtime 可接受但不轻量 | Page 10, Figure 6 | 128-bit median 57.1h/6.3GiB；247-bit 最多 62h/11.4GiB | 中 | 离线一次性可接受，在线不可行 |
| 9 | BEEP 利用已知 ECC function 推断 bit-exact raw errors | Page 10-12, Figure 7-9 | pre-correction locations recovered from miscorrections | 高 | BEER 的直接实用例子 |
| 10 | BEER 可扩展到其他 linear block code memory devices | Page 13, Future Work | Flash/STT-MRAM/PCM/RRAM 等可能扩展 | 中 | 思想可迁移，但需适配错误模型 |
