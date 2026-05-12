# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何把任意用户定义的 operation 转换成高效 MAJ/NOT-based in-DRAM implementation。
- [ ] 我能解释作者的方法：Step 1 将 AND/OR/NOT logic 转为 optimized MAJ/NOT implementation；MAJ/NOT 是逻辑完备集合，常比先生成 AND/OR 再映射到 Ambit 更少 DRAM commands，见 Page 4-5 与 Page 19。
- [ ] 我能指出核心创新：提出首个面向 processing-using-DRAM 的 flexible end-to-end framework，支持 wide range of operations，见 Page 1-3。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 15` / `Table 2`
- [ ] 我能复述最重要结果：单 DRAM bank 上，SIMDRAM 在 16 operations 上平均提供 Ambit 的 2.0x throughput 与 2.6x energy efficiency；在 7 个 kernels 上平均提供 Ambit 的 2.5x performance，见 Page 1-2 与 Page 12-13。
- [ ] 我知道这篇文章的局限：当前框架只支持 integer/fixed-point operations；floating-point operations 因 mantissa alignment 和 per-bitline shift 等问题仍然困难，见 Page 11, Section 5.6。
- [ ] 我知道这篇文章和其他工作的关系：SIMDRAM 站在 RowClone、Ambit、LISA 之上：RowClone/LISA 提供数据移动，Ambit 提供 TRA/DCC primitive，SIMDRAM 则提供自动合成、编程接口和控制单元，把 primitive 组合成通用 PuM 框架。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
