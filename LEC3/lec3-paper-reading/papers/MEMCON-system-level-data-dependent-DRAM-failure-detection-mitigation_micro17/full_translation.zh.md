# Full Chinese Translation

## Title
原文标题：Detecting and Mitigating Data-Dependent DRAM Failures by Exploiting Current Memory Content

中文标题：利用当前内存内容检测并缓解数据相关 DRAM 失效

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文研究 data-dependent DRAM failures。由于完整检测所有内容组合需要了解每颗芯片的内部结构，MEMCON 改为在线检测当前内存内容会触发的失效，并在测试后用更低刷新率保护未失败的行。

---

## 1-2. Background and Motivation / 背景与动机

### 原文位置
Page 1-4

### 中文翻译
作者解释 DRAM scaling 加剧 cell-to-cell interference，而地址 scrambling、column remapping 等厂商内部设计使系统很难知道哪些 cell 互为邻居。实验动机表明，程序实际内容触发的失效少于所有可能内容，因此可以只围绕当前内容做检测。

---

## 3. MEMCON Design / 方法

### 原文位置
Page 4-6

### 中文翻译
MEMCON 在写入后根据预测决定是否测试。测试有 Read-and-Compare 与 Copy-and-Compare 两种模式；若测试通过，行进入低刷新状态；若失败或不测试，则继续高刷新或采用其他缓解。MinWriteInterval 用来判定测试成本能否被摊销。

---

## 4. PRIL Predictor / 写间隔预测

### 原文位置
Page 6-8

### 中文翻译
PRIL 基于 Pareto 分布的性质：一个页面在写后已经保持越久，未来继续保持的期望也越长。作者用这个性质识别值得测试的长写间隔。

---

## 5-6. Evaluation / 评估

### 原文位置
Page 8-13

### 中文翻译
实验显示真实应用中长写间隔占据大部分时间，MEMCON 可减少约 64.7%-74.5% refresh operations。相对 aggressive refresh，它在 8/16/32Gb DRAM 下带来明显性能提升，同时 testing 产生的额外读写干扰较小。

---

## 7. Conclusion / 结论

### 原文位置
Page 13-14

### 中文翻译
作者总结 MEMCON 通过利用当前内容，提供了一条不依赖 DRAM 内部组织的系统级检测/缓解路线，尤其适合以刷新开销换可靠性的未来高密度 DRAM。

---
