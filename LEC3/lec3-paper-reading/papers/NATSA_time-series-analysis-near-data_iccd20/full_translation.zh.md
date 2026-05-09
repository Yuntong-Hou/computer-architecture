# Full Chinese Translation

## Title
原文标题：NATSA: A Near-Data Processing Accelerator for Time Series Analysis

中文标题：NATSA：面向时间序列分析的近数据处理加速器

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
NATSA 针对 matrix profile 的大数据、低算术强度特点，把专用浮点计算单元放到 HBM 附近。相比多核实现，它最高提升 14.2x 性能、最高降低 27.2x 能耗。

---

## 1-2. Background / 背景

### 原文位置
Page 1-3

### 中文翻译
时间序列 motif/discord discovery 可用于流行病学、基因组、神经科学等领域。Matrix profile 用欧氏距离构建 distance matrix、profile 和 profile index，但数据移动成为主要瓶颈。

---

## 3-4. NATSA Design / 方法

### 原文位置
Page 3-5

### 中文翻译
NATSA 贴近 HBM 设计多个专用 PU，支持 dot product、distance computation 和 profile update。diagonal scheduling 把 distance matrix 的对角线分给不同 PU，降低负载不均并保留 anytime 特性。

---

## 5-6. Evaluation / 评估

### 原文位置
Page 5-8

### 中文翻译
实验比较 DDR4/HBM 多核、通用 NDP、GPU 和 NATSA。NATSA 在大 time series 上利用 HBM 带宽更充分，性能、能耗和面积均优于通用平台。

---

## 8. Conclusion / 结论

### 原文位置
Page 9

### 中文翻译
作者总结 NATSA 说明 time series analysis 是近数据专用加速的合适目标：当算法 memory-bound 且计算模式稳定时，贴近 HBM 的专用设计可以明显优于搬数据到 CPU/GPU。

---
