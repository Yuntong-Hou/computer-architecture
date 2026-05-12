# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何把 cellular logic-in-memory arrays 嵌入通用计算机系统，而不是仅作为孤立 associative memory 或特殊功能单元。
- [ ] 我能解释作者的方法：基础组织是 cache-organized computer：CPU 请求先到 cache，miss 时把主存 sector 调入 cache；如果 cache sector 是 logic-in-memory array，CPU 就能对逻辑增强 sector 发出操作，见 Page 2-3, Figure 1。
- [ ] 我能指出核心创新：提出以 logic-enhanced cache memory array 为中心的 logic-in-memory computer 组织，见 Page 1, Abstract 与 Page 3。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 2` / `未检测到核心编号表`
- [ ] 我能复述最重要结果：摘要声称 logic-in-memory computer 由于 high-speed, highly parallel sector operations，指向 orders-of-magnitude performance increase 的新方向，见 Page 1, Abstract。
- [ ] 我知道这篇文章的局限：论文没有实现和定量 benchmark，除引用 IBM 360/85 cache 结果外，多数性能主张是概念性推断，见 Page 3-6。
- [ ] 我知道这篇文章和其他工作的关系：Stone 1970 是早期 logic-in-memory/PIM 思想源头之一：它不像现代 DRAM PuM 论文那样使用 sense amplifier 或 RowClone，而是从 cache organization、sector operations 和编程语言可用性角度预见了后来的 PIM 系统问题。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
