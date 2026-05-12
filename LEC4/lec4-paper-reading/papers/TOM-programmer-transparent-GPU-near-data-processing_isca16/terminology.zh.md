# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Near-Data Processing (NDP) | 近数据处理 | Page 1 | 把计算放到数据附近，例如 3D-stacked memory logic layer | 是 |
| Transparent Offloading and Mapping (TOM) | 透明卸载与映射 | Page 1-2 | 自动选择 offload code 并映射数据的机制组合 | 是 |
| Memory stack | 内存堆叠 | Page 1 | 含 DRAM layers 与 logic layer 的 3D-stacked memory | 是 |
| Offload candidate | 卸载候选代码块 | Page 3 | 编译器认为 offload 可节省带宽的 instruction block | 是 |
| tmap | 透明数据映射 | Page 9 | TOM 的 programmer-transparent mapping policy | 是 |
| Offloading aggressiveness control | 卸载激进度控制 | Page 9 | 运行时决定是否真的 offload candidate blocks | 是 |
