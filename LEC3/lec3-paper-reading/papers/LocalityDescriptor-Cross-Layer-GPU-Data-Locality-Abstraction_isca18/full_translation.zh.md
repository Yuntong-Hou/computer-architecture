# Full Chinese Translation

## Title
原文标题：The Locality Descriptor: A Holistic Cross-Layer Abstraction to Express Data Locality in GPUs

中文标题：Locality Descriptor：在 GPU 中表达数据局部性的整体跨层抽象

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文指出 GPU 需要有效利用 cache hierarchy 和未来 NUMA memory hierarchy，但现有 CUDA/OpenCL 主要表达并行性而非数据局部性。Locality Descriptor 让软件表达局部性，硬件据此协调调度、cache 管理和数据放置，带来 cache locality 平均 26.6% 与 NUMA locality 平均 53.7% 的性能提升。

---

## 1-2. Motivation / 动机

### 原文位置
Page 1-4

### 中文翻译
作者用 histo 说明 CTAs 之间共享数据，但硬件难以从地址流自动推断这些语义。单独 CTA scheduling 能减少 working set，却因为 inflight hit 增加而未必提升性能；NUMA 下仅靠 first-touch 也难处理细粒度共享。

---

## 3. Locality Descriptor / 方法

### 原文位置
Page 4-8

### 中文翻译
descriptor 描述数据结构、地址范围、locality type、tile semantics、locality semantics 和 priority。它把程序员/编译器知道的高层语义传给架构，让不同硬件模块以统一接口消费这些信息。

---

## 4-5. Hardware Support / 硬件支持

### 原文位置
Page 8-10

### 中文翻译
硬件侧根据 descriptor 调整 CTA scheduler、cache bypass/prioritization、prefetcher 和 memory placement。关键点不是发明单个策略，而是让多个策略以相同语义协同。

---

## 6. Evaluation / 评估

### 原文位置
Page 10-13

### 中文翻译
实验在多组 GPU benchmark 上显示 descriptor 能把 program semantics 转化为性能。cache locality 场景平均提升 26.6%；NUMA locality 场景平均提升 53.7%，并改善本地访问比例和 zone distribution。

---

## 7-8. Discussion and Conclusion / 讨论与结论

### 原文位置
Page 13-14

### 中文翻译
作者强调 Locality Descriptor 是一种可移植的跨层抽象，可随硬件代际演进映射到不同底层机制。它把 GPU locality 优化从零散技巧变成显式语义接口。

---
