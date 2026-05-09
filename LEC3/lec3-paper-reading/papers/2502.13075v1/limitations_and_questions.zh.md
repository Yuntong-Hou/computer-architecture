# Limitations and Questions

## 1. 作者明确承认的局限
- 完整 profiling 时间和能耗成本极高；位置：Page 12-14, Appendix。
- guardband/ECC 不能单独提供普遍安全保证；位置：Page 14-16。

## 2. 论文中隐含的局限
- HBM2 样本只有 4 颗，DDR5/LPDDR5 未覆盖。
- VRD 的物理根因尚未完全解释，更多是实验表征。

## 3. 实验设计可能存在的问题
- 长时间重复测试本身是否改变 row 状态需要进一步隔离。
- 测试参数虽多，但仍不能覆盖所有真实 workload 行为。

## 4. 方法可能不适用的场景
- 如果系统无法执行在线 profiling，论文建议的动态策略难以落地。
- 对强 ECC 系统，VRD 的安全影响需要结合 ECC granularity 和 error accumulation 分析。

## 5. 我阅读时应该追问的问题
- VRD 的物理根因是噪声、温度、电荷历史、VRT-like 现象，还是多因素叠加？
- Svärd 的 spatial profile 如何加入 temporal uncertainty？
- PRAC/Chronus 应该如何设置动态 NRH？
- 在线 profiling 会不会本身诱发额外扰动或攻击面？

## 6. 后续可以继续阅读的方向
- Spatial Variation-Aware Defenses：对比空间和时间变化。
- RowPress：理解 tAggON 对 threshold 的影响。
- AVATAR/RAIDR/REAPER：DRAM retention 中也有时间变化与 profiling 问题，可类比理解。
