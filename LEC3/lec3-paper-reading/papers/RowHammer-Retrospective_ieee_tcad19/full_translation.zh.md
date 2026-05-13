# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 RowHammer Retrospective 的历史背景、物理机制、攻击谱系、防护机制、PARA、方法论启示和硬件工程师视角。保留 RowHammer、disturbance error、PARA、TRR、ECC、refresh、memory isolation 等术语。

## Title

原文标题：RowHammer: A Retrospective

中文标题：RowHammer：回顾

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

RowHammer 是现代 DRAM scaling 下出现的典型 disturbance error：反复激活某些 aggressor rows 会导致邻近 victim rows 出现 bit flips。更重要的是，RowHammer 证明器件级可靠性问题可以被软件有意触发，并破坏操作系统和虚拟化依赖的 memory isolation。

本文回顾 RowHammer 从原始发现到安全攻击、缓解机制和未来 memory security 方法论的演进。它把 RowHammer 放在更广泛的 memory scaling 背景中，说明未来还可能出现类似跨层安全问题。

## 1. Original RowHammer Observation / 原始 RowHammer 发现

### 原文位置

Page 1 - Page 3 / Figure 1

### 中文翻译

原始 RowHammer 研究测试 129 个 2008-2014 年 DRAM modules，其中 110 个出现 RowHammer errors。2012-2013 年模块全部 vulnerable，说明问题随工艺缩放而显著出现。

RowHammer 的关键特征是可重复、可由普通内存访问诱发。攻击者不需要物理访问 DRAM，只要能让 CPU 反复触发 DRAM row activations，就可能使邻近 victim rows bit flip。

这使 RowHammer 从 reliability bug 升级为 security vulnerability。传统系统假设一个进程无法修改另一个进程的物理内存；RowHammer 打破了这个假设。

## 2. Attacks / 攻击谱系

### 原文位置

Section III-A

### 中文翻译

Google Project Zero 2015 展示用户态程序可利用 RowHammer 获取 kernel privileges。随后研究扩展到 VM、mobile、JavaScript、RDMA/network、deduplication 等场景。

攻击通常需要三步：找到或塑造可 hammer 的 aggressor rows；使 victim row 中敏感 bit 位于可翻转位置；利用 bit flip 改变 page table、object pointer、credential 或其它安全关键数据。

攻击难点在于物理地址映射、cache bypass、memory allocation control 和 bit flip 可控性。随着研究推进，攻击者使用 eviction sets、huge pages、memory spraying、templating 和远程 DMA 等技术提高可利用性。

## 3. Defenses / 防护机制

### 原文位置

Sections II-E and III-B

### 中文翻译

短期防护包括提高 refresh rate、使用 ECC、row remapping、memory isolation、physical page allocation hardening、access counters 和 TRR。每类方案都有成本或覆盖限制。

提高 refresh rate 简单但增加能耗和性能开销。ECC 可纠正部分错误，但多 bit flips 或同一 ECC word 聚集可能超出能力。Row remapping 需要识别 weak rows。Access counters 更精确，但 storage 和 timing 成本高。

PARA（Probabilistic Adjacent Row Activation）是原始论文提出的重要方案。它在每次关闭 row 时，以很低概率刷新相邻 rows。只要概率选择合适，PARA 能以低性能开销大幅降低 bit flip 概率。论文提到 p=0.001 或 0.005 时可提供强保护且开销小于 0.75%。

## 4. Broader Methodology / 更广泛的方法论

### 原文位置

Section IV

### 中文翻译

本文强调 RowHammer 的最大教训不是某个补丁，而是 memory-system co-design 方法论。随着 memory scaling，电路级边界条件会继续变窄。可靠性、安全、体系结构、OS 和应用必须共同考虑。

作者主张更 principled 的方法：公开可分析的防护机制、跨层信息传递、可更新的 mitigation、真实芯片表征和安全攻击模型。黑盒厂商防护虽然能短期缓解，但难以证明安全。

## 5. 硬件工程师视角

RowHammer 是硬件工程师必须理解的安全可靠性案例。它说明“满足 JEDEC timing”不等于系统安全；“随机低概率 bit flip”也可能被 adversarial workload 放大。

对内存控制器：需要 tracking、refresh、throttling、telemetry 和 RAS integration。对 SoC/平台：需要 ECC、page retirement、AER/EDAC logging、firmware knobs。对验证：需要 attack-pattern validation，而不是只跑标准 memory test。

## 6. 不确定与需回原文核对

- 原始 129 modules 数据和 Figure 1 建议回 PDF；
- PARA 概率与性能开销需核对原表；
- 2019 后的新攻击和防护需要结合 RowPress、TRRespass、PRAC、Chronus、VRD 继续阅读。
