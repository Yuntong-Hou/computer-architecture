# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Network-on-Memory (NoM) | 内存上网络 | Page 1 | 连接 3D-stacked memory banks 的轻量级 inter-bank copy network | 是 |
| TDM circuit switching | 时分复用电路交换 | Page 2 | 为 copy path 预留周期性 time slots，避免 packet-switched router 复杂度 | 是 |
| Circuit Control Unit (CCU) | 电路控制单元 | Page 2 | 在 memory controller 中集中分配和配置 NoM paths | 是 |
| NoM-Light | 轻量 NoM | Page 3 | 复用既有 TSVs 以减少 full 3D mesh vertical link 成本的变体 | 是 |
| Vault controller | vault 控制器 | Page 1-3 | HMC-like 3D memory 中控制一个 vault 内 banks 的控制器 | 是 |
| Inter-bank copy | bank 间复制 | Page 1 | 源和目标位于不同 DRAM banks 的 direct data copy | 是 |
