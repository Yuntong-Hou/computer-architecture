# Full Chinese Translation

## Title
原文标题：Revisiting Memory Errors in Large-Scale Production Data Centers: Analysis and Modeling of New Trends from the Field

中文标题：重新审视大规模生产数据中心中的内存错误：来自现场的新趋势分析与建模

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文分析 Facebook 全量服务器 14 个月内存错误，覆盖数十亿 device days。作者发现错误分布、来源和影响因素与早期研究存在新的趋势，并给出可靠性模型和 page offlining 部署结果。

---

## I-II. Introduction and Methodology / 引言与方法

### 原文位置
Page 1-3

### 中文翻译
作者解释 ECC、CE/UCE、MCE 日志和服务器内存组织，并说明收集每个 CE 的时间、物理地址、socket/channel/bank 与访问类型。

---

## III-IV. Statistics and Factors / 基线统计与影响因素

### 原文位置
Page 3-9

### 中文翻译
错误高度偏斜，平均值远高于中位数。controller/channel/socket 等非 DRAM failures 产生大量错误。chip density、DIMM chips/transfer width、workload 和年龄都会影响 failure rate，而 CPU/memory utilization 趋势不明显。

---

## V. Failure Model / 失效模型

### 原文位置
Page 9-10

### 中文翻译
作者用 logistic regression 建立 failure model。模型显示设计选择会显著改变可靠性，例如使用低密度 DIMMs 或减少访问 memory 的 CPUs。

---

## VI. Page Offlining / 页下线

### 原文位置
Page 10-11

### 中文翻译
page offlining 在真实系统中把出错物理页移除，86 天实验显示错误率约下降 67%。但它会减少物理内存，且部分页因 OS 限制不能立即下线。

---

## VIII. Conclusions / 结论

### 原文位置
Page 11-12

### 中文翻译
论文总结现代数据中心 memory errors 是分布、硬件、workload 与系统策略共同作用的结果，模型和数据可帮助设计更可靠 DIMM 与服务器。

---
