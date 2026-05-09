# Full Chinese Translation

## Title
原文标题：The Efficacy of Error Mitigation Techniques for DRAM Retention Failures: A Comparative Experimental Study

中文标题：DRAM retention failures 错误缓解技术有效性：一项比较实验研究

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文比较 memory tests、guardbands 和 ECC 对真实 DRAM retention failures 的缓解效果。结果表明，依赖 runtime testing alone 的技术无法保证可靠运行，而结合 ECC 的技术可在数小时甚至更短测试后达到强可靠性。

---

## 1-3. Background / 背景

### 原文位置
Page 1-4

### 中文翻译
retention failure 来自电容漏电。VRT 与 data pattern sensitivity 让 failure 间歇出现，因此制造测试无法一次性捕获所有问题。在线 profiling 有望把测试成本摊到系统运行期。

---

## 4-5. Testing and Guardband / 测试与保护裕量

### 原文位置
Page 5-9

### 中文翻译
少量 testing rounds 能发现多数 weak cells，但部分 VRT cells 长时间处于非失效状态，导致新 failures 持续出现。guardband 对多数相近 retention states 有效，但对状态差异很大的 VRT cells 无效。

---

## 6-7. ECC and Prior Techniques / ECC 与已有方案

### 原文位置
Page 10-11

### 中文翻译
ECC 与 testing/guardbanding 的组合远强于单独技术。bit repair 类方案在 intermittent failures 下失败风险高，VS-ECC/Hi-ECC 等 ECC-based 机制更适合与在线 profiling 配合。

---

## 8-9. Online Profiling and Conclusion / 在线画像与结论

### 原文位置
Page 12-14

### 中文翻译
作者建议未来系统使用持续、低开销在线 profiling，先用较强 ECC 保证初始可靠性，再随发现的 failures 调整保护强度或修复策略。

---
