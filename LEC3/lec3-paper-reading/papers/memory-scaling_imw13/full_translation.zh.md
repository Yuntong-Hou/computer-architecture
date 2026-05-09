# Full Chinese Translation

## Title
原文标题：Memory Scaling: A Systems Architecture Perspective

中文标题：内存缩放：系统架构视角

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
本文认为 memory system 已成为几乎所有系统的性能与能耗瓶颈。面对 DRAM scaling 困难，系统需要从 DRAM 架构、新型内存和 QoS 三个方向重新设计。

---

## I-III. Trends and Solution Directions / 趋势与方向

### 原文位置
Page 1

### 中文翻译
更多异构核心、数据密集应用和技术缩放限制共同加剧 memory bottleneck。作者主张跨层合作，从算法、软件、微架构到设备共同解决。

---

## IV. New DRAM Architectures / 新 DRAM 架构

### 原文位置
Page 1-2

### 中文翻译
RAIDR 利用 retention time 差异降低 refresh；SALP 利用 subarray 并行性；TL-DRAM 在 bitline 内制造 latency heterogeneity；RowClone 把 bulk copy/init 放进 DRAM。

---

## V-VI. Emerging Memories and QoS / 新型内存与可预测性

### 原文位置
Page 3-4

### 中文翻译
PCM/STT-MRAM 等技术提供非易失和更好密度，但有写延迟、能耗、耐久性和安全挑战。共享内存系统还必须估计并控制 application slowdown。

---

## VIII. Conclusion / 结论

### 原文位置
Page 4-5

### 中文翻译
作者总结 memory scaling 需要系统架构级方案，而不是只依赖底层器件缩放；跨层 co-design 会随着物理 scaling 极限临近而更重要。

---
