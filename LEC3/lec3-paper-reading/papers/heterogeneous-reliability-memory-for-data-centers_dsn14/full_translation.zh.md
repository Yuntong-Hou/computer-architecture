# Full Chinese Translation

## Title
原文标题：Characterizing Application Memory Error Vulnerability to Optimize Datacenter Cost via Heterogeneous-Reliability Memory

中文标题：通过异构可靠性内存刻画应用内存错误脆弱性以优化数据中心成本

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文指出数据中心内存可靠性不应一刀切。不同 data-intensive applications 以及同一应用的不同 memory regions 对 memory errors 的容忍度差异很大，利用这种差异可降低服务器硬件成本。

---

## I-III. Motivation and Methodology / 动机与方法

### 原文位置
Page 1-4

### 中文翻译
作者把 memory error outcomes 分为 overwrite masking、logic masking、incorrect response 和 crash，并用 safe ratio 与 recoverability 描述 memory regions 的容错能力。

---

## IV-V. Characterization / 表征

### 原文位置
Page 4-8

### 中文翻译
WebSearch、Memcached、GraphLab 的 case study 显示，应用间和应用内部 region 间 vulnerability 差异显著。WebSearch 大量数据为只读缓存，可从持久存储恢复。

---

## VI. Design Space / 异构可靠性设计

### 原文位置
Page 8-11

### 中文翻译
系统可组合 NoECC、Parity、SECDED、less-tested DRAM、software recovery 和 page retirement，并在 memory region 粒度做映射。Table 6 说明该方法能同时满足 availability 和成本目标。

---

## Conclusion / 结论

### 原文位置
Page 11-12

### 中文翻译
作者总结，随着 DRAM 错误率和成本压力上升，应用感知的 heterogeneous-reliability memory 是比统一强保护更经济的方向。

---
