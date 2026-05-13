# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 EDEN 的摘要、动机、approximate DRAM 错误模型、curricular retraining、DNN error tolerance characterization、data-to-DRAM mapping、系统评估、局限和硬件工程师视角。保留 DNN inference、approximate DRAM、BER、curricular retraining、voltage/latency scaling、Eyeriss、TPU 等术语。

## Title

原文标题：EDEN: Enabling Energy-Efficient, High-Performance Deep Neural Network Inference Using Approximate DRAM

中文标题：EDEN：使用近似 DRAM 实现高能效、高性能深度神经网络推理

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

Deep Neural Network（DNN）inference 越来越 memory-intensive。模型权重、activation maps 和 intermediate data 在处理器/加速器与 DRAM 之间移动，带来显著能耗和延迟。DRAM 厂商通常使用保守 voltage 和 timing 参数保证可靠性，但这些 guardband 会牺牲能效和性能。

EDEN 的核心思想是利用 DNN 对部分 bit errors 的容忍性，让 DRAM 在 approximate mode 下运行，例如降低 VDD 或缩短 tRCD/tRAS/tRP，从而节省能耗或提高速度。关键挑战是：错误不能让 DNN accuracy 超过用户指定损失；训练和部署必须使用真实 DRAM error characteristics，而不是过于理想化的随机错误模型。

本文提出 EDEN，一个面向 DNN inference 的 approximate DRAM 框架。它包括 curricular retraining、DNN error tolerance characterization 和 DNN-to-DRAM mapping。评估显示，在 <1% accuracy loss 下，EDEN 在 CPU/GPU/Eyeriss/TPU 上分别实现显著 DRAM energy reduction，并在 latency-bound 网络上提供 speedup。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

DNN inference 在数据中心、移动设备和边缘系统中广泛部署。虽然加速器提高了 compute throughput，但 DRAM 访问仍是重要能耗和性能瓶颈。对于大模型或 batch 较小的推理，权重和 activation movement 可能主导 energy-to-inference。

DRAM 的 voltage 和 timing 参数通常保守设置，以保证所有 cells 在 worst-case process/temperature/voltage 下正确工作。如果降低 voltage 或缩短访问 latency，某些 cells 会出现 bit errors。传统系统不能接受这些错误，但 DNN inference 具有统计鲁棒性：少量权重或 activation 错误不一定改变最终分类结果。

EDEN 的目标是在用户指定 accuracy target 下，安全利用这种容错性。它不是简单降低 DRAM 可靠性，而是通过 retraining、characterization 和 mapping 控制错误影响。

## 2. Approximate DRAM and Error Models / 近似 DRAM 与错误模型

### 原文位置

Page 2 - Page 5 / Background and error characterization

### 中文翻译

Approximate DRAM 可以通过降低 supply voltage 或缩短 timing 参数获得能耗/性能收益。降低 VDD 可减少动态和静态能耗，但增加 retention/access failures。缩短 tRCD/tRAS/tRP 可降低访问延迟，但可能在 sensing 或 restoration 未完成时读取/写入错误数据。

EDEN 使用真实 DDR4 modules 的 reduced voltage/latency 错误数据建立 error models。作者基于 8 个真实 DRAM modules，构造 4 类 error models，反映不同 approximate operating points 下的 bit error rate 和错误分布。

这一点很重要，因为 DNN 对错误的容忍性高度依赖错误位置、方向、相关性和数据类型。简单 i.i.d. random bit flip 模型可能过于乐观或悲观。硬件工程中，approximate memory 必须基于真实错误表征。

## 3. EDEN Framework Overview / EDEN 框架总览

### 原文位置

Page 4 / Figure 4

### 中文翻译

EDEN 包含三个主要步骤。

第一，curricular retraining。训练过程逐步引入 approximate DRAM errors，让 DNN 学会在错误环境下保持 accuracy。

第二，DNN error tolerance characterization。EDEN 分析不同 layer、data type、precision 和网络结构对 bit errors 的容忍度，得到每类数据可承受的 maximum BER。

第三，DNN-to-DRAM mapping。系统根据不同数据的 BER tolerance，将它们映射到不同 approximate DRAM partitions。更敏感的数据放在更可靠但收益较小的 partition；更鲁棒的数据放在更激进、能耗/延迟收益更大的 partition。

这三步共同解决一个核心问题：如何把应用级 accuracy constraint 转化为 memory-level operating point。

## 4. Curricular Retraining / 课程式再训练

### 原文位置

Page 6 - Page 8 / Section 3, Figures 9-10

### 中文翻译

如果直接在高 BER 下训练或推理，DNN accuracy 可能崩溃。EDEN 提出 curricular retraining：训练时从较低 error rate 开始，逐步增加错误强度，使模型逐渐适应 approximate DRAM 环境。

这种方法类似 curriculum learning。网络先学习在较轻扰动下保持正确，再逐步适应更强扰动。论文报告 curricular retraining 可将 DNN tolerable BER 提升 5-10x。

工程意义是，硬件错误容忍不能只靠部署时“赌模型鲁棒”。需要把硬件错误特性引入训练流程。对 AI 硬件团队来说，这意味着 memory PVT/error model、training framework 和 deployment compiler 需要协同。

## 5. Error Tolerance Characterization / 错误容忍度表征

### 原文位置

Page 8 - Page 10

### 中文翻译

EDEN 系统表征不同 DNN components 对 errors 的容忍度。论文发现，低精度数据通常更敏感，因为一个 bit flip 占数值表示的比例更大。首层和末层也往往更敏感：首层直接处理输入特征，末层直接影响最终分类/检测结果。

Pruning 对 error tolerance 的影响不显著。这说明稀疏化并不自动让模型更能容忍 memory errors。不同网络结构和数据类型有不同 maximum tolerable BER，不能使用统一阈值。

这种表征结果决定 mapping 策略。敏感 layers 或 data types 应放在可靠 DRAM partition；鲁棒部分可放在更 aggressive approximate partition。

## 6. DNN-to-DRAM Mapping / DNN 数据到 DRAM 的映射

### 原文位置

Page 10 - Page 11

### 中文翻译

EDEN 将 DNN 数据映射到不同 DRAM partitions。每个 partition 对应不同 voltage/latency operating point 和 BER。Mapping 的目标是在满足 accuracy target 的同时最大化 energy reduction 或 performance benefit。

例如，某些权重或 activation 对 errors 不敏感，可以放入低电压或低 latency partition；关键 layers、低精度敏感数据或输出相关数据则放入可靠 partition。这样可以避免全模型使用最保守配置，也避免全模型使用过于激进配置导致 accuracy loss。

工程实现需要 memory allocator、runtime 或 compiler 支持。系统必须知道哪些 tensors/layers 映射到哪些 physical pages/banks/partitions，并在执行时保持一致。

## 7. Evaluation Methodology / 评估方法

### 原文位置

Page 11 - Page 12

### 中文翻译

作者使用多种 DNN models，包括 OpenVINO 和 DarkNet 模型，如 YOLO、VGG、ResNet、SqueezeNet、DenseNet、AlexNet 等，覆盖 FP32 和 int8。系统平台包括 CPU、GPU、Eyeriss-like accelerator 和 TPU-like accelerator。

模拟工具包括 ZSim+Ramulator（CPU）、GPGPU-Sim+GPUWattch（GPU）、SCALE-Sim+DRAMPower（Eyeriss/TPU）。DRAM error models 来自真实 DDR4 reduced voltage/latency 实验。

评估指标包括 accuracy loss、DRAM energy reduction、inference speedup 和不同 accuracy target 下的收益。

## 8. Evaluation Results / 实验结果

### 原文位置

Page 11 - Page 13 / Figures 13-14

### 中文翻译

在 <1% accuracy loss 约束下，EDEN 在 CPU 上平均降低 21% DRAM energy；在 same accuracy target 下仍有约 16% savings。对于 CPU latency-bound DNN，EDEN 平均 speedup 约 8%，最高约 17%。

在 GPU 上，EDEN 平均 DRAM energy reduction 约 37%，平均 speedup 约 2.7%。GPU 的 speedup 较低可能是因为计算并行性和其它瓶颈掩盖了部分 DRAM latency benefit，但 energy benefit 仍明显。

在 Eyeriss/TPU-like accelerators 上，EDEN 平均 DRAM energy reduction 约 31%/32%。这说明 approximate DRAM 不只适用于通用 CPU/GPU，也可服务专用 DNN accelerators。

## 9. Discussion and Limitations / 讨论与局限

### 原文位置

Discussion / Limitations

### 中文翻译

EDEN 的有效性依赖准确且稳定的 DRAM error models。如果温度、电压、老化或制造差异导致错误分布变化，mapping 和 retraining 可能失效。因此，实际系统需要在线监测、保守 guardband 或定期重新 characterization。

EDEN 主要面向 inference，而不是 training。Training 对数值错误可能更敏感，且错误会影响梯度更新。论文也主要覆盖 CNN/传统 DNN，对现代 Transformer/LLM、HBM/GDDR、低精度 FP8/INT4 等场景需要更新研究。

此外，approximate DRAM 的错误必须与系统安全和可靠性隔离。不能让 approximate partition 存放控制数据、地址、metadata 或安全敏感信息。

## 10. Conclusion / 结论

### 原文位置

Conclusion

### 中文翻译

EDEN 表明，approximate DRAM 可以在严格 accuracy target 下服务 DNN inference。通过 curricular retraining、error tolerance characterization 和 DNN-to-DRAM mapping，系统能够利用 DNN 对部分 memory errors 的容忍性，降低 DRAM energy 并改善 latency-bound workload 性能。

本文的核心贡献是把硬件错误模型、机器学习鲁棒性和 memory mapping 连接起来，展示跨层协同优化的价值。

## 11. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文框架、实验和局限的工程化解读

### 中文学习笔记

1. 对 AI 加速器：DRAM energy 是 inference 的重要成本。Approximate memory 可以成为能效优化手段，但必须由模型训练和 runtime 支持。

2. 对内存控制器：需要支持不同 reliability/latency partitions，并让软件能把 tensor 映射到合适区域。

3. 对验证：必须用真实 DRAM error maps、温度、电压和老化条件验证 accuracy，而不是只注入随机 bit flips。

4. 对系统安全：approximate partition 必须隔离。控制结构、页表、代码、metadata 不能放入不可靠区域。

5. 对行业：EDEN 是 memory-system/ML co-design 的早期代表。随着 LLM 推理 memory-bound 程度上升，类似思想可能重新出现，但需要适配 HBM、GDDR 和低精度模型。

6. 对个人学习：重点掌握 curricular retraining、error tolerance characterization、DNN-to-DRAM mapping 三步，以及如何把 application-level accuracy 转成 memory-level BER 约束。

## 12. 不确定与需回原文核对

- Figures 9-14 的具体网络和数值建议回 PDF 核对。
- 结果基于当时 DNN/CNN 模型；对现代 Transformer/LLM 不应直接外推。
- Approximate DRAM 的 field reliability、RAS 和 safety certification 仍是产品化难点。
