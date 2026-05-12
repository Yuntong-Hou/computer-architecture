# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何避免对 leading zeros/ones 等无用高位执行 bit-serial PUD 计算。
- [ ] 我能解释作者的方法：Dynamic Bit-Precision Engine 在 LLC evicted cache lines 转置为 PUD vertical layout 时扫描对象，记录适合的 bit-precision，见 Page 2 与 Page 6-8。
- [ ] 我能指出核心创新：提出 Proteus，第一个面向 bulk bitwise PUD 的 data-aware hardware runtime framework，见 Page 1-2。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 14` / `Table 2`
- [ ] 我能复述最重要结果：Proteus LT-DP 相对 CPU、GPU、SIMDRAM 平均提供 17x、7.3x、10.2x performance per mm²；Proteus EN-DP 分别为 11.2x、4.8x、6.8x，见 Page 12, Figure 11。
- [ ] 我知道这篇文章的局限：真实应用需要手工修改以标记 PUD-friendly loops 和 fixed-point data arrays，工具链并非完全自动，见 Page 12。
- [ ] 我知道这篇文章和其他工作的关系：Proteus 建立在 SIMDRAM、Ambit、LISA、SALP 等工作上，解决的是 PuD arithmetic 的运行时自适应和高精度低延迟问题，可与 MIMDRAM 的资源粒度控制互补。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
