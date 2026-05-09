# Limitations and Questions

## 1. 作者明确承认的局限
- PRAC 分析基于公开规范和模型，实际厂商实现可能不同；位置：Page 7 Discussion。
- 低 NRH 下 PRAC 开销很高，需要未来机制改进；位置：Page 5-8。

## 2. 论文中隐含的局限
- 安全分析基于 activation-count 模型，对 RowPress 的 row-open time 维度覆盖有限。
- 真实系统中的 cache、OS 页面分配、地址映射会影响攻击者能否稳定触发 PRAC。

## 3. 实验设计可能存在的问题
- 使用模拟 workload，实际服务器/GPU 混合负载可能有不同 memory behavior。
- 能耗模型依赖参数假设，真实 DDR5 实现可能偏离。

## 4. 方法可能不适用的场景
- NRH 低于 20 或 temporal variation 导致瞬时阈值更低时，PRAC 的安全保证需要重新审视。
- 如果 DRAM 内部 victim selection 不透明，系统很难验证 RFM 是否覆盖所有风险 row。

## 5. 我阅读时应该追问的问题
- PRAC 能否处理 RowPress 或 Variable Read Disturbance？
- 攻击者能否通过 page coloring 或 huge page 获得更稳定 row mapping？
- PRAC 与 on-die ECC 的交互是否会隐藏早期 bitflip？
- Chronus 的改进是否完全解决 availability attack？

## 6. 后续可以继续阅读的方向
- Chronus：直接改进 PRAC。
- DSAC：另一种 in-DRAM 计数近似防护。
- Variable Read Disturbance：挑战固定 NRH 假设。
