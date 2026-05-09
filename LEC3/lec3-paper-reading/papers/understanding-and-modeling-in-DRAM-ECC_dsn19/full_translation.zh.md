# Full Chinese Translation

## Title
原文标题：Understanding and Modeling On-Die Error Correction in Modern DRAM: An Experimental Study Using Real Devices

中文标题：理解和建模现代 DRAM 中的片上错误纠正：基于真实器件的实验研究

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
on-die ECC 会把真实 DRAM errors 纠正或误纠正，使观测错误分布不再直接反映物理机制。EIN 用 MAP estimation 反推出 ECC scheme 和 pre-correction error rates。

---

## 1-2. Motivation / 动机

### 原文位置
Page 1-3

### 中文翻译
厂商为改善 yield 在 DRAM 内加入不可见 ECC，但 JEDEC 不规定实现细节，datasheet 也通常不公开。这会阻碍 runtime optimization、device comparison 和其他 ECC reverse engineering。

---

## 3-5. EIN and EINSim / 方法与工具

### 原文位置
Page 3-8

### 中文翻译
EIN 将 ECC 看作对 pre-correction error distribution 的统计变换。EINSim 模拟 encoding、error injection、decoding 与 checking，用 Monte Carlo 计算 likelihood，再求 MAP。

---

## 6-8. Experimental Study / 实验研究

### 原文位置
Page 8-11

### 中文翻译
作者测试 232 个带 on-die ECC 和 82 个无 on-die ECC 的 LPDDR4 devices。EIN 推断 ECC 为 (136,128,3) Hamming SEC，并恢复 retention error rate 与温度/refresh 的底层关系。

---

## 10. Conclusion / 结论

### 原文位置
Page 11

### 中文翻译
EIN 是理解现代 on-die ECC DRAM 的第一步，它让后续 characterization 能重新看到被 ECC 遮蔽的 pre-correction behavior。

---
