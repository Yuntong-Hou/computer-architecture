# Full Chinese Translation

## Title
原文标题：SISA: Set-Centric Instruction Set Architecture for Graph Mining on Processing-in-Memory Systems

中文标题：SISA：面向 PIM 图挖掘的集合中心 ISA

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
SISA 指出复杂 graph mining 的核心瓶颈是集合操作。通过 set-centric programming、SISA ISA extensions 和 PIM 加速，论文把高 degree bitvectors 交给 in-DRAM bitwise PUM，把低 degree integer arrays 交给 near-memory PNM。

---

## 1-3. Motivation / 动机

### 原文位置
Page 1-5

### 中文翻译
作者区分低复杂度图处理和复杂 graph mining。许多 clique/pattern/learning 算法都围绕邻居集合的交、并、差和计数展开，这些操作既 memory-bound 又有多层并行性。

---

## 4-8. SISA Design / 设计

### 原文位置
Page 5-10

### 中文翻译
SISA 包括 set-centric formulations、ISA instructions、set representations 和 PIM hardware。SCU 根据集合大小与表示选择 PUM 或 PNM 路线。

---

## 9. Evaluation / 评估

### 原文位置
Page 10-14

### 中文翻译
实验比较 hand-tuned non-set/set baselines 与 SISA variants。SISA 在多种真实图和复杂算法上获得显著 speedup，尤其是 maximal clique listing 等任务。

---

## Conclusion / 结论

### 原文位置
Page 15-16

### 中文翻译
作者总结 set operations 是复杂图挖掘的好抽象：它能提升可编程性，也能把 PIM 的大带宽转化为可用的算法加速。

---
