# Full Chinese Translation

## Title
原文标题：MetaSys: A Practical Open-Source Metadata Management System to Implement and Evaluate Cross-Layer Optimizations

中文标题：MetaSys：用于实现和评估跨层优化的实用开源元数据管理系统

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
MetaSys 是一个开源 FPGA-based RISC-V 原型基础设施，用于快速实现和评估跨层优化。它提供通用 hardware-software interface 与轻量 metadata management，并用 graph prefetching、bounds checking 和 return address protection 展示可用性。

---

## 1. Introduction / 引言

### 原文位置
Page 1-2

### 中文翻译
作者指出跨层技术需要软件语义、硬件支持、OS 和 ISA 同时改变，真实硬件实现成本高。MetaSys 的目标是把这些共同部分抽象成 metadata substrate，使研究者可更快实现不同优化。

---

## 3. MetaSys Design / 系统设计

### 原文位置
Page 3-7

### 中文翻译
MetaSys 新增 RISC-V instructions 和软件库来创建、映射、取消映射 metadata；采用 tagged memory，把地址映射到 tag ID；OS 管理 MMT，硬件 MMC 缓存常用映射，optimization clients 从 PMT 读取模块私有 metadata。

---

## 4-6. Use Cases / 用例

### 原文位置
Page 7-11

### 中文翻译
三个用例分别展示 performance hint、安全检查和控制流保护：graph analytics prefetcher 使用访问模式元数据；bounds checking 使用 base/bounds；return address protection 保护 stack frame 中返回地址。

---

## 7. Characterization / 表征评估

### 原文位置
Page 11-15

### 中文翻译
作者量化面积、内存和性能开销，发现平均 overhead 低，但 metadata locality 和 TLB miss 会显著影响最坏情况。多个技术共享系统时没有明显额外性能损失，说明单一 substrate 可扩展。

---

## 8. Conclusion / 结论

### 原文位置
Page 16-17

### 中文翻译
论文总结 MetaSys 可以作为跨层优化研究的可复用开源平台，以较低硬件/内存开销支持多种 technique 的真实系统评估。

---
