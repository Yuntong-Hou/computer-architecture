# Global Glossary

| English Term | 中文翻译 | 出现论文 | 简明解释 | 重要程度 |
|---|---|---|---|---|
| AAP | ACTIVATE-ACTIVATE-PRECHARGE | Ambit: In-Memory Accelerator for Bulk Bitwise Operations Using Commodity DRAM Technology | Ambit 执行 bulk bitwise operation 的基础命令序列 | 高 |
| AAP primitive | ACTIVATE-ACTIVATE-PRECHARGE 原语 | In-DRAM Bulk Bitwise Execution Engine | Ambit 控制器执行 bulk bitwise operation 的基本命令序列 | 高 |
| Ambit | 内存内批量按位加速器 | Ambit: In-Memory Accelerator for Bulk Bitwise Operations Using Commodity DRAM Technology | 利用 DRAM analog operation 执行 bitwise operations | 高 |
| Ambit-AND-OR | Ambit 的 AND/OR 机制 | In-DRAM Bulk Bitwise Execution Engine | 通过 TRA 和控制行实现 bulk AND/OR | 高 |
| Associative search | 关联搜索 | A Logic-in-Memory Computer | 在 sector 内按 masked equality/threshold 查找 words | 高 |
| bbop instruction | bulk bitwise operation 指令 | SIMDRAM: An End-to-End Framework for Bit-Serial SIMD Computing in DRAM | 程序员/编译器调用 SIMDRAM operation 的 ISA 接口 | 高 |
| Bit Error Rate (BER) | 比特错误率 | DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips | in-DRAM AND/OR 结果错误比例 | 高 |
| Bit-serial computing | 位串行计算 | ComputeDRAM: In-Memory Compute Using Off-the-Shelf DRAMs | 按 bit slice 在大量元素上并行执行计算 | 高 |
| Bit-slice mode | 位片模式 | A Logic-in-Memory Computer | 从许多 words 中取同一 bit slice 放入 cache 并并行处理 | 高 |
| BitWeaving | 数据库位编织扫描技术 | Ambit: In-Memory Accelerator for Bulk Bitwise Operations Using Commodity DRAM Technology | 把列值按 bit plane 存放以用 bitwise operations 加速 predicate | 中 |
| Bulk bitwise operation | 批量按位操作 | Fast Bulk Bitwise AND and OR in DRAM | 对 KB/MB 级 bitvector 执行 AND/OR | 高 |
| Bulk Zeroing (BuZ) | 批量置零 | RowClone: Fast and Energy-Efficient In-DRAM Bulk Data Copy and Initialization | 通过复制预置零行初始化目标行 | 高 |
| Cellular array | 细胞阵列 | Cellular Logic-in-Memory Arrays | 由大量相同 cell 以规则邻接方式组成的阵列 | 高 |
| Cellular Logic-in-Memory (CLIM) | 细胞式逻辑内存 | Cellular Logic-in-Memory Arrays | 每个阵列 cell 同时含逻辑和存储的二维规则结构 | 高 |
| Circuit Control Unit (CCU) | 电路控制单元 | NoM: Network-on-Memory for Inter-Bank Data Transfer in Highly-Banked Memories | 在 memory controller 中集中分配和配置 NoM paths | 高 |
| Cold-boot attack | 冷启动攻击 | Simultaneous Many-Row Activation in Off-the-Shelf DRAM Chips: Experimental Characterization and Analysis | 利用 DRAM 断电后短时保留数据读取机密信息 | 中 |
| Column success ratio | 列成功率 | ComputeDRAM: In-Memory Compute Using Off-the-Shelf DRAMs | 某列在重复测试中产生正确结果的比例 | 高 |
| Communication interface | 通信接口 | SimplePIM: A Software Framework for Productive and Efficient Processing-in-Memory | 提供 broadcast/scatter/gather/allreduce/allgather | 高 |
| ComputeDRAM | 商用 DRAM 内计算机制 | ComputeDRAM: In-Memory Compute Using Off-the-Shelf DRAMs | 通过越界 timing command sequence 在未改 DRAM 中执行计算 | 高 |
| CoMRA | consecutive multiple-row activation | PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips | 连续激活多行，常用于 in-DRAM copy | 高 |
| Content-addressed memory | 内容寻址存储器 | Cellular Logic-in-Memory Arrays | 按内容而非地址查找/选择 word 的存储器 | 中 |
| COTS DRAM | 商用现货 DRAM | Functionally-Complete Boolean Logic in Real DRAM Chips: Experimental Characterization and Analysis | 未修改、可购买的 DRAM 芯片 | 高 |
| D-RaNGe | DRAM 真随机数生成技术 | PiDRAM: A Holistic End-to-end FPGA-based Framework for Processing-in-DRAM | 利用 reduced activation latency 下的随机失败生成 TRNG | 高 |
| DaPPA | 数据并行 PIM 编程框架 | DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures | 用高层 pattern 和 Pipeline 自动生成 UPMEM 程序 | 高 |
| DFI | DDR PHY Interface | DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips | memory controller 与 PHY 间标准化接口 | 中 |
| DPU | DRAM Processing Unit | DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures | UPMEM PIM chip 内的小型多线程 in-order processor | 高 |
| DRAM Bender | DRAM 测试基础设施 | DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips | 可向真实 DRAM 发出任意低层命令的 FPGA 平台 | 高 |
| DRAM mat | DRAM 阵列小块 | MIMDRAM: An End-to-End Processing-Using-DRAM System for High-Throughput, Energy-Efficient and Programmer-Transparent Multiple-Instruction Multiple-Data Processing | subarray 内较小二维阵列，是 MIMDRAM 的细粒度资源单位 | 高 |
| Dual-contact cell (DCC) | 双接触 DRAM 单元 | In-DRAM Bulk Bitwise Execution Engine；Ambit: In-Memory Accelerator for Bulk Bitwise Operations Using Commodity DRAM Technology | 用两个访问晶体管支持读取反相值，实现 NOT | 高 |
| Dynamic bit-precision | 动态位精度 | Proteus: Enabling High-Performance Processing-Using-DRAM with Dynamic Bit-Precision, Adaptive Data Representation, and Flexible Arithmetic | 根据运行时数据实际范围选择更小 bit-width | 高 |
| Dynamic Bit-Precision Engine | 动态位精度引擎 | Proteus: Enabling High-Performance Processing-Using-DRAM with Dynamic Bit-Precision, Adaptive Data Representation, and Flexible Arithmetic | 在数据转置/写回过程中识别对象所需位宽 | 高 |
| Dynamic template-based compilation | 动态模板式编译 | DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures | 运行时填充 skeleton 并生成 UPMEM binary 的机制 | 高 |
| Error table | 错误表 | ComputeDRAM: In-Memory Compute Using Off-the-Shelf DRAMs | 记录坏 rows/columns，运行时避免使用 | 高 |
| F-MAJ | Fractional majority operation | FracDRAM: Fractional Values in Off-the-Shelf DRAM | 用 fractional value 改善四行激活下 majority operation 的覆盖和稳定性 | 高 |
| Fast Parallel Mode (FPM) | 快速并行模式 | RowClone: Fast and Energy-Efficient In-DRAM Bulk Data Copy and Initialization | 同 subarray 内用背靠背 ACTIVATE 复制整行 | 高 |
| FastBit | bitmap index 库 | Fast Bulk Bitwise AND and OR in DRAM | 论文用来估算真实 range query 收益的开源 bitmap index 实现 | 高 |
| Fault accommodation | 故障容纳 | Cellular Logic-in-Memory Arrays | 通过绕过或重编程减少故障 cell 影响 | 高 |
| FIGARO | 细粒度 DRAM 内重定位 substrate | FIGARO: Improving System Performance via Fine-Grained In-DRAM Data Relocation and Caching | 通过 global row buffer 支持 bank 内 cache-block granularity relocation | 高 |
| FIGCache | 基于 FIGARO 的 DRAM 内缓存 | FIGARO: Improving System Performance via Fine-Grained In-DRAM Data Relocation and Caching | 缓存 row segments 而不是完整 DRAM rows | 高 |
| Fine-DRAM-Act | 细粒度 DRAM 激活 | Sectored DRAM: A Practical Energy-Efficient and High-Performance Fine-Grained DRAM Architecture | 只激活部分 DRAM cells 而非完整 row | 高 |
| FMTC | copy 造成的内存流量比例 | RowClone: Fast and Energy-Efficient In-DRAM Bulk Data Copy and Initialization | Fraction of Memory Traffic due to Copies，用于解释 forkbench 收益 | 高 |
| Frac operation | Frac 操作 | FracDRAM: Fractional Values in Off-the-Shelf DRAM | 用 ACTIVATE 后立即 PRECHARGE 中断放大以生成 fractional value | 高 |
| FracDRAM | 分数电荷 DRAM 技术 | Simultaneous Many-Row Activation in Off-the-Shelf DRAM Chips: Experimental Characterization and Analysis | 利用 fractional values 执行 MAJ3 等操作 | 中 |
| Fractional value | 分数电压值 | FracDRAM: Fractional Values in Off-the-Shelf DRAM | 介于传统 0/Vdd 与 1/ground 之间的 DRAM cell 电压状态 | 高 |
| FTS | FIGCache Tag Store | FIGARO: Improving System Performance via Fine-Grained In-DRAM Data Relocation and Caching | memory controller 中保存缓存 row segment metadata 的表 | 高 |
| Functionally-complete Boolean logic | 功能完备布尔逻辑 | Functionally-Complete Boolean Logic in Real DRAM Chips: Experimental Characterization and Analysis | 能组合表达任意布尔函数的一组操作，例如 NAND 或 AND+NOT | 高 |
| Global Row Buffer (GRB) | 全局行缓冲 | FIGARO: Improving System Performance via Fine-Grained In-DRAM Data Relocation and Caching | 连接同一 bank 内 subarrays 与 I/O 的共享缓冲 | 高 |
| Half-m operation | 掩码 Half 操作 | FracDRAM: Fractional Values in Off-the-Shelf DRAM | 在 masked bits 中混合写入 normal values 与 Half values | 高 |
| HCfirst | 首次 bit flip 所需激活数 | DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips；PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips | 衡量 RowHammer 敏感性的指标 | 高 |
| High-level language mismatch | 高层语言不匹配 | A Logic-in-Memory Computer | 语言语义无法表达机器强指令导致其难以被编译器使用 | 高 |
| Input replication | 输入复制 | Simultaneous Many-Row Activation in Off-the-Shelf DRAM Chips: Experimental Characterization and Analysis | 把输入副本放入多个激活行以提高 sensing margin | 高 |
| Inter-bank copy | bank 间复制 | NoM: Network-on-Memory for Inter-Bank Data Transfer in Highly-Banked Memories | 源和目标位于不同 DRAM banks 的 direct data copy | 高 |
| Intra-HD / Inter-HD | 模块内/模块间汉明距离 | FracDRAM: Fractional Values in Off-the-Shelf DRAM | 衡量 PUF reliability 与 uniqueness 的指标 | 高 |
| Isolation transistor | 隔离晶体管 | Low-Cost Inter-Linked Subarrays (LISA): Enabling Fast Inter-Subarray Data Movement in DRAM | 打开或关闭相邻 bitlines 连接的开关 | 高 |
| Linked Precharge (LIP) | 联动预充电 | Low-Cost Inter-Linked Subarrays (LISA): Enabling Fast Inter-Subarray Data Movement in DRAM | 利用邻近 subarray 的 precharge unit 加速 precharge | 高 |
| Local Row Buffer (LRB) | 本地行缓冲 | FIGARO: Improving System Performance via Fine-Grained In-DRAM Data Relocation and Caching | 每个 subarray 的 sense amplifier row buffer | 高 |
| Locality-Aware execution | 局部性感知执行 | PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture | 根据数据局部性选择 host-side 或 memory-side 执行 PEI | 高 |
| Logic-enhanced cache | 逻辑增强 cache | A Logic-in-Memory Computer | 作为 CPU 与主存之间高速 buffer 的 logic-in-memory array | 高 |
| Logic-in-memory array | 逻辑内存阵列 | A Logic-in-Memory Computer | 每个 storage element 附带组合逻辑的 memory array | 高 |
| Low-Cost Inter-Linked Subarrays (LISA) | 低成本互连子阵列 | Low-Cost Inter-Linked Subarrays (LISA): Enabling Fast Inter-Subarray Data Movement in DRAM | 用 isolation transistors 连接相邻 subarrays bitlines 的 DRAM substrate | 高 |
| LSQ Lookahead | Load/Store Queue 前瞻 | Sectored DRAM: A Practical Energy-Efficient and High-Performance Fine-Grained DRAM Architecture | 利用队列中 younger load/store 发现同一 cache block 的未来访问 | 高 |
| Majority operation (MAJ) | 多数逻辑 | SIMDRAM: An End-to-End Framework for Bit-Serial SIMD Computing in DRAM | 三个输入中多数为 1 则输出 1，是 TRA 的逻辑模型 | 高 |
| Majority-Inverter Graph (MIG) | 多数-反相图 | SIMDRAM: An End-to-End Framework for Bit-Serial SIMD Computing in DRAM | 用 MAJ/NOT 表示和优化逻辑的图结构 | 高 |
| MAJX | X 输入多数操作 | Simultaneous Many-Row Activation in Off-the-Shelf DRAM Chips: Experimental Characterization and Analysis | X>3 的 majority operation，如 MAJ5/7/9 | 高 |
| Management interface | 管理接口 | SimplePIM: A Software Framework for Productive and Efficient Processing-in-Memory | 集中管理 PIM-resident array metadata | 高 |
| Many-input Boolean operation | 多输入布尔操作 | Functionally-Complete Boolean Logic in Real DRAM Chips: Experimental Characterization and Analysis | 输入数超过两个的 AND/NAND/OR/NOR 操作 | 高 |
| Memory stack | 内存堆叠 | Transparent Offloading and Mapping (TOM): Enabling Programmer-Transparent Near-Data Processing in GPU Systems | 含 DRAM layers 与 logic layer 的 3D-stacked memory | 高 |
| MIMD | 多指令多数据 | MIMDRAM: An End-to-End Processing-Using-DRAM System for High-Throughput, Energy-Efficient and Programmer-Transparent Multiple-Instruction Multiple-Data Processing | 不同 mats 可执行不同 PUD operations，而非全 subarray 同步执行同一操作 | 高 |
| MRAM | DPU 私有 DRAM bank | DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures | 每个 DPU 独占的 64MB 存储 | 高 |
| Multi-RowCopy | 多行并发复制 | Simultaneous Many-Row Activation in Off-the-Shelf DRAM Chips: Experimental Characterization and Analysis | 把一行内容同时复制到多个目标行 | 高 |
| Narrow values | 窄值 | Proteus: Enabling High-Performance Processing-Using-DRAM with Dynamic Bit-Precision, Adaptive Data Representation, and Flexible Arithmetic | 虽然存为 32/64-bit，但有效位很少的值 | 高 |
| Near-Data Processing (NDP) | 近数据处理 | Transparent Offloading and Mapping (TOM): Enabling Programmer-Transparent Near-Data Processing in GPU Systems | 把计算放到数据附近，例如 3D-stacked memory logic layer | 高 |
| Network-on-Memory (NoM) | 内存上网络 | NoM: Network-on-Memory for Inter-Bank Data Transfer in Highly-Banked Memories | 连接 3D-stacked memory banks 的轻量级 inter-bank copy network | 高 |
| NoM-Light | 轻量 NoM | NoM: Network-on-Memory for Inter-Bank Data Transfer in Highly-Banked Memories | 复用既有 TSVs 以减少 full 3D mesh vertical link 成本的变体 | 高 |
| Offload candidate | 卸载候选代码块 | Transparent Offloading and Mapping (TOM): Enabling Programmer-Transparent Near-Data Processing in GPU Systems | 编译器认为 offload 可节省带宽的 instruction block | 高 |
| Offloading aggressiveness control | 卸载激进度控制 | Transparent Offloading and Mapping (TOM): Enabling Programmer-Transparent Near-Data Processing in GPU Systems | 运行时决定是否真的 offload candidate blocks | 高 |
| Open-bitline architecture | 开放位线架构 | Functionally-Complete Boolean Logic in Real DRAM Chips: Experimental Characterization and Analysis | sense amplifier 两端连接不同 subarray/cell 的 DRAM 结构 | 高 |
| Parallelism-Aware µProgram Library | 并行性感知微程序库 | Proteus: Enabling High-Performance Processing-Using-DRAM with Dynamic Bit-Precision, Adaptive Data Representation, and Flexible Arithmetic | 保存不同算法/表示/位宽下的 µProgram 和 cost model | 高 |
| PEI Computation Unit (PCU) | PEI 计算单元 | PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture | 执行 PEI 的 host-side 或 memory-side 硬件单元 | 高 |
| PEI Management Unit (PMU) | PEI 管理单元 | PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture | 管理 PEI atomicity、coherence 和 locality profiling | 高 |
| pfence | PIM memory fence | PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture | 等待之前所有 PEIs 完成的同步指令 | 高 |
| Physical Unclonable Function (PUF) | 物理不可克隆函数 | FracDRAM: Fractional Values in Off-the-Shelf DRAM | 利用制造差异生成设备唯一响应的安全 primitive | 高 |
| PiDRAM | Processing-in-DRAM 框架 | PiDRAM: A Holistic End-to-end FPGA-based Framework for Processing-in-DRAM | 用于真实 DRAM PuM 技术端到端集成和评估的 FPGA/RISC-V 平台 | 高 |
| PIM-enabled instruction (PEI) | PIM 使能指令 | PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture | 既可在 host 也可在 memory-side logic 上执行的 ISA extension | 高 |
| Pipeline | 流水线数据流接口 | DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures | 由多个 data-parallel stage 组成的 DaPPA 编程抽象 | 高 |
| Pipelined Serial Mode (PSM) | 流水串行模式 | RowClone: Fast and Energy-Efficient In-DRAM Bulk Data Copy and Initialization | 跨 bank 用 internal bus 逐 cache line 流水复制 | 高 |
| PRAC | Per Row Activation Counting | PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips | DDR5 标准化的逐行激活计数防护思路 | 高 |
| Processing interface | 处理接口 | SimplePIM: A Software Framework for Productive and Efficient Processing-in-Memory | 提供 map/reduce/zip iterators | 高 |
| Processing using Memory | 利用内存进行处理 | In-DRAM Bulk Bitwise Execution Engine | 复用内存器件固有结构/行为完成计算，而不是单纯靠外加逻辑 | 高 |
| PUD | Processing-using-DRAM | MIMDRAM: An End-to-End Processing-Using-DRAM System for High-Throughput, Energy-Efficient and Programmer-Transparent Multiple-Instruction Multiple-Data Processing | 利用 DRAM 模拟操作属性执行计算 | 高 |
| PuDHammer | PuD 诱发读扰动现象 | PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips | multiple-row activation-based PuD 操作造成或加剧 read disturbance | 高 |
| PuM Operations Controller (POC) | PuM 操作控制器 | PiDRAM: A Holistic End-to-end FPGA-based Framework for Processing-in-DRAM | 把 PuM operation 暴露为 memory-mapped interface 的硬件控制器 | 高 |
| pumolib | PiDRAM 用户库 | PiDRAM: A Holistic End-to-end FPGA-based Framework for Processing-in-DRAM | 应用通过该库调用 RowClone/D-RaNGe 等 PuM 操作 | 高 |
| Pushdown memory | 下推存储/栈式存储 | Cellular Logic-in-Memory Arrays | 类似 stack 的存储用途 | 中 |
| Rapid Inter-Subarray Copy (RISC) | 快速子阵列间复制 | Low-Cost Inter-Linked Subarrays (LISA): Enabling Fast Inter-Subarray Data Movement in DRAM | 基于 RBM 的跨 subarray copy 机制 | 高 |
| Redundant Binary Representation (RBR) | 冗余二进制表示 | Proteus: Enabling High-Performance Processing-Using-DRAM with Dynamic Bit-Precision, Adaptive Data Representation, and Flexible Arithmetic | 用多个 digit 组合表示同一值，限制 carry propagation | 高 |
| Reference voltage | 参考电压 | Functionally-Complete Boolean Logic in Real DRAM Chips: Experimental Characterization and Analysis | sense amplifier 比较另一端的基准电压，可被多行激活操控 | 高 |
| RFM | Refresh Management command | DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips | DDR5 中触发 refresh management/TRR 的命令 | 中 |
| Row Buffer Movement (RBM) | 行缓冲移动 | Low-Cost Inter-Linked Subarrays (LISA): Enabling Fast Inter-Subarray Data Movement in DRAM | 通过 LISA links 将一个 row buffer 的内容移动到相邻 row buffer | 高 |
| Row copy | 行复制 | ComputeDRAM: In-Memory Compute Using Off-the-Shelf DRAMs | 把一行数据复制到另一行的 in-memory primitive | 高 |
| Row segment | 行片段 | FIGARO: Improving System Performance via Fine-Grained In-DRAM Data Relocation and Caching | DRAM row 的小片段，可小到 cache block | 高 |
| RowClone | DRAM 内行复制机制 | In-DRAM Bulk Bitwise Execution Engine；Ambit: In-Memory Accelerator for Bulk Bitwise Operations Using Commodity DRAM Technology；RowClone: Fast and Energy-Efficient In-DRAM Bulk Data Copy and Initialization | 在 DRAM 内完成行复制/初始化，Ambit 用它移动操作数和结果 | 高 |
| RowClone-Copy (rcc) | DRAM 内复制操作 | PiDRAM: A Holistic End-to-end FPGA-based Framework for Processing-in-DRAM | 利用 RowClone 在 DRAM 内执行 copy | 高 |
| RowClone-FPM | RowClone 快速并行模式 | Fast Bulk Bitwise AND and OR in DRAM | 同 subarray 内通过背靠背 ACTIVATE 复制整行 | 高 |
| RowClone-Initialize (rci) | DRAM 内初始化操作 | PiDRAM: A Holistic End-to-end FPGA-based Framework for Processing-in-DRAM | 利用 RowClone 在 DRAM 内执行初始化 | 高 |
| RowClone-Zero-Insert (RowClone-ZI) | RowClone 零插入 | RowClone: Fast and Energy-Efficient In-DRAM Bulk Data Copy and Initialization | zeroing 后同时把 zero cache lines 插入 cache，避免后续低 MLP miss | 高 |
| RowHammer | 行锤攻击/行锤现象 | DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips | 频繁激活 aggressor row 导致邻近 victim row bit flip | 高 |
| SALP/BLP | subarray/bank-level parallelism | MIMDRAM: An End-to-End Processing-Using-DRAM System for High-Throughput, Energy-Efficient and Programmer-Transparent Multiple-Instruction Multiple-Data Processing | 利用多个 subarray/bank 并发执行，提高 PUD 吞吐 | 高 |
| Scratchpad memory | 软件管理暂存存储 | SimplePIM: A Software Framework for Productive and Efficient Processing-in-Memory | 每个 PIM core 的 64KB 本地存储 | 高 |
| Sector | 扇区/数据块 | A Logic-in-Memory Computer | logic-in-memory operations 的块级操作单位 | 高 |
| Sector ADD | 扇区加法 | A Logic-in-Memory Computer | 两个 sectors 对应 words 并行相加 | 高 |
| Sector miss | sector 未命中 | Sectored DRAM: A Practical Energy-Efficient and High-Performance Fine-Grained DRAM Architecture | 请求了未被取回的 cache block 部分，导致额外 memory access | 高 |
| Sector Predictor (SP) | sector 预测器 | Sectored DRAM: A Practical Energy-Efficient and High-Performance Fine-Grained DRAM Architecture | 预测 cache block 中未来会用到的 word/sector | 高 |
| Sectored Activation (SA) | 分 sector 激活 | Sectored DRAM: A Practical Energy-Efficient and High-Performance Fine-Grained DRAM Architecture | 只激活 DRAM row 中被请求的 mats/sectors | 高 |
| Sense amplifier | 感测放大器 | Fast Bulk Bitwise AND and OR in DRAM | DRAM 中把微小 bitline 电压偏移放大为 0/1 的电路 | 高 |
| SIMD utilization | SIMD 利用率 | MIMDRAM: An End-to-End Processing-Using-DRAM System for High-Throughput, Energy-Efficient and Programmer-Transparent Multiple-Instruction Multiple-Data Processing | 实际有用 lane 占可用 lane 的比例 | 高 |
| SIMDRAM | DRAM 内 bit-serial SIMD 框架 | SIMDRAM: An End-to-End Framework for Bit-Serial SIMD Computing in DRAM | 用 MAJ/NOT 和 vertical layout 支持通用 PuM operations | 高 |
| SimplePIM | PIM 高层软件框架 | SimplePIM: A Software Framework for Productive and Efficient Processing-in-Memory | 用高层 API 简化真实 PIM 编程 | 高 |
| SiMRA | simultaneous multiple-row activation | PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips | 同时激活多行，常用于 in-DRAM bitwise operations | 高 |
| Simultaneous many-row activation | 同时多行激活 | Simultaneous Many-Row Activation in Off-the-Shelf DRAM Chips: Experimental Characterization and Analysis | 一次或近似一次激活超过四条 DRAM rows | 高 |
| Single-cache-block restriction | 单 cache block 限制 | PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture | 限制单个 PIM operation 访问一个 LLC block | 高 |
| Sorting array | 排序阵列 | Cellular Logic-in-Memory Arrays | 能自动保持内部 words 有序的 CLIM array | 高 |
| Success rate | 成功率 | Functionally-Complete Boolean Logic in Real DRAM Chips: Experimental Characterization and Analysis | 某 cell 在多次试验中正确执行操作的比例 | 高 |
| TDM circuit switching | 时分复用电路交换 | NoM: Network-on-Memory for Inter-Bank Data Transfer in Highly-Banked Memories | 为 copy path 预留周期性 time slots，避免 packet-switched router 复杂度 | 高 |
| Timing-violating command sequence | 违反时序的命令序列 | ComputeDRAM: In-Memory Compute Using Off-the-Shelf DRAMs | 故意缩短 DRAM command intervals 以触发非标准 charge sharing 行为 | 高 |
| tmap | 透明数据映射 | Transparent Offloading and Mapping (TOM): Enabling Programmer-Transparent Near-Data Processing in GPU Systems | TOM 的 programmer-transparent mapping policy | 高 |
| Transparent Offloading and Mapping (TOM) | 透明卸载与映射 | Transparent Offloading and Mapping (TOM): Enabling Programmer-Transparent Near-Data Processing in GPU Systems | 自动选择 offload code 并映射数据的机制组合 | 高 |
| Transposition unit | 转置单元 | SIMDRAM: An End-to-End Framework for Bit-Serial SIMD Computing in DRAM | 负责 horizontal/vertical layout 转换的 memory-controller 结构 | 高 |
| Triple-row activation | 三行同时激活 | Fast Bulk Bitwise AND and OR in DRAM | 同时把三行 cell 接到 bitline，让 sense amplifier 输出多数值 | 高 |
| Triple-Row Activation (TRA) | 三行同时激活 | In-DRAM Bulk Bitwise Execution Engine；Ambit: In-Memory Accelerator for Bulk Bitwise Operations Using Commodity DRAM Technology | 同时激活三条 DRAM wordline，使 sense amplifier 得到 majority 结果 | 高 |
| TRR | Target Row Refresh | PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips | DRAM 内 RowHammer mitigation | 高 |
| UPMEM | 商用 PIM 系统 | DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures；SimplePIM: A Software Framework for Productive and Efficient Processing-in-Memory | 由带 DPU 的 DRAM DIMM 组成的 PIM 平台 | 高 |
| Variable Burst Length (VBL) | 可变突发长度 | Sectored DRAM: A Practical Energy-Efficient and High-Performance Fine-Grained DRAM Architecture | 根据 sector/word 需求动态改变 DRAM burst cycle 数 | 高 |
| Vault controller | vault 控制器 | NoM: Network-on-Memory for Inter-Bank Data Transfer in Highly-Banked Memories | HMC-like 3D memory 中控制一个 vault 内 banks 的控制器 | 高 |
| Vector reduction | 向量归约 | MIMDRAM: An End-to-End Processing-Using-DRAM System for High-Throughput, Energy-Efficient and Programmer-Transparent Multiple-Instruction Multiple-Data Processing | 把向量多元素聚合成标量，如 sum reduction | 高 |
| Vertical data layout | 垂直数据布局 | SIMDRAM: An End-to-End Framework for Bit-Serial SIMD Computing in DRAM | 一个元素的 bits 沿同一 bitline 分布，使 bitline 成为 SIMD lane | 高 |
| VILLA DRAM | 可变延迟 DRAM | Low-Cost Inter-Linked Subarrays (LISA): Enabling Fast Inter-Subarray Data Movement in DRAM | 用 fast/slow subarrays 管理 hot rows 的 heterogeneous DRAM | 高 |
| WRAM | DPU scratchpad memory | DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures | DPU 内 64KB scratchpad，需要显式搬移数据 | 高 |
| µProgram | 微程序 | Proteus: Enabling High-Performance Processing-Using-DRAM with Dynamic Bit-Precision, Adaptive Data Representation, and Flexible Arithmetic；SIMDRAM: An End-to-End Framework for Bit-Serial SIMD Computing in DRAM | 实现一个 PUD operation 的 DRAM command sequence | 高 |
