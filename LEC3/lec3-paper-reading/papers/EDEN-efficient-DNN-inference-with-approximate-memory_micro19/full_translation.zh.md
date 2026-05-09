# Full Chinese Translation

## 版权与完整性说明
以下为逐节中文详译/译述，覆盖论文主体、实验和结论；不提供逐字长篇翻译。

## Title
原文标题：EDEN: Enabling Energy-Efficient, High-Performance Deep Neural Network Inference Using Approximate DRAM

中文标题：EDEN：使用近似 DRAM 实现高能效、高性能 DNN 推理

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
DNN inference 对能效和性能要求很高，而 DRAM energy 和 latency 常成为瓶颈。approximate DRAM 通过降低 voltage 或 latency 超出标准规格来节能/加速，但会产生更高 bit error rate。EDEN 利用 DNN 的 error tolerance，通过 retraining 和 data mapping，在满足用户 accuracy target 的同时使用 approximate DRAM。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2

### 中文翻译
DNN 模型越来越大，memory footprint 和 off-chip access 增长。DRAM 可占 DNN 系统能耗的重要部分，LLC miss latency 也会阻塞推理。已有工作通过压缩、量化、PIM 或新 DRAM 结构优化 memory efficiency；EDEN 则采取正交方向：调整现有 DRAM 的运行参数，让它以更低 voltage/latency 近似运行。

EDEN 建立在两个观察上：DNN 对输入、权重和输出中的错误有容忍性；DRAM 参数可以用可靠性换性能/能耗。

## 2. Background / 背景

### 原文位置
Page 2 - Page 3

### 中文翻译
论文介绍 DNN data types：input feature maps（IFMs）、output feature maps（OFMs）和 weights。不同 layer 和 data type 的 memory access 行为、数值范围和 error sensitivity 不同。DRAM 方面，论文回顾 cell、subarray、bank、timing 参数和 voltage/latency scaling。

## 3. EDEN Framework / EDEN 框架

### 原文位置
Page 3 - Page 5; Figure 4

### 中文翻译
EDEN 包含三步。第一，boosting DNN error tolerance：用 approximate DRAM 的 error characteristics 在训练中注入错误，使 DNN 适应目标设备。第二，DNN error tolerance characterization：测量各 DNN data type 可承受的 maximum BER。第三，DNN-to-DRAM mapping：把不同数据放到不同 approximate DRAM partitions，使每部分 BER 不超过其容忍阈值，并尽量降低 voltage/latency。

curricular retraining 是第一步的关键。若一开始注入高 error rate，训练可能 accuracy collapse；EDEN 逐步增加 error rate，使模型渐进适应。对浮点 exponent bit 导致的异常值，EDEN 也提供 correction/saturation/zeroing 类机制避免训练崩溃。

## 4. Error Models / 错误模型

### 原文位置
Page 6 - Page 8

### 中文翻译
EDEN 需要 approximate DRAM 的 error model，以便在训练和离线 mapping 中模拟真实错误。作者从真实 DDR3/DDR4 模块在 reduced voltage 和 reduced latency 下的错误分布构造四类 probabilistic models，覆盖 uniform、row/bitline locality、data pattern dependence 等现象。

这些模型用于 EDEN offloading：即使目标 approximate DRAM 不在训练机器上，也能用 error model 注入近似错误进行 retraining。

## 5. DNN Characterization / DNN 表征

### 原文位置
Page 8 - Page 11

### 中文翻译
作者表征不同 DNN 在不同 BER、precision、layer 和 data type 下的 accuracy。结果显示，较低 precision 通常更敏感；first/last layers 比中间层更敏感；weights 通常比 IFMs 更能容忍错误；magnitude-based pruning 对 error resilience 影响不显著。

fine-grained characterization 能让不同 IFMs/weights 映射到不同 DRAM partitions，从而比 coarse-grained mapping 使用更激进的 voltage reduction。

## 6. System-Level Evaluation / 系统级评估

### 原文位置
Page 11 - Page 12

### 中文翻译
CPU 评估显示，在 <1% accuracy loss 下，EDEN 平均节省 21% DRAM energy；若要求与原始 accuracy 相同，仍有 16% 平均 energy saving。降低 tRCD 在 latency-bound networks 上带来平均 8%、最高 17% speedup。

GPU 评估显示，EDEN 对 YOLO/YOLO-Tiny 等 workload 平均降低 37% DRAM energy，平均 speedup 2.7%。Eyeriss 和 TPU 评估显示，降低 DDR4 voltage 分别带来 31% 和 32% 平均 DRAM energy savings；但 reduced tRCD 对这些 accelerator 没有 speedup，因为其 dataflow/prefetch 使 memory access 更可预测。

## 7. Related Work / 相关工作

### 原文位置
Page 12 - Page 13

### 中文翻译
相关工作包括 DNN approximate hardware、reduced refresh、low-voltage SRAM、approximate arithmetic、emerging memory、approximate storage 和随机 error injection。EDEN 的区别是使用真实 approximate DRAM error characterization，并将 DNN retraining 与 memory partition mapping 结合。

## 8. Conclusion / 结论

### 原文位置
Page 13

### 中文翻译
EDEN 证明 approximate DRAM 可以在 DNN inference 中带来能耗和性能收益，同时满足 accuracy target。关键是使用与真实 memory error pattern 匹配的 curricular retraining，并按 data type/layer 的 error tolerance 做映射。
