# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| PIM-enabled instruction (PEI) | PIM 使能指令 | Page 2-3 | 既可在 host 也可在 memory-side logic 上执行的 ISA extension | 是 |
| PEI Computation Unit (PCU) | PEI 计算单元 | Page 5 | 执行 PEI 的 host-side 或 memory-side 硬件单元 | 是 |
| PEI Management Unit (PMU) | PEI 管理单元 | Page 5-7 | 管理 PEI atomicity、coherence 和 locality profiling | 是 |
| Single-cache-block restriction | 单 cache block 限制 | Page 3 | 限制单个 PIM operation 访问一个 LLC block | 是 |
| Locality-Aware execution | 局部性感知执行 | Page 9 | 根据数据局部性选择 host-side 或 memory-side 执行 PEI | 是 |
| pfence | PIM memory fence | Page 4 | 等待之前所有 PEIs 完成的同步指令 | 是 |
