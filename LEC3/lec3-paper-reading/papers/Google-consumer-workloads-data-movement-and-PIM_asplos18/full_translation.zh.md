# Full Chinese Translation

## Title
原文标题：Google Workloads for Consumer Devices: Mitigating Data Movement Bottlenecks

中文标题：面向消费设备的 Google 工作负载：缓解数据移动瓶颈

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文指出消费设备的电池与热约束使能效成为一等目标。作者分析 Chrome、TensorFlow Mobile、VP9 playback/capture 等 Google 工作负载，发现主存与计算单元之间的数据移动显著支配能耗和执行时间。将简单、数据密集的 primitive 放到 memory logic 附近执行，可以平均减少 55.4% 系统能耗并缩短 54.2% 执行时间。

---

## 1. Introduction / 引言

### 原文位置
Page 1-2

### 中文翻译
引言从消费设备增长、4K/VR/AR 等需求和电池/散热停滞切入，说明仅提升计算单元不够。核心观察是数据移动能耗远高于计算本身；在作者研究的应用中，平均 62.7% 能耗来自主存与计算单元之间的数据移动。因此，文章把问题转化为识别哪些函数既产生大量数据移动又能被便宜的 PIM logic 执行。

---

## 2-3. Background and Methodology / 背景与方法

### 原文位置
Page 2-3

### 中文翻译
作者介绍 3D-stacked memory 的 logic layer 为 PIM 提供实现空间，但消费设备无法承受复杂通用处理器式 PIM。方法上先用硬件计数器和能耗模型做 workload characterization，再以能耗占比、memory boundedness 和 PIM 执行可行性筛选 PIM target。

---

## 4-7. Workload Analyses / 工作负载分析

### 原文位置
Page 4-9

### 中文翻译
Chrome 部分显示 texture tiling、color blitting 等图形数据整理函数消耗大量数据移动能耗。TensorFlow Mobile 中 packing/data layout conversion 是重要目标。VP9 playback/capture 中，预测、变换、运动估计等数据密集阶段可受益于近存处理。

---

## 8-10. Evaluation / 评估

### 原文位置
Page 10-15

### 中文翻译
实验比较 CPU-only、PIM core 和 PIM accelerator。总体上，PIM accelerator 因定制化更强而收益更大；PIM core 更通用、面积更低。对 Chrome、TensorFlow 和 VP9，减少 off-chip/on-chip data movement 是主要收益来源。

---

## 11. Conclusion / 结论

### 原文位置
Page 16

### 中文翻译
作者总结说，在消费端应用里，数据移动已是系统级能耗与性能瓶颈。只要选取简单、数据密集且可在 memory logic 中实现的目标，PIM 就能在严格面积/功耗预算下提供显著收益。

---
