# Full Chinese Translation

## Title
原文标题：DASH: Deadline-Aware High-Performance Memory Scheduler for Heterogeneous Systems with Hardware Accelerators

中文标题：DASH：面向含硬件加速器异构系统的 deadline-aware 高性能内存调度器

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
DASH 是一种 memory scheduler，用于 CPU 和 hardware accelerators 共享 DRAM 的异构系统。它在满足 HWA deadline 的同时，尽量保持 CPU 高性能。

---

## 1-3. Background and Motivation / 背景与动机

### 原文位置
Page 1-5

### 中文翻译
HWA 处理图像/视频等 frame-based workload，需要在 deadline 前完成；CPU workloads 同时需要 DRAM bandwidth。传统 FRFCFS 或简单优先级策略难以同时满足这两个目标。

---

## 4. DASH Design / 设计

### 原文位置
Page 5-10

### 中文翻译
DASH 的关键是 Distributed Priority、application-aware prioritization 和短 deadline HWA 的保守 worst-case 处理。调度器持续判断 HWA progress 是否 on track，并在必要时优先 HWA 请求。

---

## 5-6. Methodology and Evaluation / 方法与评估

### 原文位置
Page 10-22

### 中文翻译
实验使用多种 CPU workloads、HWA 类型和 GPU-HWA 组合。DASH 在 deadline-met ratio 与 frame rate 上保持目标，同时比能满足 deadline 的先前策略有更高 CPU performance。

---

## Conclusion / 结论

### 原文位置
Page 26-28

### 中文翻译
作者总结异构系统的 memory scheduler 必须理解加速器 deadline 和 CPU 应用特性，才能避免过度保守或过度冒险的调度。

---
