# Limitations and Questions

## 1. 作者明确承认的局限

- HBM-based design 的能效会随 PE/channel 增加而饱和甚至下降。原文位置：Page 9, Energy Efficiency Analysis。
- 最大 PE 数受 FPGA resources、timing closure 和 SLR 到 HBM channel 连接限制。原文位置：Page 10, Discussion。
- DDR4-based FPGA 对多个 PE 的扩展受单 memory channel 竞争限制。原文位置：Page 8-9。

## 2. 论文中隐含的局限

- 评估是 kernel-level，而不是完整 genome analysis pipeline 或完整 weather prediction application 的端到端评估。原文位置：Page 7, Evaluation。
- 使用的 FPGA/POWER9/OCAPI 平台较特定，结论对其它 FPGA、GPU 或 CPU 平台需要重新验证。
- SneakySnake 数据集只使用 100bp_2 的前 30,000 pairs，是否代表更长 reads 或不同 sequencing technologies 需要进一步确认。

## 3. 实验设计可能存在的问题

- CPU baseline 是 POWER9 64 threads，但 GPU baseline 或其它 FPGA/HBM platforms 没有系统比较。
- 能耗测量包含 socket/board active power，和纯 kernel energy 的边界需要留意。原文位置：Page 9。
- 对 weather kernels 使用 256 x 256 x 64 grid，真实 COSMO 全模型中的数据布局、I/O 和 coupling overhead 可能不同。

## 4. 方法可能不适用的场景

- 算术强度高、cache locality 好、数据搬移不是瓶颈的应用。
- 控制流复杂到难以 pipeline，或数据依赖无法拆分到多个 PE 的 workload。
- HBM channel 数不足或 host-FPGA 互连成为瓶颈的系统。

## 5. 我阅读时应该追问的问题

- Figure 6 中每个 kernel 的最佳 PE 数和最佳能效点是否一致？
- 为什么 multi-channel-single PE 不如更多 single-channel PEs？
- SneakySnake 的访问模式和普通 dynamic programming alignment 的差异在哪里？
- 这篇论文的结果和专用 PIM accelerator 相比，优势是通用性还是开发便利性？

## 6. 后续可以继续阅读的方向

- `GenASM`：更专用的 genome sequence analysis accelerator。
- `NERO` / `NATSA`：其它 near-memory / near-data kernels。
- `ModernPrimerOnPIM`：系统性理解 PIM 分类和历史。
