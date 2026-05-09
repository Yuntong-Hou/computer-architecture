# Full Chinese Translation

## Title
原文标题：Phase-Change Technology and the Future of Main Memory

中文标题：相变技术与主存的未来

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Title and Overview / 标题与概览

### 原文位置
Page 1

### 中文翻译
文章讨论 PCM 是否可成为未来主存。PCM 可缩放、非易失，但必须解决比 DRAM 更高的访问延迟、写功耗和磨损问题。

---

## Technology / 技术基础

### 原文位置
Page 1-4

### 中文翻译
PCM cell 由 heater 与 chalcogenide 构成。RESET 用高短脉冲形成 amorphous 高阻态，SET 用较长脉冲形成 crystalline 低阻态。写入是主要 wear 来源。

---

## Architecting PCM / 架构设计

### 原文位置
Page 4-6

### 中文翻译
通过把单个宽 buffer 改为多个窄 buffers，可减少写入粒度、提高 row locality 和 write coalescing，从而把 PCM delay/energy 接近 DRAM。

---

## Wear Reduction / 磨损降低

### 原文位置
Page 7-9

### 中文翻译
redundant bit-write removal、row shifting 和 segment swapping 分别从 bit、row 和 segment 粒度减少并均衡写入，使 projected lifetime 达到多年到十多年。

---

## Implications / 启示

### 原文位置
Page 9-11

### 中文翻译
PCM 的非易失性可能改变 memory hierarchy，但需要软件理解 persistence，并处理一致性、安全和磨损问题。

---
