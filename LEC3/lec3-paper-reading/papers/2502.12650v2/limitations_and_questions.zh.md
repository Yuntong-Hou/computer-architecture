# Limitations and Questions

## 1. 作者明确承认的局限
- 结果修正说明显示早期实验/模拟存在 bug，需以 v2 附录修正值为准；位置：Appendix B。
- Chronus 仍需工业标准和 DRAM 实现支持；位置：Discussion。

## 2. 论文中隐含的局限
- 评估主要基于模拟，真实芯片实现可能暴露新的 timing/area/power 问题。
- 机制主要面向 activation-count disturbance，对 RowPress/VRD 的完整覆盖不足。

## 3. 实验设计可能存在的问题
- 与 PRAC variants 的公平比较依赖具体参数配置。
- attack model 是否覆盖最强攻击者仍需更多形式化分析。

## 4. 方法可能不适用的场景
- 如果 DRAM 标准无法支持 counter-data separation 或动态 RFM，Chronus 难以部署。
- 对极端低 NRH 或 row-open-time 主导的扰动，Chronus 可能仍需扩展。

## 5. 我阅读时应该追问的问题
- Chronus 如何与 JEDEC 实际命令/时序兼容？
- 动态 refresh 数量是否会泄露 side-channel 信息？
- VRD 下如果 NRH 随时间突然降低，Chronus 如何更新配置？
- Chronus 与 spatial profile/Svärd 能否组合？

## 6. 后续可以继续阅读的方向
- PRAC analysis paper：理解 Chronus 针对的问题。
- Variable Read Disturbance：检查阈值时间变化。
- DSAC：比较 in-DRAM stochastic/approximate counting 思路。
