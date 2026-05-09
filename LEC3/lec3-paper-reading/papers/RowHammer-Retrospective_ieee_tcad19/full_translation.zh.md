# Full Chinese Translation

## Title
原文标题：RowHammer: A Retrospective

中文标题：RowHammer 回顾

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
文章回顾 RowHammer：反复访问某个 DRAM row 会在相邻 row 的可预测 bit 位置引发 bit flips。Google Project Zero 之后，多种实际攻击证明它是硬件可靠性问题转化为安全漏洞的代表。

---

## I-II. Problem Summary / 问题总结

### 原文位置
Page 1-4

### 中文翻译
作者复述原始 ISCA 2014 发现、RowHammer 的 circuit-level disturbance 机制、用户态触发方式和可重复 bit flip 特征。129 个模块中 110 个有错误，说明问题广泛存在。

---

## III-A. Attacks / 攻击

### 原文位置
Page 4-6

### 中文翻译
后续攻击包括 kernel privilege escalation、VM takeover、mobile device attack、JavaScript/WebGL/RDMA 远程触发等。核心都是利用 RowHammer 打破 memory isolation。

---

## III-B. Defenses / 防御

### 原文位置
Page 6-9

### 中文翻译
防御包括制造更可靠 DRAM、ECC、提高刷新率、remapping/retirement、runtime detection、access counters、PARA 等。PARA 以低概率 adjacent-row refresh 获得强保证，但需要 controller/DRAM 支持。

---

## IV. Future Directions / 未来方向

### 原文位置
Page 12-15

### 中文翻译
作者把 RowHammer 放到更广泛的 memory scaling/security 语境中，主张通过系统-内存协同、可观测接口、可配置 controller 和更早期的 vulnerability discovery 来避免下一类问题。

---
