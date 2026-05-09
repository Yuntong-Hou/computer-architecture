from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


PAPERS = {
    "2310.14665v3": {
        "title": "Read Disturbance in High Bandwidth Memory: A Detailed Experimental Study on HBM2 DRAM Chips",
        "zh_title": "高带宽内存中的读扰动：对 HBM2 DRAM 芯片的详细实验研究",
        "authors": "Ataberk Olgun, Majd Osseiran, Damla Senol Cali, Hasan Hassan, Geraldo F. Oliveira, Minesh Patel, Onur Mutlu 等",
        "year": "2023 / 2024",
        "venue": "arXiv:2310.14665v3",
        "topic": "HBM2 read disturbance / RowHammer / RowPress characterization",
        "keywords": "HBM2, RowHammer, RowPress, read disturbance, TRR, ECC",
        "url": "https://arxiv.org/abs/2310.14665",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
这篇论文首次系统实验分析了真实 HBM2 芯片中的 RowHammer 与 RowPress 读扰动现象，证明 HBM2 同样存在可被放大的读扰动脆弱性，并揭示了芯片内部未公开防护机制及其可绕过性。

## 2. 研究背景
HBM2 通过 3D-stacked DRAM、多个 channel/pseudo-channel 和高带宽接口支撑 GPU、FPGA 和加速器系统。过去 RowHammer 研究主要集中在 DDR3/DDR4/LPDDR，HBM2 因封装、组织结构和目标工作负载不同而缺少公开实验数据。作者指出，如果 HBM2 被用于共享加速平台或云端高性能计算，读扰动不仅是可靠性问题，也会成为安全问题。

## 3. 核心问题
- HBM2 是否会发生 RowHammer 和 RowPress bitflip。
- 读扰动脆弱性是否随 chip、channel、pseudo-channel、bank、row 位置变化。
- 现代 HBM2 是否含有未公开的 in-DRAM read-disturbance mitigation。
- 增大 aggressor row 开启时间 tAggON 是否会显著降低触发 bitflip 所需 activation 数。
- HBM2 的 ECC word 分布会怎样影响攻击可利用性与防护设计。

## 4. 核心贡献
- 在 6 颗真实 HBM2 芯片上完成详细 read disturbance 实验，覆盖 RowHammer 和 RowPress。
- 发现所有测试芯片都存在 RowHammer bitflip，但脆弱程度在 chip、channel、bank 和 row 位置上差异很大。
- 观察到 bank 中端/末端 row 更抗扰动，说明 row 的物理/布局位置对可靠性有重要影响。
- 分析同一 victim row 的前 10 个 bitflip，发现出现第一个 bitflip 后，后续 bitflip 所需额外 hammer 数往往更少。
- 证明较长 tAggON 可以显著放大扰动，tAggON=35.1us 时平均 HCfirst 比 29ns 小约 222.57x。
- 揭示并分析 HBM2 中未公开的 activation-count based TRR-like 机制，并展示特定访问模式可绕过。
- 开源实验基础设施与数据，便于复现和后续研究。

## 5. 方法概述
作者使用 FPGA-based HBM2 测试平台，对不同 HBM2 chip 施加可控 activation 序列。核心测量指标包括 bit error rate、HCfirst、不同 row/channel/bank 的空间分布，以及 RowPress 中 tAggON 对扰动强度的影响。实验既使用传统 hammering，也使用插入 dummy row 或改变访问模式的测试来推断芯片内部防护行为。

## 6. 实验设计
实验对象为两块 FPGA 板上的 6 颗 HBM2 DRAM chip。作者在不同 channel、pseudo-channel、bank、row segment 上测试 read disturbance。评估指标包括 bitflip 数、bit error rate、HCfirst、前 10 个 bitflip 的 hammer count、ECC word 中 bitflip 分布等。主要图表包括 Page 4-8 的 spatial variation 分析、Page 9-11 的 RowPress 与防护机制分析。

## 7. 主要结果
- 所有 6 颗 HBM2 芯片都出现 RowHammer bitflip；结果见 Page 4-5, Figure 4-5。
- HCfirst 和 BER 在 chip 内部结构之间显著变化，channel/pseudo-channel/bank/row 位置均有影响；见 Page 5-7, Figure 6-10。
- tAggON 从 29ns 增至 35.1us 时，HCfirst 平均降低 222.57x；见 Page 9-10, Figure 14-15。
- 某些设置下一次 activation 并保持 row open 16ms 就能诱发 bitflip；见 Page 10, RowPress analysis。
- 芯片存在未公开 TRR-like 防护，但可被专门访问模式绕过；见 Page 11, Figure 16。
- ECC word 中 bitflip 分布说明多 bit error 可能跨越 ECC 修正能力边界；见 Page 12, Figure 17。

## 8. 关键结论
HBM2 并没有天然免疫 read disturbance。相反，高密度、复杂组织结构和长期 row-open 行为使其需要针对 HBM 的专门防护。RowPress 结果尤其说明，仅考虑 activation count 的 RowHammer 防护不足以覆盖所有读扰动路径。

## 9. 局限性
作者只测试 6 颗 HBM2 芯片，供应商和世代覆盖有限；实验依赖 FPGA 平台和可控访问序列，不能完全代表所有 GPU/HPC 系统的真实调度；内部 TRR 机制只能通过黑盒推断；ECC 影响也主要从 bitflip 分布角度分析，而不是完整系统安全攻击演示。

## 10. 适合我重点关注的内容
建议重点读 Figure 4-8 理解空间差异，Figure 14-15 理解 RowPress，Figure 16 理解未公开防护机制，以及 Section 5 的 implication 部分。

## 11. 和其他文献的关系
这篇文章把 RowHammer/RowPress 从 DDR4 扩展到 HBM2，与 RowPress ISCA 2023、Spatial Variation-Aware Defenses、PRAC/Chronus 和 Variable Read Disturbance 形成直接脉络：先证明现象存在，再讨论空间/时间变化，最后推动更健壮的防护机制。""",
        "key_points": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | HBM2 也会受到 RowHammer 读扰动影响 | Page 1, Abstract; Page 4-5, Figure 4-5 | 6 颗 HBM2 chip 全部可诱发 bitflip | 高 | HBM 的封装和带宽优势不等于读扰动可靠性更强 |
| 2 | 脆弱性在 chip 与内部结构之间高度不均匀 | Page 5-7, Figure 6-10 | channel、pseudo-channel、bank、row 位置均表现不同 | 高 | 防护不能只设置全局统一阈值 |
| 3 | bank 中端/末端 row 更抗扰动 | Page 7, Figure 8 | 不同 row 位置 HCfirst/BER 分布有系统性差异 | 中 | 可能反映物理布局、sense amplifier 或边界结构差异 |
| 4 | 第一个 bitflip 后，后续 bitflip 往往更容易出现 | Page 8, Figure 11-12 | 对前 10 个 bitflip 的 hammer count 做序列分析 | 高 | 单看 HCfirst 可能低估多 bit error 风险 |
| 5 | RowPress 显著放大读扰动 | Page 9-10, Figure 14-15 | tAggON=35.1us 时 HCfirst 平均比 29ns 小 222.57x | 高 | 仅跟踪 activation count 的防护会漏掉 row-open 时间维度 |
| 6 | 极端 RowPress 下单次 activation 也可能触发 bitflip | Page 10, RowPress analysis | row 保持 open 16ms 的测试出现 bitflip | 高 | 这对内存控制器的 open-page policy 很关键 |
| 7 | 现代 HBM2 含未公开 TRR-like 防护 | Page 11, Figure 16 | dummy row 和 aggressor tracking 实验显示 activation-count-based 行为 | 高 | 工业防护黑盒化会增加系统安全验证难度 |
| 8 | 特定访问模式可绕过该防护 | Page 11, Figure 16 | 插入/组织访问序列后仍可诱发 bitflip | 高 | 防护评估必须包含自适应攻击，而不只是标准 hammer pattern |
| 9 | ECC word 分布影响错误可修复性 | Page 12, Figure 17 | bitflip 在 ECC word 中分布不均 | 中 | HBM 系统需要联合考虑 on-die ECC、外部 ECC 和扰动模式 |
| 10 | 开源实验数据和基础设施 | Page 2, Contributions; GitHub link | 作者提供 HBM read-disturbance repo | 中 | 对复现实验和后续防护比较很有价值 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
本文基于已下载 PDF 的可提取文本生成逐节中文详译/译述，覆盖摘要、背景、方法、实验、结果、讨论和结论。为避免对版权论文做大段逐字翻译，以下内容采用忠实转述方式，不复制英文长段；公式、指标、数据集、模型名和专有术语保留英文。

## Title
原文标题：Read Disturbance in High Bandwidth Memory: A Detailed Experimental Study on HBM2 DRAM Chips

中文标题：高带宽内存中的读扰动：对 HBM2 DRAM 芯片的详细实验研究

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文研究 HBM2 DRAM 中的 read disturbance。作者指出，RowHammer 已经在多代 DDR DRAM 中被证实，但 HBM2 由于 3D stacked 结构、高带宽接口和较少公开可控测试平台，仍缺少细粒度实验理解。论文在真实 HBM2 芯片上测量 RowHammer 与 RowPress，发现所有被测芯片都可出现 bitflip，且脆弱性具有明显空间差异。作者进一步发现，延长 aggressor row 的开启时间 tAggON 会大幅降低触发 bitflip 所需 activation 数，并揭示 HBM2 芯片中存在未公开的 read disturbance 防护机制，但这种机制可以被特定访问模式绕过。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 3

### 中文翻译
引言首先说明 HBM2 的重要性：许多 GPU、FPGA 和高性能加速器系统依赖 HBM2 来提供远高于传统 DDR 的内存带宽。随着 HBM2 被用于云端、AI、HPC 和多租户平台，其可靠性和安全性不再只是器件层问题，而会影响系统隔离和服务可用性。

作者回顾 RowHammer：重复激活一个或多个 aggressor row 会干扰相邻 victim row 中的电荷，导致 bitflip。以往研究主要关注 DDR3、DDR4、LPDDR 和部分 GDDR/commodity DRAM。HBM2 的内部结构不同，包括多个 channel、pseudo-channel、bank 和 3D 堆叠，因此 DDR 上的结论不能直接外推。

论文还把 RowPress 纳入研究。RowPress 的关键不是简单增加 activation 次数，而是让 aggressor row 保持开启较长时间。这个维度对 HBM2 尤其重要，因为高性能内存控制器可能采用 open-page policy 或产生长 row-open 行为。

## 2. Background / 背景

### 原文位置
Page 2 - Page 3

### 中文翻译
背景部分介绍 HBM2 的组织结构。HBM2 通过 stacked DRAM dies 和宽 I/O 接口提供高带宽。每个 stack 被划分为多个 channel，每个 channel 又可包含 pseudo-channel 和多个 bank。这样的结构意味着 read disturbance 的空间位置不只是 row number，还包括 channel、pseudo-channel、bank 和 die/stack 相关因素。

作者还解释 RowHammer 与防护机制。现代 DRAM 往往实现 TRR-like 机制，即在芯片内部跟踪激活次数较多的 row，并刷新潜在 victim row。但这些机制通常未公开，系统软件和研究者很难知道其阈值、追踪粒度和绕过条件。

## 3. Methodology / 方法

### 原文位置
Page 3 - Page 4

### 中文翻译
实验使用 FPGA-based HBM2 平台生成精确的访问序列。作者可以控制 aggressor row、victim row、activation 数、row-open 时间 tAggON 和 dummy row 插入方式。主要测量指标包括 bitflip 数、bit error rate、HCfirst 以及不同空间位置上的分布。

为了研究 RowHammer，作者施加大量 activation 并检查 victim row 是否出现 bitflip。为了研究 RowPress，作者固定或改变 row-open 时间，并观察较长 tAggON 是否降低 HCfirst。为了推断内部防护机制，作者构造不同 hammer/dummy-row pattern，观察 bitflip 是否被抑制或重新出现。

## 4. RowHammer Characterization / RowHammer 表征

### 原文位置
Page 4 - Page 8

### 中文翻译
作者首先展示 6 颗 HBM2 芯片的总体 bitflip 与 HCfirst 分布。结果说明所有芯片都可产生 RowHammer bitflip，但不同芯片间差异明显。有些芯片表现出更低 HCfirst 或更高 bit error rate，说明制造差异和芯片内部组织对扰动敏感性有影响。

随后，论文按 channel、pseudo-channel、bank 和 row 位置分析空间变化。结果显示，即使在同一颗 HBM2 chip 内，不同组件也可能表现出不同脆弱性。特别是 bank 中不同 row segment 的结果不均匀，bank 中间或末端的 row 相对更抗扰动。

作者还分析前 10 个 bitflip 的出现过程。一个重要观察是：触发第一个 bitflip 所需 hammer count 高，并不意味着后续 bitflip 也同样困难。许多 row 在第一个 bitflip 后，后续 bitflip 需要的额外 hammer 数下降。这意味着只用 HCfirst 评价安全性可能不足，因为攻击者关心的往往是多 bit 错误或特定 ECC word 中的错误组合。

## 5. RowPress Characterization / RowPress 表征

### 原文位置
Page 9 - Page 10

### 中文翻译
RowPress 实验改变 aggressor row 保持开启的时间 tAggON。结果非常显著：当 tAggON 从常规纳秒级提升到微秒级时，触发第一个 bitflip 所需 activation 数大幅下降。论文报告 tAggON=35.1us 时平均 HCfirst 比 29ns 设置小约 222.57x。

更极端地，作者发现当 row 保持 open 16ms 时，单次 activation 也可能导致 bitflip。这个结果说明 read disturbance 的根本原因不只是激活次数，还与 row 被打开期间相邻电路受到的持续电气压力有关。对系统而言，这意味着防护需要考虑 row-open duration，而不是只统计 ACT 命令。

## 6. Undocumented In-DRAM Defense / 未公开片内防护

### 原文位置
Page 10 - Page 11

### 中文翻译
通过构造不同 dummy row 和 aggressor 访问序列，作者推断某些 HBM2 芯片中存在未公开的 TRR-like 防护。该机制似乎会根据 activation count 跟踪高频访问 row，并触发针对相邻 victim 的保护刷新。

不过，这种防护并不完整。作者展示特定访问模式可以影响 tracking 行为，使真实 aggressor 不再被充分保护，从而重新诱发 bitflip。该结果与 DDR4 上 TRRespass 等工作相呼应：只要防护机制黑盒且资源有限，就可能被自适应访问序列绕过。

## 7. ECC Implications / ECC 影响

### 原文位置
Page 12, Figure 17

### 中文翻译
论文分析 bitflip 在 ECC word 中的分布。结果表明，某些扰动模式可能在同一 ECC word 中产生多个错误，或以不利方式跨 ECC word 分布。对系统设计来说，这意味着不能仅依赖“有 ECC”这一事实判断安全；需要知道 ECC granularity、correction capability、on-die ECC 与外部 ECC 的组合方式。

## 8. Discussion / 讨论

### 原文位置
Page 12 - Page 14

### 中文翻译
讨论部分强调 HBM2 读扰动对未来系统的含义。HBM 被越来越多地用于加速器和共享平台，攻击者可能不需要直接访问 DRAM 命令接口，只要能诱导特定内存访问模式，就可能增加扰动风险。RowPress 进一步扩大风险面，因为它把 memory controller policy、row buffer 行为和 read disturbance 连接起来。

作者建议未来防护需要同时考虑空间差异、row-open 时间、ECC 组织和片内防护可验证性。公开实验基础设施和数据有助于避免每篇论文都重新构建测试平台，也能让工业界和学术界比较不同防护方案。

## 9. Conclusion / 结论

### 原文位置
Page 14 - Page 15

### 中文翻译
论文结论是：HBM2 DRAM 对 read disturbance 并不免疫，RowHammer 和 RowPress 都能在真实芯片中诱发 bitflip。脆弱性具有显著空间变化，且现代芯片中的未公开防护机制不能保证安全。未来 HBM 系统需要透明、可评估且能覆盖 activation count 与 row-open time 两个维度的防护。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | HBM2 组织/读扰动背景 | 帮助读者理解 channel、pseudo-channel、bank、row 的层级 | 后续空间差异分析都依赖这个结构 | 先对照 HBM2 结构再读结果图 |
| Figure 4 | Page 4 | 各 chip 的 RowHammer bit error rate | 不同 HBM2 chip 的 BER 差异明显 | 证明 chip-to-chip variation | 结合 Figure 5 看 BER 与 HCfirst |
| Figure 5 | Page 5 | HCfirst 分布 | 不同芯片触发首个 bitflip 的 hammer count 不同 | HCfirst 是防护阈值的重要参考 | 注意它不能代表后续 bitflip 风险 |
| Figure 6-7 | Page 5-6 | channel/pseudo-channel 差异 | HBM 内部通道间脆弱性不同 | 说明统一阈值可能过粗 | 看是否存在结构性偏差 |
| Figure 8 | Page 7 | bank 内 row 位置差异 | bank 中端/末端 row 较抗扰动 | 对 spatial-aware defense 有启发 | 重点看 row segment 趋势 |
| Figure 11-12 | Page 8 | 前 10 个 bitflip 的 hammer count | 第一个 bitflip 后后续 bitflip 更容易出现 | 影响 ECC 与安全攻击评估 | 不要只看 HCfirst |
| Figure 14-15 | Page 9-10 | RowPress 与 tAggON | 延长 row-open 时间显著降低 HCfirst | 证明 RowPress 是关键风险 | 这是本文最重要图之一 |
| Figure 16 | Page 11 | TRR-like 防护推断与绕过 | HBM2 存在未公开防护，但访问模式可绕过 | 关系到工业防护可信度 | 建议回 PDF 仔细看 pattern |
| Figure 17 | Page 12 | ECC word 中 bitflip 分布 | 多 bit 错误与 ECC granularity 相关 | 连接器件错误和系统容错 | 结合系统 ECC 设计理解 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 3 | 实验平台/芯片参数 | 说明 HBM2 chip 与 FPGA board 配置 | 判断实验外推范围 | 先看样本数量和芯片类别 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 未发现核心编号公式 | 全文 | 本文以实验测量为主 | HCfirst、BER、tAggON 为关键指标 | 重点是实验定义而非数学推导 | 否 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| High Bandwidth Memory (HBM2) | 高带宽内存 HBM2 | Page 1-3 | 3D-stacked DRAM，提供高带宽接口 | 是 |
| Read Disturbance | 读扰动 | Page 1 | 读取/激活某些 row 对邻近 row 造成电气干扰 | 是 |
| RowHammer | 行锤击 | Page 1 | 反复激活 aggressor row 诱发 victim row bitflip | 是 |
| RowPress | 行压迫 | Page 1, Page 9 | 延长 aggressor row open 时间造成更强扰动 | 是 |
| HCfirst | 首个 bitflip 的 hammer count | Page 4-8 | 触发第一个错误所需 activation 数 | 是 |
| Bit Error Rate (BER) | 位错误率 | Page 4 | bitflip 数相对测试位数的比例 | 是 |
| tAggON | aggressor row 开启时间 | Page 9 | RowPress 中 aggressor row 保持 open 的时间 | 是 |
| TRR-like Defense | 类 TRR 防护 | Page 10-11 | 片内跟踪高 activation row 并刷新 victim 的机制 | 是 |
| Dummy Row | 干扰/填充 row | Page 11 | 用于影响内部 tracking 的额外访问 row | 是 |
| ECC Word | ECC 码字 | Page 12 | ECC 进行错误检测/纠正的粒度 | 中 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- 样本为 6 颗 HBM2 chip，不能覆盖所有厂商、容量和世代；位置：Page 3 Methodology, Page 12 Discussion。
- 芯片内部防护机制是黑盒推断，作者无法直接读取厂商实现；位置：Page 10-11。

## 2. 论文中隐含的局限
- FPGA 测试环境能精确控制访问序列，但真实 GPU/HPC 系统中的调度、cache、memory controller policy 会改变可达攻击模式。
- 对 ECC 的讨论主要基于 bitflip 分布，未完整构建端到端 exploit 或系统级容错评估。

## 3. 实验设计可能存在的问题
- HBM2 样本数量较少，chip-to-chip variation 又很大，因此最坏情况可能未被捕捉。
- tAggON 极端设置对真实系统代表性需要结合具体 memory controller policy 判断。

## 4. 方法可能不适用的场景
- 对无法控制 row-open time 的系统，RowPress 攻击可行性可能低于实验平台。
- 未来 HBM3/HBM4 可能采用不同内部防护和 ECC，不能直接沿用阈值。

## 5. 我阅读时应该追问的问题
- HBM2 的 address mapping 是否会限制攻击者定位 aggressor/victim row？
- GPU cache/coalescing 是否会削弱或增强可控 hammer pattern？
- 如果外部 ECC 与 on-die ECC 同时存在，Figure 17 的安全含义如何变化？
- RowPress 是否能由正常 HPC kernel 意外触发？

## 6. 后续可以继续阅读的方向
- RowPress ISCA 2023：理解 tAggON 对 DDR4 的影响。
- Spatial Variation-Aware Defenses：把本文空间差异转化为防护策略。
- PRAC/Chronus：理解 JEDEC/industry 方案如何处理更低 NRH。""",
        "log": """# Extraction Log

- Input Type: GitHub repository PDF
- Source: `paper reading/sources/LEC3/2310.14665v3.pdf`
- Access Status: 已下载并可读取
- Full Text Retrieved: Yes
- PDF Pages: 16
- Sections Detected: Abstract, Introduction, Background, Methodology, Characterization, RowPress, TRR-like defense, ECC implications, Discussion, Conclusion
- Figures Detected: Yes
- Tables Detected: Yes
- Equations Detected: 未发现核心编号公式
- Appendix Detected: 未发现独立 appendix
- Supplementary Material Detected: 开源数据/代码链接
- OCR Used: No
- Missing Content: 图像本体未做视觉 OCR；部分图中细粒度数值需回 PDF 查看
- Parsing Problems: pdftotext 对作者列表和部分图注换行不稳定
- Uncertain Parts: 内部 TRR-like 机制为黑盒推断，非厂商确认
- Need User Action: 如需逐字翻译或图像级复核，请提供版权授权或指定重点页
- Quality Check: 已覆盖全文结构、主要实验、图表、局限和原文位置；`full_translation.zh.md` 为版权友好的逐节中文译述，不是逐字全文翻译
- Batch Status: 第二轮深度阅读完成""",
    },
    "2402.18652v1": {
        "title": "Spatial Variation-Aware Read Disturbance Defenses: Experimental Analysis of Real DRAM Chips and Implications on Future Solutions",
        "zh_title": "空间变化感知的读扰动防护：真实 DRAM 芯片实验分析及其对未来方案的启示",
        "authors": "Ataberk Olgun, F. Nisa Bostanci, Minesh Patel, Hasan Hassan, Jeremie S. Kim, Onur Mutlu 等",
        "year": "2024",
        "venue": "arXiv:2402.18652v1",
        "topic": "Spatial variation-aware RowHammer/read-disturbance defense",
        "keywords": "RowHammer, read disturbance, spatial variation, DRAM, Svard, PARA, Hydra, AQUA, BlockHammer",
        "url": "https://arxiv.org/abs/2402.18652",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
这篇论文通过 144 颗真实 DDR4 芯片的大规模实验说明 RowHammer/read disturbance 脆弱性存在显著空间变化，并提出 Svärd 利用 row-level profile 调整防护强度，从而在保证安全目标的同时降低性能开销。

## 2. 研究背景
传统 RowHammer 防护通常假设所有 row 共享一个最坏情况阈值 NRH。随着工艺缩小，真实芯片的脆弱性不仅更强，而且在空间上高度不均匀。如果所有 row 都按最弱 row 保护，防护会过于保守；如果忽略弱 row，则会不安全。作者希望回答：能否利用空间变化，让防护对脆弱 row 更激进、对稳健 row 更宽松。

## 3. 核心问题
- 真实 DDR4 芯片中 read disturbance 的空间变化有多大。
- row/subarray/bank/module 等空间特征能否预测脆弱性。
- 现有防护是否能通过空间 profile 降低开销。
- 在 benign workload 和 adversarial pattern 下，空间感知策略是否仍安全有效。

## 4. 核心贡献
- 在 144 颗 DDR4 芯片、10 种 chip design、3 家主要厂商上表征空间变化。
- 发现同一 subarray 内 BER 可相差约 2x，HCfirst 可相差一个数量级。
- 发现简单空间特征只在 15 个 module 中的 4 个表现出明显相关性，说明不能只靠 row index 推断脆弱性。
- 提出 Svärd，利用离线/在线 row-level profile 为不同 row 设置不同防护 aggressiveness。
- 将 Svärd 叠加到 AQUA、BlockHammer、Hydra、PARA、RRS 上评估。
- 在 120 个 multiprogrammed memory-intensive workload 上分别带来 1.23x、2.65x、1.03x、1.57x、2.76x 平均性能改善。

## 5. 方法概述
作者先做芯片级实验，得到每个 row 或 row group 的 read disturbance profile。然后将 profile 转化为防护参数：弱 row 使用更保守/更频繁的保护，强 row 使用更少保护。Svärd 不是一个独立替代所有防护的机制，而是一个 spatial variation-aware wrapper，可以与多种已有 RowHammer mitigation 结合。

## 6. 实验设计
实验部分分两层：第一层是 144 颗 DDR4 芯片的真实器件表征，分析 BER、HCfirst 与 row/subarray/bank/module 位置的关系；第二层是系统模拟，将 Svärd 与 AQUA、BlockHammer、Hydra、PARA 和 RRS 组合，在 120 个四核 memory-intensive workload 上比较性能，同时测试 adversarial access pattern。

## 7. 主要结果
- 同一 subarray 内 BER 和 HCfirst 变化显著；见 Page 5-8, Figure 3-10。
- 空间特征与 vulnerability 的相关性不稳定，只在部分 module 中明显；见 Page 7-8。
- Svärd 与五类防护结合后，平均性能相对原方案提升 1.23x 到 2.76x；见 Page 13-15, Figure 12。
- 在 adversarial pattern 下，Svärd 需要保持对弱 row 的最坏情况保护，否则会降低安全 margin；见 Page 15-16, Figure 13。

## 8. 关键结论
空间变化是 RowHammer 防护设计必须面对的事实，但它不能被简单地压缩成“某些 row index 更危险”的规则。有效方案应基于测量 profile，并能与现有防护机制结合，在安全和开销之间做 row-granularity 的权衡。

## 9. 局限性
Svärd 依赖 profile 的准确性和稳定性；profile 获取成本、老化、温度、电压和 temporal variation 会影响有效性。论文主要使用 DDR4 数据，对 HBM2、LPDDR5、DDR5 的外推需要谨慎。

## 10. 适合我重点关注的内容
重点读 Figure 3-10 的 characterization、Svärd 设计部分、Figure 12 的性能结果和 Figure 13 的 adversarial pattern。

## 11. 和其他文献的关系
本文与 HBM2 read disturbance 论文共同说明空间变化重要；与 Variable Read Disturbance 形成互补，后者强调时间变化会挑战 profile；与 PRAC/Chronus 的关系在于：当 NRH 越低，防护越贵，利用空间/时间信息降低开销越有价值。""",
        "key_points": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 真实 DRAM read disturbance 脆弱性存在显著空间变化 | Page 1 Abstract; Page 5-8, Figure 3-10 | 144 颗 DDR4 芯片实验 | 高 | 防护阈值不能只看全局平均 |
| 2 | 同一 subarray 内 BER 可约 2x 变化，HCfirst 可差一个数量级 | Page 1 Abstract; Page 6-7 | 细粒度 row-level 测量 | 高 | 最坏 row 会决定安全阈值，强 row 则承担过度防护成本 |
| 3 | 简单空间特征不稳定，不能可靠预测脆弱性 | Page 7-8 | 15 个 module 中仅 4 个有明显相关性 | 高 | 必须实际 profile，而不是只做启发式映射 |
| 4 | Svärd 利用 row-level profile 调整防护 aggressiveness | Page 10-12, Svärd design | 不同 row 使用不同保护强度 | 高 | 这是从表征到系统机制的核心桥梁 |
| 5 | Svärd 可与多种防护组合 | Page 12-13 | AQUA, BlockHammer, Hydra, PARA, RRS | 中 | 它更像通用优化层，而不是单一防护 |
| 6 | Svärd 显著降低已有防护性能开销 | Page 13-15, Figure 12 | 平均提升 1.23x/2.65x/1.03x/1.57x/2.76x | 高 | 当防护开销高时，空间信息价值最大 |
| 7 | adversarial pattern 下仍需保守处理弱 row | Page 15-16, Figure 13 | 攻击者可集中访问最弱 row | 高 | 安全策略必须按最弱 row 保证，而不是平均收益 |
| 8 | profile 成本和稳定性是关键挑战 | Page 16 Discussion | 温度、老化、时间变化未完全解决 | 高 | 与 VRD 论文直接关联 |
| 9 | 研究对象主要为 DDR4 | Page 4 Methodology | 144 DDR4 chips, 10 designs, 3 vendors | 中 | 对 HBM/DDR5 需要重新实验 |
| 10 | 本文强调 measurement-driven defense | Page 17 Conclusion | 结论呼吁利用真实芯片 variation | 中 | 是未来 adaptive memory reliability 的代表方向 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
本文基于可访问 PDF 的提取文本生成逐节中文详译/译述，覆盖论文所有主要部分。以下内容不进行逐字长篇翻译，而是按原文章节忠实转述，并保留关键英文术语。

## Title
原文标题：Spatial Variation-Aware Read Disturbance Defenses: Experimental Analysis of Real DRAM Chips and Implications on Future Solutions

中文标题：空间变化感知的读扰动防护：真实 DRAM 芯片实验分析及其对未来方案的启示

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文研究 DRAM read disturbance vulnerability 的空间变化。作者在大量真实 DDR4 芯片上发现，同一芯片内部不同 row、subarray、bank 的 RowHammer 敏感性差异很大。基于这一现象，论文提出 Svärd：一种利用 row-level vulnerability profile 调整防护强度的方法。Svärd 可叠加到多种已有 RowHammer mitigation 上，在保持安全约束的同时降低性能开销。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 3

### 中文翻译
引言说明 RowHammer 防护越来越困难。随着 DRAM cell 缩小，触发 bitflip 所需 activation 数下降，系统必须更频繁地刷新或阻止潜在攻击访问。许多防护采用单一阈值：只要某个 row 的 activation count 接近 NRH，就采取刷新、限速或隔离措施。

作者指出，这种设计忽略了一个事实：不同 row 的脆弱性并不相同。若所有 row 都按最弱 row 保护，系统性能和能耗开销会增加；若按平均 row 保护，则弱 row 会暴露在攻击下。因此，空间变化既是风险，也是优化机会。

## 2. Background and Motivation / 背景与动机

### 原文位置
Page 2 - Page 4

### 中文翻译
背景部分介绍 RowHammer、read disturbance、NRH 以及常见防护机制。防护方案可以在 memory controller 中记录 activation count，也可以在 DRAM 内部实现概率刷新或 row tracking。无论机制如何，它们都需要决定什么时候触发保护。

作者用初步例子说明 spatial variation：如果某些 row 的 HCfirst 远高于最弱 row，那么对这些 row 采用同样保守的防护会浪费带宽和能量。这激励了 row-level profile 的思想。

## 3. Experimental Methodology / 实验方法

### 原文位置
Page 4 - Page 5

### 中文翻译
论文测试 144 颗 DDR4 chip，覆盖 10 种 chip design 和 3 家主要 DRAM 厂商。实验通过可控内存访问测量不同位置 row 的 bit error rate 和 HCfirst。作者关注多层空间粒度：module、chip、bank、subarray 和 row。

系统模拟部分使用多程序 memory-intensive workload，比较原始防护和加入 Svärd 后的性能。作者还构造 adversarial access pattern，以测试空间感知策略是否会被攻击者利用。

## 4. Characterization of Spatial Variation / 空间变化表征

### 原文位置
Page 5 - Page 9

### 中文翻译
表征结果显示，读扰动脆弱性在多个层级上变化。不同 chip 和 module 的总体脆弱性不同；同一 chip 内，不同 bank/subarray/row 也有显著差异。论文特别强调，同一 subarray 内部的 BER 可能相差约 2x，HCfirst 可能相差一个数量级。

作者进一步分析 row index、subarray 位置等特征是否能预测 vulnerability。结果并不理想：在 15 个被测试 module 中，只有 4 个显示出明显空间特征相关性。换句话说，空间变化存在，但它不总是呈现简单、可泛化的几何规律。

这一发现非常关键。它一方面支持利用 variation，另一方面否定了“只根据 row 位置猜测安全阈值”的简单方案。

## 5. Svärd Design / Svärd 设计

### 原文位置
Page 10 - Page 12

### 中文翻译
Svärd 的核心思想是：先获得 row-level 或 row-group-level vulnerability profile，然后根据每个 row 的脆弱性调整防护 aggressive 程度。弱 row 使用更严格阈值或更频繁刷新；强 row 则允许更宽松策略，从而减少不必要保护。

Svärd 并不替代具体防护机制，而是作为一个 spatial variation-aware layer。作者把它与 AQUA、BlockHammer、Hydra、PARA 和 RRS 结合，说明 profile 可以影响不同类型防护：计数型、概率型、限速型或刷新型。

设计上必须保证安全。即使大多数 row 较强，攻击者也可能专门访问最弱 row。因此 Svärd 不能简单降低全局防护强度，而要确保每个 row 都满足自己的安全 margin。

## 6. Evaluation / 评估

### 原文位置
Page 13 - Page 16

### 中文翻译
性能评估显示，加入 Svärd 后多种防护的性能开销下降。论文报告在 120 个 multiprogrammed memory-intensive workload 上，相对于原防护，Svärd+AQUA、Svärd+BlockHammer、Svärd+Hydra、Svärd+PARA、Svärd+RRS 分别获得 1.23x、2.65x、1.03x、1.57x、2.76x 平均性能改善。

这些收益来源于强 row 不再被最坏情况 row 拖累。尤其当原防护开销高、触发保护频繁时，空间感知策略带来的收益更明显。Hydra 的改善较小，说明某些防护本身开销结构不同，留给 Svärd 优化的空间有限。

对 adversarial pattern 的评估提醒读者：空间感知不是单纯性能优化。攻击者可以瞄准最弱 row，因此防护必须保留 per-row 安全约束。Figure 13 展示了在攻击访问下的行为差异。

## 7. Discussion / 讨论

### 原文位置
Page 16 - Page 17

### 中文翻译
讨论部分集中在 profile 的成本和稳定性。要部署 Svärd，系统需要知道 row-level vulnerability。这个 profile 可以来自制造测试、启动时测试、后台测试或运行时监测。但 RowHammer vulnerability 可能随温度、电压、老化和时间变化改变，因此 profile 需要更新或留出 guardband。

作者还强调，本文并不声称一个固定 profile 能永久保证安全。更现实的方向是让防护机制能够利用 profile，同时也能在不确定时退回保守策略。

## 8. Conclusion / 结论

### 原文位置
Page 17 - Page 18

### 中文翻译
论文结论是：真实 DRAM 芯片中的 read disturbance vulnerability 具有显著空间变化。利用这种变化可以显著降低 RowHammer mitigation 的性能开销，但前提是基于真实测量 profile，并保持对最弱 row 的安全保证。Svärd 证明了 spatial variation-aware defense 是未来低开销安全 DRAM 的可行方向。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | 空间变化动机 | 不同 row 脆弱性不同会造成统一防护过度保守 | 引出 Svärd | 先理解最弱 row 与强 row 的差别 |
| Figure 3-5 | Page 5-6 | chip/module 层级变化 | 不同 chip 和 module 的 BER/HCfirst 差异 | 说明 variation 不是局部噪声 | 看分布而非单点 |
| Figure 6-10 | Page 6-8 | bank/subarray/row 变化 | 同一 subarray 内也有明显差异 | 支撑 row-level profile | 这是 characterization 核心 |
| Figure 11 | Page 11-12 | Svärd 机制示意 | 如何将 profile 映射到防护 aggressive 程度 | 理解系统设计 | 对照文字看数据流 |
| Figure 12 | Page 13-15 | 性能结果 | Svärd 叠加多种防护降低开销 | 主要量化结果 | 注意不同 base defense 收益不同 |
| Figure 13 | Page 15-16 | adversarial pattern | 攻击者可集中访问弱 row | 检查安全性 | 重点看最坏情况而非平均 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 4 | 测试芯片信息 | 144 DDR4 chips, 10 designs, 3 vendors | 判断实验覆盖范围 | 先看样本规模 |
| Table 2 | Page 12 | Svärd 与防护组合 | 展示可结合的 mitigation 类型 | 说明 Svärd 通用性 | 对比各方案参数 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 未发现核心编号公式 | 全文 | 论文以实验和机制设计为主 | NRH、HCfirst、BER 是核心指标 | 关键在 profile 到防护参数的映射 | 否 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Spatial Variation | 空间变化 | Page 1 | 不同物理位置 row 的脆弱性差异 | 是 |
| Read Disturbance | 读扰动 | Page 1 | 访问某些 row 对其他 row 的影响 | 是 |
| HCfirst | 首错 hammer count | Page 5-8 | 第一个 bitflip 出现所需 activation 数 | 是 |
| Bit Error Rate (BER) | 位错误率 | Page 5-8 | bitflip 数与测试位数比例 | 是 |
| Subarray | 子阵列 | Page 5-8 | DRAM bank 内共享局部电路的 row group | 是 |
| Svärd | 空间变化感知防护框架 | Page 10-12 | 根据 row vulnerability profile 调整防护强度 | 是 |
| AQUA | RowHammer 防护方案 | Page 12-15 | Svärd 评估中的 base mitigation | 中 |
| BlockHammer | RowHammer 防护方案 | Page 12-15 | 通过限制高风险访问降低攻击能力 | 中 |
| Hydra | RowHammer 防护方案 | Page 12-15 | 计数/跟踪型防护 | 中 |
| PARA | Probabilistic Adjacent Row Activation | Page 12-15 | 概率刷新相邻 row 的经典方案 | 是 |
| RRS | Reactive Refresh Scheme | Page 12-15 | 响应式刷新防护 | 中 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- 空间特征不能稳定预测脆弱性，需要实际 profile；位置：Page 7-8。
- profile 可能受环境和时间影响，需要更新或 guardband；位置：Page 16 Discussion。

## 2. 论文中隐含的局限
- 主要实验对象是 DDR4，不能直接代表 HBM2、DDR5 或 LPDDR5。
- Svärd 的收益取决于 profile granularity；row-level profile 最准确但成本最高。

## 3. 实验设计可能存在的问题
- 系统模拟的 workload 与真实多租户攻击流量之间存在差距。
- adversarial pattern 覆盖有限，实际攻击者可能利用 profile 机制本身。

## 4. 方法可能不适用的场景
- vulnerability 随时间快速变化时，静态 profile 可能过期。
- 低成本系统无法存储或查询细粒度 row profile 时，Svärd 需要粗粒度近似，安全收益会下降。

## 5. 我阅读时应该追问的问题
- profile 应由 DRAM 厂商、BIOS、memory controller 还是 OS 维护？
- VRD 论文提出的 temporal variation 会不会使 Svärd 需要频繁重测？
- 如果攻击者知道哪些 row 更弱，是否能反过来增强攻击？
- Svärd 与 JEDEC PRAC/RFM 能否结合？

## 6. 后续可以继续阅读的方向
- Variable Read Disturbance：检查 profile 随时间变化的问题。
- Chronus/PRAC：理解工业防护与 adaptive profile 的结合点。
- HBM2 Read Disturbance：比较 DDR4 与 HBM2 的 spatial variation。""",
        "log": """# Extraction Log

- Input Type: GitHub repository PDF
- Source: `paper reading/sources/LEC3/2402.18652v1.pdf`
- Access Status: 已下载并可读取
- Full Text Retrieved: Yes
- PDF Pages: 19
- Sections Detected: Abstract, Introduction, Methodology, Characterization, Svärd Design, Evaluation, Discussion, Conclusion
- Figures Detected: Yes
- Tables Detected: Yes
- Equations Detected: 未发现核心编号公式
- Appendix Detected: 未发现明显独立 appendix
- Supplementary Material Detected: 未确认
- OCR Used: No
- Missing Content: 图中精确坐标值需回 PDF 查看
- Parsing Problems: `Svärd` 字符和部分作者名在 pdftotext 中可能显示不稳定
- Uncertain Parts: profile 获取成本的具体实现依赖系统设计，论文中部分属于未来方向
- Need User Action: 如需把 Figure 3-13 的数值逐项抄录，请人工指定图页或允许图像 OCR
- Quality Check: 已覆盖全文、主要图表、方法、实验、结果和局限；逐节译述不是逐字全文翻译
- Batch Status: 第二轮深度阅读完成""",
    },
    "2406.19094v3": {
        "title": "Understanding the Security Benefits and Overheads of Emerging Industry Solutions to DRAM Read Disturbance",
        "zh_title": "理解新兴工业 DRAM 读扰动解决方案的安全收益与开销",
        "authors": "Oğuzhan Canpolat, Yağmur Gizem Cirit, Ataberk Olgun, A. Giray Yağlıkçı, Minesh Patel, Onur Mutlu 等",
        "year": "2024",
        "venue": "arXiv:2406.19094v3",
        "topic": "JEDEC PRAC / RFM security and overhead analysis",
        "keywords": "PRAC, RFM, DDR5, RowHammer, read disturbance, memory security",
        "url": "https://arxiv.org/abs/2406.19094",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
这篇论文首次系统分析 JEDEC DDR5 PRAC/RFM 对 RowHammer/read disturbance 的安全收益、性能能耗成本和潜在可用性攻击，指出 PRAC 可在足够阈值下安全，但在低 NRH 未来芯片上成本可能极高。

## 2. 研究背景
DRAM 行锤击阈值持续下降，传统 TRR 不透明且多次被绕过。JEDEC 在 DDR5 中引入 PRAC 与 RFM，希望让 DRAM 片内计数并通知 memory controller 触发 refresh management。工业标准方案看似更正式，但学术界需要理解其安全边界和系统开销。

## 3. 核心问题
- PRAC/RFM 在什么 NRH 假设下能阻止 RowHammer bitflip。
- PRAC 的 timing changes 会带来多少性能和能耗开销。
- 与 Graphene、Hydra、PARA 等学术方案相比，PRAC 的开销如何。
- 攻击者是否能利用 PRAC/RFM 造成 memory availability/performance attack。

## 4. 核心贡献
- 对 2024 年 4 月 JEDEC DDR5 规范中的 PRAC/RFM 做首次严谨系统分析。
- 证明 PRAC 可配置为安全，前提是任何位置在 20 次访问前不会产生 bitflip，即 NRH >= 20。
- 量化 benign workload 下的性能和 DRAM energy overhead。
- 展示未来 NRH 降至 20 时 PRAC 性能开销可达 84.7% 平均、94.0% 最大，能耗开销可达 13x 平均、18x 最大。
- 指出 adversarial pattern 可占用最多 94% DRAM throughput，使系统性能平均下降 86.8%、最高 94.5%。
- 与 Graphene、Hydra、PARA 比较，说明 PRAC 在低 NRH 下相对 PARA 更好，但现代高 NRH 下不总是最优。

## 5. 方法概述
论文建模 PRAC：DRAM 为 row activation 维护片内计数，当接近阈值时向 memory controller 发出 back-off signal。控制器暂停普通请求并发出 RFM 命令，触发 DRAM 刷新潜在 victim rows。作者通过理论安全分析和 cycle-level/system-level 模拟评估性能、能耗、存储开销及攻击行为。

## 6. 实验设计
作者评估 60 个 benign four-core workload，覆盖现代 NRH 10000/4800/1000 和未来 NRH 128/64/20。比较对象包括 Graphene、Hydra、PARA。指标包括 system performance slowdown、DRAM energy overhead、storage cost、DRAM throughput loss 和 adversarial workload 下的性能下降。

## 7. 主要结果
- PRAC 在 NRH >= 20 时可通过配置保证安全；见 Page 3-4, security analysis。
- 对现代 NRH 10000/4800/1000，PRAC 平均/最大性能开销约 9.9%/13.1%，DRAM energy overhead 18.5%/22.7%；见 Page 5-6, Figure 2-3。
- 对未来 NRH=20，PRAC 平均/最大性能开销约 84.7%/94.0%，能耗开销约 13x/18x；见 Page 5-6。
- availability attack 可占据最多 94% DRAM throughput，并造成平均 86.8%、最高 94.5% 系统性能下降；见 Page 7, attack analysis。

## 8. 关键结论
PRAC 是工业界向透明标准化 RowHammer 防护迈进的重要一步，但它不是免费午餐。随着 NRH 下降，强制 RFM 和 timing overhead 会急剧放大，甚至带来新的可用性攻击面。

## 9. 局限性
分析基于公开 JEDEC 语义和模拟模型；实际 DRAM 厂商实现细节、PRAC counter granularity、内部 victim selection 可能不同。论文主要关注 read disturbance，对真实 exploit、OS isolation 和 mixed workloads 的覆盖有限。

## 10. 适合我重点关注的内容
重点看 PRAC/RFM 背景、security proof 条件、Figure 2-4 的性能/能耗/存储开销，以及 availability attack 部分。

## 11. 和其他文献的关系
这篇是 Chronus 的直接前置工作：先指出 PRAC 的安全边界与开销，再由 Chronus 提出改进。它也与 DSAC、Graphene、Hydra、PARA 等防护形成比较脉络。""",
        "key_points": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | PRAC/RFM 是 JEDEC DDR5 中面向 RowHammer 的新工业机制 | Page 2, Background | DRAM 片内计数并通过 back-off/RFM 协同 memory controller | 高 | 标准化方案值得系统级评估 |
| 2 | PRAC 可配置为安全，但依赖 NRH >= 20 条件 | Page 3-4, Security Analysis | 论文证明任意位置 20 次访问前不 flip 时可防护 | 高 | 安全边界很低但并非无条件 |
| 3 | PRAC 增加 tRP/tRC 等关键 timing | Page 2-3 | counter update 和 RFM 协议改变命令时序 | 高 | 性能开销来自正常访问路径和防护路径 |
| 4 | 现代 NRH 下 PRAC 仍有可观性能/能耗开销 | Page 5-6, Figure 2-3 | NRH 10K/4.8K/1K 平均性能 9.9%，能耗 18.5% | 高 | 即使不是未来极低阈值，也不是零成本 |
| 5 | NRH=20 时 PRAC 开销灾难性增加 | Page 5-6, Figure 2-3 | 平均性能开销 84.7%，能耗 13x | 高 | 说明未来工艺缩小会压垮固定协议 |
| 6 | PRAC 与 Graphene/Hydra/PARA 的相对优劣依赖 NRH | Page 6, comparative evaluation | 低 NRH 下优于 PARA，现代高 NRH 下不总是优于学术方案 | 中 | 方案选择必须看阈值区间 |
| 7 | PRAC 引入 memory performance attack 面 | Page 7, Attack Analysis | adversarial pattern 可占用最多 94% throughput | 高 | 防护机制本身可能成为 DoS 放大器 |
| 8 | storage cost 需要纳入工业可行性分析 | Page 6, Figure 4 | 片内 counter 与实现成本评估 | 中 | 工业方案受面积/成本强约束 |
| 9 | RFM 减少不必要周期性刷新但增加强制暂停 | Page 2, PRAC/RFM overview | back-off 后控制器必须发 RFM | 中 | 它在 refresh 精准性和服务中断之间取舍 |
| 10 | 本文为 Chronus 提供问题定义 | Page 8 Conclusion | 结论指出需要更低开销和更抗攻击方案 | 中 | Chronus 的设计动机基本从这里来 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
以下为基于 PDF 提取文本的逐节中文详译/译述。为遵守版权边界，不提供逐字长篇翻译；技术术语、指标和机制名称保留英文。

## Title
原文标题：Understanding the Security Benefits and Overheads of Emerging Industry Solutions to DRAM Read Disturbance

中文标题：理解新兴工业 DRAM 读扰动解决方案的安全收益与开销

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文分析 DDR5 标准中新出现的 PRAC/RFM 机制。PRAC 让 DRAM 在片内跟踪 row activation，并在需要时通知 memory controller 触发 RFM。作者从安全、性能、能耗、存储成本和攻击面角度评估该机制。结论是：PRAC 可以在特定 NRH 条件下提供安全保证，但随着 RowHammer threshold 降低，它的性能和能耗开销会急剧上升，并可能被攻击者用来制造内存可用性攻击。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2

### 中文翻译
引言强调 RowHammer 防护已经从学术问题变成工业标准问题。过去厂商使用 TRR-like 机制，但实现不透明且已有绕过案例。JEDEC 的 PRAC/RFM 是更公开、标准化的方向，因此需要认真评估它是否足够安全，以及部署代价是否可接受。

作者提出一个核心矛盾：如果未来 DRAM 的 NRH 继续降低，任何防护都必须更频繁地触发。PRAC 虽然把一部分逻辑放入 DRAM 内部，但它仍需要 memory controller 停止正常请求并执行 RFM。因此低 NRH 可能把保护流量变成主要瓶颈。

## 2. Background: PRAC and RFM / 背景：PRAC 与 RFM

### 原文位置
Page 2 - Page 3

### 中文翻译
PRAC 即 Per-Row Activation Counting。DRAM 片内维护与 row activation 相关的计数或近似计数，当某些 row 接近危险阈值时，DRAM 向 memory controller 发出 back-off signal。控制器收到信号后需要暂停普通内存访问，并发出 RFM 命令。

RFM 即 Refresh Management。它让 DRAM 执行与潜在 victim row 相关的额外刷新，以避免电荷被扰动到错误状态。PRAC/RFM 的目标是比传统固定周期刷新更有针对性，但这也引入了新的 timing constraints，如 tRP/tRC 增加，以及 back-off 期间的服务中断。

## 3. Security Analysis / 安全分析

### 原文位置
Page 3 - Page 4

### 中文翻译
安全分析试图回答：PRAC 在什么条件下可以阻止 RowHammer。作者给出一个关键结论：如果 DRAM 中任何位置在被访问 20 次之前不会产生 bitflip，即 NRH 至少为 20，那么 PRAC 可以通过适当配置保证安全。

这个结论的重要性在于，它把 PRAC 的安全边界明确化。PRAC 不是靠概率侥幸工作，而是可以在特定 threshold 假设下给出形式化 reasoning。但这个假设也说明，如果未来器件的有效阈值低于该范围，或者 RowPress/VRD 等现象使实际风险偏离 activation count 模型，PRAC 需要重新评估。

## 4. Performance and Energy Evaluation / 性能与能耗评估

### 原文位置
Page 4 - Page 6

### 中文翻译
作者用 60 个四核 benign workload 评估 PRAC。对现代 NRH 设置 10000、4800 和 1000，PRAC 的平均性能开销约 9.9%，最大约 13.1%；DRAM energy overhead 平均约 18.5%，最大约 22.7%。这些结果说明，即使在相对宽松阈值下，PRAC 也会带来非忽略的系统代价。

当 NRH 降至未来更严苛的 128、64、20 时，开销急剧上升。特别是 NRH=20 时，平均性能开销约 84.7%，最大约 94.0%；能耗开销可达 13x 平均、18x 最大。此时系统大量时间花在防护相关等待和 RFM 上，正常内存服务被严重挤压。

## 5. Comparison with Prior Defenses / 与已有防护比较

### 原文位置
Page 6

### 中文翻译
论文将 PRAC 与 Graphene、Hydra 和 PARA 比较。结果不是单向的：在较低 NRH 区间，PRAC 相比 PARA 更有优势，因为 PARA 的概率刷新需要非常频繁才能保证安全；与 Graphene/Hydra 相比，PRAC 在某些低阈值下表现接近。

但在现代较高 NRH 下，一些学术方案可能以更低性能开销达到类似目标。这说明工业标准方案的价值不仅在性能，还在可部署性、标准化和片内可见性；但从系统效率角度，它仍有改进空间。

## 6. Storage and Implementation Cost / 存储与实现成本

### 原文位置
Page 6, Figure 4

### 中文翻译
PRAC 需要在 DRAM 片内维护 activation tracking 相关状态。论文估算 counter/storage cost，并将其作为工业可行性的一部分。对 DRAM 厂商来说，面积和功耗成本非常敏感，因此防护设计必须在安全性、存储开销、时序开销之间平衡。

## 7. Memory Performance Attack / 内存性能攻击

### 原文位置
Page 7

### 中文翻译
作者进一步指出，PRAC/RFM 可能成为攻击者利用的性能攻击面。攻击者可以构造访问模式频繁触发 back-off 和 RFM，使 memory controller 大量时间无法服务正常请求。论文报告 adversarial pattern 最多可占用 94% DRAM throughput，使系统性能平均下降 86.8%，最高下降 94.5%。

这个结果非常重要，因为防护机制原本用于阻止 RowHammer bitflip，但如果它能被廉价触发并造成服务降级，就会形成新的 denial-of-service 风险。

## 8. Discussion / 讨论

### 原文位置
Page 7 - Page 8

### 中文翻译
讨论部分强调未来方案需要同时满足安全、低开销和抗滥用。单纯把 activation counter 放进 DRAM 并不自动解决问题；关键在于 counter 更新是否在关键路径上、RFM 是否会阻塞正常请求、保护刷新数量是否固定、以及攻击者能否操纵触发频率。

这些观察直接引出后续 Chronus 一类方案：通过改进计数器组织、动态控制刷新数量和消除不必要 delay 来降低开销。

## 9. Conclusion / 结论

### 原文位置
Page 8

### 中文翻译
本文结论是：PRAC/RFM 是 RowHammer 防护标准化的重要进展，能够在一定 NRH 假设下提供安全保证。然而，它在性能、能耗和可用性攻击方面存在显著挑战。若 DRAM vulnerability 继续恶化，现有 PRAC 设计可能无法以可接受成本维持安全。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 4 | PRAC 安全分析/最大 activation | 展示 PRAC 配置下 victim 前可发生的最大激活数 | 支撑 NRH >= 20 的安全结论 | 结合 security analysis 读 |
| Figure 2 | Page 5 | 性能开销 | PRAC 在不同 NRH 下 slowdown 急剧变化 | 本文主要系统结果 | 注意现代和未来 NRH 的分界 |
| Figure 3 | Page 6 | DRAM energy overhead | RFM 和 timing overhead 带来能耗增长 | 说明问题不只是性能 | 与 Figure 2 对照 |
| Figure 4 | Page 6 | storage cost | 片内状态规模和成本估计 | 工业可行性关键 | 看 counter granularity 假设 |
| Figure 5 | Page 7 | performance attack | adversarial pattern 抢占 DRAM throughput | 揭示新攻击面 | 重点读攻击模式描述 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 3 | PRAC/RFM timing 参数 | PRAC 增加/改变关键 DRAM timing | 性能开销的直接来源 | 结合 tRP/tRC 理解 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 安全不等式/阈值推理 | Page 3-4 | 证明 PRAC 在 NRH >= 20 下安全 | NRH 为触发 bitflip 所需激活阈值 | 最大可能扰动小于 bitflip 阈值即安全 | 是 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| PRAC | Per-Row Activation Counting | Page 1-3 | DDR5 中片内跟踪 row activation 的机制 | 是 |
| RFM | Refresh Management | Page 1-3 | memory controller 触发 DRAM 执行额外保护刷新 | 是 |
| Back-off Signal | 回退信号 | Page 2 | DRAM 通知控制器暂停普通请求并执行 RFM | 是 |
| NRH | RowHammer threshold | Page 3-6 | 触发 RowHammer bitflip 所需 activation 数 | 是 |
| tRP/tRC | DRAM timing 参数 | Page 2-3 | precharge/row cycle 等关键时序 | 是 |
| Graphene | RowHammer 防护方案 | Page 6 | 计数型 memory controller defense | 中 |
| Hydra | RowHammer 防护方案 | Page 6 | 低开销 tracking defense | 中 |
| PARA | Probabilistic Adjacent Row Activation | Page 6 | 概率性相邻行刷新方案 | 中 |
| Memory Performance Attack | 内存性能攻击 | Page 7 | 利用防护机制降低系统吞吐 | 是 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- PRAC 分析基于公开规范和模型，实际厂商实现可能不同；位置：Page 7 Discussion。
- 低 NRH 下 PRAC 开销很高，需要未来机制改进；位置：Page 5-8。

## 2. 论文中隐含的局限
- 安全分析基于 activation-count 模型，对 RowPress 的 row-open time 维度覆盖有限。
- 真实系统中的 cache、OS 页面分配、地址映射会影响攻击者能否稳定触发 PRAC。

## 3. 实验设计可能存在的问题
- 使用模拟 workload，实际服务器/GPU 混合负载可能有不同 memory behavior。
- 能耗模型依赖参数假设，真实 DDR5 实现可能偏离。

## 4. 方法可能不适用的场景
- NRH 低于 20 或 temporal variation 导致瞬时阈值更低时，PRAC 的安全保证需要重新审视。
- 如果 DRAM 内部 victim selection 不透明，系统很难验证 RFM 是否覆盖所有风险 row。

## 5. 我阅读时应该追问的问题
- PRAC 能否处理 RowPress 或 Variable Read Disturbance？
- 攻击者能否通过 page coloring 或 huge page 获得更稳定 row mapping？
- PRAC 与 on-die ECC 的交互是否会隐藏早期 bitflip？
- Chronus 的改进是否完全解决 availability attack？

## 6. 后续可以继续阅读的方向
- Chronus：直接改进 PRAC。
- DSAC：另一种 in-DRAM 计数近似防护。
- Variable Read Disturbance：挑战固定 NRH 假设。""",
        "log": """# Extraction Log

- Input Type: GitHub repository PDF
- Source: `paper reading/sources/LEC3/2406.19094v3.pdf`
- Access Status: 已下载并可读取
- Full Text Retrieved: Yes
- PDF Pages: 10
- Sections Detected: Abstract, Introduction, Background, Security Analysis, Evaluation, Attack Analysis, Discussion, Conclusion
- Figures Detected: Yes
- Tables Detected: Yes
- Equations Detected: 安全阈值推理，未发现复杂编号公式
- Appendix Detected: 未发现明显 appendix
- Supplementary Material Detected: 未确认
- OCR Used: No
- Missing Content: JEDEC 原规范全文未随 PDF 提供；本文只处理论文可访问内容
- Parsing Problems: 部分百分比和图注需回 PDF 复核精确格式
- Uncertain Parts: 实际 PRAC 厂商实现与论文模型可能不同
- Need User Action: 若需标准条文级核对，请提供 JEDEC 文档或允许只基于论文讨论
- Quality Check: 已覆盖安全分析、性能、能耗、storage、攻击和局限；逐节译述不是逐字全文翻译
- Batch Status: 第二轮深度阅读完成""",
    },
    "2502.12650v2": {
        "title": "Chronus: Understanding and Securing the Cutting-Edge Industry Solutions to DRAM Read Disturbance",
        "zh_title": "Chronus：理解并加固前沿工业 DRAM 读扰动解决方案",
        "authors": "Oğuzhan Canpolat, Yağmur Gizem Cirit, Ataberk Olgun, A. Giray Yağlıkçı, Minesh Patel, Onur Mutlu 等",
        "year": "2025",
        "venue": "HPCA 2025 / arXiv:2502.12650v2",
        "topic": "Chronus / improved PRAC / DRAM read disturbance defense",
        "keywords": "Chronus, PRAC, RFM, RowHammer, wave attack, feinting attack, DRAM",
        "url": "https://arxiv.org/abs/2502.12650",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
Chronus 针对 JEDEC PRAC 的关键路径计数、固定保护刷新和 delay-period 弱点提出改进，通过并行 counter update、动态保护刷新数量和取消延迟期，在现代与未来 NRH 下显著降低性能/能耗开销并提升抗攻击能力。

## 2. 研究背景
前一篇 PRAC 分析说明工业标准方案可提供安全保证，但在低 NRH 下开销大且存在可用性攻击。Chronus 进一步研究 PRAC 的内部设计瓶颈：counter update 影响 tRP/tRC，固定 preventive refresh 数量不能适应不同攻击强度，refresh 后的 delay period 会被 wave attack/feinting attack 利用。

## 3. 核心问题
- PRAC 的哪些机制导致高性能和能耗开销。
- 现有 PRAC variant 在 adversarial pattern 下为什么需要保守阈值。
- 是否能重新组织 DRAM 内部计数和刷新调度，使安全与性能同时改善。
- Chronus 在不同 NRH、benign workload 和攻击 pattern 下是否优于 PRAC、Graphene、Hydra、PARA。

## 4. 核心贡献
- 系统分析 PRAC 的 timing overhead 与安全弱点。
- 提出 wave attack 和 feinting attack，说明固定刷新和 delay period 可被利用。
- 设计 Chronus，将 activation counters 与 data path 分离，使 counter update 与正常访问并行。
- 动态控制 preventive refresh 数量，并去除固定 delay period。
- 在现代 NRH=1K 下平均性能开销低于 0.1%，DRAM energy overhead 约 10.3%。
- 在未来 NRH=20 下平均性能开销约 8.3%，能耗约 17.9%，显著优于 PRAC variants。
- 与 Graphene、Hydra、PARA 比较，Chronus 在多种 NRH 区间保持较好综合表现。

## 5. 方法概述
Chronus 的设计有三条主线：第一，把 activation counter 组织从关键数据路径中移出，使 row activation 期间可并行更新计数；第二，根据风险动态决定 preventive refresh 数量，不再使用固定数量；第三，取消 PRAC 中 refresh 后的 delay period，避免攻击者利用周期性窗口组织 wave/feinting pattern。

## 6. 实验设计
论文使用与 PRAC 分析类似的 workload 和模拟框架，评估现代 NRH 与未来更低 NRH。比较对象包括三种 PRAC variant、Graphene、Hydra、PARA，并分析 benign workload、adversarial attack、DRAM energy、performance overhead 和实现成本。论文附录还包含 artifact 信息和修正说明。

## 7. 主要结果
- PRAC 在现代 NRH>1K 下平均/最大性能开销约 5.8%/8.9%，能耗 10.7%/13.5%；在 NRH=20 下性能开销 78.5%/90.7%，能耗 6.6x/7.1x；见 Page 6-8。
- Chronus 在 NRH=1K 下平均性能开销低于 0.1%，能耗约 10.3%；见 Page 10-12。
- Chronus 在 NRH=20 下平均性能开销约 8.3%，能耗约 17.9%；见 Page 10-12。
- Chronus 对 wave attack/feinting attack 更稳健，因为不依赖固定 delay window 和固定刷新数量；见 Page 4-5, Figure 2-3。

## 8. 关键结论
PRAC 的问题不是“片内计数”方向错误，而是具体协议和时序组织不够灵活。Chronus 说明，若把计数、刷新和控制器协同重新设计，可以让工业可部署方案在低 NRH 时代仍接近可用。

## 9. 局限性
Chronus 仍是论文级设计和模拟评估，真实 DDR5/DDR6 采用需要标准与厂商实现支持。附录中的 errata 表明早期结果有 bug 修正，阅读时应以 v2 结果为准。对 RowPress、VRD 和跨代 DRAM 的覆盖仍需进一步验证。

## 10. 适合我重点关注的内容
重点读 PRAC weakness 分析、Figure 2 的 wave/feinting attack、Chronus design、performance/energy evaluation，以及附录 errata。

## 11. 和其他文献的关系
Chronus 是 PRAC 分析论文的直接后续；与 DSAC 都属于 in-DRAM/industry-oriented 防护；与 Variable Read Disturbance 结合阅读可理解固定阈值方案在 temporal variation 下的风险。""",
        "key_points": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | PRAC counter update 增加关键 DRAM timing | Page 3, Table 1 | tRP/tRC 等参数受影响 | 高 | 这是正常 workload 开销的根源 |
| 2 | 固定 preventive refresh 和 delay period 可被攻击利用 | Page 4-5, Figure 2 | wave attack/feinting attack | 高 | 防护协议的确定性会暴露节奏 |
| 3 | Chronus 将 counter 与 data 分离并行更新 | Page 6-7, Chronus design | counter update 不再阻塞访问关键路径 | 高 | 核心性能优化 |
| 4 | Chronus 动态控制 preventive refresh 数量 | Page 7-8 | 根据风险调整刷新而非固定次数 | 高 | 减少过度刷新，也提升安全 |
| 5 | Chronus 移除 refresh 后固定 delay period | Page 7-8 | 避免 wave/feinting attack 利用窗口 | 高 | 核心安全优化 |
| 6 | 现代 NRH 下 Chronus 几乎无性能开销 | Page 10-12, Evaluation | NRH=1K 平均性能开销 <0.1% | 高 | 与 PRAC 的 5.8%+ 形成对比 |
| 7 | NRH=20 下 Chronus 仍保持可接受开销 | Page 10-12 | 平均性能 8.3%，能耗 17.9% | 高 | 面向未来低阈值的重要结果 |
| 8 | Chronus 优于多种 PRAC variant 与 Graphene/Hydra/PARA | Page 10-13 | 多方案比较 | 中 | 表明设计同时改善性能与安全 |
| 9 | 附录包含 errata/bug 修正 | Appendix B | 旧/新结果表说明修正 | 高 | 引用时必须标注版本 |
| 10 | 对 RowPress/VRD 的覆盖仍需额外研究 | Discussion/Limitations | 机制主要围绕 activation count | 中 | 低 NRH 之外还有 row-open time 和 temporal variation 问题 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
以下为基于 PDF 提取文本的逐节中文详译/译述，不提供逐字长篇翻译。本文为 2025 年较新版本，附录包含结果修正说明；笔记按当前 PDF v2 记录。

## Title
原文标题：Chronus: Understanding and Securing the Cutting-Edge Industry Solutions to DRAM Read Disturbance

中文标题：Chronus：理解并加固前沿工业 DRAM 读扰动解决方案

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文研究工业界最新的 DRAM read disturbance 防护，尤其是 PRAC/RFM。作者指出 PRAC 虽然朝标准化方向前进，但仍存在性能、能耗和安全弱点。论文提出 Chronus，通过重新组织片内计数器、动态保护刷新和去除固定延迟，显著降低开销并提升对攻击访问模式的抵抗能力。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2

### 中文翻译
引言说明 RowHammer threshold 继续下降，传统防护越来越难以承受。PRAC 代表工业界将 row activation tracking 放入 DRAM 的努力，但初步研究显示其成本很高，尤其在未来低 NRH 下可能使系统不可用。

作者认为，需要更深入地理解 PRAC 的设计弱点，而不是简单否定片内计数方向。Chronus 的目标是在保持工业可部署性的同时，减少关键路径开销并避免攻击者利用固定刷新节奏。

## 2. Background and PRAC Weaknesses / 背景与 PRAC 弱点

### 原文位置
Page 2 - Page 5

### 中文翻译
背景部分回顾 PRAC/RFM 工作方式。DRAM 跟踪 row activation，当风险升高时向 memory controller 发出 back-off；控制器随后发出 RFM，让 DRAM 执行 preventive refresh。

论文指出三类问题。第一，activation counter update 位于关键时序路径上，导致 tRP/tRC 等 timing 增加，即使没有攻击也影响正常访问。第二，PRAC 使用固定数量的 preventive refresh，不能根据实际风险灵活调整。第三，refresh 后存在 delay period，攻击者可以围绕这一固定窗口构造 wave attack 或 feinting attack，从而迫使系统使用更保守阈值。

## 3. Attacks on PRAC Variants / 对 PRAC 变体的攻击

### 原文位置
Page 4 - Page 6

### 中文翻译
wave attack 利用 PRAC 的刷新与延迟节奏，让 aggressor activation 分布在多个窗口中，从而尽可能接近或超过危险累积扰动。feinting attack 则通过诱导防护机制关注某些 row 或时段，掩护真正危险的访问序列。

这些攻击说明，防护机制的确定性本身会成为攻击面。如果防护总是在固定条件下执行固定数量刷新，并在固定时间后恢复，攻击者就可以学习这个节奏。

## 4. Chronus Design / Chronus 设计

### 原文位置
Page 6 - Page 9

### 中文翻译
Chronus 的第一项设计是把 counter 与 data 分离。传统 PRAC 在访问过程中更新计数，可能延长关键 timing；Chronus 让 counter update 与数据访问并行，避免把计数逻辑放在 tRP/tRC 关键路径上。

第二项设计是动态控制 preventive refresh 数量。与固定刷新次数不同，Chronus 根据当前风险状态决定需要刷新多少 victim row，从而在安全时减少无效刷新，在高风险时提供足够保护。

第三项设计是去除固定 delay period。这样攻击者无法围绕固定延迟窗口组织 wave 或 feinting pattern，也减少了 memory controller 被迫等待的时间。

## 5. Evaluation Methodology / 评估方法

### 原文位置
Page 9 - Page 10

### 中文翻译
评估使用 cycle-level/system-level 模拟，覆盖现代和未来 NRH。工作负载包括多程序 memory-intensive workloads；比较对象包括多个 PRAC variant 以及 Graphene、Hydra、PARA。指标包括性能开销、DRAM energy overhead、攻击模式下的稳健性和实现成本。

## 6. Results / 结果

### 原文位置
Page 10 - Page 13

### 中文翻译
结果显示，PRAC 变体在现代 NRH 下已有明显开销，在未来低 NRH 下开销急剧恶化。论文报告 PRAC 在现代 NRH>1K 时平均/最大性能开销约 5.8%/8.9%，能耗 10.7%/13.5%；NRH=20 时性能开销升至 78.5%/90.7%，能耗 6.6x/7.1x。

Chronus 显著改善这一情况。在 NRH=1K 时，Chronus 平均性能开销低于 0.1%，DRAM energy overhead 约 10.3%。在 NRH=20 时，Chronus 平均性能开销约 8.3%，能耗开销约 17.9%。这说明 Chronus 在极低阈值下仍能保持系统可用性。

与 Graphene、Hydra 和 PARA 相比，Chronus 的综合表现更稳定。它既避免 PARA 在低 NRH 下概率刷新过多的问题，也避免 PRAC 固定 RFM 和 delay 带来的严重阻塞。

## 7. Discussion / 讨论

### 原文位置
Page 13 - Page 15

### 中文翻译
讨论部分强调 Chronus 的意义：它不是完全重写 DRAM 系统，而是在 PRAC/RFM 思路上修改关键设计点，使工业方向更可持续。作者也讨论实现成本、与标准兼容性、以及未来低 threshold DRAM 的需求。

需要注意的是，Chronus 仍主要围绕 activation-count based RowHammer。对于 RowPress 中的 row-open time、Variable Read Disturbance 中的 temporal variation，以及复杂 on-die ECC 行为，仍需要进一步扩展分析。

## Appendix / 附录

### 原文位置
Appendix A-B

### 中文翻译
附录包含 decrementer/counter 相关实现细节、artifact 说明以及结果修正说明。论文 v2 明确给出早期结果 bug 的修正表，并说明主要结论保持不变。阅读和引用时应使用修正后的数值。

## Conclusion / 结论

### 原文位置
Page 15

### 中文翻译
Chronus 证明，PRAC 的工业方向可以通过更好的计数器组织、动态刷新和去确定性延迟得到显著改进。在未来 RowHammer threshold 继续下降的情况下，这类低开销、抗攻击的片内/控制器协同防护可能成为 DRAM 安全的关键。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2-3 | PRAC/RFM 基础流程 | DRAM 计数、back-off、RFM 的协同 | 理解 Chronus 修改点 | 先看再读设计 |
| Figure 2 | Page 4 | wave/feinting attack | 固定刷新与 delay 可被攻击利用 | Chronus 安全动机 | 重点图 |
| Figure 3 | Page 5 | PRAC 最大 activation/攻击窗口 | PRAC variants 仍需保守配置 | 连接攻击和性能开销 | 对照 security text |
| Figure 4-6 | Page 10-12 | 性能/能耗结果 | Chronus 在不同 NRH 下显著优于 PRAC | 主要实验结论 | 注意 v2 修正数值 |
| Figure 7+ | Page 12-13 | 与 Graphene/Hydra/PARA 比较 | Chronus 综合表现稳定 | 放在防护谱系中理解 | 看不同 NRH 区间 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 3 | PRAC timing 参数 | counter update 增加关键 timing | 性能问题根源 | 重点看 tRP/tRC |
| Appendix Table | Appendix B | 结果修正 | v2 修正早期 bug 后数值变化 | 引用必须用新数值 | 回 PDF 核对 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 安全阈值推理 | Page 4-6 | 分析攻击窗口内最大扰动 | NRH、refresh count、delay window | 防护必须保证窗口内累积扰动低于 NRH | 是 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Chronus | Chronus 防护机制 | Page 1, Page 6-9 | 改进 PRAC 的片内/控制器协同防护 | 是 |
| PRAC | Per-Row Activation Counting | Page 1-3 | DDR5 row activation tracking 机制 | 是 |
| RFM | Refresh Management | Page 1-3 | 保护刷新命令/机制 | 是 |
| Preventive Refresh | 预防性刷新 | Page 3-8 | 在 bitflip 前刷新潜在 victim row | 是 |
| Wave Attack | 波形攻击 | Page 4-5 | 利用固定刷新/延迟窗口累积扰动的攻击 | 是 |
| Feinting Attack | 佯攻攻击 | Page 4-5 | 诱导防护误判或分散资源的访问模式 | 是 |
| Delay Period | 延迟期 | Page 3-8 | RFM 后控制器/DRAM 等待窗口 | 是 |
| Counter-Data Separation | 计数器与数据路径分离 | Page 6-7 | Chronus 避免计数更新阻塞关键路径的设计 | 是 |
| NRH | RowHammer threshold | Page 4-13 | 触发 bitflip 所需 activation 数 | 是 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- 结果修正说明显示早期实验/模拟存在 bug，需以 v2 附录修正值为准；位置：Appendix B。
- Chronus 仍需工业标准和 DRAM 实现支持；位置：Discussion。

## 2. 论文中隐含的局限
- 评估主要基于模拟，真实芯片实现可能暴露新的 timing/area/power 问题。
- 机制主要面向 activation-count disturbance，对 RowPress/VRD 的完整覆盖不足。

## 3. 实验设计可能存在的问题
- 与 PRAC variants 的公平比较依赖具体参数配置。
- attack model 是否覆盖最强攻击者仍需更多形式化分析。

## 4. 方法可能不适用的场景
- 如果 DRAM 标准无法支持 counter-data separation 或动态 RFM，Chronus 难以部署。
- 对极端低 NRH 或 row-open-time 主导的扰动，Chronus 可能仍需扩展。

## 5. 我阅读时应该追问的问题
- Chronus 如何与 JEDEC 实际命令/时序兼容？
- 动态 refresh 数量是否会泄露 side-channel 信息？
- VRD 下如果 NRH 随时间突然降低，Chronus 如何更新配置？
- Chronus 与 spatial profile/Svärd 能否组合？

## 6. 后续可以继续阅读的方向
- PRAC analysis paper：理解 Chronus 针对的问题。
- Variable Read Disturbance：检查阈值时间变化。
- DSAC：比较 in-DRAM stochastic/approximate counting 思路。""",
        "log": """# Extraction Log

- Input Type: GitHub repository PDF
- Source: `paper reading/sources/LEC3/2502.12650v2.pdf`
- Access Status: 已下载并可读取
- Full Text Retrieved: Yes
- PDF Pages: 22
- Sections Detected: Abstract, Introduction, Background, PRAC Analysis, Attacks, Chronus Design, Evaluation, Discussion, Appendix, Conclusion
- Figures Detected: Yes
- Tables Detected: Yes
- Equations Detected: 安全阈值推理和机制公式，需回 PDF 精确复核
- Appendix Detected: Yes
- Supplementary Material Detected: Artifact information in appendix
- OCR Used: No
- Missing Content: 图中精确数值未全部逐项抄录
- Parsing Problems: 部分附录表格在 pdftotext 中列对齐不稳定
- Uncertain Parts: 真实工业实现可行性需标准/厂商信息确认
- Need User Action: 引用结果时建议回 PDF 核对 v2 errata 表
- Quality Check: 已覆盖 PRAC 问题、攻击、Chronus 设计、评估、附录修正和局限；逐节译述不是逐字全文翻译
- Batch Status: 第二轮深度阅读完成""",
    },
    "2502.13075v1": {
        "title": "Variable Read Disturbance: An Experimental Analysis of Temporal Variation in DRAM Read Disturbance",
        "zh_title": "可变读扰动：DRAM 读扰动时间变化的实验分析",
        "authors": "Ataberk Olgun, F. Nisa Bostanci, Minesh Patel, Hasan Hassan, Onur Mutlu 等",
        "year": "2025",
        "venue": "arXiv:2502.13075v1",
        "topic": "Temporal variation in DRAM read disturbance / VRD",
        "keywords": "Variable Read Disturbance, VRD, RowHammer, RDT, temporal variation, guardband, ECC",
        "url": "https://arxiv.org/abs/2502.13075",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
这篇论文通过 160 颗 DDR4 和 4 颗 HBM2 芯片的大规模实验提出 Variable Read Disturbance（VRD），证明同一 DRAM row 的 read disturbance threshold 会随时间显著且不可预测地变化，从而挑战基于一次或少数几次 profiling 的 RowHammer 防护。

## 2. 研究背景
许多 RowHammer 防护依赖一个关键参数：某 row 或某芯片触发 bitflip 的最小阈值 RDT/NRH。如果该阈值可通过测试稳定获得，系统就能据此设置防护。然而，若阈值随时间变化，尤其是偶尔出现更低阈值，那么 profile 可能高估安全 margin。

## 3. 核心问题
- 同一 row 的 read disturbance threshold 是否随时间变化。
- 需要多少次测量才能观察到真实最小 RDT。
- VRD 是否普遍存在于 DDR4/HBM2、不同厂商和不同测试参数中。
- guardband 与 ECC 是否足以弥补 RDT 不确定性。
- 现有 RowHammer mitigation 在 VRD 下有哪些风险。

## 4. 核心贡献
- 提出并命名 Variable Read Disturbance（VRD）。
- 在 160 颗 DDR4 和 4 颗 HBM2 芯片、3 家厂商上进行大规模实验。
- 发现单个 row 的最小 RDT 可能在数万次测量后才出现，最多观察到 94,467 次测量后才得到最低值。
- 发现同一 row 的最小 RDT 可比最大观测 RDT 小 3.5x。
- 发现 97.1% 测试 row 在所有参数组合下表现出 VRD，其余 2.9% 至少在一个组合下表现出 VRD。
- 评估 guardband 与 ECC，指出它们可缓解但不能单独构成稳健解决方案。
- 呼吁在线 RDT profiling 和 runtime-configurable mitigation。

## 5. 方法概述
作者对同一 row 反复测量 RDT，记录每次触发 bitflip 所需 activation 数，并观察序列随时间的变化。实验覆盖不同 data pattern、tAggON、温度、芯片密度/工艺节点。随后评估如果系统只测量一次或少量次数，会多大概率错过真实低阈值。

## 6. 实验设计
实验对象包括 160 颗 DDR4 chips 和 4 颗 HBM2 chips，覆盖 3 家厂商。主要指标是 RDT 分布、最小 RDT 出现的测量次数、min/max RDT ratio、不同参数对 VRD 的影响，以及 guardband/ECC 对 bitflip 避免能力和系统性能的影响。

## 7. 主要结果
- 单次测量只能在 22.4% row 中得到 1000 次测量内的最小 RDT；见 Page 1-3, Figure 1。
- 最小 RDT 可能晚到第 94,467 次测量才出现；RDT=1000 的 row 测 94,467 次约 9.5 秒，但完整 bank 测试可能约 29 天；见 Page 5-6。
- 同一 row 的最小 RDT 可比最大观测 RDT 小 3.5x；见 Page 6-8。
- 97.1% row 在所有参数组合下表现出 VRD；见 Page 7-9。
- 10% guardband 与 SECDED/Chipkill-like SSC 可能缓解部分风险，但不能保证安全；较大 guardband 会带来明显性能开销，例如 50% guardband 性能损失约 45%；见 Page 14-16。

## 8. 关键结论
RowHammer 阈值不是一次测出来就固定不变的常数。任何依赖静态 profile 或单次 characterization 的防护都可能在 VRD 下不安全。未来系统需要持续测量、动态调整或采用能容忍阈值不确定性的防护。

## 9. 局限性
论文虽覆盖大量 DDR4 和少量 HBM2，但对 DDR5/LPDDR5、长期老化、多年尺度环境变化和真实 workload 诱发 VRD 的关系仍需研究。guardband/ECC 分析依赖模型和已有 ECC 假设。

## 10. 适合我重点关注的内容
重点读 Figure 1、Algorithm 1、VRD findings、guardband/ECC 分析，以及对现有 mitigation 的 implications。

## 11. 和其他文献的关系
本文直接挑战 Svärd 等 profile-based defense，也挑战 PRAC/Chronus 中固定 NRH 的配置假设。它与 HBM2 read disturbance 的空间变化形成互补：一个讲空间不稳定，一个讲时间不稳定。""",
        "key_points": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | VRD 表示同一 row 的 RDT 随时间变化 | Page 1 Abstract; Page 2, Figure 1 | RDT 序列显著波动 | 高 | 阈值不是固定常数 |
| 2 | 少数测量很可能错过真实最低 RDT | Page 2-5 | 单次测量只在 22.4% row 命中 1000 次内最低值 | 高 | 静态 profile 有安全风险 |
| 3 | 最低 RDT 可能非常晚才出现 | Page 5-6 | 最多 94,467 次测量后才观测到最低 RDT | 高 | 完整 profiling 成本巨大 |
| 4 | 同一 row min RDT 可比 max RDT 小 3.5x | Page 6-8 | min/max ratio 分析 | 高 | guardband 需要很大才稳健 |
| 5 | VRD 普遍存在 | Page 7-9 | 97.1% row 在所有参数组合下表现 VRD | 高 | 不是个别异常 row |
| 6 | data pattern、tAggON、温度、密度/工艺影响 VRD | Page 8-12 | 参数实验 | 中 | 与 RowPress 和技术缩放关联 |
| 7 | guardband + ECC 可缓解但不足以单独保证 | Page 14-16 | 10%/50% guardband 与 SECDED/SSC 分析 | 高 | 安全和性能之间有尖锐权衡 |
| 8 | 50% guardband 可造成约 45% 性能损失 | Page 15-16 | mitigation overhead 分析 | 高 | 单纯保守阈值不可持续 |
| 9 | 需要 online RDT profiling 与 runtime configurable mitigation | Page 16-17, Conclusion | 作者建议动态方案 | 高 | 未来防护方向 |
| 10 | 结果挑战 spatial-profile-based defense | Page 13-16 Implications | 静态 profile 可能过期或漏测 | 高 | 与 Svärd 必须结合阅读 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
以下为基于 PDF 提取文本的逐节中文详译/译述，覆盖全文主要内容。为避免未经授权的逐字全文翻译，本文采用忠实转述；关键术语和指标保留英文。

## Title
原文标题：Variable Read Disturbance: An Experimental Analysis of Temporal Variation in DRAM Read Disturbance

中文标题：可变读扰动：DRAM 读扰动时间变化的实验分析

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文提出 Variable Read Disturbance（VRD）：同一 DRAM row 的 read disturbance threshold 会随时间变化。作者在 160 颗 DDR4 和 4 颗 HBM2 芯片上反复测量 RDT，发现最低阈值可能在大量重复实验后才出现，且一次或少数几次 profile 很可能高估安全性。这一现象对 RowHammer 防护、guardband 和 ECC 都有重要影响。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 3

### 中文翻译
引言从 RowHammer 防护依赖阈值开始。大多数防护都需要知道某个安全阈值：在达到这个 activation count 前必须刷新、限速或采取保护。若阈值稳定，profile 可以在制造、启动或维护期间完成；若阈值随时间波动，系统就可能在实际运行中遇到比 profile 更弱的状态。

作者用 Figure 1 展示同一 row 的 RDT 序列：多次测量得到的阈值并不相同，最低值可能很晚才出现。这说明 RowHammer vulnerability 具有 temporal variation，而不仅是 chip-to-chip 或 row-to-row spatial variation。

## 2. Background and Definitions / 背景与定义

### 原文位置
Page 3 - Page 4

### 中文翻译
论文定义 RDT（Read Disturbance Threshold）为触发 read disturbance bitflip 所需访问/activation 数。RDT 越低，row 越脆弱。VRD 则指同一 row 在不同时间或重复测量中的 RDT 变化。

作者区分 spatial variation 与 temporal variation。前者表示不同位置 row 的差异；后者表示同一 row 的状态随时间变化。两者会叠加，使防护设计更复杂。

## 3. Methodology / 方法

### 原文位置
Page 4 - Page 6; Algorithm 1

### 中文翻译
实验方法是对同一 row 重复执行 read disturbance 测试，并记录每次触发第一个 bitflip 的 RDT。Algorithm 1 描述了重复测量过程：初始化数据 pattern，施加访问序列，检查 victim row，记录阈值，然后重复。

实验覆盖 160 颗 DDR4 和 4 颗 HBM2 芯片，来自 3 家厂商。作者改变 data pattern、tAggON、温度等参数，以观察 VRD 是否受这些条件影响。

## 4. Main Findings / 主要发现

### 原文位置
Page 6 - Page 12

### 中文翻译
第一项发现是，少量测量不足以发现最低 RDT。论文报告，在 1000 次测量范围内，单次测量只对 22.4% 的 row 命中最低 RDT。对某些 row，最低 RDT 需要数万次重复才出现；最高例子是第 94,467 次测量才观察到最低值。

第二项发现是，同一 row 的 RDT 波动幅度很大。最小 RDT 可比最大观测 RDT 小 3.5x。这意味着如果系统根据某次较高 RDT 设置阈值，实际运行中可能遇到远低于 profile 的危险状态。

第三项发现是，VRD 非常普遍。97.1% 测试 row 在所有参数组合下都表现出 VRD，其余 2.9% 至少在一个参数组合下表现出 VRD。这说明 VRD 不是少数异常样本，而是广泛存在的现象。

第四项发现是，VRD 与参数相关。data pattern、tAggON、温度和工艺/密度都会影响 RDT 分布。更先进或更高密度的芯片可能表现出更严重的变化趋势，这与 DRAM scaling 下 cell margin 缩小相一致。

## 5. Implications for Profiling and Mitigation / 对 profiling 与防护的启示

### 原文位置
Page 12 - Page 14

### 中文翻译
VRD 对 profile-based defense 构成挑战。若系统只做一次或少数几次测量，很可能错过真实最小 RDT。即使大规模 profiling，也可能因为测试时间和能耗过高而难以覆盖所有 row。

作者估算，对于 RDT=1000 的单个 row，94,467 次测量约需 9.5 秒；但若扩展到一个包含 256K row 的 bank，完整测试可能需要约 29 天。这说明制造或启动时完全 profile 所有 row 很难实际部署。

## 6. Guardband and ECC / Guardband 与 ECC

### 原文位置
Page 14 - Page 16

### 中文翻译
一个自然想法是使用 guardband，即把测得的 RDT 再降低一定比例作为防护阈值。论文分析表明，guardband 可以降低风险，但很难在安全和性能之间取得稳定平衡。10% guardband 结合 SECDED 或 Chipkill-like SSC 在某些场景可缓解问题，但不能保证所有情况安全。

更大的 guardband 会带来高性能成本。论文指出 50% guardband 可能造成约 45% 性能损失，而 10% guardband 的开销约 5.9%。因此，单纯依靠大 guardband 会让系统难以接受。

## 7. Discussion / 讨论

### 原文位置
Page 16 - Page 17

### 中文翻译
作者认为未来防护需要 online RDT profiling 和 runtime-configurable mitigation。系统应能在运行时观察或估计 vulnerability 变化，并动态调整 refresh、throttling 或 tracking 参数。

VRD 还说明，安全分析不能只依赖某个固定 NRH。对于 PRAC、Chronus、Svärd 或任何 profile-based defense，都需要考虑阈值随时间降低的可能性。

## 8. Conclusion / 结论

### 原文位置
Page 17

### 中文翻译
本文结论是：DRAM read disturbance threshold 会随时间显著变化，且这种现象广泛存在。少量 profiling 会高估安全性，完整 profiling 又成本极高。未来 DRAM 防护必须能处理 temporal variation，不能把 RDT/NRH 当作静态常数。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 1-2 | 同一 row 的 RDT 时间序列 | RDT 随重复测量变化，最低值可能晚出现 | 引出 VRD | 必读 |
| Figure 2-4 | Page 6-8 | RDT 分布与 min/max 差异 | 少量测量无法捕捉最低阈值 | 支撑核心发现 | 看分布尾部 |
| Figure 5-8 | Page 8-12 | 参数影响 | data pattern、tAggON、温度、工艺影响 VRD | 连接 RowPress/工艺缩放 | 关注趋势而非单点 |
| Figure 9+ | Page 14-16 | guardband/ECC 分析 | 大 guardband 成本高，小 guardband 不稳健 | 防护启示核心 | 对照性能开销 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 4-5 | 实验芯片/平台 | 160 DDR4 + 4 HBM2，3 厂商 | 判断覆盖范围 | 先看样本 |
| Appendix Tables | Appendix | 测试时间/能耗补充 | 完整 profiling 成本很高 | 支撑部署难度 | 有需要时回查 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Algorithm 1 | Page 5 | RDT 重复测量流程 | RDT、victim row、aggressor row、pattern | 通过重复实验观察 temporal variation | 是 |
| Guardband 计算 | Page 14-16 | 根据测得 RDT 设置更低保护阈值 | guardband percentage、profiled RDT | 用性能换安全余量 | 是 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Variable Read Disturbance (VRD) | 可变读扰动 | Page 1 | 同一 row 的 RDT 随时间变化 | 是 |
| Read Disturbance Threshold (RDT) | 读扰动阈值 | Page 3 | 触发 bitflip 所需 activation/access 数 | 是 |
| Temporal Variation | 时间变化 | Page 1-3 | 同一对象随时间的脆弱性变化 | 是 |
| Spatial Variation | 空间变化 | Page 2-3 | 不同位置 row 之间的差异 | 是 |
| Guardband | 安全裕量 | Page 14-16 | 在测得阈值基础上进一步保守设置 | 是 |
| SECDED | Single Error Correction, Double Error Detection | Page 14-16 | 常见 ECC 能力 | 中 |
| Chipkill-like SSC | 类 Chipkill 符号级纠错 | Page 14-16 | 更强 ECC 组织形式 | 中 |
| tAggON | aggressor row 开启时间 | Page 8-12 | RowPress 相关参数 | 是 |
| Online RDT Profiling | 在线 RDT 剖析 | Page 16-17 | 运行时更新阈值估计 | 是 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- 完整 profiling 时间和能耗成本极高；位置：Page 12-14, Appendix。
- guardband/ECC 不能单独提供普遍安全保证；位置：Page 14-16。

## 2. 论文中隐含的局限
- HBM2 样本只有 4 颗，DDR5/LPDDR5 未覆盖。
- VRD 的物理根因尚未完全解释，更多是实验表征。

## 3. 实验设计可能存在的问题
- 长时间重复测试本身是否改变 row 状态需要进一步隔离。
- 测试参数虽多，但仍不能覆盖所有真实 workload 行为。

## 4. 方法可能不适用的场景
- 如果系统无法执行在线 profiling，论文建议的动态策略难以落地。
- 对强 ECC 系统，VRD 的安全影响需要结合 ECC granularity 和 error accumulation 分析。

## 5. 我阅读时应该追问的问题
- VRD 的物理根因是噪声、温度、电荷历史、VRT-like 现象，还是多因素叠加？
- Svärd 的 spatial profile 如何加入 temporal uncertainty？
- PRAC/Chronus 应该如何设置动态 NRH？
- 在线 profiling 会不会本身诱发额外扰动或攻击面？

## 6. 后续可以继续阅读的方向
- Spatial Variation-Aware Defenses：对比空间和时间变化。
- RowPress：理解 tAggON 对 threshold 的影响。
- AVATAR/RAIDR/REAPER：DRAM retention 中也有时间变化与 profiling 问题，可类比理解。""",
        "log": """# Extraction Log

- Input Type: GitHub repository PDF
- Source: `paper reading/sources/LEC3/2502.13075v1.pdf`
- Access Status: 已下载并可读取
- Full Text Retrieved: Yes
- PDF Pages: 23
- Sections Detected: Abstract, Introduction, Background, Methodology, Findings, Implications, Guardband/ECC, Discussion, Conclusion, Appendix
- Figures Detected: Yes
- Tables Detected: Yes
- Equations Detected: Algorithm and guardband reasoning; no heavy mathematical derivation
- Appendix Detected: Yes
- Supplementary Material Detected: 未确认
- OCR Used: No
- Missing Content: 附录中部分长表未逐项转录
- Parsing Problems: 图表数值需回 PDF 精确核对
- Uncertain Parts: VRD 物理根因仍未完全确定
- Need User Action: 如需完整附录表格翻译，请指定优先页
- Quality Check: 已覆盖全文结构、核心发现、实验、guardband/ECC、局限和位置；逐节译述不是逐字全文翻译
- Batch Status: 第二轮深度阅读完成""",
    },
}


for slug, p in PAPERS.items():
    base = f"papers/{slug}"
    write(f"{base}/metadata.md", f"""# Paper Metadata

- Title: {p['title']}
- Chinese Title: {p['zh_title']}
- Authors: {p['authors']}
- Year: {p['year']}
- Venue / Journal / Conference: {p['venue']}
- DOI: 未找到
- arXiv ID: {slug if slug.startswith(('23','24','25')) else '未找到'}
- URL: {p['url']}
- PDF Source: `paper reading/sources/LEC3/{slug}.pdf`
- Code / Project Page: 见正文或 extraction_log，未确认则为未找到
- Dataset: 真实 DRAM/HBM 芯片实验与系统模拟 workload
- Main Topic: {p['topic']}
- Keywords: {p['keywords']}
- Reading Status: 第二轮深度阅读完成
- Full Text Available: Yes
- Notes: 已基于 PDF 提取文本完成深度中文阅读笔记；`full_translation.zh.md` 为版权友好的逐节中文详译/译述，不是逐字全文翻译。""")
    write(f"{base}/reading_summary.zh.md", p["summary"])
    write(f"{base}/key_points_with_locations.zh.md", p["key_points"])
    write(f"{base}/full_translation.zh.md", p["translation"])
    write(f"{base}/figures_tables_equations_notes.zh.md", p["figures"])
    write(f"{base}/terminology.zh.md", p["terms"])
    write(f"{base}/limitations_and_questions.zh.md", p["limitations"])
    write(f"{base}/extraction_log.md", p["log"])
