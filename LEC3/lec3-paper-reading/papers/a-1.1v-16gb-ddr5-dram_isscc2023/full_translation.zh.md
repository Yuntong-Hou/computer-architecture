# Full Chinese Translation

## Title
原文标题：A 1.1V 16Gb DDR5 DRAM with Probabilistic-Aggressor Tracking, Refresh-Management Functionality, Per-Row Hammer Tracking, a Multi-Step Precharge, and Core-Bias Modulation for Security and Reliability Enhancement

中文标题：一种 1.1V 16Gb DDR5 DRAM：面向安全与可靠性的概率 aggressor 跟踪、RFM、逐行 hammer 跟踪、多步预充电与 core-bias 调制

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Title and Summary / 标题与概要

### 原文位置
Page 1

### 中文翻译
本文介绍一颗 1.1V、16Gb DDR5 DRAM，目标是在 1a-nm 缩放节点下增强安全性和可靠性。论文把 RowHammer mitigation、refresh management、per-row tracking、多步预充电和 core-bias 调制组合在同一芯片中。

---

## RFM and PAT / RFM 与概率跟踪

### 原文位置
Page 1-2

### 中文翻译
控制器统计 row activation accumulation count，并在达到阈值时发送 RFM command。芯片内部的 probabilistic-aggressor tracking 进一步帮助识别高风险 aggressor rows，以便对相邻 rows 进行 refresh。

---

## PRHT and Precharge / PRHT 与预充电

### 原文位置
Page 2

### 中文翻译
PRHT 使用 R/H cells 保存每条 wordline 的 hammer 计数，通过内部 read-modify-write 更新状态；当计数超过阈值时，芯片对相邻 row 进行额外 refresh。multi-step precharge 通过改善电路层行为提升 intrinsic row hammer tolerance。

---

## Retention Enhancement / retention 增强

### 原文位置
Page 3

### 中文翻译
core-bias modulation 根据温度调节 VBB，以提升高温下的 retention time。测量结果显示在 90C 时 refresh retention time 提升 17%。

---

## Conclusion / 结论

### 原文位置
Page 3

### 中文翻译
论文说明现代 DDR5 DRAM 的可靠性需要协议、架构和电路联合设计；单独依赖外部控制器或单一阈值策略不足以覆盖 row hammer 与 retention 问题。

---
