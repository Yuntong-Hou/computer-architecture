# Full Chinese Translation

## Title
原文标题：The Virtual Block Interface: A Flexible Alternative to the Conventional Virtual Memory Framework

中文标题：Virtual Block Interface：传统虚拟内存框架的灵活替代方案

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
VBI 是传统虚拟内存的替代框架。它向应用暴露 variable-sized virtual blocks，把 access protection 与 memory allocation/address translation 分离，并由 memory-controller hardware 管理物理分配和翻译。

---

## 1-3. Motivation and Overview / 动机与总览

### 原文位置
Page 1-4

### 中文翻译
虚拟化、地址翻译和异构内存让传统 page-table-centric 框架变得复杂。VBI 用全局 VB address space 表示语义对象，OS 控制权限，MTL 管理底层物理资源。

---

## 4-6. Detailed Design / 详细设计

### 原文位置
Page 4-8

### 中文翻译
论文定义 VB、memory clients、CVT、VIT、VBI address、MTL 操作和 VM/multinode 支持。VBI 可支持 VIVT caches、避免 2D page walks、delayed allocation 和 flexible translation structures。

---

## 7. Evaluation / 评估

### 原文位置
Page 8-12

### 中文翻译
地址翻译实验显示 VBI 减少 TLB/translation-related memory accesses；异构内存实验显示 VBI 能根据 hotness/latency sensitivity 更好放置数据。

---

## 9. Conclusion / 结论

### 原文位置
Page 13-14

### 中文翻译
作者认为重新设计 virtual memory framework 可以比不断给传统框架打补丁更好地适配未来多样化系统。

---
