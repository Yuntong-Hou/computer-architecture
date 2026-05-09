# Full Chinese Translation

## Title
原文标题：SMASH: Co-designing Software Compression and Hardware-Accelerated Indexing for Efficient Sparse Matrix Operations

中文标题：SMASH：协同设计软件压缩与硬件索引以高效执行稀疏矩阵操作

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
SMASH 通过 hierarchical bitmap 软件编码和 BMU 硬件索引，让硬件识别稀疏矩阵压缩格式。相比 CSR，SpMV/SpMM 平均提升 38%/44%，面积开销很小。

---

## 1-2. Motivation / 动机

### 原文位置
Page 1-3

### 中文翻译
CSR 等格式减少零元素存储和计算，但发现 non-zero positions 需要 col_ind 扫描、pointer chasing 和 index matching。理想去除 indexing 后性能大幅提升，证明这是关键瓶颈。

---

## 3-4. SMASH Design / 设计

### 原文位置
Page 4-7

### 中文翻译
SMASH 用多层 bitmap 表示稀疏结构。BMU 通过 SRAM buffers、扫描逻辑、寄存器和输出 index registers 遍历层次位图，并由 ISA primitives 控制。

---

## 5-7. Use Cases and Evaluation / 用例与评估

### 原文位置
Page 7-13

### 中文翻译
SpMV、SpMM、PageRank、BC 等应用显示 SMASH 在多种矩阵稀疏结构下均有收益。压缩率和 BMU 参数影响性能，但面积最多约 0.076% OoO core。

---

## Conclusion / 结论

### 原文位置
Page 14-15

### 中文翻译
作者强调跨层 co-design 的必要性：压缩格式要同时适合软件存储和硬件索引，才能真正提升稀疏计算效率。

---
