# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Tesseract | PIM 图处理加速器 | Page 1-2 | 基于 3D-stacked memory vault cores 的 programmable graph accelerator。 | 是 |
| Processing-in-memory (PIM) | 存内/近存计算 | Page 2-3 | 把 computation 移到 memory 内部或附近以利用内部带宽。 | 是 |
| Vault | HMC 垂直分区 | Page 4 | 含 DRAM banks、memory controller 和 Tesseract core 的 HMC slice。 | 是 |
| Remote function call | 远程函数调用 | Page 5 | 通过 message passing 在数据所在 vault 执行函数。 | 是 |
| Message-triggered prefetching | 消息触发预取 | Page 6 | 利用消息等待处理的 slack 预取目标数据。 | 是 |
