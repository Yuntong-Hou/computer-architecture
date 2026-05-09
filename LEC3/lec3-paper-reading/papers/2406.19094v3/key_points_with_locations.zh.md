# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | PRAC/RFM 是 JEDEC DDR5 中面向 RowHammer 的新工业机制 | Page 2, Background | DRAM 片内计数并通过 back-off/RFM 协同 memory controller | 高 | 标准化方案值得系统级评估 |
| 2 | PRAC 可配置为安全，但依赖 NRH >= 20 条件 | Page 3-4, Security Analysis | 论文证明任意位置 20 次访问前不 flip 时可防护 | 高 | 安全边界很低但并非无条件 |
| 3 | PRAC 增加 tRP/tRC 等关键 timing | Page 2-3 | counter update 和 RFM 协议改变命令时序 | 高 | 性能开销来自正常访问路径和防护路径 |
| 4 | 现代 NRH 下 PRAC 仍有可观性能/能耗开销 | Page 5-6, Figure 2-3 | NRH 10K/4.8K/1K 平均性能 9.9%，能耗 18.5% | 高 | 即使不是未来极低阈值，也不是零成本 |
| 5 | NRH=20 时 PRAC 开销灾难性增加 | Page 5-6, Figure 2-3 | 平均性能开销 84.7%，能耗 13x | 高 | 说明未来工艺缩小会压垮固定协议 |
| 6 | PRAC 与 Graphene/Hydra/PARA 的相对优劣依赖 NRH | Page 6, comparative evaluation | 低 NRH 下优于 PARA，现代高 NRH 下不总是优于学术方案 | 中 | 方案选择必须看阈值区间 |
| 7 | PRAC 引入 memory performance attack 面 | Page 7, Attack Analysis | adversarial pattern 可占用最多 94% throughput | 高 | 防护机制本身可能成为 DoS 放大器 |
| 8 | storage cost 需要纳入工业可行性分析 | Page 6, Figure 4 | 片内 counter 与实现成本评估 | 中 | 工业方案受面积/成本强约束 |
| 9 | RFM 减少不必要周期性刷新但增加强制暂停 | Page 2, PRAC/RFM overview | back-off 后控制器必须发 RFM | 中 | 它在 refresh 精准性和服务中断之间取舍 |
| 10 | 本文为 Chronus 提供问题定义 | Page 8 Conclusion | 结论指出需要更低开销和更抗攻击方案 | 中 | Chronus 的设计动机基本从这里来 |
