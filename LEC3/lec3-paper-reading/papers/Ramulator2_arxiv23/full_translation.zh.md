# Full Chinese Translation

## Title
原文标题：Ramulator 2.0: A Modern, Modular, and Extensible DRAM Simulator

中文标题：Ramulator 2.0：现代、模块化、可扩展的 DRAM 模拟器

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
Ramulator 2.0 是模块化、可扩展的 DRAM simulator，支持快速实现 memory controller 与 DRAM design changes。它提供独立接口、简洁 DRAM spec syntax、新标准支持、RowHammer mitigation plugins，并以 MIT license 开源。

---

## 1. Introduction / 引言

### 原文位置
Page 1

### 中文翻译
作者指出现有模拟器难以承载 intrusive design changes，因为 controller、DRAM spec、时序和功能实现耦合。Ramulator 2.0 的目标是让新标准、新调度、新 mitigation 能以模块方式加入。

---

## 2. Design Features / 设计特性

### 原文位置
Page 2-3

### 中文翻译
框架用 Interface 和 Implementation 抽象组件，配置文件实例化具体实现。DRAM specification 使用 human-readable 字符串、permutation timing constraints 和 templated lambda functions，减少重复代码。

---

## 3. Evaluation / 验证与案例

### 原文位置
Page 3-4

### 中文翻译
作者通过命令 trace 对照 Verilog model 验证正确性，比较 simulation speed，并以六种 RowHammer mitigation 展示 controller plugin 能力。

---

## Conclusion / 结论

### 原文位置
Page 4

### 中文翻译
Ramulator 2.0 的价值在于让内存系统研究更敏捷：研究者可以更快实现复杂 controller/DRAM 修改，并在统一框架中比较。

---
