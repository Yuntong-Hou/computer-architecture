# Full Chinese Translation

## Title
原文标题：A Scalable Processing-in-Memory Accelerator for Parallel Graph Processing

中文标题：面向并行图处理的可扩展 Processing-in-Memory 加速器

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
Tesseract 是面向 large-scale graph processing 的 programmable PIM accelerator。它利用 3D-stacked memory 的 internal bandwidth、message passing 和 graph-aware prefetching，平均提升性能并降低能耗。

---

## 1-2. Motivation / 动机

### 原文位置
Page 1-3

### 中文翻译
图处理访问随机、局部性差、每项计算少。传统体系结构受 off-chip bandwidth 限制，memory capacity 增加不会带来 proportional bandwidth。PIM 可以让 bandwidth 随 memory cubes 增加而增加。

---

## 3. Architecture / 架构

### 原文位置
Page 4-7

### 中文翻译
每个 HMC vault 包含一个 Tesseract core。core 只访问本地 partition，远端访问通过 message passing，把计算移到数据处。编程接口提供 get/put/list_for/barrier 等 primitives。

---

## 3.3. Prefetching / 预取

### 原文位置
Page 5-6

### 中文翻译
list prefetcher 处理列表/边数组的 strided traversal；message-triggered prefetcher 利用消息排队到处理中间的时间预取远程函数所需数据。

---

## 5. Evaluation / 评估

### 原文位置
Page 8-12

### 中文翻译
Tesseract 显著提升性能，主要因为利用 TB/s internal bandwidth 并降低 memory access latency。scaling 受 off-chip network 和 graph partitioning 影响，能耗大幅下降但功耗上升仍在热限制内。

---

## 7. Conclusion / 结论

### 原文位置
Page 12-13

### 中文翻译
论文总结 Tesseract 展示了 3D-stacked memory 上 PIM 对 graph processing 的可扩展性，并指出未来需进一步优化网络和数据分布。

---
