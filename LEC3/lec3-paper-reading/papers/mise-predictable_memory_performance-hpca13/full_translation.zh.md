# Full Chinese Translation

## Title
原文标题：MISE: Providing Performance Predictability and Improving Fairness in Shared Main Memory Systems

中文标题：MISE：在共享主存系统中提供性能可预测性并提升公平性

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
MISE 是一种简单模型，用于估计多程序共享主存时单个应用的 slowdown。它利用 request-service-rate 作为性能代理，并周期性给应用最高优先级来估计独占服务率。

---

## 1-4. Model / 模型

### 原文位置
Page 1-4

### 中文翻译
对于 memory-bound 应用，performance 与 request-service-rate 近似成正比。MISE 用 ARSR/SRSR 估计 slowdown；对 non-memory-bound 应用，引入 stall fraction alpha 来考虑 compute phase。

---

## 5-7. Accuracy and Sensitivity / 准确性与敏感性

### 原文位置
Page 5-6

### 中文翻译
与 STFM 相比，MISE 的平均误差显著更低。epoch 和 interval 过小/过大都会影响估计稳定性，论文选择 5M cycles interval 和 10K cycles epoch。

---

## 8. QoS and Fairness / QoS 与公平性

### 原文位置
Page 8-11

### 中文翻译
MISE-QoS 根据 slowdown estimate 给 applications of interest 分配刚好足够的 bandwidth；MISE-Fair 则动态调整目标 bound 和带宽分配，以降低 maximum slowdown。

---

## 10. Conclusion / 结论

### 原文位置
Page 12

### 中文翻译
作者总结 MISE 可作为更可预测、更可控 shared-memory systems 的基础，并计划将类似模型扩展到其他共享资源。

---
