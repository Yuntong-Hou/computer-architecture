# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 PIM 综述的问题背景、PUM/PNM 分类、代表系统、adoption challenges 和硬件工程师视角。保留 Processing-in-Memory、PUM、PNM、RowClone、Ambit、Tesseract、3D-stacked memory 等术语。

## Title

原文标题：A Modern Primer on Processing in Memory

中文标题：Processing in Memory 现代入门综述

## Abstract / 摘要

### 原文位置

Book chapter / Abstract and Introduction

### 中文翻译

现代计算的主要瓶颈之一是 data movement。Processor-centric systems 把数据从 memory 搬到 CPU/GPU/accelerator 计算，再写回 memory。对于 graph analytics、genome analysis、time series、ML、database 等 data-intensive applications，数据移动能耗和延迟可能远高于实际计算。

Processing-in-Memory（PIM）试图把计算放到 memory 内部或附近。本文将 PIM 分为 Processing Using Memory（PUM）和 Processing Near Memory（PNM）。PUM 利用 memory array 本身执行 bulk copy/bitwise operations；PNM 在 3D-stacked memory logic layer、near-memory logic 或 memory-side accelerator 中执行计算。

## 1. Motivation / 动机

### 原文位置

Page 1 - Page 12

### 中文翻译

DRAM capacity 增长速度长期快于 bandwidth 和 latency 改善，导致 memory wall 加剧。与此同时，RowHammer、retention time variation、data-dependent failures 等可靠性问题说明 memory scaling 本身也需要更智能的系统支持。

Data movement energy 可比简单计算高 100-1000x。对大数据应用，减少搬移比提高 ALU 峰值更重要。PIM 因此重新受到关注。

## 2. Processing Using Memory / 利用内存计算

### 原文位置

PUM sections / RowClone, Ambit, Gather-Scatter DRAM

### 中文翻译

PUM 直接利用 memory array 的物理操作。RowClone 使用 DRAM row activation 机制实现快速 bulk copy/initialization。Ambit 利用多行激活实现 bulk bitwise AND/OR/NOT 等操作。Gather-Scatter DRAM 通过内存内部数据重排支持更高效访问。

PUM 的优势是能效高、靠近数据、硬件增量小。限制是操作类型受 DRAM 物理机制约束，可编程性弱，需要 ISA/runtime/OS 暴露接口，并且必须处理可靠性和安全隔离。

## 3. Processing Near Memory / 近内存处理

### 原文位置

PNM sections / Tesseract, mobile workloads, GPU workloads, domain accelerators

### 中文翻译

PNM 在 memory 附近放置计算逻辑。3D-stacked memory logic layer 是典型位置，因为它靠近高带宽 DRAM vaults。Tesseract 用 PNM 加速 graph analytics；Google consumer workloads 研究展示移动端数据搬移 primitive 适合 PIM；GenASM、NATSA、NERO 等展示 genome、time series、weather stencil 等 domain-specific near-data acceleration。

PNM 比 PUM 更可编程，但面积、功耗、热、编程模型、coherence 和 virtual memory 更复杂。通用 PNM core 灵活但能效有限；专用 accelerator 高效但通用性低。

## 4. Adoption Challenges / 采用挑战

### 原文位置

Section 8 / Page 24-31

### 中文翻译

PIM 落地需要解决编程模型、编译器/runtime、数据映射、任务调度、cache coherence、virtual memory、memory consistency、security isolation、debugging 和 benchmarking。

软件必须知道哪些数据放在 PIM-friendly memory，何时 offload，如何处理 CPU/PIM 数据一致性。系统需要 fallback path，因为不是所有 workload 都适合 PIM。Benchmark 也必须端到端评估，不能只看 kernel speedup。

## 5. 硬件工程师视角

PIM 不是单一技术，而是一组跨层设计选择。硬件工程师需要根据 workload 判断使用 PUM、PNM core 还是专用 NDP accelerator。核心问题是数据移动、局部性、带宽、容量、同步和软件接口。

对未来 HBM/CXL memory systems，PIM 可能以 memory-side copy/transform、near-memory filtering、compression、graph/genome/time-series accelerators 或 self-managing memory 的形式落地。

## 6. 不确定与需回原文核对

- 综述引用的各系统结果来自不同平台，不应直接横向比较；
- PUM/PNM 案例图建议回 PDF；
- 商业 PIM 进展需要结合更新资料补充。
