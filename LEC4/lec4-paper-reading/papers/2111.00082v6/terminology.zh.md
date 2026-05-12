# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| PiDRAM | Processing-in-DRAM 框架 | Page 1-2 | 用于真实 DRAM PuM 技术端到端集成和评估的 FPGA/RISC-V 平台 | 是 |
| PuM Operations Controller (POC) | PuM 操作控制器 | Page 2, Page 5 | 把 PuM operation 暴露为 memory-mapped interface 的硬件控制器 | 是 |
| pumolib | PiDRAM 用户库 | Page 4-7 | 应用通过该库调用 RowClone/D-RaNGe 等 PuM 操作 | 是 |
| RowClone-Copy (rcc) | DRAM 内复制操作 | Page 8-13 | 利用 RowClone 在 DRAM 内执行 copy | 是 |
| RowClone-Initialize (rci) | DRAM 内初始化操作 | Page 8-13 | 利用 RowClone 在 DRAM 内执行初始化 | 是 |
| D-RaNGe | DRAM 真随机数生成技术 | Page 13-15 | 利用 reduced activation latency 下的随机失败生成 TRNG | 是 |
