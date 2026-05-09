# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| SoftMC | Soft Memory Controller | Page 1-2 | 开源 FPGA-based 可编程 DRAM testing infrastructure。 | 是 |
| DDR command | DDR 命令 | Page 2-3 | ACTIVATE/READ/WRITE/PRECHARGE/REFRESH 等控制 DRAM 的标准接口命令。 | 是 |
| Timing parameter | 时序参数 | Page 3 | tRCD、tRAS、tRP 等命令间最小间隔约束。 | 是 |
| Retention test | 保持时间测试 | Page 7 | 写入数据、等待指定 refresh interval、读回比较错误。 | 是 |
| RIFFA | FPGA PCIe 通信框架 | Page 4-6 | SoftMC host 与 FPGA 间传输 instruction/data 的接口。 | 中 |
