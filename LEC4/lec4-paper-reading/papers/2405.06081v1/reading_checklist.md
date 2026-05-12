# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：COTS DRAM 是否能稳健地同时激活超过四行，甚至 32 行。
- [ ] 我能解释作者的方法：作者用 DRAM Bender 精细调度 ACT/PRE 等命令，违反标准 timing parameters，以触发 simultaneous many-row activation，见 Page 3-5。
- [ ] 我能指出核心创新：在 120 个 COTS DDR4 chips 上展示可同时激活 2/4/8/16/32 行，见 Page 2 与 Section 4。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 17` / `Table 2`
- [ ] 我能复述最重要结果：COTS DRAM 可同时激活最多 32 行；MAJ3/MAJ5/MAJ7/MAJ9 平均 success rate 分别为 99.00%、79.64%、33.87%、5.91%，见 Page 2。
- [ ] 我知道这篇文章的局限：部分 Samsung 芯片未观察到同一 subarray 中多于一行的同时激活，因此不支持测试的 PUD operations，见 Page 12, Section 9。
- [ ] 我知道这篇文章和其他工作的关系：这篇论文与 FCDRAM 是互补关系：FCDRAM 展示 functionally-complete Boolean logic，本论文展示 simultaneous many-row activation、MAJX 和 Multi-RowCopy。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
