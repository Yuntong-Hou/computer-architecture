# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| DaPPA | 数据并行 PIM 编程框架 | Page 1-2 | 用高层 pattern 和 Pipeline 自动生成 UPMEM 程序 | 是 |
| UPMEM | 商用 PIM 系统 | Page 1-3 | 由带 DPU 的 DRAM DIMM 组成的 PIM 平台 | 是 |
| DPU | DRAM Processing Unit | Page 1-3 | UPMEM PIM chip 内的小型多线程 in-order processor | 是 |
| MRAM | DPU 私有 DRAM bank | Page 1-3 | 每个 DPU 独占的 64MB 存储 | 是 |
| WRAM | DPU scratchpad memory | Page 1-3 | DPU 内 64KB scratchpad，需要显式搬移数据 | 是 |
| Pipeline | 流水线数据流接口 | Page 5-7 | 由多个 data-parallel stage 组成的 DaPPA 编程抽象 | 是 |
| Dynamic template-based compilation | 动态模板式编译 | Page 8-10 | 运行时填充 skeleton 并生成 UPMEM binary 的机制 | 是 |
