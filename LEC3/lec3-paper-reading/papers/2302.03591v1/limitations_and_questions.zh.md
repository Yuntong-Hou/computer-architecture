# Limitations and Questions

## 1. 作者明确承认的局限

- 作者说明由于 DSAC 不需要 DRAM 外部操作，本文不评估 system performance。原文位置：Page 10, Evaluation。
- DSAC leveraged probability，因此安全分析基于 probability theory。原文位置：Appendix / extracted text Page 13+。

## 2. 论文中隐含的局限

- 评估主要是合成 attack pattern 和模型，不是完整真实系统实测。
- 面积、access energy、static power 来自 CACTI 6.0，不是真实 DRAM silicon 测量。
- DSAC 需要 DRAM 内部实现 count table、PRNG/LUT、Time-Weighted Counter 等，工程落地需 DRAM vendor 支持。
- 英文表达、公式排版和符号解释不够清晰，读者需要仔细核对 Table I、Equations 和 Appendix。

## 3. 实验设计可能存在的问题

- 只评估 Maximum Disturbance，不评估真实 workload 下的 false positive、extra TRR、latency/energy system impact。
- attack patterns 包括 TRRespass/random，但真实攻击可能有更复杂 temporal/spatial locality。
- MRLoc 在 Table V 中表现低 disturbance，但作者指出未注入 MRLoc adversarial pattern；这说明比较依赖 threat model。

## 4. 方法可能不适用的场景

- DRAM 无法增加内部 counting logic 的场景。
- 需要 deterministic guarantee 而不能接受 probabilistic filtering 的安全场景。
- RowHammer threshold 极低、需要更大 blast radius 防护时，TRRTH 和 counter 配置可能需要重新分析。

## 5. 我阅读时应该追问的问题

- DSAC 对 Blacksmith / frequency-domain RowHammer patterns 是否仍有效？
- DSAC 的概率安全分析是否覆盖 adaptive attacker？
- Time-Weighted Counting 会不会被 benign long activation patterns 触发过多 TRR？
- 在真实系统中，DSAC 额外 TRR 造成的性能/能耗开销是多少？

## 6. 后续可以继续阅读的方向

- `Graphene`、`PARA`、`BlockHammer`、`Hydra` 原论文。
- `SMD`：理解 DSAC 这类 in-DRAM algorithm 如何被系统接口支持。
- `TRRespass` / `Blacksmith`：理解 decoy-row 和 adversarial access patterns。
