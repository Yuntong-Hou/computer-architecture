# Full Chinese Translation

## Title
原文标题：Self-Optimizing Memory Controllers: A Reinforcement Learning Approach

中文标题：自优化内存控制器：一种强化学习方法

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
作者提出 self-optimizing memory controller，通过 reinforcement learning 在线学习 DRAM scheduling policy。结果显示在 4-core CMP 上比 FR-FCFS 平均提升 19%，并提升带宽利用率。

---

## 1-2. Motivation / 动机

### 原文位置
Page 1-3

### 中文翻译
CMP 需要更高 off-chip bandwidth，但传统 fixed policy 不能预判长期影响，也不能适应 workload 动态变化。DRAM scheduling 同时受 timing constraints、row buffer locality、bank conflicts 和 request criticality 影响。

---

## 3. RL-Based Scheduling / RL 调度设计

### 原文位置
Page 4-7

### 中文翻译
scheduler 被建模为 RL agent。state 包含 transaction queue 和 request 属性；actions 是合法 DRAM commands；reward 奖励利用 data bus 的命令。CMAC 结构用于压缩巨大 state space 并实现 generalization。

---

## 4-5. Evaluation / 实验评估

### 原文位置
Page 8-11

### 中文翻译
实验用九个 memory-intensive parallel workloads。RL 相比 FR-FCFS 提升性能和 bus utilization，显著优于 offline RL、FR-FCFS derivatives 和 Fair Queueing。多控制器实验说明无需显式协调也能收敛。

---

## 7. Conclusions / 结论

### 原文位置
Page 12

### 中文翻译
论文总结 RL controller 能在线适应并降低人工调度策略设计负担，是更高效利用 DRAM bandwidth 的有前景路径。

---
