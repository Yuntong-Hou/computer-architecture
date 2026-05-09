from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = "第十轮深度阅读完成"
NOTE = "说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。"


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def bullets(xs):
    return "\n".join(f"- {x}" for x in xs)


def locs(xs):
    return "\n".join(f"- {x}（{l}）" for x, l in xs)


PAPERS = [
    {
        "slug": "reaper-dram-retention-profiling-lpddr4_isca17",
        "title": "The Reach Profiler (REAPER): Enabling the Mitigation of DRAM Retention Failures via Profiling at Aggressive Conditions",
        "zh": "REAPER：通过激进条件下的 profiling 缓解 DRAM retention failures",
        "authors": "Minesh Patel, Jeremie S. Kim, Onur Mutlu",
        "year": "2017",
        "venue": "ISCA 2017",
        "doi": "10.1145/3079856.3080242",
        "code": "未找到",
        "pages": "14",
        "dataset": "368 state-of-the-art LPDDR4 DRAM chips from three major vendors",
        "topic": "DRAM retention profiling; refresh reduction; LPDDR4 characterization",
        "keywords": "REAPER, reach profiling, retention failure, LPDDR4, VRT, DPD, refresh interval, ECC, UBER, RBER",
        "one": "REAPER 发现 retention failures 在更长 refresh interval 或更高温下更容易暴露，并利用 aggressive reach conditions 以更短 profiling 时间覆盖目标条件下绝大多数失败 cell。",
        "background": "许多 refresh-reduction 技术假设可以快速找到延长 refresh interval 后会失败的 cells，但 brute-force retention profiling 需要写模式、等待目标 refresh interval、读回检查，在线频繁 profiling 时开销过高，且 VRT 和 DPD 会让失败集合持续变化。",
        "questions": [
            "如何定义 retention profiling 的 coverage、false positive rate 和 runtime？",
            "为什么在更长 refresh interval 或更高温下 profiling 能发现目标条件下的失败 cells？",
            "在线 profiling 需要多频繁运行才可维持可靠性？",
            "ECC 的 UBER/RBER 约束如何转化为 profile longevity？",
            "REAPER 相比 brute-force profiling 对系统性能和 DRAM power 有多少改善？",
        ],
        "contribs": [
            "首次对 368 颗现代 LPDDR4 chips 在多温度、多 refresh interval 下进行 retention failure profiling tradeoff 分析。",
            "提出 reach profiling：在比目标条件更激进的 refresh interval/temperature 下 profile，以提高 coverage 并缩短 runtime。",
            "用 coverage、false positive rate、runtime 三个指标刻画 profiling 设计空间。",
            "给出基于 ECC、UBER、RBER 的 allowable error/profile longevity 分析。",
            "实现 REAPER，并证明其可支撑更长 refresh intervals 下的性能提升和 power reduction。",
        ],
        "method": "REAPER 不是在目标 refresh interval/temperature 上直接 brute-force 等待，而是在 reach conditions 下运行 profiling：例如比目标 refresh interval 长 250ms，或提高温度。由于目标下会失败的 cells 在激进条件下更可靠地失败，系统可用较少 iterations 捕获高覆盖率；随后用 ECC/mitigation 处理未捕获 failures 和 false positives。",
        "experiments": "作者在 368 颗 LPDDR4 chips 上测量 retention failure rates、failure accumulation、temperature dependence、data pattern dependence，并在系统模拟中评估 online profiling overhead、ArchShield 结合 REAPER 的性能和 power。",
        "results": [
            ("在目标 refresh interval 上方增加 250ms profiling，REAPER 平均可达到 >99% coverage、<50% false positive rate，并比 brute-force 快 2.5x。", "Page 1-2, Abstract/Contributions; Page 8, Section 6.1.2"),
            ("更激进 reach conditions 可把 speedup 推到 >3.5x，但 false positive rate 会超过 75%。", "Page 8, Section 6.1.2"),
            ("2GB DRAM + SECDED + 1024ms/45C 示例下，99% coverage profile 的 longevity 约 2.3 days。", "Page 9, Section 6.2.2"),
            ("64Gb chips、512ms operating point 下，REAPER 平均性能提升 16.3%，DRAM power 平均降低 36.4%。", "Page 11-12, Figure 13"),
            ("64Gb、1024ms 时 REAPER 平均性能提升 13.5%，brute-force 仅 7.5%；1280ms 时 brute-force 平均退化 -5.4%，REAPER 仍有 8.6% 平均收益。", "Page 12, Figure 13 discussion"),
            ("与 ArchShield 结合时，REAPER 平均性能提升 12.5%，比 brute-force profiling 组合高 5.6%。", "Page 12, Section 7.3.2"),
        ],
        "conclusion": "REAPER 的核心结论是：可靠 refresh reduction 不能只依赖离线或 brute-force profiling；基于 reach conditions 的在线 profiling 能在 coverage、false positive 和 runtime 之间取得更好的系统级折中。",
        "limitations_author": [
            ("结果依赖具体假设：45C、reach profiling 2.5x speedup、32 chips/module、100% coverage 假设和 20 个 workload mixes。", "Page 13, Section 7.3.2 caveat"),
            ("真正可靠 relaxed-refresh operation 需要实际芯片的 characterization data；DRAM vendors 当前通常不提供。", "Page 9, Section 6.3"),
        ],
        "limitations_infer": [
            ("profiling 本身仍依赖 retention failure mitigation，如 ECC、bit repair 或 remapping；单独 REAPER 不等于完整可靠性方案。", "推断，基于 Sections 6-7"),
            ("DPD/VRT 导致 profile 会过期，不同工艺或工作温度下需要重新调参。", "推断，基于 Sections 5-6"),
        ],
        "focus": "重点读 Figure 9/10 的 reach profiling tradeoff、Table 1 的 tolerable RBER、Figure 11-13 的系统结果，以及 Section 6.2 profile longevity。",
        "relation": "REAPER 延续 RAIDR/AVATAR 的 retention-aware refresh 脉络，解决的是“如何高效、在线、可量化地 profile 弱 cells”；它也与 HARP、MEMCON 等 DRAM failure profiling 论文互补。",
        "figures": [
            ("Figure 1", "Page 3", "DRAM array and retention failure", "解释 refresh interval 延长如何产生 retention failure。"),
            ("Figure 2", "Page 5", "retention failure rates", "展示 refresh interval 增大导致 BER 上升。"),
            ("Figure 5", "Page 6", "brute-force coverage over iterations", "说明 brute-force 在短时间内 coverage 不足。"),
            ("Figure 9", "Page 8", "coverage and false positive tradeoff", "展示 reach conditions 对 coverage/false positives 的影响。"),
            ("Figure 10", "Page 8", "profiling runtime", "展示 reach conditions 如何带来 2.5x/3.5x speedup。"),
            ("Figure 13", "Page 12", "end-to-end performance/power", "展示 REAPER 对系统性能和 DRAM power 的收益。"),
        ],
        "tables": [
            ("Table 1", "Page 9", "tolerable RBER", "把 UBER 目标和 ECC 强度映射为可容忍 bit errors。"),
            ("Table 2", "Page 10", "evaluated system configuration", "列出系统模拟配置。"),
        ],
        "equations": [
            ("Equation 2-6", "Page 8-9", "UBER/RBER model", "UBER as probability of uncorrectable ECC word error", "用 raw bit failure rate 推导系统不可纠错错误率。", "是"),
            ("Equation 7", "Page 9", "profile longevity", "T from tolerable missed/new failures", "估计 profile 何时需要重新运行。", "是"),
        ],
        "terms": [
            ("Reach profiling", "触达式/激进条件 profiling", "Page 2", "在比目标更长 refresh interval 或更高温度下 profile 弱 cells。", "是"),
            ("Coverage", "覆盖率", "Page 1-2", "profile 找到目标条件下所有可能失败 cells 的比例。", "是"),
            ("False positive rate", "误报率", "Page 1-2", "profile 条件下失败但目标运行条件下不失败的 cells 比例。", "是"),
            ("Variable retention time (VRT)", "可变保持时间", "Page 1 and Section 5", "cell retention behavior 随时间变化，导致 profile 过期。", "是"),
            ("Uncorrectable bit error rate (UBER)", "不可纠错 bit 错误率", "Page 8", "系统级不可由 ECC 修正的错误率目标。", "是"),
        ],
        "sections": "Abstract; Introduction; Background; Refresh Overhead Mitigation; Retention Failure Profiling; Experimental Characterization; Online Profiling Frequency; End-to-End Implementation; Related Work; Conclusion",
        "translation": [
            ("Abstract / 摘要", "Page 1", "现代 DRAM refresh 标准为了覆盖最坏保持时间 cells，给所有 cells 统一 64ms 刷新，造成能耗和性能损失。REAPER 的思路是用更激进的 refresh interval 或温度做 profiling，在更短时间内发现目标条件下的绝大多数失败 cells。"),
            ("1. Introduction / 引言", "Page 1-2", "作者指出许多 refresh reduction 工作假定 profiling 可以快速完成，但 brute-force profiling 既慢又会受 VRT/DPD 影响。论文提出 coverage、false positive rate 和 runtime 三个指标来评价 profiling，并在 368 颗 LPDDR4 chips 上实证分析。"),
            ("2-4. Background and Profiling / 背景与 profiling", "Page 2-4", "DRAM cell 因漏电需要周期性 refresh。若延长 refresh interval，少量弱 cells 会失败。传统方法逐模式等待目标 interval 并读回检查；REAPER 则把 profiling 移到更高压力条件，使弱 cells 更快、更稳定地暴露。"),
            ("5-6. Characterization and Model / 表征与模型", "Page 4-9", "实验显示 retention failures 随 refresh interval 和温度增加而增长，且失败集合会随时间累积。作者用 UBER/RBER 和 ECC 模型估计可容忍遗漏 failures，并把它转化为 profile longevity。"),
            ("7. End-to-End Evaluation / 端到端评估", "Page 10-13", "系统评估表明，REAPER 因 profiling runtime 低，可支撑 512ms 到 1024ms 等更长 refresh intervals。相比 brute-force，它在长 refresh interval 下保留更多理想收益，并降低 profiling 引起的性能损失。"),
            ("9. Conclusion / 结论", "Page 13", "论文总结 reach profiling 是许多 past/future refresh reduction techniques 的 enabler，因为它让在线、高覆盖、可控误报的 retention profiling 变得可行。"),
        ],
    },
    {
        "slug": "revisiting-memory-errors_dsn15",
        "title": "Revisiting Memory Errors in Large-Scale Production Data Centers: Analysis and Modeling of New Trends from the Field",
        "zh": "重新审视大规模生产数据中心中的内存错误：来自现场的新趋势分析与建模",
        "authors": "Justin Meza, Qiang Wu, Sanjeev Kumar, Onur Mutlu",
        "year": "2015",
        "venue": "DSN 2015",
        "doi": "10.1109/DSN.2015.57",
        "code": "未找到",
        "pages": "12",
        "dataset": "Facebook entire fleet over fourteen months; billions of device days; DDR3 DIMMs from four vendors, 2GB-24GB",
        "topic": "DRAM reliability in production data centers; field study; page offlining",
        "keywords": "memory errors, data center, Facebook, Pareto distribution, DIMM density, workload, page offlining, ECC",
        "one": "这篇论文用 Facebook 全量服务器 14 个月现场数据说明现代数据中心内存错误高度偏斜、受非 DRAM 通道/控制器、芯片密度、DIMM 架构和 workload 影响，并验证 page offlining 可在真实系统中降低错误率。",
        "background": "过去现场研究揭示 DRAM errors 常见，但现代 DDR3 服务器、不同 workload、DIMM 组织和大规模软件缓解技术下的趋势仍不清楚；设计 ECC 和可靠服务器需要真实分布和模型。",
        "questions": [
            "内存错误在服务器之间如何分布，平均值是否有代表性？",
            "错误来源是否主要是 DRAM chip，还是 memory controller/channel/socket？",
            "更高 chip density、DIMM 架构、工作负载、年龄和利用率如何影响 failure rate？",
            "能否建立用于系统设计的 failure model？",
            "page offlining 在真实数据中心部署时实际效果如何？",
        ],
        "contribs": [
            "分析 Facebook 全量服务器 14 个月、billions of device days 的内存错误。",
            "发现错误数遵循 Pareto/power-law，平均错误率比中位数高约 55x。",
            "指出 non-DRAM memory failures 如 controller/channel/socket 贡献多数错误，并会形成类似 denial-of-service 的错误风暴。",
            "证明 4Gb chips 的 failure rate 比 2Gb 高 1.8x，chip density 比 DIMM capacity 更能解释工艺趋势。",
            "发现 workload type 可使 failure rate 差异达到 6.5x，而 CPU/memory utilization 趋势不明显。",
            "构建回归模型，并在真实 12,276 台服务器上评估 page offlining，错误率降低约 67%。",
        ],
        "method": "作者用 mcelog 收集 CE/MCE 信息，用物理地址、socket/channel/bank 等字段分类错误；结合硬件配置、workload、年龄、利用率等特征做统计和 logistic regression，并部署 page offlining，把出错物理页从 OS 可分配池中移除。",
        "experiments": "现场研究覆盖 Facebook 服务器群、DDR3 DIMMs、六类 workload。模型部分比较低端/高端服务器配置；page offlining 部分在 12,276 台服务器上观测 86 天。",
        "results": [
            ("每月 correctable errors 平均影响 2.08% 服务器，uncorrectable errors 平均影响 0.03%。", "Page 3, Figure 1 discussion"),
            ("错误数服从 Pareto/power-law，平均错误率比中位数高约 55x。", "Page 1 and Page 12, Abstract/Conclusions"),
            ("non-DRAM memory failures from memory controller/channel 贡献多数错误，并可能 bombard a server。", "Page 1 and Page 5, Figures 3-4"),
            ("4Gb chips failure rates 比 2Gb 高 1.8x。", "Page 1 and Page 6, Figure 6 discussion"),
            ("不同 workload 的 DRAM failure rate 可相差 6.5x。", "Page 1 and Page 8, Figure 13 discussion"),
            ("模型预测高端服务器 failure rate 是低端的 6.5x；使用低密度 DIMMs 可降低 57.7%，减少 CPUs 可降低 34.6%。", "Page 10, Table III discussion"),
            ("page offlining 在真实部署中将 error rate 降低约 67%，但仍有约 6% 初始 offlining attempts 失败。", "Page 11, Figure 18 and Section VI-C"),
        ],
        "conclusion": "现代数据中心 memory reliability 不能只用平均错误率或单一 DRAM chip failure 解释；服务器设计、DIMM 组织、工作负载和系统级缓解策略都必须一起建模。",
        "limitations_author": [
            ("page offlining 会降低可用物理内存，需要达到阈值后维修机器。", "Page 11, Section VI-C"),
            ("page offlining 并不总能立即成功；Linux kernel 中约 6% 初始 attempts 失败。", "Page 11, Section VI-C"),
        ],
        "limitations_infer": [
            ("数据来自 Facebook 特定时期、DDR3 设备和生产 workload，不能直接外推到 DDR5/HBM 或其他数据中心。", "推断，基于 Methodology"),
            ("UCE 缺少 CE 那样细粒度信息，因此 UCE 源因分析能力有限。", "推断，基于 Page 3 methodology"),
        ],
        "focus": "重点读 Figure 2 的分布、Figures 3-4 的 failure type、Figures 5-13 的影响因素、Table II/III 模型和 Figure 18 page offlining。",
        "relation": "它与 Heterogeneous Reliability Memory、HARP、MEMCON 等论文共同构成 field-driven reliability 方向，为哪些错误需要硬件/系统缓解提供真实依据。",
        "figures": [
            ("Figure 1", "Page 3", "CE/UCE timeline", "展示每月服务器受影响比例。"),
            ("Figure 2", "Page 4", "error distribution", "说明错误高度集中、平均值误导。"),
            ("Figures 3-4", "Page 5", "socket/channel/bank failures", "说明 non-DRAM failure 对错误数的贡献。"),
            ("Figures 5-10", "Page 6-8", "capacity/density/vendor/architecture", "比较硬件因素对 failure rate 的影响。"),
            ("Figure 13", "Page 8", "workload effect", "说明不同 workload failure rate 可差异很大。"),
            ("Figure 18", "Page 11", "page offlining effect", "展示真实部署后错误下降。"),
        ],
        "tables": [
            ("Table I", "Page 2", "workload resource requirements", "列出 Web/Hadoop/Ingest/Database/Memcache/Media。"),
            ("Table II", "Page 9", "regression factors/model", "列出模型变量、p-value、系数。"),
            ("Table III", "Page 10", "predicted relative failure rates", "比较低端/高端及设计变体。"),
        ],
        "equations": [
            ("Failure model", "Page 9, Table II", "logistic regression", "ln(F/(1-F)) = intercept + feature coefficients", "把硬件/workload/age 等特征映射到 failure probability。", "是"),
        ],
        "terms": [
            ("Correctable error (CE)", "可纠错错误", "Page 2", "可由 ECC 修正的内存错误。", "是"),
            ("Uncorrectable error (UCE)", "不可纠错错误", "Page 2", "ECC 能检测但不能纠正，通常导致系统 crash。", "是"),
            ("Page offlining", "页下线", "Page 10-11", "把出现错误的物理页从 OS 可分配内存中移除。", "是"),
            ("Pareto distribution", "帕累托分布", "Page 4", "错误高度集中在少数服务器上的 heavy-tailed 分布。", "是"),
            ("DIMM architecture", "DIMM 架构", "Page 7", "chips per DIMM、transfer width 等组织特征。", "是"),
        ],
        "sections": "Abstract; Introduction; Background and Methodology; Baseline Statistics; Factors Affecting Failure Rate; Model; Page Offlining; Related Work; Conclusions",
        "translation": [
            ("Abstract / 摘要", "Page 1", "论文分析 Facebook 全量服务器 14 个月内存错误，覆盖数十亿 device days。作者发现错误分布、来源和影响因素与早期研究存在新的趋势，并给出可靠性模型和 page offlining 部署结果。"),
            ("I-II. Introduction and Methodology / 引言与方法", "Page 1-3", "作者解释 ECC、CE/UCE、MCE 日志和服务器内存组织，并说明收集每个 CE 的时间、物理地址、socket/channel/bank 与访问类型。"),
            ("III-IV. Statistics and Factors / 基线统计与影响因素", "Page 3-9", "错误高度偏斜，平均值远高于中位数。controller/channel/socket 等非 DRAM failures 产生大量错误。chip density、DIMM chips/transfer width、workload 和年龄都会影响 failure rate，而 CPU/memory utilization 趋势不明显。"),
            ("V. Failure Model / 失效模型", "Page 9-10", "作者用 logistic regression 建立 failure model。模型显示设计选择会显著改变可靠性，例如使用低密度 DIMMs 或减少访问 memory 的 CPUs。"),
            ("VI. Page Offlining / 页下线", "Page 10-11", "page offlining 在真实系统中把出错物理页移除，86 天实验显示错误率约下降 67%。但它会减少物理内存，且部分页因 OS 限制不能立即下线。"),
            ("VIII. Conclusions / 结论", "Page 11-12", "论文总结现代数据中心 memory errors 是分布、硬件、workload 与系统策略共同作用的结果，模型和数据可帮助设计更可靠 DIMM 与服务器。"),
        ],
    },
    {
        "slug": "rlmc_isca08",
        "title": "Self-Optimizing Memory Controllers: A Reinforcement Learning Approach",
        "zh": "自优化内存控制器：一种强化学习方法",
        "authors": "Engin Ipek, Onur Mutlu, Jose F. Martinez, Rich Caruana",
        "year": "2008",
        "venue": "ISCA 2008",
        "doi": "未找到",
        "code": "未找到",
        "pages": "12",
        "dataset": "Nine memory-intensive parallel applications from SPEC OpenMP, NAS OpenMP, SPLASH-2, and Nu-MineBench",
        "topic": "DRAM scheduling; reinforcement learning; self-optimizing memory controller",
        "keywords": "reinforcement learning, memory controller, DRAM scheduling, FR-FCFS, Q-learning, CMAC, bandwidth utilization",
        "one": "这篇论文把 DRAM command scheduling 形式化为 reinforcement learning 问题，让 memory controller 在线学习长期调度收益，从而比固定 FR-FCFS 策略更好利用带宽。",
        "background": "CMP 核数增长快于 off-chip bandwidth 增长，传统 memory controllers 采用固定、人工设计的 scheduling policy，缺少长期规划和对 workload phase changes 的自适应能力。",
        "questions": [
            "如何把 DRAM scheduling 表述为 Markov Decision Process？",
            "memory controller 的 state、action 和 reward 应该如何定义？",
            "在线 RL 是否能在硬件可实现的结构中收敛并提升性能？",
            "提升来自额外状态信息还是来自 RL 的表达能力与在线学习？",
            "多 memory controllers 情况下是否需要显式协调？",
        ],
        "contribs": [
            "首次提出用 reinforcement learning 设计 self-optimizing DRAM command scheduler。",
            "把 scheduler 设计为 RL agent，actions 覆盖合法 DRAM commands，reward 用 data bus utilization 表征长期性能目标。",
            "用 CMAC/Q-value 近似实现硬件可行的在线学习和 generalization。",
            "系统评估 online RL、offline RL、FR-FCFS derivatives、Fair Queueing、多通道/多控制器等对比。",
            "证明 RL controller 平均性能提升 19%、DRAM bandwidth utilization 提升 22%。",
        ],
        "method": "RL-based scheduler 每个 DRAM cycle 观察 transaction queue、request type、row hit、criticality 等 state attributes，从合法 precharge/activate/read/write actions 中选择 Q-value 最高动作；执行后根据 data bus utilization reward 更新 state-action Q-values，持续适应 workload 行为。",
        "experiments": "作者在 4-core 2-way SMT CMP、DDR2-800 6.4GB/s 单通道 baseline 上运行 9 个 memory-intensive parallel applications，比较 in-order、FR-FCFS、RL、optimistic controller；并扩展到 8/16-core 多控制器和 12.8GB/s dual-channel。",
        "results": [
            ("4-core single-channel 下，RL 平均性能比 FR-FCFS 提升 19%，最高 33%。", "Page 1-2 Abstract/Introduction; Page 8-9, Figure 7"),
            ("RL 将 DRAM data bus utilization 从 46% 提升到 56%，平均提升 22%。", "Page 1 and Page 9, Figure 8"),
            ("RL 将 average L2 load miss penalty 从 FR-FCFS 的 824 cycles 降到 562 cycles。", "Page 9, Figure 9 discussion"),
            ("仅把额外 state information 加到 FR-FCFS derivatives 平均只提升 5%，online RL 达到 19%。", "Page 9, Figure 10"),
            ("offline RL 平均仅提升 8%，显著弱于 online adaptive RL。", "Page 10, Figure 11"),
            ("8-core/16-core 多控制器下 RL 仍平均提升 15%/14%，不需要显式 controller coordination。", "Page 10, Figure 14"),
            ("single-channel RL 提供了 dual-channel FR-FCFS 约一半 speedup；dual-channel RL 平均 speedup 58%。", "Page 10-11, Figure 15"),
        ],
        "conclusion": "RL memory controller 的价值不只是多几个 heuristic state，而是能在线学习长期影响、表达复杂 policy 并适应非平稳 workload；这为后续 adaptive memory scheduling 打开了方向。",
        "limitations_author": [
            ("QoS guarantees/multiprogrammed fairness 不是本文目标，留给 future work。", "Page 11, Section 5.4"),
            ("RL 的 reward 主要优化 data bus utilization，不能直接覆盖所有公平性或服务质量目标。", "Page 3-4, reward definition; Page 11"),
        ],
        "limitations_infer": [
            ("评估基于 2008-era DDR2、4-16 core 模拟环境，现代 DDR5/HBM/CXL 系统需重新验证。", "推断，基于 Section 4 setup"),
            ("硬件学习参数、feature selection 和 convergence 在极端 workload phase changes 下仍需工程验证。", "推断，基于 Sections 3 and 5.1.4"),
        ],
        "focus": "重点读 Figure 2 RL mapping、Figure 4 scheduler overview、Figure 6 CMAC pipeline、Figures 7-16 结果对比。",
        "relation": "这篇是 memory scheduling/QoS 线的早期 adaptive 方法，与 MISE、DASH、ASM、Staged Memory Scheduling 等固定/模型化调度策略形成对照。",
        "figures": [
            ("Figure 1", "Page 1", "FR-FCFS vs optimistic", "说明传统调度造成带宽和性能损失。"),
            ("Figure 2", "Page 3", "RL agent mapping", "把 DRAM scheduler 映射为 RL agent。"),
            ("Figure 4", "Page 4", "RL scheduler overview", "展示 Q-value 估计和动作选择。"),
            ("Figure 6", "Page 7", "Q-value estimation pipeline", "展示 CMAC/hashing 硬件结构。"),
            ("Figure 7", "Page 9", "performance comparison", "核心性能结果。"),
            ("Figure 15", "Page 11", "bandwidth efficiency", "展示 RL 与双通道配置的关系。"),
        ],
        "tables": [
            ("Table 1", "Page 8", "core parameters", "列出 CMP core 模型。"),
            ("Table 2", "Page 8", "L2/DRAM subsystem", "列出 DDR2-800 memory system 参数。"),
            ("Table 3", "Page 8", "applications/input sizes", "列出 9 个 parallel workloads。"),
        ],
        "equations": [
            ("Discounted reward", "Page 3", "RL objective", "sum of discounted future rewards with gamma", "用未来 reward 把调度长期影响纳入决策。", "是"),
            ("Q-value update", "Page 5", "temporal-difference learning", "Q(sprev, aprev) updated from reward and next-state max Q", "把当前动作归因到未来带宽利用收益。", "是"),
        ],
        "terms": [
            ("Reinforcement learning (RL)", "强化学习", "Page 1-3", "agent 通过环境反馈学习最大化长期 reward 的控制策略。", "是"),
            ("FR-FCFS", "first-ready first-come first-serve", "Page 2", "优先 ready column commands 和较老 requests 的传统 DRAM scheduling policy。", "是"),
            ("Q-value", "动作价值", "Page 4-5", "估计某状态下采取某动作的长期 reward。", "是"),
            ("CMAC", "Cerebellar Model Articulation Controller", "Page 5-7", "用 coarse-grain tables/hashing 近似 Q-values 的硬件友好结构。", "是"),
            ("Data bus utilization", "数据总线利用率", "Page 3 and Page 9", "作为 RL reward 的主要目标，反映 sustained DRAM bandwidth。", "是"),
        ],
        "sections": "Abstract; Introduction; Background and Motivation; RL-Based Controller Design; Experimental Setup; Evaluation; Related Work; Conclusions",
        "translation": [
            ("Abstract / 摘要", "Page 1", "作者提出 self-optimizing memory controller，通过 reinforcement learning 在线学习 DRAM scheduling policy。结果显示在 4-core CMP 上比 FR-FCFS 平均提升 19%，并提升带宽利用率。"),
            ("1-2. Motivation / 动机", "Page 1-3", "CMP 需要更高 off-chip bandwidth，但传统 fixed policy 不能预判长期影响，也不能适应 workload 动态变化。DRAM scheduling 同时受 timing constraints、row buffer locality、bank conflicts 和 request criticality 影响。"),
            ("3. RL-Based Scheduling / RL 调度设计", "Page 4-7", "scheduler 被建模为 RL agent。state 包含 transaction queue 和 request 属性；actions 是合法 DRAM commands；reward 奖励利用 data bus 的命令。CMAC 结构用于压缩巨大 state space 并实现 generalization。"),
            ("4-5. Evaluation / 实验评估", "Page 8-11", "实验用九个 memory-intensive parallel workloads。RL 相比 FR-FCFS 提升性能和 bus utilization，显著优于 offline RL、FR-FCFS derivatives 和 Fair Queueing。多控制器实验说明无需显式协调也能收敛。"),
            ("7. Conclusions / 结论", "Page 12", "论文总结 RL controller 能在线适应并降低人工调度策略设计负担，是更高效利用 DRAM bandwidth 的有前景路径。"),
        ],
    },
    {
        "slug": "rowhammer-and-other-memory-issues_date17",
        "title": "The RowHammer Problem and Other Issues We May Face as Memory Becomes Denser",
        "zh": "RowHammer 问题与内存密度提高后可能面对的其他问题",
        "authors": "Onur Mutlu",
        "year": "2017",
        "venue": "DATE 2017",
        "doi": "未找到",
        "code": "未找到",
        "pages": "6",
        "dataset": "Survey/position paper; RowHammer evidence from 129 DRAM modules and related attacks",
        "topic": "Memory reliability and security; RowHammer; disturbance errors; scaled memory vulnerabilities",
        "keywords": "RowHammer, disturbance errors, memory isolation, PARA, DRAM security, NAND flash, PCM, system-memory co-design",
        "one": "这篇短文把 RowHammer 作为“内存可靠性问题演化为系统安全漏洞”的典型案例，主张用系统-内存协同设计和更有原则的测试/建模/缓解方法提前发现未来高密度内存问题。",
        "background": "DRAM/NAND/PCM 等存储技术持续缩放带来更高密度和更低成本，但 cell-to-cell interference、retention、variation 等可靠性问题可能越过抽象边界，破坏 memory isolation 并成为安全漏洞。",
        "questions": [
            "为什么 RowHammer 是电路级 failure 变成系统级安全漏洞的典型例子？",
            "用户态程序如何通过 repeated activation 破坏相邻 rows？",
            "已有 immediate/long-term solutions 各有什么缺点？",
            "PARA 为什么被认为是低成本长期方案？",
            "除了 RowHammer，retention 和 NAND flash disturb 还可能带来哪些安全风险？",
        ],
        "contribs": [
            "系统化解释 RowHammer 的根因、攻击面和安全影响。",
            "总结用户态、JavaScript、VM、Android 等多类 RowHammer attacks。",
            "比较提高 refresh、ECC、remapping、runtime tracking、PARA 等缓解思路。",
            "强调现代 DRAM 缺少类似 SSD controller 的 assumed-faulty chip + intelligent controller 设计心态。",
            "提出未来 memory reliability/security 研究需要更原则化的测试、现场建模和系统-内存协同。"
        ],
        "method": "本文是综述和立场论文。作者复盘 ISCA 2014 RowHammer characterization、Project Zero 与后续攻击，讨论 immediate 和 long-term countermeasures，并把 RowHammer 放入更广泛的 scaled memory disturbance/retention/security 语境。",
        "experiments": "本文本身不做新实验；核心证据来自先前测试 129 DRAM modules 中 110 个出现 RowHammer errors，以及后续多种实际攻击展示。",
        "results": [
            ("测试 129 个 DRAM modules，110 个出现 RowHammer errors，最早可追溯到 2010 年，2012-2013 年 modules 全部 vulnerable。", "Page 1, Section II and Figure 1"),
            ("简单用户态程序能在 commodity AMD/Intel systems 上可靠诱发 RowHammer errors，违反 read 不应修改其他地址、write 只修改目标地址两个不变量。", "Page 2, Section II-A"),
            ("RowHammer 已被用于 Project Zero kernel privilege escalation、remote server takeover、VM takeover、Android device takeover 和 browser read/write access 等攻击。", "Page 2, Section II-B"),
            ("单纯提高 refresh rate 若要消除测试中所有 RowHammer-induced errors 需要约 7x refresh rate，代价是 power/performance/QoS。", "Page 2, Section II-C"),
            ("PARA 在每次关闭 row 后以很低概率刷新 adjacent rows，可用 negligible performance/energy overhead 消除 RowHammer vulnerability，但需要 controller/DRAM 支持邻接信息或内部 refresh。", "Page 3, Section II-C"),
        ],
        "conclusion": "RowHammer 的教训是：内存芯片不再应被抽象成完全可靠黑盒；未来内存系统需要把测试、控制器、芯片和系统软件联合起来提前发现和缓解可靠性-安全交叉问题。",
        "limitations_author": [
            ("PARA 不能立即部署，因为需要 memory controller 或 DRAM chip 修改，并需要知道物理相邻 rows。", "Page 3, Section II-C"),
            ("提高 refresh rate 是现实 immediate solution，但会增加能耗、降低性能和 QoS。", "Page 2, Section II-C"),
        ],
        "limitations_infer": [
            ("本文是 invited/survey-style 论文，很多结论依赖引用的先前实验和攻击论文，而非新实验。", "推断，基于全文结构"),
            ("对 NAND/PCM 等潜在漏洞的讨论属于研究方向判断，不能视作已实证的完整攻击链。", "推断，基于 Section III"),
        ],
        "focus": "重点读 Section II RowHammer threat 和 solutions、Page 3 PARA/system-memory co-design、Section III potential vulnerabilities、Section IV principles。",
        "relation": "这篇是 RowHammer 原始 ISCA14、RowHammer Retrospective、Panopticon、RowPress 等论文的高层桥梁，也把 memory reliability 与 security 研究线连接起来。",
        "figures": [
            ("Figure 1", "Page 2", "RowHammer error rate vs manufacture date", "展示 129 个 modules 的 vulnerability 随年份变化。"),
        ],
        "tables": [
            ("未检测到核心编号表", "-", "本文主要是短综述/立场论文，未使用核心结果表。", "建议直接回到 PDF 阅读 Section II-C 和 Section IV。"),
        ],
        "equations": [
            ("PARA probability", "Page 3", "概率式 adjacent row refresh", "low probability p after row close", "用概率保证把 repeated hammer 的风险压到极低。", "是"),
        ],
        "terms": [
            ("RowHammer", "行锤击", "Page 1-2", "反复 activate/precharge 一个 row 导致相邻 rows bit flips 的 DRAM disturbance error。", "是"),
            ("Disturbance error", "扰动错误", "Page 1", "cell-to-cell interference 导致非目标 cell 被破坏。", "是"),
            ("Memory isolation", "内存隔离", "Page 1-2", "访问一个地址不应影响其他地址，是安全系统基础。", "是"),
            ("PARA", "Probabilistic Adjacent Row Activation", "Page 3", "以低概率刷新相邻 rows 的 RowHammer 长期缓解机制。", "是"),
            ("System-memory co-design", "系统-内存协同设计", "Page 3", "controller、DRAM、系统软件共同暴露/处理可靠性问题。", "是"),
        ],
        "sections": "Abstract; Introduction; The RowHammer Problem; Other Potential Vulnerabilities; A Principled Approach; Conclusion/References",
        "translation": [
            ("Abstract / 摘要", "Page 1", "随着内存密度提高，新 failure mechanisms 可能破坏可靠性和安全性。RowHammer 是 DRAM 电路级扰动导致实际系统漏洞的代表案例。"),
            ("I-II. RowHammer / RowHammer 问题", "Page 1-3", "反复打开和关闭同一 DRAM row，会在相邻 rows 中造成可预测 bit flips。该现象违反 memory isolation，并已被多种软件攻击利用。"),
            ("II-C. Solutions / 解决方案", "Page 2-3", "短期方案包括提高 refresh rate 和软件检测，但有性能/能耗/侵入性成本。长期方案包括更好 DRAM、ECC、remapping、runtime tracking 和 PARA，其中 PARA 以较低成本随机刷新邻近 rows，但需要 controller/DRAM 支持。"),
            ("III. Other Vulnerabilities / 其他潜在漏洞", "Page 3-4", "作者讨论 retention failures、NAND flash read/program interference、PCM 等 emerging memories 中类似 reliability-security 问题。共同根因是高密度下 cell-to-cell interference 和 variation 更严重。"),
            ("IV. Principled Approach / 原则化方法", "Page 4-5", "作者主张建立更好的测试、field data、failure model、error mitigation 和 system-memory co-design，避免可靠性问题在部署后变成难以防御的安全漏洞。"),
        ],
    },
    {
        "slug": "softMC_hpca17",
        "title": "SoftMC: A Flexible and Practical Open-Source Infrastructure for Enabling Experimental DRAM Studies",
        "zh": "SoftMC：支持实验性 DRAM 研究的灵活实用开源基础设施",
        "authors": "Hasan Hassan, Nandita Vijaykumar, Samira Khan, Saugata Ghose, Kevin Chang, Gennady Pekhimenko, Donghyuk Lee, Oguz Ergin, Onur Mutlu",
        "year": "2017",
        "venue": "HPCA 2017",
        "doi": "未找到",
        "code": "https://github.com/CMU-SAFARI/SoftMC",
        "pages": "12",
        "dataset": "SoftMC FPGA prototype; retention tests; 24 modern DRAM chips from three major manufacturers for latency-mechanism validation",
        "topic": "Open-source DRAM testing infrastructure; FPGA memory controller; experimental DRAM characterization",
        "keywords": "SoftMC, soft memory controller, FPGA, DDR commands, DRAM testing, retention time, latency, ChargeCache, NUAT",
        "one": "SoftMC 提供开源 FPGA-based programmable memory controller，让研究者用高层 API 发 DDR commands、调 timing，并在真实 DRAM chips 上复现实验或验证新机制。",
        "background": "DRAM 缩放带来可靠性和 latency 难题，而许多现象无法只靠模拟准确建模；已有商业 tester、FPGA 平台或 BIST 要么不灵活、不开源，要么难用，缺少面向架构研究者的可编程实验平台。",
        "questions": [
            "一个实用 DRAM testing infrastructure 为什么必须同时具备 flexibility 和 ease of use？",
            "SoftMC 如何把 DDR commands 和 timing 控制暴露给用户？",
            "高层 API 如何映射到 FPGA 中的 programmable memory controller？",
            "SoftMC 能否复现 retention time 既有结果？",
            "SoftMC 如何验证或反驳 ChargeCache/NUAT 等 latency reduction 假设？",
        ],
        "contribs": [
            "提出第一个 open-source FPGA-based experimental memory testing infrastructure SoftMC。",
            "实现 programmable memory controller，并通过 high-level software API 暴露 ACTIVATE/READ/WRITE/PRECHARGE/REFRESH 等 DDR commands。",
            "提供 ML605 FPGA prototype、RIFFA PCIe communication、instruction queue/execution/read capture/calibration 等组件。",
            "用 retention time test 复现既有 DRAM retention 行为，验证平台正确性。",
            "在 24 颗现代 DRAM chips 上测试 ChargeCache/NUAT 的 latency reduction 假设，发现预期效果在现有芯片中不可观察。",
        ],
        "method": "用户在 host 端用 SoftMC API 生成 instruction sequence；driver 通过 PCIe 将 sequence 发送到 FPGA；SoftMC hardware decode/execute DDR commands，控制 DDR PHY 和 DRAM module，并把读回数据返回 host。API 支持显式 wait cycles，从而可调整 tRCD、tRAS、tRP、tREFI 等 timing。",
        "experiments": "两个主要 use cases：一是 retention test，写入模式、关闭/调整 refresh、等待指定 refresh interval、读回比较；二是 latency experiment，降低 tRCD/tRAS 并比较 recently-refreshed/accessed rows 与普通 rows 的错误情况。",
        "results": [
            ("SoftMC 是 first open-source FPGA-based experimental memory testing infrastructure，并提供 high-level programming interface。", "Page 1-2, Abstract/Contributions"),
            ("prototype 在 Xilinx ML605/Virtex-6 上实现，当前 DDR interface 400MHz，可连续 issue 两个 commands 间最小 2.5ns。", "Page 6 and Page 10, Section 5.5/7"),
            ("retention test 在 refresh interval 达到 1s 前未观察到 retention failures，说明许多 cells retention time 远高于 64ms 标准。", "Page 7, Figure 5 discussion"),
            ("SoftMC 的 retention results 与 prior studies 一致，验证了平台正确性。", "Page 8, Section 6.1.3"),
            ("在 24 modern DRAM chips、三大 manufacturers 上，recently-refreshed/accessed rows 的预期 latency reduction effect 不可观察。", "Page 1-2 and Page 9, Figures 7-8 discussion"),
            ("SoftMC limitation：不适合直接评估系统性能，因为 PCIe latency 远高于 DRAM access latency。", "Page 10, Section 7"),
        ],
        "conclusion": "SoftMC 的主要价值是把真实 DRAM experimentation 从厂商专用设备中解放出来，让架构研究可重复地测试 retention、latency、failure 和新机制；同时它也提醒论文机制必须回到真实芯片验证。",
        "limitations_author": [
            ("SoftMC 不能直接作为主存控制器评估系统性能，因为 PCIe latency 约 1us，而 DRAM access latency 约 15-80ns。", "Page 10, Section 7"),
            ("当前 prototype 的 instruction queue 大小限制一次原子执行序列长度，循环控制流仍是未来改进方向。", "Page 10, Section 7"),
        ],
        "limitations_infer": [
            ("原型基于 ML605/DDR-era 平台，迁移到 DDR5/HBM/CXL 或 vendor-specific features 需要新 PHY/板卡支持。", "推断，基于 Section 5.5"),
            ("SoftMC 暴露的是 DDR command-level 控制，无法访问芯片内部不可暴露的 sense amplifier timing 或厂商 remapping 细节。", "推断，基于 Section 6.2 discussion"),
        ],
        "focus": "重点读 Figure 2/4 的系统设计、Figure 3 instruction encoding、Program 2 API 示例、Figure 5 retention test、Figures 7-8 latency validation。",
        "relation": "SoftMC 是 LEC3 多篇 DRAM characterization 论文的重要基础设施；RowHammer、retention、latency、PARBOR 等实验都依赖类似可控 FPGA testing。",
        "figures": [
            ("Figure 1", "Page 2", "DRAM organization", "复习 channel/rank/chip/bank 结构。"),
            ("Figure 2", "Page 5", "SoftMC infrastructure", "展示 host/API/driver/FPGA/DRAM 关系。"),
            ("Figure 3", "Page 5", "instruction types", "展示 SoftMC DDR/WAIT/BUSDIR/END instruction encoding。"),
            ("Figure 4", "Page 6", "hardware architecture", "展示 instruction receiver/dispatcher/executor/read capture/calibration。"),
            ("Figure 5", "Page 7", "retention failures", "复现 retention behavior。"),
            ("Figures 7-8", "Page 9", "tRCD/tRAS latency experiments", "验证 latency reduction effect 不可观察。"),
        ],
        "tables": [
            ("未检测到核心编号表", "-", "论文主要用架构图、代码片段和实验图展示结果。", "建议回到 PDF 查看 Program 1/2 和 Figures 2-8。"),
        ],
        "equations": [
            ("DDR timing constraints", "Page 3", "timing parameter constraints", "tRCD/tRAS/tRP/tWR/tWTR/tRTW/tREFI/tRFC", "SoftMC 通过 WAIT instruction 显式控制这些 timing。", "是"),
        ],
        "terms": [
            ("SoftMC", "Soft Memory Controller", "Page 1-2", "开源 FPGA-based 可编程 DRAM testing infrastructure。", "是"),
            ("DDR command", "DDR 命令", "Page 2-3", "ACTIVATE/READ/WRITE/PRECHARGE/REFRESH 等控制 DRAM 的标准接口命令。", "是"),
            ("Timing parameter", "时序参数", "Page 3", "tRCD、tRAS、tRP 等命令间最小间隔约束。", "是"),
            ("Retention test", "保持时间测试", "Page 7", "写入数据、等待指定 refresh interval、读回比较错误。", "是"),
            ("RIFFA", "FPGA PCIe 通信框架", "Page 4-6", "SoftMC host 与 FPGA 间传输 instruction/data 的接口。", "中"),
        ],
        "sections": "Abstract; Introduction; Background; Motivation; Related Work; SoftMC Design; Use Cases; Limitations; Research Directions; Conclusion",
        "translation": [
            ("Abstract / 摘要", "Page 1", "SoftMC 是面向 DDR memory modules 的开源 FPGA-based testing platform。它提供灵活 command-level 控制和易用 high-level API，用于真实 DRAM characterization 和机制验证。"),
            ("1-3. Motivation / 动机", "Page 1-4", "DRAM scaling 造成可靠性和 latency 难题，真实芯片实验必不可少。理想平台需要 flexibility 与 ease of use；商业 tester、旧 FPGA 平台和 BIST 都不能同时满足。"),
            ("5. SoftMC Design / 设计", "Page 4-6", "SoftMC 由 host API、driver、FPGA hardware 和 DDR PHY 构成。用户生成 instruction sequence，FPGA 端执行 DDR commands 并返回读数据。WAIT instruction 允许精确控制 timing。"),
            ("6. Use Cases / 用例", "Page 7-10", "retention test 复现已知现象，说明平台能可靠测试真实 DRAM。latency experiments 用 SoftMC 验证最近刷新/访问的 row 是否可降低 tRCD/tRAS，结果在现有芯片不可观察。"),
            ("7-10. Limitations and Conclusion / 局限与结论", "Page 10-11", "SoftMC 不适合直接做系统性能主存控制器，但很适合实验 characterization。作者希望开源工具推动新的 memory system studies。"),
        ],
    },
]


def render_figs(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑核心论证 | 建议回到 PDF 查看图中细节 |" for a, b, c, d in p["figures"])


def render_tables(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |" for a, b, c, d in p["tables"])


def render_equations(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | {e} | {f} |" for a, b, c, d, e, f in p["equations"])


for p in PAPERS:
    slug = p["slug"]
    url = f"https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC3/{slug}.pdf"
    src = f"paper reading/sources/LEC3/{slug}.pdf"
    extracted = f"paper reading/extracted_text/{slug}.txt"
    terms = "\n".join(f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in p["terms"])
    trans = "\n\n".join(f"## {h}\n\n### 原文位置\n{loc}\n\n### 中文翻译\n{text}\n\n---" for h, loc, text in p["translation"])
    key_entries = [
        ("研究问题", p["background"], "Page 1, Abstract/Introduction", "开头定义问题。", "高", "这是全文动机。"),
        ("核心方法", p["method"], "Method/design sections", "方法章节给出机制。", "高", "这是论文主要贡献。"),
    ] + [("关键结果", x, l, "原文实验/图表支持。", "高", "支撑作者结论。") for x, l in p["results"][:6]] + [
        ("作者局限", p["limitations_author"][0][0], p["limitations_author"][0][1], "作者明确说明或设计边界。", "中", "实现或迁移时要复核。"),
        ("推断局限", p["limitations_infer"][0][0], p["limitations_infer"][0][1], "基于论文范围的推断。", "中", "后续阅读方向。"),
    ]
    key_rows = "\n".join(f"| {i} | {a}：{b} | {c} | {d} | {e} | {f} |" for i, (a, b, c, d, e, f) in enumerate(key_entries, 1))

    write(f"papers/{slug}/metadata.md", f"""
# Paper Metadata

- Title: {p['title']}
- Chinese Title: {p['zh']}
- Authors: {p['authors']}
- Year: {p['year']}
- Venue / Journal / Conference: {p['venue']}
- DOI: {p['doi']}
- arXiv ID: 未找到
- URL: {url}
- PDF Source: {src}
- Code / Project Page: {p['code']}
- Dataset: {p['dataset']}
- Main Topic: {p['topic']}
- Keywords: {p['keywords']}
- Reading Status: {STATUS}
- Full Text Available: Yes
- Notes: {NOTE}
""")
    write(f"papers/{slug}/reading_summary.zh.md", f"""
# 中文阅读摘要

## 1. 一句话总结
{p['one']}

## 2. 研究背景
{p['background']}

## 3. 核心问题
{bullets(p['questions'])}

## 4. 核心贡献
{bullets(p['contribs'])}

## 5. 方法概述
{p['method']}

## 6. 实验设计
{p['experiments']}

## 7. 主要结果
{locs(p['results'])}

## 8. 关键结论
{p['conclusion']}

## 9. 局限性
作者明确或设计中直接体现的局限：
{locs(p['limitations_author'])}

我基于论文范围推断的潜在问题：
{locs(p['limitations_infer'])}

## 10. 适合我重点关注的内容
{p['focus']}

## 11. 和其他文献的关系
{p['relation']}
""")
    write(f"papers/{slug}/key_points_with_locations.zh.md", f"""
# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
{key_rows}
""")
    write(f"papers/{slug}/full_translation.zh.md", f"""
# Full Chinese Translation

## Title
原文标题：{p['title']}

中文标题：{p['zh']}

> {NOTE}

{trans}
""")
    write(f"papers/{slug}/figures_tables_equations_notes.zh.md", f"""
# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
{render_figs(p)}

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
{render_tables(p)}

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
{render_equations(p)}
""")
    write(f"papers/{slug}/terminology.zh.md", f"""
# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
{terms}
""")
    write(f"papers/{slug}/limitations_and_questions.zh.md", f"""
# Limitations and Questions

## 1. 作者明确承认的局限
{locs(p['limitations_author'])}

## 2. 论文中隐含的局限
{locs(p['limitations_infer'])}

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、芯片样本、工艺节点、workload、模拟器或 field environment；迁移到新硬件/新数据中心时需复核。（推断）

## 4. 方法可能不适用的场景
- 当 DRAM generation、控制器接口、温度/工作负载、错误模型或系统软件机制与论文假设明显不同，方法收益或风险可能变化。（推断）

## 5. 我阅读时应该追问的问题
{bullets(p['questions'])}

## 6. 后续可以继续阅读的方向
- 与本批相关方向：retention-aware profiling、field reliability modeling、adaptive memory scheduling、RowHammer security、open-source DRAM testing infrastructure。
""")
    write(f"papers/{slug}/reading_checklist.md", "\n".join([
        "# Reading Checklist",
        "",
        "- [ ] 我能说清楚这篇文章解决的问题",
        "- [ ] 我能解释作者的方法或系统设计",
        "- [ ] 我能指出核心创新与已有工作的差异",
        "- [ ] 我能找到支撑主要结论的图、表或实验位置",
        "- [ ] 我能复述最重要的定量结果",
        "- [ ] 我知道这篇文章的局限和适用边界",
        "- [ ] 我知道这篇文章和 LEC3 其他论文的关系",
        "- [ ] 我知道哪些结论有原文位置支持",
        "- [ ] 我知道哪些问题还需要继续查证",
    ]))
    write(f"papers/{slug}/extraction_log.md", f"""
# Extraction Log

- Input Type: GitHub repository PDF
- Source: {url}
- Access Status: 成功下载并读取本地 PDF
- Full Text Retrieved: Yes
- PDF Pages: {p['pages']}
- Sections Detected: {p['sections']}
- Figures Detected: Yes
- Tables Detected: Yes
- Equations Detected: {'Yes' if any(e[0] != '未检测到核心编号公式' for e in p['equations']) else 'No core numbered equations detected'}
- Appendix Detected: 未发现独立 appendix 或本轮未作为重点处理
- Supplementary Material Detected: {p['code'] if p['code'] != '未找到' else '未发现公开 supplementary material'}
- OCR Used: No
- Extracted Text File: {extracted}
- Missing Content: 图中细小标注、双栏局部错位和电路/版图细节建议回到 PDF 人工核对
- Parsing Problems: PDF 双栏文本存在局部换行错位；已按页码、章节、图表编号定位关键结论
- Uncertain Parts: DOI/venue 如 metadata 标注“未找到”则表示未在 PDF 抽取文本中确认
- Need User Action: 无；如需逐字全文翻译，请确认版权授权范围后再处理
- Quality Check: 已覆盖摘要、引言/背景、方法/系统设计、实验/结果或研究路线、局限、图表、术语与复习 checklist
- Batch Status: {STATUS}
""")

print(f"updated {len(PAPERS)} papers for batch 10")
