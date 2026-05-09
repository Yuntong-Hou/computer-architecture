# Limitations and Questions

## 1. 作者明确承认的局限
- 空间特征不能稳定预测脆弱性，需要实际 profile；位置：Page 7-8。
- profile 可能受环境和时间影响，需要更新或 guardband；位置：Page 16 Discussion。

## 2. 论文中隐含的局限
- 主要实验对象是 DDR4，不能直接代表 HBM2、DDR5 或 LPDDR5。
- Svärd 的收益取决于 profile granularity；row-level profile 最准确但成本最高。

## 3. 实验设计可能存在的问题
- 系统模拟的 workload 与真实多租户攻击流量之间存在差距。
- adversarial pattern 覆盖有限，实际攻击者可能利用 profile 机制本身。

## 4. 方法可能不适用的场景
- vulnerability 随时间快速变化时，静态 profile 可能过期。
- 低成本系统无法存储或查询细粒度 row profile 时，Svärd 需要粗粒度近似，安全收益会下降。

## 5. 我阅读时应该追问的问题
- profile 应由 DRAM 厂商、BIOS、memory controller 还是 OS 维护？
- VRD 论文提出的 temporal variation 会不会使 Svärd 需要频繁重测？
- 如果攻击者知道哪些 row 更弱，是否能反过来增强攻击？
- Svärd 与 JEDEC PRAC/RFM 能否结合？

## 6. 后续可以继续阅读的方向
- Variable Read Disturbance：检查 profile 随时间变化的问题。
- Chronus/PRAC：理解工业防护与 adaptive profile 的结合点。
- HBM2 Read Disturbance：比较 DDR4 与 HBM2 的 spatial variation。
