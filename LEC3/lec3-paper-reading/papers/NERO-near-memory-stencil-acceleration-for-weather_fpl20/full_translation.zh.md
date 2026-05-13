# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 NERO 的天气 stencil 背景、POWER9+CAPI2+FPGA+HBM 平台、vadvc/hdiff、memory hierarchy、auto-tuning、评估、局限和硬件工程师视角。保留 stencil、COSMO、HBM、FPGA、CAPI2、SNAP、PE、URAM/BRAM 等术语。

## Title

原文标题：NERO: A Near High-Bandwidth Memory Stencil Accelerator for Weather Prediction Modeling

中文标题：NERO：面向天气预报建模的近 HBM stencil 加速器

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

天气/气候模型包含大量 stencil computations。COSMO 模型中的 vadvc 和 hdiff 是 compound stencil kernels，访问模式复杂、算术强度低，在 POWER9 CPU 上受 DRAM bandwidth 限制。NERO 在 FPGA+HBM 平台上构建近内存加速器，通过多个 processing elements、HBM ports 和片上 memory hierarchy 缓解数据移动瓶颈。

评估显示，HBM-based NERO 对 vadvc 和 hdiff 分别比 16-core POWER9 快 4.2x 和 8.3x，能耗分别降低 22x 和 29x。

## 1. Motivation / 动机

### 原文位置

Page 1 - Page 2 / Figure 1

### 中文翻译

天气模型需要在三维网格上反复执行 stencil 更新。每个 output point 依赖邻域多个 input points。Compound stencil 将多个 stencil 操作组合，增加数据重用机会，但也增加 buffering 和调度复杂度。

POWER9 roofline 显示 vadvc/hdiff 受 host DRAM bandwidth 限制，64-thread 性能仅 29.1/58.5 GFLOP/s。常规 CPU 多线程无法突破内存带宽瓶颈。

## 2. NERO Architecture / NERO 架构

### 原文位置

Page 3 - Page 5 / Figures 3-4

### 中文翻译

NERO 使用 IBM POWER9 AC922 与 HBM2 FPGA board，通过 CAPI2 coherent accelerator interface 和 SNAP framework 连接 host 与 FPGA。Host 发起任务，数据通过 DMA 移动到 FPGA/HBM，多个 PEs 并行处理 stencil tiles。

FPGA 内部使用 HBM、URAM、BRAM 形成层次缓存。HBM 提供高带宽，URAM/BRAM 保存 stencil window 和 intermediate data，减少重复访问。多个 PEs 可连接不同 HBM ports，提高并行度。

NERO 使用 HLS 和 auto-tuning 搜索 tile/window/resource 配置。FPGA 频率低于 CPU/GPU，因此必须通过并行 PE、pipeline 和 memory hierarchy 弥补。

## 3. Evaluation / 评估

### 原文位置

Page 6 - Page 7 / Figures 6-7

### 中文翻译

作者评估 vadvc、hdiff 的 single/half precision、DDR4 vs HBM FPGA、不同 PE 数量、auto-tuning 和 energy efficiency。

HBM-based NERO 对 vadvc 和 hdiff 分别比 16-core POWER9 快 4.2x 和 8.3x。能耗分别降低 22x 和 29x。能效约为 1.5 GFLOPS/Watt 和 17.3 GFLOPS/Watt。

HBM ports 与 PE 数量对扩展性很关键。hdiff/vadvc 的收益取决于 PE 数量、window size、资源占用和 HBM bandwidth 的平衡。

## 4. Discussion and Limitations / 讨论与局限

### 原文位置

Design/evaluation discussion

### 中文翻译

NERO 聚焦 COSMO 的两个代表 kernels，不等同于完整天气模型端到端加速。完整模型还包含边界条件、通信、I/O、其它 kernels 和多节点同步。

平台特定性也明显：POWER9+CAPI2+SNAP+HBM FPGA 的结果不能直接外推到 CXL、PCIe-attached FPGA 或不同 HBM 设备。迁移需要重新做 memory mapping、coherence、DMA 和 auto-tuning。

## 5. 硬件工程师视角

NERO 是典型 FPGA+HBM near-memory design。关键不是“有 HBM 就快”，而是 PE pipeline、HBM port mapping、BRAM/URAM window buffer、tile size 和 data reuse 是否匹配。

做类似设计时，先做 roofline，确认 kernel memory-bound；再估算每个 PE 每周期需要多少 bytes；最后用 HBM channel/port 数反推 PE 数和 buffer 结构。验证重点是边界处理、tile halo、precision、DMA correctness 和 host-FPGA synchronization。

## 6. 不确定与需回原文核对

- Figure 1 roofline 和 Figures 6-7 结果需回 PDF；
- vadvc/hdiff 数据流、window size 和 HLS pragma 细节需核对；
- 完整天气模型端到端收益需要额外资料。
