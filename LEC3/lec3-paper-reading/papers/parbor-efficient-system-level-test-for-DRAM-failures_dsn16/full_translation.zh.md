# Full Chinese Translation

## Title
原文标题：PARBOR: An Efficient System-Level Technique to Detect Data-Dependent Failures in DRAM

中文标题：PARBOR：高效检测 DRAM data-dependent failures 的系统级技术

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
PARBOR 是系统级检测 DRAM data-dependent failures 的方法。它先确定物理邻近 cells 在 system address space 中的位置，再利用这些信息构造 neighbor-aware tests。

---

## 1-4. Motivation and Key Ideas / 动机与关键思想

### 原文位置
Page 1-5

### 中文翻译
DRAM 内部地址 scrambling 使相邻 system addresses 不能代表物理邻居。PARBOR 利用 strongly coupled cells 和 DRAM 映射 regularity，把原本不可行的 O(n^2) 邻居测试转化为少量递归并行测试。

---

## 5-7. PARBOR and Evaluation / 方法与评估

### 原文位置
Page 5-10

### 中文翻译
PARBOR 递归测试多个 rows，统计 failure-triggering distances 并过滤 random failures。真实 144 chips 结果显示只需 66-90 tests，且比 random patterns 多发现 21.9% failures。

---

## 8. DC-REF Use Case / DC-REF 用例

### 原文位置
Page 10-11

### 中文翻译
DC-REF 根据 row 当前数据是否匹配 worst-case pattern 决定是否高频刷新弱 rows。它相比传统 retention-aware refresh 进一步减少 refresh 并提升性能。

---

## 10. Conclusion / 结论

### 原文位置
Page 11-12

### 中文翻译
作者总结 PARBOR 为系统级 DRAM profiling 提供了缺失的物理邻接信息，可支撑后续可靠性、性能和能耗优化。

---
