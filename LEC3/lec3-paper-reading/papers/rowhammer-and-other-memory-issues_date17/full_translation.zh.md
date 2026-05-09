# Full Chinese Translation

## Title
原文标题：The RowHammer Problem and Other Issues We May Face as Memory Becomes Denser

中文标题：RowHammer 问题与内存密度提高后可能面对的其他问题

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
随着内存密度提高，新 failure mechanisms 可能破坏可靠性和安全性。RowHammer 是 DRAM 电路级扰动导致实际系统漏洞的代表案例。

---

## I-II. RowHammer / RowHammer 问题

### 原文位置
Page 1-3

### 中文翻译
反复打开和关闭同一 DRAM row，会在相邻 rows 中造成可预测 bit flips。该现象违反 memory isolation，并已被多种软件攻击利用。

---

## II-C. Solutions / 解决方案

### 原文位置
Page 2-3

### 中文翻译
短期方案包括提高 refresh rate 和软件检测，但有性能/能耗/侵入性成本。长期方案包括更好 DRAM、ECC、remapping、runtime tracking 和 PARA，其中 PARA 以较低成本随机刷新邻近 rows，但需要 controller/DRAM 支持。

---

## III. Other Vulnerabilities / 其他潜在漏洞

### 原文位置
Page 3-4

### 中文翻译
作者讨论 retention failures、NAND flash read/program interference、PCM 等 emerging memories 中类似 reliability-security 问题。共同根因是高密度下 cell-to-cell interference 和 variation 更严重。

---

## IV. Principled Approach / 原则化方法

### 原文位置
Page 4-5

### 中文翻译
作者主张建立更好的测试、field data、failure model、error mitigation 和 system-memory co-design，避免可靠性问题在部署后变成难以防御的安全漏洞。

---
