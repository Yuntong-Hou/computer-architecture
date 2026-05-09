from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = "第九轮深度阅读完成"
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
        "slug": "panopticon",
        "title": "Panopticon: A Complete In-DRAM Rowhammer Mitigation",
        "zh": "Panopticon：完整的 in-DRAM RowHammer 缓解机制",
        "authors": "Tanj Bennett, Stefan Saroiu, Alec Wolman, Lucian Cojocar",
        "year": "2021",
        "venue": "未找到",
        "doi": "未找到",
        "code": "https://github.com/microsoft/Panopticon",
        "pages": "7",
        "dataset": "Design/security analysis for DDR4 in-DRAM RowHammer mitigation",
        "topic": "RowHammer mitigation; in-DRAM counters; DDR4 ALERTn",
        "keywords": "Panopticon, RowHammer, DDR4, ALERTn, in-DRAM counter, service queue, counter mat",
        "one": "Panopticon 将每行 activation counter 放入 DRAM 内部 counter mats，并复用 row decoder 与 DDR4 ALERTn 信号，以仅修改 DRAM 的方式实现完整 RowHammer 防御。",
        "background": "已有 RowHammer tracking/sampling/partitioning/clean-slate 方案要么需要大量 SRAM/CAM，要么依赖 memory controller、DRAM、OS 多方协作，难以部署；DDR4 仍受 multi-row RowHammer attacks 影响。",
        "questions": ["如何避免 Graphene/TWiCe/BlockHammer 等方案的大量 fast-memory 状态？", "DRAM 内部如何为每行维护 counter 而不拖慢普通访问？", "不修改 DDR4 controller/protocol 时，DRAM 如何请求时间刷新 victim rows？", "service queue 是否可能被攻击者填满或连续触发？"],
        "contribs": ["提出 complete in-DRAM RowHammer mitigation，DDR4 场景除 DRAM 外无需修改其他硬件。", "用 thin 16-bit counter mats 为每条 row 存储 counter，并复用 DRAM row decoding logic 做 lookup。", "用 threshold bit 替代完整阈值比较，避免昂贵 counter reset。", "用 service queue 记录需服务的 aggressor rows，并刷新潜在 victim rows。", "复用 DDR4 ALERTn 信号暂停 memory controller，为 mitigation 争取时间。"],
        "method": "Panopticon 在 DRAM bank 内增加 counter mats、incrementer/testing logic、service queue 和 ALERTn state machine。每次 ACTIVATE 同步更新对应 row counter；threshold bit toggle 时将 row address 入队；收到 REF 或队列需要服务时刷新邻近 victim rows，必要时 assert ALERTn 让 controller 暂停发命令。",
        "experiments": "论文主要进行 architecture/security analysis，而非完整系统性能评估；比较状态开销，分析 service queue 被连续占用或填满的攻击可行性，讨论 counter mats power/space overhead。",
        "results": [("Graphene 在 DDR4 每 channel 需 39.23KB CAM、每 CPU 约 156.9KB；BlockHammer/TWiCe 需求更高。", "Page 1-2, Table I"), ("Panopticon service queue 只需 8 entries/bank；DDR4 row address 18 bits 时约 144 bits/bank，远小于 Graphene 2511 bits/bank。", "Page 5, Section V-D"), ("Panopticon 用 threshold bit，如 b10 toggle 时每 1024 activations 入队一次，避免比较完整 counter value。", "Page 3-5, Figure 1/Figure 5"), ("安全分析显示若不能请求 controller 时间，攻击者可在较短时间内填满 service queue，因此 ALERTn 机制是必要条件。", "Page 5-6, Figures 6-7"), ("16-bit counter 可支持最高 65,536 activations threshold，适合现代较低 RowHammer threshold 场景。", "Page 6, Section VII-C")],
        "conclusion": "Panopticon 的核心价值是把 RowHammer 防御状态和 victim refresh 能力都放进 DRAM 内部，减少跨供应商协议变更；但它必须拥有向 controller 请求时间的机制。",
        "limitations_author": [("若没有 ALERTn 或类似方式请求额外时间，攻击者可通过填满 service queue 破坏安全性。", "Page 5-6, Figures 6-7"), ("counter mats 的实际 power/space overhead 需要 DRAM vendor 精确评估。", "Page 6, Section VII-C")],
        "limitations_infer": [("Panopticon 需要 DRAM 内部设计改动，仍依赖厂商采用和验证，且对 DDR5/HBM 需重新适配。", "推断，基于 in-DRAM architecture"), ("论文偏设计和安全分析，缺少基于完整 workload 的性能/能耗评估。", "推断，基于 evaluation scope")],
        "focus": "重点读 Table I 状态开销、Figure 1 threshold bit/service queue、Figures 4-5 counter mat/incrementer、Figures 6-7 queue attack 分析。",
        "relation": "Panopticon 与 DDR5 RFM/PRHT、PRAC/Graphene/TWiCe 构成 RowHammer 防御谱系：它更强调单 DRAM vendor 可独立部署。",
        "figures": [("Figure 1", "Page 3", "counter table and service queue", "展示 threshold bit toggle 如何入队。"), ("Figure 4", "Page 4", "counter mat layout", "展示 open-space staggered counter mats。"), ("Figure 5", "Page 5", "incrementer", "展示 counter increment/test logic。"), ("Figure 6", "Page 5", "consecutive tREFI attack", "分析连续刷新间隔入队攻击时间。"), ("Figure 7", "Page 6", "queue fill attack", "说明 queue 需要额外时间机制。")],
        "tables": [("Table I", "Page 2", "state size comparison", "Graphene/BlockHammer/TWiCe 的 per-bank/channel/CPU 状态成本。")],
        "equations": [("Threshold bit service rate", "Page 3", "counter 入队频率", "row serviced every 2^i activates", "只检测 bit toggle 即可触发服务，避免完整比较。", "是")],
        "terms": [("Panopticon", "in-DRAM RowHammer 防御", "Page 1", "在 DRAM 内部追踪 row activations 并刷新 victim rows 的完整机制。", "是"), ("ALERTn", "DDR4 错误提示信号", "Page 1 and Page 5", "被 Panopticon 复用来暂停 controller 命令流。", "是"), ("Counter mat", "计数器 mat", "Page 4", "与 data mat 共同布局的薄 counter 存储阵列。", "是"), ("Service queue", "服务队列", "Page 3-5", "保存达到 threshold 的 aggressor rows，等待刷新 victims。", "是")],
        "sections": "Abstract; Introduction; Prior Proposals; Panopticon Design; In-DRAM Architecture; Security Analysis; Discussion; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "Panopticon 是完整 in-DRAM RowHammer mitigation。它把 row counters 放在 DRAM 内部，用 row decoding logic 找到对应 counter，并在 DDR4 中复用 ALERTn 暂停 memory controller。"), ("I-II. Motivation / 动机", "Page 1-3", "已有方案存在快速存储开销和跨层部署障碍。Graphene、BlockHammer、TWiCe 等都需要大量状态，或要求 DRAM 暴露内部映射/支持新命令。"), ("III-V. Design / 设计", "Page 3-5", "Panopticon 为每行维护 counter，threshold bit toggle 时将 row 放入 service queue。counter mats 采用 open-space、staggered layout，避免改变现有 data mats/sense amplifiers。"), ("VI-VII. Security and Discussion / 安全分析与讨论", "Page 5-6", "如果只能利用 REF 间隙服务队列，攻击者可能制造连续入队或填满队列。因此 Panopticon 必须能通过 ALERTn 或类似机制向 controller 请求时间。"), ("VIII. Conclusion / 结论", "Page 6-7", "论文总结 Panopticon 以 DRAM 内部修改为主，绕开 controller/OS 协调难题，但部署仍取决于 DRAM 设计和 ALERTn 行为。")],
    },
    {
        "slug": "parbor-efficient-system-level-test-for-DRAM-failures_dsn16",
        "title": "PARBOR: An Efficient System-Level Technique to Detect Data-Dependent Failures in DRAM",
        "zh": "PARBOR：高效检测 DRAM data-dependent failures 的系统级技术",
        "authors": "Samira Khan, Donghyuk Lee, Onur Mutlu",
        "year": "2016",
        "venue": "DSN 2016",
        "doi": "未找到",
        "code": "https://github.com/CMU-SAFARI/PARBOR",
        "pages": "12",
        "dataset": "144 real DRAM chips from three major vendors; FPGA-based DRAM testing infrastructure",
        "topic": "DRAM testing; data-dependent failures; address scrambling; refresh optimization",
        "keywords": "PARBOR, data-dependent failure, neighbor cells, address scrambling, strongly coupled cells, DC-REF",
        "one": "PARBOR 通过递归并行定位 physical neighbor cells 在 system address space 中的位置，使系统级测试能在 DRAM 内部地址 scrambling 存在时发现 data-dependent failures。",
        "background": "许多 DRAM failures 依赖邻近 cells 的数据模式；但 DRAM vendor 内部会 scramble/remap system addresses，使相邻 system-level bits 不等于物理相邻 cells，导致系统级 worst-case pattern 测试失效。",
        "questions": ["如何在不知道 vendor 内部映射的情况下找到物理邻居 cell 的 system address？", "strongly coupled cells 如何将 O(n^2) 测试降到 O(n)？", "递归并行测试如何进一步减少测试数量？", "neighbor-aware patterns 相比 random patterns 多发现多少 failures？", "PARBOR 如何支持 DC-REF 降低 refresh？"],
        "contribs": ["提出第一个在地址 scrambling 存在时系统级定位 DRAM neighbor cells 的机制。", "利用 strongly coupled cells 和 regular internal DRAM organization 把测试复杂度从 naive O(n^2) 大幅降低。", "在 144 颗真实 DRAM chips 上只需 66-90 tests 即可定位邻近 cell 位置。", "相比 naive test 实现 745,654x 测试数减少，相比优化 O(n) test 减少约 90x。", "PARBOR 比 random-pattern test 平均多发现 21.9% failures，并支持 DC-REF。"],
        "method": "PARBOR 先找到 sample victim bits，再利用 strongly coupled cells 只需改变一个邻居即可触发 failure 的特性，递归地将候选地址空间分块并并行测试多行；根据 failure distance frequency 排名过滤 random failures，推断左右邻居在 system address space 中的距离。",
        "experiments": "作者用 FPGA infrastructure 测试 144 real DRAM chips，比较 PARBOR、random patterns、optimized/naive neighbor discovery；并在模拟器中评估 DC-REF 在 32Gbit DRAM、8-core、SPEC workloads 上的性能和 refresh reduction。",
        "results": [("naive exhaustively testing two neighbors in an 8K-cell row 需要约 49 days；三/四邻居将达 1115 years/9.1M years。", "Page 1, Introduction"), ("PARBOR 仅用 66-90 tests 定位 neighbor cell locations，相比 naive test 减少 745,654x。", "Page 1-2, Abstract/Contributions"), ("PARBOR 在 144 chips 上比 random-pattern test 平均多发现 21.9% failures。", "Page 1-2 and Page 8, Figure 12"), ("PARBOR 在每个 tested module 中多发现 1K 到 45K failures，总 detected failures 增加 2%-55%。", "Page 8, Figure 12 discussion"), ("DC-REF 将 refreshes 减少 73%，在 32Gbit DRAM/8-core 系统上提升性能 18%。", "Page 2 and Page 11, Figure 16")],
        "conclusion": "系统级 DRAM failure mitigation 必须理解物理邻接关系；PARBOR 说明即使 vendor 不公开 address mapping，仍可通过故障行为推断邻居位置并构建更有效测试。",
        "limitations_author": [("PARBOR 依赖 DRAM internal organization 的 regularity；remapped columns/cells 会降低覆盖率。", "Page 10, Section 7.3 Limitation"), ("sample size 太小会让 random failures 干扰 distance ranking。", "Page 10, Figure 15")],
        "limitations_infer": [("不同工艺世代、更强 redundancy/remapping 或 3D/HBM 组织可能改变 PARBOR 假设。", "推断，基于 address mapping regularity"), ("DC-REF 需要运行时监控 row data content 与 worst-case pattern，实际硬件开销需进一步实现验证。", "推断，基于 DC-REF design")],
        "focus": "重点读 Figure 1 address scrambling、Figure 2 strong/weak coupling、Section 5 PARBOR algorithm、Figure 12 detection improvement、Figure 16 DC-REF。",
        "relation": "PARBOR 与 retention/VRT 论文一样属于系统级 DRAM profiling，但它专注 data-dependent/coupling failures，并可补充 RAIDR 类 refresh optimization。",
        "figures": [("Figure 1", "Page 1", "address scrambling", "说明 system adjacency 与 physical adjacency 不一致。"), ("Figure 2", "Page 2", "strong vs weak coupling", "展示 PARBOR 降低复杂度的关键观察。"), ("Figure 5", "Page 4", "address scrambling example", "展示 DRAM internal buffering 导致地址重排。"), ("Figure 12", "Page 8", "new failures detected", "量化 PARBOR 多发现 failures。"), ("Figure 16", "Page 11", "DC-REF performance", "展示 data content-based refresh 收益。")],
        "tables": [("Table 2", "Page 11", "simulated system configuration", "列出 DC-REF performance evaluation 参数。")],
        "equations": [("Test complexity", "Page 1 and Appendix", "测试时间复杂度", "naive O(n^2), PARBOR recursive/parallel tests", "利用 strong coupling 和 regular mapping 将不可行测试变为可部署测试。", "是")],
        "terms": [("PARBOR", "Parallel Recursive neighBOR testing", "Page 2", "并行递归定位物理邻居 cell 地址的系统级测试。", "是"), ("Data-dependent failure", "数据依赖故障", "Page 1", "cell 是否失效依赖邻居 cells 数据模式。", "是"), ("Strongly coupled cell", "强耦合 cell", "Page 2", "只受一个邻居数据内容影响即可失败的 cell。", "是"), ("DC-REF", "data content-based refresh", "Page 2 and Page 11", "仅当弱 row 中出现 worst-case pattern 时高频刷新。", "是")],
        "sections": "Abstract; Introduction; Background; Challenges; Key Ideas; PARBOR; Evaluation; DC-REF; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "PARBOR 是系统级检测 DRAM data-dependent failures 的方法。它先确定物理邻近 cells 在 system address space 中的位置，再利用这些信息构造 neighbor-aware tests。"), ("1-4. Motivation and Key Ideas / 动机与关键思想", "Page 1-5", "DRAM 内部地址 scrambling 使相邻 system addresses 不能代表物理邻居。PARBOR 利用 strongly coupled cells 和 DRAM 映射 regularity，把原本不可行的 O(n^2) 邻居测试转化为少量递归并行测试。"), ("5-7. PARBOR and Evaluation / 方法与评估", "Page 5-10", "PARBOR 递归测试多个 rows，统计 failure-triggering distances 并过滤 random failures。真实 144 chips 结果显示只需 66-90 tests，且比 random patterns 多发现 21.9% failures。"), ("8. DC-REF Use Case / DC-REF 用例", "Page 10-11", "DC-REF 根据 row 当前数据是否匹配 worst-case pattern 决定是否高频刷新弱 rows。它相比传统 retention-aware refresh 进一步减少 refresh 并提升性能。"), ("10. Conclusion / 结论", "Page 11-12", "作者总结 PARBOR 为系统级 DRAM profiling 提供了缺失的物理邻接信息，可支撑后续可靠性、性能和能耗优化。")],
    },
    {
        "slug": "pcm_ieee_micro10",
        "title": "Phase-Change Technology and the Future of Main Memory",
        "zh": "相变技术与主存的未来",
        "authors": "Benjamin C. Lee, Ping Zhou, Jun Yang, Youtao Zhang, Bo Zhao, Engin Ipek, Onur Mutlu, Doug Burger",
        "year": "2010",
        "venue": "IEEE Micro 2010",
        "doi": "未找到",
        "code": "未找到",
        "pages": "11",
        "dataset": "Technology survey and architectural evaluation summarized from PCM main-memory studies",
        "topic": "Phase-change memory; scalable main memory; buffering; wear reduction",
        "keywords": "PCM, phase-change memory, DRAM alternative, row buffer, write coalescing, redundant bit-write removal, row shifting, segment swapping",
        "one": "这篇 IEEE Micro 文章解释 PCM 作为 DRAM 替代的机会与三大挑战，并展示 buffer organization、write reduction 和 wear leveling 如何让 PCM 性能/能耗/寿命接近可用。",
        "background": "DRAM beyond 40nm 缩放困难，而 PCM 依赖电流和热效应，可望继续缩放并提供非易失性；但 PCM 读写更慢、写能耗高、写入会磨损 cell。",
        "questions": ["PCM cell 如何通过 SET/RESET 相变存储信息？", "为什么 PCM 可缩放性好但访问延迟、能耗和 endurance 差？", "row buffer design 如何缩小 PCM 与 DRAM 的性能/能耗差距？", "redundant bit-write removal、row shifting、segment swapping 如何提升寿命？"],
        "contribs": ["以可读形式总结 PCM device/circuit 特性与 system implications。", "说明 multiple narrow row buffers 可将 PCM delay/energy 推近 DRAM baseline。", "解释 redundant bit-write removal 可过滤 71%-85% redundant bit writes。", "结合 bit-write removal、row shifting、segment swapping 使平均 PCM lifetime 达到 22 years。", "展示 PCM 总能耗可比 DRAM 低约 65%，性能惩罚平均约 5.7%。"],
        "method": "文章综合 device survey、architectural simulation 和 energy/endurance modeling，讨论四类架构技术：buffer sizing、row caching/write coalescing、write reduction、wear leveling。",
        "experiments": "以 memory-intensive benchmarks 为代表，比较 DRAM baseline、PCM baseline、buffered PCM、wear-reduced/leveled PCM；指标包括 delay、dynamic/total energy、ED2、redundant bit-write rate、lifetime。",
        "results": [("四个 512-byte buffers 是平均 delay/energy 的有效折中，可将 PCM delay/energy disadvantage 从 1.6x/2.2x 降到 1.1x/1.0x。", "Page 5, Figure 2 discussion"), ("effectively buffered PCM 下，超过一半 benchmarks 性能距离 DRAM 在 5% 内。", "Page 6, Figure 3 discussion"), ("40nm 时 PCM system energy 平均为 DRAM 的 61.3%，至少节省 22.1%、最高 68.7%。", "Page 6, scaling discussion"), ("SLC/MLC-2/MLC-4 中 85%/77%/71% bit writes 是 redundant。", "Page 7, wear reduction discussion"), ("redundant bit-write removal + row shifting + segment swapping 后，SLC/MLC-2/MLC-4 平均 lifetime 为 22/17/13 years。", "Page 8, Figure 5")],
        "conclusion": "PCM 不会自然替代 DRAM；只有当架构把写粒度、buffer locality 和 wear distribution 一起设计好，PCM 的可缩放性和非易失性才会转化为主存优势。",
        "limitations_author": [("PCM 仍有 long latencies、high write energy、finite endurance，必须依靠架构缓解。", "Page 1-3"), ("multilevel PCM 区分多 resistance levels 有较高延迟/复杂度，可能限制每 cell bits。", "Page 3")],
        "limitations_infer": [("文章基于早期 PCM prototypes 和模型，商业技术参数可能随年代变化。", "推断，基于 technology survey"), ("非易失主存的软件/一致性/安全模型只做展望，未完整解决。", "推断，基于 conclusion")],
        "focus": "重点读 Figure 1 PCM cell、Table 1 technology survey、Figures 2-3 buffering、Figures 4-5 endurance、Figures 6-7 energy。",
        "relation": "这是 PCM_ISCA09 的扩展解读版；与后续 hybrid memory/PCM main memory 研究共同构成 emerging memory 方向基础。",
        "figures": [("Figure 1", "Page 2", "PCM storage element/cell", "解释 heater/chalcogenide/BJT access device。"), ("Figure 2", "Page 5", "buffer organization Pareto", "展示 delay/energy 设计空间。"), ("Figure 4", "Page 7", "redundant bit-write removal and row shifting", "展示 wear reduction hardware。"), ("Figure 5", "Page 8", "PCM lifetime", "展示三种技术组合后的寿命。"), ("Figure 7", "Page 9", "total energy and ED2", "展示总体能效。")],
        "tables": [("Table 1", "Page 4", "technology survey", "汇总多个 PCM prototype 参数。")],
        "equations": [("PCM write energy", "Page 8", "写能耗模型", "Epcmwrite = Efixed + Eread + Ebitchange", "实际写能耗取决于固定开销、读旧值和变化 bit 数。", "是")],
        "terms": [("Phase-change memory (PCM)", "相变存储器", "Page 1", "通过 chalcogenide 在 crystalline/amorphous 状态间切换存储数据。", "是"), ("SET / RESET", "置位/复位相变写入", "Page 2-3", "SET 结晶降低电阻，RESET 非晶化提高电阻。", "是"), ("Redundant bit-write removal", "冗余 bit 写消除", "Page 7", "不写入与旧值相同的 bits，降低磨损和能耗。", "是"), ("Row shifting", "行内位移", "Page 7", "周期性移动 row 内写热点以均衡 wear。", "是")],
        "sections": "Overview; Technology and Challenges; PCM Characteristics; Architecting a DRAM Alternative; Mitigating Wear and Energy; Implications",
        "translation": [("Title and Overview / 标题与概览", "Page 1", "文章讨论 PCM 是否可成为未来主存。PCM 可缩放、非易失，但必须解决比 DRAM 更高的访问延迟、写功耗和磨损问题。"), ("Technology / 技术基础", "Page 1-4", "PCM cell 由 heater 与 chalcogenide 构成。RESET 用高短脉冲形成 amorphous 高阻态，SET 用较长脉冲形成 crystalline 低阻态。写入是主要 wear 来源。"), ("Architecting PCM / 架构设计", "Page 4-6", "通过把单个宽 buffer 改为多个窄 buffers，可减少写入粒度、提高 row locality 和 write coalescing，从而把 PCM delay/energy 接近 DRAM。"), ("Wear Reduction / 磨损降低", "Page 7-9", "redundant bit-write removal、row shifting 和 segment swapping 分别从 bit、row 和 segment 粒度减少并均衡写入，使 projected lifetime 达到多年到十多年。"), ("Implications / 启示", "Page 9-11", "PCM 的非易失性可能改变 memory hierarchy，但需要软件理解 persistence，并处理一致性、安全和磨损问题。")],
    },
    {
        "slug": "pcm_isca09",
        "title": "Architecting Phase Change Memory as a Scalable DRAM Alternative",
        "zh": "将相变存储器架构为可缩放 DRAM 替代方案",
        "authors": "Benjamin C. Lee, Engin Ipek, Onur Mutlu, Doug Burger",
        "year": "2009",
        "venue": "ISCA 2009",
        "doi": "未找到",
        "code": "未找到",
        "pages": "12",
        "dataset": "Technology survey; SESC simulation of memory-intensive workloads; PCM/DRAM timing and energy models",
        "topic": "Phase-change memory architecture; DRAM alternative; buffering; partial writes",
        "keywords": "PCM, phase-change memory, DRAM alternative, buffer organization, partial writes, endurance, scalability",
        "one": "这篇 ISCA 论文是 PCM 主存架构经典工作，提出 area-neutral buffer reorganization 与 partial writes，使 PCM 从 1.6x slower/2.2x energy 接近 DRAM，并把寿命提升到 5.6 years。",
        "background": "DRAM 缩放受 charge storage/control 限制，而 PCM 有更好缩放潜力和非易失性；问题是 PCM read/write latency 较高、write energy 很大、endurance 有限。",
        "questions": ["如何把 PCM prototype 参数映射到 DDR-style timing/energy model？", "buffer width/row count 如何影响 delay、energy、write coalescing？", "partial writes 如何提升 endurance？", "PCM scaling 是否在 40nm 后比 DRAM 更有能耗优势？"],
        "contribs": ["系统整理 PCM device/circuit prototypes 并导出 conservative technology parameters。", "提出 area-neutral PCM buffer organizations：narrow buffers 降低写能耗，多 rows 改善 locality/coalescing。", "证明 buffer reorganization 可将 execution time 从 1.6x DRAM 降至 1.2x，将 energy 从 2.2x 降至 1.0x。", "提出 partial writes，跟踪 cache-line/word dirty state，只写修改部分。", "用 endurance model 估计 buffered PCM + 4B partial writes 平均 lifetime 5.6 years。"],
        "method": "论文从 PCM SET/RESET/read/endurance 参数出发，建立 DDR-compatible timing/energy model；用 SESC 模拟 4-core CMP 和 memory-intensive workloads，探索 buffer width/row count Pareto frontier，并用 partial-write endurance equation 估计寿命。",
        "experiments": "比较 DRAM baseline、baseline PCM、不同 buffer organizations、64B/4B partial writes；指标包括 normalized delay、memory subsystem energy、array reads/writes、write coalescing、endurance、40nm energy scaling。",
        "results": [("baseline PCM system 比 DRAM 慢 1.6x、能耗高 2.2x。", "Page 1, Abstract"), ("narrow+multiple buffer reorganization 将 delay/energy gap 降到 1.2x/1.0x。", "Page 1 and Page 6, Figure 7"), ("四个 512B-wide buffers 将 delay penalty 从 1.60x 降至 1.16x，超过一半 benchmarks 距 DRAM 5% 内。", "Page 6, Figure 7 discussion"), ("40nm 时 PCM subsystem energy 约为 DRAM 的 61.3%，能耗节省 22.1%-68.7%。", "Page 7, Figure 7R discussion"), ("64B/4B partial writes 将 endurance 提升到 0.7/5.6 years；baseline lifetime 约 525 hours。", "Page 9, Figure 8 and Section 5.2")],
        "conclusion": "PCM 作为 DRAM 替代的可行性取决于体系结构是否能显式处理写能耗和 endurance；area-neutral buffering 与 partial writes 是关键第一步。",
        "limitations_author": [("PCM 技术仍处于 speculative/early prototype 状态，参数来自多篇 prototype survey。", "Page 2, Section 2"), ("5.6 years lifetime 仍依赖 effective wear-leveling；更细粒度 partial bit writes 需额外 shadow buffers/comparators。", "Page 9, Section 5.2")],
        "limitations_infer": [("论文未完整解决 PCM non-volatility 带来的 persistence consistency/security 问题。", "推断，基于 conclusion"), ("现代 NVM 技术与内存控制器已经演化，早期参数需谨慎迁移。", "推断，基于 2009-era technology")],
        "focus": "重点读 Table 1 PCM technology survey、Table 2 DDR timing/energy mapping、Figures 5-7 buffer design、Equation 3/Figure 8 endurance。",
        "relation": "这是 PCM_ieee_micro10 的核心技术来源，也与 Memory Scaling 中 emerging memory/hybrid memory 章节直接关联。",
        "figures": [("Figure 1", "Page 3", "phase change memory", "解释 PCM cell 和 SET/RESET。"), ("Figure 2", "Page 4", "PCM RESET energy scaling", "展示 PCM energy scaling 趋势。"), ("Figure 5", "Page 6", "Pareto analysis", "比较 buffer design area/delay/energy。"), ("Figure 7", "Page 7", "application delay/energy", "展示 optimized buffering 结果。"), ("Figure 8", "Page 9", "PCM endurance", "展示 partial writes 后寿命。")],
        "tables": [("Table 1", "Page 2", "technology survey", "整理 PCM prototypes 参数。"), ("Table 2", "Page 5", "memory subsystem parameters", "比较 PCM/DRAM timing 与 energy。"), ("Table 4", "Page 9", "endurance model parameters", "列出寿命模型变量。")],
        "equations": [("Endurance model", "Page 9, Equation 3", "估计 memory module lifetime", "L_hat = E / W_hat", "通过每 bit 写入速率和 cell endurance 推算寿命。", "是")],
        "terms": [("Partial writes", "部分写", "Page 8-9", "只把 dirty cache lines/words 写入 PCM array，减少磨损。", "是"), ("Buffer organization", "缓冲组织", "Page 5-7", "通过 buffer width 和 rows 调节写粒度、局部性和 coalescing。", "是"), ("Write coalescing", "写合并", "Page 6", "多个 writes 在 buffer 中合并，减少 array writes。", "是"), ("Endurance", "写入耐久性", "Page 3 and Page 9", "PCM cell 可可靠写入的次数。", "是")],
        "sections": "Abstract; Introduction; PCM Technology; Baseline PCM/DRAM; Buffer Organization; Partial Writes; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "论文提出把 PCM 作为 DRAM 替代时所需的架构增强。baseline PCM 慢且耗能，但 area-neutral buffer reorganizations 和 partial writes 可使其性能、能耗和寿命接近可用。"), ("1-2. PCM Technology / PCM 技术", "Page 1-4", "PCM 通过相变材料的电阻差存储数据。SET/RESET 分别形成晶态/非晶态。论文从近五年 prototype 中导出保守 read/write/endurance 参数。"), ("3-4. Buffer Organization / 缓冲组织", "Page 4-7", "PCM read nondestructive、write expensive，适合把 sensing 与 buffering 分离。窄 buffer 降低每次 array write 能耗，多 buffer rows 捕获局部性并提升 write coalescing。"), ("5. Partial Writes / 部分写", "Page 8-10", "partial writes 从 cache 传递 dirty granularity，只写修改过的数据。endurance model 显示 4B granularity 可把平均寿命提升到 5.6 years。"), ("Conclusion / 结论", "Page 10-12", "作者总结 PCM 的可扩展性和非易失性很有吸引力，但只有结合架构优化才能成为实际主存替代。")],
    },
    {
        "slug": "raidr-dram-refresh_isca12",
        "title": "RAIDR: Retention-Aware Intelligent DRAM Refresh",
        "zh": "RAIDR：保持时间感知的智能 DRAM 刷新",
        "authors": "Jamie Liu, Ben Jaiyen, Richard Veras, Onur Mutlu",
        "year": "2012",
        "venue": "ISCA 2012",
        "doi": "未找到",
        "code": "未找到",
        "pages": "12",
        "dataset": "Retention-time distribution from 60nm process; 8-core 32GB DRAM simulation; SPEC multiprogrammed workloads",
        "topic": "DRAM refresh reduction; retention-time profiling; Bloom filters",
        "keywords": "RAIDR, DRAM refresh, retention time, Bloom filter, weak cells, refresh bins",
        "one": "RAIDR 利用 DRAM rows retention time 差异，把 rows 放入不同 refresh-rate bins，并用 Bloom filters 在 memory controller 中低开销存储，从而跳过大量不必要 refreshes。",
        "background": "DRAM refresh 会阻塞 bank、增加访问延迟并消耗能量；随着 DRAM density 上升，refresh latency、throughput loss 和 refresh power 占比都会快速增加，但绝大多数 cells retention time 远高于标准 64ms。",
        "questions": ["如何利用 retention time variation 减少 refresh 而不修改 DRAM 芯片？", "Bloom filters 为什么适合存储 retention bins？", "RAIDR 在性能、能耗、idle power 和 future density scaling 上收益如何？", "false positives、温度和 retention distribution 变化如何影响正确性？"],
        "contribs": ["提出低成本 memory-controller-only refresh reduction 机制 RAIDR。", "将 rows 根据 minimum retention time 分入 64-128ms、128-256ms 等 bins。", "用 Bloom filters 存储 bins，保证无 false negatives；false positives 只导致多刷新。", "在 32GB/8-core 系统中实现 74.6% refresh reduction、16.1% DRAM power reduction、8.6% performance improvement。", "分析 RAIDR 对 Bloom filter 配置、capacity scaling、temperature 和 retention error sensitivity 的鲁棒性。"],
        "method": "系统先 profile 每行 retention time；memory controller 维护若干 Bloom filters 表示短 retention rows。运行时 controller 以 64ms 基础周期遍历 candidate rows，根据 period counter 和 bin membership 决定是否发 RAS-only refresh。",
        "experiments": "作者使用 retention distribution、DRAM timing/power model 和 8-core multiprogrammed workloads，比较 auto-refresh、distributed refresh、refresh pausing/no-refresh ideal 和 RAIDR；评估 normal/extended temperature、idle power、Bloom filter size/bins 和 4Gb-64Gb scaling。",
        "results": [("32GB DRAM 中少于 1000 cells 需要短于 256ms refresh interval，约 30 cells 需要短于 128ms。", "Page 1-2, Figure 1"), ("RAIDR 在 32GB/8-core 系统中减少 74.6% refreshes。", "Page 1 and Page 8, Figure 6"), ("RAIDR 平均性能提升 4.1% normal / 8.6% extended temperature。", "Page 8, Figure 7"), ("RAIDR 平均 energy per access 降低 8.3% normal / 16.1% extended temperature。", "Page 8-9, Figure 8"), ("64Gb device capacity 下，RAIDR performance 比 auto-refresh baseline 高 107.9%，access energy saving 达 49.7%。", "Page 10, Figure 9")],
        "conclusion": "RAIDR 证明 refresh overhead 可通过 retention-aware profiling + controller-side metadata 大幅降低；它成为后续 refresh reduction 和 VRT-aware refresh 工作的基线。",
        "limitations_author": [("RAIDR 依赖准确 retention time profiling；data pattern 和温度对 retention 的影响留待进一步分析。", "Page 4, Section 3.2 footnote and Page 5, Section 3.5"), ("RAS-only refresh 会带来额外 bus power，尽管评估显示节能收益超过开销。", "Page 5, Section 3.4")],
        "limitations_infer": [("VRT 会使静态 retention profile 过期，需结合 AVATAR/Reaper 等运行时机制。", "推断，结合后续文献"), ("Bloom filter false positives 不影响正确性但会降低 refresh reduction，配置需随容量扩展。", "推断，基于 Figure 9/Table 3")],
        "focus": "重点读 Figure 1 retention distribution、Figure 4 operation、Figure 5 Bloom filters、Figures 6-9 评估。",
        "relation": "RAIDR 是 retention-aware refresh 经典论文；AVATAR 处理 VRT 对 RAIDR 类 profile 的挑战，Reaper 处理 LPDDR4 profiling，PARBOR/DC-REF 从 data content 角度进一步减少 refresh。",
        "figures": [("Figure 1", "Page 2", "retention time distribution", "说明多数 cells 不需要 64ms refresh。"), ("Figure 3", "Page 3", "adverse effects of refresh", "展示容量扩展下 refresh latency/power/throughput loss。"), ("Figure 4", "Page 4", "RAIDR operation", "展示 profiling、bins、candidate refresh decision。"), ("Figure 5", "Page 5", "Bloom filter implementation", "说明 bins 存储和组件。"), ("Figure 7", "Page 8", "performance", "展示性能提升。"), ("Figure 9", "Page 10", "sensitivity/scaling", "展示配置和容量扩展。")],
        "tables": [("Table 3", "Page 10", "RAIDR configurations", "比较 2 bins/3 bins 和不同 Bloom filter overhead。")],
        "equations": [("Bloom filter membership", "Page 5", "retention bin membership test", "k hash functions over m-bit array", "false positive 只造成额外 refresh，false negative 不会发生。", "是")],
        "terms": [("RAIDR", "Retention-Aware Intelligent DRAM Refresh", "Page 1", "根据 row retention time 差异化刷新。", "是"), ("Retention time bin", "保持时间分箱", "Page 4", "按需要 refresh interval 将 rows 分组。", "是"), ("Bloom filter", "布隆过滤器", "Page 5", "低开销近似集合，用于存储短 retention rows。", "是"), ("RAS-only refresh", "按行地址刷新", "Page 5", "controller 指定 row 进行 refresh，而非标准 auto-refresh。", "是")],
        "sections": "Abstract; Introduction; Background; RAIDR; Implementation; Methodology; Evaluation; Sensitivity; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "RAIDR 根据 DRAM cells retention time 差异减少 refresh。它把 rows 放入不同 retention bins，并使用 Bloom filters 低开销存储这些 bins。"), ("1-2. Motivation / 动机", "Page 1-3", "refresh 会降低性能和能效，且随容量增加更严重。大多数 cells 能保持数据远超 64ms，因此统一最坏情况 refresh 是浪费。"), ("3. RAIDR Design / 设计", "Page 4-6", "RAIDR 先 profile 每行 retention time，然后在 memory controller 中保存 bins。Bloom filters 没有 false negatives，能保证不会漏刷新弱 rows。"), ("5-6. Evaluation / 评估", "Page 6-10", "RAIDR 显著减少 refreshes，提升性能并降低能耗；收益在 extended temperature 和未来更高 density 下更大。"), ("7. Conclusion / 结论", "Page 10-12", "作者总结 RAIDR 是一种低成本 controller 修改，可缓解当前和未来 DRAM refresh overhead。")],
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
- 结论依赖论文的硬件模型、benchmark、芯片样本、工艺假设或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征、DRAM/NVM 工艺参数或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
{bullets(p['questions'])}

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowHammer in-DRAM mitigation、DRAM data-dependent testing、phase-change memory/hybrid memory、retention-aware refresh、VRT-aware profiling。
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
- Supplementary Material Detected: 未发现；Panopticon/PARBOR 提供开源链接见 metadata
- OCR Used: No
- Extracted Text File: {extracted}
- Missing Content: 图中细小标注、双栏局部错位和电路/版图细节建议回到 PDF 人工核对
- Parsing Problems: PDF 双栏文本存在局部换行错位；已按页码、章节、图表编号定位关键结论
- Uncertain Parts: DOI/venue 如 metadata 标注“未找到”则表示未在 PDF 抽取文本中确认
- Need User Action: 无；如需逐字全文翻译，请确认版权授权范围后再处理
- Quality Check: 已覆盖摘要、引言/背景、方法/系统设计、实验/结果或研究路线、局限、图表、术语与复习 checklist
- Batch Status: {STATUS}
""")

print(f"updated {len(P)} papers for batch 9")
