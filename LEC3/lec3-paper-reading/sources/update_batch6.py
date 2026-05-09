from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = "第六轮深度阅读完成"
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
        "slug": "RowPress_isca23",
        "title": "RowPress: Amplifying Read Disturbance in Modern DRAM Chips",
        "zh": "RowPress：放大现代 DRAM 芯片中的读扰动",
        "authors": "Haocong Luo, Ataberk Olgun, A. Giray Yağlıkçı, Yahya Can Tuğrul, Steve Rhyner, Meryem Banu Cavlak, Joël Lindegger, Mohammad Sadrosadati, Onur Mutlu",
        "year": "2023",
        "venue": "ISCA 2023",
        "doi": "10.1145/3579371.3589063",
        "pages": "18",
        "dataset": "164 real DDR4 DRAM chips from three major manufacturers; real DDR4 system demo",
        "topic": "DRAM read disturbance; RowPress; RowHammer security; mitigation",
        "keywords": "RowPress, RowHammer, tAggON, ACmin, DDR4, PARA, Graphene, TRR",
        "one": "RowPress 证明长时间保持 aggressor row open 也会造成读扰动，并能将触发 bitflip 所需 activation 数降低一到两个数量级，甚至一次 activation 即可触发。",
        "background": "RowHammer 已说明反复开关 row 会破坏 memory isolation；本文进一步证明 row-open time 本身也是危险因素，现有只考虑 activation count 的防御不足。",
        "questions": ["RowPress 与 RowHammer 在物理触发条件、bitflip cell 集合、温度和访问模式敏感性上有何不同？", "增加 aggressor row on time (tAggON) 会怎样降低 ACmin？", "真实系统和 in-DRAM RowHammer 防御存在时，用户态程序是否仍能触发 RowPress？", "现有 RowHammer mitigation 如何适配 RowPress？"],
        "contribs": ["首次在 164 颗真实 DDR4 芯片上系统表征 RowPress。", "证明 RowPress 影响三大厂商，随技术节点缩小而变严重，且 vulnerable cells 与 RowHammer/retention cells 大多不同。", "展示真实 DDR4 系统中用户态程序可利用 RowPress 触发 bitflips，而传统 RowHammer 不能。", "提出通过限制 maximum row-open time 并调整 RowHammer defense 参数来同时缓解 RowHammer/RowPress。", "开源代码和数据以支持复现。"],
        "method": "作者扫 tAggON、temperature、single/double-sided access patterns 和 tAggOFF，测量最小 aggressor activation count ACmin；再在带 RowHammer 防御的真实系统中构造用户态 RowPress 程序，最后把 Graphene/PARA 适配为 Graphene-RP/PARA-RP 评估开销。",
        "experiments": "测试 164 颗 DDR4 chips/21 modules，覆盖厂商 S/H/M 与多种 die revisions；温度 50-80C；访问模式包括 single-sided、double-sided、ONOFF；系统演示和 mitigation 评估使用真实/模拟 workload weighted speedup。",
        "results": [("RowPress 在现实条件下把 ACmin 降低 1-2 个数量级，极端 tAggON=30ms 时一次 activation 可触发 bitflip。", "Page 1-2, Figure 1"), ("tAggON=7.8us 时 ACmin 平均降低 13.9x；tAggON=70.2us 时平均降低 159.4x、最高 363.8x。", "Page 2, Figure 1 discussion"), ("对 tAggON >= 7.8us，RowPress vulnerable cells 与 RowHammer cells 的重叠平均低于 0.013%，与 retention failures 低于 0.34%。", "Page 7-8, Figure 9"), ("温度从 50C 到 80C 会显著恶化 RowPress，且行为不同于 RowHammer。", "Page 9-10, Figures 11-13"), ("Graphene-RP/PARA-RP 能以较低额外开销缓解 RowPress；示例配置下最大 slowdown 分别约 4.6%/13.1%。", "Page 15-16, Table 2")],
        "conclusion": "RowPress 扩展了读扰动威胁模型：memory controller 的 row policy 与 row-open time 会影响安全性，未来防御必须同时考虑 activation count 和 row-open duration。",
        "limitations_author": [("只限制 maximum row-open time 本身不足，且可能带来高达 34.1% 性能退化。", "Page 15, Section 7"), ("RowPress 需要纳入 RowHammer mitigation 参数配置，否则只看 hammer count 的防御可能失效。", "Page 15-16, Section 7.4")],
        "limitations_infer": [("本文聚焦 DDR4；DDR5/HBM/LPDDR 的 RowPress 行为需要结合后续实验继续确认。", "推断，基于 tested chips scope"), ("真实攻击 exploit 的完整权限提升链不在本文主线，系统风险还需与 OS/allocator/防御配置结合分析。", "推断，基于 user-level bitflip demo")],
        "focus": "重点读 Page 1-2 Figure 1、Page 6-10 characterization、Page 13 real-system demo、Page 15-16 mitigation Table 2。",
        "relation": "RowPress 是 RowHammer Retrospective 后续最重要的新扰动之一，也与 2310 HBM2 read disturbance、VRD、PRAC/Chronus 等防御论文直接相关。",
        "figures": [("Figure 1", "Page 2", "ACmin vs tAggON", "展示 row-open time 如何放大读扰动。"), ("Figure 4", "Page 4", "DDR4 testing infrastructure", "说明实验平台如何控制温度和访问。"), ("Figure 5", "Page 4", "single-sided RowPress pattern", "定义核心访问模式。"), ("Figure 9", "Page 8", "vulnerable cell overlap", "显示 RowPress 与 RowHammer/retention cell 集合差异。"), ("Figure 19", "Page 13", "RowHammer vs RowPress bitflips", "真实系统中 RowPress 能绕过传统条件触发更多 bitflips。")],
        "tables": [("Table 1", "Page 4", "tested DDR4 chips", "列出 164 颗芯片的厂商/容量/die revision。"), ("Table 2", "Page 15", "Graphene-RP/PARA-RP overhead", "展示适配防御的参数和性能开销。")],
        "terms": [("RowPress", "行按压", "Page 1", "长时间保持 DRAM row open 导致附近 row bitflips 的 read-disturb 现象。", "是"), ("tAggON", "aggressor row on time", "Page 1-2", "aggressor row 保持打开的时间。", "是"), ("ACmin", "最小触发 activation 数", "Page 2", "诱发至少一个 bitflip 所需最小 aggressor activations。", "是"), ("Graphene-RP / PARA-RP", "适配 RowPress 的 Graphene/PARA", "Page 15-16", "同时考虑 row-open time 和 RowHammer threshold 的防御版本。", "是")],
        "sections": "Abstract; Introduction; Background; Methodology; Characterization; Real-System Demo; Mitigation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "论文展示 RowPress：不是反复 hammer，而是把 DRAM row 长时间保持打开，也能扰动相邻 row。它显著降低触发 bitflip 所需 activation 数，影响三大厂商 DDR4 芯片，并可在真实系统中触发。"), ("1-3. Motivation and Methodology / 动机与方法", "Page 1-5", "作者定义 tAggON 和 ACmin，构建温控 DDR4 测试基础设施，禁用纠错干扰以直接观察 circuit-level bitflips，并扫多种访问模式与温度。"), ("4-5. Characterization / 表征", "Page 5-11", "随着 tAggON 增加，ACmin 大幅下降。RowPress vulnerable cells 与 RowHammer/retention vulnerable cells 基本不同，且温度、single/double-sided 模式和 tAggOFF 会改变其行为。"), ("6-7. System Demo and Mitigation / 系统演示与防御", "Page 12-16", "用户态程序可在带 RowHammer 防御的 DDR4 系统中利用 RowPress 触发 bitflips。作者提出把现有防御适配为 Graphene-RP/PARA-RP，以较低额外性能开销同时覆盖 RowPress。"), ("9. Conclusion / 结论", "Page 17-18", "RowPress 表明 read disturbance 的安全边界比 RowHammer activation count 更宽。未来 DRAM 防御需要把 row-open duration 纳入威胁模型。")],
    },
    {
        "slug": "SISA-GraphMining-on-PIM_micro21",
        "title": "SISA: Set-Centric Instruction Set Architecture for Graph Mining on Processing-in-Memory Systems",
        "zh": "SISA：面向 PIM 图挖掘的集合中心 ISA",
        "authors": "Maciej Besta, Raghavendra Kanakagiri, Grzegorz Kwasniewski, Rachata Ausavarungnirun, Jakub Beránek, Konstantinos Kanellopoulos, Kacper Janda, Zur Vonarburg-Shmaria, Lukas Gianinazzi, Ioana Stefan, Juan Gómez-Luna, Marcin Copik, Lukas Kapp-Schwoerer, Salvatore Di Girolamo, Nils Blach, Marek Konieczny, Onur Mutlu, Torsten Hoefler",
        "year": "2021",
        "venue": "MICRO 2021",
        "doi": "10.1145/3466752.3480133",
        "pages": "16",
        "dataset": "Graph mining benchmarks and real-world graphs from network datasets",
        "topic": "Graph mining; PIM; set-centric ISA; graph pattern matching",
        "keywords": "SISA, graph mining, set operations, PIM, bitvectors, sparse arrays, clique listing",
        "one": "SISA 观察到复杂 graph mining 大量时间花在 vertex set operations 上，于是把 set operations 提升为 ISA 级抽象，并用 PUM/PNM 加速不同 set representations。",
        "background": "传统图加速多关注 BFS/PageRank 等低复杂度 vertex-centric 算法，而 clique listing、pattern matching、graph learning 等 graph mining 更复杂、更 memory-bound，且并行性不直观。",
        "questions": ["能否用 set-centric programming model 表达多种复杂 graph mining 算法？", "哪些 set operations 应成为 ISA primitives？", "高阶/低阶 vertex set 该用 bitvector 还是 sparse array？", "PUM 与 PNM 分别适合加速哪些 set representation？"],
        "contribs": ["提出 set-centric programming paradigm，把 graph mining 重写为集合交/并/差/计数等操作。", "设计 SISA ISA extensions，支持多种 set operations 和 representations。", "将高 degree bitvectors 映射到 in-DRAM bitwise PUM，将低 degree integer arrays 映射到 near-memory PNM。", "给出 10+ graph mining algorithm formulations，覆盖 clique、pattern matching、learning 等。", "在 maximal clique listing 等任务上相对 Bron-Kerbosch 获得超过 10x speedup。"],
        "method": "SISA 在软件层提供 set-centric formulations 和 thin wrappers，在 ISA 层定义 set instructions，在硬件层由 SISA Controller Unit 选择 sparse array/dense bitvector、merge/galloping/bitwise 等实现，并把操作映射到 PUM 或 PNM。",
        "experiments": "论文使用多种 graph mining workloads、真实图数据和 hand-tuned baselines，比较 non-set、set-based、SISA-enhanced variants 的 runtime/speedup，并做 representation、threshold、load balancing 等敏感性分析。",
        "results": [("SISA-enhanced algorithms 对 established Bron-Kerbosch maximal clique listing 在许多真实图上超过 10x speedup。", "Page 1 and Page 6, contributions"), ("Figure 6 显示 full parallelism 下 SISA 对 non-set/set-based baselines 的显著加速，部分任务 >10x。", "Page 11-12, Figure 6"), ("Figure 8 在 large graphs 上继续显示 SISA-PNM/SISA 维持高性能。", "Page 13, Figure 8"), ("Table 1 比较 set-centric/SISA 与 vertex-centric、edge-centric、linear algebra、joins 等图抽象的覆盖范围。", "Page 2, Table 1"), ("Table 4 总结 SISA instructions，覆盖 set union/intersection/difference/count 等操作变体。", "Page 8, Table 4")],
        "conclusion": "复杂 graph mining 不适合只用 vertex-centric 或单一 graph accelerator 思路；把集合运算作为跨层抽象可以同时获得表达力、并行性和 PIM 加速机会。",
        "limitations_author": [("SISA 需要算法以 set-centric 形式重写或包装，软件生态有迁移成本。", "Page 4-8, design sections"), ("性能依赖 set representation、degree distribution、threshold 和负载均衡。", "Page 12-14, sensitivity analysis")],
        "limitations_infer": [("PUM/PNM 硬件假设较强，真实商业内存系统中部署需要 ISA、runtime 和 memory substrate 支持。", "推断，基于 PIM design"), ("对动态图、在线更新图或小图 workload 的收益可能弱于大规模静态图挖掘。", "推断，基于 benchmark scope")],
        "focus": "重点读 Page 1-3 的 set-centric 动机、Figure 2 总览、Table 4 ISA、Figure 6/8 性能。",
        "relation": "SISA 是 Modern Primer 中 PNM/PUM 融合图挖掘案例；与 Tesseract 都面向图，但 Tesseract偏 graph processing，SISA偏复杂 graph mining/set algebra。",
        "figures": [("Figure 1", "Page 3", "Bron-Kerbosch runtime/stalls", "说明 graph mining 受内存和 set operations 限制。"), ("Figure 2", "Page 5", "SISA overview", "展示 programming model、ISA、PIM hardware 三层。"), ("Figure 4", "Page 8", "set representations", "比较 sparse array 与 dense bitvector。"), ("Figure 6", "Page 11-12", "runtime/speedups", "展示 SISA 主要性能收益。"), ("Figure 8", "Page 13", "large graph runtimes", "说明大图下仍有收益。")],
        "tables": [("Table 1", "Page 2", "graph paradigms comparison", "比较不同图抽象对 graph mining/learning/low-complexity 的支持。"), ("Table 4", "Page 8", "SISA instructions", "列出 set operation ISA variants。"), ("Table 6", "Page 10", "considered graphs", "列出评估图数据集。")],
        "terms": [("Set-centric programming", "集合中心编程", "Page 1-2", "把图挖掘表达为 vertex set operations 的范式。", "是"), ("SISA", "集合中心 ISA", "Page 1", "用于表达和加速 set operations 的 ISA extensions。", "是"), ("Dense bitvector (DB)", "稠密位向量", "Page 7-8", "高 degree vertex sets 的表示，适合 PUM bitwise。", "是"), ("Sparse array (SA)", "稀疏数组", "Page 7-8", "低 degree vertex sets 的整数列表表示，适合 PNM。", "是")],
        "sections": "Abstract; Introduction; Background; Overview; Set-Centric Formulations; SISA Instructions; PIM Acceleration; Evaluation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "SISA 指出复杂 graph mining 的核心瓶颈是集合操作。通过 set-centric programming、SISA ISA extensions 和 PIM 加速，论文把高 degree bitvectors 交给 in-DRAM bitwise PUM，把低 degree integer arrays 交给 near-memory PNM。"), ("1-3. Motivation / 动机", "Page 1-5", "作者区分低复杂度图处理和复杂 graph mining。许多 clique/pattern/learning 算法都围绕邻居集合的交、并、差和计数展开，这些操作既 memory-bound 又有多层并行性。"), ("4-8. SISA Design / 设计", "Page 5-10", "SISA 包括 set-centric formulations、ISA instructions、set representations 和 PIM hardware。SCU 根据集合大小与表示选择 PUM 或 PNM 路线。"), ("9. Evaluation / 评估", "Page 10-14", "实验比较 hand-tuned non-set/set baselines 与 SISA variants。SISA 在多种真实图和复杂算法上获得显著 speedup，尤其是 maximal clique listing 等任务。"), ("Conclusion / 结论", "Page 15-16", "作者总结 set operations 是复杂图挖掘的好抽象：它能提升可编程性，也能把 PIM 的大带宽转化为可用的算法加速。")],
    },
    {
        "slug": "SMASH-sparse-matrix-software-hardware-acceleration_micro19",
        "title": "SMASH: Co-designing Software Compression and Hardware-Accelerated Indexing for Efficient Sparse Matrix Operations",
        "zh": "SMASH：协同设计软件压缩与硬件索引以高效执行稀疏矩阵操作",
        "authors": "Konstantinos Kanellopoulos, Nandita Vijaykumar, Christina Giannoula, Roknoddin Azizi, Skanda Koppula, Nika Mansouri Ghiasi, Taha Shahroodi, Juan Gomez Luna, Onur Mutlu",
        "year": "2019",
        "venue": "MICRO 2019",
        "doi": "10.1145/3352460.3358286",
        "pages": "15",
        "dataset": "15 sparse matrices; SpMV, SpMM, PageRank, Betweenness Centrality",
        "topic": "Sparse matrix; hardware-software co-design; compression; indexing",
        "keywords": "SMASH, sparse matrices, hierarchical bitmap, BMU, SpMV, SpMM, CSR",
        "one": "SMASH 发现 CSR 类格式的非零元素位置发现/indexing 是稀疏矩阵瓶颈，并用 hierarchical bitmap + BMU + ISA 让硬件直接理解压缩格式。",
        "background": "稀疏线性代数广泛用于 ML、图分析和 HPC；压缩可以省存储和跳过零元素，但 CSR/COO 等格式引入 pointer chasing 和 index matching，抵消部分收益。",
        "questions": ["如何在保持通用性和压缩率的同时减少 indexing 开销？", "hierarchical bitmap 如何表示任意稀疏结构？", "BMU 需要哪些 buffers/registers/ISA primitives 才能扫描 bitmap hierarchy？", "SMASH 对 SpMV/SpMM/PageRank/BC 的收益和硬件面积开销是多少？"],
        "contribs": ["提出 SMASH：软件 hierarchical bitmap encoding + 硬件 Bitmap Management Unit。", "设计 SMASH ISA primitives，让软件配置矩阵/bitmap 并驱动 BMU 找非零块。", "证明 bitmap encoding 不依赖稀疏结构，适用于多种矩阵。", "在 SpMV、SpMM、PageRank、BC 上评估，对 CSR/BCSR 有显著性能提升。"],
        "method": "软件把 sparse matrix 转成多层 bitmap hierarchy；每个 bitmap bit 表示下层或数据块是否含 non-zero。BMU 缓存并扫描 bitmap buffers，返回 non-zero block 的 row/column indices；CPU 只处理真实非零值，减少 pointer chasing。",
        "experiments": "使用 TACO-CSR/TACO-BCSR 等 state-of-the-art baselines，15 个矩阵，SpMV/SpMM 和图分析应用；比较 speedup、instruction count、compression ratio、BMU area、compression ratio sensitivity。",
        "results": [("SMASH 对 SpMV 平均提升 38%，对 SpMM 平均提升 44%，相对 state-of-the-art CSR。", "Page 1, Abstract; Page 10-11 evaluation"), ("跨 SpMV/SpMM 15 个矩阵平均提升 41.5%，PageRank/BC 平均提升 20%。", "Page 2, contributions"), ("理想化去除 CSR indexing 可带来 2.21x/2.13x/2.81x（SpMatAdd/SpMV/SpMM）收益，说明 indexing 是关键瓶颈。", "Page 3, Figure 3"), ("BMU 硬件面积最多仅为 OoO CPU core 的 0.076%。", "Page 1 and Page 13, area evaluation"), ("software-only SMASH 即使没有 BMU 也平均优于 CSR，但硬件 BMU 才能充分发挥 bitmap encoding。", "Page 6 and evaluation discussion")],
        "conclusion": "稀疏矩阵优化不能只看存储压缩率，还必须把压缩格式能否被硬件高效索引纳入设计；SMASH 用跨层格式让软件压缩和硬件发现非零位置协同。",
        "limitations_author": [("转换为 SMASH hierarchical bitmap format 有软件预处理成本。", "Page 5, Section 4.1.3"), ("compression ratio 选择影响 bitmap size、扫描速度和额外零元素处理之间的权衡。", "Page 5 and Figure 14")],
        "limitations_infer": [("对动态更新频繁的 sparse matrix，格式转换和 bitmap 维护成本可能降低收益。", "推断，基于 conversion process"), ("BMU 与 ISA 需要 CPU/编译器/库支持，部署难度高于纯软件格式。", "推断，基于 hardware-software co-design")],
        "focus": "重点读 Page 2-3 的 CSR indexing bottleneck、Figure 4/6 的 bitmap/BMU、Table 1 ISA、Figure 12-14 评估。",
        "relation": "SMASH 与 SISA 都把高层数据结构操作暴露给硬件；SMASH 针对 sparse matrix indexing，SISA 针对 graph mining set operations。",
        "figures": [("Figure 1", "Page 2", "CSR format", "说明 row_ptr/col_ind/value 的索引路径。"), ("Figure 3", "Page 3", "Ideal CSR speedup", "证明 indexing 是瓶颈。"), ("Figure 4", "Page 5", "hierarchical bitmap", "展示 SMASH 压缩表示。"), ("Figure 6", "Page 6", "BMU structure", "展示硬件扫描 bitmap 的结构。"), ("Figure 12", "Page 10", "SpMM speedup", "展示核心性能收益。")],
        "tables": [("Table 1", "Page 6", "SMASH instructions", "列出 MATINFO/BMAPINFO/RDBMAP/PBMAP/RDIND 等 ISA。")],
        "terms": [("Hierarchical bitmap", "层次化位图", "Page 4-5", "用多层位图表示哪些块含非零元素。", "是"), ("Bitmap Management Unit (BMU)", "位图管理单元", "Page 6", "硬件扫描位图层次并返回非零块位置。", "是"), ("CSR", "压缩稀疏行格式", "Page 1-2", "常见稀疏矩阵格式，但 indexing/pointer chasing 开销高。", "是"), ("SpMV / SpMM", "稀疏矩阵向量/矩阵乘法", "Page 2", "SMASH 的两个核心稀疏线性代数用例。", "是")],
        "sections": "Abstract; Introduction; Motivation; SMASH Key Components; BMU; ISA; Use Cases; Evaluation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "SMASH 通过 hierarchical bitmap 软件编码和 BMU 硬件索引，让硬件识别稀疏矩阵压缩格式。相比 CSR，SpMV/SpMM 平均提升 38%/44%，面积开销很小。"), ("1-2. Motivation / 动机", "Page 1-3", "CSR 等格式减少零元素存储和计算，但发现 non-zero positions 需要 col_ind 扫描、pointer chasing 和 index matching。理想去除 indexing 后性能大幅提升，证明这是关键瓶颈。"), ("3-4. SMASH Design / 设计", "Page 4-7", "SMASH 用多层 bitmap 表示稀疏结构。BMU 通过 SRAM buffers、扫描逻辑、寄存器和输出 index registers 遍历层次位图，并由 ISA primitives 控制。"), ("5-7. Use Cases and Evaluation / 用例与评估", "Page 7-13", "SpMV、SpMM、PageRank、BC 等应用显示 SMASH 在多种矩阵稀疏结构下均有收益。压缩率和 BMU 参数影响性能，但面积最多约 0.076% OoO core。"), ("Conclusion / 结论", "Page 14-15", "作者强调跨层 co-design 的必要性：压缩格式要同时适合软件存储和硬件索引，才能真正提升稀疏计算效率。")],
    },
    {
        "slug": "VBI-virtual-block-interface_isca20",
        "title": "The Virtual Block Interface: A Flexible Alternative to the Conventional Virtual Memory Framework",
        "zh": "Virtual Block Interface：传统虚拟内存框架的灵活替代方案",
        "authors": "Minesh Patel, Konstantinos Kanellopoulos, Saugata Ghose, Nastaran Hajinazar, Pratyush Patel, Rachata Ausavarungnirun, Geraldo F. Oliveira, Jonathan Appavoo, Vivek Seshadri, Onur Mutlu",
        "year": "2020",
        "venue": "ISCA 2020",
        "doi": "未找到",
        "pages": "14",
        "dataset": "SPEC and Graph500 traces; PCM-DRAM and TL-DRAM heterogeneous memory evaluations",
        "topic": "Virtual memory; memory-controller managed translation; heterogeneous memory",
        "keywords": "VBI, virtual blocks, MTL, address translation, virtual memory, heterogeneous memory",
        "one": "VBI 用全局 virtual blocks 和 memory-controller-side Memory Translation Layer 替代传统 page-table-centric 虚拟内存，把 access protection、allocation 和 translation 解耦。",
        "background": "传统虚拟内存难以适配虚拟化、多级页表、异构内存和应用多样需求；OS 同时管理 protection、allocation、translation 造成复杂性和性能损失。",
        "questions": ["能否让应用用可变大小 virtual blocks 表达语义单位？", "能否把 physical allocation 和 address translation 交给 memory controller 侧硬件？", "VBI 如何降低 native/VM address translation overhead？", "VBI 如何更好管理 PCM-DRAM/TL-DRAM 等异构内存？"],
        "contribs": ["提出 VBI address space，由 variable-sized Virtual Blocks 组成。", "把 access protection 由 OS 控制，把 allocation/translation 委托给 Memory Translation Layer (MTL)。", "支持 VIVT cache、避免 2D page walks、delayed physical allocation、flexible translation structures。", "在 address translation 和 heterogeneous memory 两个 use cases 中量化性能提升。"],
        "method": "应用把语义相关对象放入 VB；OS 控制 process-VB permissions；CPU 使用 system-wide unique VBI address 访问 cache；LLC miss 后由 memory controller 的 MTL 完成 VBI-to-physical translation 和物理内存分配/迁移。",
        "experiments": "使用定制 simulator、SPEC/Graph500 traces、多程序 workloads；比较 Native/Virtual/VIVT/Enigma/VBI variants；异构内存场景包括 PCM-DRAM 与 TL-DRAM。",
        "results": [("4KB granularity simplified VBI 在 native/VM address translation 场景分别最高提升 2.6x/3.8x。", "Page 2 and Page 9, Figure 6"), ("在启用 large pages 后，VBI 仍比 Native-2M 提升 77%，比 Virtual-2M 提升 89%。", "Page 9-10, Figure 7"), ("VBI-Full 将 translation-related memory accesses 平均减少 56%。", "Page 9-10, Figure 7 discussion"), ("在 PCM-DRAM 和 TL-DRAM 两种异构内存中，VBI 分别提升 33% 和 21%。", "Page 11, Figures 9-10"), ("虚拟机中 VBI 避免 2D page walks，使 VM translation 与 native 类似。", "Page 5 and Section 6.1")],
        "conclusion": "VBI 的核心价值是把传统虚拟内存中绑在一起的职责拆开：OS 负责保护语义，硬件负责更细粒度、更接近内存行为的分配和翻译。",
        "limitations_author": [("VBI 是新虚拟内存框架，需要 ISA/OS/hardware/memory-controller 协同修改。", "Page 3-7, design sections"), ("MTL 变成关键硬件组件，需要正确处理 capacity management、sharing、copy-on-write、swap 等功能。", "Page 4-7, Section 3-4")],
        "limitations_infer": [("真实系统采用 VBI 的兼容性成本很高，尤其对现有 OS、hypervisor 和应用 ABI。", "推断，基于 framework replacement"), ("安全性依赖 VB permission/CVT/VIT/MTL 实现正确性，攻击面转移到新硬件软件边界。", "推断，基于 protection design")],
        "focus": "重点读 Page 1-2 的问题定义、Figure 1/2 的 VBI vs x86-64、Page 4-7 detailed design、Figures 6-10 结果。",
        "relation": "VBI 与 X-MEM/MetaSys 都是 cross-layer abstraction，但 VBI 更激进地重构 virtual memory contract。",
        "figures": [("Figure 1", "Page 2", "x86-64 vs VBI memory management", "展示 page tables 与 VBI/MTL 的职责差异。"), ("Figure 2", "Page 3", "VBI overview", "展示 VBI address space、MTL、physical memory。"), ("Figure 4", "Page 6", "reference microarchitecture", "展示 load path、CVT、VIT、MTL。"), ("Figure 6", "Page 9", "4KB page performance", "展示 address translation 降低收益。"), ("Figure 9", "Page 11", "PCM-DRAM performance", "展示异构内存提升。")],
        "tables": [("Table 1", "Page 8", "simulation configuration", "列出 cache/memory/simulator 参数。"), ("Table 2", "Page 10", "multiprogrammed workloads", "列出多程序 workload bundles。")],
        "terms": [("Virtual Block (VB)", "虚拟块", "Page 1-3", "全局 VBI address space 中可变大小、语义相关的连续区域。", "是"), ("Memory Translation Layer (MTL)", "内存翻译层", "Page 2-4", "memory controller 侧管理 allocation 和 VBI-to-physical translation 的硬件层。", "是"), ("Client-VB Table (CVT)", "客户端-VB 表", "Page 4-6", "记录 process/client 对哪些 VBs 有访问权限。", "是"), ("VBI address", "VBI 地址", "Page 3-4", "由 VB ID 和 offset 构成的系统唯一地址。", "是")],
        "sections": "Abstract; Introduction; VBI Overview; Detailed Design; Optimizations; Evaluation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "VBI 是传统虚拟内存的替代框架。它向应用暴露 variable-sized virtual blocks，把 access protection 与 memory allocation/address translation 分离，并由 memory-controller hardware 管理物理分配和翻译。"), ("1-3. Motivation and Overview / 动机与总览", "Page 1-4", "虚拟化、地址翻译和异构内存让传统 page-table-centric 框架变得复杂。VBI 用全局 VB address space 表示语义对象，OS 控制权限，MTL 管理底层物理资源。"), ("4-6. Detailed Design / 详细设计", "Page 4-8", "论文定义 VB、memory clients、CVT、VIT、VBI address、MTL 操作和 VM/multinode 支持。VBI 可支持 VIVT caches、避免 2D page walks、delayed allocation 和 flexible translation structures。"), ("7. Evaluation / 评估", "Page 8-12", "地址翻译实验显示 VBI 减少 TLB/translation-related memory accesses；异构内存实验显示 VBI 能根据 hotness/latency sensitivity 更好放置数据。"), ("9. Conclusion / 结论", "Page 13-14", "作者认为重新设计 virtual memory framework 可以比不断给传统框架打补丁更好地适配未来多样化系统。")],
    },
    {
        "slug": "X-MEM_Expressive-Memory-for-Rich-Cross-Layer-Abstractions_isca18",
        "title": "A Case for Richer Cross-layer Abstractions: Bridging the Semantic Gap with Expressive Memory",
        "zh": "用 Expressive Memory 弥合语义鸿沟：更丰富跨层抽象的案例",
        "authors": "Nandita Vijaykumar, Abhilasha Jain, Diptesh Majumdar, Kevin Hsieh, Gennady Pekhimenko, Eiman Ebrahimi, Nastaran Hajinazar, Phillip B. Gibbons, Onur Mutlu",
        "year": "2018",
        "venue": "ISCA 2018",
        "doi": "未找到",
        "pages": "14",
        "dataset": "Simulation workloads for cache tiling portability and DRAM page placement",
        "topic": "Cross-layer memory abstraction; program semantics; cache and DRAM optimization",
        "keywords": "XMem, Expressive Memory, Atom, semantic gap, cache management, page placement",
        "one": "XMem 提出 Atom 抽象，把应用中的数据结构语义传给 OS 和硬件，以提高 cache optimization portability 和 DRAM page placement 效果。",
        "background": "传统 ISA/virtual memory 只表达程序功能和地址访问，丢失 data structure、reuse、access pattern 等高层语义，导致 OS/硬件只能局部推断程序行为。",
        "questions": ["能否设计通用跨层接口，把程序语义传递给 cache、prefetcher、memory controller 等组件？", "Atom 应该携带哪些属性、如何 map/unmap/activate？", "XMem 如何在 cache tiling 资源不匹配时减少性能损失？", "XMem 如何帮助 OS-based DRAM page placement？"],
        "contribs": ["提出 Expressive Memory (XMem) 和 Atom 抽象。", "定义 CREATE、MAP/UNMAP、ACTIVATE/DEACTIVATE 操作及 XMemLib/ISA/OS/hardware interfaces。", "展示 XMem 可帮助至少九类 memory optimizations。", "通过 cache optimization portability 与 DRAM page placement 两个 use cases 量化收益。"],
        "method": "应用用 XMemLib 创建 Atom，给数据结构或 tile 标注 data properties、access pattern、reuse、read/write characteristics。OS 保存静态属性，Atom Management Unit (AMU) 维护 AAM/AST，硬件组件按地址查询 Atom ID 并选择 cache/prefetch/page placement policy。",
        "experiments": "Use Case 1 评估 cache tiling 在实际 cache space 与假设不匹配时的性能损失；Use Case 2 用 DRAM placement 根据 data structure semantics 分离 high row-buffer locality 与 irregular data structures。",
        "results": [("当软件优化错误假设 available cache space 时，baseline 平均性能损失 55%，XMem 降至 6%。", "Page 2 and Page 9, Figures 4-6"), ("XMem-based DRAM page placement 平均提升 8.5%，最高 31.9%。", "Page 2 and Page 12, Figure 7"), ("XMem 还能把 read latency 平均降低 12.6%，最高 31.4%。", "Page 12, Figure 8"), ("默认 AAM 每 512B 约 0.2% storage overhead，可增大粒度降至 0.07%。", "Page 6, Section 4.4"), ("Table 1 总结 cache management、page placement、prefetching、compression、QoS 等九类可受益优化。", "Page 2-3, Table 1")],
        "conclusion": "XMem 的核心论点是：面向性能的系统不应只靠硬件猜测；用低开销、架构无关的语义接口暴露数据结构属性，可以让多种内存优化更有效且更可移植。",
        "limitations_author": [("XMem 需要程序员、autotuner 或 compiler 标注 atoms，语义表达错误会影响优化效果。", "Page 3-6, Atom design"), ("它影响性能而不影响正确性，但需要 OS/ISA/hardware 支持 AAM/AST/AMU。", "Page 5-7, implementation")],
        "limitations_infer": [("两个 use cases 不能完全证明所有九类优化都能低成本受益。", "推断，基于 Table 1 vs evaluated use cases"), ("与后来的 MetaSys 相比，XMem 更偏 proposal/模拟评估，真实硬件基础设施还需补充。", "推断，结合 MetaSys")],
        "focus": "重点读 Page 1-3 的 semantic gap 和 Atom、Figure 3 系统组件、Table 2 operators、Figures 4-8 评估。",
        "relation": "XMem 是 MetaSys 和 Locality Descriptor 的前序思想之一；MetaSys 更进一步提供开源 RISC-V/FPGA metadata substrate。",
        "figures": [("Figure 1", "Page 2", "XMem system/interfaces", "展示应用、OS、硬件如何通过 XMem 传语义。"), ("Figure 2", "Page 4", "Atom operators", "展示 CREATE/MAP/UNMAP/ACTIVATE。"), ("Figure 3", "Page 5", "XMem components", "展示 AAM/AST/AMU 等机制。"), ("Figure 6", "Page 9", "cache use case speedup", "展示 XMem 减少 cache tiling 性能损失。"), ("Figure 7", "Page 12", "DRAM placement speedup", "展示 page placement 收益。")],
        "tables": [("Table 1", "Page 2-3", "memory optimizations aided by XMem", "列出九类可用语义增强的优化。"), ("Table 2", "Page 6", "XMem operators and ISA", "列出 XMemLib functions 与 ISA instructions。"), ("Table 3", "Page 8", "simulation configuration", "列出 cache/memory model 参数。")],
        "terms": [("Expressive Memory (XMem)", "表达式内存/富语义内存接口", "Page 1", "把程序高层语义传给系统和硬件的跨层接口。", "是"), ("Atom", "语义原子", "Page 2-4", "承载数据属性、访问属性和局部性的虚拟内存区域抽象。", "是"), ("Atom Management Unit (AMU)", "Atom 管理单元", "Page 5", "维护 AAM/AST 并服务硬件语义查询。", "是"), ("Semantic gap", "语义鸿沟", "Page 1", "应用知道的高层数据语义无法被 OS/硬件看到。", "是")],
        "sections": "Abstract; Introduction; Goals; Atom; XMem Interfaces; Use Case 1; Use Case 2; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "XMem 是一种新的 cross-layer interface，允许应用把高层程序语义传给 OS 和硬件。核心抽象 Atom 表达数据属性、访问属性和局部性，帮助 cache、memory controller 等组件更好优化性能。"), ("1-3. Motivation and Atom / 动机与 Atom", "Page 1-5", "传统接口只保留执行正确性所需信息，数据结构级语义丢失。Atom 将 semantically similar data 绑定到属性和映射范围，并通过 create/map/activate 等操作动态传递给系统。"), ("4. XMem Implementation / 实现", "Page 5-7", "XMemLib、OS、ISA instructions 和 AMU 共同维护 Global/Private Attribute Tables、Atom Address Map 和 Atom Status Table。硬件组件可按地址查询 Atom ID 和属性。"), ("5-6. Use Cases / 用例", "Page 8-12", "cache tiling 用例中，XMem 通过工作集和 reuse 语义协调 cache management/prefetching；DRAM placement 用例中，XMem 根据 data structure 的 row-buffer locality 和 irregularity 进行 bank/channel 放置。"), ("8. Conclusion / 结论", "Page 13-14", "作者总结 XMem 提供通用、低开销的程序语义通道，可提升多种 memory optimization 的效果和可移植性。")],
    },
]


def render_figs(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |" for a, b, c, d in p["figures"])


def render_tables(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |" for a, b, c, d in p["tables"])


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
- Code / Project Page: {'https://github.com/CMU-SAFARI/RowPress' if slug == 'RowPress_isca23' else '未找到'}
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
| 未检测到核心编号公式 | - | 本轮阅读未发现必须掌握的核心编号公式 | - | - | 否 |
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
- 当软件无法表达所需语义、硬件接口不可用，或 workload 行为与评估集差异很大时，收益可能明显下降。（推断）

## 5. 我阅读时应该追问的问题
{bullets(p['questions'])}

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowPress 后续防御、PIM graph mining、稀疏计算 ISA、virtual memory redesign、metadata substrate。
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
- Equations Detected: No core numbered equations detected in this round
- Appendix Detected: 未发现独立 appendix 或本轮未作为重点处理
- Supplementary Material Detected: 未发现
- OCR Used: No
- Extracted Text File: {extracted}
- Missing Content: 图中细小标注和双栏排版细节建议回到 PDF 人工核对
- Parsing Problems: PDF 双栏文本存在局部换行错位；SISA 抽取文本版式较乱，已用图表编号与章节定位关键结论
- Uncertain Parts: DOI/arXiv 如 metadata 标注“未找到”则表示未在 PDF 抽取文本中确认
- Need User Action: 无；如需逐字全文翻译，请确认版权授权范围后再处理
- Quality Check: 已覆盖摘要、引言、方法/系统设计、实验/结果、局限、图表、术语与复习 checklist
- Batch Status: {STATUS}
""")

print(f"updated {len(P)} papers for batch 6")
