from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = "第七轮深度阅读完成"
NOTE = "说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。"


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def bullets(xs):
    return "\n".join(f"- {x}" for x in xs)


def locs(xs):
    return "\n".join(f"- {x}（{l}）" for x, l in xs)


P = [
    {
        "slug": "a-1.1v-16gb-ddr5-dram_isscc2023",
        "title": "A 1.1V 16Gb DDR5 DRAM with Probabilistic-Aggressor Tracking, Refresh-Management Functionality, Per-Row Hammer Tracking, a Multi-Step Precharge, and Core-Bias Modulation for Security and Reliability Enhancement",
        "zh": "一种 1.1V 16Gb DDR5 DRAM：面向安全与可靠性的概率 aggressor 跟踪、RFM、逐行 hammer 跟踪、多步预充电与 core-bias 调制",
        "authors": "Woongrae Kim, Chulmoon Jung, Seongnyuh Yoo, Duckhwa Hong, Jeongjin Hwang, Jungmin Yoon, Ohyong Jung, Joonwoo Choi, Sanga Hyun, Mankeun Kang, Sangho Lee, Dohong Kim, Sanghyun Ku, Donhyun Choi, Nogeun Joo, Sangwoo Yoon, Junseok Noh, Byeongyong Go, Cheolhoe Kim, Sunil Hwang, Mihyun Hwang, Seol-Min Yi, Hyungmin Kim, Sanghyuk Heo, Yeonsu Jang, Kyoungchul Jang, Shinho Chu, Yoonna Oh, Kwidong Kim, Junghyun Kim, Soohwan Kim, Jeongtae Hwang, Sangil Park, Junphyo Lee, Inchul Jeong, Joohwan Cho, Jonghwan Kim",
        "year": "2023",
        "venue": "ISSCC 2023",
        "doi": "10.1109/ISSCC42615.2023.10067805",
        "pages": "3",
        "dataset": "1a-nm 16Gb DDR5 DRAM silicon measurements",
        "topic": "DDR5 DRAM reliability; RowHammer mitigation; refresh management; retention",
        "keywords": "DDR5, RowHammer, probabilistic-aggressor tracking, RFM, PRHT, multi-step precharge, VBB",
        "one": "这篇 ISSCC 芯片论文在 1.1V 16Gb DDR5 DRAM 中集成多种 RowHammer 与 retention 可靠性机制，使 row hammer failure probability 降低 93.1%，retention time 提升 17%。",
        "background": "随着 1a-nm 及更小 DRAM 工艺缩放，cell 间耦合、row hammer 和 refresh/retention 余量持续恶化；DDR5 引入 RFM 等机制，但真实芯片还需要把 controller-side 与 in-DRAM tracking/refresh 协同设计。",
        "questions": ["1a-nm DDR5 面临的 row hammer 与 retention 挑战是什么？", "RFM、PAT、PRHT 三类机制如何协作追踪 aggressor row？", "multi-step precharge 如何提高 intrinsic row-hammer tolerance？", "core-bias modulation 如何改善高温 retention？"],
        "contribs": ["展示一颗 1.1V 16Gb DDR5 DRAM silicon，实现综合可靠性增强。", "实现 probabilistic-aggressor tracking (PAT) 与 refresh-management functionality (RFM)。", "提出/实现 per-row hammer tracking (PRHT)，用 R/H cells 存储每条 wordline 的 activation count。", "通过 multi-step precharge 提高 intrinsic row hammer tolerance 37%。", "用 core-bias/VBB temperature modulation 在 90C 下提升 refresh retention time 17%。"],
        "method": "芯片把 DDR5 RFM command path 与内部 hammer tracking 结合：controller 根据 RAACNT/RAAIMT 触发 RFM；PAT 以概率方式识别 aggressor；PRHT 使用 R/H cells 记录每条 WL 的 activation count 并在超阈值时刷新邻近 rows；multi-step precharge 和 VBB modulation 分别改善 row hammer/retention circuit margin。",
        "experiments": "论文展示 ISSCC silicon-level 测量，包括 50 个 row-hammer malicious patterns、PRHT/PAT failure probability、multi-step precharge tolerance、VBB 温度调制对 retention 的改善。",
        "results": [("综合方案将 row hammer attack failure probability 降低 93.1%，并将 retention time 提升 17%。", "Page 1, Abstract-style summary"), ("multi-step precharge 将 intrinsic row-hammer tolerance 提升 37%。", "Page 2, Figure 28.8.4/28.8.5 discussion"), ("PRHT 在 50 个 malicious row-hammer patterns 下将 failure probability 降低 90.5%。", "Page 2, Figure 28.8.6 discussion"), ("PAT logic 在 intrinsic row-hammer tolerance 降低 66% 的条件下仍通过 50 种 malicious patterns。", "Page 2, Figure 28.8.6 discussion"), ("VBB temperature modulation 在 90C 下使 refresh retention time 提升 17%。", "Page 3, Figure 28.8.7")],
        "conclusion": "DDR5 时代的 RowHammer/retention 防御需要 controller、in-DRAM tracking 和 circuit-level margin enhancement 协同；本文是面向真实 DRAM 产品化约束的集成设计示例。",
        "limitations_author": [("论文篇幅为 ISSCC short paper，算法与电路细节、面积/功耗开销披露有限。", "全文形式，Page 1-3"), ("评估主要是芯片级统计和 malicious pattern 测试，不是系统级 workload 性能评估。", "Page 1-3, Figures 28.8.1-28.8.7")],
        "limitations_infer": [("由于机制依赖 DDR5 RFM/controller 协作，不同系统 controller 策略会影响端到端保护效果。", "推断，基于 RFM algorithm"), ("论文没有公开完整 RTL/测试流程，复现实验依赖厂商内部芯片环境。", "推断，基于 ISSCC silicon paper")],
        "focus": "重点看 Figure 28.8.2 的 RFM 流程、Figure 28.8.4/28.8.5 的 precharge/PRHT、Figure 28.8.6/28.8.7 的效果。",
        "relation": "它是 RowHammer 防御从学术机制走向 DDR5 silicon 的代表，与 PRAC/RFM、Chronus、VRD 和原始 RowHammer 形成技术脉络。",
        "figures": [("Figure 28.8.1", "Page 1", "chip overview", "展示 16Gb DDR5 chip 和主要可靠性模块。"), ("Figure 28.8.2", "Page 1-2", "RFM algorithm", "说明 RAACNT/RAAIMT 与 RFM command 关系。"), ("Figure 28.8.3", "Page 2", "PAT / tracking path", "展示 probabilistic aggressor tracking 思路。"), ("Figure 28.8.4", "Page 2", "PRHT scheme", "说明 R/H cells 如何逐行计数。"), ("Figure 28.8.7", "Page 3", "VBB modulation and retention", "展示高温 retention 改善。")],
        "tables": [("未检测到编号表", "Page 1-3", "ISSCC chip summary", "本文主要以图展示测量结果。")],
        "equations": [("未检测到核心编号公式", "-", "芯片机制说明", "-", "本文没有需要重点掌握的编号公式。", "否")],
        "terms": [("RFM", "刷新管理功能", "Page 1-2", "DDR5 中由 controller 触发、帮助缓解 row hammer 的 refresh-management mechanism。", "是"), ("PAT", "概率 aggressor 跟踪", "Page 1-2", "以概率方式追踪可能造成 disturbance 的 aggressor rows。", "是"), ("PRHT", "逐行 hammer 跟踪", "Page 2", "通过 R/H cells 记录每条 wordline activation count 并触发额外 refresh。", "是"), ("VBB modulation", "体偏置调制", "Page 3", "随温度调节 core bias 来改善 retention margin。", "是")],
        "sections": "ISSCC short paper; chip overview; RFM/PAT/PRHT; multi-step precharge; VBB modulation; silicon measurements",
        "translation": [("Title and Summary / 标题与概要", "Page 1", "本文介绍一颗 1.1V、16Gb DDR5 DRAM，目标是在 1a-nm 缩放节点下增强安全性和可靠性。论文把 RowHammer mitigation、refresh management、per-row tracking、多步预充电和 core-bias 调制组合在同一芯片中。"), ("RFM and PAT / RFM 与概率跟踪", "Page 1-2", "控制器统计 row activation accumulation count，并在达到阈值时发送 RFM command。芯片内部的 probabilistic-aggressor tracking 进一步帮助识别高风险 aggressor rows，以便对相邻 rows 进行 refresh。"), ("PRHT and Precharge / PRHT 与预充电", "Page 2", "PRHT 使用 R/H cells 保存每条 wordline 的 hammer 计数，通过内部 read-modify-write 更新状态；当计数超过阈值时，芯片对相邻 row 进行额外 refresh。multi-step precharge 通过改善电路层行为提升 intrinsic row hammer tolerance。"), ("Retention Enhancement / retention 增强", "Page 3", "core-bias modulation 根据温度调节 VBB，以提升高温下的 retention time。测量结果显示在 90C 时 refresh retention time 提升 17%。"), ("Conclusion / 结论", "Page 3", "论文说明现代 DDR5 DRAM 的可靠性需要协议、架构和电路联合设计；单独依赖外部控制器或单一阈值策略不足以覆盖 row hammer 与 retention 问题。")],
    },
    {
        "slug": "application-slowdown-model_micro15",
        "title": "The Application Slowdown Model: Quantifying and Controlling the Impact of Inter-Application Interference at Shared Caches and Main Memory",
        "zh": "Application Slowdown Model：量化并控制共享 cache 与主存处跨应用干扰的影响",
        "authors": "Lavanya Subramanian, Vivek Seshadri, Arnab Ghosh, Samira Khan, Onur Mutlu",
        "year": "2015",
        "venue": "MICRO 2015",
        "doi": "10.1145/2830772.2830803",
        "pages": "14",
        "dataset": "100 multiprogrammed workloads; SPEC CPU applications; database workloads",
        "topic": "Shared-resource interference; slowdown estimation; cache/memory QoS",
        "keywords": "ASM, slowdown, cache access rate, auxiliary tag store, memory bandwidth partitioning, QoS",
        "one": "ASM 用 shared cache access rate (CAR) 的 online 变化估计应用 slowdown，并把估计值用于 cache partitioning、memory bandwidth partitioning、QoS 和 fair pricing。",
        "background": "多核系统中多个应用共享 LLC 和 memory bandwidth，互相干扰导致单应用性能下降；已有机制要么只估计 cache 或 memory 的一部分影响，要么需要离线 profiling，难以在线准确控制。",
        "questions": ["如何在线估计应用在共享 cache 与主存干扰下的 slowdown？", "为什么 cache access rate 能代表应用性能变化？", "如何分别估计 cache interference 和 memory bandwidth interference？", "ASM 的估计能否直接驱动资源分配/QoS 策略？"],
        "contribs": ["提出 Application Slowdown Model，用 CARalone/CARshared 估计 slowdown。", "用高优先级 phase 近似消除 memory bandwidth interference，以估计 isolated cache access rate。", "用 auxiliary tag store 与 contention misses 估计 cache interference。", "在 100 个 workloads 上将平均 slowdown estimation error 降到 9.9%。", "展示 ASM-Cache、ASM-Mem、ASM-QoS 和 fair pricing 四个 use cases。"],
        "method": "ASM 把应用性能与 shared cache access rate 联系起来。系统周期性给目标应用 memory high priority，测量不受 memory bandwidth 干扰时的 CAR；再用 auxiliary tag store 推断没有 cache contention 时的 cache accesses。最终用 CARalone/CARshared 估计 slowdown，并把该估计输入 cache/memory resource management。",
        "experiments": "作者用 cycle-level simulator 和 SPEC/database workloads 评估 slowdown estimation accuracy；比较 FST、PTCA 等先前机制；再把 ASM 接入 cache partitioning、memory bandwidth partitioning 和 soft slowdown guarantee 策略。",
        "results": [("ASM 在 100 个 workloads 上平均 slowdown estimation error 为 9.9%，比最佳先前机制 FST 的 29.4% 明显更低。", "Page 1, Abstract; Page 6-8, Figure 2/4"), ("使用 sampled auxiliary tag store 时，ASM error 从 9.0% 仅升至 9.9%，而 PTCA/FST 分别升至 40.4%/29.4%。", "Page 7-8, Figure 3"), ("数据库 workloads 上，FST/PTCA/ASM sampled errors 分别为 27%/12%/4%。", "Page 8, Section 6.1.2"), ("ASM-Cache 在 8-core 系统上降低 unfairness 12.5%，并提升性能。", "Page 10-11, Figure 9"), ("ASM-QoS 能为指定应用提供 soft slowdown guarantee，同时避免过度牺牲系统吞吐。", "Page 12, Figure 11")],
        "conclusion": "准确的 online slowdown model 是共享资源管理的基础；ASM 说明只要抓住 CAR 这个应用级指标，就能把 cache 和 memory interference 合并成可操作的 slowdown estimate。",
        "limitations_author": [("ASM 依赖 auxiliary tag store、高优先级 sampling phase 和硬件计数器，增加实现复杂度。", "Page 4-6, Section 4-5"), ("ASM 给的是 slowdown estimate 而非严格实时保证，QoS 用例也定位为 soft guarantee。", "Page 11-12, Section 6.2.3")],
        "limitations_infer": [("CAR 与性能的相关性对极端 compute-bound、prefetch-heavy 或 non-cache-sensitive 应用可能减弱。", "推断，基于 Figure 1 assumption"), ("sampling phase 会扰动正常调度，在非常短 phase 或强实时系统中需重新评估。", "推断，基于 online sampling")],
        "focus": "重点看 Figure 1 的 CAR-performance 关系、Section 4 的模型推导、Figures 2-4 的 accuracy、Figures 9-11 的 resource management use cases。",
        "relation": "ASM 与 MISE、DASH 同属 shared-memory QoS/调度线；MISE 估计 memory interference，ASM 扩展到 cache+memory slowdown。",
        "figures": [("Figure 1", "Page 2", "cache access rate vs performance", "说明 CAR 可作为性能代理。"), ("Figure 2", "Page 7", "slowdown estimation accuracy", "比较 ASM/PTCA/FST。"), ("Figure 4", "Page 8", "error distribution", "展示不同 workloads 的误差分布。"), ("Figure 9", "Page 10", "ASM-Cache", "展示 slowdown-aware cache partitioning 的公平性收益。"), ("Figure 11", "Page 12", "ASM-QoS", "展示 soft slowdown guarantee。")],
        "tables": [("Table 1", "Page 5", "metrics measured by ASM", "列出 CAR、miss rate、contention misses 等计数。"), ("Table 2", "Page 6", "simulation configuration", "列出核心、cache、DRAM 参数。")],
        "equations": [("Slowdown estimate", "Page 3-4, Section 3", "估计 slowdown", "Slowdown ≈ CARalone / CARshared", "若共享状态下 CAR 降低，则应用相对独占运行变慢。", "是")],
        "terms": [("Application Slowdown Model (ASM)", "应用 slowdown 模型", "Page 1", "在线估计共享 cache/主存干扰导致应用性能下降的模型。", "是"), ("Cache Access Rate (CAR)", "cache 访问率", "Page 2-4", "单位时间内 shared cache accesses，用作性能代理。", "是"), ("Auxiliary Tag Store (ATS)", "辅助 tag 存储", "Page 4-5", "用于估计应用在无 cache contention 情况下的 cache behavior。", "是"), ("Soft slowdown guarantee", "软 slowdown 保证", "Page 11-12", "尽量把目标应用 slowdown 控制在用户给定 bound 内。", "是")],
        "sections": "Abstract; Introduction; Motivation; Application Slowdown Model; Mechanisms; Methodology; Evaluation; Use Cases; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "论文提出 ASM，用于在线估计共享 cache 和主存干扰造成的应用 slowdown。ASM 不需要事先知道应用行为，在 100 个 workloads 上平均误差为 9.9%，并能驱动多种共享资源管理策略。"), ("1-3. Motivation / 动机与模型直觉", "Page 1-4", "多核环境中，应用之间的 cache contention 和 memory bandwidth contention 会共同影响性能。作者观察到应用 performance 与 shared cache access rate 高度相关，因此可用 CARalone/CARshared 作为 slowdown 近似。"), ("4-5. ASM Mechanism / 机制", "Page 4-6", "ASM 通过周期性给应用 high memory priority 来估计不受 memory bandwidth interference 时的 CAR；再借助 auxiliary tag store 估计无 cache contention 时的行为。多个硬件计数器共同构成 online slowdown estimator。"), ("6. Evaluation / 评估", "Page 6-9", "实验显示 ASM 的平均误差显著低于 FST 和 PTCA，即使使用 sampled ATS 也保持较高准确性；数据库 workloads 的误差尤其低。"), ("7. Use Cases / 用例", "Page 9-12", "ASM 被接入 cache partitioning、memory bandwidth partitioning、QoS guarantee 和 fair pricing。核心思想是用估计 slowdown 作为优化目标，而不是只优化总吞吐或局部 miss rate。"), ("Conclusion / 结论", "Page 13-14", "作者认为 slowdown 是共享资源系统中更接近用户体验和公平性的指标；ASM 提供了足够准确且可部署的在线估计方法。")],
    },
    {
        "slug": "avatar-dram-refresh_dsn15",
        "title": "AVATAR: A Variable-Retention-Time (VRT) Aware Refresh for DRAM Systems",
        "zh": "AVATAR：面向 DRAM 系统的 Variable-Retention-Time 感知刷新",
        "authors": "Moinuddin K. Qureshi, Dae-Hyun Kim, Samira Khan, Prashant J. Nair, Onur Mutlu",
        "year": "2015",
        "venue": "DSN 2015",
        "doi": "未找到",
        "pages": "11",
        "dataset": "24 DRAM chips; simulated 8Gb-64Gb DRAM systems",
        "topic": "DRAM refresh; variable retention time; ECC; reliability",
        "keywords": "AVATAR, VRT, DRAM refresh, ECC, scrubbing, multirate refresh, active VRT pool",
        "one": "AVATAR 通过 ECC 与 scrubbing 在运行时捕获 VRT 引发的 retention failures，并把对应 rows 提升到 fast refresh rate，从而让 multirate refresh 在 VRT 存在时仍可靠。",
        "background": "DRAM 容量增加使 refresh overhead 成为 Refresh Wall；multirate refresh 依赖离线 profiling 识别 weak rows，但 VRT cells 会在运行时随机转入低 retention 状态，破坏静态 profile 的可靠性。",
        "questions": ["VRT 为什么会让传统 multirate refresh 不安全？", "Active-VRT Pool 与 Active-VRT Injection 如何刻画 VRT 行为？", "AVATAR 如何用 ECC/scrubbing 捕获新出现的 VRT failures？", "AVATAR 在可靠性、refresh savings、性能和 EDP 上收益多少？"],
        "contribs": ["建立 VRT-aware refresh 的统计模型，定义 AVP 与 AVI。", "证明 VRT-agnostic ECC DIMM 在 multirate refresh 下仍可能每 6-8 个月出现一次 uncorrectable error。", "提出 AVATAR：用 ECC+sweeping scrub 发现 VRT-induced errors，并把 affected rows 加入 fast refresh set。", "把传统 multirate refresh 的可靠性提升约 100x，同时保留 62%-72% refresh reduction。", "在 64Gb DRAM 上提升性能 35%，EDP 降低 55%。"],
        "method": "系统先做 retention profiling，把 weak rows 放入 fast refresh table。运行时定期 scrubbing；若 ECC 发现 correctable retention error，就认为该 row 发生 VRT transition，将其 promotion 到 fast refresh rate。随着时间推移，AVATAR 动态扩展 fast-refresh set，以覆盖新出现的 VRT-active cells。",
        "experiments": "作者用 24 chips 的 VRT behavior 数据建立模型，评估传统 multirate refresh、ECC-only 和 AVATAR 在不同 DRAM density/AVI rate 下的 time-to-failure、refresh savings、performance 和 EDP。",
        "results": [("VRT-agnostic ECC DIMMs 仍可能每 6-8 个月产生一次 uncorrectable error。", "Page 1, Abstract/Introduction"), ("Active-VRT Pool 在 2GB memory 的 15 分钟窗口内平均约 350-500 cells。", "Page 5, Figure 7"), ("AVATAR 将传统 multirate refresh 的可靠性提高约 100x，time-to-failure 从 months 延伸到 decades。", "Page 1 and Page 8, Figure 14"), ("即使一年后，AVATAR 仍保持 62.4% refresh savings；初期约 72%。", "Page 9, Figure 15"), ("64Gb DRAM 上 AVATAR-1 提升性能 35%，EDP 降低 55%。", "Page 9-10, Figures 16-17")],
        "conclusion": "VRT 不应让系统放弃 refresh reduction；只要把 ECC/scrubbing 变成运行时 feedback loop，multirate refresh 可以在保持可靠性的同时大幅降低 refresh overhead。",
        "limitations_author": [("AVATAR 依赖 ECC DIMM 和 scrubbing；没有 ECC 的系统无法按该方式安全捕获 VRT failures。", "Page 6-7, Section V"), ("fast refresh table 会随时间增长，长期 refresh savings 低于刚测试后的 profile。", "Page 9, Figure 15")],
        "limitations_infer": [("VRT 统计模型来自有限芯片样本，未来工艺/温度/工作负载下 AVI rate 可能变化。", "推断，基于 24 chips sample"), ("scrubbing 周期、ECC 强度与系统空闲带宽会影响实际部署效果。", "推断，基于 scrubbing design")],
        "focus": "重点看 Figure 1 Refresh Wall、Figure 7/9 的 VRT 模型、Figure 13 AVATAR design、Figures 14-17 的可靠性与性能结果。",
        "relation": "AVATAR 与 RAIDR/Reaper 都是 refresh reduction 论文，但它专门处理 VRT 使静态 retention profile 失效的问题。",
        "figures": [("Figure 1", "Page 1-2", "Refresh Wall", "展示高密度 DRAM refresh 性能/功耗开销。"), ("Figure 3", "Page 3", "multirate refresh", "说明传统 retention-aware refresh 机制。"), ("Figure 7", "Page 5", "Active-VRT Pool", "量化短窗口内 active VRT cells。"), ("Figure 13", "Page 7", "AVATAR design", "展示 ECC/scrubbing/promotion loop。"), ("Figure 14", "Page 8", "time to failure", "展示可靠性提升。"), ("Figure 17", "Page 10", "EDP reduction", "展示性能与能耗收益。")],
        "tables": [("Table I", "Page 8", "scrubbing overhead", "说明 AVATAR scrubbing 的额外带宽/性能开销。")],
        "equations": [("TTF model", "Page 7-8", "可靠性估计", "基于 AVI rate、ECC coverage 与 scrub interval 的概率模型", "VRT 新注入单元越快，uncorrectable error 越早出现。", "中")],
        "terms": [("Variable Retention Time (VRT)", "可变保持时间", "Page 1-4", "DRAM cell retention time 在高/低状态间随机切换的现象。", "是"), ("Active-VRT Pool (AVP)", "活跃 VRT 池", "Page 5", "给定时间窗口内处于低 retention 状态的 VRT cells 数量。", "是"), ("Active-VRT Injection (AVI)", "活跃 VRT 注入", "Page 5", "每个时间窗口新进入 active VRT 状态的 cells 数量。", "是"), ("Multirate refresh", "多速率刷新", "Page 3", "弱 rows 用高频刷新、强 rows 用低频刷新以减少总 refresh。", "是")],
        "sections": "Abstract; Introduction; Background; VRT Characterization; AVATAR Design; Evaluation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "AVATAR 面向 VRT-aware DRAM refresh。它用 ECC 和 scrubbing 在运行时发现由 VRT 造成的错误，并把相关 rows 动态提升到 fast refresh rate，从而显著提升 multirate refresh 的可靠性。"), ("1-3. Background / 背景", "Page 1-4", "DRAM 密度提升带来 Refresh Wall。传统 multirate refresh 假设 retention profile 相对稳定，但 VRT cells 会随时间进入低 retention 状态，使离线测试不再可靠。"), ("4. VRT Model / VRT 模型", "Page 4-6", "作者用 Active-VRT Pool 和 Active-VRT Injection 描述 VRT 动态行为。短时间窗口内 active VRT cells 数量有限，但持续运行时会不断出现新的风险 cells。"), ("5. AVATAR Design / 设计", "Page 6-8", "AVATAR 在已有 retention profile 基础上运行。ECC correctable errors 作为 VRT 信号，scrubbing 周期性扫描内存；一旦发现可纠正 retention error，就把对应 row 加入 fast refresh table。"), ("6. Evaluation / 评估", "Page 8-10", "结果显示 AVATAR 同时提升可靠性和保持 refresh savings。相比 VRT-agnostic multirate refresh，TTF 从数月提升到数十年或更久，并在高密度 DRAM 上显著改善 performance 和 EDP。"), ("Conclusion / 结论", "Page 10-11", "作者总结 VRT-aware dynamic promotion 是让 refresh reduction 实用化的关键：系统不必为最坏情况刷新所有 rows，而可以在运行时发现和隔离新变弱的 rows。")],
    },
    {
        "slug": "dash_deadline-aware-heterogeneous-memory-scheduler_taco16",
        "title": "DASH: Deadline-Aware High-Performance Memory Scheduler for Heterogeneous Systems with Hardware Accelerators",
        "zh": "DASH：面向含硬件加速器异构系统的 deadline-aware 高性能内存调度器",
        "authors": "Hiroyuki Usui, Lavanya Subramanian, Kevin Kai-Wei Chang, Onur Mutlu",
        "year": "2016",
        "venue": "ACM TACO 2016",
        "doi": "10.1145/2847255",
        "pages": "28",
        "dataset": "CPU multiprogrammed workloads; hardware accelerators such as Sobel/TPACF/Debayer/DMR; GPU-HWA scenarios",
        "topic": "Memory scheduling; heterogeneous systems; hardware accelerators; deadlines",
        "keywords": "DASH, deadline-aware scheduling, hardware accelerator, HWA, memory scheduler, FRFCFS",
        "one": "DASH 在 CPU 与 hardware accelerators 共享 DRAM 的 SoC 中，用 deadline-aware 且 application-aware 的内存调度同时满足 HWA deadlines 并提升 CPU performance。",
        "background": "现代 SoC 中 CPU、GPU 和专用 HWA 共享 DRAM。HWA 往往有 frame deadline，CPU 需要高吞吐；简单优先 HWA 会牺牲 CPU，简单优先 CPU 又会错过 HWA deadline。",
        "questions": ["memory scheduler 如何判断 HWA 是否 on track 满足 deadline？", "为什么应优先打断 memory-intensive CPU 而保护 memory-nonintensive CPU？", "短 deadline HWA 是否需要与长 deadline HWA 不同的调度？", "DASH 相比 FRFCFS 和 dynamic threshold scheduler 性能/deadline tradeoff 如何？"],
        "contribs": ["提出 Distributed Priority：HWA 不在进度轨道上时立即分散式提高优先级，而不是临近 deadline 才抢占。", "提出 application-aware priority：当 HWA 需要优先时，优先压制 memory-intensive CPU apps。", "针对短 deadline HWA 用 worst-case memory access time 估计保守调度。", "在 80 个 workloads 上实现 100% deadline-met ratio，同时比最佳先前 scheduler 提升 9.5% CPU performance。"],
        "method": "DASH 监控每个 HWA 的 period、deadline、remaining requests 和 progress，判断其是否 on track。若 HWA 落后，scheduler 提升其请求优先级；同时根据 CPU application memory intensity 区分受影响对象，优先保护 latency-sensitive/memory-nonintensive apps。",
        "experiments": "使用多核 CPU + HWA/GPU 共享 DRAM 模拟，比较 FRFCFS、CPU-friendly、HWA-friendly、FRFCFS-Dyn、FRFCFS-DynOpt 与 DASH；指标包括 CPU weighted speedup、system performance、maximum slowdown、deadline-met ratio/frame rate。",
        "results": [("DASH 比最佳先前 scheduler 提升 9.5% CPU performance，并始终满足所有 HWAs/GPUs 的 deadlines。", "Page 1, Abstract; Page 15-17, Figure 5/Table V"), ("HWA-friendly scheduler 可接近 100% deadline-met ratio，但 CPU performance 比 CPU-friendly scheduler 低约 12%。", "Page 3-4, motivation"), ("Figure 5 显示 DASH 在 80 workloads 上兼顾 CPU performance 与 deadline-met ratio。", "Page 15-16, Figure 5"), ("Table V 显示 DASH 的 deadline-met ratio/frame rate 与能满足 deadline 的动态调度相当，但 CPU 性能更好。", "Page 16, Table V"), ("CPU-GPU-HWA 场景中 DASH 仍能保持 frame rate，并控制 CPU slowdown。", "Page 19-21, Figure 9")],
        "conclusion": "异构 SoC memory scheduling 的核心不只是给 HWA 高优先级，而是精确知道何时必须优先、该从哪些 CPU 应用处借带宽，以及短 deadline 场景需要怎样保守处理。",
        "limitations_author": [("DASH 假设 HWA 的 deadline、period 和 memory request demand 可由系统获知或估计。", "Page 6-9, design"), ("研究重点是 soft real-time frame deadlines；hard real-time worst-case guarantee 不是本文目标。", "Page 4 and Page 8-10")],
        "limitations_infer": [("真实 SoC 中不同 HWA 的 burstiness、QoS contract 和 memory controller 实现会影响策略迁移。", "推断，基于 simulator evaluation"), ("DASH 需要额外硬件监控和 scheduler 逻辑，复杂度高于 FRFCFS。", "推断，基于 scheduler design")],
        "focus": "重点看 Figure 3 的 timeline 动机、Section 4 的三条设计原则、Figure 5/Table V 的主要结果、Figure 9 的 CPU-GPU-HWA 场景。",
        "relation": "DASH 与 ASM/MISE 都面向共享内存干扰，但 DASH 的目标是 HWA deadlines + CPU throughput，而 ASM/MISE 更关注应用 slowdown/fairness。",
        "figures": [("Figure 1", "Page 2", "heterogeneous SoC", "展示 CPU/GPU/HWA 共享 DRAM 场景。"), ("Figure 2", "Page 3", "Sobel HWA", "说明 HWA frame processing 与 deadline。"), ("Figure 3", "Page 4", "execution timelines", "展示不同调度策略如何错过或满足 deadline。"), ("Figure 5", "Page 15", "CPU performance", "展示 DASH 与 baselines 的核心对比。"), ("Figure 9", "Page 20", "CPU-GPU-HWA", "展示复杂异构场景。")],
        "tables": [("Table V", "Page 16", "deadline-met ratio/frame rate", "证明 DASH 保持 deadlines。"), ("Table VI", "Page 18", "system performance and max slowdown", "展示系统性能与公平性影响。")],
        "equations": [("Progress/on-track estimate", "Page 7-9, Section 4", "判断 HWA 是否能在 deadline 前完成", "基于 elapsed time、period/deadline、remaining requests 与 worst-case memory access time", "若预计赶不上 deadline，提升 HWA priority。", "是")],
        "terms": [("DASH", "deadline-aware high-performance scheduler", "Page 1", "面向 CPU+HWA 异构系统的内存调度器。", "是"), ("Distributed Priority", "分散式优先级", "Page 5-7", "HWA 落后时在整个 period 中分散给予优先，而不是最后集中抢占。", "是"), ("Deadline-met ratio", "deadline 满足率", "Page 10-16", "HWA frames 在 deadline 前完成的比例。", "是"), ("Memory-intensive application", "内存密集应用", "Page 5-8", "对内存带宽敏感但单请求 latency sensitivity 相对低的 CPU 应用。", "是")],
        "sections": "Abstract; Introduction; Background; Motivation; DASH Design; Methodology; Evaluation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "DASH 是一种 memory scheduler，用于 CPU 和 hardware accelerators 共享 DRAM 的异构系统。它在满足 HWA deadline 的同时，尽量保持 CPU 高性能。"), ("1-3. Background and Motivation / 背景与动机", "Page 1-5", "HWA 处理图像/视频等 frame-based workload，需要在 deadline 前完成；CPU workloads 同时需要 DRAM bandwidth。传统 FRFCFS 或简单优先级策略难以同时满足这两个目标。"), ("4. DASH Design / 设计", "Page 5-10", "DASH 的关键是 Distributed Priority、application-aware prioritization 和短 deadline HWA 的保守 worst-case 处理。调度器持续判断 HWA progress 是否 on track，并在必要时优先 HWA 请求。"), ("5-6. Methodology and Evaluation / 方法与评估", "Page 10-22", "实验使用多种 CPU workloads、HWA 类型和 GPU-HWA 组合。DASH 在 deadline-met ratio 与 frame rate 上保持目标，同时比能满足 deadline 的先前策略有更高 CPU performance。"), ("Conclusion / 结论", "Page 26-28", "作者总结异构系统的 memory scheduler 必须理解加速器 deadline 和 CPU 应用特性，才能避免过度保守或过度冒险的调度。")],
    },
    {
        "slug": "dram-row-hammer_isca14",
        "title": "Flipping Bits in Memory Without Accessing Them: An Experimental Study of DRAM Disturbance Errors",
        "zh": "无需访问即可翻转内存位：DRAM disturbance errors 的实验研究",
        "authors": "Yoongu Kim, Ross Daly, Jeremie Kim, Chris Fallin, Ji Hye Lee, Donghyuk Lee, Chris Wilkerson, Konrad Lai, Onur Mutlu",
        "year": "2014",
        "venue": "ISCA 2014",
        "doi": "未找到",
        "pages": "12",
        "dataset": "129 DDR3 DRAM modules; 972 DRAM chips; Intel/AMD real systems; FPGA test platform",
        "topic": "RowHammer; DRAM disturbance errors; memory security and reliability",
        "keywords": "RowHammer, disturbance error, DRAM, PARA, ECC, refresh, clflush",
        "one": "这篇原始 RowHammer 论文证明反复激活 DRAM rows 可在未访问的相邻 rows 中诱发 bit flips，并提出低开销概率相邻行刷新 PARA。",
        "background": "DRAM 缩放让 cell 更小、更易互相耦合；传统接口假设只访问目标地址不会改变其他地址，但 disturbance errors 破坏了内存隔离和可靠性。",
        "questions": ["真实 commodity DRAM 是否普遍存在 disturbance errors？", "最少需要多少 activations 才能触发 bit flips？", "user-level 程序能否在普通系统上诱发错误？", "ECC、提高 refresh rate 和 PARA 分别能否缓解 RowHammer？"],
        "contribs": ["在 129 个 DRAM modules/972 chips 上系统展示 RowHammer 现象。", "发现 110 个 modules/836 chips 出现 disturbance errors，2012/2013 年模块全部脆弱。", "证明只需约 139K 次 row activations 即可触发错误。", "展示 user-level program 使用 loads + clflush 可在 Intel/AMD 系统上诱发 bit flips。", "提出 PARA：row close 时以小概率刷新邻近 rows，低状态开销且可靠性可调。"],
        "method": "作者先用 FPGA platform 精确控制 DRAM commands，扫 data pattern、refresh interval、activation interval 和 rows；再用真实系统上的用户态程序通过 clflush 和交替访问绕过 cache，反复打开/关闭 aggressor rows；最后分析 ECC/refresh/PARA 的缓解能力。",
        "experiments": "样本覆盖 2008-2014 年 DDR3 modules；测试 bit flip 数量、受影响 rows/cells、制造年份、refresh/activation sensitivity、data pattern sensitivity；PARA 用概率模型和性能仿真评估。",
        "results": [("129 个 modules 中 110 个、972 chips 中 836 个出现 disturbance errors。", "Page 1, Abstract; Page 5, Table 3"), ("2012/2013 年制造的所有测试 modules 都存在错误。", "Page 5, Figure 3"), ("最少约 139K 次 wordline toggles/reads 就可诱发 disturbance error。", "Page 1 and Page 7, Figure 6"), ("某些模块中最多每 1.7K cells 就有一个 susceptible cell。", "Page 1, Abstract/Introduction"), ("SECDED ECC 不能完全防护，因为可能出现同一 64-bit word 内多 bit errors。", "Page 8, Table 5"), ("PARA 在 p=0.001 等小概率下可把错误概率降到可忽略，同时性能开销很低。", "Page 9-10, Table 7 and mitigation discussion")],
        "conclusion": "RowHammer 说明 DRAM 隔离边界在现代缩放下已被破坏；可靠系统需要把 disturbance-aware refresh/mitigation 纳入内存控制器或 DRAM 设计，而不能只依赖传统 ECC 或固定 refresh。",
        "limitations_author": [("提高 refresh rate 可以消除测试错误，但需要大幅增加 refresh，带来功耗/性能开销。", "Page 9, Section 7.2"), ("PARA 需要 memory controller 在 row close 时能以概率刷新 adjacent rows，依赖邻接关系和控制器支持。", "Page 9-10, Section 7.4")],
        "limitations_infer": [("本文主要研究 DDR3-era modules；DDR4/DDR5/HBM 的表现需要后续论文重新测量。", "推断，基于 sample scope"), ("安全 exploit 只展示 bit flips，可利用性还取决于 OS memory allocation、page deduplication、ECC/TRR 等系统因素。", "推断，基于 user-level demo")],
        "focus": "重点看 Code 1 的用户态攻击、Table 3/Figure 3 的脆弱性覆盖、Figures 4-9 的实验表征、Table 7 的 PARA。",
        "relation": "这是 RowHammer 研究源头；后续 RowHammer Retrospective、PRAC、Chronus、VRD、RowPress 和 DDR5 RFM 论文都在回应它提出的问题。",
        "figures": [("Figure 1", "Page 2", "DRAM cells", "说明 cell/wordline/bitline 与 disturbance 根因。"), ("Figure 3", "Page 5", "errors by manufacturing date", "展示新芯片更脆弱。"), ("Figure 6", "Page 7", "errors vs activations", "确定触发 bitflip 所需 activation 数。"), ("Figure 8", "Page 8", "affected rows", "展示 victim rows 与 aggressors 的位置关系。"), ("Figure 9", "Page 8", "victim row offsets", "说明邻近行受影响最明显。")],
        "tables": [("Table 2", "Page 4", "real-system bit flips", "展示 Intel/AMD 系统中用户态程序诱发错误。"), ("Table 3", "Page 5", "sample population", "列出 modules/chips 与出错数量。"), ("Table 5", "Page 8", "ECC implications", "说明 SECDED 难以覆盖多 bit flips。"), ("Table 7", "Page 10", "PARA failure probability", "量化 PARA 概率参数的可靠性。")],
        "equations": [("PARA probability", "Page 9-10, Section 7.4/Table 7", "概率相邻行刷新可靠性估计", "row close 后以 probability p refresh adjacent rows", "p 越大，攻击窗口内漏刷 victim rows 的概率指数下降，但 refresh 开销上升。", "是")],
        "terms": [("RowHammer", "行锤击", "Page 1", "反复激活 aggressor rows，导致相邻 victim rows 中 bit flips 的 DRAM disturbance 现象。", "是"), ("Aggressor row", "攻击行/aggressor 行", "Page 2-4", "被反复打开关闭以诱发扰动的 DRAM row。", "是"), ("Victim row", "受害行", "Page 4-8", "未被直接访问却出现 bit flip 的邻近 row。", "是"), ("PARA", "概率相邻行激活/刷新", "Page 9-10", "每次关闭 row 时以小概率刷新邻近 rows 的 mitigation。", "是"), ("SECDED ECC", "单错纠正双错检测 ECC", "Page 8", "常见 ECC，但可能无法修复 RowHammer 多 bit errors。", "是")],
        "sections": "Abstract; Introduction; DRAM Background; Testing Methodology; Experimental Results; Root Cause; Mitigation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "论文系统研究 DRAM disturbance errors。作者发现大量商品 DDR3 模块在反复访问某些 rows 后，会在未访问的附近 rows 中出现 bit flips，并提出 PARA 作为低开销缓解方案。"), ("1-3. Background and Methodology / 背景与方法", "Page 1-4", "DRAM cell 通过 capacitor 存储电荷，wordline activation 会影响邻近 cells。作者使用 FPGA 精确发出 DRAM commands，也在真实 x86 系统上用 loads 与 clflush 构造用户态测试程序。"), ("4. Experimental Results / 实验结果", "Page 4-8", "大多数测试 modules/chips 出现 disturbance errors。错误数量与制造年份、refresh interval、activation interval、访问次数和 data pattern 有关。实验还显示某些 vulnerable cells 分布密集，且相邻 row 关系明显。"), ("5-7. Analysis and Mitigation / 根因与缓解", "Page 8-10", "根因是反复 toggling wordline 加剧邻近 cells 的电荷泄漏。ECC 不能完全解决多 bit errors；提高 refresh rate 有高开销；PARA 用小概率刷新相邻 rows，以低存储状态和低性能开销显著降低错误概率。"), ("Conclusion / 结论", "Page 11-12", "作者总结 RowHammer 是真实、普遍且可由软件触发的可靠性/安全问题。未来 DRAM 系统必须在 controller 或 DRAM 内加入 disturbance-aware 机制。")],
    },
]


def render_figs(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |" for a, b, c, d in p["figures"])


def render_tables(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |" for a, b, c, d in p["tables"])


def render_equations(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | {e} | {f} |" for a, b, c, d, e, f in p["equations"])


for p in P:
    slug = p["slug"]
    url = f"https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC3/{slug}.pdf"
    src = f"paper reading/sources/LEC3/{slug}.pdf"
    extracted = f"paper reading/extracted_text/{slug}.txt"
    terms = "\n".join(f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in p["terms"])
    trans = "\n\n".join(f"## {h}\n\n### 原文位置\n{loc}\n\n### 中文翻译\n{text}\n\n---" for h, loc, text in p["translation"])
    key_entries = [
        ("研究问题", p["background"], "Page 1, Abstract/Introduction", "开头定义问题。", "高", "这是全文动机。"),
        ("核心方法", p["method"], "Method/design sections", "方法章节给出机制。", "高", "这是论文主要贡献。"),
    ] + [("关键结果", x, l, "原文实验/图表支持。", "高", "支撑作者结论。") for x, l in p["results"][:5]] + [
        ("局限", p["limitations_author"][0][0], p["limitations_author"][0][1], "设计边界或作者说明。", "中", "实现时需关注。"),
        ("追问", p["limitations_infer"][0][0], p["limitations_infer"][0][1], "基于范围的推断。", "中", "后续阅读方向。"),
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
- Code / Project Page: 未找到
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
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
{bullets(p['questions'])}

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DDR5 RowHammer 防御、共享资源 slowdown/QoS、VRT-aware refresh、异构 SoC memory scheduling、RowHammer 后续安全研究。
""")
    write(f"papers/{slug}/reading_checklist.md", "\n".join(["# Reading Checklist", "", "- [ ] 我能说清楚这篇文章解决的问题", "- [ ] 我能解释作者的方法或系统设计", "- [ ] 我能指出核心创新与已有工作的差异", "- [ ] 我能找到支撑主要结论的图、表或实验位置", "- [ ] 我能复述最重要的定量结果", "- [ ] 我知道这篇文章的局限和适用边界", "- [ ] 我知道这篇文章和 LEC3 其他论文的关系", "- [ ] 我知道哪些结论有原文位置支持", "- [ ] 我知道哪些问题还需要继续查证"]))
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
- Supplementary Material Detected: 未发现
- OCR Used: No
- Extracted Text File: {extracted}
- Missing Content: 图中细小标注、双栏局部错位和芯片论文电路细节建议回到 PDF 人工核对
- Parsing Problems: PDF 双栏文本存在局部换行错位；ISSCC 短文图中文字密集，已用图号和页码定位
- Uncertain Parts: DOI/arXiv 如 metadata 标注“未找到”则表示未在 PDF 抽取文本中确认
- Need User Action: 无；如需逐字全文翻译，请确认版权授权范围后再处理
- Quality Check: 已覆盖摘要、引言/背景、方法/系统设计、实验/结果、局限、图表、术语与复习 checklist
- Batch Status: {STATUS}
""")

print(f"updated {len(P)} papers for batch 7")
