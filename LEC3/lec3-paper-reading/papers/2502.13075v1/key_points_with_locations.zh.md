# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | VRD 表示同一 row 的 RDT 随时间变化 | Page 1 Abstract; Page 2, Figure 1 | RDT 序列显著波动 | 高 | 阈值不是固定常数 |
| 2 | 少数测量很可能错过真实最低 RDT | Page 2-5 | 单次测量只在 22.4% row 命中 1000 次内最低值 | 高 | 静态 profile 有安全风险 |
| 3 | 最低 RDT 可能非常晚才出现 | Page 5-6 | 最多 94,467 次测量后才观测到最低 RDT | 高 | 完整 profiling 成本巨大 |
| 4 | 同一 row min RDT 可比 max RDT 小 3.5x | Page 6-8 | min/max ratio 分析 | 高 | guardband 需要很大才稳健 |
| 5 | VRD 普遍存在 | Page 7-9 | 97.1% row 在所有参数组合下表现 VRD | 高 | 不是个别异常 row |
| 6 | data pattern、tAggON、温度、密度/工艺影响 VRD | Page 8-12 | 参数实验 | 中 | 与 RowPress 和技术缩放关联 |
| 7 | guardband + ECC 可缓解但不足以单独保证 | Page 14-16 | 10%/50% guardband 与 SECDED/SSC 分析 | 高 | 安全和性能之间有尖锐权衡 |
| 8 | 50% guardband 可造成约 45% 性能损失 | Page 15-16 | mitigation overhead 分析 | 高 | 单纯保守阈值不可持续 |
| 9 | 需要 online RDT profiling 与 runtime configurable mitigation | Page 16-17, Conclusion | 作者建议动态方案 | 高 | 未来防护方向 |
| 10 | 结果挑战 spatial-profile-based defense | Page 13-16 Implications | 静态 profile 可能过期或漏测 | 高 | 与 Svärd 必须结合阅读 |
