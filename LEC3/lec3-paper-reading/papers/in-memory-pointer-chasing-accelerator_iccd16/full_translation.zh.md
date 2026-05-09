# Full Chinese Translation

## Title
原文标题：Accelerating Pointer Chasing in 3D-Stacked Memory: Challenges, Mechanisms, Evaluation

中文标题：在 3D-stacked memory 中加速 pointer chasing：挑战、机制与评估

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文提出 IMPICA，在 3D-stacked memory 的 logic layer 中执行 pointer chasing。它通过 address-access decoupling 和 region-based page table 解决并行性与地址翻译问题，并在微基准和 DBx1000 上提升性能与能效。

---

## 1-2. Motivation / 动机

### 原文位置
Page 1-3

### 中文翻译
linked lists、hash tables、B-trees 等结构中的 pointer chasing 会导致串行 memory accesses、cache/TLB misses 和低 prefetch accuracy。3D-stacked memory logic layer 提供低延迟近数据执行机会。

---

## 3-4. Challenges and Mechanisms / 挑战与机制

### 原文位置
Page 3-5

### 中文翻译
简单 accelerator 会把多个 traversal streams 串行化；IMPICA 通过解耦地址生成和访问来利用等待时间。由于指针保存 virtual address，IMPICA 使用 region-based page table 在 memory side 翻译。

---

## 7. Evaluation / 评估

### 原文位置
Page 6-7

### 中文翻译
IMPICA 在 linked list、hash table、B-tree 中显著加速，在 DBx1000 中获得 16% throughput improvement，并降低 transaction latency 和 system energy。

---

## Conclusion / 结论

### 原文位置
Page 8

### 中文翻译
作者认为 pointer chasing 是 PIM 的合适目标，而 parallelism 和 translation 两个问题也会出现在许多其他 in-memory accelerators 中。

---
