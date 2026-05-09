# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | PRAC counter update 增加关键 DRAM timing | Page 3, Table 1 | tRP/tRC 等参数受影响 | 高 | 这是正常 workload 开销的根源 |
| 2 | 固定 preventive refresh 和 delay period 可被攻击利用 | Page 4-5, Figure 2 | wave attack/feinting attack | 高 | 防护协议的确定性会暴露节奏 |
| 3 | Chronus 将 counter 与 data 分离并行更新 | Page 6-7, Chronus design | counter update 不再阻塞访问关键路径 | 高 | 核心性能优化 |
| 4 | Chronus 动态控制 preventive refresh 数量 | Page 7-8 | 根据风险调整刷新而非固定次数 | 高 | 减少过度刷新，也提升安全 |
| 5 | Chronus 移除 refresh 后固定 delay period | Page 7-8 | 避免 wave/feinting attack 利用窗口 | 高 | 核心安全优化 |
| 6 | 现代 NRH 下 Chronus 几乎无性能开销 | Page 10-12, Evaluation | NRH=1K 平均性能开销 <0.1% | 高 | 与 PRAC 的 5.8%+ 形成对比 |
| 7 | NRH=20 下 Chronus 仍保持可接受开销 | Page 10-12 | 平均性能 8.3%，能耗 17.9% | 高 | 面向未来低阈值的重要结果 |
| 8 | Chronus 优于多种 PRAC variant 与 Graphene/Hydra/PARA | Page 10-13 | 多方案比较 | 中 | 表明设计同时改善性能与安全 |
| 9 | 附录包含 errata/bug 修正 | Appendix B | 旧/新结果表说明修正 | 高 | 引用时必须标注版本 |
| 10 | 对 RowPress/VRD 的覆盖仍需额外研究 | Discussion/Limitations | 机制主要围绕 activation count | 中 | 低 NRH 之外还有 row-open time 和 temporal variation 问题 |
