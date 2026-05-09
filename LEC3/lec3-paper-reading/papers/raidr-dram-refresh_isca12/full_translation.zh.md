# Full Chinese Translation

## Title
原文标题：RAIDR: Retention-Aware Intelligent DRAM Refresh

中文标题：RAIDR：保持时间感知的智能 DRAM 刷新

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
RAIDR 根据 DRAM cells retention time 差异减少 refresh。它把 rows 放入不同 retention bins，并使用 Bloom filters 低开销存储这些 bins。

---

## 1-2. Motivation / 动机

### 原文位置
Page 1-3

### 中文翻译
refresh 会降低性能和能效，且随容量增加更严重。大多数 cells 能保持数据远超 64ms，因此统一最坏情况 refresh 是浪费。

---

## 3. RAIDR Design / 设计

### 原文位置
Page 4-6

### 中文翻译
RAIDR 先 profile 每行 retention time，然后在 memory controller 中保存 bins。Bloom filters 没有 false negatives，能保证不会漏刷新弱 rows。

---

## 5-6. Evaluation / 评估

### 原文位置
Page 6-10

### 中文翻译
RAIDR 显著减少 refreshes，提升性能并降低能耗；收益在 extended temperature 和未来更高 density 下更大。

---

## 7. Conclusion / 结论

### 原文位置
Page 10-12

### 中文翻译
作者总结 RAIDR 是一种低成本 controller 修改，可缓解当前和未来 DRAM refresh overhead。

---
