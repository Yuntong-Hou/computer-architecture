# Full Chinese Translation

## Title
原文标题：AVATAR: A Variable-Retention-Time (VRT) Aware Refresh for DRAM Systems

中文标题：AVATAR：面向 DRAM 系统的 Variable-Retention-Time 感知刷新

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
AVATAR 面向 VRT-aware DRAM refresh。它用 ECC 和 scrubbing 在运行时发现由 VRT 造成的错误，并把相关 rows 动态提升到 fast refresh rate，从而显著提升 multirate refresh 的可靠性。

---

## 1-3. Background / 背景

### 原文位置
Page 1-4

### 中文翻译
DRAM 密度提升带来 Refresh Wall。传统 multirate refresh 假设 retention profile 相对稳定，但 VRT cells 会随时间进入低 retention 状态，使离线测试不再可靠。

---

## 4. VRT Model / VRT 模型

### 原文位置
Page 4-6

### 中文翻译
作者用 Active-VRT Pool 和 Active-VRT Injection 描述 VRT 动态行为。短时间窗口内 active VRT cells 数量有限，但持续运行时会不断出现新的风险 cells。

---

## 5. AVATAR Design / 设计

### 原文位置
Page 6-8

### 中文翻译
AVATAR 在已有 retention profile 基础上运行。ECC correctable errors 作为 VRT 信号，scrubbing 周期性扫描内存；一旦发现可纠正 retention error，就把对应 row 加入 fast refresh table。

---

## 6. Evaluation / 评估

### 原文位置
Page 8-10

### 中文翻译
结果显示 AVATAR 同时提升可靠性和保持 refresh savings。相比 VRT-agnostic multirate refresh，TTF 从数月提升到数十年或更久，并在高密度 DRAM 上显著改善 performance 和 EDP。

---

## Conclusion / 结论

### 原文位置
Page 10-11

### 中文翻译
作者总结 VRT-aware dynamic promotion 是让 refresh reduction 实用化的关键：系统不必为最坏情况刷新所有 rows，而可以在运行时发现和隔离新变弱的 rows。

---
