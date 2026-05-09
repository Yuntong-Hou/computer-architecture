# Full Chinese Translation

## Title
原文标题：Panopticon: A Complete In-DRAM Rowhammer Mitigation

中文标题：Panopticon：完整的 in-DRAM RowHammer 缓解机制

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
Panopticon 是完整 in-DRAM RowHammer mitigation。它把 row counters 放在 DRAM 内部，用 row decoding logic 找到对应 counter，并在 DDR4 中复用 ALERTn 暂停 memory controller。

---

## I-II. Motivation / 动机

### 原文位置
Page 1-3

### 中文翻译
已有方案存在快速存储开销和跨层部署障碍。Graphene、BlockHammer、TWiCe 等都需要大量状态，或要求 DRAM 暴露内部映射/支持新命令。

---

## III-V. Design / 设计

### 原文位置
Page 3-5

### 中文翻译
Panopticon 为每行维护 counter，threshold bit toggle 时将 row 放入 service queue。counter mats 采用 open-space、staggered layout，避免改变现有 data mats/sense amplifiers。

---

## VI-VII. Security and Discussion / 安全分析与讨论

### 原文位置
Page 5-6

### 中文翻译
如果只能利用 REF 间隙服务队列，攻击者可能制造连续入队或填满队列。因此 Panopticon 必须能通过 ALERTn 或类似机制向 controller 请求时间。

---

## VIII. Conclusion / 结论

### 原文位置
Page 6-7

### 中文翻译
论文总结 Panopticon 以 DRAM 内部修改为主，绕开 controller/OS 协调难题，但部署仍取决于 DRAM 设计和 ALERTn 行为。

---
