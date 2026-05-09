# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 真实 DRAM read disturbance 脆弱性存在显著空间变化 | Page 1 Abstract; Page 5-8, Figure 3-10 | 144 颗 DDR4 芯片实验 | 高 | 防护阈值不能只看全局平均 |
| 2 | 同一 subarray 内 BER 可约 2x 变化，HCfirst 可差一个数量级 | Page 1 Abstract; Page 6-7 | 细粒度 row-level 测量 | 高 | 最坏 row 会决定安全阈值，强 row 则承担过度防护成本 |
| 3 | 简单空间特征不稳定，不能可靠预测脆弱性 | Page 7-8 | 15 个 module 中仅 4 个有明显相关性 | 高 | 必须实际 profile，而不是只做启发式映射 |
| 4 | Svärd 利用 row-level profile 调整防护 aggressiveness | Page 10-12, Svärd design | 不同 row 使用不同保护强度 | 高 | 这是从表征到系统机制的核心桥梁 |
| 5 | Svärd 可与多种防护组合 | Page 12-13 | AQUA, BlockHammer, Hydra, PARA, RRS | 中 | 它更像通用优化层，而不是单一防护 |
| 6 | Svärd 显著降低已有防护性能开销 | Page 13-15, Figure 12 | 平均提升 1.23x/2.65x/1.03x/1.57x/2.76x | 高 | 当防护开销高时，空间信息价值最大 |
| 7 | adversarial pattern 下仍需保守处理弱 row | Page 15-16, Figure 13 | 攻击者可集中访问最弱 row | 高 | 安全策略必须按最弱 row 保证，而不是平均收益 |
| 8 | profile 成本和稳定性是关键挑战 | Page 16 Discussion | 温度、老化、时间变化未完全解决 | 高 | 与 VRD 论文直接关联 |
| 9 | 研究对象主要为 DDR4 | Page 4 Methodology | 144 DDR4 chips, 10 designs, 3 vendors | 中 | 对 HBM/DDR5 需要重新实验 |
| 10 | 本文强调 measurement-driven defense | Page 17 Conclusion | 结论呼吁利用真实芯片 variation | 中 | 是未来 adaptive memory reliability 的代表方向 |
