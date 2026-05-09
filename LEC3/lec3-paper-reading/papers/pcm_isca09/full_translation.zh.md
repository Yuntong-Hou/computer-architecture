# Full Chinese Translation

## Title
原文标题：Architecting Phase Change Memory as a Scalable DRAM Alternative

中文标题：将相变存储器架构为可缩放 DRAM 替代方案

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文提出把 PCM 作为 DRAM 替代时所需的架构增强。baseline PCM 慢且耗能，但 area-neutral buffer reorganizations 和 partial writes 可使其性能、能耗和寿命接近可用。

---

## 1-2. PCM Technology / PCM 技术

### 原文位置
Page 1-4

### 中文翻译
PCM 通过相变材料的电阻差存储数据。SET/RESET 分别形成晶态/非晶态。论文从近五年 prototype 中导出保守 read/write/endurance 参数。

---

## 3-4. Buffer Organization / 缓冲组织

### 原文位置
Page 4-7

### 中文翻译
PCM read nondestructive、write expensive，适合把 sensing 与 buffering 分离。窄 buffer 降低每次 array write 能耗，多 buffer rows 捕获局部性并提升 write coalescing。

---

## 5. Partial Writes / 部分写

### 原文位置
Page 8-10

### 中文翻译
partial writes 从 cache 传递 dirty granularity，只写修改过的数据。endurance model 显示 4B granularity 可把平均寿命提升到 5.6 years。

---

## Conclusion / 结论

### 原文位置
Page 10-12

### 中文翻译
作者总结 PCM 的可扩展性和非易失性很有吸引力，但只有结合架构优化才能成为实际主存替代。

---
