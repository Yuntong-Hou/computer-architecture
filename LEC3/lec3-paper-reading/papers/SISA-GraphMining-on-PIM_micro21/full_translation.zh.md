# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 SISA 的 set-centric programming paradigm、ISA primitives、PUM/PNM 映射、graph mining workloads、评估、局限和硬件工程师视角。保留 set-centric、PIM、PUM、PNM、bitvector、sparse array、graph mining 等术语。

## Title

原文标题：SISA: Set-Centric Instruction Set Architecture for Graph Mining on Processing-in-Memory

中文标题：SISA：面向 PIM 图挖掘的集合中心指令集架构

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

复杂 graph mining 任务，如 clique listing、pattern matching、graph learning，常花大量时间执行 vertex set operations。传统 graph accelerators 多关注 BFS/PageRank 等 vertex-centric 算法，不适合表达复杂集合操作。

SISA 提出 set-centric programming paradigm，把 graph mining 重写为集合交、并、差、计数等操作，并将这些操作提升为 ISA primitives。硬件根据 set representation 选择 PUM 或 PNM 加速：高 degree dense bitvectors 适合 in-DRAM bitwise PUM，低 degree sparse arrays 适合 near-memory PNM。

## 1. Motivation / 动机

### 原文位置

Page 1 - Page 3 / Table 1

### 中文翻译

复杂 graph mining 与传统 graph processing 不同。它不是简单遍历所有 vertices/edges，而是反复对邻接集合求交、差、包含关系和计数。软件中这些 set operations 会产生大量 memory traffic 和 branch/control overhead。

Vertex-centric、edge-centric、linear algebra、joins 等抽象都不能很好覆盖复杂 graph mining。Set-centric abstraction 更接近算法本质。

## 2. SISA Design / SISA 设计

### 原文位置

Page 4 - Page 8 / Figure 2, Table 4

### 中文翻译

SISA 在软件层提供 set-centric formulations 和 thin wrappers；在 ISA 层定义 set instructions；在硬件层由 SISA Controller Unit 执行或调度 set operations。

Set representation 有两类：dense bitvector 和 sparse integer array。Dense bitvector 适合高 degree vertices，可用 PUM 在 DRAM 内部进行 bitwise AND/OR/XOR。Sparse array 适合低 degree vertices，可用 PNM merge/galloping 等近内存逻辑处理。

SISA instructions 覆盖 set union、intersection、difference、count、membership、iteration 等变体。Controller 根据 degree、threshold、representation 和操作类型选择最佳执行路径。

## 3. Evaluation / 评估

### 原文位置

Page 11 - Page 14 / Figures 6-8

### 中文翻译

论文用多种 graph mining workloads 和真实图数据评估 SISA。结果显示，SISA-enhanced algorithms 对 maximal clique listing 等任务相对 established Bron-Kerbosch 获得超过 10x speedup。Figure 6/8 展示在 full parallelism 和 large graphs 下，SISA 对 non-set/set-based baselines 有显著加速。

性能依赖 set representation、degree distribution、threshold 和 load balancing。Representation 选择错误会降低收益。

## 4. Discussion and Limitations / 讨论与局限

### 原文位置

Design/evaluation discussion

### 中文翻译

SISA 需要算法以 set-centric 形式重写或包装，软件生态有迁移成本。PUM/PNM 硬件假设也较强，真实商业内存系统需要 ISA、runtime、memory substrate 支持。

对动态图或小图，格式转换和调度开销可能削弱收益。负载不均衡也是复杂图挖掘的重要问题。

## 5. 硬件工程师视角

SISA 的启发是：为复杂 workload 加速时，应找真正的 common primitive。对 graph mining，primitive 不是 vertex visit，而是 set algebra。

硬件实现重点是 representation-aware execution。Dense bitvectors 和 sparse arrays 的最佳硬件完全不同。一个好的 accelerator 需要 runtime threshold 和动态选择。

## 6. 不确定与需回原文核对

- Table 4 ISA definitions 需回 PDF；
- Figure 6/8 性能结果和 workload 设置建议核对；
- PUM/PNM 具体硬件假设需结合原文细节。
