# Full Chinese Translation

## Title
原文标题：HARP: Practically and Effectively Identifying Uncorrectable Errors in Memory Chips That Use On-Die Error-Correcting Codes

中文标题：HARP：在使用 On-Die ECC 的内存芯片中实用且有效地识别不可纠正错误

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文指出内存密度提升加剧错误率，而 on-die ECC 虽能在芯片内部隐藏错误，却会混淆内存控制器对错误的观察，阻碍 bit-level repair 所需的 error profiling。HARP 把 ECC 后不可纠正错误分解为 direct errors 与 indirect errors，并用 hybrid active-reactive profiling 更快达到覆盖。

---

## 1. Introduction / 引言

### 原文位置
Page 1-2

### 中文翻译
作者解释 scaling-related errors、repair mechanism 与 on-die ECC 之间的矛盾：repair 需要知道哪些 bit 有风险，但 on-die ECC 会先修改错误表现形式。传统 profiling 要么只能观察 correction 后结果，要么需要大量测试轮次。

---

## 2-4. Background and Analysis / 背景与分析

### 原文位置
Page 2-8

### 中文翻译
论文回顾 repair granularity、active/reactive profiling、error model 与 on-die ECC，并形式化说明 ECC 如何使 bit errors 之间不再独立。关键结论是，控制器外部看到的 post-correction errors 并不直接对应 raw errors。

---

## 5-6. HARP / 方法

### 原文位置
Page 8-12

### 中文翻译
HARP 的 active phase 利用修改后的 read operation 读取 raw data values，尽快找出 direct at-risk bits；reactive phase 利用 memory-controller secondary ECC 在实际运行时检测和安全标记 indirect errors。HARP-U 不知道校验矩阵，HARP-A 知道并利用校验矩阵辅助 indirect 部分。

---

## 7-8. Evaluation and Case Study / 评估

### 原文位置
Page 12-17

### 中文翻译
实验显示 HARP 相比 baseline 更快达到高覆盖率，尤其在 pre-correction errors 数量增加时优势明显。BER case study 表明，更快且完整的 profiling 能让 repair mechanism 更早覆盖所有需要修复的错误。

---

## 9. Conclusion / 结论

### 原文位置
Page 17-18

### 中文翻译
作者总结 HARP 解决了 on-die ECC 给 profiling 带来的三个核心困难，说明未来内存可靠性机制不能忽略芯片内 ECC 对系统可见错误的改变。

---
