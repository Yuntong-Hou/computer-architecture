# Full Chinese Translation

## Title
原文标题：RowPress: Amplifying Read Disturbance in Modern DRAM Chips

中文标题：RowPress：放大现代 DRAM 芯片中的读扰动

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
论文展示 RowPress：不是反复 hammer，而是把 DRAM row 长时间保持打开，也能扰动相邻 row。它显著降低触发 bitflip 所需 activation 数，影响三大厂商 DDR4 芯片，并可在真实系统中触发。

---

## 1-3. Motivation and Methodology / 动机与方法

### 原文位置
Page 1-5

### 中文翻译
作者定义 tAggON 和 ACmin，构建温控 DDR4 测试基础设施，禁用纠错干扰以直接观察 circuit-level bitflips，并扫多种访问模式与温度。

---

## 4-5. Characterization / 表征

### 原文位置
Page 5-11

### 中文翻译
随着 tAggON 增加，ACmin 大幅下降。RowPress vulnerable cells 与 RowHammer/retention vulnerable cells 基本不同，且温度、single/double-sided 模式和 tAggOFF 会改变其行为。

---

## 6-7. System Demo and Mitigation / 系统演示与防御

### 原文位置
Page 12-16

### 中文翻译
用户态程序可在带 RowHammer 防御的 DDR4 系统中利用 RowPress 触发 bitflips。作者提出把现有防御适配为 Graphene-RP/PARA-RP，以较低额外性能开销同时覆盖 RowPress。

---

## 9. Conclusion / 结论

### 原文位置
Page 17-18

### 中文翻译
RowPress 表明 read disturbance 的安全边界比 RowHammer activation count 更宽。未来 DRAM 防御需要把 row-open duration 纳入威胁模型。

---
