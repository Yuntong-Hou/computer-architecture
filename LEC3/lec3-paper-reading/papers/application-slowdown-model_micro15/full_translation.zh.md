# Full Chinese Translation

## Title
原文标题：The Application Slowdown Model: Quantifying and Controlling the Impact of Inter-Application Interference at Shared Caches and Main Memory

中文标题：Application Slowdown Model：量化并控制共享 cache 与主存处跨应用干扰的影响

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文提出 ASM，用于在线估计共享 cache 和主存干扰造成的应用 slowdown。ASM 不需要事先知道应用行为，在 100 个 workloads 上平均误差为 9.9%，并能驱动多种共享资源管理策略。

---

## 1-3. Motivation / 动机与模型直觉

### 原文位置
Page 1-4

### 中文翻译
多核环境中，应用之间的 cache contention 和 memory bandwidth contention 会共同影响性能。作者观察到应用 performance 与 shared cache access rate 高度相关，因此可用 CARalone/CARshared 作为 slowdown 近似。

---

## 4-5. ASM Mechanism / 机制

### 原文位置
Page 4-6

### 中文翻译
ASM 通过周期性给应用 high memory priority 来估计不受 memory bandwidth interference 时的 CAR；再借助 auxiliary tag store 估计无 cache contention 时的行为。多个硬件计数器共同构成 online slowdown estimator。

---

## 6. Evaluation / 评估

### 原文位置
Page 6-9

### 中文翻译
实验显示 ASM 的平均误差显著低于 FST 和 PTCA，即使使用 sampled ATS 也保持较高准确性；数据库 workloads 的误差尤其低。

---

## 7. Use Cases / 用例

### 原文位置
Page 9-12

### 中文翻译
ASM 被接入 cache partitioning、memory bandwidth partitioning、QoS guarantee 和 fair pricing。核心思想是用估计 slowdown 作为优化目标，而不是只优化总吞吐或局部 miss rate。

---

## Conclusion / 结论

### 原文位置
Page 13-14

### 中文翻译
作者认为 slowdown 是共享资源系统中更接近用户体验和公平性的指标；ASM 提供了足够准确且可部署的在线估计方法。

---
