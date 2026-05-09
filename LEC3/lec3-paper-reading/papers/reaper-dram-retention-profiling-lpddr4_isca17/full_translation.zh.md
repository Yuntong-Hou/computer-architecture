# Full Chinese Translation

## Title
原文标题：The Reach Profiler (REAPER): Enabling the Mitigation of DRAM Retention Failures via Profiling at Aggressive Conditions

中文标题：REAPER：通过激进条件下的 profiling 缓解 DRAM retention failures

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
现代 DRAM refresh 标准为了覆盖最坏保持时间 cells，给所有 cells 统一 64ms 刷新，造成能耗和性能损失。REAPER 的思路是用更激进的 refresh interval 或温度做 profiling，在更短时间内发现目标条件下的绝大多数失败 cells。

---

## 1. Introduction / 引言

### 原文位置
Page 1-2

### 中文翻译
作者指出许多 refresh reduction 工作假定 profiling 可以快速完成，但 brute-force profiling 既慢又会受 VRT/DPD 影响。论文提出 coverage、false positive rate 和 runtime 三个指标来评价 profiling，并在 368 颗 LPDDR4 chips 上实证分析。

---

## 2-4. Background and Profiling / 背景与 profiling

### 原文位置
Page 2-4

### 中文翻译
DRAM cell 因漏电需要周期性 refresh。若延长 refresh interval，少量弱 cells 会失败。传统方法逐模式等待目标 interval 并读回检查；REAPER 则把 profiling 移到更高压力条件，使弱 cells 更快、更稳定地暴露。

---

## 5-6. Characterization and Model / 表征与模型

### 原文位置
Page 4-9

### 中文翻译
实验显示 retention failures 随 refresh interval 和温度增加而增长，且失败集合会随时间累积。作者用 UBER/RBER 和 ECC 模型估计可容忍遗漏 failures，并把它转化为 profile longevity。

---

## 7. End-to-End Evaluation / 端到端评估

### 原文位置
Page 10-13

### 中文翻译
系统评估表明，REAPER 因 profiling runtime 低，可支撑 512ms 到 1024ms 等更长 refresh intervals。相比 brute-force，它在长 refresh interval 下保留更多理想收益，并降低 profiling 引起的性能损失。

---

## 9. Conclusion / 结论

### 原文位置
Page 13

### 中文翻译
论文总结 reach profiling 是许多 past/future refresh reduction techniques 的 enabler，因为它让在线、高覆盖、可控误报的 retention profiling 变得可行。

---
