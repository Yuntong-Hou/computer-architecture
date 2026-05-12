# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：在端子数受限、芯片不可修复、需要少数模块类型的 LSI 背景下，如何组织有用的数字电路模块。
- [ ] 我能解释作者的方法：CLIM 基本形式是二维矩形 identical cells，每个 cell 包含简单 logic-and-storage circuit，并主要连接相邻 cells，见 Page 2。
- [ ] 我能指出核心创新：系统提出 CLIM arrays 的设计特征：identical cells、local neighbor connections、cell-level storage 和 programmability，见 Page 1-2, Section II。
- [ ] 我能看懂主要实验表格和图，例如 `Fig. 5` / `未检测到核心表格`
- [ ] 我能复述最重要结果：Sorting Array I 可作为保持 words 有序的 single-address multiword memory，也可作为 CAM、pushdown memory、queue/buffer memory 和 programmable switching array，见 Page 1 与 Page 6-8。
- [ ] 我知道这篇文章的局限：这是一篇 1969 年概念与工程设计论文，没有现代 benchmark、能耗、面积或系统级定量评估。
- [ ] 我知道这篇文章和其他工作的关系：这是 PIM/logic-in-memory 的早期思想源头之一；后来的 Stone logic-in-memory、near-data processing、Ambit/PuD 都可以看作在不同技术时代重新探索“把逻辑放进/靠近存储”的问题。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
