# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 NATSA 的 matrix profile 背景、near-HBM 架构、processing units、diagonal scheduling、评估、局限和硬件工程师视角。保留 matrix profile、SCRIMP、HBM、NDP、PU、DCU、DPU、anytime property 等术语。

## Title

原文标题：NATSA: A Near-Data Processing Accelerator for Time Series Analysis

中文标题：NATSA：面向时间序列分析的近数据处理加速器

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

Matrix profile 是 time series motif/discord discovery 的重要 exact anytime algorithm，但它需要对大量 subsequences 计算距离，数据量大、算术强度低，CPU/GPU 实现容易受 memory bandwidth 和 data movement 限制。

NATSA 提出第一个面向 time series analysis 的 near-data processing accelerator。它把专用 floating-point processing units 放在 HBM logic layer 附近，直接利用 HBM 高带宽计算 matrix profile。通过 diagonal scheduling 和专用 datapath，NATSA 在性能和能耗上显著优于多核 CPU、GPU 和通用 NDP cores。

## 1. Background: Matrix Profile / 背景：Matrix Profile

### 原文位置

Page 2 / Equation 1 and algorithm explanation

### 中文翻译

Matrix profile 描述时间序列中每个 subsequence 与其最近邻 subsequence 的距离。它可用于 motif discovery、discord detection、similarity search 等。SCRIMP 等算法通过遍历 distance matrix 的 diagonals 逐步更新 profile，具有 anytime property：运行过程中随时可给出逐步改善的结果。

计算瓶颈在于大量 dot product、Euclidean distance 和 profile update。数据访问有规律但数据量大，适合利用 HBM bandwidth 和 near-data compute。

## 2. NATSA Architecture / NATSA 架构

### 原文位置

Page 4 - Page 5 / Architecture and scheduling

### 中文翻译

NATSA 将 time series 数据存放在 3D-stacked HBM 中，多个 processing units 靠近 HBM vaults。每个 PU 包含用于 dot product/update 的 DCU 和用于 distance/profile update 的 DPU。专用 floating-point datapath 避免通用 core 的指令和控制开销。

Diagonal scheduling 将 distance matrix diagonals 分配给 PUs。调度需要平衡负载、HBM bandwidth 和 anytime property。某些调度方式可改善局部性或并行性，但可能影响 anytime 输出顺序。

## 3. Evaluation / 评估

### 原文位置

Page 6 - Page 8 / Figures 7-11

### 中文翻译

作者比较 DDR4-OoO multicore、HBM-OoO、HBM-inOrder general-purpose NDP、Intel Xeon Phi KNL、NVIDIA GPU 等。数据包括 synthetic random 128K-2M、ECG、seismology 等时间序列。

NATSA 相比 state-of-the-art multi-core baseline 最高 14.2x、平均 9.9x 性能提升；能耗最高降低 27.2x、平均 19.4x。相比 64 in-order core general-purpose NDP，NATSA 性能提升 6.3x、能耗降低 10.2x。

结果说明，单纯把通用 cores 放近 HBM 不一定能充分利用带宽；domain-specific datapath 才能把 bandwidth 转化为有效吞吐。

## 4. Discussion and Limitations / 讨论与局限

### 原文位置

Design scope / evaluation discussion

### 中文翻译

NATSA 专注 matrix profile/SCRIMP 类算法，通用性低于 general-purpose NDP。收益依赖足够大的 time series、HBM bandwidth 和算法访问规律。小数据、不同 time series algorithm 或复杂预处理可能降低收益。

实际系统还需要 host interface、data transfer、programming API、HBM capacity management 和多任务调度支持。

## 5. 硬件工程师视角

NATSA 展示了 HBM near-data accelerator 的典型设计方法：先找 memory-bound kernel，再设计专用 datapath，使计算吞吐匹配 HBM bandwidth。通用 core 不一定是好答案，因为 instruction overhead 和控制流会浪费带宽。

对类似设计，应重点做 roofline 分析、HBM channel/vault mapping、PE 数量选择、SRAM buffering、load balance 和 precision tradeoff。

## 6. 不确定与需回原文核对

- Matrix profile 公式和 SCRIMP diagonal update 需回 PDF；
- Figures 7-11 的性能/能耗数据建议核对；
- Anytime property 与调度优化之间的 tradeoff 需看原文细节。
