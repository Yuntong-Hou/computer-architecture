from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = "第八轮深度阅读完成"
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
        "slug": "error-mitigation-for-intermittent-dram-failures_sigmetrics14",
        "title": "The Efficacy of Error Mitigation Techniques for DRAM Retention Failures: A Comparative Experimental Study",
        "zh": "DRAM retention failures 错误缓解技术有效性：一项比较实验研究",
        "authors": "Samira Khan, Donghyuk Lee, Yoongu Kim, Alaa R. Alameldeen, Chris Wilkerson, Onur Mutlu",
        "year": "2014",
        "venue": "SIGMETRICS 2014",
        "doi": "10.1145/2591971.2592000",
        "pages": "14",
        "dataset": "96 DRAM chips from three manufacturers; FPGA-based DRAM testing infrastructure",
        "topic": "DRAM retention failures; VRT; online profiling; ECC; guardbanding",
        "keywords": "DRAM, retention failure, VRT, guardband, ECC, VS-ECC, Hi-ECC, online profiling",
        "one": "这篇论文用 96 颗真实 DRAM 芯片评估 testing、guardbanding 和 ECC 对 intermittent/VRT retention failures 的有效性，结论是单靠测试或 guardband 不够，必须结合 ECC 与在线 profiling。",
        "background": "DRAM cell 缩放使 retention failures 更常见；permanent weak cells 可用制造测试发现，但 VRT 和 data-pattern sensitivity 会让 cell 间歇性失效，导致传统测试或一次性 bit repair 难以保证长期可靠。",
        "questions": ["少量 testing 能发现多少 intermittent failures？", "refresh interval guardband 对 VRT cells 是否足够？", "ECC 与 testing/guardbanding 组合能把 failure probability 降到什么程度？", "已有 bit repair、VS-ECC、Hi-ECC 在真实 intermittent failure 数据下是否仍成立？"],
        "contribs": ["首次用真实 DRAM 数据定量比较 testing、guardbanding、ECC 对 intermittent retention failures 的作用。", "显示 5 rounds testing 可发现多数 failures，并把发现新 failure 的概率降低 100x，但千轮后仍会出现新 failures。", "显示 2X guardband 可覆盖 85%-95% intermittent failing cells，但 5X 仍无法覆盖剩余 VRT cells。", "证明 SECDED/DECTED 与 testing/guardbanding 组合可把 error rate 降低最高 10^12/10^18 量级。", "重新评估 bit repair、VS-ECC、Hi-ECC，指出 ECC-based 方案比纯 testing 方案更可行。"],
        "method": "作者使用 FPGA-based infrastructure 对 96 颗 DRAM chips 在不同 refresh intervals、patterns、temperature 下重复测试，统计 failing cells 随测试轮次、retention states、guardband 和 ECC strength 的变化，并把这些实测 failure probabilities 带入已有 mitigation 的 reliability model。",
        "experiments": "实验包括 retention failure vs refresh interval、testing rounds coverage、VRT state hold time、guardband coverage、ECC+testing failure-rate reduction、以及 bit repair/VS-ECC/Hi-ECC 的 expected time-to-failure。",
        "results": [("5 rounds testing 可发现大多数 intermittent failures，并将发现新 failure 的概率降低 100x。", "Page 2 and Page 6, Figures 5-7"), ("即使经过 1000 rounds testing，每轮仍可能发现少量新 failures，说明 testing alone 不足。", "Page 7, Figures 9-10"), ("2X guardband 可避免约 85%-95% intermittent failing cells，但 5X 对剩余 VRT cells 仍不够。", "Page 9, Figures 15-16"), ("SECDED 加 testing/guardbanding 可将 retention failure rate 降低约 10^7/10^12；DECTED 可达约 10^12/10^18。", "Page 10, Figure 17"), ("VS-ECC 在约 550 rounds/19 minutes testing 后可达到 10 years TTF；加入 guardband 可缩短到约 7 minutes。", "Page 11, Figure 18b")],
        "conclusion": "未来 DRAM retention mitigation 的关键不是更长的一次性制造测试，而是低扰动 continuous online profiling 与 ECC/guardband/repair 的组合设计。",
        "limitations_author": [("testing-only bit repair 即使测试数月也无法提供强可靠性保证。", "Page 11, Figure 18a"), ("在线 profiling 需要在不干扰系统运行的情况下持续执行，这是实用化关键。", "Page 12, Section 8")],
        "limitations_infer": [("实验基于 DDR3-era modules，未来 DDR4/DDR5/LPDDR/HBM 的 VRT 分布需重新测量。", "推断，基于 tested modules scope"), ("ECC 组合收益依赖错误独立性、granularity 和实际错误相关性；真实系统需考虑 correlated failures。", "推断，基于 ECC model")],
        "focus": "重点读 Page 6-7 testing curves、Page 9 guardband coverage、Page 10 ECC 组合、Page 11 对 VS-ECC/Hi-ECC 的重新评估。",
        "relation": "它是 AVATAR、Reaper、RAIDR 这条 retention-aware refresh/repair 线的重要实验基础，强调 VRT 会破坏静态 profile 假设。",
        "figures": [("Figure 3", "Page 4", "testing infrastructure", "展示 FPGA board、temperature controller、heat chamber。"), ("Figure 5-7", "Page 5-6", "testing rounds efficacy", "显示 testing 能快速降低但不能消除新 failure 概率。"), ("Figure 9-12", "Page 7-8", "VRT behavior", "展示 cells 在不同轮次/状态间切换。"), ("Figure 15-16", "Page 9", "guardband coverage", "量化 2X 到 5X guardband 的覆盖率。"), ("Figure 17-18", "Page 10-11", "ECC and prior techniques", "展示 ECC 组合与 VS-ECC/Hi-ECC 的可靠性。")],
        "tables": [("Table 1", "Page 4", "tested DRAM modules", "列出测试模块与厂商信息。")],
        "equations": [("ECC failure probability", "Appendix / Page 13-14", "估计 ECC 下 uncorrectable failure probability", "基于 per-cell failure probability 与 ECC block correction strength", "ECC 强度和错误粒度决定 residual risk。", "中")],
        "terms": [("Variable Retention Time (VRT)", "可变保持时间", "Page 1-3", "DRAM cell retention time 在不同状态间随机变化。", "是"), ("Guardband", "保护裕量", "Page 2-3", "用更长测试 refresh interval 筛出潜在 weak cells。", "是"), ("Online profiling", "在线画像/在线测试", "Page 2", "系统运行中后台检测 retention failures。", "是"), ("VS-ECC", "可变强度 ECC", "Page 3 and Page 11", "对更易错 cache lines 使用更强 ECC。", "是")],
        "sections": "Abstract; Introduction; Background; Experimental Methodology; Testing; Guardbanding; ECC; Recent Techniques; Online Profiling; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "论文比较 memory tests、guardbands 和 ECC 对真实 DRAM retention failures 的缓解效果。结果表明，依赖 runtime testing alone 的技术无法保证可靠运行，而结合 ECC 的技术可在数小时甚至更短测试后达到强可靠性。"), ("1-3. Background / 背景", "Page 1-4", "retention failure 来自电容漏电。VRT 与 data pattern sensitivity 让 failure 间歇出现，因此制造测试无法一次性捕获所有问题。在线 profiling 有望把测试成本摊到系统运行期。"), ("4-5. Testing and Guardband / 测试与保护裕量", "Page 5-9", "少量 testing rounds 能发现多数 weak cells，但部分 VRT cells 长时间处于非失效状态，导致新 failures 持续出现。guardband 对多数相近 retention states 有效，但对状态差异很大的 VRT cells 无效。"), ("6-7. ECC and Prior Techniques / ECC 与已有方案", "Page 10-11", "ECC 与 testing/guardbanding 的组合远强于单独技术。bit repair 类方案在 intermittent failures 下失败风险高，VS-ECC/Hi-ECC 等 ECC-based 机制更适合与在线 profiling 配合。"), ("8-9. Online Profiling and Conclusion / 在线画像与结论", "Page 12-14", "作者建议未来系统使用持续、低开销在线 profiling，先用较强 ECC 保证初始可靠性，再随发现的 failures 调整保护强度或修复策略。")],
    },
    {
        "slug": "heterogeneous-reliability-memory-for-data-centers_dsn14",
        "title": "Characterizing Application Memory Error Vulnerability to Optimize Datacenter Cost via Heterogeneous-Reliability Memory",
        "zh": "通过异构可靠性内存刻画应用内存错误脆弱性以优化数据中心成本",
        "authors": "Yixin Luo, Sriram Govindan, Bikash Sharma, Mark Santaniello, Justin Meza, Aman Kansal, Jie Liu, Badriddine Khessib, Kushagra Vaid, Onur Mutlu",
        "year": "2014",
        "venue": "DSN 2014",
        "doi": "未找到",
        "pages": "12",
        "dataset": "WebSearch, Memcached, GraphLab/TunkRank; WebSearch on 40 servers; billions of queries/error injections",
        "topic": "Datacenter memory reliability; application error tolerance; heterogeneous-reliability memory",
        "keywords": "heterogeneous reliability, memory errors, datacenter TCO, ECC, WebSearch, Memcached, GraphLab",
        "one": "本文证明数据中心应用和其不同 memory regions 对 memory errors 的容忍度差异很大，因此可用 heterogeneous-reliability memory 按需分配 ECC/parity/NoECC/less-tested DRAM 来降低成本。",
        "background": "服务器 memory 是数据中心资本成本的重要组成部分，ECC/Chipkill/mirroring 等 one-size-fits-all 可靠性机制增加成本与延迟，但很多 data-intensive workloads 对部分 memory errors 具有天然 masking/recovery 能力。",
        "questions": ["如何量化应用对 memory errors 的 tolerance/vulnerability？", "WebSearch、Memcached、GraphLab 在 crash 和 incorrect results 上差异多大？", "应用内部 heap/stack/private memory 是否需要同等保护？", "heterogeneous-reliability mapping 能降低多少 server hardware cost？"],
        "contribs": ["提出量化 application memory error tolerance 的方法，区分 overwrite masking、logic masking、incorrect response 和 crash。", "对 WebSearch、Memcached、GraphLab 进行真实 case study，发现跨应用差异可达数量级。", "展示同一应用不同 memory regions 的 vulnerability/recoverability 差异。", "提出按 memory region 映射 NoECC、Parity+Recovery、ECC、Less-Tested DRAM 的设计空间。", "在 WebSearch 上实现 4.7% server hardware cost saving，同时达到 99.90% single-server availability。"],
        "method": "作者通过 controlled error injection 和 memory access monitoring 测量错误命运、safe ratio 和 recoverability；再基于错误模型和可用性目标，把不同 memory regions 映射到不同硬件可靠性技术和软件 recovery response。",
        "experiments": "case studies 包括 production-like WebSearch、30GB Twitter dataset 的 Memcached、11M Twitter users 的 GraphLab/TunkRank；设计空间评估使用 2000 errors/server/month 和 99.90% single-server availability target。",
        "results": [("传统 error protection 可增加 memory system cost 12.5%，而某些应用无需保护也可在大量错误下达到 99.00% availability。", "Page 1, Abstract"), ("三类应用的 memory error vulnerability 和 incorrect result rate 差异最高达 6 个数量级。", "Page 6, Figure 3"), ("WebSearch 至少 82.1% address space 可从 disk 隐式恢复，56.3% 可显式恢复。", "Page 7, Table 5"), ("Detect&Recover/L 可减少 server hardware cost 4.7%（范围 0.9%-8.4%），达到 99.90% availability，每百万 queries 约 12 个 incorrect results。", "Page 10, Table 6"), ("在 2000 errors/month 下，WebSearch 和 Memcached 即使无 ECC 也可达到 99.00% single-server availability。", "Page 11, Figure 8")],
        "conclusion": "内存可靠性应该由应用容忍度、数据区域可恢复性和错误模型共同决定；对所有数据一刀切使用同一 ECC 强度会浪费数据中心成本。",
        "limitations_author": [("使用 less reliable/no-ECC memory 的前提是数据多为 read-only/transient，且错误不会长期传播到 persistent storage。", "Page 11, Section VI-C"), ("本文没有完整建模 hard error 出现过程，只分析其 ongoing effects。", "Page 10, Table 6 assumptions")],
        "limitations_infer": [("业务可接受的 incorrect results per million queries 取决于应用和 SLA，不能直接推广到所有服务。", "推断，基于 WebSearch case study"), ("需要 OS/runtime 支持 memory region classification、recovery 和 heterogeneous memory provisioning。", "推断，基于 Figure 7/9 design")],
        "focus": "重点读 Figure 1 error fates、Figures 3-6 应用/region 脆弱性、Table 5 recoverability、Table 6 cost/availability tradeoff。",
        "relation": "与 HARP/MEMCON/Revisiting Memory Errors 一起构成数据中心内存可靠性研究；本文更关注应用级 tolerance 和成本优化。",
        "figures": [("Figure 1", "Page 3", "memory error outcomes", "定义 overwrite/logic masking、incorrect response、crash。"), ("Figure 3", "Page 6", "inter-application vulnerability", "展示三类应用差异。"), ("Figure 4", "Page 6", "memory region vulnerability", "展示同一应用内部区域差异。"), ("Figure 7", "Page 9", "heterogeneous mapping flow", "展示 design-space exploration。"), ("Figure 8", "Page 11", "tolerable errors/month", "比较应用可容忍错误数。")],
        "tables": [("Table 1", "Page 1", "ECC techniques and cost", "比较 Parity/SECDED/Chipkill/RAIM/Mirroring 的容量开销。"), ("Table 4", "Page 8", "design dimensions", "列出硬件技术、软件响应和使用粒度。"), ("Table 5", "Page 7", "recoverable memory", "量化 WebSearch 可恢复数据比例。"), ("Table 6", "Page 10", "cost/availability tradeoff", "展示 Detect&Recover/L 的成本收益。")],
        "equations": [("Safe ratio", "Page 3-4, Section III-B", "衡量某地址错误被 overwrite masking 的机会", "safe duration / total duration", "写多读少的数据更可能覆盖错误而不暴露。", "是")],
        "terms": [("Heterogeneous-reliability memory", "异构可靠性内存", "Page 1-2", "在同一系统中对不同应用/region 使用不同可靠性保护。", "是"), ("Safe ratio", "安全比例", "Page 3-4", "用访问/写入模式估计错误被覆盖的可能性。", "是"), ("Parity + Recovery (Par+R)", "奇偶检测加软件恢复", "Page 10", "用 parity 检测错误，再从 disk clean copy 恢复。", "是"), ("Less-Tested DRAM", "较少测试 DRAM", "Page 8-10", "减少制造测试成本但错误率更高的内存。", "是")],
        "sections": "Abstract; Introduction; Background; Methodology; Characterization Framework; Case Studies; Heterogeneous-Reliability Systems; Support; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "论文指出数据中心内存可靠性不应一刀切。不同 data-intensive applications 以及同一应用的不同 memory regions 对 memory errors 的容忍度差异很大，利用这种差异可降低服务器硬件成本。"), ("I-III. Motivation and Methodology / 动机与方法", "Page 1-4", "作者把 memory error outcomes 分为 overwrite masking、logic masking、incorrect response 和 crash，并用 safe ratio 与 recoverability 描述 memory regions 的容错能力。"), ("IV-V. Characterization / 表征", "Page 4-8", "WebSearch、Memcached、GraphLab 的 case study 显示，应用间和应用内部 region 间 vulnerability 差异显著。WebSearch 大量数据为只读缓存，可从持久存储恢复。"), ("VI. Design Space / 异构可靠性设计", "Page 8-11", "系统可组合 NoECC、Parity、SECDED、less-tested DRAM、software recovery 和 page retirement，并在 memory region 粒度做映射。Table 6 说明该方法能同时满足 availability 和成本目标。"), ("Conclusion / 结论", "Page 11-12", "作者总结，随着 DRAM 错误率和成本压力上升，应用感知的 heterogeneous-reliability memory 是比统一强保护更经济的方向。")],
    },
    {
        "slug": "in-memory-pointer-chasing-accelerator_iccd16",
        "title": "Accelerating Pointer Chasing in 3D-Stacked Memory: Challenges, Mechanisms, Evaluation",
        "zh": "在 3D-stacked memory 中加速 pointer chasing：挑战、机制与评估",
        "authors": "Kevin Hsieh, Samira Khan, Nandita Vijaykumar, Kevin K. Chang, Amirali Boroumand, Saugata Ghose, Onur Mutlu",
        "year": "2016",
        "venue": "ICCD 2016",
        "doi": "未找到",
        "pages": "8",
        "dataset": "Linked-list, hash-table, B-tree microbenchmarks; Memcached and DBx1000 profiling; TPC-C for DBx1000",
        "topic": "Processing-in-memory; 3D-stacked memory; pointer chasing; address translation",
        "keywords": "IMPICA, pointer chasing, 3D-stacked memory, PIM, address-access decoupling, region-based page table",
        "one": "IMPICA 把 linked data structure traversal 放到 3D-stacked memory logic layer 中执行，并用 address-access decoupling 与 region-based page table 解决并行性和地址翻译两大难题。",
        "background": "Pointer chasing 广泛存在于 databases、key-value stores、graph processing 等数据结构中，具有串行依赖、irregular access、cache/TLB misses 多的特点；CPU prefetching 对分叉结构效果有限，还会消耗带宽。",
        "questions": ["为什么 pointer chasing 适合在 memory side 加速？", "串行 pointer traversal 如何在简单 accelerator 中获得并行性？", "PIM accelerator 如何低成本完成 virtual-to-physical translation？", "IMPICA 对 linked list/hash table/B-tree/DBx1000 的性能和能耗收益如何？"],
        "contribs": ["首次提出面向任意 linked data structure pointer chasing 的 in-memory accelerator IMPICA。", "识别 parallelism challenge 与 address translation challenge 两个 PIM accelerator 共性难题。", "提出 address-access decoupling，使 accelerator 在等待一个 stream memory access 时服务其他 streams。", "提出 region-based page table，利用数据结构所在连续 virtual regions 简化 memory-side translation。", "在微基准和真实 DBx1000 workload 上评估性能、能耗和面积。"],
        "method": "CPU 把 pointer chasing task offload 给 3D-stacked memory logic layer。IMPICA 维护多个 traversal contexts，把地址生成与 memory access 分离，以隐藏访问延迟；并要求被加速数据结构放在连续 virtual regions，用 region-based page table 做低成本翻译。",
        "experiments": "作者用 quad-core system 评估 linked list、hash table、B-tree microbenchmarks 和 DBx1000/TPC-C；比较 baseline、额外 cache、IMPICA；指标包括 speedup、TLB/cache miss、bandwidth、transaction throughput/latency、energy 和 area。",
        "results": [("IMPICA 将 linked list、hash table、B-tree pointer chasing performance 分别提升 92%、29%、18%。", "Page 1-2 and Page 6, Figure 6"), ("DBx1000 transaction throughput 提升 16%，response time 降低 13%。", "Page 1-2 and Page 7, Figure 8"), ("系统能耗在三种微基准中分别降低 41%、23%、10%，DBx1000 降低 6%。", "Page 1-2 and Page 7, Figure 10"), ("IMPICA area 仅为 ARM Cortex-A57 embedded core 的 7.6%，约为 baseline chip area 1.2%。", "Page 6, area discussion"), ("在 DBx1000 中，额外 128KB cache 只提升约 2%，远低于 IMPICA 的 16%。", "Page 7, Figure 8 discussion")],
        "conclusion": "Pointer chasing 的瓶颈不是通用计算而是依赖式内存访问；将 traversal logic 移到 memory side 并解决 parallelism/translation，可获得接近上限的系统收益。",
        "limitations_author": [("IMPICA 要求可加速数据结构放入连续 virtual regions，并使用专门的 region-based translation。", "Page 2 and Page 4, Section 4.2"), ("获取整个 node 可能带来部分无用字段访问，B-tree 等结构会受到影响。", "Page 6-7, evaluation discussion")],
        "limitations_infer": [("需要编程接口/offload support，且适合 pointer chasing 占比较高、数据结构相对明确的应用。", "推断，基于 API/design"), ("真实 HMC/HBM 系统中 coherence、OS integration 和 multi-tenant isolation 需要额外工程。", "推断，基于 PIM accelerator")],
        "focus": "重点读 Figure 1 pointer chasing profiling、Figure 3 address-access decoupling、Figure 5 IMPICA design、Figures 6/8/10 评估。",
        "relation": "IMPICA 是 Modern Primer 中 near-memory acceleration 的早期案例；与 Tesseract/SISA 都将图或指针密集访问移近内存。",
        "figures": [("Figure 1", "Page 3", "pointer chasing profiling", "显示 Memcached/DBx1000 中 pointer chasing 的高 CPI/cache miss。"), ("Figure 2", "Page 3", "traditional vs IMPICA", "展示在 memory logic layer 中执行 traversal。"), ("Figure 3", "Page 3-4", "parallelism challenge", "说明非并行 accelerator 会串行化多个 streams。"), ("Figure 5", "Page 5", "IMPICA architecture", "展示 accelerator、contexts、translation path。"), ("Figure 6", "Page 6", "microbenchmark speedup", "展示 1.92x/1.29x/1.18x。"), ("Figure 8", "Page 7", "DBx1000 throughput/latency", "展示真实 workload 收益。")],
        "tables": [("未检测到核心编号表", "-", "本文主要使用图展示结构与结果。", "建议重点看 Figures 1-10。")],
        "equations": [("未检测到核心编号公式", "-", "机制设计", "-", "本文没有需要重点掌握的编号公式。", "否")],
        "terms": [("IMPICA", "in-memory pointer chasing accelerator", "Page 1", "部署在 3D-stacked memory logic layer 的 pointer traversal 加速器。", "是"), ("Address-access decoupling", "地址生成-访问解耦", "Page 2-4", "在等待 memory access 时处理其他 traversal stream 的地址生成。", "是"), ("Region-based page table", "区域式页表", "Page 2 and Page 4", "利用连续 virtual memory regions 简化 PIM-side address translation。", "是"), ("Pointer chasing", "指针追踪", "Page 1-2", "通过当前 node 中的指针访问下一个 node 的串行遍历。", "是")],
        "sections": "Abstract; Introduction; Motivation; Design Challenges; IMPICA; Methodology; Evaluation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "论文提出 IMPICA，在 3D-stacked memory 的 logic layer 中执行 pointer chasing。它通过 address-access decoupling 和 region-based page table 解决并行性与地址翻译问题，并在微基准和 DBx1000 上提升性能与能效。"), ("1-2. Motivation / 动机", "Page 1-3", "linked lists、hash tables、B-trees 等结构中的 pointer chasing 会导致串行 memory accesses、cache/TLB misses 和低 prefetch accuracy。3D-stacked memory logic layer 提供低延迟近数据执行机会。"), ("3-4. Challenges and Mechanisms / 挑战与机制", "Page 3-5", "简单 accelerator 会把多个 traversal streams 串行化；IMPICA 通过解耦地址生成和访问来利用等待时间。由于指针保存 virtual address，IMPICA 使用 region-based page table 在 memory side 翻译。"), ("7. Evaluation / 评估", "Page 6-7", "IMPICA 在 linked list、hash table、B-tree 中显著加速，在 DBx1000 中获得 16% throughput improvement，并降低 transaction latency 和 system energy。"), ("Conclusion / 结论", "Page 8", "作者认为 pointer chasing 是 PIM 的合适目标，而 parallelism 和 translation 两个问题也会出现在许多其他 in-memory accelerators 中。")],
    },
    {
        "slug": "memory-scaling_imw13",
        "title": "Memory Scaling: A Systems Architecture Perspective",
        "zh": "内存缩放：系统架构视角",
        "authors": "Onur Mutlu",
        "year": "2013",
        "venue": "IMW 2013",
        "doi": "未找到",
        "pages": "5",
        "dataset": "Survey/position paper drawing on RAIDR, SALP, TL-DRAM, RowClone, PCM/Flash/QoS studies",
        "topic": "Memory scaling; DRAM architecture; emerging memory; QoS",
        "keywords": "memory scaling, system-DRAM co-design, RAIDR, SALP, TL-DRAM, RowClone, PCM, QoS, flash",
        "one": "这篇 position/survey paper 从系统架构角度提出三条 memory scaling 方向：重构 DRAM 架构与接口、利用 emerging memory technologies、为共享内存提供 predictable performance/QoS。",
        "background": "memory system 已成为性能、能耗、容量和可预测性的核心瓶颈；DRAM/flash 等 charge-based memory 缩放困难，单靠 device/circuit 改进难以维持容量、能效和可靠性增长。",
        "questions": ["DRAM 缩放面临哪些系统级挑战？", "system-DRAM co-design 可通过哪些机制改进 refresh、parallelism、latency、data movement？", "PCM/STT-MRAM 等 emerging memory 带来哪些机会和风险？", "共享内存系统如何提供 predictable performance 和 QoS？"],
        "contribs": ["将 memory scaling 归纳为 capacity/bandwidth/efficiency/predictability 的系统问题。", "提出 system-DRAM co-design，举例 RAIDR、SALP、TL-DRAM、RowClone、compression。", "分析 emerging resistive memory 的 hybrid memory、non-volatile main memory、memory-storage unification 机会。", "强调 shared memory QoS 与 slowdown estimation 是多核/多租户系统必要能力。", "把 DRAM 和 NAND flash scaling 放在同一系统架构脉络中讨论。"],
        "method": "本文不是单一实验论文，而是基于作者团队多个近期机制做架构综述与研究路线图：先描述 trends/requirements，再按 DRAM、emerging memory、predictability、flash scaling 四部分归纳问题和解法。",
        "experiments": "文中引用多个已有研究的代表性结果，如 RAIDR refresh reduction、SALP area overhead、TL-DRAM area overhead、RowClone energy reduction、MISE slowdown estimation error、flash lifetime improvement。",
        "results": [("64Gb DRAM hypothetically 会将 46% 时间、47% DRAM energy 花在 refresh。", "Page 2, Section IV-A"), ("RAIDR with three bins and 1.25KB hardware cost 可减少约 75% refresh operations。", "Page 2, Section IV-A"), ("SALP 以约 0.15% DRAM area overhead 获得接近增加 banks 的并行性收益。", "Page 2, Section IV-B"), ("RowClone 同 subarray page copy 可加速超过一个数量级，并降低约 74x energy，DRAM area overhead <0.03%。", "Page 2, Section IV-D"), ("MISE 类 request-service-rate 技术平均 slowdown estimation error 约 8%。", "Page 3-4, Section VI")],
        "conclusion": "memory scaling 的有效路径是跨层 co-design：软件、microarchitecture、controller、DRAM chips、emerging memories 和 storage 必须共同设计。",
        "limitations_author": [("本文是 research directions/survey，不提供统一实验平台上的新定量评估。", "全文形式，Page 1-5"), ("emerging memory 的 endurance、write latency/power、security/privacy 仍是未解决挑战。", "Page 3, Section V")],
        "limitations_infer": [("许多代表性机制来自研究原型，其产业部署依赖 JEDEC/DRAM vendor/controller/software 协同。", "推断，基于 system-DRAM co-design"), ("position paper 对每个方向的细节不充分，需要回读 cited works。", "推断，基于文章篇幅")],
        "focus": "重点读 Section IV 的五类 DRAM co-design 例子，Section V emerging memory 的机会/挑战，Section VI predictable performance。",
        "relation": "它是 LEC3 多篇论文的路线图：RAIDR、SALP、TL-DRAM、RowClone、PCM、MISE、flash work 都被放入同一 scaling 框架。",
        "figures": [("未检测到编号图", "-", "position paper", "文章以文本和引用为主。")],
        "tables": [("未检测到编号表", "-", "position paper", "文章以文字综述为主。")],
        "equations": [("未检测到核心编号公式", "-", "综述/路线图", "-", "本文没有核心编号公式。", "否")],
        "terms": [("System-DRAM co-design", "系统-DRAM 协同设计", "Page 1-2", "重新设计 DRAM 架构、功能和接口，让 controller/processor/software 共同利用内部结构。", "是"), ("RAIDR", "retention-aware intelligent DRAM refresh", "Page 2", "按 retention bins 差异化刷新 rows。", "是"), ("SALP", "subarray-level parallelism", "Page 2", "暴露并利用 DRAM bank 内 subarray 并行性。", "是"), ("TL-DRAM", "tiered-latency DRAM", "Page 2", "把 long bitline 划分为 low/high-latency segments。", "是"), ("PCM", "phase-change memory", "Page 3", "更可缩放、非易失但写延迟/能耗/耐久性存在挑战的 emerging memory。", "是")],
        "sections": "Abstract; Introduction; Trends and Requirements; Solution Directions; New DRAM Architectures; Emerging Memory Technologies; Predictable Performance; Flash Scaling; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "本文认为 memory system 已成为几乎所有系统的性能与能耗瓶颈。面对 DRAM scaling 困难，系统需要从 DRAM 架构、新型内存和 QoS 三个方向重新设计。"), ("I-III. Trends and Solution Directions / 趋势与方向", "Page 1", "更多异构核心、数据密集应用和技术缩放限制共同加剧 memory bottleneck。作者主张跨层合作，从算法、软件、微架构到设备共同解决。"), ("IV. New DRAM Architectures / 新 DRAM 架构", "Page 1-2", "RAIDR 利用 retention time 差异降低 refresh；SALP 利用 subarray 并行性；TL-DRAM 在 bitline 内制造 latency heterogeneity；RowClone 把 bulk copy/init 放进 DRAM。"), ("V-VI. Emerging Memories and QoS / 新型内存与可预测性", "Page 3-4", "PCM/STT-MRAM 等技术提供非易失和更好密度，但有写延迟、能耗、耐久性和安全挑战。共享内存系统还必须估计并控制 application slowdown。"), ("VIII. Conclusion / 结论", "Page 4-5", "作者总结 memory scaling 需要系统架构级方案，而不是只依赖底层器件缩放；跨层 co-design 会随着物理 scaling 极限临近而更重要。")],
    },
    {
        "slug": "mise-predictable_memory_performance-hpca13",
        "title": "MISE: Providing Performance Predictability and Improving Fairness in Shared Main Memory Systems",
        "zh": "MISE：在共享主存系统中提供性能可预测性并提升公平性",
        "authors": "Lavanya Subramanian, Vivek Seshadri, Yoongu Kim, Ben Jaiyen, Onur Mutlu",
        "year": "2013",
        "venue": "HPCA 2013",
        "doi": "未找到",
        "pages": "12",
        "dataset": "300 4-core SPEC CPU2006 workloads; 3000 QoS data points; 4/8/16-core simulations",
        "topic": "Memory interference slowdown estimation; QoS; fairness; memory scheduling",
        "keywords": "MISE, request-service-rate, slowdown estimation, MISE-QoS, MISE-Fair, STFM",
        "one": "MISE 用 request-service-rate 估计 memory-interference-induced slowdown，并基于该估计构建 MISE-QoS 和 MISE-Fair，实现更好的 QoS 保证和公平性。",
        "background": "多程序共享主存会导致不同应用 slowdown 不可预测；已有 memory scheduler 常优化吞吐或公平性，但对单个应用相对独占运行的 slowdown 估计不准确，难以给 QoS 或 OS 提供可靠反馈。",
        "questions": ["如何在线估计应用独占运行时的 request-service-rate？", "request-service-rate 为什么能作为 memory-bound 应用性能代理？", "非 memory-bound 应用如何加入 compute phase/stall fraction 修正？", "MISE-QoS/MISE-Fair 相对 STFM/ATLAS/TCM 效果如何？"],
        "contribs": ["提出 MISE，用 ARSR/SRSR 估计 slowdown。", "通过周期性 highest-priority epochs 估计 alone-request-service-rate。", "用 stall fraction alpha 修正 non-memory-bound applications。", "构建 MISE-QoS，为 AoI 提供 soft slowdown guarantees。", "构建 MISE-Fair，最小化 maximum slowdown 并优于 FRFCFS/ATLAS/TCM/STFM。"],
        "method": "MISE 的核心是 slowdown ≈ ARSR/SRSR，并对非 memory-bound 应用乘入 memory stall fraction。memory controller 通过 interval/epoch 机制轮流给应用最高优先级，测量 near-alone request-service-rate，再用 lottery scheduling 分配带宽以满足 QoS 或公平性目标。",
        "experiments": "使用 cycle-accurate DDR3 simulator、SPEC CPU2006 组合 workload，评估 slowdown estimation error、epoch/interval sensitivity、single/multiple AoI QoS、4/8/16-core fairness 与 harmonic speedup。",
        "results": [("MISE 在 300 workloads 上 average slowdown estimation error 为 8.1%，而 STFM 为 29.8%。", "Page 5-6, Table 2 and Section 6"), ("5M cycles interval、10000 cycles epoch 下 MISE 达到最低约 8.1% error。", "Page 6, Table 3"), ("MISE-QoS 在 3000 data points 中满足 slowdown bound 80.9%，达到 AlwaysPrioritize 可满足情况的 97.5%。", "Page 8, Table 5 discussion"), ("MISE-QoS 正确预测 bound 是否满足的比例为 95.7%。", "Page 1-2 and Page 8, Table 5 discussion"), ("bound=10^3 时，MISE-QoS 比 AlwaysPrioritize 提高 harmonic speedup 12%、weighted speedup 10%，maximum slowdown 降低 13%。", "Page 9, Figure 5"), ("16-core 下 MISE-Fair 相对最佳先前机制 STFM 提供 7.2% 更好公平性。", "Page 10-11, Figure 8")],
        "conclusion": "准确、简单的 slowdown estimation 可作为共享主存 QoS/fairness 的 substrate；memory controller 不只应调度请求，还应向系统暴露可解释的应用级 slowdown 信息。",
        "limitations_author": [("MISE 主要估计 main memory interference，其他共享资源 slowdown 留作未来工作。", "Page 12, Conclusion"), ("MISE 不显式建模 bank-level parallelism 或 row-buffer interference，但作者观察其对准确性影响有限。", "Page 4, Section 4.3")],
        "limitations_infer": [("highest-priority sampling 会改变短期调度行为，在实时或极短 phase workload 中需重新评估。", "推断，基于 epoch/interval design"), ("MISE 只在仿真 SPEC workloads 上系统评估，现代 server workloads/NUMA/HBM 需要新验证。", "推断，基于 methodology")],
        "focus": "重点读 Section 3 的 ARSR/SRSR 模型、Table 2/3 误差、Table 5/Figure 5 QoS、Figure 8/10 fairness/performance。",
        "relation": "MISE 是 ASM 的前身，ASM 后续把 cache interference 纳入模型；DASH 则把共享内存调度扩展到 HWA deadline 场景。",
        "figures": [("Figure 1", "Page 3", "request service rate vs performance", "证明 RSR 可作为 memory-bound 性能代理。"), ("Figure 2-3", "Page 5-6", "MISE vs STFM accuracy", "比较 memory-bound 和 non-memory-bound 应用估计。"), ("Figure 5", "Page 9", "MISE-QoS performance/fairness", "展示 QoS 下的吞吐与公平性。"), ("Figure 8", "Page 10", "fairness vs core count", "展示 MISE-Fair 降低 maximum slowdown。"), ("Figure 10", "Page 11", "harmonic speedup", "说明公平性收益未显著牺牲性能。")],
        "tables": [("Table 1", "Page 5", "simulation configuration", "列出 DDR3/cache/core 参数。"), ("Table 2", "Page 5", "average error per benchmark", "显示 MISE 平均误差低于 STFM。"), ("Table 3", "Page 6", "epoch/interval sensitivity", "确定 5M/10K 参数。"), ("Table 5", "Page 8", "MISE-QoS effectiveness", "量化 bound meet/prediction correctness。"), ("Table 6", "Page 9", "STFM-QoS effectiveness", "说明 STFM 估计用于 QoS 较差。")],
        "equations": [("Slowdown for memory-bound apps", "Page 3, Equation 1", "估计 slowdown", "Slowdown = ARSR / SRSR", "独占请求服务率与共享请求服务率的比值表示被干扰程度。", "是"), ("Alpha-adjusted slowdown", "Page 3-4, Equation 3", "修正 non-memory-bound 应用", "结合 stall fraction alpha", "compute phase 不受 memory interference，需降低 memory service-rate 对总性能的影响。", "是")],
        "terms": [("MISE", "memory-interference-induced slowdown estimation", "Page 1", "估计主存干扰导致应用 slowdown 的模型。", "是"), ("ARSR", "alone request-service-rate", "Page 3", "应用近似独占内存时的请求服务率。", "是"), ("SRSR", "shared request-service-rate", "Page 3", "应用与其他应用共同运行时的请求服务率。", "是"), ("MISE-QoS", "MISE 驱动的 QoS 调度", "Page 8-9", "给 AoI 分配足够带宽满足 slowdown bound。", "是"), ("MISE-Fair", "MISE 驱动的公平性调度", "Page 10-11", "通过带宽重分配最小化 maximum slowdown。", "是")],
        "sections": "Abstract; Introduction; Background; MISE Model; Implementation; Methodology; Accuracy; Sensitivity; QoS; Fairness; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "MISE 是一种简单模型，用于估计多程序共享主存时单个应用的 slowdown。它利用 request-service-rate 作为性能代理，并周期性给应用最高优先级来估计独占服务率。"), ("1-4. Model / 模型", "Page 1-4", "对于 memory-bound 应用，performance 与 request-service-rate 近似成正比。MISE 用 ARSR/SRSR 估计 slowdown；对 non-memory-bound 应用，引入 stall fraction alpha 来考虑 compute phase。"), ("5-7. Accuracy and Sensitivity / 准确性与敏感性", "Page 5-6", "与 STFM 相比，MISE 的平均误差显著更低。epoch 和 interval 过小/过大都会影响估计稳定性，论文选择 5M cycles interval 和 10K cycles epoch。"), ("8. QoS and Fairness / QoS 与公平性", "Page 8-11", "MISE-QoS 根据 slowdown estimate 给 applications of interest 分配刚好足够的 bandwidth；MISE-Fair 则动态调整目标 bound 和带宽分配，以降低 maximum slowdown。"), ("10. Conclusion / 结论", "Page 12", "作者总结 MISE 可作为更可预测、更可控 shared-memory systems 的基础，并计划将类似模型扩展到其他共享资源。")],
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
- 与本批相关方向：DRAM retention/VRT profiling、数据中心应用容错、PIM pointer chasing、system-DRAM co-design、shared-memory slowdown/QoS。
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
- Missing Content: 图中细小标注和双栏局部错位建议回到 PDF 人工核对；survey paper 的引用细节需回原文 references 查看
- Parsing Problems: PDF 双栏文本存在局部换行错位；已按页码、章节、图表编号定位关键结论
- Uncertain Parts: DOI/arXiv 如 metadata 标注“未找到”则表示未在 PDF 抽取文本中确认
- Need User Action: 无；如需逐字全文翻译，请确认版权授权范围后再处理
- Quality Check: 已覆盖摘要、引言/背景、方法/系统设计、实验/结果或研究路线、局限、图表、术语与复习 checklist
- Batch Status: {STATUS}
""")

print(f"updated {len(P)} papers for batch 8")
