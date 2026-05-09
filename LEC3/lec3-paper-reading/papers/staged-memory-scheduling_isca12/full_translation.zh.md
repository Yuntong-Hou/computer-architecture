# Full Chinese Translation

## Title
原文标题：Staged Memory Scheduling: Achieving High Performance and Scalability in Heterogeneous Systems

中文标题：分阶段内存调度：在异构系统中实现高性能与可扩展性

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
SMS 面向 CPU-GPU 共享内存系统，把 memory controller 的主要任务拆为三阶段。它在提升 CPU performance/fairness 的同时，让实现复杂度低于以往应用感知调度器。

---

## 1-3. Motivation / 动机

### 原文位置
Page 1-4

### 中文翻译
GPU requests 数量巨大，会占据 controller request buffer，使 controller 难以观察 CPU applications 的差异。扩大 buffer 会带来面积、功耗、时序和逻辑复杂度问题。

---

## 4. SMS Design / 设计

### 原文位置
Page 4-6

### 中文翻译
SMS 用 per-source FIFO 捕获 row-buffer locality，用 batch scheduler 做高层应用优先级，用 per-bank FIFO 做低层 DRAM timing。这样把全局复杂逻辑分解到更简单结构中。

---

## 5-6. Evaluation / 评估

### 原文位置
Page 7-11

### 中文翻译
SMS0.9 偏向 CPU，提升 CPU performance 和 fairness；SMS0 偏向 GPU，更适合 GPUweight 高的场景。p 是静态或动态可调的性能旋钮。

---

## 8. Conclusion / 结论

### 原文位置
Page 12

### 中文翻译
作者总结 staged approach 可以为未来异构系统 memory controller 提供可扩展基础，因为它同时解决 performance、fairness 和 design complexity。

---
