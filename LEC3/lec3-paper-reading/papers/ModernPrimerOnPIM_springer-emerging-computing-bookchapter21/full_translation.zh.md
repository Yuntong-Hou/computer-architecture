# Full Chinese Translation

## Title
原文标题：A Modern Primer on Processing in Memory

中文标题：Processing in Memory 现代入门

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
本章指出现代系统的大量瓶颈来自把数据搬到计算单元。PIM 把计算机制放在内存芯片、3D-stacked memory logic layer 或 memory controller 附近，以减少或消除数据移动。文章重点讨论 PUM 与 PNM 两类路线及其跨层挑战。

---

## 1-5. Motivation and Enablers / 动机与使能技术

### 原文位置
Page 2-14

### 中文翻译
作者从 DRAM scaling、RowHammer、retention、hybrid memory、data movement energy 等趋势解释为什么需要 intelligent memory。3D-stacked memory 和新型非易失内存为 PIM 提供了新的物理基础。

---

## 6. Processing Using Memory / PUM

### 原文位置
Page 14-18

### 中文翻译
PUM 利用 DRAM 内部操作特性做计算。RowClone 适合 bulk copy/initialization；Ambit 适合 bulk bitwise operations；其他机制把 DRAM 用作安全 primitive 或 gather-scatter substrate。

---

## 7. Processing Near Memory / PNM

### 原文位置
Page 18-24

### 中文翻译
PNM 在内存附近加入可编程或专用逻辑。案例包括 Tesseract graph processing、移动端 Google workload function offload、GPU NDP、PIM-enabled instructions、genome analysis 和 time-series analysis。

---

## 8-9. Adoption and Outlook / 落地挑战与展望

### 原文位置
Page 24-31

### 中文翻译
要让 PIM 真正可用，还需要编程模型、代码生成、runtime scheduling、data mapping、coherence、virtual memory、数据结构和 benchmark 支持。作者主张以 data-centric 方式重新设计系统。

---
