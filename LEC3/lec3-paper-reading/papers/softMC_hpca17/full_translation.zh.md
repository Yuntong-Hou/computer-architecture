# Full Chinese Translation

## Title
原文标题：SoftMC: A Flexible and Practical Open-Source Infrastructure for Enabling Experimental DRAM Studies

中文标题：SoftMC：支持实验性 DRAM 研究的灵活实用开源基础设施

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
SoftMC 是面向 DDR memory modules 的开源 FPGA-based testing platform。它提供灵活 command-level 控制和易用 high-level API，用于真实 DRAM characterization 和机制验证。

---

## 1-3. Motivation / 动机

### 原文位置
Page 1-4

### 中文翻译
DRAM scaling 造成可靠性和 latency 难题，真实芯片实验必不可少。理想平台需要 flexibility 与 ease of use；商业 tester、旧 FPGA 平台和 BIST 都不能同时满足。

---

## 5. SoftMC Design / 设计

### 原文位置
Page 4-6

### 中文翻译
SoftMC 由 host API、driver、FPGA hardware 和 DDR PHY 构成。用户生成 instruction sequence，FPGA 端执行 DDR commands 并返回读数据。WAIT instruction 允许精确控制 timing。

---

## 6. Use Cases / 用例

### 原文位置
Page 7-10

### 中文翻译
retention test 复现已知现象，说明平台能可靠测试真实 DRAM。latency experiments 用 SoftMC 验证最近刷新/访问的 row 是否可降低 tRCD/tRAS，结果在现有芯片不可观察。

---

## 7-10. Limitations and Conclusion / 局限与结论

### 原文位置
Page 10-11

### 中文翻译
SoftMC 不适合直接做系统性能主存控制器，但很适合实验 characterization。作者希望开源工具推动新的 memory system studies。

---
