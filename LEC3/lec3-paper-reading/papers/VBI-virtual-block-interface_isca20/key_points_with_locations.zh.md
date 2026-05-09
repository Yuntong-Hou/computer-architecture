# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：传统虚拟内存难以适配虚拟化、多级页表、异构内存和应用多样需求；OS 同时管理 protection、allocation、translation 造成复杂性和性能损失。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：应用把语义相关对象放入 VB；OS 控制 process-VB permissions；CPU 使用 system-wide unique VBI address 访问 cache；LLC miss 后由 memory controller 的 MTL 完成 VBI-to-physical translation 和物理内存分配/迁移。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：4KB granularity simplified VBI 在 native/VM address translation 场景分别最高提升 2.6x/3.8x。 | Page 2 and Page 9, Figure 6 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：在启用 large pages 后，VBI 仍比 Native-2M 提升 77%，比 Virtual-2M 提升 89%。 | Page 9-10, Figure 7 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：VBI-Full 将 translation-related memory accesses 平均减少 56%。 | Page 9-10, Figure 7 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：在 PCM-DRAM 和 TL-DRAM 两种异构内存中，VBI 分别提升 33% 和 21%。 | Page 11, Figures 9-10 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：虚拟机中 VBI 避免 2D page walks，使 VM translation 与 native 类似。 | Page 5 and Section 6.1 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：VBI 是新虚拟内存框架，需要 ISA/OS/hardware/memory-controller 协同修改。 | Page 3-7, design sections | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：真实系统采用 VBI 的兼容性成本很高，尤其对现有 OS、hypervisor 和应用 ABI。 | 推断，基于 framework replacement | 基于范围的推断。 | 中 | 后续阅读方向。 |
