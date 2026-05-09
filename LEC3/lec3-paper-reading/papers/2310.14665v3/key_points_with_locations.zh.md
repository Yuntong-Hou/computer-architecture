# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | HBM2 也会受到 RowHammer 读扰动影响 | Page 1, Abstract; Page 4-5, Figure 4-5 | 6 颗 HBM2 chip 全部可诱发 bitflip | 高 | HBM 的封装和带宽优势不等于读扰动可靠性更强 |
| 2 | 脆弱性在 chip 与内部结构之间高度不均匀 | Page 5-7, Figure 6-10 | channel、pseudo-channel、bank、row 位置均表现不同 | 高 | 防护不能只设置全局统一阈值 |
| 3 | bank 中端/末端 row 更抗扰动 | Page 7, Figure 8 | 不同 row 位置 HCfirst/BER 分布有系统性差异 | 中 | 可能反映物理布局、sense amplifier 或边界结构差异 |
| 4 | 第一个 bitflip 后，后续 bitflip 往往更容易出现 | Page 8, Figure 11-12 | 对前 10 个 bitflip 的 hammer count 做序列分析 | 高 | 单看 HCfirst 可能低估多 bit error 风险 |
| 5 | RowPress 显著放大读扰动 | Page 9-10, Figure 14-15 | tAggON=35.1us 时 HCfirst 平均比 29ns 小 222.57x | 高 | 仅跟踪 activation count 的防护会漏掉 row-open 时间维度 |
| 6 | 极端 RowPress 下单次 activation 也可能触发 bitflip | Page 10, RowPress analysis | row 保持 open 16ms 的测试出现 bitflip | 高 | 这对内存控制器的 open-page policy 很关键 |
| 7 | 现代 HBM2 含未公开 TRR-like 防护 | Page 11, Figure 16 | dummy row 和 aggressor tracking 实验显示 activation-count-based 行为 | 高 | 工业防护黑盒化会增加系统安全验证难度 |
| 8 | 特定访问模式可绕过该防护 | Page 11, Figure 16 | 插入/组织访问序列后仍可诱发 bitflip | 高 | 防护评估必须包含自适应攻击，而不只是标准 hammer pattern |
| 9 | ECC word 分布影响错误可修复性 | Page 12, Figure 17 | bitflip 在 ECC word 中分布不均 | 中 | HBM 系统需要联合考虑 on-die ECC、外部 ECC 和扰动模式 |
| 10 | 开源实验数据和基础设施 | Page 2, Contributions; GitHub link | 作者提供 HBM read-disturbance repo | 中 | 对复现实验和后续防护比较很有价值 |
