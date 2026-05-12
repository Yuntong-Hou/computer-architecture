# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Variable Burst Length (VBL) | 可变突发长度 | Page 2, Page 6 | 根据 sector/word 需求动态改变 DRAM burst cycle 数 | 是 |
| Sectored Activation (SA) | 分 sector 激活 | Page 2, Page 5-6 | 只激活 DRAM row 中被请求的 mats/sectors | 是 |
| Sector Predictor (SP) | sector 预测器 | Page 2, Page 7 | 预测 cache block 中未来会用到的 word/sector | 是 |
| LSQ Lookahead | Load/Store Queue 前瞻 | Page 2, Page 7 | 利用队列中 younger load/store 发现同一 cache block 的未来访问 | 是 |
| Sector miss | sector 未命中 | Page 10-11 | 请求了未被取回的 cache block 部分，导致额外 memory access | 是 |
| Fine-DRAM-Act | 细粒度 DRAM 激活 | Page 15 | 只激活部分 DRAM cells 而非完整 row | 是 |
