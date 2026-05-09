# Full Chinese Translation

## Title
原文标题：A Case for Richer Cross-layer Abstractions: Bridging the Semantic Gap with Expressive Memory

中文标题：用 Expressive Memory 弥合语义鸿沟：更丰富跨层抽象的案例

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
XMem 是一种新的 cross-layer interface，允许应用把高层程序语义传给 OS 和硬件。核心抽象 Atom 表达数据属性、访问属性和局部性，帮助 cache、memory controller 等组件更好优化性能。

---

## 1-3. Motivation and Atom / 动机与 Atom

### 原文位置
Page 1-5

### 中文翻译
传统接口只保留执行正确性所需信息，数据结构级语义丢失。Atom 将 semantically similar data 绑定到属性和映射范围，并通过 create/map/activate 等操作动态传递给系统。

---

## 4. XMem Implementation / 实现

### 原文位置
Page 5-7

### 中文翻译
XMemLib、OS、ISA instructions 和 AMU 共同维护 Global/Private Attribute Tables、Atom Address Map 和 Atom Status Table。硬件组件可按地址查询 Atom ID 和属性。

---

## 5-6. Use Cases / 用例

### 原文位置
Page 8-12

### 中文翻译
cache tiling 用例中，XMem 通过工作集和 reuse 语义协调 cache management/prefetching；DRAM placement 用例中，XMem 根据 data structure 的 row-buffer locality 和 irregularity 进行 bank/channel 放置。

---

## 8. Conclusion / 结论

### 原文位置
Page 13-14

### 中文翻译
作者总结 XMem 提供通用、低开销的程序语义通道，可提升多种 memory optimization 的效果和可移植性。

---
