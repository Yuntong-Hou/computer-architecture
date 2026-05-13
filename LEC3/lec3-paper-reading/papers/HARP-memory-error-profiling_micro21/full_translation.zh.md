# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 HARP 的 on-die ECC 问题定义、direct/indirect errors、active/reactive profiling、HARP-U/HARP-A、评估、repair case study、局限和硬件工程师视角。保留 on-die ECC、direct error、indirect error、profiling、repair、secondary ECC 等术语。

## Title

原文标题：HARP: Practically and Effectively Identifying Uncorrectable Errors in Memory Chips That Use On-Die Error-Correcting Codes

中文标题：HARP：在使用 on-die ECC 的内存芯片中实用且有效地识别不可纠正错误

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

现代 DRAM 和新型内存越来越多使用 on-die ECC。On-die ECC 能隐藏 raw bit errors，提高良率和可靠性，但也让 memory controller 看到的错误模式被改变。系统级 profiling 和 repair 需要知道哪些 bits 有风险；如果 on-die ECC 把真实错误纠正、掩盖或 miscorrect，传统 profiling 会变慢、不完整或误判。

HARP 提出 Hybrid Active-Reactive Profiling，把错误分成 direct errors 和 indirect errors。Direct errors 是 on-die ECC 后仍直接可观察的错误；indirect errors 是由 on-die ECC miscorrection 或隐藏行为导致的间接风险。HARP 使用 active profiling 识别 direct errors，并用 runtime reactive profiling 识别 indirect errors。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

系统级 memory repair 需要 bit-granularity error profiling。传统情况下，若某个 bit 在测试中反复出错，controller 可把它标记为 at-risk 并通过 repair、remapping 或 stronger ECC 处理。

On-die ECC 改变了这一过程。它在 memory chip 内部先纠正错误，controller 只看到 post-correction result。单个 raw bit error 可能被完全隐藏；多个 raw errors 可能被 miscorrect 成另一个 bit 的 visible error；某些 data patterns 的测试效果也会被 ECC 逻辑改变。

HARP 的核心观点是：系统不能把 on-die ECC 当作透明层。Profiling algorithm 必须显式建模 on-die ECC 如何改变错误可见性。

## 2. On-Die ECC Challenges / On-die ECC 带来的挑战

### 原文位置

Page 3 - Page 7

### 中文翻译

论文总结三类挑战。第一，at-risk bits 组合数指数增加。若 ECC word 中多个 bits 可能出错，controller 需要理解它们组合后是否导致 uncorrectable 或 miscorrection。

第二，单个 at-risk bit 更难观察。On-die ECC 会纠正单 bit raw error，使外部看不到它。传统 active profiling 需要更多 rounds 才能间接暴露这些 bits。

第三，常用 data pattern 被干扰。Profiling 依赖写入特定 pattern 激发错误，但 on-die ECC 可能把某些错误隐藏或变形，导致 pattern 与 observed error 不再直接对应。

这些挑战会让 naive profiling 覆盖率下降，repair 机制无法知道真正需要修复的 bits。

## 3. HARP Overview / HARP 总览

### 原文位置

Page 8 - Page 11

### 中文翻译

HARP 使用 hybrid active-reactive approach。Active profiling 在受控测试期间主动写入 patterns、读取数据、寻找错误。Reactive profiling 在正常运行中观察错误事件，并利用 controller-side secondary ECC 安全识别 indirect errors。

HARP 首先识别 direct errors。论文假设可以对 on-die ECC read operation 做一个小修改，使 controller 能读取 raw data values 或更接近 raw behavior，从而识别 direct at-risk bits。

然后处理 indirect errors。Indirect errors 不一定在 active test 中直接暴露，但在运行中与其它 raw errors 组合时可能导致 visible failure。HARP 使用 correction capability 不低于 on-die ECC 的 secondary ECC，保证在观察和记录 indirect errors 时系统仍能安全运行。

## 4. HARP-U and HARP-A / HARP-U 与 HARP-A

### 原文位置

Section 5-6

### 中文翻译

HARP-U 表示不知道 on-die ECC parity-check matrix 的版本。它不依赖厂商公开 ECC function，而是通过观察和 active/reactive profiling 逐步识别风险。

HARP-A 表示知道 parity-check matrix 的版本。若系统知道 ECC function，可以预计算某些 indirect at-risk bits，从而更快建立 coverage。HARP-A 可与 BEER/BEEP 这类 ECC reverse-engineering 工作形成互补。

两者的共同点是：direct-error coverage 仍需要 active profiling；indirect-error handling 需要运行时观察和 secondary ECC 支持。

## 5. Evaluation / 评估

### 原文位置

Page 13 - Page 17

### 中文翻译

论文用仿真比较 HARP 与两个 state-of-the-art baseline profiling algorithms。实验改变每个 ECC word 中 raw bit errors 数量和错误概率，评估达到 99th-percentile coverage 或 full coverage 所需 profiling rounds。

结果显示，对 2/3/4/5 个 pre-correction errors 的场景，HARP 只需最佳 baseline 20.6%/36.4%/52.9%/62.1% 的 profiling rounds 即可达到 99th-percentile coverage。

在 repair case study 中，当 raw per-bit error probability 为 0.75 时，HARP 比最佳 baseline 快 3.7x 获得足够信息，使 repair 覆盖全部错误并降低 BER。

## 6. Discussion and Limitations / 讨论与局限

### 原文位置

Discussion / Assumptions

### 中文翻译

HARP 假设 on-die ECC 使用 systematic encoding，并需要修改 read operation 以读取 raw data values。这对真实商品 DRAM 不一定可行，因为 on-die ECC 接口通常不开放。

HARP 还需要 controller 侧 secondary ECC，且 correction capability 不低于 on-die ECC。这会增加 controller storage、latency、area 和 design complexity。

评估主要是仿真和模型化 case study。真实芯片中 ECC function、interleaving、scrambling、vendor repair 和 error modes 可能更复杂。

## 7. 硬件工程师视角

HARP 对 RAS 设计的核心启发是：on-die ECC 改善表面错误率，但降低可观测性。系统若只依赖 post-correction errors 做 page retirement 或 repair，可能错过隐藏的 weak cells。

对 memory controller，未来高可靠系统可能需要更强 telemetry：raw error hints、syndrome-like summaries、on-die ECC correction counts、scrubbing results。若厂商不暴露这些信息，controller 侧只能用更保守策略。

对验证团队，带 on-die ECC 的 DRAM 不能用传统 raw error profiling 方法直接评估可靠性。必须考虑 miscorrection、masking、indirect errors 和 secondary ECC interaction。

## 8. 不确定与需回原文核对

- HARP 对 read operation 的小修改需回原文确认接口假设；
- HARP-U/HARP-A 具体算法流程和 coverage 定义需对照图表；
- 仿真 ECC model 与真实商用 DRAM 的差异需要谨慎；
- 与 BEER/BEEP 的关系建议结合 BEER 论文阅读。
