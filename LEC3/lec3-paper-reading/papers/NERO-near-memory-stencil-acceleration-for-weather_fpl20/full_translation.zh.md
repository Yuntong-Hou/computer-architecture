# Full Chinese Translation

## Title
原文标题：NERO: A Near High-Bandwidth Memory Stencil Accelerator for Weather Prediction Modeling

中文标题：NERO：面向天气预报建模的近 HBM stencil 加速器

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
NERO 针对天气预测模型中的 compound stencil kernel，使用 FPGA+HBM 近内存加速。实验显示 vadvc/hdiff 相比 16-core POWER9 分别快 4.2x/8.3x，能耗降低 22x/29x。

---

## 1-2. Background / 背景

### 原文位置
Page 1-3

### 中文翻译
COSMO dycore 包含 horizontal stencils、vertical tridiagonal solvers 和 point-wise computation。vadvc 与 hdiff 代表这种复杂访问和低算术强度，roofline 表明 CPU 受 DRAM 带宽限制。

---

## 3. NERO Design / 设计

### 原文位置
Page 3-5

### 中文翻译
NERO 通过 CAPI2/SNAP 连接 host 与 FPGA。数据从 host 传入 FPGA/HBM，多个 PE 使用独立 HBM ports 和 URAM/BRAM/HBM 层次读取邻域数据。auto-tuning 用于选择 tile/window 和资源配置。

---

## 4. Evaluation / 评估

### 原文位置
Page 5-7

### 中文翻译
HBM-based design 随 PE 增加取得更好扩展，相比 DDR4-FPGA 更能支撑 stencil bandwidth。最终设计在性能和能效上均明显优于 POWER9。

---

## 5-6. Related Work and Conclusion / 相关工作与结论

### 原文位置
Page 8-9

### 中文翻译
作者认为 near-HBM FPGA 是天气预测建模的有前景路线，但核心在于根据 kernel 访问模式定制 memory hierarchy 和并行结构。

---
