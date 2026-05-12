# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：是否可以在 off-the-shelf, unmodified, commercial DRAM 中实现 in-memory row copy 与逻辑 AND/OR。
- [ ] 我能解释作者的方法：ComputeDRAM 用 ACTIVATE(R1)-PRECHARGE-ACTIVATE(R2) 等 timing-violating command sequence 让多行在同一 subarray 中同时影响 bitline，从而实现 row copy 或 AND/OR，见 Page 3-5, Figures 3-6。
- [ ] 我能指出核心创新：首次展示在未修改商用 DRAM 中实现 row copy，见 Page 1-2 与 Page 3-4。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 12-13` / `Table 2`
- [ ] 我能复述最重要结果：Figure 10 显示至少存在 off-the-shelf unmodified commercial DRAM modules 可同时执行 row copy 与 logical AND/OR；几乎所有 configuration groups 至少有部分 columns 能执行 row copy，见 Page 9。
- [ ] 我知道这篇文章的局限：不是所有 vendor/configuration 都支持完整 AND/OR；作者推测某些芯片会检查并丢弃过紧 command timing，但内部设计不可见，见 Page 10。
- [ ] 我知道这篇文章和其他工作的关系：ComputeDRAM 与 Ambit 解决相似 primitive，但路线相反：Ambit 修改 DRAM 控制逻辑支持规范化 TRA，ComputeDRAM 则用现有商用 DRAM 的 out-of-spec timing 行为做 proof-of-concept。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
