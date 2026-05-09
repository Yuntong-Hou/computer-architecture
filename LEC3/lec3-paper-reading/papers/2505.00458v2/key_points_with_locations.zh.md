# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 现代计算的核心瓶颈是 memory system | Page 1, Section 1 | memory 负责大量能耗、性能瓶颈、可靠性问题、成本和面积 | 高 | 这是全文的总论点 |
| 2 | processor-centric paradigm 把 memory 当作被动组件 | Page 1, Section 1 | 计算只能在 processor，memory 只响应请求 | 高 | 后续 MCC 的反面定义 |
| 3 | DRAM scaling 导致 RowHammer/RowPress/VRD 等问题恶化 | Page 2, Section 2; Figure 1-2 | RowPress、VRD 数值作为例子 | 高 | memory 需要自主管理可靠性 |
| 4 | PRAC 是向 memory-centric 方向的一小步但还不够 | Page 3, Section 2 | PRAC 把 activation counters 放入 DRAM，但仍依赖 MC | 中 | 和 PRAC/Chronus 论文直接连接 |
| 5 | SMD 通过 DRAM negative acknowledgment 支持自主维护 | Page 3, Figure 3 | SMD chip 拒绝维护区域请求，允许其他区域访问 | 高 | 这是 memory maintenance 的关键接口变化 |
| 6 | PNM 能把容量/带宽/计算能力按比例扩展 | Page 3-4, Section 3.1 | 3D-stacked memory logic layer、UPMEM、Tesseract | 高 | 解决 system/application scaling |
| 7 | Tesseract 代表 graph analytics PNM 路线 | Page 4, Figure 4 | 引用 13.8x 性能、>8x 能耗改进 | 中 | 老牌 PIM 案例，应和 Tesseract 论文一起读 |
| 8 | PAPI/CENT 说明 LLM inference 也受益于 PNM | Page 4-5, Figure 5-6 | PAPI/CENT 用 PIM units 处理 FC/attention/KV-cache 等 | 高 | 把 PIM 连接到最新 AI workload |
| 9 | PUM 利用 memory array 的模拟/电路行为执行计算 | Page 5, Section 3.2 | RowClone、Ambit、SIMDRAM、COTS DRAM 多行激活 | 高 | 这是比 PNM 更激进的路线 |
| 10 | 采用挑战主要是软件、接口和生态 | Page 6, Section 4 | 需要 programming frameworks, compilers, runtime, prototypes | 高 | 技术可行之外还要可编程和可部署 |
