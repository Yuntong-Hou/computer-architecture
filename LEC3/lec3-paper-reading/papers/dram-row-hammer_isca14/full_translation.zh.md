# Full Chinese Translation

## Title
原文标题：Flipping Bits in Memory Without Accessing Them: An Experimental Study of DRAM Disturbance Errors

中文标题：无需访问即可翻转内存位：DRAM disturbance errors 的实验研究

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文系统研究 DRAM disturbance errors。作者发现大量商品 DDR3 模块在反复访问某些 rows 后，会在未访问的附近 rows 中出现 bit flips，并提出 PARA 作为低开销缓解方案。

---

## 1-3. Background and Methodology / 背景与方法

### 原文位置
Page 1-4

### 中文翻译
DRAM cell 通过 capacitor 存储电荷，wordline activation 会影响邻近 cells。作者使用 FPGA 精确发出 DRAM commands，也在真实 x86 系统上用 loads 与 clflush 构造用户态测试程序。

---

## 4. Experimental Results / 实验结果

### 原文位置
Page 4-8

### 中文翻译
大多数测试 modules/chips 出现 disturbance errors。错误数量与制造年份、refresh interval、activation interval、访问次数和 data pattern 有关。实验还显示某些 vulnerable cells 分布密集，且相邻 row 关系明显。

---

## 5-7. Analysis and Mitigation / 根因与缓解

### 原文位置
Page 8-10

### 中文翻译
根因是反复 toggling wordline 加剧邻近 cells 的电荷泄漏。ECC 不能完全解决多 bit errors；提高 refresh rate 有高开销；PARA 用小概率刷新相邻 rows，以低存储状态和低性能开销显著降低错误概率。

---

## Conclusion / 结论

### 原文位置
Page 11-12

### 中文翻译
作者总结 RowHammer 是真实、普遍且可由软件触发的可靠性/安全问题。未来 DRAM 系统必须在 controller 或 DRAM 内加入 disturbance-aware 机制。

---
